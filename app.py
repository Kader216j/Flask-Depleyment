from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", name="Abdul Kader", available=True)

@app.route("/about")
def about():
    skills = ["Python", "Flask", "HTML", "CSS", "JavaScript"]
    return render_template("about.html", skills=skills)

@app.route("/projects")
def projects():
    project_list = [
        {"title": "Invoice Generator", "desc": "Create and export PDF invoices"},
        {"title": "Inventory Manager", "desc": "Track stock and generate reports"},
        {"title": "Task Scheduler", "desc": "Add tasks and get reminders"},
    ]
    return render_template("projects.html", projects=project_list)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
