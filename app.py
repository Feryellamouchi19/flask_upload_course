from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# --------------------------
# Configuration Flask
# --------------------------
app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin depuis FlutterFlow

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --------------------------
# Route d’upload
# --------------------------
@app.route("/upload_course", methods=["POST"])
def upload_course():
    try:
        # Récupération du fichier PDF
        file = request.files.get("file")
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # URL publique pour Render
            file_url = f"https://flask-upload-course.onrender.com/uploads/{filename}"
        else:
            file_url = ""

        # Récupération des autres champs du formulaire
        matieres = request.form.get("matieres")
        type_ = request.form.get("type")
        level = request.form.get("level")
        name = request.form.get("name")
        price = request.form.get("price")

        # Réponse JSON
        return jsonify({
            "message": "Cours uploadé avec succès",
            "file_url": file_url,
            "matieres": matieres,
            "type": type_,
            "level": level,
            "name": name,
            "price": price
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# --------------------------
# Route principale (optionnel)
# --------------------------
@app.route("/", methods=["GET"])
def home():
    return "API UploadCourse en ligne 🚀"

# --------------------------
# Lancement de l’application
# --------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
