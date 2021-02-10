# using for loop GUI APP

import tkinter as tk       
from tkinter import ttk  
win = tk.Tk() 
win.title('LOOP')

# create label :
# =================

labels = ['What is your name : ', 'what is your Age : ', 'what is your Gender : ', 'Country : ', 'State : ', 'City : ']

for i in range(len(labels)):
    cur_label = 'label' + str(i) # label0,label1-----etc.
    cur_label = ttk.Label(win, text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W, padx=3,pady=3)   #here we give the padding to our o/p window around 3-pixals

# entry box:
# ===========
name_var = tk.StringVar()
user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()

}
counter=0
for i in user_info:
    cur_entrybox = 'entry_' + i   # entry_name, entry_age----etc.
    cur_enterybox = ttk.Entry(win, width=16, textvariable=user_info[i])
    cur_enterybox.grid(row=counter,column=1, padx=3,pady=3)  #here we give the padding to our o/p window around 3-pixals
    counter += 1

# submit button:
#===============

def submit():
    print(user_info['name'].get())      # here we use the tkinter's get methode
    print(user_info.get('age').get())   # here we use the dictionaries's get methode
    print(user_info.get('gender').get())  # here we use the dictionaries's get methode
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())


submit_btn = ttk.Button(win, text='Submit',command=submit)
submit_btn.grid(row=6,columnspan=2)

win.mainloop()  