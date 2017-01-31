#!/usr/bin/env python3

import sqlite3
import codecs
import re

# ---functions---

# reads the file and returns a list of strings representing each email
def read_file(file_name):
    with codecs.open(file_name, encoding='utf-8') as f: 
        temp = re.split(r'(From.+\nFrom.+\n)', f.read())
        del temp[0]

    emails = []

    for i in range(0, len(temp), 2):
        emails.append(temp[i] + temp[i+1])

    for i, email in enumerate(emails):
        emails[i] = email.strip()

    return emails

# parses the list of emails into a list of the component parts
# the list returned has the following element order:
# [0] date_sent
# [1] sender_name
# [2] sender_email
# [3] subject
# [4] email
def parse_email(email):
    email_components = []

    # extracting the date_sent
    temp = email.split('\n')
    first_line = temp[0]
    email_components.append(first_line[-24:-4] + 'UTC ' + first_line[-4:])

    # extracting the sender_name
    second_line = temp[1]
    pat = re.compile(r'\((.+)\)')
    m = pat.search(second_line)
    email_components.append(m.group(1))

    # extracting the sender_email
    pat = re.compile(r'From:\s+(.+) \(')
    m = pat.search(second_line)
    email_components.append(m.group(1).replace(' at ', '@'))

    # extracting the subject
    fourth_line = temp[3]
    pat = re.compile(r'Subject:\s+(.+)')
    m = pat.search(fourth_line)
    email_components.append(m.group(1))

    # extracting the email body
    temp = '\n'.join(temp)
    pat = re.compile(r'Message-ID:\s+<.+>(.+)', re.DOTALL)
    m = pat.search(temp)
    email_components.append(m.group(1).strip())

    return email_components

# ---script---

# reading file into a list of emails
emails = read_file('email_data.txt')

# creating / connecting to pipermail.db
db = sqlite3.connect('pipermail.db')

# creating db cursor in order to execute sql statements
db_cursor = db.cursor()

# creating table (commented if table has already been created
db_cursor.execute('''CREATE TABLE csmail (
                    date_sent text,
                    sender_name text,
                    sender_email text,
                    subject text,
                    email text
                  );''')

# parsing emails into component parts
for email in emails:
    email_components = parse_email(email)

    # inserting the email into the db
    db_cursor.execute('INSERT INTO csmail VALUES (?, ?, ?, ?, ?)', email_components)

# saving db actions
db.commit()

# closing db connection
db.close()
