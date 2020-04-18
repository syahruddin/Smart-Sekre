from flask import Flask, request, jsonify,session, render_template, redirect, url_for, flash
import requests
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.methods == 'POST':
        if request.form['password'] == 'kemahasiswaan' and request.form['username'] == 'lkitb':
            session['logged_in'] = True
        else:
            flash('Username/Password Salah!')
        return index()
    else:
        if not session.get('logged_in'):
            return render_template('index.html')
        else:
            return viewSekre()


@app.route('/view', methods=['POST','GET'])
def viewSekre():
    return render_template('view.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
