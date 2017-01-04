About This Repository
=====================
This homework was assigned to me in my Text Analytics class at the University of Oklahoma.

The homework consists of two parts, extracting data from a remote server, and formatting and storing the
data in a sqlite database.

My Approach
-----------
To populate the database I first created a python script that would download all of the files from
the cs mail website given, extract, and combine all of those files into one text file.
(email-extraction.py)

I used this text file (named email-data.txt) as the input to another python script that
created the sqlite database, processed the email text data, and populated the database using
built in python sqlite functions.
(email-processing.py)

Run Instructions
----------------
Run email-extraction.py first, then run email-processing.py with email-data.txt passed as an argument.

It is possible that the web server can't be reached from within email-extraction.py.
If this is the case, you can still run email-processing.py because the repository should have included
files that have the output from email-extraction.py from previous runs.

Running email-processing.py should generate a sqlite database file that can be explored.