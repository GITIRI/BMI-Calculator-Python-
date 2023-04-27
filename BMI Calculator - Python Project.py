BMI CALCULATOR

#importing the necessary libraries/modules
from tkinter import *
from tkinter import messagebox

#define a function to get the name of the user & calculate BMI
def calculate_BMI():
    name = name_tf.get()
    weight = int(weight_tf.get())
    height = float(height_tf.get())
    BMI = (weight) / (height * height)
    BMI = round(BMI, 1)
    BMI_index (name, BMI)
    
#define a function to reset the entries
def reset_entry():
    name_tf.delete(0,'end')
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

#Display name, BMI & message based on user's details    
def BMI_index(name, BMI):
    if BMI > 0: 
        if BMI < 18.5:
             messagebox.showinfo('BMI info', f'{name}, your BMI is {BMI}, which means that you are underweight with minimal health risk')
        elif BMI <= 24.9:
            messagebox.showinfo('BMI info', f'{name}, your BMI is {BMI}, which means that you have normal weight with minimal health risk')
        elif BMI <= 29.9:
             messagebox.showinfo('BMI info', f'{name}, your BMI is {BMI},, which means that you are overweight with an increased health risk')
        elif BMI <= 34.9:
            messagebox.showinfo('BMI info', f'{name}, your BMI is {BMI}, which means that you are obese with a high health risk')
        elif BMI <= 39.9:
            messagebox.showinfo('BMI info', f'{name}, your BMI is {BMI}, which means that you are severely obese with a very high health risk')
        else:
            messagebox.showinfo('BMI info', f'{name}, your BMI is {BMI}, which means that you are morbidly obese with an extremely high health risk')
            
#create main window for the GUI            
ws= Tk()
ws.title('BMI Calculator')
ws.geometry('300x250')
ws.config(bg='#FFFFF0')

var = IntVar()

#create frame
frame = Frame(
    ws,
    padx=15, 
    pady=15
)
frame.pack(expand=True)

#create labels, entry widgets & radio buttons
name_lb = Label(
    frame,
    text="Enter Your Name"
)
name_lb.grid(row=1, column=1)

name_tf = Entry(
    frame, 
)
name_tf.grid(row=1, column=2, pady=5)


age_lb = Label(
    frame,
    text="Enter Your Age (0 - 100)"
)
age_lb.grid(row=2, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=2, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=3, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=3, column=2, pady=5)

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
    text="Enter Your Height (m)  "
)
height_lb.grid(row=4, column=1)

weight_lb = Label(
    frame,
    text="Enter Your Weight (kg)  ",

)
weight_lb.grid(row=5, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=4, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=5, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=6, columnspan=3, pady=10)

#create calculate, reset & exit buttons
cal_btn = Button(
    frame3,
    text='Calculate',
    command = calculate_BMI
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

#run the window
ws.mainloop()         
    
