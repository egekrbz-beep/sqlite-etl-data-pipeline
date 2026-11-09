import sqlite3

connection = sqlite3.connect("okul.db")
cursor = connection.cursor()

# SQL JOIN Query:
# We select student id, name, city, course name, and score.
# 's' aliases 'ogrenciler', 'g' aliases 'grades'.
query = """
SELECT 
    s.id,
    s.isim,
    s.sehir,
    g.course_name,
    g.score
FROM ogrenciler AS s
INNER JOIN grades AS g ON s.id = g.student_id
ORDER BY s.id ASC, g.score DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\n" + "=" * 55)
print(f"{'ID':<4} | {'NAME':<12} | {'CITY':<10} | {'COURSE':<14} | {'SCORE':<5}")
print("=" * 55)

for student_id, name, city, course, score in results:
    print(f"{student_id:<4} | {name:<12} | {city:<10} | {course:<14} | {score:<5}")

print("=" * 55 + "\n")

connection.close()