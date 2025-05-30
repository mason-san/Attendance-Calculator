from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, bcrypt, UserAttendance
from forms import RegistrationForms, LoginForm

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/register', methods=["GET", "POST"])
def register(): 
    
    form = RegistrationForms()

    if form.validate_on_submit():  
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        #Check if the user exists or not.
        existing_users = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if existing_users: 
            flash("Username or Email already exists. please try another", "danger")
            return render_template("register.html", form=form)

        user = User(username=form.username.data,email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account Created! You can now log in", "Success")
        login_user(user)
        session.permanent = True

        return redirect("/")

    return render_template("register.html", form=form)

@app_blueprint.route('/login', methods=["GET", "POST"]) 
def login(): 
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): 
            login_user(user)
            flash("Login successful!", "Success")
            return redirect("/")
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
@login_required
def index(): 
    return render_template("dashboard.html") 

"""app_blueprint.route('/home')
@login_required
def home():
    return render_template("dashboard.html")"""

#send subjects to front end dashboard.html
@app_blueprint.route('/get_subjects')
def get_subjects():
    if current_user.is_authenticated:
        data = UserAttendance.query.filter_by(user_id=current_user.id).all()
    else: 
        return redirect(url_for('app_blueprint.login'))
    subjects = [{
        "subject_name":s.name,
        "total_classes":s.total_classes,
        "attended_classes":s.attended_classes
    } for s in data]

    return jsonify(subjects)

#Adding only the last element from the database
@app_blueprint.route("/update_subject_card")
def update_subject_card():
    if current_user.is_authenticated:
        data = UserAttendance.query.filter_by(user_id = current_user.id).all()
    else: 
        return redirect(url_for("app_blueprint.login"))
    subject = [{
        "subject_name":s.name,
        "total_classes":s.total_classes,
        "attended_classes":s.attended_classes
    } for s in data]

    return jsonify(subject[-1])

@app_blueprint.route('/add_subject', methods=["POST"])
def add_subject():
    #Getting the data
    data = request.get_json()

    #All modal class data gotten from the front-end
    subject_name = data.get("subject_name")
    total_classes = data.get("total_classes")
    attended_classes = data.get("attended_classes")

    print(f"Received Data: {subject_name}, {total_classes}, {attended_classes}")
    #Getting the current user's id.
    current_user_id = current_user.id
    #Adding the data to database
    user_attendance = UserAttendance(
        user_id = current_user_id,
        name=subject_name,
        total_classes = total_classes,
        attended_classes = attended_classes
    )
    #Adding to database.
    db.session.add(user_attendance)
    db.session.commit()

    return jsonify({"message": "Subject Added Successfully!"}, 200)