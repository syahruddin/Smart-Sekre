from flask import Flask, request, jsonify,session, render_template, redirect, url_for, flash,abort, Markup
import requests
import os
app = Flask(__name__)
app.secret_key = 'ha21j3nhhi08jhfd88'
#session['logged_in'] = False

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        if request.form['password'] == 'kemahasiswaan' and request.form['username'] == 'lkitb':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Username/Password Salah!')
            return redirect(url_for('index'))
    else:
        if not session.get('logged_in'):
            return render_template('index.html')
        else:
            return redirect(url_for('view'))


@app.route('/view', methods=['POST','GET'])
def view():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        if request.method == 'GET':
            url = "https://apismartsekre.herokuapp.com/getstatus"
            data = requests.get(url).json()
            data = data[1]
            code = ""
            for i in data:
                code = code +"<tr><td>"+str(data[1])+"</td><td>"+str(data[2])+"</td><td>"+str(data[3])+"</td></tr>"

            return render_template('view.html',d = Markup(code))
        else:
            return redirect(url_for('logout'))

@app.route('/logout', methods=['POST','GET'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))


if __name__ == '__main__':

    app.run(threaded=True, port=5000)
