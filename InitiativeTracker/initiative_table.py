import tkinter as tk
from tkinter import ttk

class InitiativeTracker:
    combatants = []
    turn_index = 0
    active_combatant = ""

    def __init__(self, root):
        self.root = root
        self.root.title("DM Control Panel")

        #           CONTROL PANEL

        # Adds some text and an input box where the user inputs text.
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # Same as above.
        tk.Label(root, text="Initiative:").pack()
        self.initiative_entry = tk.Entry(root)
        self.initiative_entry.pack()

        # Adds a button which, when pressed, runs the method "add_combatant".
        self.add_button = tk.Button(root, text = "Add Combatant", command = self.add_combatant)
        self.add_button.pack()

        # Adds a button that can change the turn.
        self.next_turn_btn = tk.Button(root, text = "Next Turn", command = self.next_turn)
        self.next_turn_btn.pack()

        # Creates a table with 2 columns: "Name" and "Initiative".
        self.main_table = ttk.Treeview(root, columns = ("Name", "Initiative"), show='headings')
        for col in ("Name", "Initiative"):
            self.main_table.heading(col, text=col)
        self.main_table.pack(fill = "both", expand = True)  # The table should fill out the screen in both X and Y.



        #           PLAYER WINDOW
        self.display_window = tk.Toplevel(self.root)  # Creates a new window for the players to see.
        self.display_window.title("Combat Initiative")

        # Same as above.
        self.display_table = ttk.Treeview(self.display_window, columns=("Name", "Initiative"), show='headings')
        for col in ("Name", "Initiative"):
            self.display_table.heading(col, text=col)
        self.display_table.pack(fill = "both", expand = True)


    # The method that runs when the "Add" button is pressed.
    def add_combatant(self):
        # Get the value of the "Name: " text field.
        name = self.name_entry.get()
        try:
            # Same for the "Initiative: " text field.
            initiative = int(self.initiative_entry.get())
        except ValueError:
            return

        # Add the new combatant to the "combatants" list.
        self.combatants.append((name, initiative))

        # If there is no combatant in the list, then this newly added one becomes the one whose turn it is.
        if len(self.combatants) == 0: self.active_combatant = name

        # Sort the "combatants" list so that the one with the highest "initiative" value comes first.
        self.combatants.sort(key=lambda x: -x[1])  # Sort descending by initiative

        self.refresh_tables()


    def refresh_tables(self):
        # For both trees/tables...
        for tree in [self.main_table, self.display_table]:
            # Get each child in the tree/table...
            for row in tree.get_children():
                # Delete each row in the table.
                tree.delete(row)

            # Then, add them all back again, but in the updated order (and if a new child has been added).
            for name, initiative in self.combatants:
                tree.insert("", "end", values=(name, initiative))

            # After refreshing all tables, change to the correct turn.
            if 0 <= self.turn_index < len(tree.get_children()):
                item_id = tree.get_children()[self.turn_index]
                tree.see(item_id)   # Makes sure the row whose turn it is, is visible in the window.
                tree.selection_set(item_id) # "Selects" the row whose turn it is.


    def next_turn(self):
        self.turn_index = (self.turn_index + 1) % len(self.combatants)
        self.refresh_tables()



    