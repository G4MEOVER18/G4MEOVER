# NetzwerkAnalyseTool

Netzwerk-Analyse-Werkzeug mit grafischer Oberfläche (Python/Tkinter).

## Funktionen

- **WLAN-Scanner** – Zeigt alle Zugriffspunkte an: SSID, BSSID, Signalstärke, Kanal, Funkstandard, Band (2,4 GHz / 5 GHz / 6 GHz), Verschlüsselungsmethode, Basisraten
- **Netzwerkscanner** – Zeigt offen ersichtliche Geräte im lokalen Netzwerk an
- **Geräteübersicht** – Aufgebaut durch einen internen Netzwerkscan, der dynamisch das lokale Subnetz erkennt (z. B. `172.29.136.*`), alle IPs pingt und auswertet. Die MAC-zu-Hersteller-Auflösung erfolgt über eine lokal gepflegte OUI-Datenbank
- **Portscanner** – Zeigt offene Ports einer beliebigen IP oder eines Hostnamens an
- **DNS/WHOIS-Abfrage** – Ermittelt alle öffentlichen Informationen über eine IP-Adresse oder Webadresse

## Hinweise

- Scans können etwas Zeit in Anspruch nehmen – das Programm kann dabei kurz einfrieren (normal, Multithreading)
- Bei einigen Scans öffnet und schließt sich die Konsole für Sekundenbruchteile – das ist beabsichtigt
