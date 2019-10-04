from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# config db
conf = yaml.load(open("config.yaml"))

app.config["MYSQL_HOST"] = conf['mysql_host']
app.config["MYSQL_USER"] = conf['mysql_name']
app.config["MYSQL_PASSWORD"] = conf['mysql_password']
app.config["MYSQL_DB"] = conf['mysql_name']

mysql = MySQL(app)


@app.route("/")
def my_home():
    return render_template("index.html", title="My Portfolio")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(f"{page_name}.html", title="My Portfolio")


def save_data(data):
    if data["email"] and data["subject"] and data["message"] != "":
        try:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO Contacts(email, subject, message) VALUES(%s, %s, %s)",
                (email, subject, message),
            )
            mysql.connection.commit()
            cur.close()
        except:
            return "somthing worng wents"


@app.route("/submit-form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            if data["email"] and data["subject"] and data["message"] != "":
                save_data(data)
                return redirect("thanks")
            else:
                return redirect("404")
        except:
            return "somthing worng went"


# url for admin to see all contact messages
@app.route("/<string:admin>/<int:password>")
def get_data(admin, password):

    if admin == conf['url_name'] and password == conf['url_password']:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM Contacts")
        if resultValue > 0:
            userData = cur.fetchall()
            cur.close()
            return render_template("people.html", userData=userData)
    return "Somthing worng went"


if __name__ == '__main__':
    app.debug = True
    app.run()