import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="distribuidora_brayan_sandoval"
)

cursor=db.cursor()
cursor.execute('SHOW DATABASES')
for dbs in cursor:
    print(dbs)

print('--------------------------------')
cursor.execute('SHOW TABLES')
for n in cursor:
    print(n)

cursor.execute("""insert into productos(categoria_id,marca_id,nombre,descripcion,imagen,precio,inventario,vendedor_id)values(3,1,'Bicicleta','rin28','023',2340000,12,1);""")
db.commit()

cursor.execute('select * from usuario')
for ap in cursor:
    print(ap(1))