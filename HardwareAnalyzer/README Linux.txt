Um die .py-Datei unter Linux direkt auszuführen:
Abhängigkeiten installieren (einmalig):

bash
Kopieren
Bearbeiten
sudo apt update
sudo apt install python3 python3-pip dmidecode
pip3 install psutil
Datei ausführbar machen (einmalig):

bash
Kopieren
Bearbeiten
chmod +x main.py
Starten:

bash
Kopieren
Bearbeiten
python3 main.py
Wenn du daraus ein .AppImage oder .deb bauen möchtest, wäre ein zusätzliches Packaging nötig – sag Bescheid, wenn du das willst. Ansonsten kannst du mit dem aktuellen Skript direkt unter Linux weiterarbeiten.
