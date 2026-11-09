import sqlite3
connection = sqlite3.connect("okul.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT ,
    score INTEGER,
    student_id INTEGER
)
""")
sample_grades = [
    ("Mathematics",90,1),
    ("Physics",85,1),
    ("Chemistry",78,2),
    ("Biology",92,2),
]
cursor.executemany("""
INSERT INTO grades (course_name, score, student_id)
VALUES (?,?,?)
""",sample_grades)
connection.commit()
connection.close()
print("Table 'grades' created and records inserted successfully.")
