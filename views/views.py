from flask import render_template, url_for, redirect, flash
from main import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from forms.register import ClientsRegistrationForm
from forms.login import LoginForm
from models.clients import Clients

app.config.from_object('configs.configs.DevelopmentConfig')

@app.before_first_request
def create_table():
    db.create_all()
    # db.drop_all()

# home/landing page route

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

# about us route

@app.route('/about_us')
def about_us():
    return render_template('about-us.html', title='About | Us')

# properties route

@app.route('/properties')
def properties():
    return render_template('properties.html', title='Properties')

# media route

@app.route('/media')
def media():
    return render_template('media.html', title = 'Media')

# contact us route

@app.route('/contact_us')
def contact_us():
    return render_template('contact-us.html', title = 'Contact | Us')

# register route

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = ClientsRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        client = Clients(firstName = form.firstName.data, lastName = form.lastName.data, username = form.username.data, 
                        email = form.email.data, mobile_number=form.mobile_number.data, password = hashed_password)
        db.session.add(client)
        db.session.commit()
        flash(f'Dear {form.firstName.data}, your account has been created successfully, now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

# login route

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        client = Clients.query.filter_by(email=form.email.data).first()
        if client and bcrypt.check_password_hash(client.password, form.password.data):
            login_user(client, remember=form.remember.data)
            flash(f'Dear {form.email.data}, you have successfully logged into your account, a list of properties should appear below for your site booking convenience, site still under development !!!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Invalid email or password, please try again !!!', 'danger')
    return render_template('login.html', title = 'Login', form=form)

# user account route

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title = 'Account')

# a user logout route

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# booking site visit route
    
@app.route('/book_visit', methods = ['GET', 'POST'])
@login_required
def book_visit():
    return render_template('book-visit.html', title = 'Book Visit')

