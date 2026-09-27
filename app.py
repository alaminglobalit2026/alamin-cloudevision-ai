import os
from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError
from google import genai

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB

STUDENT_NAME = "Al Amin"          # Change if needed
STUDENT_ID = "2026512806"
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def analyze_image(image_file):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    if not allowed_file(image_file.filename):
        raise ValueError("Please upload PNG, JPG, JPEG, or WEBP.")

    try:
        image = Image.open(image_file).convert("RGB")
    except UnidentifiedImageError:
        raise ValueError("The uploaded file is not a valid image.")

    client = genai.Client(api_key=api_key)

    prompt = """
You are an image-analysis assistant for a university cloud-computing project.
Analyze the uploaded image and return a concise, useful report with exactly
these four sections:

1. Scene
2. Main objects
3. Short description
4. Useful observation

Use simple English and stay under 180 words.
Do not identify or guess the identity of any person.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[image, prompt],
    )

    if not response.text:
        raise RuntimeError("The AI service returned an empty response.")

    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        image_file = request.files.get("image")

        if not image_file or not image_file.filename:
            error = "Please choose an image first."
        else:
            try:
                result = analyze_image(image_file)
            except Exception as exc:
                error = str(exc)

    return render_template(
        "index.html",
        result=result,
        error=error,
        student_name=STUDENT_NAME,
        student_id=STUDENT_ID,
    )

@app.get("/health")
def health():
    return {"status": "ok", "service": "CloudVision AI"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
