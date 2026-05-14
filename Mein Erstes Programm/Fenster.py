import tkinter as tk

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200
LABEL_FONT = ("Arial", 12)
BUTTON_FONT = ("Arial", 20)
BUTTON_WIDTH = 4
BUTTON_PADX = 10
COLOR_DEFAULT = "black"
COLOR_ACTIVE = "green"
GREETING_TEXT = "Hallo Yanis!"


class SymbolGUI:
    """Einfache Tkinter-GUI mit zwei Symbolen (Kreis und Dreieck).

    Der Kreis-Button zeigt beim Drücken eine Begrüssungsmeldung an
    und wechselt die Farbe. Der Dreieck-Button tauscht die Reihenfolge
    beider Buttons.
    """

    def __init__(self, root: tk.Tk) -> None:
        """Initialisiert das Hauptfenster, zentriert es und erstellt die Steuerelemente."""
        self.root = root
        self.root.title("Erstes Programm")
        self._center_window()

        self.label = tk.Label(root, text="", font=LABEL_FONT)
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.symbol_order = ["circle", "triangle"]
        self.create_buttons()

    def _center_window(self) -> None:
        """Positioniert das Fenster in der Mitte des Bildschirms."""
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w - WINDOW_WIDTH) // 2
        y = (screen_h - WINDOW_HEIGHT) // 2
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

    def create_buttons(self) -> None:
        """Löscht alle vorhandenen Buttons und erstellt sie in der aktuellen Reihenfolge neu."""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        for symbol in self.symbol_order:
            if symbol == "circle":
                self.circle_button = tk.Button(
                    self.button_frame, text="●", fg=COLOR_DEFAULT,
                    font=BUTTON_FONT, width=BUTTON_WIDTH
                )
                self.circle_button.bind("<ButtonPress-1>", self.circle_press)
                self.circle_button.bind("<ButtonRelease-1>", self.circle_release)
                self.circle_button.pack(side=tk.LEFT, padx=BUTTON_PADX)
            elif symbol == "triangle":
                self.triangle_button = tk.Button(
                    self.button_frame, text="▲", fg=COLOR_DEFAULT,
                    font=BUTTON_FONT, width=BUTTON_WIDTH,
                    command=self.swap_buttons
                )
                self.triangle_button.pack(side=tk.LEFT, padx=BUTTON_PADX)

    def circle_press(self, event: tk.Event) -> None:
        """Färbt den Kreis-Button grün und zeigt die Begrüssungsmeldung."""
        event.widget.config(fg=COLOR_ACTIVE)
        self.label.config(text=GREETING_TEXT)

    def circle_release(self, event: tk.Event) -> None:
        """Setzt die Farbe des Kreis-Buttons auf Schwarz zurück."""
        event.widget.config(fg=COLOR_DEFAULT)

    def swap_buttons(self) -> None:
        """Vertauscht die Reihenfolge der Buttons."""
        self.symbol_order.reverse()
        self.create_buttons()


if __name__ == "__main__":
    root = tk.Tk()
    app = SymbolGUI(root)
    root.mainloop()
