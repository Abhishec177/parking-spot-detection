from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def home():
    if request.method == "POST":
        name = request.form["nm"]
        return redirect(url_for("user",name=name))
    else:
        return render_template("index.html")

@app.route('/<name>', methods=["POST","GET"])
def user(name):
    if request.method == "POST":
        image = request.form["img"]
        output = detect(image) #Function call to Parking Spot Detection Model
        return redirect(url_for("output",image=output))
    else:
        return render_template("home.html",name=name)

if __name__ == '__main__':
    app.run(debug=True)

def detect(img):
    return img