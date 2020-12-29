import cv2
import tkinter as tk
import string
import os

root = tk.Tk()
root.geometry("500x800")
root.title("STEGANOGRAPHY")
root.configure(bg="skyblue")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# print(c)

x = cv2.imread("wp5476073.jpg")
i = x.shape[0]
j = x.shape[1]
dim=str(i)
y=str("The Picture dimension willl be-"+dim+" x " + str(j))

Dim_Label= tk.Label(root,text= y).place(x=10,y=50)
label= tk.Label(root,text="Data Hiding Using Steganography",bg="darkblue",fg="white").place(x=100,y=10)

key_button= tk.Button(root,text="Enter key to edit(Security Key) :").place(x=10,y=100)
key_entry= tk.Entry(root).place(x=250,y=100)
key=get.key_entry()
text_button=tk.Button(root, text="Enter text to hide- ").place(x=100,y=150)
text_entry=tk.Entry(root).place(x=250,y=150)
text=get.text_entry()

kl = 0
tln = len(text)
z = 0  # decides plane
n = 0  # number of row
m = 0  # number of column

l = len(text)

for i in range(l):
    x[n, m, z] = d[text[i]] ^ d[key[kl]]
    n = n + 1
    m = m + 1
    m = (
                    m + 1) % 3  # this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
    # whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
    kl = (kl + 1) % len(key)

cv2.imwrite("wp5476073.jpg", x)
os.startfile("wp5476073.jpg")

label2= tk.Label(root,text="Data Hiding in Image completed successfully.",bg="yellow",fg="black").place(x=100,y=200)

kl = 0
tln = len(text)
z = 0  # decides plane
n = 0  # number of row
m = 0  # number of column

def extract_data():
    key2_label=tk.Label(root,text="re-enter the to extract data-").place(x=100,y=250)
    key2_entry=tk.Entry(root).place(x=250,y=250)
    key2=get.key_entry()

    decrypt = ""

    if key == key1:
        for i in range(l):
            decrypt += c[x[n, m, z] ^ d[key[kl]]]
            n = n + 1
            m = m + 1
            m = (m + 1) % 3
            kl = (kl + 1) % len(key)
        text_encrypted= ("Encrypted text was : "+decrypt)
        label_3=tk.Label(root,text=text_encrypted).place(x=100,y=300)
    else:
        label_4= tk.Label(root,text="Key doesn't matched.").place(x=100,y=300)


Decryption =tk.Button(root,text="Decrypt",command=extract_data).place(x=100,y=450)


def quit():
    root.destroy()

quit_btn= tk.Button(root, text="Quit",width=35,bg="White",fg="blue",command=quit).place(x=100,y=760)

root.mainloop()
