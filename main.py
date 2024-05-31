from flask import Flask, render_template, url_for, redirect, session
from flask_migrate import Migrate
from os import urandom
from db import db, User, Upload
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.secret_key = urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:12345@localhost:5432/road_to_python"
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/authorization", methods=["GET", "POST"])
def authorization():
    login = LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(nickname=login.username.data).first()
        if user and user.check_password(login.password.data):
            session["user_id"] = user.id
            return redirect(url_for("profile"))
        else:
            return render_template("authorization.html", form=login, message="Неверное имя пользователя или пароль")
    return render_template("authorization.html", form=login)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    registration = RegistrationForm()
    if registration.validate_on_submit():
        if User.query.filter_by(nickname=registration.username.data).first():
            return render_template("register.html", form=registration, message="Такой пользователь уже существует")
        user = User(nickname=registration.username.data, email=registration.email.data,
                    password=registration.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("authorization"))
    return render_template("register.html", form=registration)


@app.get("/profile")
def profile():
    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for("authorization"))


if __name__ == "__main__":
    app.run(debug=True)
