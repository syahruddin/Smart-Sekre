from flask import Flask, request, jsonify,session, render_template, redirect, url_for, flash,abort
import requests
import os
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        if request.form['password'] == 'kemahasiswaan' and request.form['username'] == 'lkitb':
            session['logged_in'] = True
            return index()
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
    app.secret_key = os.urandom(12)
    app.run(threaded=True, port=5000)
