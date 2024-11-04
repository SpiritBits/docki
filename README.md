# docki
Übungsserver

Docki ist ein Flask-Server, entwickelt, um verschiedene Module bereit zu stellen. In der ersten Version (1.0.0) stellt es ein Standard-Flask-Server mit zwei "Modulen" und einem Menü dar. 
Docki ist in erster Linie ein Übungsprojekt, mit viel Potential für einen vielseitigen Server zur Dateiverwaltung, Bildbearbeitung, Machine-Learning-Tasks oder auch ganz andere Aufgabenbereiche. Der Name leitet sich von Docker ab: Ziel dieses Projektes ist ein Server, der auf einem Docker-Container läuft und ständig im Hintergrund läuft und per Browser auf dem Port 5000 erreichbar ist.
In der ersten Version stellt es zwei Module bereit: Ein File-Download-Service (FDS), der Dateien im Ordner `app/static/FilesForDownload` im Browser in der Liste anzeigt und per Klick zum Download bereit stellt. Das zweite Modul ist ein Image-Background-Remover-Tool (IBR), welches über die U2Net models in Python Hintergründe aus Bildern entfernt. 
Noch ist es sehr rudimentär und benötigt noch enige Optimierungen, z.B. lässt sich dieses Tool noch mittels Task-Managements mit Celery als Hintergrundtask auslagern.

## Installation

# 1. Python Installation

```bash
git clone https://github.com/SpiritBits/docki.git
cd docki
pip install -r requirements.txt
```

Falls das Model für das IBR-Tools nicht erkannt wird, kann es mit folgendem Skript herunter geldaden werden:

```bash
python app/IBR/download_model.py
```


Mittels folgendem Befehl in der Konsole wird der Server gestartet:

```bash
python app/main.py
```

# 2.  Installation über docker

Docker Image erstellen

```bash
docker build -t Dockerfile
```

Docker Image Starten

```bash
docker run Dockerfile
```

# 3. Aufruf des Servers

Der Server ist local über den Browser mit 

`http://localhost:5000` erreichbar.





