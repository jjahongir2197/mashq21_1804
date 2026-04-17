from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def palindrome():

    if request.method == "POST":

        text = request.form["text"]

        if text == text[::-1]:
            return "Bu palindrom"

        else:
            return "Bu palindrom emas"

    return render_template("index.html")

app.run(debug=True)
