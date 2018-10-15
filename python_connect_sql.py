import pymssql


server  = 'mmmmm'
port = 'mmm'
user = 'user' #user name@server  eg:username@btdigitalsandbox.database.windows.net
password = 'password'
database = 'digitalsandbox'

#how to connect sql and python
conn = pymssql.connect(server=server,
    port = port,
    user='user',
    password=password,
    database='digitalsandbox')
cur = conn.cursor()

#Example of how to use the sql in python
cur.execute('SELECT TOP 10 m.ISBN, m.Market, m.CirculationWeek, h.ISBN FROM Axis360Circulation m, Axis360Hold h where m.ISBN = h.ISBN ')
row = cur.fetchall()
for i in row:
    print(i)