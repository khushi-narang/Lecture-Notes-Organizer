# Lecture Notes Organizer

A simple web application that helps organize lecture notes by converting images to searchable text using OCR technology.

## Features

- Upload images of lecture notes
- Extract text from images using OCR
- Tag notes for better organization
- Search through notes using keywords or tags
- Modern, responsive web interface

## Prerequisites

- Python 3.7+
- Tesseract OCR engine
- pip (Python package manager)

## Installation

1. Install Tesseract OCR:
   - Windows: Download and install from https://github.com/UB-Mannheim/tesseract/wiki
   - Make sure to add Tesseract to your system PATH

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload images of your lecture notes and add relevant tags

4. Use the search bar to find notes by content or tags

## Note

Make sure you have proper lighting and clear images for best OCR results.
