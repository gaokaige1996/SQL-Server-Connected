import pymssql

#select bookid and author from checkout transaction Archive table, 
#Aim to seperate author based on the past 3 year transaction data. 
#if the book written by the author has a lot of checkouts, we can assume that the author
# is a famouse author.
conn = pymssql.connect(server='btdigitalsandbox.database.windows.net',
    port = '1433',
    user='Dbadmin@btdigitalsandbox.database.windows.net',
    password='BT!pw0915',
    database='digitalsandbox')
cur = conn.cursor()
cur.execute("select  c.ItemID, o.Author from CheckoutTransactionArchive c left join OMNI o on c.ItemID = o.BTkey "
            "where cast(ActionStartDate as Date) between '20150701' and '20180630'")
rows = cur.fetchall()
with open('authorid.txt','w')as f:
    for row in rows:
        id = row[0]
        author = row[1]
        f.write(str(id) + '|'+str(author) + '\n')
