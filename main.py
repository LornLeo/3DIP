from tkinter import *
from PIL import ImageTk, Image
import os
import math
window = Tk()
window.geometry('1000x550')
window.title("Menu")
window.resizable(0, 0)
window.configure(bg="white")
left_frame = Frame(window,bg="white")
left_frame.grid(row=0,column=0,rowspan=3,sticky=N)
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
disable_list=[None]
Menu_index=[{'Image_path': 'salmon-518032_1280.jpg', 'Name': 'Pizza', 'Price': '$12.99 ', 'Description': 'Savor the taste of our delectable pizza topped with the finest ingredients. Perfectly baked for your enjoyment.'},{'Image_path': 'pancake-1984716_1280.jpg', 'Name': 'Burger', 'Price': '$9.99 ', 'Description': 'Indulge in our mouth-watering burger made with premium ingredients. Juicy, flavorful, and satisfying.'},{'Image_path': 'asparagus-2169305_1280.jpg', 'Name': 'Steak', 'Price': '$153.99 ', 'Description': 'Experience culinary perfection with our prime steak. Tender, flavorful, and cooked to perfection.'},{'Image_path': 'salmon-518032_1280.jpg',
    'Name': 'Sushi',
    'Price': '$14.99',
    'Description': 'Made with the finest seafood and expertly crafted for an unforgettable dinner'}]
category_1_dict=[{'Image_path': 'pancake-1984716_1280.jpg', 'Name': 'Pizza', 'Price': '$11.99 ', 'Description': 'Savor the taste of our delectable pizza topped with the finest ingredients. Perfectly baked for your enjoyment.'},{'Image_path': 'salmon-518032_1280.jpg', 'Name': 'Bu2rger', 'Price': '$9.99 ', 'Description': 'Indulge in our mouth-watering burger made with premium ingredients. Juicy, flavorful, and satisfying.'},{'Image_path': 'asparagus-2169305_1280.jpg', 'Name': 'Steak', 'Price': '$15.99 ', 'Description': 'Experience culinary perfection with our prime steak. Tender, flavorful, and cooked to perfection.'},{'Image_path': 'pancake-1984716_1280.jpg',
    'Name': 'Pasta',
    'Price': '$11.99',
    'Description': 'Delight your taste buds with our mouthwatering pasta, prepared with a variety of fresh ingredients and flavorful sauces.'}]
category_2_dict=[ {'Image_path': 'pancake-1984716_1280.jpg', 'Name': 'Pizza', 'Price': '$13.99 ', 'Description': 'Savor the taste of our delectable pizza topped with the finest ingredients. Perfectly baked for your enjoyment.'}]


category_3_dict = [
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 3 Item 1',
        'Price': '$12.99',
        'Description': 'Description for Category 3 Item 1'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 3 Item 2',
        'Price': '$11.99',
        'Description': 'Description for Category 3 Item 2'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 3 Item 3',
        'Price': '$10.99',
        'Description': 'Description for Category 3 Item 3'
    }
]

category_4_dict = [
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 4 Item 1',
        'Price': '$14.99',
        'Description': 'Description for Category 4 Item 1'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 4 Item 2',
        'Price': '$13.99',
        'Description': 'Description for Category 4 Item 2'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 4 Item 3',
        'Price': '$12.99',
        'Description': 'Description for Category 4 Item 3'
    },    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 3 Item 3',
        'Price': '$10.99',
        'Description': 'Description for Category 3 Item 3'
    }]

category_5_dict = [
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 1',
        'Price': '$16.99',
        'Description': 'Description for Category 5 Item 1'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 2',
        'Price': '$15.99',
        'Description': 'Description for Category 5 Item 2'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 3',
        'Price': '$14.99',
        'Description': 'Description for Category 5 Item 3'
    }
]

category_6_dict = [
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 6 Item 1',
        'Price': '$18.99',
        'Description': 'Description for Category 6 Item 1'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 6 Item 2',
        'Price': '$17.99',
        'Description': 'Description for Category 6 Item 2'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 6 Item 3',
        'Price': '$16.99',
        'Description': 'Description for Category 6 Item 3'
    }]
category_7_dict = [
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 1',
        'Price': '$16.99',
        'Description': 'Description for Category 5 Item 1'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 2',
        'Price': '$15.99',
        'Description': 'Description for Category 5 Item 2'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 3',
        'Price': '$14.99',
        'Description': 'Description for Category 5 Item 3'
    }]
category_8_dict = [
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 1',
        'Price': '$16.99',
        'Description': 'Description for Category 5 Item 1'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 2',
        'Price': '$15.99',
        'Description': 'Description for Category 5 Item 2'
    },
    {
        'Image_path': 'salmon-518032_1280.jpg',
        'Name': 'Category 5 Item 3',
        'Price': '$14.99',
        'Description': 'Description for Category 5 Item 3'
    }]
Index_list=[category_1_dict,category_2_dict,category_3_dict,category_4_dict,category_5_dict,category_6_dict,category_7_dict,category_8_dict]
Index_name=["Category_1","Category_2","Category_3","Category_4","Category_5","Category_6","Category_7","Category_8"]

def selected_button(button_name,button_press):
    global Menu_index
    Menu_index=Index_list[button_press]
    global total_page_number
    total_page_number=math.ceil(len(Menu_index)/3)
    global page_number
    page_number=1
    page_displayed.configure(text="1"+"/"+str(total_page_number))

    if disable_list[0]!=None:
        disable_list[0].configure(state="normal")
        disable_list[0].configure(bg="white")
    disable_list[0]=None    
    disable_list[0]=button_name
    
    food_item_1 = FoodItem(Menu_index[0]['Image_path'], Menu_index[0]['Name'], Menu_index[0]['Price'], Menu_index[0]['Description'],remove_frame=False)
    food_item_1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)
    if len(Index_list[button_press]) > 1:
        food_item2 = FoodItem(Menu_index[1]['Image_path'], Menu_index[1]['Name'], Menu_index[1]['Price'], Menu_index[1]['Description'],remove_frame=False)
        food_item2.grid(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    else:
        food_item2 = FoodItem('', '','', '',remove_frame=True)
        
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    if len(Index_list[button_press]) > 2:
        food_item3 = FoodItem(Menu_index[2]['Image_path'], Menu_index[2]['Name'], Menu_index[2]['Price'], Menu_index[2]['Description'],remove_frame=False)
        food_item3.grid(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
    else:
        food_item3 = FoodItem('', '','', '',remove_frame=True)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
    button_name.configure(state="disabled")
    button_name.configure(bg="yellow")
def add_order():
    print(item1_price.cget("text"))
category_1=Button(left_frame,text="Category_1",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5,command=lambda:selected_button(category_1,0))
category_1.grid(row=1,column=0,pady=(25,0))
category_2=Button(left_frame,text="Category_2",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5, command=lambda:selected_button(category_2,1))
category_2.grid(row=2,column=0,pady=(13,0))
category_3=Button(left_frame,text="Category_3",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5,command=lambda:selected_button(category_3,2))
category_3.grid(row=3,column=0,pady=(13,0))
category_4=Button(left_frame,text="Category_4",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5,command=lambda:selected_button(category_4,3))
category_4.grid(row=4,column=0,pady=(13,0))
category_5=Button(left_frame,text="Category_5",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5,command=lambda:selected_button(category_5,4))
category_5.grid(row=5,column=0,pady=(13,0))
category_6=Button(left_frame,text="Category_6",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5,command=lambda:selected_button(category_6,5))
category_6.grid(row=6,column=0,pady=(13,0))
category_7=Button(left_frame,text="Category_7",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5,command=lambda:selected_button(category_7,6))
category_7.grid(row=7,column=0,pady=(13,0))
category_8=Button(left_frame,text="Category_8",font=('serif 15'),bg="white",width=18,activebackground="#FBFF3C",activeforeground="black",padx=5,command=lambda:selected_button(category_8,7))
category_8.grid(row=8,column=0,pady=(13,0))


food_item1=Frame(middle_frame,bg='white')           
food_item1.grid(row=0,column=0,pady=(0,51),padx=0)

food_image1=Image.open(Menu_index[0]["Image_path"])
resized_image = food_image1.resize((150, 100),Image.ANTIALIAS)
food_image1 = ImageTk.PhotoImage(resized_image)
item1_image=Label(food_item1,image='',bg="white",height=100,width=150)
item1_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item1_name=Label(food_item1,text=Menu_index[0]['Name'],bg="white",font=("Arial", 15, "bold"),width=15,anchor=W)
item1_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item1_description=Label(food_item1,text=Menu_index[0]['Description'],justify="left",anchor=W,bg="white",wraplength=370,font=("Arial", 9),width=50)
item1_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item1_price=Label(food_item1,text=Menu_index[0]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item1_price.grid(row=2,column=2,sticky=W,padx=15)
item1_quantity=Spinbox(food_item1,from_=1,to=10,width=5,bg="white",state="readonly")
item1_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item1_order=Button(food_item1,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"),command=add_order)
item1_order.grid(row=2,column=3,sticky=W) 

food_item2=Frame(middle_frame,bg='white')           
food_item2.grid(row=1,column=0,pady=(0,51),padx=0)

food_image2=Image.open(Menu_index[0]["Image_path"])
resized_image2 = food_image2.resize((150, 100),Image.ANTIALIAS)
food_image2 = ImageTk.PhotoImage(resized_image)
item2_image=Label(food_item2,image=food_image2,bg="white",height=100,width=150)
item2_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item2_name=Label(food_item2,text=Menu_index[0]['Name'],bg="white",font=("Arial", 15, "bold"),width=15,anchor=W)
item2_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item2_description=Label(food_item2,text=Menu_index[0]['Description'],justify="left",anchor=W,bg="white",wraplength=370,font=("Arial", 9),width=50)
item2_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item2_price=Label(food_item2,text=Menu_index[0]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item2_price.grid(row=2,column=2,sticky=W,padx=15)
item2_quantity=Spinbox(food_item2,from_=1,to=10,width=5,bg="white",state="readonly")
item2_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item2_order=Button(food_item2,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"))
item2_order.grid(row=2,column=3,sticky=W)

food_item3=Frame(middle_frame,bg='white')           
food_item3.grid(row=2,column=0,pady=(0,0),padx=0)

food_image3=Image.open(Menu_index[0]["Image_path"])
resized_image3 = food_image3.resize((150, 100),Image.ANTIALIAS)
food_image3 = ImageTk.PhotoImage(resized_image3)
item3_image=Label(food_item3,image=food_image3,bg="white",height=100,width=150)
item3_image.grid(row=0,column=0,rowspan=4,sticky=NW)
item3_name=Label(food_item3,text=Menu_index[0]['Name'],bg="white",font=("Arial", 15, "bold"),width=15,anchor=W)
item3_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
item3_description=Label(food_item3,text=Menu_index[0]['Description'],justify="left",anchor=W,bg="white",wraplength=370,font=("Arial", 9),width=50)
item3_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
item3_price=Label(food_item3,text=Menu_index[0]['Price'],justify="left",fg="red",wraplength=350,font=("Arial", 12),pady=7,width=10)
item3_price.grid(row=2,column=2,sticky=W,padx=15)
item3_quantity=Spinbox(food_item3,from_=1,to=10,width=5,bg="white",state="readonly")
item3_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
item3_order=Button(food_item3,text="ORDER",fg="white",bg="red",width=9,font=("Arial", 11,"bold"))
item3_order.grid(row=2,column=3,sticky=W)




class FoodItem:
    def __init__(self,image_path,name,price,description,remove_frame=False):
        self.image_path=image_path
        self.name=name
        self.price=price
        self.description=description
        self.remove_frame=remove_frame
    def grid(self, item_image, item_name, item_price, item_description,item_order,item_quantity):
            item_image.grid(row=0,column=0,rowspan=4,sticky=NW)
            item_name.grid(row=0,column=1,columnspan=3,sticky=NW,padx=(0,100))
            item_description.grid(row=1,column=1,columnspan=3,padx=0,sticky=NW)
            item_price.grid(row=2,column=2,sticky=W,padx=15)
            item_quantity.grid(row=2,column=1,sticky=W+E+N+S,padx=3)
            item_order.grid(row=2,column=3,sticky=W) 

    def configure(self, item_image, item_name, item_price, item_description,item_order,item_quantity):
        if self.remove_frame:
            item_image.grid_remove()
            item_name.grid_remove()
            item_price.grid_remove()
            item_description.grid_remove()
            item_order.grid_remove()
            item_quantity.grid_remove()
        else:
            food_image = Image.open(self.image_path)
            resized_image = food_image.resize((150, 100), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized_image)
            item_image.image = self.image 
            item_image.configure(image=self.image)
            item_name.configure(text=self.name)
            item_price.configure(text=self.price)
            item_description.configure(text=self.description)

food_item1 = FoodItem(Menu_index[0]['Image_path'], Menu_index[0]['Name'], Menu_index[0]['Price'], Menu_index[0]['Description'],remove_frame=False)
food_item1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)

food_item2 = FoodItem(Menu_index[1]['Image_path'], Menu_index[1]['Name'], Menu_index[1]['Price'], Menu_index[1]['Description'],remove_frame=False)
food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)

food_item3 = FoodItem(Menu_index[2]['Image_path'], Menu_index[2]['Name'], Menu_index[2]['Price'], Menu_index[2]['Description'],remove_frame=False)
food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)



page_number=1
total_page_number=math.ceil(len(Menu_index)/3)
def next_page():
    global page_number   
    if page_number==total_page_number:
        page_number=1
    else:
        page_number=page_number+1
    display=str(page_number)+'/'+str(total_page_number)
    page_displayed.configure(text=display)
    page_displayed.text=display
    food_item_1 = FoodItem(Menu_index[(page_number-1)*3]['Image_path'], Menu_index[(page_number-1)*3]['Name'], Menu_index[(page_number-1)*3]['Price'], Menu_index[(page_number-1)*3]['Description'],remove_frame=False)
    food_item_1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)
    if ((page_number-1)*3+1)<len(Menu_index):
        food_item2 = FoodItem(Menu_index[(page_number-1)*3+1]['Image_path'], Menu_index[(page_number-1)*3+1]['Name'], Menu_index[(page_number-1)*3+1]['Price'], Menu_index[(page_number-1)*3+1]['Description'],remove_frame=False)
        food_item2.grid(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    else:
        food_item2 = FoodItem('', '','', '',remove_frame=True)
        
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    if ((page_number-1)*3+2)<len(Menu_index):
        food_item3 = FoodItem(Menu_index[(page_number-1)*3+2]['Image_path'], Menu_index[(page_number-1)*3+2]['Name'], Menu_index[(page_number-1)*3+2]['Price'], Menu_index[(page_number-1)*3+2]['Description'],remove_frame=False)
        food_item3.grid(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
    else:
        food_item3 = FoodItem('', '','', '',remove_frame=True)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
def last_page():
    global page_number   
    if page_number==1:
        page_number=total_page_number
    else:
        page_number=page_number-1
    display=str(page_number)+'/'+str(total_page_number)
    page_displayed.configure(text=display)
    page_displayed.text=display
    food_item_1 = FoodItem(Menu_index[(page_number-1)*3]['Image_path'], Menu_index[(page_number-1)*3]['Name'], Menu_index[(page_number-1)*3]['Price'], Menu_index[(page_number-1)*3]['Description'],remove_frame=False)
    food_item_1.configure(item1_image, item1_name, item1_price, item1_description,item1_order,item1_quantity)
    if ((page_number-1)*3+1)<len(Menu_index):
        food_item2 = FoodItem(Menu_index[(page_number-1)*3+1]['Image_path'], Menu_index[(page_number-1)*3+1]['Name'], Menu_index[(page_number-1)*3+1]['Price'], Menu_index[(page_number-1)*3+1]['Description'],remove_frame=False)
        food_item2.grid(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    else:
        food_item2 = FoodItem('', '','', '',remove_frame=True)
        
        food_item2.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    if ((page_number-1)*3+2)<len(Menu_index):
        food_item3 = FoodItem(Menu_index[(page_number-1)*3+2]['Image_path'], Menu_index[(page_number-1)*3+2]['Name'], Menu_index[(page_number-1)*3+2]['Price'], Menu_index[(page_number-1)*3+2]['Description'],remove_frame=False)
        food_item3.grid(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
        food_item3.configure(item2_image, item2_name, item2_price, item2_description,item2_order,item2_quantity)
    else:
        food_item3 = FoodItem('', '','', '',remove_frame=True)
        food_item3.configure(item3_image, item3_name, item3_price, item3_description,item3_order,item3_quantity)
page_change=Frame(window,bg='white')
page_change.grid(row=1,column=1)
page_displayed=Label(page_change,borderwidth=1,width=7,text=str(page_number)+'/'+str(total_page_number),bg="white",font=("Arial", 13),relief="solid")
page_displayed.grid(row=0,column=1,sticky=N,pady=(20))
icon_image1=Image.open("11.png")
resized_icon = icon_image1.resize((30, 20))
left_arrowicon = ImageTk.PhotoImage(resized_icon)
next_page=Button(page_change,image=left_arrowicon,command=next_page)
next_page.grid(row=0,column=2,padx=10)
icon_image2=Image.open("b033.png")
resized_icon = icon_image2.resize((30, 20))
right_arrowicon = ImageTk.PhotoImage(resized_icon)
last_page=Button(page_change,image=right_arrowicon,command=last_page)
last_page.grid(row=0,column=0,padx=(0,10))

window.mainloop()




'''import csv
  
# csv fileused id Geeks.csv
filename="menu_database.csv"
 
# opening the file using "with"
# statement

with open(filename, 'r') as data:
  for line in csv.DictReader(data):
      print(line)'''
