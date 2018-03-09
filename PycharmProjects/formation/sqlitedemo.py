import sqlite3

# sudo apt install sqlite3

conn = sqlite3.connect('jedis.sqlite3')

c = conn.cursor() # curseur pour pouvoir executer des commmandes sql
c.execute("""
CREATE TABLE IF NOT EXISTS jedis(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    prenom TEXT
)
""")

c.execute("INSERT INTO jedis (nom, prenom) VALUES ('SKYWALKER', 'Luke')")

nom = input("Nom : ")
prenom = input("Prénom : ")

# c.execute("INSERT INTO jedis (nom, prenom) VALUES ('{}', '{}')".format(nom, prenom))

# Nom : WINDU
# Prénom : Mace'); DELETE FROM jedis; --

c.execute("INSERT INTO jedis (nom, prenom) VALUES (?, ?)", (nom, prenom))

conn.commit()

c.execute("SELECT * FROM jedis")
for jedi in c:
    print(jedi[2])

conn.close()
