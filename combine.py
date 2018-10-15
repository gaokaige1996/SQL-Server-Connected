import pymssql


server  = 'mmmmm'
port = 'mmm'
user = 'user' #user name@server  eg:username@btdigitalsandbox.database.windows.net
password = 'password'
database = 'digitalsandbox'

conn = pymssql.connect(server=server,
    port = port,
    user='user',
    password=password,
    database='digitalsandbox')
cur = conn.cursor()

def omni(low):
    cur.execute('SELECT BTkey,Title,Series, Author, EFormatCode,PubDate,LanguageCode,BisacCode,'
                'BisacDesc,AudienceCode,AudienceDesc, Annotation,ShortTitle,SubTitle '
                'FROM (SELECT ROW_NUMBER() OVER(ORDER BY (select NULL as noorder)) AS RowNum, *'
                'FROM OMNI ) as alias WHERE RowNum BETWEEN (%s) AND (%s)',(low,low+99999))
    rows = cur.fetchall()
    with open('OMNI_'+str(low)+'.txt', 'w') as f:
        for i in rows:
                i = str(i)
                #i= i.replace({'(':'',')':''})
                f.write(i+'\n')
def patron(low):
    cur.execute('SELECT ID, PatronUUID,LibraryID,Active, RemainedCheckOut,RemainingHold,OS,Device,AppVersion,GradeLevel '
                'FROM (SELECT ROW_NUMBER() OVER(ORDER BY (select NULL as noorder)) AS RowNum, * FROM patron ) as alias '
                'WHERE RowNum BETWEEN (%s) AND (%s)', (low, low + 99999))
    rows = cur.fetchall()
    with open('patron_' + str(low) + '.txt', 'w') as f:
        for i in rows:
            i = str(i)
            # i= i.replace({'(':'',')':''})
            f.write(i + '\n')
def Library(low):
    cur.execute('SELECT ItemID,LibraryID,TotalQuantity,OriginalQuantity,ConsortiaType,RTVFormats,HasCirculationLimit FROM '
            '(SELECT ROW_NUMBER() OVER(ORDER BY (select NULL as noorder)) AS RowNum, *'
                'FROM  LibraryInventory) as alias WHERE RowNum BETWEEN (%s) AND (%s)', (low, low +99999))
    rows = cur.fetchall()
    with open('library_' + str(low) + '.txt', 'w') as f:
        for i in rows:
            i = str(i)
            f.write(i + '\n')

def Checkout(low):
    cur.execute(
        'SELECT ID,PatronID,ItemID,LibraryID,FormatID,IsConsumed,ActionStartDate FROM '
        '(SELECT ROW_NUMBER() OVER(ORDER BY (select NULL as noorder)) AS RowNum, *'
        'FROM  CheckoutTransaction) as alias WHERE RowNum BETWEEN (%s) AND (%s)', (low, 134377))#14104628
    rows = cur.fetchall()
    with open('Checkout_' + str(low) + '.txt', 'w') as f:
        for i in rows:
            i = str(i)
            f.write(i + '\n')
#3177822
# cur.execute('select  count(distinct ID) from Patron')
# row = cur.fetchall()
# print(row)

for i in range(1,2715973,100000):
    Library(i)
    print(i, 'has finished')
cur.execute("SELECT * FROM  CheckoutTransaction")
col_name_list = [tuple[0] for tuple in cur.description]
for i in col_name_list:
    print(i)

def othertable(low):
    cur.execute(
        'SELECT ID,PatronID,ItemID,LibraryID,FormatID,IsConsumed,ActionStartDate FROM '
        '(SELECT ROW_NUMBER() OVER(ORDER BY (select NULL as noorder)) AS RowNum, *'
        'FROM  CheckoutTransaction) as alias WHERE RowNum BETWEEN (%s) AND (%s)', (low, 134377))
    rows = cur.fetchall()
    with open('Checkout_' + str(low) + '.txt', 'w') as f:
        for i in rows:
            i = str(i)
#             f.write(i + '\n')
# cur.execute(
#   #  'select  c.ID,c.PatronID,c.ItemID,o.BTKey,o.ISBN from CheckoutTransactionArchive c left join OMNI o on c.ItemID  = o.BTKey ')#134377
# rows = cur.fetchall()
# with open('Checkout_Archive.txt', 'w') as f:
#     for i in rows:
#         i = str(i)
#         f.write(i + '\n')

# cur.execute('SELECT TOP 10 m.ISBN, m.Market, m.CirculationWeek, h.ISBN FROM Axis360Circulation m, Axis360Hold h where m.ISBN = h.ISBN ')
# row = cur.fetchall()
# for i in row:
#     print(i)
# cur.execute("SELECT * FROM  Axis360Circulation")
# col_name_list = [tuple[0] for tuple in cur.description]
# for i in col_name_list:
#     print(i)
# select a.id, a.desc, b.id, b.name
# from parts a, custs b
# where a.rownum = b.rownum;