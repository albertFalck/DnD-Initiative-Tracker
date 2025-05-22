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
* Fixa finare formattering av alla menyer i Control Panel fönstret (kanske använda "Frame" i tkinter?)

* Fixa så att jag kan ha som typ "presets" där jag kan lägga till karaktärer.

* Fixa bakgrund till delar av fönstret så att jag kan få det att se lite snyggare ut (främst spelarnas fönster).
    *   from PIL import ImageTk, Image
        myimg = ImageTk.PhotoImage(Image.open('myimage.png'))

* Fixa så att jag kan trycka på t.ex mellanslag för att köra "Next Turn". Även Enter för att köra "Add Combatant".

* Fixa så att jag kan track:a HP också
    * Ha att jag kan skriva in hur mycket HP en fiende har, så visas det i min Control Panel tabell men det visas lite annorlunda i Player Initiative fönstret.
        * För mig visas det typ "56/56 HP", för fiender visas "Unharmed" om en fiende har 100%-90% av ens HP kvar, sedan "Slightly Hurt" om den har 89%-60% HP kvar, sedan... Avrundar alltid uppåt.
    * Ha så att jag kan snabbt skriva in hur mycket skada en fiende har tagit. (Jag kanske kan select:a en rad och sedan skriva in den damage fienden tar?)
"""