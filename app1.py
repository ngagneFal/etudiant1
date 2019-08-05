from flask import Flask, render_template ,url_for,request,redirect,flash,session,escape
from flask_sqlalchemy import SQLAlchemy
import datetime

#On donne ensuite un nom à l’application ici ce sera app
app = Flask(__name__)
#app.secret_key = "flash message"
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:ngagne03@localhost/isi1'
db = SQLAlchemy(app)
class students(db.Model):
    id_etudiant = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

#@app.route permet de préciser à quelle adresse ce qui suit va s’appliquer
@app.route('/')
def index():
    return render_template('index.html')

#def connexion():
if __name__ == "__main__":
    app.run(debug=True, port=5000)