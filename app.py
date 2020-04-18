from flask import Flask, request, jsonify,session, render_template, redirect, url_for, flash,abort
import requests
from flask.ext.session import Session
import os
app = Flask(__name__)
sess = Session()

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
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
    app.secret_key = '500505'
    app.config['SESSION_TYPE'] = 'filesystem'
    # Threaded option to enable multiple instances for multiple user access support
    sess.init_app(app)
    app.run(threaded=True, port=5000)
