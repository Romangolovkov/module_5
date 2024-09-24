from flask import Flask, render_template



app = Flask(__name__)


@app.route("/multiple_of_3")
def multiple_of_3():
    return render_template("multiple_of_3.html", title='Числа от 1 до 50 кратные трём')


if __name__ == "__main__":
    app.run()