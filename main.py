from flask import Flask, render_template, redirect, request
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
