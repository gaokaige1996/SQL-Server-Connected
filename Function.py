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

#select data from OMNI, and seperate the database into 50 file with 100000 rows each. 
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

#select data from Patron table, and seperate the data base into small files with 100000 each.
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


for i in range(1,2715973,100000):
    Library(i)
    print(i, 'has finished')

 #select all the column name of a table
cur.execute("SELECT * FROM  CheckoutTransaction")
col_name_list = [tuple[0] for tuple in cur.description]
for i in col_name_list:
    print(i)

