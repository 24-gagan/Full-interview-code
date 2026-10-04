"""
LibraryDB - Python se MySQL chalana
=====================================
Pehle apne computer par ye install karo (ek hi baar):
    pip install mysql-connector-python

Fir ye script chalao:
    python library_db.py
"""

import mysql.connector

# ------------------------------------------------------------------
# STEP 1: MySQL se connection banana
# ------------------------------------------------------------------
# Socho ye "phone call" jaisa hai - hum MySQL server ko call kar rahe
# hain apna username aur password batakar.
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akashdeep@1964",  # apna wahi password jo set kiya tha
)

# cursor = ek "pen" jisse hum MySQL ko commands likh kar bhejte hain
cursor = conn.cursor()

# ------------------------------------------------------------------
# STEP 2: Database aur Tables banana
# ------------------------------------------------------------------
cursor.execute("CREATE DATABASE IF NOT EXISTS LibraryDB")
cursor.execute("USE LibraryDB")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Members (
    MemberID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    JoinDate DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(200),
    Author VARCHAR(100),
    Publisher VARCHAR(100),
    Quantity INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS IssuedBooks (
    IssueID INT PRIMARY KEY,
    BookID INT,
    MemberID INT,
    IssueDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
)
""")

print("Database aur tables ban gaye!")

# ------------------------------------------------------------------
# STEP 3: Members ki entry karna
# ------------------------------------------------------------------
# executemany() ka matlab - ek saath kai rows daalna
members_data = [
    (1, "Amit Kumar", "amit@example.com", "2024-01-10"),
    (2, "Priya Sharma", "priya@example.com", "2024-02-15"),
]

# Pehle check karte hain ki data already to nahi hai (baar baar mat daalo)
cursor.execute("SELECT COUNT(*) FROM Members")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany("INSERT INTO Members VALUES (%s, %s, %s, %s)", members_data)
    conn.commit()  # commit() = "pakka save kar do, permanent kar do"
    print("Members add ho gaye!")
else:
    print("Members pehle se hain, dobara add nahi kiya.")

# ------------------------------------------------------------------
# STEP 4: Data dekhna (SELECT)
# ------------------------------------------------------------------
print("\n--- Members ki list ---")
cursor.execute("SELECT * FROM Members")
for row in cursor.fetchall():  # fetchall() = "sara result utha lo"
    print(row)

print("\n--- Books ki list ---")
cursor.execute("SELECT * FROM Books")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------------
# STEP 5: Kis member ne kaunsi kitab li (JOIN wala query)
# ------------------------------------------------------------------
print("\n--- Kisne kaunsi kitab li ---")
cursor.execute("""
    SELECT m.Name, b.Title, i.IssueDate, i.ReturnDate
    FROM IssuedBooks i
    JOIN Members m ON i.MemberID = m.MemberID
    JOIN Books b ON i.BookID = b.BookID
""")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------------
# STEP 6: Jo kitabein abhi tak wapas nahi aayin
# ------------------------------------------------------------------
print("\n--- Abhi tak wapas na aayi kitabein ---")
cursor.execute("""
    SELECT m.Name, b.Title, i.IssueDate
    FROM IssuedBooks i
    JOIN Members m ON i.MemberID = m.MemberID
    JOIN Books b ON i.BookID = b.BookID
    WHERE i.ReturnDate IS NULL
""")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------------
# STEP 7: Sabse zyada issue hui kitab
# ------------------------------------------------------------------
print("\n--- Sabse popular kitab ---")
cursor.execute("""
    SELECT b.Title, COUNT(*) AS TimesIssued
    FROM IssuedBooks i
    JOIN Books b ON i.BookID = b.BookID
    GROUP BY b.Title
    ORDER BY TimesIssued DESC
""")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------------
# STEP 8: Connection band karna
# ------------------------------------------------------------------
# Jaise phone call ke baad phone rakh dete hain, waise hi connection
# band karna zaroori hai.
cursor.close()
conn.close()
print("\nDone! Connection band ho gaya.")
