Data Extraction & Storage
-------------------------
The project consists of two components:
* Extracting data from a remote server
* Formatting and storing the data in a sqlite database.

### Run Instructions
Run email_extraction.py first, then run email_processing.py with email_data.txt passed as an argument.

* python3 email_extraction.py
* python3 email_processing.py email_data.txt

It is possible that the web server can't be reached from within email-extraction.py due to security reasons at the University of Oklahoma.
If this is the case, you can still run email-processing.py because the repository should have included
files containing the output from email-extraction.py from previous runs.

Running email-processing.py should generate a sqlite database file that can be explored.

### Discussion / Explanation
To populate the database I first created a python script that would download all of the files from
the cs mail website given, extract, and combine all of those files into one text file.
(email_extraction.py)

I used this text file (email_data.txt) as the input to another python script that
created the sqlite database, processed the email text data, and populated the database using
built in python sqlite functions.
(email_processing.py)