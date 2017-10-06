import sqlite3
import re

#database handle
conn = sqlite3.connect('emaildb2.sqlite')
#a methood within the handle called cursor - used to execute queries
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    dmn = str(re.findall('@(\S+)',email))
    dmn = dmn.strip('[]').replace("'", "")

    # print("Email: ", email, "Domain is:", dmn.strip("[]")
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (dmn, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (dmn,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (dmn,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()