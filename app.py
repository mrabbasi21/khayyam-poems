from flask import Flask, render_template, abort
import yaml

app = Flask(__name__)

def load_poems():
    with open("data.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)["R"]

@app.route("/")
def index():
    poems = load_poems()
    return render_template("index.html", poems=poems)

@app.route("/poem/<int:pid>")
def show_poem(pid):
    poems = load_poems()
    poem = poems.get(pid)
    if not poem:
        abort(404)
    return render_template("poem.html", poem=poem, pid=pid)

if __name__ == "__main__":
    app.run(debug=False)
