
from flask import Blueprint, request, jsonify, render_template, send_from_directory, Flask, request, send_file
import os
from IBR.AiBackgroundRemoval import remove_background
from PIL import Image  # Pillow Library für Bildverarbeitung (installiere mit `pip install pillow`)
import io

IBR_BP = Blueprint('IBR',__name__)

@IBR_BP.route('/remove-background', methods=['POST'])
def rb():
    file = request.files['image']
    #image = Image.open(file)
    
    # Beispielhafte Bildbearbeitung (hier: einfaches Konvertieren in Graustufen)
    #image = image.convert('L')

    # Bild in einen Bytestream speichern und zurücksenden
    #img_io = io.BytesIO()
    #image.save(img_io, 'PNG')
    #img_io.seek(0)

    ## Beispielverwendung
    img_io = remove_background(file, "output.png")
    
    return send_file(img_io, mimetype='image/png')





@IBR_BP.route('/IBR',methods=["GET"])
def index():
    return render_template("template_IBR.html")

