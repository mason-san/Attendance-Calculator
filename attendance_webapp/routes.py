from flask import Blueprint, render_template, redirect, url_for, flash 
from flask_login import login_user, logout_user, login_required 
from models import db, User, bcrypt
from forms import RegistrationForms, LoginForm

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/register', methods=["GET", "POST"])
def register(): 
    form = RegistrationForms()
    if form.validate_on_submit():  
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account Created! You can now log in", "Success")
        login_user(user)
        return redirect(url_for("app_blueprint.home"))
    return render_template("register.html", form=form)

@app_blueprint.route('/login', methods=["GET", "POST"]) 
def login(): 
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): 
            login_user(user)
            flash("Login successful!", "Success")
            return redirect(url_for("app_blueprint.home"))
        else: 
            flash("Login Failed. Check your email and password", "Danger")
    return render_template("login.html", form=form)

@app_blueprint.route('/logout')
@login_required
def logout(): 
    logout_user()

    flash("You have been logged out.", "info")

    return redirect(url_for("app_blueprint.login"))

@app_blueprint.route('/')
def index(): 
    return render_template("dashboard.html") 

@app_blueprint.route('/home')
@login_required
def home():
    return render_template("home.html")