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

    def __init__(self, wurzel: tk.Tk) -> None:
        """Initialisiert das Hauptfenster, zentriert es und erstellt die Steuerelemente."""
        self.wurzel = wurzel
        self.wurzel.title("Erstes Programm")
        self._fenster_zentrieren()

        self.beschriftung = tk.Label(wurzel, text="", font=BESCHRIFTUNG_SCHRIFT)
        self.beschriftung.pack(pady=10)

        self.knopf_rahmen = tk.Frame(wurzel)
        self.knopf_rahmen.pack()

        self.symbol_reihenfolge = ["kreis", "dreieck"]
        self.knoepfe_erstellen()

    def _fenster_zentrieren(self) -> None:
        """Positioniert das Fenster in der Mitte des Bildschirms."""
        self.wurzel.update_idletasks()
        bildschirm_breite = self.wurzel.winfo_screenwidth()
        bildschirm_hoehe = self.wurzel.winfo_screenheight()
        x = (bildschirm_breite - FENSTER_BREITE) // 2
        y = (bildschirm_hoehe - FENSTER_HOEHE) // 2
        self.wurzel.geometry(f"{FENSTER_BREITE}x{FENSTER_HOEHE}+{x}+{y}")

    def knoepfe_erstellen(self) -> None:
        """Löscht alle vorhandenen Knöpfe und erstellt sie in der aktuellen Reihenfolge neu."""
        for widget in self.knopf_rahmen.winfo_children():
            widget.destroy()

        for symbol in self.symbol_reihenfolge:
            if symbol == "kreis":
                self.kreis_knopf = tk.Button(
                    self.knopf_rahmen, text="●", fg=FARBE_STANDARD,
                    font=SCHALTFLAECHE_SCHRIFT, width=SCHALTFLAECHE_BREITE
                )
                self.kreis_knopf.bind("<ButtonPress-1>", self.kreis_gedrueckt)
                self.kreis_knopf.bind("<ButtonRelease-1>", self.kreis_losgelassen)
                self.kreis_knopf.pack(side=tk.LEFT, padx=SCHALTFLAECHE_ABSTAND)
            elif symbol == "dreieck":
                self.dreieck_knopf = tk.Button(
                    self.knopf_rahmen, text="▲", fg=FARBE_STANDARD,
                    font=SCHALTFLAECHE_SCHRIFT, width=SCHALTFLAECHE_BREITE,
                    command=self.knoepfe_tauschen
                )
                self.dreieck_knopf.pack(side=tk.LEFT, padx=SCHALTFLAECHE_ABSTAND)

    def kreis_gedrueckt(self, ereignis: tk.Event) -> None:
        """Färbt den Kreis-Knopf grün und zeigt die Begrüssungsmeldung."""
        ereignis.widget.config(fg=FARBE_AKTIV)
        self.beschriftung.config(text=BEGRUESSUNGSTEXT)

    def kreis_losgelassen(self, ereignis: tk.Event) -> None:
        """Setzt die Farbe des Kreis-Knopfs auf Schwarz zurück."""
        ereignis.widget.config(fg=FARBE_STANDARD)

    def knoepfe_tauschen(self) -> None:
        """Vertauscht die Reihenfolge der Knöpfe."""
        self.symbol_reihenfolge.reverse()
        self.knoepfe_erstellen()


if __name__ == "__main__":
    wurzel = tk.Tk()
    programm = SymbolGUI(wurzel)
    wurzel.mainloop()
