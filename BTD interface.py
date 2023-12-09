from tkinter import *
from tkinter import Frame
from keras.models import load_model
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from openpyxl import load_workbook
from keras.preprocessing.image import ImageDataGenerator


root = Tk()
root.geometry("900x700")
root.title("Brain Tumor Detection")
root.geometry('900x700')
root.resizable(False, False)

def main():
    # =====================Create Frame======================
    mainroot = Frame(root)
    mainroot.place(x=0, y=0, width=900, height=700)
    # ===========================header==============================================================
    heading = Label(mainroot, text="BRAIN  TUMOR  DETECTION", bg="#00FFFF",fg="#006837", bd=20, relief=RIDGE, font=("Times new roman", 35, " italic bold"),
                 height=2)
    heading.pack(side='top', fill=X)
    # =========================Frame=================================================================
    frame = Frame(root)
    frame.place(x=0, y=145, width=900, height=565)
    image = Image.open("images/1.jpg").resize((897, 552))
    render = ImageTk.PhotoImage(image)
    img = Label(frame, image=render)
    img.image = render
    img.place(x=-1, y=-1)

    # ========================Button=================================================================
    sb = Button(frame, text="Single MRI Testing", bg="#00FFFF", width=23, height=2, font=("Helvetica 15 "), command=single)
    sb.place(x=70, y=110)

    mub = Button(frame, text="Model Testing", bg="#00FFFF", width=23, height=2, font=("Helvetica 15 "), command=model)
    mub.place(x=70, y=390)

    mb = Button(frame, text="Multiple MRI Testing", bg="#00FFFF", width=23, height=2, font=("Helvetica 15 "),
                command=multiple)
    mb.place(x=595, y=110)

    eb = Button(frame, text="Exit", bg="#00FFFF", width=23, height=2, font=("Helvetica 15 "), command=exit)
    eb.place(x=595, y=390)
def single():
    # =====================Create Frame======================
    singleroot = Frame(root)
    singleroot.place(x=0, y=0, width=900, height=700)
    image = Image.open("images/1.jpg").resize((898, 695))
    render = ImageTk.PhotoImage(image)
    img = Label(singleroot, image=render)
    img.image = render
    img.place(x=-1, y=0)
    # ===================load the model===========================================
    best_model = load_model(filepath='bestmodel.h5')

    # ====================Header of the window================================
    title = Label(singleroot, text="Single MRI Testing", bg="#00FFFF", font=("times new roman", 50, "bold"), bd=20, relief=RIDGE)
    title.pack(side=TOP, fill=X)
    # ====================function============================================
    def upload_file():
        global img, filename
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img=Image.open(filename)
        img_resized=img.resize((250,250)) # new width & heightmuhammad
        img=ImageTk.PhotoImage(img_resized)
        b2 = Button(singleroot, image=img) # using Button
        b2.place(x=500, y=170)
    def result():
        global pred
        ab = StringVar(singleroot)

        ab.set(filename)
        path = ab.get()

        img = load_img(path, target_size=(224, 224))

        input_arr = img_to_array(img) / 225

        input_arr = np.expand_dims(input_arr, axis=0)

        pred = (best_model.predict(input_arr) > 0.5).astype("int32")

        pentery.delete(0, "end")
        if pred == 1:
            pentery.insert(0, "Brain Tumor is Detected")
        else:
            pentery.insert(0, "Brain Tumor is not Detected")

        a = nentry.get()
        b = aentry.get()
        c = gentry.get()
        d = pentery.get()
        e = a, b, c, d
        excelfile = "Data of patient.xlsx"

        wb = load_workbook(excelfile)
        ws = wb.worksheets[0]
        ws.append(e)
        wb.save(excelfile)
    def back():
       main()

    # =================Frame================================================
    frame= Frame(singleroot,bg="#00FFFF", bd=12, relief=RIDGE)
    frame.place(x=0, y=520, width=900, height=180)
    image2= Image.open("images/3.jpg").resize((870, 150))
    render = ImageTk.PhotoImage(image2)
    img2 = Label(frame, image=render)
    img2.image = render
    img2.place(x=-1, y=0)


    # =================button================================================
    sb = Button(singleroot, text='Select image !', bg="#00FFFF", width=23, bd='5',
                   command= lambda:upload_file())
    sb.place(x=550, y=130)


    rb = Button(frame, text="Result", bg="#00FFFF", width=23, bd='5', command=result)
    rb.place(x=60, y=60)

    eb = Button(frame, text="Exit", bg="#00FFFF", width=23, bd='5', command=back)
    eb.place(x=600, y=60)

    # ===============Label===================================================
    nlabel = Label(singleroot, text="Name:", bg="#00FFFF")
    nlabel.place(x=50, y=165, height=25, width=50)

    alabel = Label(singleroot, text="Age:", bg="#00FFFF")
    alabel.place(x=50, y=265, height=25, width=50)

    glabel = Label(singleroot, text="Gender:", bg="#00FFFF")
    glabel.place(x=50, y=365, height=25, width=50)

    # =================Entry=================================================
    pentery= Entry(frame)
    pentery.place(x=260, y=70, width=300)

    nentry= Entry(singleroot)
    nentry.place(x=105, y=170, width=300)

    aentry= Entry(singleroot)
    aentry.place(x=105, y=270, width=300)

    gentry= Entry(singleroot)
    gentry.place(x=105, y=370, width=300)
def multiple():
    # =====================Create Frame======================
    multipleroot = Frame(root)
    multipleroot.place(x=0, y=0, width=900, height=700)
    image = Image.open("images/1.jpg").resize((898, 695))
    render = ImageTk.PhotoImage(image)
    img = Label(multipleroot, image=render)
    img.image = render
    img.place(x=-1, y=0)
    # ================Header===========================
    title = Label(multipleroot, text="Multiple MRI Testing", bg="#00FFFF", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"))
    title.pack(side=TOP, fill=X)

    # ================load model=======================
    best_model = load_model(filepath="bestmodel.h5")

    # ================function=========================
    def upload_file():
        global filename
        f_types = [('Jpg Files', '*.jpg'),
                   ('PNG Files', '*.png')]  # type of files to select
        filename = filedialog.askopenfilename(multiple=True, filetypes=f_types)
        col = 170
        row = 50
        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((100, 100))  # new width & height
            img = ImageTk.PhotoImage(img)
            e1 = Label(multipleroot)
            e1.place(x=row, y=col)
            e1.image = img
            e1['image'] = img  # garbage collection
            if (row == 750):  # start new line after third column
                col = col + 100  # start wtih next row
                row = 50  # start with first column
            else:  # within the same row
                row = row + 100  # increase to next column
    def result():
        global pred, c
        no = 1
        paths = filename
        for path in paths:
            img = load_img(path, target_size=(224, 224))

            input_arr = img_to_array(img) / 225

            input_arr = np.expand_dims(input_arr, axis=0)

            pred = (best_model.predict(input_arr) > 0.5).astype("int32")

            if (pred == 1):
                rentry.insert(50, str(no) + "Brain Tumor is Detected")
            else:
                rentry.insert(50, str(no) + "Brain Tumor is not Detected")
            no = no + 1
    def exit():
        main()

    # ================frame==========================
    frame = Frame(multipleroot, bg="#00FFFF", bd=12, relief=RIDGE)
    frame.place(x=0, y=520, width=900, height=180)
    image2 = Image.open("images/3.jpg").resize((870, 150))
    render = ImageTk.PhotoImage(image2)
    img2 = Label(frame, image=render)
    img2.image = render
    img2.place(x=-1, y=0)

    # ================button==========================
    ubtn = Button(multipleroot, text="Select images", bg="#00FFFF", width=23, bd=5, command=lambda: upload_file())
    ubtn.place(x=350, y=130)

    rbtn = Button(frame, text="Result", bg="#00FFFF", width=23, bd=5, command=result)
    rbtn.place(x=60, y=50)

    ebtn = Button(frame, text="Exit", bg="#00FFFF", width=23, bd=5, command=exit)
    ebtn.place(x=600, y=50)

    # =============Entry==============================
    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.place(x=560, y=20, height=130)
    rentry = Listbox(frame, yscrollcommand=scrollbar.set)
    rentry.place(x=260, y=20, width=300, height=130)
def model():
    # =====================Create Frame======================
    modelroot = Frame(root)
    modelroot.place(x=0, y=0, width=900, height=700)
    # ===================load the model===========================================
    best_model = load_model(filepath='bestmodel.h5')

    # =======================header==================================================================
    header = Label(modelroot, text="Model Testing", bg="#00FFFF", bd=12, relief=RIDGE, font=("times new roman", 65, "bold"))
    header.pack(side=TOP, fill=X)
    # =======================Frame================================================
    fp = Frame(modelroot, bg="#00FFFF", bd=12, relief=RIDGE)
    fp.place(x=0, y=125, width=900, height=150)
    image2 = Image.open("images/3.jpg").resize((872, 120))
    render = ImageTk.PhotoImage(image2)
    img2 = Label(fp, image=render)
    img2.image = render
    img2.place(x=-1, y=0)

    fr = Frame(modelroot, bg="#00FFFF", bd=12, relief=RIDGE)
    fr.place(x=0, y=275, width=900, height=425)
    image = Image.open("images/1.jpg").resize((870, 398))
    render = ImageTk.PhotoImage(image)
    img = Label(fr, image=render)
    img.image = render
    img.place(x=-1, y=0)

    # ======================path Entry================================================
    p = Entry(fp)
    p.place(x=400, y=55, width=200, height=30)

    # ======================Function==================================================
    def value():
        c = p.get()
        image_data = ImageDataGenerator(rescale=1 / 225)
        image = image_data.flow_from_directory(directory=c, target_size=(224, 224), batch_size=32, class_mode='binary')
        loss, accuracy, precision, recall, true_positives, false_positives, specificity_at_sensitivity_6, specificity_at_sensitivity_7 = best_model.evaluate(
            image)
        a.delete(0, "end")
        a.insert(0, str(accuracy))
        l.delete(0, "end")
        l.insert(0, str(loss))
        pe.delete(0, "end")
        pe.insert(0, str(precision))
    def exit():
        main()

    # =====================Button=====================================================
    btn = Button(fp, text="Result", bg="#00FFFF", width=23, bd=5, command=value)
    btn.place(x=670, y=80)
    btnm = Button(fr, text="Exit", bg="#00FFFF", width=23, bd=5, command=exit)
    btnm.place(x=600, y=300)

    # ===================Label========================================================================
    plab = Label(fp, text="Path", bg="#00FFFF", font=("times new roman", 20, "bold"))
    plab.place(x=150, y=50)

    talab = Label(fr, text="Test Accuracy", bg="#00FFFF", font=("times new roman", 20, "italic"))
    talab.place(x=150, y=80)
    tllab = Label(fr, text="Test Loss", bg="#00FFFF", font=("times new roman", 20, "italic"))
    tllab.place(x=150, y=150)
    tplab = Label(fr, text="Test Precision", bg="#00FFFF", font=("times new roman", 20, "italic"))
    tplab.place(x=150, y=220)

    # ====================Result Entry===================================================
    a = Entry(fr)
    a.place(x=400, y=85, width=200, height=30)
    l = Entry(fr)
    l.place(x=400, y=155, width=200, height=30)
    pe = Entry(fr)
    pe.place(x=400, y=225, width=200, height=30)

main()
root.mainloop()