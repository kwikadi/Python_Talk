import sqlite3

con = sqlite3.connect('test.db', check_same_thread=False)


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
        cur = con.cursor().execute(sql, (values,))
    else:
        cur = con.cursor().execute(sql)

    result = cur.fetchall()
    return result


def insert_values():
    cur = con.cursor()

    cur.execute(
        '''
        INSERT INTO LINKS (NAME, FIELD) VALUES
        ('http://www.theverge.com', 'Computers'),
        ('http://www.wired.com', 'Music'),
        ('http://www.engadget.com', 'English'),
        ('http://www.reddit.com', 'English'),
        ('http://www.kickass.so', 'Computers'),
        ('http://www.thepiratebay.org', 'Maths'),
        ('http://www.youtube.com', 'Maths'),
        ('http://www.facebook.com', 'Science'),
        ('http://www.thisismynext.com', 'Science'),
        ('http://www.windowsphone.com', 'Music'),
        ('http://www.amazinglink.com', 'Computers'),
        ('http://www.randomsite.com', 'Science'),
        ('http://www.wowowow.com', 'English'),
        ('http://www.random.org', 'Maths'),
        ('http://www.samsung.com', 'Philosophy'),
        ('http://www.nokia.com', 'Philosophy'),
        ('http://www.gmail.com', 'Philosophy'),
        ('http://www.google.com', 'Maths'),
        ('http://www.thenextweb.com', 'Computers'),
        ('http://www.yahoo.com', 'Philosophy'),
        ('http://www.bangbang.com', 'English'),
        ('http://www.lalloo.com', 'Music'),
        ('http://www.digg.com', 'Music'),
        ('http://www.github.com', 'Science');
        '''
    )

    con.commit()


def create_tables():
    cur = con.cursor()

    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS LINKS (

            ID          INTEGER         PRIMARY KEY AUTOINCREMENT,

            NAME        VARCHAR(200)    NOT NULL,

            FIELD       VARCHAR(20)     NOT NULL);
        '''
    )

    con.commit()
