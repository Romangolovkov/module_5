from flask import Flask, render_template


app = Flask(__name__)


@app.route("/logo/<name>/<surname>/<int:age>")
def index(name, surname, age):
    if age % 10 == 1 and age != 11:
        return render_template("base.html", name=name, surname=surname, age=age, year='год')
    elif age % 10 in (2, 3, 4) and age not in (12, 13, 14):
        return render_template("base.html", name=name, surname=surname, age=age, year='года')
    else:
        return render_template("base.html", name=name, surname=surname, age=age, year='лет')



if __name__ == "__main__":
    app.run()