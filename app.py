import string
from select import select
from flask import Flask, g, request, session, render_template, abort
from flask.helpers import url_for
import random, atexit
from datetime import timedelta, datetime, timezone
import requests, json
import re, sqlite3
from werkzeug.utils import redirect

server = Flask(__name__)

@server.route("/",methods=['POST', 'GET'])
def main():
    if request.method == 'GET':       
        options = ['Fortune Spell', 'Love Spell', 'Diarrhea Spell'] 
        return render_template('main.html',options=options)
    return redirect(url_for('success'))

@server.route("/success",methods=['GET','POST'])
def success():
    return render_template('success.html')

if __name__ == "__main__":
    server.run()  