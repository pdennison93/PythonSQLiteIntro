import sqlite3

conn = sqlite3.connect('store')

conn.execute("DROP TABLE IF EXISTS pet")
conn.execute("""
    CREATE TABLE pet (
        name VARCHAR(20),
        owner VARCHAR(20),
        species VARCHAR(20),
        sex CHAR(1),
        checkups SMALLINT UNSIGNED,
        birth DATE,
        death DATE
    )
""")

conn.execute("INSERT INTO pet VALUES ('Fluffy','Harold','cat','f',5,'2001-02-04','')")
conn.execute("INSERT INTO pet VALUES ('Claws','Gwen','cat','m',2,'2000-03-17','')")
conn.execute("INSERT INTO pet VALUES ('Tiger','Sarah','cat','f',4,'2010-05-27','')")
conn.execute("INSERT INTO pet VALUES ('Cheep','Gwen','bird','m',2,'2000-03-17','2018-09-17')")



conn.commit()
print(f"Setup complete. {conn.total_changes} rows inserted.")
conn.close()