# **Lecture Notes Organizer**  

## **Overview**  
The Lecture Notes Organizer is a Flask-based web application designed to help students digitize and efficiently organize their handwritten lecture notes. It utilizes Tesseract OCR to extract text from images, enabling quick searches across notes and tags. The application features a modern, intuitive interface built with Tailwind CSS and stores all notes locally in a JSON file, ensuring ease of use without requiring a database.  

## **Features**  
- **OCR-Based Text Extraction:** Converts handwritten notes into searchable text using Tesseract OCR.  
- **Tagging System:** Allows users to organize notes with custom tags for better categorization.  
- **Advanced Search:** Enables searching across extracted text and tags for quick content retrieval.  
- **Minimalist and Lightweight:** No database required; all notes are stored locally in JSON format.  
- **Modern UI:** Built with Flask and Tailwind CSS for a clean and responsive user experience.  

## **Technology Stack**  
- **Backend:** Flask (Python)  
- **OCR:** Tesseract OCR  
- **Frontend:** Tailwind CSS, JavaScript  
- **Storage:** JSON (local storage)  

## **Installation & Usage**  
1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/lecture-notes-organizer.git
   cd lecture-notes-organizer
   ```  
2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  
3. Run the application:  
   ```sh
   python app.py
   ```  
4. Access the web app at `http://127.0.0.1:5000` in your browser.  

## **Future Enhancements**  
- Cloud-based storage for cross-device access.  
- Handwriting recognition improvements for better accuracy.  
- User authentication for personalized note management.  

This project provides a simple yet effective solution for students looking to digitize and manage their lecture notes effortlessly.
