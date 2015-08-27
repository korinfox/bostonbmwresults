# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:27:23 2015

@author: Justin
"""

import csv

# import tab separated tex file containing pax values for 2015

paxfilename = 'pax2015.txt'

with open(paxfilename, 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    paxlist = list(csv_reader)
    pax = {rows[0]:float(rows[1]) for rows in paxlist}
paxlist = None
paxfilename = None    
    