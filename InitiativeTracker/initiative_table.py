import tkinter as tk
from tkinter import ttk

class InitiativeTracker:
    combatants = []
    turn_index = 0
    round_number = 1

    def __init__(self, root):
        self.root = root
        self.root.title("DM Control Panel")

        #           CONTROL PANEL

        # Adds some text and an input box where the user inputs text.
        tk.Label(root, text="Name:").pack(anchor="nw", padx=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(anchor="nw", padx=20, pady=10)

        # Same as above.
        tk.Label(root, text="Initiative:").pack(anchor="nw", padx=10)
        self.initiative_entry = tk.Entry(root)
        self.initiative_entry.pack(anchor="nw", padx=20, pady=10)

        # Adds a button which, when pressed, runs the method "add_combatant".
        self.add_button = tk.Button(root, text = "Add Combatant", command = self.add_combatant)
        self.add_button.pack(anchor="nw", side="left", padx=10)

        # Adds a button that can change the turn.
        self.next_turn_btn = tk.Button(root, text = "Next Turn", command = self.next_turn)
        self.next_turn_btn.pack(anchor="nw", side="left", padx=10)

        self.round_text = tk.StringVar()
        self.round_text.set("Round 1")
        self.round_counter = tk.Label(root, textvariable = self.round_text, anchor=tk.CENTER, justify="center", font=("Times New Roman", 20, "bold"))
        self.round_counter.pack(anchor="n", side="top", pady=20)

        # Creates a table with 2 columns: "Name" and "Initiative".
        self.main_table = ttk.Treeview(root, columns = ("Name", "Initiative"), show='headings')
        for col in ("Name", "Initiative"):
            self.main_table.heading(col, text=col)
            self.main_table.column(col, anchor="center")
        self.main_table.pack(fill = "both", expand = True)  # The table should fill out the screen in both X and Y.



        #           PLAYER WINDOW
        self.display_window = tk.Toplevel(self.root)  # Creates a new window for the players to see.
        self.display_window.title("Combat Initiative")

        self.round_counter = tk.Label(self.display_window, textvariable = self.round_text, anchor=tk.CENTER, justify="center", font=("Times New Roman", 26, "bold"))
        self.round_counter.pack(pady=20)

        # Same as above.
        self.display_table = ttk.Treeview(self.display_window, columns=("Name", "Initiative"), show='headings')
        for col in ("Name", "Initiative"):
            self.display_table.heading(col, text=col)
            self.display_table.column(col, anchor="center")
        self.display_table.pack(fill = "both", expand = True, padx=20, pady=20)


        style = ttk.Style()
        style.configure("Treeview.Heading", 
                        font=("Helvetica", 16, "italic"),
                        foreground="black")
        
        style.configure("Treeview", 
                font=("Century", 14), 
                rowheight=30)  # Makes rows taller for readability



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
                tree.see(item_id)
                tree.selection_set(item_id)


    def next_turn(self):
        # Update turn index and change whose turn it is.
        self.turn_index = (self.turn_index + 1) % len(self.combatants)
        # Update the "Round __" number if the next round is to start.
        if (self.turn_index == 0): 
            self.round_number += 1   # If we are to start over from the beginning of the list, then the next round is to start.
            self.round_text.set("Round " + str(self.round_number))
            print("New round has started. Round: " + str(self.round_number))
        self.refresh_tables()



    