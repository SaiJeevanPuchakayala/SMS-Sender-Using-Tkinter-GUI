import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter.scrolledtext import ScrolledText


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'your api code',# your fast2sms api code must be entered here.
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    status = response.json()  # response.json() returns a JSON object of the URL you have requested.
    print(status)
    return status.get('return') #The get() method returns the value for the specified key if key is in dictionary.


def button_click(): # This button_click function is used for send button in Tkinter GUI window.
    num = MobileNumber.get()
    msg = textMsg.get("1.0", END)
    sender = send_sms(num, msg)
    if sender:
        showinfo("Alert Box", "Message Sent Successfully.!")
    else:
        showerror("Alert Box", "Something went wrong. Message was not delivered!")


#calling Tk() method
root = Tk()

#title() method is used to change the title 
root.title(" Jeevan's SMS Sender ")

#geometry() method is used to resize the Gui Window
root.geometry("400x400")


#Sets the Tkinter Window Background Color
root.configure(bg='gray25')

#Sets Window Icon in Tkinter
root.iconbitmap('Send_sms.ico')

# Lable() function creates a label widget 
l =  Label(root, text="⇚ New Message ⇛",font=('verdana',15,'bold'),bg="gray25",fg="yellow")
l.place(x=85,y=10)


# Lable() function creates a label widget 
l1 = Label(root, text = "To Mobile Number:",font=('verdana',12,'bold'),bg="gray25",fg="yellow")
l1.place(x=10,y=70)

# entry widgets, used to take entry from user 
MobileNumber = Entry(root, font=("Helvetica", 10, "bold"))
MobileNumber.pack(fill=None, pady=100,ipadx = 120,ipady = 5)


# Lable() function creates a label widget 
l2 = Label(root, text = "Message:",font=('verdana',12,'bold'),bg="gray25",fg="yellow")
l2.place(x=10,y=160)

# ScrolledText entry widgets, used to take entry from user
textMsg = ScrolledText(root,width=40,height=5)
textMsg['font'] = ("verdana",10,'bold')
textMsg.place(x=10,y=190)


# Button() function is used to create button widgets
sendBtn = Button(root, text="⮞ SEND", command=button_click,font=('verdana',10,'bold'),bg="blue",fg="white",cursor='hand2')
sendBtn.place(x=250,y=322)


# Button for closing 
exit_button = Button(root, text="X EXIT", command=root.destroy,font=('verdana',10,'bold'),bg="blue",fg="white",cursor='hand2') 
exit_button.place(x=75,y=322)



# Disables resizing in a Tkinter Window.
root.resizable(False, False) 


#mainloop() is used to load the GUI Window
root.mainloop()
