from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/upload_course', methods=['POST'])
def upload_course():
    file = request.files.get('file')
    subject = request.form.get('subject')
    type_ = request.form.get('type')
    level = request.form.get('level')
    name = request.form.get('name')
    price = request.form.get('price')

    # Sauvegarde du fichier (optionnel)
    if file:
        filename = file.filename
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, filename))
    else:
        filename = None

    return jsonify({
        "message": "Cours uploadé avec succès",
        "file_name": filename,
        "subject": subject,
        "type": type_,
        "level": level,
        "name": name,
        "price": price
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
