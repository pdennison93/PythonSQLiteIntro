import sqlite3

conn = sqlite3.connect('store')
cursor = conn.execute("SELECT * FROM pet")

for row in cursor:
    print(f"Name: {row[0]}, Owner: {row[1]}, Species: {row[2]}, "
          f"Sex: {row[3]}, Checkups: {row[4]}, Birth: {row[5]}, Death: {row[6]}")

conn.close()

# conn = sqlite3.connect('store')
# conn.execute("UPDATE pet SET sex = 'm' WHERE name = 'Fluffy'")
# conn.commit()

# cursor = conn.execute("SELECT * FROM pet")
# for row in cursor:
#     print(row)

# conn.close()