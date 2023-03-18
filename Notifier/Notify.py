from tkinter import*
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time
root=Tk()
root.title('Notifier')
root.geometry("420x300")
AOT = Image.open("title.png")
tkimage = ImageTk.PhotoImage(AOT)

# fetching the details
def fetch_data():
    title_data= data_title.get()
    msg_info = notification_data.get()
    time_details = timer_time.get()
    # print(get_title,get_msg, tt)

    if title_data == "" or msg_info == "" or time_details == "":
        messagebox.showerror("Alert", "All fields are required!")
    
    else:
        round_time = int(float(time_details))
        sec_time = round_time * 60
        msg=messagebox.askquestion("Confirmation","Do you want to clear this notification ?")
        if msg=="yes":
            reset()
        else:
            root.destroy()
            time.sleep(sec_time)

        notification.notify(title=title_data,
                            message=msg_info,
                            app_name="Notifier",
                            app_icon="ico.ico",
                            toast=False,
                            timeout=20)

img_label = Label(root, image=tkimage).grid()

def reset():
    global data_title,notification_data,timer_time
# Label - Title
    title_head = Label(root, text="Title",bg='#000', fg='#EFF0F3',font=("Times New Roman", 10,"bold")).place(x=12, y=70)


# ENTRY - Title
    data_title = Entry(root, width="25",font=("Times New Roman", 13),bg="#071844",fg="#F1F4F6")
    data_title.place(x=110, y=70)


# Label - Message
    notifier_head = Label(root, text="Message",bg='#000', fg='#EFF0F3',font=("Times New Roman", 10,"bold")).place(x=12, y=120)

# ENTRY - Message
    notification_data= Entry(root, width="40", font=("Times New Roman", 13),bg="#071844",fg="#F1F4F6")
    notification_data.place(x=110,height=30, y=120)


# Label - Time
    timer_head = Label(root, text="Timer",bg='#000', fg='#EFF0F3', font=("Times New Roman", 10,"bold")).place(x=12, y=175)


# ENTRY - Time
    timer_time = Entry(root, width="5", font=("Times New Roman", 13),bg="#071844",fg="#F1F4F6")
    timer_time.place(x=110, y=175)

# Label - min
    min_head = Label(root, text="min",bg='#000', fg='#EFF0F3', font=("Times New Roman", 10,"bold")).place(x=175, y=180)

# Button
    notification_button = Button(root, text="SET NOTIFICATION", font=("Times New Roman", 10, "bold"), fg="#F1F4F6", bg="#47689D", width=20,
             relief="raised", command=fetch_data).place(x=170, y=230)
    
reset()

root.resizable(0,0)
root.mainloop()










