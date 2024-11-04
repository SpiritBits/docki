const imageUpload = document.getElementById('imageUpload');
    const previewImage = document.getElementById('previewImage');
    const removeBackgroundButton = document.getElementById('removeBackgroundButton');

    // Vorschau des Bildes anzeigen
    imageUpload.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                previewImage.style.display = 'block';
                removeBackgroundButton.style.display = 'inline-block';
            };
            reader.readAsDataURL(file);
        }
    });

    // Hintergrund-Entfernungsprozess starten
    removeBackgroundButton.addEventListener('click', async function() {
        const file = imageUpload.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('image', file);

            try {
                const response = await fetch('/remove-background', {
                    method: 'POST',
                    body: formData
                });

                if (response.ok) {
                    const data = await response.blob();
                    const url = URL.createObjectURL(data);
                    previewImage.src = url;  // Aktualisiert das Bild mit der bearbeiteten Version
                } else {
                    console.error('Fehler beim Entfernen des Hintergrunds.');
                }
            } catch (error) {
                console.error('Netzwerkfehler:', error);
            }
        }
    });