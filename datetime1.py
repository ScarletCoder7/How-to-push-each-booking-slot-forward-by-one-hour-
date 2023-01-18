import mysql.connector as connector, datetime
connection = connector.connect(user = "root", password = "flash")
cursor = connection.cursor()
create_database = """CREATE DATABASE little_lemon8"""
cursor.execute(create_database)
cursor.execute("""USE little_lemon8""")
create_bookings_table = """CREATE TABLE bookings(GuestFirstName VARCHAR(200), GuestLastName VARCHAR(200), TableNo VARCHAR(100), BookingSlot TIME, EmployeeID INT, PRIMARY KEY(EmployeeID))"""
cursor.execute(create_bookings_table)
#Insert into table
mysql_insert_query = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, BookingSlot, EmployeeID) VALUES("Marcos", "LLorente", "2", "19:00", 5)"""
cursor.execute(mysql_insert_query)
connection.commit()

mysql_insert_query2 = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, BookingSlot, EmployeeID) VALUES("Tomiyu", "Nakamoto", "3", "19:15", 1)"""
cursor.execute(mysql_insert_query2)
connection.commit()

mysql_insert_query3 = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, bookingSlot, EmployeeID) VALUES("Sakura", "Nakamura", "1", "15:10", 2)"""
cursor.execute(mysql_insert_query3)
connection.commit()

read_data_query = """SELECT * FROM bookings"""
cursor.execute(read_data_query)
print(cursor.column_names)

for row in cursor:
    employee_id = row[4]
    booking_slot = row[3]
    new_booking_slot = booking_slot + datetime.timedelta(hours = 1)
    print("Booking slot for customer iD {} moved from {} to {}".format(employee_id, booking_slot, new_booking_slot))