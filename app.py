import datetime
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Création de notre DB
def init_db():
    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()

    # Création des tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS livres
        (id INTEGER PRIMARY KEY,
        Titre TEXT NOT NULL,
        auteur TEXT NOT NULL,
        annee INTEGER NOT NULL)
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS lecteurs
        (id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL)
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS emprunts
        (id INTEGER PRIMARY KEY,
        id_livre INTEGER,
        id_lecteur INTEGER,
        date_emprunt DATE,
        date_retour DATE)
    ''')

    livres = [
        (1, 'Une si longue lettre', 'Mariama Ba', 1979),
        (2, 'Les bouts de bois de Dieu', 'Ousamane Sembene', 1960),
        (3, 'Le Baobab fou', 'Ken Bugul', 1982),
        (4, 'Le soleil des indépendances', 'Ahmadou Kourouma', 1968)
    ]

    lecteurs = [
        (1, 'Isabelle Olive', 'Kantoussan'),
        (2, 'Gomis', 'Pierre'),
        (3, 'Faye', 'Lorie'),
        (4, 'Diatta', 'Marie-Louise')
    ]

    c.executemany('INSERT OR REPLACE INTO livres VALUES (?, ?, ?, ?)', livres)
    c.executemany('INSERT OR REPLACE INTO lecteurs VALUES (?, ?, ?)', lecteurs)

    conn.commit()
    conn.close()

init_db()

# Route principale
@app.route('/')
def index():
    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()
    c.execute('SELECT * FROM livres')
    livres = c.fetchall()
    c.execute('SELECT * FROM lecteurs')
    lecteurs = c.fetchall()
    conn.close()
    return render_template('index.html', livres=livres, lecteurs=lecteurs)

# Méthode pour emprunter un livre
@app.route('/emprunter', methods=['POST'])
def emprunter_livre():
    data = request.get_json()
    id_livre = data['id_livre']
    id_lecteur = data['id_lecteur']

    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()

    date_emprunt = datetime.datetime.now().strftime('%Y-%m-%d')

    c.execute('''
        INSERT INTO emprunts (id_livre, id_lecteur, date_emprunt)
        VALUES (?, ?, ?)
    ''', (id_livre, id_lecteur, date_emprunt))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Livre emprunté avec succès'})

@app.route('/retourner/<int:livre_id>', methods=['PUT'])
def retourner_livre(livre_id):
    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()

    date_retour = datetime.datetime.now().strftime('%Y-%m-%d')
    c.execute('''
        UPDATE emprunts
        SET date_retour = ? WHERE id_livre = ?
        AND date_retour IS NULL
    ''', (date_retour, livre_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Livre retourné avec succès'})

if __name__ == '__main__':
    app.run(debug=True)
import datetime
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Création de notre DB
def init_db():
    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()

    # Création des tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS livres
        (id INTEGER PRIMARY KEY,
        Titre TEXT NOT NULL,
        auteur TEXT NOT NULL,
        annee INTEGER NOT NULL)
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS lecteurs
        (id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL)
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS emprunts
        (id INTEGER PRIMARY KEY,
        id_livre INTEGER,
        id_lecteur INTEGER,
        date_emprunt DATE,
        date_retour DATE)
    ''')

    livres = [
        (1, 'Une si longue lettre', 'Mariama Ba', 1979),
        (2, 'Les bouts de bois de Dieu', 'Ousamane Sembene', 1960),
        (3, 'Le Baobab fou', 'Ken Bugul', 1982),
        (4, 'Le soleil des indépendances', 'Ahmadou Kourouma', 1968)
    ]

    lecteurs = [
        (1, 'Isabelle Olive', 'Kantoussan'),
        (2, 'Gomis', 'Pierre'),
        (3, 'Faye', 'Lorie'),
        (4, 'Diatta', 'Marie-Louise')
    ]

    c.executemany('INSERT OR REPLACE INTO livres VALUES (?, ?, ?, ?)', livres)
    c.executemany('INSERT OR REPLACE INTO lecteurs VALUES (?, ?, ?)', lecteurs)

    conn.commit()
    conn.close()

init_db()

# Route principale
@app.route('/')
def index():
    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()
    c.execute('SELECT * FROM livres')
    livres = c.fetchall()
    c.execute('SELECT * FROM lecteurs')
    lecteurs = c.fetchall()
    conn.close()
    return render_template('index.html', livres=livres, lecteurs=lecteurs)

# Méthode pour emprunter un livre
@app.route('/emprunter', methods=['POST'])
def emprunter_livre():
    data = request.get_json()
    id_livre = data['id_livre']
    id_lecteur = data['id_lecteur']

    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()

    date_emprunt = datetime.datetime.now().strftime('%Y-%m-%d')

    c.execute('''
        INSERT INTO emprunts (id_livre, id_lecteur, date_emprunt)
        VALUES (?, ?, ?)
    ''', (id_livre, id_lecteur, date_emprunt))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Livre emprunté avec succès'})

@app.route('/retourner/<int:livre_id>', methods=['PUT'])
def retourner_livre(livre_id):
    conn = sqlite3.connect('bibliotheque.db')
    c = conn.cursor()

    date_retour = datetime.datetime.now().strftime('%Y-%m-%d')
    c.execute('''
        UPDATE emprunts
        SET date_retour = ? WHERE id_livre = ?
        AND date_retour IS NULL
    ''', (date_retour, livre_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Livre retourné avec succès'})

if __name__ == '__main__':
    app.run(debug=True)
