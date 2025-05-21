# Import Module
import tkinter as tk
import initiative_table as table

# create root window
root = tk.Tk()
# Set geometry(widthxheight)
root.geometry('1500x800')
# Initialize table with initiatives
app = table.InitiativeTracker(root)

# Execute Tkinter
root.mainloop()



"""Att göra:
* Fixa finare text för namn.
* Fixa så att namn text och initiative text visas i mitten av varje rad.
* Fixa så det är lite avstånd mellan varje rad?
* Fixa en counter för hur många rundor det har gått ("Round 1", sedan när vi når element 1 i listan igen: "Round 2"...)
* Fixa så att 
* Fixa så att jag kan ha som typ "presets" där jag kan lägga till karaktärer.
"""