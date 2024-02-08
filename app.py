from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import os
app = Flask(__name__)

# Flask-Mail Configuration
mail_username = os.environ.get('MAIL_USERNAME')
mail_password = os.environ.get('MAIL_PASSWORD')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
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
    app.secret_key = 'your_secret_key'
    app.run(debug=True)