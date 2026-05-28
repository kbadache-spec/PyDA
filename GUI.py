import tkinter as tk
import pyda

background_clr="#66545e"
entry_clr="#aa6f73"
txt_clr="#f6e0b5"

##Function for after hitting enter

def done(event):
    question=entry.get()
    entry.delete(0,tk.END)
    thinking.grid(column=0,row=2)
    window.update()
    answer = pyda.start(question)
    response.configure(text=answer)
    thinking.grid_forget()
    response.grid(column=0, row=2)
##window creation
window=tk.Tk()
window.geometry("1500x400")
window.configure(background=background_clr)
window.title("PyDA")
greeting=tk.Label(window, background=background_clr, text="Hey! What can I do for you today?", font=("sans-serif",16), fg=txt_clr )
greeting.grid(column=0,row=0, padx=400)

entry=tk.Entry(window, background=entry_clr, fg=txt_clr, font=("sans-serif",16), width=50, highlightbackground=background_clr, highlightcolor=background_clr)
entry.grid(column=0,row=1, padx=30)


##prepare response placeholder
response=tk.Label(window, background=background_clr, fg=txt_clr, font=("sans-serif"), wraplength=1200, padx=250,pady=100)
response.grid(column=0,row=2)
response.grid_forget()

##Thinking text
thinking=tk.Label(window,background=background_clr, fg=txt_clr, font=("sans-serif"), text="Thinking...")
thinking.grid(column=0,row=2)
thinking.grid_forget()

##take user input

entry.bind("<Return>", done)

window.mainloop()
