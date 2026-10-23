import sqlite3


conn = sqlite3.connect("StudentRecords.db")  
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS StudentRecords")

cur.execute("""
    CREATE TABLE StudentRecords
    (   ID     INT         NOT NULL,
        Name   VARCHAR(30) NOT NULL,
        Age    INT,
        Major  VARCHAR(20),
        PRIMARY KEY (ID) )
""")

students = [
    (1, "Maya",  18, "Biology"),
    (2, "Leo",   21, "History"),
    (3, "Priya", 20, "Computer Science"),
    (4, "Omar",  19, "Math"),
    (5, "Mia",   23, "Chemistry"),
]
cur.executemany("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)", students)
conn.commit()   


print("Students:")
for name, age, major in cur.execute("SELECT Name, Age, Major FROM StudentRecords"):
    print(name, "-", age, "-", major)


answer = input("\nDo you want to add a new student? (yes/no) ").strip().lower()
while answer != "yes" and answer != "no":
    print("Please type yes or no.")
    answer = input("Do you want to add a new student? (yes/no) ").strip().lower()

if answer == "yes":

 
    name = input("Name: ").strip()
    while name == "":
        print("The name cannot be empty.")
        name = input("Name: ").strip()

    
    age = None
    while age is None:
        text = input("Age: ").strip()
        try:
            age = int(text)
        except ValueError:
            print("The age must be a whole number.")
            continue
        if age < 0:
            print("The age cannot be negative.")
            age = None

    
    major = input("Major: ").strip()
    while major == "":
        print("The major cannot be empty.")
        major = input("Major: ").strip()

    
    cur.execute("SELECT MAX(ID) FROM StudentRecords")
    largest = cur.fetchone()[0]
    new_id = largest + 1

    cur.execute("INSERT INTO StudentRecords VALUES (?, ?, ?, ?)", (new_id, name, age, major))
    print("Student added.")

conn.commit() 
