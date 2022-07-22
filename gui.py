import tkinter as tk

root = tk.Tk()
root.title("PlagiatChecker")
root.configure(bg='#0D1821')
root.geometry('1200x600')


def getTextInput():
    result=textExample.get("1.0","end")
    content = result.replace("\n", "").split(".")[0:-1]
    print(content)
    results = tk.Tk()
    
    

textExample=tk.Text(root, height=30, width=100)
textExample.pack(pady=10)
btnRead=tk.Button(root, height=1, width=10, text="Read", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()