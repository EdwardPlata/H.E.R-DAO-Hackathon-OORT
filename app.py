import tkinter as tk
from tkinter import filedialog
from oortwrapper import OortWrapper

def on_drop(event):
    if event.data:
        files = root.tk.splitlist(event.data)
        for file in files:
            # Upload the file to the Oort bucket
            file_name = os.path.basename(file)
            with open(file, 'rb') as f:
                oort.put_object(bucket_name, file_name, f.read())

# Initialize the OortWrapper
oort = OortWrapper()

# Create a bucket or use an existing one
bucket_name = 'my-bucket'
if bucket_name not in oort.list_buckets():
    oort.create_bucket(bucket_name)

root = tk.Tk()
root.title("Oort Drag & Drop")

frame = tk.Frame(root, width=400, height=200)
frame.pack()

label = tk.Label(frame, text="Drag and drop files here")
label.pack(pady=20)

frame.drop_target_register(tk.DND_FILES)
frame.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
