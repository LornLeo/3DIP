from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
window = Tk()
window.geometry('1000x550')
window.title("Menu")
window.resizable(0, 0)
window.configure(bg="white")
left_frame = Frame(window,bg="white")
left_frame.grid(row=0,column=0,sticky=N)
middle_frame=Frame(window,bg="white")
middle_frame.grid(row=0, column=1,padx=(20,0),pady=(62,0),sticky=N)
menu_title = Label(left_frame,
                   text="Our Menu",
                   font=('Rockwell 21'),
                   bg='#fcc302',
                   fg="white",
                   width=9,
                   padx=30,
                   pady=2
                   )
menu_title.grid(row=0,column=0)

category_1=Button(left_frame,text="Category_1",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_1.grid(row=1,column=0,pady=(25,0))
category_2=Button(left_frame,text="Category_2",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_2.grid(row=2,column=0,pady=(13,0))
category_3=Button(left_frame,text="Category_3",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_3.grid(row=3,column=0,pady=(13,0))
category_4=Button(left_frame,text="Category_4",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_4.grid(row=4,column=0,pady=(13,0))
category_5=Button(left_frame,text="Category_5",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_5.grid(row=5,column=0,pady=(13,0))
category_6=Button(left_frame,text="Category_6",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_6.grid(row=6,column=0,pady=(13,0))
category_7=Button(left_frame,text="Category_7",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_7.grid(row=7,column=0,pady=(13,0))
category_8=Button(left_frame,text="Category_8",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5)
category_8.grid(row=8,column=0,pady=(13,0))



class FoodItem:
    def __init__(self,image,name,price,description):
        self.image=Image.open(image)
        self.name=name
        self.price=price
        self.description=description
    def create_widgets(self,row):
        self.food_item1=Frame(middle_frame,bg='white')
        self.food_item1.grid(row=row,column=0,pady=(0,51),padx=0)
        self.resized_image = self.image.resize((150, 100),Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        self.item1_image=Label(self.food_item1,image=self.tk_image,bg="white",height=100,width=150)
        self.item1_image.grid(row=0,column=0,rowspan=4,sticky=NW)
        self.item1_name=Label(self.food_item1,text=self.name,bg="white",font=("Arial", 15, "bold"),width=10,anchor=W)
        self.item1_name.grid(row=0,column=1,sticky=NW,padx=(0,100))
        self.item1_description=Label(self.food_item1,text=self.description,justify="left",anchor=W,bg="white",wraplength=370,font=("Arial", 9),width=50)
        self.item1_description.grid(row=1,column=1,columnspan=2,padx=0,sticky=NW)
        self.item1_price=Label(self.food_item1,text=self.price,justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
        self.item1_price.grid(row=2,column=2,sticky=NE,padx=(0,22))
        self.item1_order=Button(self.food_item1,text="ORDER",fg="white",bg="red",width=10,font=("Arial", 11,"bold"))
        self.item1_order.grid(row=2,column=1,sticky=W)
food_item1 = FoodItem(
    "asparagus-2169305_1280.jpg",
    "Steak",
    "$15.99",
    "Experience culinary perfection with our prime steak. Tender, flavorful, and cooked to perfection.",
)
food_item1.create_widgets(0)

food_item2 = FoodItem(
    "pancake-1984716_1280.jpg",
    "Burger",
    "$9.99",
    "Indulge in our mouth-watering burger made with premium ingredients. Juicy, flavorful, and satisfying.",
)
food_item2.create_widgets(1)

food_item3 = FoodItem(
    "salmon-518032_1280.jpg",
    "Pizza",
    "$12.99",
    "Savor the taste of our delectable pizza topped with the finest ingredients. Perfectly baked for your enjoyment.",
)
food_item3.create_widgets(2)

window.mainloop()