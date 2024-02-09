from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import os
application = Flask(__name__)

# Flask-Mail Configuration
mail_username = os.environ.get('MAIL_USERNAME')
mail_password = os.environ.get('MAIL_PASSWORD')

application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USE_SSL'] = True
application.config['MAIL_USERNAME'] = mail_username
application.config['MAIL_PASSWORD'] = mail_password

mail = Mail(application)


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        phone = request.form['phone']
        message = request.form['message']

        msg = Message(subject=subject, sender=mail_username, recipients=["kannanthuyavan@gmail.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash('Your message has been sent!', 'success')
        except Exception as e:
            flash(f'Something went wrong: {str(e)}', 'error')

        return render_template('index.html')

if __name__ == '__main__':
    application.secret_key = 'tkm19722000'
    application.run(debug=False)