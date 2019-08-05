import psycopg2
con=psycopg2.connect (
    host= "localhost",
    database="isi",
    user="postgres",
    password="ngagne03",
    port ="5432"
)
#connection = psycopg2.connect(con)
cur=con.cursor()
#create table into sonatel1 from postgres Database

cur.execute(
"""CREATE TABLE etudiant (
            id_et SERIAL PRIMARY KEY,
            mat_et varchar,
            nom_et VARCHAR(255) NOT NULL,
            prenom_et VARCHAR(255) NOT NULL,
            date_nais DATE
)
""")

cur.execute(
"""CREATE TABLE filier (
            id_fi SERIAL PRIMARY KEY,
            libelle_fi VARCHAR(255) NOT NULL    
)
""")


cur.execute(
"""CREATE TABLE classe (
            id_clas SERIAL PRIMARY KEY,
            libelle VARCHAR(255) NOT NULL,
            montantins INTEGER,
            mensualite INTEGER,
            id_fi INTEGER,
            FOREIGN KEY (id_fi)
            REFERENCES filier (id_fi)
)
""")



cur.execute(
"""CREATE TABLE inscription (
            id_ins SERIAL PRIMARY KEY,
            date_nais DATE,
            anne_aca DATERANGE,
            id_et INTEGER,
            FOREIGN KEY (id_et)
            REFERENCES etudiant (id_et),
            id_clas INTEGER,
            FOREIGN KEY (id_clas)
            REFERENCES classe (id_clas)
            
            

)
""")



con.commit()
cur.close()



        

