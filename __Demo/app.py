from flask import Flask, render_template, request
import marks as mk

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def Hello():
    if request.method == "POST":
        text=request.form['text']
        frrom=request.form['from']
        to=request.form['to']
        test1=mk.translate(text,frrom,to)
        test2=test1
        return render_template("index.html", test3=test2)
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)