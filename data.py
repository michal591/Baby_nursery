import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("children_center.db")
cursor = conn.cursor()

# Insert data into Groups table
groups = [(1, "0-1", "Shiri"), (2, "1-2 years", "Rivka"), (3, "2-3 years", "Ester")]
cursor.executemany("INSERT INTO Groups (id, age, teacher) VALUES (?, ?, ?)", groups)

# Insert data into Babies table
babies = [
    (1, "Ariel", 1.5, 333333333, 2),
    (2, "Michael", 0.5, 222222222, 1),
    (3, "Avital", 2.5, 111111111, 3),
    (4, "Shira", 1.8, 111222333, 2),
    (5, "Moti", 0.8, 222333444, 1),
    (6, "Efrat", 2.6, 333444555, 3),
]
cursor.executemany(
    "INSERT INTO Babies (id, name, age, id_number, fk_group) VALUES (?, ?, ?, ?, ?)",
    babies,
)

# Insert data into Activities table
activities = [
    (1, "7:00-8:15", "Reception of children and free play on the carpet", 2),
    (2, "8:15-8:45", "Breakfast", 2),
    (3, "8:45-9:45", "activity in motion", 2),
    (4, "9:45-10:15", "free game", 2),
    (5, "10:15-10:30", "the diaper", 2),
    (6, "10:30-11:00", "Exit to the yard", 2),
    (7, "11:00-11:30", "Assembly games", 2),
    (8, "11:30-12:00", "Lunch", 2),
    (9, "12:00-14:00", "rest", 2),
    (10, "14:00-14:15", "the diaper", 2),
    (11, "14:15-14:35", "Afternoon meal", 2),
    (12, "14:35-15:00", "Gymboree activity", 2),
    (13, "15:00-15:30", "free game", 2),
    (14, "15:30-15:45", "story time", 2),
    (15, "15:45-16:00", "Getting ready to leave", 2),
    (16, "7:00-8:15", "Reception of children and free play on the carpet", 3),
    (17, "8:15-8:45", "Breakfast", 3),
    (18, "8:45-9:45", "activity in motion", 3),
    (19, "9:45-10:15", "free game", 3),
    (20, "10:15-10:30", "the diaper", 3),
    (21, "10:30-11:00", "Exit to the yard", 3),
    (22, "11:00-11:30", "Assembly games", 3),
    (23, "11:30-12:00", "Lunch", 3),
    (24, "12:00-14:00", "rest", 3),
    (25, "14:00-14:15", "the diaper", 3),
    (26, "14:15-14:35", "Afternoon meal", 3),
    (27, "14:35-15:00", "Gymboree activity", 3),
    (28, "15:00-15:30", "free game", 3),
    (29, "15:30-15:45", "story time", 3),
    (30, "15:45-16:00", "Getting ready to leave", 3),
    (31, "7:00-8:15", "Reception of children", 1),
    (32, "8:15-9:00", "Breakfast", 1),
    (33, "9:00-10:00", "Time on the carpet", 1),
    (34, "10:00-10:30", "the diaper", 1),
    (35, "10:30-11:30", "Gymboree room/ activity on the carpet", 1),
    (36, "11:30-12:00", "Lunch", 1),
    (37, "12:00-14:00", "rest", 1),
    (38, "14:00-14:30", "the diaper", 1),
    (39, "14:30-15:00", "Exit to the yard", 1),
    (40, "15:00-15:30", "Afternoon meal", 1),
    (41, "15:30-16:00", "Free time on the carpet and getting ready to leave", 1),
]
cursor.executemany(
    "INSERT INTO Activities (id, time, activity, fk_group) VALUES (?, ?, ?, ?)",
    activities,
)

# Commit changes and close the connection
conn.commit()
conn.close()
