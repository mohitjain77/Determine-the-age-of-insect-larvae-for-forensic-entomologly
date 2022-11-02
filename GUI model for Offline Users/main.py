from tkinter import *
import tkinter as gui
import agePred as a
from PIL import ImageTk, Image
from io import BytesIO
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import PIL.Image



def submit_value():
    age_in_hours = a.LarvaeAge().age_prediction(float(length.get()), float(weight.get()), float(stage.get()), float(temperature.get()))
    age_in_days = round((age_in_hours)/24,2)
    L1 =  Label(root, text=f'The Predicted Age of Larvae is : {age_in_hours} hours({age_in_days} days approx.)')
    L1.place(x= 200, y= 430)
all_photoimages = []

def click_for_tree_view():
    global img
    top = Toplevel()
    top.title("Tree View")
    top.geometry("1600x1000")
    top.maxsize(1600, 1000)
    top.minsize(1600, 1000)
    a.LarvaeAge().tree_view(float(length.get()), float(weight.get()), float(stage.get()), float(temperature.get()))
    svgfile = svg2rlg(f"uploaded_images/tree_view{float(length.get())}-{float(weight.get())}-{float(stage.get())}-{float(temperature.get())}.svg")
    bytespng = BytesIO()
    renderPM.drawToFile(svgfile, bytespng,fmt="PNG")
    pht =  PIL.Image.open(bytespng)
    pht = pht.resize((1600, 1000), PIL.Image.ANTIALIAS)
    img = ImageTk.PhotoImage(pht)
    my_label = Label(top, image= img).pack()

def click_for_path_view():
    global img
    top = Toplevel()
    top.title("Tree View")
    top.geometry("800x300")
    top.maxsize(1600, 1000)
    top.minsize(800, 300)
    a.LarvaeAge().path_view(float(length.get()), float(weight.get()), float(stage.get()), float(temperature.get()))
    svgfile = svg2rlg(f"uploaded_images/path_view{float(length.get())}-{float(weight.get())}-{float(stage.get())}-{float(temperature.get())}.svg")
    bytespng = BytesIO()
    renderPM.drawToFile(svgfile, bytespng,fmt="PNG")
    pht =  Image.open(bytespng)
    pht = pht.resize((800, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(pht)
    my_label = Label(top, image= img).pack()
    



root = gui.Tk()
root.title("MSc Project")
root.geometry("800x500")
root.maxsize(800, 500)
root.minsize(800, 500)
root.resizable(False, False)
root.configure(bg='white')
my_logo = Image.open('/Users/mohitjain/Desktop/Msc Project on Machine Learning/GUI model for Offline Users/logo.png')
resized =  my_logo.resize((120, 100), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)

my_label = Label(root,image=new_logo, bd=0, highlightthickness = 0)
my_label.pack(pady=10)

label_1 = Label(root, text="Select the Temperature: ",width=18, height= 1,font=("bold", 12))
label_1.place(x=230,y=130)
temperature = StringVar(root)
temperature.set(25)
temp = OptionMenu(root, temperature, 25, 20, 15)
temp.pack()
temp.place(x= 430, y=130, width= 100)

label_2 = Label(root, text="Select the LarvelStage: ",width=18, height= 1,font=("bold", 12))
label_2.place(x=230,y=180)
stage = StringVar(root)
stage.set(1)
larv = OptionMenu(root, stage, 1, 2, 3, 4)
larv.pack()
larv.place(x= 430, y=180, width=100)
 
label_3 = Label(root, text="Enter the Weight: ", width=18, height=1, font=("bold", 12))
label_3.place(x= 230, y= 230)
weight = StringVar(root)
wt =  Entry(root, textvariable=weight, width = 9, font='none 12 bold')
wt.place(x = 430, y= 230, width= 100)

label_4 = Label(root, text="Enter the Length: ", width=18, height=1, font=("bold", 12))
label_4.place(x= 230, y= 280)
length = StringVar(root)
ln =  Entry(root, textvariable=length, width = 9, font='none 12 bold')
ln.place(x = 430, y= 280, width= 100)

b1 = Button(root, text="Submit", font=40, command=submit_value)
b1.place(x= 350, y= 330, width= 100, height=40)

b2 = Button(root, text="Tree View", font=40, command=click_for_tree_view)
b2.place(x= 250, y= 380, width= 100, height=40)

b2 = Button(root, text="Path View", font=40, command=click_for_path_view)
b2.place(x= 450, y= 380, width= 100, height=40)

# output_label =  Label(root, text="The predicted age of an Insect Larvae is : ")
# output_label.place(x = 600, y= 380)

root.mainloop()
