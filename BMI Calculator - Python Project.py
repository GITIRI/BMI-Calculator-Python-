#!/usr/bin/env python
# coding: utf-8

#  # BMI CALCULATOR
#  
# https://mercer-health.com/services/weight-management-center/bmi-calculator#:~:text=Body%20Mass%20Index%2C%20or%20BMI,inches%20x%20height%20in%20inches
# 
# 

# In[1]:


#create variables that accept inputs

name = input("Enter your name: ")

weight = int (input("Enter your weight in kilograms: "))

height = float(input("Enter your height in metres: "))

BMI = (weight) / (height * height)

BMI = round (BMI, 1)

print (BMI)
print (name)


# In[ ]:


from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!')   

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)


age_lb = Label(
    frame,
    text="Enter Age (2 - 120)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()


# In[3]:


if BMI < 18.5:
    print (name,", you are underweight with minimal health risk")
elif BMI <= 24.9:
    print (name,", you have normal weight with minimal health risk")
elif BMI <= 29.9:
    print (name,", you are overweight with an increased health risk")
elif BMI <= 34.9:
    print (name,", you are obese with a high health risk")
elif BMI <= 39.9:
    print (name,", you are severely obese with a very high health risk")
else:
    print (name,", you are morbidly obese with an extremely high health risk")


# In[ ]:




