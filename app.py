from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Dossier pour stocker les PDFs
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Route racine pour tester
# -----------------------------
@app.route('/', methods=['GET'])
def home():
    return "API Flask Upload Course fonctionne ✅"

# -----------------------------
# API 1 : Upload PDF (POST)
# -----------------------------
@app.route('/upload_course', methods=['POST'])
def upload_course():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "Aucun fichier reçu"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "Nom du fichier vide"})
    
    # Sauvegarde le fichier
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # Retourne JSON avec l’URL publique du fichier
    return jsonify({
        "success": True,
        "message": "Cours uploadé avec succès",
        "file_url": f"https://flask-upload-course-3.onrender.com/uploads/{file.filename}"
    })

# -----------------------------
# API 2 : Lister tous les PDFs (GET)
# -----------------------------
@app.route('/list_courses', methods=['GET'])
def list_courses():
    files = os.listdir(UPLOAD_FOLDER)
    file_urls = [f"https://flask-upload-course-3.onrender.com/uploads/{f}" for f in files]
    return jsonify(file_urls)

# -----------------------------
# Servir les fichiers PDF
# -----------------------------
@app.route('/uploads/<filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# -----------------------------
# Lancer l’application
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
