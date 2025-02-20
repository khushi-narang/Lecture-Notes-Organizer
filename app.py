from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
import pytesseract
import json
from werkzeug.utils import secure_filename

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Store notes in a simple JSON file
NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    tags = request.form.get('tags', '').split(',')
    tags = [tag.strip() for tag in tags if tag.strip()]
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    # Extract text from image using OCR
    try:
        image = Image.open(filepath)
        text = pytesseract.image_to_string(image)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Save note data
    notes = load_notes()
    note = {
        'filename': filename,
        'text': text,
        'tags': tags,
        'filepath': filepath
    }
    notes.append(note)
    save_notes(notes)
    
    return jsonify({'success': True, 'text': text})

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '').lower()
    notes = load_notes()
    
    results = []
    for note in notes:
        if (query in note['text'].lower() or 
            any(query in tag.lower() for tag in note['tags'])):
            results.append(note)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
