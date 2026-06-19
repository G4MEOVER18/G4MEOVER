# IT-Portfolio – Yanis Ameseder

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) ![Lizenz](https://img.shields.io/badge/Lizenz-MIT-green) ![Stand](https://img.shields.io/badge/Stand-Lernprojekt-orange)

## Inhalt

- [Über mich](#über-mich)
- [Technische Schwerpunkte](#technische-schwerpunkte)
- [Projekte](#projekte)
- [Projekte in Arbeit](#projekte-in-arbeit)
- [Wie starten](#wie-starten--mein-erstes-programm)
- [Ausbildung & Perspektive](#ausbildung--perspektive)
- [Lizenz](#lizenz)

## Über mich

**Selbstständiger Security-Denker & Systemanalyst** (ohne formale IT-Ausbildung)

Ich bin ein engagierter Quereinsteiger mit wachsender Spezialisierung auf IT-Systeme, Netzwerktechnologie und Cybersecurity. Der TECH-Track der Digital Talents Academy ab August 2026 dient als Sprungbrett für meine berufliche Neuorientierung.

Ich baue, teste und betreibe Systeme dort, wo Hardware, Netzwerke, Virtualisierung, Linux, Container, Embedded/IoT und lokale KI ineinandergreifen. Mein Stil ist: **Hypothese → Test → Logs → Fix → Dokumentation.**

Meine Kenntnisse kommen aus Projekten, die ich mir selbst aufgebaut habe: Homelab/Proxmox, KI-Stack, RAG-Workflows, Funk/Embedded (LoRa/BLE/GNSS), Debugging von Boot-/Update-Problemen und praxisnahe Netzwerk-Themen. Ich arbeite strukturiert, dokumentiere Entscheidungen, sammle Logs, baue reproduzierbare Setups und lerne sichtbar durch Debugging.

## Technische Schwerpunkte

- Python (GUI, Netzwerk, Automatisierung)
- Windows/Linux-Administration, Batch, PowerShell
- Virtualisierung & Betrieb: Proxmox, Hyper-V, VM-Design (UEFI/OVMF, Cloud-Init), saubere Storage-Trennung (OS vs. Daten)
- Linux & Services: systemd/OpenRC, Nginx Reverse Proxy, Docker/Compose, Logs/Healthchecks
- **Remote & Sicherheit:** Cloudflare Tunnel/Access, SSH key-only, „Remote-Zugriff darf nie verloren gehen” als Betriebsregel
- Lokale KI: Ollama + OpenWebUI, Tool-Server (REST), RAG-Ingest-Pipeline, klare Datenpfade/Caches
- IoT/Funk: ESP32-S3, LoRa (SX1262/SX1278), BLE, GNSS (u-blox NEO, ...), MQTT-Telemetrie
- WLAN-Scanner & Netzwerkanalyse mit OUI-Datenbank
- Diverse Firmware für Mikrocontroller
- Software-Builds mit PyInstaller & Signatur
- Cybersecurity, Systemhärtung, ethisches Hacking
- KI System mit Model-Orchestrierung und Modellquantisierung
- Multi-VM OpenClaw AI-Agentensystem auf Proxmox mit Gateway-Orchestrierung, isolierten Runner-VMs (Sandbox, Hardware-Flash, Admin), automatischer Cloud-Init-Provisionierung, Skill-Integration und sicherer Web-UI-Steuerung

## Projekte

- **Systemanalyse-Tool:** GUI-Export von Hardwaredaten, RAM/Mainboard/BIOS
- **NetzwerkAnalyseTool:** WLAN-/Portscanner mit Subnetzerkennung & OUI-Auflösung
- **BLE Beacon-Simulator:** Flipper Zero & ROG Ally mit Android/Discord-Integration
- **Infrastruktur-Lab:** Aufbau lokaler Server-Topologien mit virtuellen Maschinen
- Noch nicht umgesetzte Ideen werden nach Fertigstellung oder Publizierung ergänzt – sehr vieles in Arbeit!

## Projekte in Arbeit

- **ESP32-LCD-Time-SD-FTP:** ESP32‑S3 Dashboard mit Uhrzeit (NTP), SD‑Logging mit FTP-Server, webUI und Display
- **StoneBook:** Multi-KI-Analyse-und-Datenbank-Tool (für Edel-/Steine & Mineralien)
- **SmartTag:** Multi-Radio-LowPower-Tracker (derzeit nicht öffentlich)
- **RadioGateway:** RadioGateway-ESP32-MQTT-LoRa-Gateway
- **LoRa-868:** (derzeit nicht öffentlich)
- **LoRa-433:** (derzeit nicht öffentlich)
- **LinkVault-XIAO-Notes:** (derzeit nicht öffentlich)
- **ESP32S3-MiniPwn-Dashboard:** ESP32‑S3 Display‑Dashboard
- **SoundNode:** ESP-IDF Projekt (ESP32 cheap yellow display als MP3 Player)
- **TFT-AutoProbe:** Mini‑Sketch zum schnellen Verifizieren von TFT_eSPI Setup

## Wie starten – Mein Erstes Programm

```bash
# Python 3.8+ vorausgesetzt (tkinter ist im Standard-Lieferumfang enthalten)
python “Mein Erstes Programm/Fenster.py”
```

Das Fenster öffnet sich zentriert auf dem Bildschirm.

| Aktion | Maus | Tastatur |
|---|---|---|
| Begrüssung anzeigen | Kreis-Knopf gedrückt halten | `Leertaste` |
| Knöpfe tauschen | Dreieck-Knopf klicken | `Enter` |

![Screenshot](Mein%20Erstes%20Programm/Screenshot%202025-07-12%20023028.png)

## Ausbildung & Perspektive

Ab August 2026: Zertifikatslehrgang „Digital Talents Academy – TECH-Track”  
Gewerbliches Berufs- und Weiterbildungszentrum St.Gallen

## Lizenz

Dieses Repository steht unter der [MIT-Lizenz](LICENSE).
