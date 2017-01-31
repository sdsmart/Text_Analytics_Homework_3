#!/usr/bin/env python3

import os

# variables
output_file = 'email_data.txt'
base_url = 'http://mail.cs.ou.edu/pipermail/cs/'
documents = ['2014-April.txt.gz',
             '2014-May.txt.gz',
             '2014-June.txt.gz',
             '2014-July.txt.gz',
             '2014-August.txt.gz',
             '2014-September.txt.gz',
             '2014-October.txt.gz',
             '2014-November.txt.gz',
             '2014-December.txt.gz',
             '2015-January.txt.gz',
             '2015-February.txt.gz',
             '2015-March.txt.gz',
             '2015-April.txt.gz',
             '2015-May.txt.gz',
             '2015-June.txt.gz',
             '2015-July.txt.gz',
             '2015-August.txt.gz',
             '2015-September.txt.gz',
             '2015-October.txt.gz',
             '2015-November.txt.gz']

# creating output file
os.system('touch ' + output_file)

# extracting data
for doc in documents:
    # downloading file
    os.system('wget ' + base_url + doc)
    # extracting file
    os.system('gzip -d ' + doc)
    # adding contents of file to main file
    os.system('cat ' + doc[:-3] + '>>' + output_file)
    # removing individual text files
    os.system('rm ' + doc[:-3])

