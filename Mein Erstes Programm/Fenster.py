import tkinter as tk

FENSTER_BREITE = 300
FENSTER_HOEHE = 200
BESCHRIFTUNG_SCHRIFT = ("Arial", 12)
SCHALTFLAECHE_SCHRIFT = ("Arial", 20)
SCHALTFLAECHE_BREITE = 4
SCHALTFLAECHE_ABSTAND = 10
FARBE_STANDARD = "black"
FARBE_AKTIV = "green"
BEGRUESSUNGSTEXT = "Hallo Yanis!"


class SymbolGUI:
    """Einfache Tkinter-GUI mit zwei Symbolen (Kreis und Dreieck).

    Der Kreis-Knopf zeigt beim Drücken eine Begrüssungsmeldung an
    und wechselt die Farbe. Der Dreieck-Knopf tauscht die Reihenfolge
    beider Knöpfe.
    """

    def __init__(self, root: tk.Tk) -> None:
        """Initialisiert das Hauptfenster, zentriert es und erstellt die Steuerelemente."""
        self.root = root
        self.root.title("Erstes Programm")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        self._center_window()

        self.label = tk.Label(root, text="", font=BESCHRIFTUNG_SCHRIFT)
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.symbol_order = ["kreis", "dreieck"]
        self.create_buttons()

        self.root.bind("<space>", self._tastatur_kreis)
        self.root.bind("<Return>", lambda e: self.swap_buttons())

    def _center_window(self) -> None:
        """Positioniert das Fenster in der Mitte des Bildschirms."""
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w - FENSTER_BREITE) // 2
        y = (screen_h - FENSTER_HOEHE) // 2
        self.root.geometry(f"{FENSTER_BREITE}x{FENSTER_HOEHE}+{x}+{y}")

    def create_buttons(self) -> None:
        """Löscht alle vorhandenen Knöpfe und erstellt sie in der aktuellen Reihenfolge neu."""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        for symbol in self.symbol_order:
            if symbol == "kreis":
                self.circle_button = tk.Button(
                    self.button_frame, text="●", fg=FARBE_STANDARD,
                    font=SCHALTFLAECHE_SCHRIFT, width=SCHALTFLAECHE_BREITE
                )
                self.circle_button.bind("<ButtonPress-1>", self.circle_press)
                self.circle_button.bind("<ButtonRelease-1>", self.circle_release)
                self.circle_button.pack(side=tk.LEFT, padx=SCHALTFLAECHE_ABSTAND)
            elif symbol == "dreieck":
                self.triangle_button = tk.Button(
                    self.button_frame, text="▲", fg=FARBE_STANDARD,
                    font=SCHALTFLAECHE_SCHRIFT, width=SCHALTFLAECHE_BREITE,
                    command=self.swap_buttons
                )
                self.triangle_button.pack(side=tk.LEFT, padx=SCHALTFLAECHE_ABSTAND)

    def _tastatur_kreis(self, event: tk.Event) -> None:
        """Simuliert Kreis-Drücken und -Loslassen via Leertaste."""
        if hasattr(self, "circle_button"):
            self.circle_button.config(fg=FARBE_AKTIV)
            self.label.config(text=BEGRUESSUNGSTEXT)
            self.root.after(150, lambda: self.circle_button.config(fg=FARBE_STANDARD))

    def circle_press(self, event: tk.Event) -> None:
        """Färbt den Kreis-Knopf grün und zeigt die Begrüssungsmeldung."""
        event.widget.config(fg=FARBE_AKTIV)
        self.label.config(text=BEGRUESSUNGSTEXT)

    def circle_release(self, event: tk.Event) -> None:
        """Setzt die Farbe des Kreis-Knopfs auf Schwarz zurück."""
        event.widget.config(fg=FARBE_STANDARD)

    def swap_buttons(self) -> None:
        """Vertauscht die Reihenfolge der Knöpfe."""
        self.symbol_order.reverse()
        self.create_buttons()


if __name__ == "__main__":
    root = tk.Tk()
    app = SymbolGUI(root)
    root.mainloop()
