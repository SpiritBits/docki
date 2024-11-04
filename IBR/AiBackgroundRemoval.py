import torch
import cv2
import numpy as np
from PIL import Image
from torchvision import transforms
from torch.autograd import Variable
from IBR.U2Net.model import U2NET  # Importiere das U^2-Net-Modell (sieh Hinweis unten)

import IBR.saved_models.u2net as u2net

# Laden des U^2-Net-Modells
model_path = "IBR/saved_models/u2net/u2net.pth"
model = U2NET(3, 1)
model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()

# Transformations für das Bild
transform = transforms.Compose([
    transforms.Resize((320, 320)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

def remove_background(image_path, output_path):
    # Bild laden und vorverarbeiten
    image = Image.open(image_path).convert("RGB")
    input_image = transform(image).unsqueeze(0)
    input_image = Variable(input_image)

    # Vorhersage erhalten
    with torch.no_grad():
        prediction = model(input_image)[0][:, 0, :, :].cpu().data.numpy()
    
    # Reshape und Maske normalisieren
    mask = prediction[0]
    mask = (mask - mask.min()) / (mask.max() - mask.min())
    mask = (mask * 255).astype(np.uint8)
    mask = cv2.resize(mask, (image.width, image.height))

    # Hintergrund entfernen
    original = np.array(image)
    bg_removed = cv2.bitwise_and(original, original, mask=mask)

    # Bild speichern
    cv2.imwrite(output_path, bg_removed)
    print(f"Bild mit entferntem Hintergrund gespeichert unter: {output_path}")
    return output_path

