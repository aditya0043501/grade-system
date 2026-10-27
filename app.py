from flask import Flask, request, render_template_string
app = Flask(__name__)
marks = []

HTML = """
<h2>Grade System v1 - Enter Marks (24MIS0058)</h2>
<form method="post">
  Subject: <input name="subject" required>
  Marks: <input name="mark" type="number" min="0" max="100" required>
  <button>Add</button>
</form>
<ul>{% for s, m in marks %}<li>{{ s }}: {{ m }}</li>{% endfor %}</ul>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        marks.append((request.form["subject"], int(request.form["mark"])))
    return render_template_string(HTML, marks=marks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
