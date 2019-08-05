from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from sqlalchemy import func
import datetime
app = Flask(__name__)
app.secret_key = "flash message"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ngagne03@localhost/isi2'

db = SQLAlchemy(app)
############################################  creation des tables etudiant#####################
class Etudiant(db.Model):
    __tablename__ = 'Etudiant'
    id= db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String(100), unique=True,nullable = False)
    prenom = db.Column(db.String(200),nullable = False)
    nom = db.Column(db.String(200),nullable = False)
    email = db.Column(db.String(200),nullable = False)
    date_naiss = db.Column(db.Date)
   
    
    def __init__(self,matricule,prenom,nom,email,date_naiss):
        self.matricule =  matricule
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.date_naiss = date_naiss

    def __repr__(self):
        return '<Etudiant %r>'  
####################### filiere#####################
class filiere(db.Model):
    __tablename__ = 'filiere'
    id= db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(200))

    def __init__(self,libelle):
        self.libelle =   libelle


    def __repr__(self):
        return '<filiere %r>'% self.libelle     
#######################classe#####################       
class classe(db.Model):
    __tablename__ = 'classe'
    id= db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(200))
    montant_ins = db.Column(db.String(200))
    mensualite = db.Column(db.String(200))
    filiere_id=db.Column(db.Integer, db.ForeignKey('filiere.id'))
    

    def __init__(self,libelle,montant_ins, mensualite,filiere_id):
        self.libelle = libelle
        self.montant_ins = montant_ins
        self.mensualite =  mensualite
        self.filiere_id =  filiere_id
        

    def __repr__(self):
        return '<classe %r>'% self.libelle  

#######################inscription#####################       
class inscription(db.Model):
    __tablename__ = 'inscription'
    id= db.Column(db.Integer, primary_key=True)
    annee_acade = db.Column(db.String(200))
    date_ins = db.Column(db.Date)
    classe_id=db.Column(db.Integer, db.ForeignKey('classe.id'))
    Etudiant_id=db.Column(db.Integer, db.ForeignKey('Etudiant.id')) 
    

    def __init__(self,annee_acade,date_ins,classe_id,etudiant_id):
        self.annee_acade = annee_acade
        self.date_ins = date_ins
        self.classe_id =  classe_id
        self.etudiant_id =etudiant_id
        
    def __repr__(self):
        return '<inscription %r>'% self.annee_acade         
############################################ formulaire ###############################################################


@app.route('/')
def kha():
    
    
    etu=Etudiant.query.all()
    db.session.commit()

    fi=filiere.query.all()
    db.session.commit()

    clas=classe.query.all()
    db.session.commit()
     
    matricule=db.session.query(func.max(Etudiant.id)).one()

    if matricule[0] == None:
        num=1
        val='-'+str(num)
        naf = "SA"+val
    else:
        num=matricule[0]+2
        val='-'+str(num)
        naf="SA"+val
    return render_template('index.html',clas=clas,etu=etu,naf=naf,fi=fi)


#####################################################################
@app.route('/' , methods=['GET','POST'])
def insertion():
  

    if request.method == 'POST':
    
        if not request.form['nom'] or not request.form['prenom']  or not request.form['date_nais'] :
            flash('Please enter all the fields', 'error')
        else:
            Etudiants = Etudiant(request.form['matricule'], request.form['nom'], request.form['prenom'], request.form['email'], request.form['date_nais'])
            db.session.add(Etudiants)
            db.session.commit()
            flash('Record was successfully added')

    return redirect(url_for('kha'))



if __name__ == '__main__':
    app.run(debug=True)