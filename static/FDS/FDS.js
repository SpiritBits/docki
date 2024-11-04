

// Funktion zum Laden und Anzeigen der Dateien
async function loadFiles() {
  try {
      const response = await fetch('/files');
      const files = await response.json();
      const fileList = document.getElementById('fileList');

      // Liste aller Dateien anzeigen
      files.forEach(file => {
          const listItem = document.createElement('li');
          const link = document.createElement('a');
          
          link.href = `/download/${file}`;
          link.textContent = file;
          link.setAttribute('download', file);  // Download-Attribut setzen

          listItem.appendChild(link);
          fileList.appendChild(listItem);
      });
  } catch (error) {
      console.error('Fehler beim Laden der Dateien:', error);
  }
}

// Dateien beim Laden der Seite abrufen
loadFiles();