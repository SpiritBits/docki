
from flask import Blueprint, request, jsonify, render_template, send_from_directory
import os


# File Download Service (FDS)
# Dieses Modul stellt die Dateien im Ordner app/static/FilesForDownloads zum Download bereit



FDS_BP = Blueprint('FDS',__name__)
@FDS_BP.route('/FDS',methods=["GET"])
def index():
    return render_template("template_FDS.html")

# Route, um die Liste der Dateien im Ordner 'static' zu laden
@FDS_BP.route('/files')
def list_files():
    print(os.getcwd())
    files = os.listdir(os.getcwd()+'/static/FilesForDownloads/')
    return jsonify(files)

# Route zum Herunterladen einer Datei
@FDS_BP.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(directory='static/FilesForDownloads', path=filename, as_attachment=True)