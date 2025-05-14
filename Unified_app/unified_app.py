
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your-secret-key"

# 🗂️ Static + template paths setup (assuming unified folder layout)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(APP_ROOT, "kamimIntel_course_agent", "static")
TEMPLATE_DIR = os.path.join(APP_ROOT, "kamimIntel_course_agent", "templates")

ECO_STATIC = os.path.join(APP_ROOT, "Eecokaremaciu_travel", "assets")
ECO_PAGES = os.path.join(APP_ROOT, "Eecokaremaciu_travel", "pages")

# Mount both static folders
@app.route('/static/<path:filename>')
def custom_static(filename):
    path = os.path.join(STATIC_DIR, filename)
    if os.path.exists(path):
        return send_from_directory(STATIC_DIR, filename)
    return send_from_directory(ECO_STATIC, filename)

# Homepage route → EcoFrontier
@app.route("/")
def homepage():
    return send_from_directory(os.path.join(APP_ROOT, "Eecokaremaciu_travel"), "index.html")

# Serve EcoFrontier HTML pages (clean routing)
@app.route("/<page>")
def serve_page(page):
    html_path = os.path.join(ECO_PAGES, f"{page}.html")
    if os.path.exists(html_path):
        return send_from_directory(ECO_PAGES, f"{page}.html")
    return "Page not found", 404

# Include basic stub for generate_course, just a placeholder
@app.route("/generate_course", methods=["GET", "POST"])
def generate_course():
    if request.method == "POST":
        prompt = request.form.get("course_prompt", "")
        flash(f"Course generated for: {prompt}", "success")
        return redirect(url_for("generate_course"))
    return render_template("generate_course.html")  # should exist in kamimIntel_course_agent/templates/

# View courses - placeholder
@app.route("/courses")
def view_courses():
    course_dir = os.path.join(APP_ROOT, "kamimIntel_course_agent", "chat_data", "generated_courses")
    files = []
    for root, _, filenames in os.walk(course_dir):
        for fname in filenames:
            files.append({
                "name": fname,
                "path": os.path.relpath(os.path.join(root, fname), APP_ROOT),
                "time": datetime.fromtimestamp(os.path.getctime(os.path.join(root, fname))).strftime("%Y-%m-%d %H:%M")
            })
    return render_template("view_courses.html", courses=files)

# Add any other routes for chat, upload, reports, etc. as needed

if __name__ == "__main__":
    app.run(debug=True, port=8002, host="0.0.0.0")
