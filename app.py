from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import requests
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/view', methods=['POST','GET'])
def viewSekre():
    return render_template('view.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
