from tkinter import * 
import screen1
import screen2
root = Tk()
root.geometry("300x150")

topframe=screen1.create_screen1(root)
bottomframe=screen2.create_screen2(root)

topframe.pack()

def handleButtonClick1():
    bottomframe.pack()
    topframe.pack_forget()
    
def handleButtonClick2():
    bottomframe.pack_forget()
    topframe.pack()
    
b1_button = Button(topframe, text ="Button 1", fg ="red",command=handleButtonClick1)
b1_button.pack( side = LEFT)

b2_button = Button(bottomframe, text ="Button 2", fg ="red",command=handleButtonClick2)
b2_button.pack( side = LEFT)




root.mainloop()
