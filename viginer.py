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
Tops = customtkinter.CTkFrame(master=root, fg_color="#7286D3")
Tops.grid(row=0, column=0, sticky="nsew", pady=0)
Tops.configure(height = 50)
Tops.grid_rowconfigure(0, weight=1)
Tops.grid_columnconfigure(0, weight=1)


f1 = customtkinter.CTkFrame(master=root, fg_color="#8EA7E9")
f1.grid(row=1, column=0, sticky="nsew", pady=0)



Bottom = customtkinter.CTkFrame(master=root, fg_color="#E5E0FF")
Bottom.grid(row=2, column=0, sticky="nsew")
Bottom.configure(height=50)


root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=2)
root.grid_rowconfigure(2, weight=1)
# ==============================================
#				 DRO
# ==============================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = customtkinter.CTkLabel(Tops, font = ('helvetica', 30),
		text = "ვიჟინერის მეთოდი", text_color="#FFF2F2",anchor="center")
lblInfo.pack(side=TOP, anchor="center")


lblInfo = customtkinter.CTkLabel(Tops, font=('arial', 20),
text = localtime, text_color="#E5E0FF",
height = 60)
lblInfo.pack(side=TOP, anchor = 'center')
						

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
	mode.set(0)
	Result.set("")


# reference

# lblReference = customtkinter.CTkLabel(master=f1,
#                                text="სახელი",
#                                text_color="#FFFFE8",
#                                width=200,
#                                height=60, font = ('arial', 25))
				
# lblReference.grid(row = 0, column = 0,pady=8)

# txtReference = customtkinter.CTkEntry(master=f1,
#                                textvariable=rand,
#                                width=200,
#                                height=50,
#                                fg_color="#FFF2F2",
#                                border_width=3,
#                                corner_radius=10)
						
# txtReference.grid(row = 0, column = 1,pady=8)

# labels
lblMsg = customtkinter.CTkLabel(master=f1,
                               text="ტექსტური მესიჯი",
                               text_color="#FFFFE8",
                               width=200,
                               height=60, font = ('arial', 25))
		
lblMsg.grid(row = 0, column = 0,pady=50)

txtMsg = customtkinter.CTkEntry(master=f1,
                               textvariable=Msg,
                               width=200,
                               height=50,
                               fg_color="#FFF2F2",
                               border_width=3,
                               corner_radius=10)			
txtMsg.grid(row = 0, column = 1,pady=8)

lblkey = customtkinter.CTkLabel(master=f1,
                               text="გასაღები",
                                                              text_color="#FFFFE8",

                               width=200,
                               height=60, font = ('arial', 25))
			
lblkey.grid(row = 1, column = 0,pady=8)

txtkey = customtkinter.CTkEntry(master=f1,
                               textvariable=key,
                               width=200,
                               height=50,
                               fg_color="#FFF2F2",
                               border_width=3,
                               corner_radius=10)
				
txtkey.grid(row = 1, column = 1,pady=8)

lblmode = customtkinter.CTkLabel(master=f1,
                               text="აირჩიეთ",
                               width=200,
                                text_color="#FFFFE8",
                               height=60, font = ('arial', 25))
								
lblmode.grid(row = 2, column = 0,pady=5)



txtrdbtnmode1 =customtkinter.CTkRadioButton(master=f1, text="კოდირება", variable= mode,fg_color="#FF8B13", value=1)
txtrdbtnmode1.grid(row = 2, column = 1,pady=35)


txtrdbtnmode2 =customtkinter.CTkRadioButton(master=f1, text="დეკოდირება", variable= mode,fg_color="#FF8B13", value=2)
txtrdbtnmode2.grid(row = 2, column = 2,pady=5)
                                          
				



txtService = customtkinter.CTkEntry(master=Bottom,
                               textvariable=Result,
                               width=400,
                               height=50,
                               fg_color="#FFF2F2",
                               border_width=3,
                               corner_radius=10)
Bottom.grid_columnconfigure(0, weight=1)
Bottom.grid_rowconfigure(0, weight=1)
txtService.grid(row=0, column=0)



# Vigenère cipher
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))


# Function to encode
def kodireba(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))

# Function to decode
def dekodireba(key, enc):
	orig_text = []
	for i in range(len(enc)):
		x = (ord(enc[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))

def Ref():
        msg = Msg.get()
        k = key.get()
        m = mode.get()
        generateKeyWord = generateKey(msg,k)
        if (not Msg.get() == "") and (not key.get() == "") and (not mode.get() == 0):
            if (m == 1):
                Result.set(kodireba(generateKeyWord, msg))
            else:
                Result.set(dekodireba(generateKeyWord, msg))
        else:
            messagebox.showerror("showerror", "გთხოვთ შეავსოთ მოცემული ველები !")


# Show message button


btnTotal = customtkinter.CTkButton(master=f1,
                                  width=120,
                                   height=32,
                                    border_width=0,
                                        corner_radius=8,
                                        text="Show Message",
                                        command=Ref, hover=True
                                        , hover_color="green")
btnTotal.grid(row=4, column=0, padx=2)

btnReset = customtkinter.CTkButton(master=f1, width=120, height=32, border_width=0, corner_radius=8, text="Reset", command=Reset, hover=True, hover_color="yellow")
btnReset.grid(row=4, column=1, padx=2)

btnExit = customtkinter.CTkButton(master=f1, width=120, height=32, border_width=0, corner_radius=8, text="Exit", command=qExit, hover=True, hover_color="red")
btnExit.grid(row=4, column=2, padx=2)


f1.grid_columnconfigure(0, weight=1)
f1.grid_columnconfigure(1, weight=1)
f1.grid_columnconfigure(2, weight=1)
f1.grid_rowconfigure(3, weight=1)
# keeps window alive
root.mainloop()