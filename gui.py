# OLD - Don't Use

import tkinter as tk
import main

root = tk.Tk()
root.title("PlagiatChecker")
root.configure(bg='#0D1821')
root.geometry('1200x600')

def getTextInput():
    content=textExample.get("1.0","end")
    # content = result.replace("\n", "").split(".")[0:-1]
    plagiate = main.main(content)
    showPlagiate(plagiate)

def showPlagiate(plagiate):
    results = tk.Tk()
    for p in plagiate:
        label1 = tk.Text(results, width=150, height=5)
        label1.grid(row=plagiate.index(p), column=0)
        label1.insert("1.0", p[0])
        label1.config(state="disabled")

        label2 = tk.Text(results, width=50, height=5)
        label2.grid(row=plagiate.index(p), column=1)
        label2.insert("1.0", p[1])
        label2.config(state="disabled")

    
textExample=tk.Text(root, height=30, width=100)
textExample.insert('1.0', 'Klein trieb im Vorstand eine engere Verzahnung aller Unternehmensbereiche und eine leistungsfähige IT-Organisation voran. Anfang 2019 übernahm er vom bisherigen Vorstandsmitglied Bernd Leukert den Bereich der globalen SAP-Entwicklung und Auslieferung der Kernanwendungen, besonders S/4HANA, unter dem Titel „The Intelligent Enterprise“.[6]')

textExample.pack(pady=10)

btnRead=tk.Button(root, height=1, width=10, text="Read", command=getTextInput)
btnRead.pack()


root.mainloop()