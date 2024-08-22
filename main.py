from customtkinter import *
from PIL import Image
import os
from datetime import datetime

# Set appearance mode and color theme
set_appearance_mode("dark")
set_default_color_theme("dark-blue")

# Create the main window
root = CTk(fg_color="black")
root.title("Notes App")
root.geometry("1000x600")
root.minsize(1000, 600)
root.iconbitmap("images\\notes.ico")

# Load images
image_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), "images")
notes_image = CTkImage(Image.open(os.path.join(image_path, "notes.png")), size=(40, 40))
plus_image = CTkImage(Image.open(os.path.join(image_path, "plus.png")), size=(35, 35))
close_image = CTkImage(Image.open(os.path.join(image_path, "x.png")), size=(35, 35))
edit_image = CTkImage(Image.open(os.path.join(image_path, "edit.png")), size=(30, 30))
delete_image = CTkImage(Image.open(os.path.join(image_path, "trash.png")), size=(30, 30))

class NotesApp:
    def __init__(self, master):
        self.root = master
        self.notes = []

        frame = CTkFrame(self.root, fg_color="transparent")

        self.title_frame = CTkFrame(frame, fg_color="transparent")
        CTkLabel(self.title_frame, text="Notes App", image=notes_image, compound=LEFT, font=("Poppins", 30, "bold"), text_color="white").pack(side=LEFT, anchor="nw", padx=10)
        CTkButton(self.title_frame, text="", image=plus_image, width=0, fg_color="transparent", hover_color="#222", command=self.open_popup).pack(side=RIGHT, anchor="ne", padx=10)
        self.title_frame.pack(side=TOP, fill=X, padx=45, pady=5)

        self.notes_frame = CTkScrollableFrame(frame, fg_color="#000")
        self.notes_frame.pack(side=TOP, fill=BOTH, expand=True, padx=40, pady=10)
        
        frame.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=20)

        self.add_note(title="Note Maker", description="Hello all, \nWelcome to Note Making app build with Python.")

    def open_popup(self):
        self.type_frame = CTkToplevel(self.root, fg_color="#000")
        self.type_frame.overrideredirect(True)

        toplevel_width = 500
        toplevel_height = 500

        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()

        x = root_x + (root_width - toplevel_width) // 2
        y = root_y + (root_height - toplevel_height) // 2

        self.type_frame.geometry(f"{toplevel_width}x{toplevel_height}+{x}+{y-40}")
        self.type_frame.resizable(False, False)
        self.type_frame.attributes("-topmost", True)
        self.type_frame.grab_set()

        self.frame = CTkFrame(self.type_frame, fg_color="#222", border_color="#111", corner_radius=10)

        self.note_title_frame = CTkFrame(self.frame, fg_color="#222")

        note_frame = CTkFrame(self.note_title_frame, fg_color="transparent")
        CTkLabel(note_frame, text="Add a new Note", font=("IBM Plex Sans", 30, "bold"), text_color="white").pack(side=LEFT, padx=10)
        CTkButton(note_frame, text="", width=0, fg_color="transparent", hover_color="#333", image=close_image, command=lambda: self.type_frame.destroy()).pack(side=RIGHT)
        note_frame.pack(side=TOP, fill=X, padx=20, pady=10)

        self.horizontal_line_note_title = CTkFrame(self.note_title_frame, height=2, fg_color="#a5a5a5")
        self.horizontal_line_note_title.pack(side=BOTTOM, fill=X, pady=0, padx=0)

        self.note_title_frame.pack(fill=X, pady=5, padx=0, ipady=0)
        
        note_title_frame = CTkFrame(self.frame)
        CTkLabel(note_title_frame, text="Title", font=("Poppins", 25, "bold"), text_color="white").pack(side=TOP, anchor="nw", padx=30)
        self.note_entry = CTkEntry(note_title_frame, height=60, placeholder_text="", font=("Poppins", 25), fg_color="transparent", border_color="#cdcdcd", text_color="white")
        self.note_entry.pack(side=TOP, fill=X, padx=30, pady=10)
        note_title_frame.pack(side=TOP, fill=X, pady=10)
        
        note_description_frame = CTkFrame(self.frame)
        CTkLabel(note_description_frame, text="Description", font=("Poppins", 25, "bold"), text_color="white").pack(side=TOP, anchor="nw", padx=30, pady=5)
        self.note_description = CTkTextbox(note_description_frame, height=60, font=("Poppins", 25), fg_color="transparent", border_color="#cdcdcd", text_color="white", border_width=1)
        self.note_description.pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=10)
        note_description_frame.pack(side=TOP, fill=BOTH, expand=True, pady=5)

        CTkButton(self.frame, text="Add Note", fg_color="#4D76DB", hover_color="#567DDC", font=("Poppins", 20), command=lambda: (self.add_note(title=self.note_entry.get(), description=self.note_description.get("1.0", END)), self.type_frame.destroy())).pack(side=TOP, fill=X, ipady=15, pady=20, padx=30)

        self.frame.pack(fill=BOTH, expand=True)

    def update_note(self, note_frame, old_title, old_description):
        self.type_frame = CTkToplevel(self.root, fg_color="#000")
        self.type_frame.overrideredirect(True)

        toplevel_width = 500
        toplevel_height = 500

        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()

        x = root_x + (root_width - toplevel_width) // 2
        y = root_y + (root_height - toplevel_height) // 2

        self.type_frame.geometry(f"{toplevel_width}x{toplevel_height}+{x}+{y-40}")
        self.type_frame.resizable(False, False)
        self.type_frame.attributes("-topmost", True)
        self.type_frame.grab_set()

        self.frame = CTkFrame(self.type_frame, fg_color="#222", border_color="#111", corner_radius=10)

        self.note_title_frame = CTkFrame(self.frame, fg_color="#222")

        note_frame_header = CTkFrame(self.note_title_frame, fg_color="transparent")
        CTkLabel(note_frame_header, text="Update a Note", font=("IBM Plex Sans", 30, "bold"), text_color="white").pack(side=LEFT, padx=10)
        CTkButton(note_frame_header, text="", width=0, fg_color="transparent", hover_color="#333", image=close_image, command=lambda: self.type_frame.destroy()).pack(side=RIGHT)
        note_frame_header.pack(side=TOP, fill=X, padx=20, pady=10)

        self.horizontal_line_note_title = CTkFrame(self.note_title_frame, height=2, fg_color="#a5a5a5")
        self.horizontal_line_note_title.pack(side=BOTTOM, fill=X, pady=0, padx=0)

        self.note_title_frame.pack(fill=X, pady=5, padx=0, ipady=0)
        
        note_title_frame = CTkFrame(self.frame)
        CTkLabel(note_title_frame, text="Title", font=("Poppins", 25, "bold"), text_color="white").pack(side=TOP, anchor="nw", padx=30)
        self.note_entry = CTkEntry(note_title_frame, height=60, placeholder_text="", font=("Poppins", 25), fg_color="transparent", border_color="#cdcdcd", text_color="white")
        self.note_entry.insert(0, old_title)
        self.note_entry.pack(side=TOP, fill=X, padx=30, pady=10)
        note_title_frame.pack(side=TOP, fill=X, pady=10)
        
        note_description_frame = CTkFrame(self.frame)
        CTkLabel(note_description_frame, text="Description", font=("Poppins", 25, "bold"), text_color="white").pack(side=TOP, anchor="nw", padx=30, pady=5)
        self.note_description = CTkTextbox(note_description_frame, height=60, font=("Poppins", 25), fg_color="transparent", border_color="#cdcdcd", text_color="white", border_width=1)
        self.note_description.insert("1.0", old_description)
        self.note_description.pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=10)
        note_description_frame.pack(side=TOP, fill=BOTH, expand=True, pady=5)

        CTkButton(self.frame, text="Update Note", fg_color="#4D76DB", hover_color="#567DDC", font=("Poppins", 20), command=lambda: self.apply_update(note_frame)).pack(side=TOP, fill=X, ipady=15, pady=20, padx=30)

        self.frame.pack(fill=BOTH, expand=True)

    def apply_update(self, note_frame):
        new_title = self.note_entry.get()
        new_description = self.note_description.get("1.0", END)
        
        # Update the note frame with new values
        for widget in note_frame.winfo_children():
            if isinstance(widget, CTkLabel):
                widget.configure(text=new_title)
            if isinstance(widget, CTkTextbox):
                widget.configure(state="normal")
                widget.delete("1.0", END)
                widget.insert("1.0", new_description)
                widget.configure(state="disabled")
        
        self.type_frame.destroy()

    def delete_note(self, note_frame):
        note_frame.destroy()

    def add_note(self, title=None, description=None):
        note_frame = CTkFrame(self.notes_frame, fg_color="#111")

        title_label = CTkLabel(note_frame, text=title, font=("Carbel", 28, "bold"), text_color="white")
        title_label.pack(side=TOP, anchor="nw", padx=20, pady=10)

        description_box = CTkTextbox(note_frame, font=("Candera", 25, "bold"), text_color="#e5e5e5", fg_color="transparent", height=80)
        description_box.pack(side=TOP, fill=X, anchor="nw", padx=15, pady=1)
        description_box.insert("1.0", description)
        description_box.configure(state="disabled")

        info_title_frame = CTkFrame(note_frame, fg_color="transparent")
        now = datetime.now()
        formatted_time = now.strftime("%B %d, %Y")
        CTkLabel(info_title_frame, text=formatted_time, text_color="#a5a5a5", font=("Carbel", 20)).pack(side=LEFT, anchor="nw", padx=20, pady=8)
        CTkButton(info_title_frame, text="", text_color="white", font=("Carbel", 20, "bold"), image=delete_image, compound=LEFT, fg_color="transparent", width=0, hover_color="#444",
                   command=lambda: self.delete_note(note_frame)).pack(side=RIGHT, anchor="ne", padx=0)
        CTkButton(info_title_frame, text="", text_color="white", font=("Carbel", 20, "bold"), image=edit_image, compound=LEFT, fg_color="transparent", width=0, hover_color="#444",
                   command=lambda: self.update_note(note_frame, title, description)).pack(side=RIGHT, anchor="ne", padx=0)
        info_title_frame.pack(side=BOTTOM, fill=X, padx=5)

        note_frame.pack(side=TOP, padx=10, fill=X, ipadx=10, ipady=5, pady=15)

NotesApp(root)

root.mainloop()
