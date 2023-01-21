# import tkinter module
from tkinter import *
import customtkinter
from tkinter import messagebox


# import other necessary modules
import time
# creating root object
root = customtkinter.CTk()   
 
# defining size of window
root.geometry("700x550")
root.resizable(False,False)

# setting up the title of window
root.title("ვიჟინერის მეთოდი") 
Tops = customtkinter.CTkFrame(master=root,
                            fg_color="#7286D3")                    
Tops.place(relx=0.5, rely=0, width=850, height=100, anchor="n") 


f1 = customtkinter.CTkFrame(master=root, height=1222,width=800,fg_color="#8EA7E9")
f1.place_configure(x=0, y=100,width=850, height=350)

Bottom = customtkinter.CTkFrame(master=root,
                            fg_color="#E5E0FF")
Bottom.place(x=0, y=450,width = 850)
# ==============================================
#				 DRO
# ==============================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = customtkinter.CTkLabel(Tops, font = ('helvetica', 30),
		text = "ვიჟინერის მეთოდი", text_color="#FFF2F2",anchor="center")
lblInfo.place(x=310,y=10)

lblInfo = customtkinter.CTkLabel(Tops, font=('arial', 20),
			text = localtime, text_color="#E5E0FF",
						height = 60, anchor = 'center')
lblInfo.place(x=325,y=50)
						

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = IntVar()
Result = StringVar()

# exit function
def qExit():
	root.destroy()

# Function to reset the window
def Reset():
	rand.set("")
	Msg.set("")
	key.set("")
	mode.set("")
	Result.set("")


# reference

lblReference = customtkinter.CTkLabel(master=f1,
                               text="სახელი",
                               text_color="#FFFFE8",
                               width=200,
                               height=60, font = ('arial', 25))
				
lblReference.grid(row = 0, column = 0,pady=8)

txtReference = customtkinter.CTkEntry(master=f1,
                               textvariable=rand,
                               width=200,
                               height=50,
                               fg_color="#FFF2F2",
                               border_width=3,
                               corner_radius=10)
						
txtReference.grid(row = 0, column = 1,pady=8)

# labels
lblMsg = customtkinter.CTkLabel(master=f1,
                               text="ტექსტური მესიჯი",
                               text_color="#FFFFE8",
                               width=200,
                               height=60, font = ('arial', 25))
		
lblMsg.grid(row = 1, column = 0,pady=8)

txtMsg = customtkinter.CTkEntry(master=f1,
                               textvariable=Msg,
                               width=200,
                               height=50,
                               fg_color="#FFF2F2",
                               border_width=3,
                               corner_radius=10)			
txtMsg.grid(row = 1, column = 1,pady=8)

lblkey = customtkinter.CTkLabel(master=f1,
                               text="გასაღები",
                                                              text_color="#FFFFE8",

                               width=200,
                               height=60, font = ('arial', 25))
			
lblkey.grid(row = 2, column = 0,pady=8)

txtkey = customtkinter.CTkEntry(master=f1,
                               textvariable=key,
                               width=200,
                               height=50,
                               fg_color="#FFF2F2",
                               border_width=3,
                               corner_radius=10)
				
txtkey.grid(row = 2, column = 1,pady=8)

lblmode = customtkinter.CTkLabel(master=f1,
                               text="აირჩიეთ",
                               width=200,
                                                              text_color="#FFFFE8",

                               height=60, font = ('arial', 25))
								
lblmode.grid(row = 3, column = 0,pady=8)



txtrdbtnmode1 =customtkinter.CTkRadioButton(master=f1, text="კოდირება", variable= mode,fg_color="#FF8B13", value=1)
txtrdbtnmode1.grid(row = 3, column = 1,pady=8)


txtrdbtnmode2 =customtkinter.CTkRadioButton(master=f1, text="დეკოდირება", variable= mode,fg_color="#FF8B13", value=2)
txtrdbtnmode2.grid(row = 3, column = 2,pady=8)
                                          
				



txtService = customtkinter.CTkEntry(master=Bottom,
                               textvariable=Result,
                               width=400,
                               height=50,
                               fg_color="#FFF2F2",
                               border_width=3,
                               corner_radius=10)
						
txtService.place(x = 160, y=20)



# Vigenère cipher
import base64

# Function to encode
def kodireba(key, clear):
	enc = []
	
	for i in range(len(clear)):
		key_c = key[i % len(key)]
		enc_c = chr((ord(clear[i]) +
					ord(key_c)) % 256)
					
		enc.append(enc_c)
		
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode
def dekodireba(key, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec)


def Ref():
    try:
        msg = Msg.get()
        k = key.get()
        m = mode.get()
        if (not Msg.get() == "") and (not key.get() == "") and (not mode.get() == ""):
            if (m == 1):
                Result.set(kodireba(k, msg))
            else:
                Result.set(dekodireba(k, msg))
        else:
            messagebox.showerror("showerror", "გთხოვთ შეავსოთ მოცემული ველები !")
    except:
        messagebox.showerror("showerror", "გთხოვთ აირჩიოთ კოდირება გსურთ , თუ დეკოდირება !")


# Show message button


btnTotal = customtkinter.CTkButton(master=f1,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Show Message",
                                 command=Ref, hover=True, hover_color="green").place(x=150, y=310)


# Reset button
btnReset = customtkinter.CTkButton(master=f1,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Reset",
                                 command=Reset,hover=True, hover_color="yellow",).place(x=316, y=310)

# Exit button
btnExit =customtkinter.CTkButton(master=f1,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Exit",
                                 command=qExit, hover=True, hover_color="red").place(x=467, y=310)

# keeps window alive
root.mainloop()