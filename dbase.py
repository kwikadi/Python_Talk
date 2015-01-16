import sqlite3

con = sqlite3.connect('test.db')

def init():
	create_tables()
	insert_values()


def write(sql, values):
	""" Execute an Insert SQL Query. """
	con.cursor().execute(sql, values)
	con.commit()


def read(sql, values=None):
	""" Perform read operations on the databse. """

	result = None
	if values:
		cur = con.cursor().execute(sql, values)
	else:
		cur = con.cursor().execute(sql)

	result = cur.fetchall()
	return result

def insert_values():
	con.execute('''INSERT INTO LINK VALUES
						(,r'http://www.theverge.com', 'Computers'),
						(,r'http://www.wired.com', 'Music'),
						(,r'http://www.engadget.com', 'English'),
						(,r'http://www.reddit.com', 'English'),
						(,r'http://www.kickass.so', 'Computers'),
						(,r'http://www.thepiratebay.org', 'Maths'),
						(,r'http://www.youtube.com', 'Maths'),
						(,r'http://www.facebook.com', 'Science'),
						(,r'http://www.thisismynext.com', 'Science'),
						(,r'http://www.windowsphone.com', 'Music'),
						(,r'http://www.amazinglink.com', 'Computers'),
						(,r'http://www.randomsite.com', 'Science'),
						(,r'http://www.wowowow.com', 'English'),
						(,r'http://www.random.org', 'Maths'),
						(,r'http://www.samsung.com', 'Philosophy'),
						(,r'http://www.nokia.com', 'Philosophy'),
						(,r'http://www.gmail.com', 'Philosophy'),
						(,r'http://www.google.com', 'Maths'),
						(,r'http://www.thenextweb.com', 'Computers'),
						(,r'http://www.yahoo.com', 'Philosophy'),
						(,r'http://www.bangbang.com', 'English'),
						(,r'http://www.lalloo.com', 'Music'),
						(,r'http://www.digg.com', 'Music'),
						(,r'http://www.github.com', 'Science')
						);''')

def create_tables():
	con.execute('''CREATE TABLE IF NOT EXISTS LINKS
	       (ID	INTEGER	PRIMARY KEY	AUTOINCREMENT,
	       NAME	VARCHAR(200)	NOT NULL,
	       FIELD	VARCHAR(20)	NOT NULL);''')

