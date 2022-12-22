from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
from gtts import gTTS
import pygame
from pygame import mixer
root = Tk()
root.geometry("1000x1000")  # Size of the window
root.title('player')
pygame.mixer.init()  # initialise the pygame
audio = "speech.mp3"
language = "en"
global img1
global bck
#global bck1
#global img2

def imageextraction():
    lab1.destroy()
    b1.destroy()
    def tab1():
        global img1
        global bck
        img1 = Image.open(r"C:\Users\metla\Downloads\bg1.jpg")
        resize_im = img1.resize((2000, 1000))
        bck = ImageTk.PhotoImage(resize_im)
        lab = Label(root, image=bck)
        lab.place(x=0, y=0)

        def tab2():
            title.destroy()
            l1.destroy()
            b1.destroy()
            lab.destroy()
            l2 = Label(root, text="Extracting text from Image", font=("times new roman", 25))
            l2.pack(side='top')

            def back():
                l2.destroy()
                b4.destroy()
                tab1()

            b4 = Button(root, text='Back', font=("times new roman", 25), command=back)
            b4.pack(side=BOTTOM)

        title = Label(root, text="VISUAL PERCEPTION",
                      bd=10, relief=GROOVE, font=("times new roman", 50, "bold"), bg="sky blue", fg="navy blue")
        title.pack(side=TOP, fill=X)
        my_font1 = ('times', 18, 'bold')
        l1 = Label(root, text='Upload Image', bg="sky blue", width=30, font=my_font1)
        # l1.grid(row=1,column=1)
        l1.pack(side=TOP, fill=X)
        b1 = Button(root, text='UPLOAD FILE', font=("times new roman", 15), width=20, bg="light pink", command=lambda: upload_file())
        # b1.grid(row=2,column=1)
        b1.pack(side=TOP)

        def upload_file():
            global img

            f_types = [('Jpg Files', '*.jpg'), ('png Files', '*.png'), ('jpeg Files', '*.jpeg'),
                       ('webp files', '*.webp')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            img_resized = img.resize((600, 500))  # new width & height
            img = ImageTk.PhotoImage(img_resized)

            def imgext():
                lab.destroy()
                b2.destroy()
                b1.destroy()
                l1.destroy()
                frame = Frame(root, width=1000, height=1500)
                frame.pack()
                frame.place(anchor='e', relx=0.5, rely=0.5)
                global img1
                img1 = Image.open(filename)
                resize_image = img1.resize((400, 500))
                photo = ImageTk.PhotoImage(resize_image)

                # Create a Label Widget to display the text or Image
                label = Label(frame, image=photo, anchor="center", font=('Times new roman', 5, 'bold'))
                label.pack()
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                text = pytesseract.image_to_string(filename)
                if(text):
                    w = Label(root, anchor='center', bg="light green", bd=10, text=text,
                              font=('Times new roman', 20, "bold"))
                    w.pack()
                else:
                    text="NO TEXT TO PRINT"
                    w = Label(root, anchor='center', bg="light green", bd=10, text=text,
                              font=('Times new roman', 20, "bold"))
                    w.pack()
                # ans = text
                sp = gTTS(text=text, lang=language, slow=False)
                sp.save(audio)


                def play():
                    pygame.mixer.music.load(audio)
                    pygame.mixer.music.play(loops=0)

                play_button = Button(root, text="PLAY", font=("Helvetica", 15), command=play, bg= "gold")
                play_button.pack(padx=0, side=LEFT,expand=True)

                def pause_music():
                    mixer.music.pause()

                pausebtn = Button(root, text="PAUSE", font=("Helvetica", 15), command=pause_music, bg="gold")
                pausebtn.pack(padx=0, side=LEFT,expand=True)

                def unpause_music():
                    mixer.music.unpause()

                unp = Button(root, text="RESUME", font=("Helvetica", 15), command=unpause_music, bg= "gold")
                unp.pack(padx=0, side=LEFT,expand=True)

                def stop_music():
                    mixer.music.stop()

                stop = Button(root, text="STOP", font=("Helvetica", 15), command=stop_music, bg="gold")
                stop.pack(padx=0, side=LEFT,expand=True)

            b2 = Button(root, image=img, command=imgext)  # using Button
            b2.pack()
    tab1()


img2=Image.open(r"C:\Users\metla\Downloads\WhatsApp Image.jpg")
img = img2.resize((500, 500))
bck1 = ImageTk.PhotoImage(img2)
lab1 = Label(root, image=bck1)
lab1.place(x=0,y=0)
b1=Button(root,text='NEXT',bg='black',fg='yellow',font=('Times new roman',20),command=imageextraction)
b1.pack(side=BOTTOM)


root.mainloop()