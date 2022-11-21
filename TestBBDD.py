import sqlite3

conn = sqlite3.connect('ej1.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Nerea', 'Santos')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Coral', 'Moradas')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Miguel', 'Antoniez')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Francisco', 'Perez')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Jorge', 'Herrero')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Juan', 'Pedro')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Monica', 'Santamaria')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Pablo', 'Villanueva')")

conn.commit()

cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Maria'")

filas = cursor.fetchall()

print(filas)

conn.close()