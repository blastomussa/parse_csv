#!/usr/bin/env python
# Author: blastomussa
# Date: 6/15/2021
# Description: finds chromebooks that need to be replaced by comparing 2 csv files

import csv

#paths
lastUser = "path/to/csv"
students = "path/to/csv"
replace = "path/to/csv"

with open(lastUser, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        serial = row['serial']
        username = row['username']

        with open(students, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                email = line['s_email']
                first = line['s_first']
                last = line['s_last']
                lc_first = line['LC_first']
                lc_last = line['LC_last']
                lc_mail = line['LC_email']
                phone = line['LC_Phone']

                if email == username:

                    with open(replace, 'a', newline='') as csvfile:
                        fieldnames = ['s_first','s_last','s_email','LC_first',	'LC_last','LC_email','LC_Phone','serial']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                        writer.writerow({'s_first': first,'s_last': last,'s_email':email,'LC_first':lc_first,	'LC_last':lc_last,'LC_email':lc_mail,'LC_Phone':phone,'serial':serial})
