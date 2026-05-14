import tkinter as tk


class SymbolGUI:
    """Einfache Tkinter-GUI mit zwei Symbolen (Kreis und Dreieck).

    Der Kreis-Button zeigt beim Drücken eine Begrüssungsmeldung an
    und wechselt die Farbe. Der Dreieck-Button tauscht die Reihenfolge
    beider Buttons.
    """

    def __init__(self, root: tk.Tk) -> None:
        """Initialisiert das Hauptfenster und die Steuerelemente."""
        self.root = root
        self.root.title("Erstes Programm")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="", font=("Arial", 12))
        self.label.pack(pady=10)

        # Initiale Button-Reihenfolge: Kreis, Dreieck
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.symbol_order = ["circle", "triangle"]
        self.create_buttons()

    def create_buttons(self) -> None:
        """Löscht alle vorhandenen Buttons und erstellt sie in der aktuellen Reihenfolge neu."""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        for symbol in self.symbol_order:
            if symbol == "circle":
                self.circle_button = tk.Button(
                    self.button_frame, text="●", fg="black", font=("Arial", 20), width=4
                )
                self.circle_button.bind("<ButtonPress-1>", self.circle_press)
                self.circle_button.bind("<ButtonRelease-1>", self.circle_release)
                self.circle_button.pack(side=tk.LEFT, padx=10)
            elif symbol == "triangle":
                self.triangle_button = tk.Button(
                    self.button_frame, text="▲", fg="black", font=("Arial", 20), width=4,
                    command=self.swap_buttons
                )
                self.triangle_button.pack(side=tk.LEFT, padx=10)

    def circle_press(self, event: tk.Event) -> None:
        """Färbt den Kreis-Button grün und zeigt die Begrüssungsmeldung."""
        event.widget.config(fg="green")
        self.label.config(text="Hallo Yanis!")

    def circle_release(self, event: tk.Event) -> None:
        """Setzt die Farbe des Kreis-Buttons auf Schwarz zurück."""
        event.widget.config(fg="black")

    def swap_buttons(self) -> None:
        """Vertauscht die Reihenfolge der Buttons."""
        self.symbol_order.reverse()
        self.create_buttons()

# Programm starten
if __name__ == "__main__":
    root = tk.Tk()
    app = SymbolGUI(root)
    root.mainloop()
