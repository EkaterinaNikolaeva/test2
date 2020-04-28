from data import db_session
from flask import Flask, render_template, redirect, request
from loginform import LoginForm
from registerform import RegisterForm
import sqlite3
from PIL import Image
import io
import maps
import requests
import lxml.etree
from data import users
from flask_login import LoginManager, login_user, logout_user, login_required
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



def main():
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)




@app.route('/')
def root():
    return render_template("success.html")





if __name__ == '__main__':
    db_session.global_init("db/1.db")
    main()
