
from flask import Flask, render_template, redirect, send_file, request, flash, url_for
import os

print("✅ Flask app script loaded.")

app = Flask(__name__)
app.secret_key = "your-secret-key"
GENERATED_REPORT_DIR = "chat_data/generated_reports"

@app.route("/")
def home():
    return redirect("/course_portal")

@app.route("/course_portal")
def course_portal():
    return render_template("generate_course.html")

@app.route("/download_course/<filename>")
def download_course(filename):
    file_path = os.path.join("static/generated_courses", filename)
    if os.path.exists(file_path):
        mimetype = None
        if filename.endswith('.docx'):
            mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        elif filename.endswith('.txt'):
            mimetype = 'text/plain'
        elif filename.endswith('.pptx'):
            mimetype = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        return send_file(file_path, as_attachment=True, mimetype=mimetype)
    return "File not found", 404

@app.route("/chat_data/<path:filename>") 
def serve_chatdata_file(filename):
    file_path = os.path.join("chat_data", filename)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        mimetype = None
        if filename.endswith('.docx'):
            mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        elif filename.endswith('.txt'):
            mimetype = 'text/plain'
        return send_file(file_path, as_attachment=True, mimetype=mimetype)
    return "File not found.", 404

if __name__ == "__main__":
    print("✅ Preparing necessary directories...")
    os.makedirs("chat_data/prompts", exist_ok=True)
    os.makedirs("chat_data/responses", exist_ok=True)
    os.makedirs("chat_data/raw_data", exist_ok=True)
    os.makedirs("chat_data/logs", exist_ok=True)
    os.makedirs(GENERATED_REPORT_DIR, exist_ok=True)
    os.makedirs("static/generated_courses", exist_ok=True)

    print("✅ About to start server on port 8002...")
    app.run(debug=True, port=8002)
