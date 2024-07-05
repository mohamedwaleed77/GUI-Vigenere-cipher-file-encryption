import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from cipher import Cipher
import bg_images
from tkinter import messagebox

class CipherGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Cipher")

        # Load the background image
        self.bg_image = PhotoImage(data=bg_images.background_base64)
        self.bg_encrypt_button = PhotoImage(data=bg_images.encrypt_base64)
        self.bg_decrypt_button = PhotoImage(data=bg_images.decrypt_base64)
        self.bg_browse_button = PhotoImage(data=bg_images.browse_base64)
        self.background_label = tk.Label(master, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.master.title("File Cipher| 203659 | 212421")
        self.master.geometry(f"{self.bg_image.width()}x{self.bg_image.height()}")
        self.master.resizable(False, False)
        
        self.file_listbox = tk.Listbox(master, width=76, height=11)
        self.file_listbox.place( x=15, y=50)

        self.btn_browse = tk.Button(master, image=self.bg_browse_button,text="Browse", command=self.browse_files,borderwidth=0)
        self.btn_browse.place(x=400,y=282)

        self.btn_clear = tk.Button(master, text="Clear", command=self.clear_list)
        self.btn_clear.place( x=440, y=20)

        self.entry_key = tk.Entry(master, width=51)
        self.entry_key.place(x=165, y=247)

        self.btn_encrypt = tk.Button(master, image=self.bg_encrypt_button , text="Encrypt", command=lambda: self.process_cipher('e'),borderwidth=0)
        self.btn_encrypt.place(x=86, y=291)

        self.btn_decrypt = tk.Button(master, image=self.bg_decrypt_button,  text="Decrypt", command=lambda: self.process_cipher('d'),borderwidth=0)
        self.btn_decrypt.place(x=250, y=291)
        tk.messagebox.showinfo("IMPORTANT!!","IF you are decrypting & you are not 100% sure of password \nplease make backup of files!")

    def browse_files(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.file_listbox.delete(0, tk.END)
            for file_path in file_paths:
                self.file_listbox.insert(tk.END, file_path)

    def clear_list(self):
        self.file_listbox.delete(0, tk.END)

    def process_cipher(self, mode):
        key = self.entry_key.get()
        if key:
            selected_files = self.file_listbox.get(0, tk.END)
            for file_path in selected_files:
                cipher_obj = Cipher(file_path, key)
                cipher_obj.vig(mode)
                output_path = file_path
                cipher_obj.output(output_path)
            tk.messagebox.showinfo("Success","no errors :) !")
        else:
            #no need to send 0 to vigenere cipher bcoz i'm sure there is no changes will happen
            tk.messagebox.showinfo("Null key","NULL = No changes :) !")

def main():
    root = tk.Tk()
    app = CipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
