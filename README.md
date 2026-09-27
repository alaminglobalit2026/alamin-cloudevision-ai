# CloudVision AI — Assignment 01

## Project title
**CloudVision AI: A Render-Based Cloud Service with AI Image Analysis**

## Requirement mapping
- Home page contains student name and student ID.
- The application has a working AI-based feature.
- The AI feature uses an external API/token (Google Gemini API).
- The application is deployed as a cloud web service on Render.
- The interface is intentionally simple because the course is not focused on app development.

## Technology
- Frontend: HTML5, CSS3, JavaScript
- Backend: Python Flask
- AI: Google Gemini API
- Image handling: Pillow
- Cloud deployment: Render
- Production server: Gunicorn

## Local setup
1. Install Python 3.11+.
2. Run:
   `pip install -r requirements.txt`
3. Set:
   `GEMINI_API_KEY=YOUR_API_KEY`
4. Run:
   `python app.py`
5. Open `http://127.0.0.1:5000`

## Render deployment
Create a Render Web Service from the GitHub repository.

Build command:
`pip install -r requirements.txt`

Start command:
`gunicorn app:app`

Environment variables:
- `GEMINI_API_KEY` = your Gemini API key
- `GEMINI_MODEL` = `gemini-3.8-flash`

Never commit the real API key to GitHub.

## Important
Before submission, replace `2026512806` in `app.py` with the actual student ID and deploy the service successfully. Add the final Render URL to the report.


## Submission information
Student Name: Al Amin
Student ID: 2026512806
Assignment: 01
