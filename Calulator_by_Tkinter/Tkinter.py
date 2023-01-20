from tkinter import *

def Button_presstracker():
	print("Trust the process")

window_1=Tk()



window_1.geometry('330x280')

label_1=Label(window_1,text="Image Button",fg='black')

b1  =Button(window_1,text="0",background='white',width=5,height=2)
b2  =Button(window_1,text=".",background='white',width=5,height=2)
b3  =Button(window_1,text="=",background='white',width=5,height=2)
b4  =Button(window_1,text="+",background='white',width=5,height=2)
b5  =Button(window_1,text="1",background='white',width=5,height=2)
b6  =Button(window_1,text="2",background='white',width=5,height=2)
b7  =Button(window_1,text="3",background='white',width=5,height=2)
b8  =Button(window_1,text="-",background='white',width=5,height=2)
b9  =Button(window_1,text="4",background='white',width=5,height=2)
b10 =Button(window_1,text="5",background='white',width=5,height=2)
b11 =Button(window_1,text="6",background='white',width=5,height=2)
b12 =Button(window_1,text="*",background='white',width=5,height=2)
b13 =Button(window_1,text="7",background='white',width=5,height=2)
b14 =Button(window_1,text="8",background='white',width=5,height=2)
b15 =Button(window_1,text="9",background='white',width=5,height=2)
b16 =Button(window_1,text="/",background='white',width=5,height=2)

# b3 =Button(window_1,text="Increment the button", bd='15', command=Button_presstracker)
b17 =Button(window_1,text="Exit", bd='5',width=4,height=2, command=window_1.destroy)
# photo_1 = PhotoImage(file='Embedded.png')
# photo_1 = photo_1.subsample(2,2)


# b2=Button(window_1,text="We trust the process", bd='8', image=photo_1, background='green', fg='red',  command=Button_presstracker)


# b1.pack(side=LEFT)
b1.place(x=100,y=150)
b2.place(x=140,y=150)
b3.place(x=180,y=150)
b4.place(x=220,y=150)
b5.place(x=100,y=110)
b6.place(x=140,y=110)
b7.place(x=180,y=110)
b8.place(x=220,y=110)
b9.place(x=100,y=70)
b10.place(x=140,y=70)
b11.place(x=180,y=70)
b12.place(x=220,y=70)
b13.place(x=100,y=30)
b14.place(x=140,y=30)
b15.place(x=180,y=30)
b16.place(x=220,y=30)
# b3.pack(side=BOTTOM)
b17.pack(side=BOTTOM)

label_1.pack(side=BOTTOM)

label_1.mainloop()