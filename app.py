from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "✅ L'API fonctionne parfaitement (version simplifiée) !"

@app.route('/upload_course', methods=['POST'])
def upload_course():
    try:
        # Récupération du fichier PDF
        pdf = request.files.get('file')
        if not pdf:
            return jsonify({'error': 'Aucun fichier reçu'}), 400

        # Sauvegarde du fichier localement
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename)
        pdf.save(file_path)

        # Récupération des champs restants
        subject = request.form.get('subject')
        level = request.form.get('level')
        name = request.form.get('name')

        # (Tu pourras plus tard ajouter l'enregistrement dans Firebase ici)

        return jsonify({
            'message': 'Cours uploadé avec succès 🎉',
            'file_name': pdf.filename,
            'subject': subject,
            'level': level,
            'name': name
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
