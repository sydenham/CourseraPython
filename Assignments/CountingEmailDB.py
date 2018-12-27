import sqlite3
import re

def main():
    conn = sqlite3.connect('emaildb.sqlite')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Counts')

    cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')

    fname = input('Enter file name: ')

    fh = open(fname)
    for line in fh:
        if not line.startswith('From: '): continue
        pieces = line.split()
        #re.findall zwraca liste temu wiec na koncu jest 0 aby wybrac sam string
        domain = (re.findall('@(.+)', pieces[1]))[0]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (domain,))
        conn.commit()

    # https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT org, count FROM Counts'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()

if __name__ == "__main__":
    main()