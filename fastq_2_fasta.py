import sqlite3
from os import path 

data_dir = '/home/hwu/dev/stock_data/data'
conn = sqlite3.connect(path.join(data_dir, 'stock.db'))

with open(filename, "r") as ins:
    line_num = 0
    seq_id = ""
    seq = ""
    score = ""
    for line in ins:
        if (line_num % 4 == 0):
            seq_id  = line[1:].strip()
            line_num = 0
        if (line_num  == 1):
            seq = line.strip() 
        if (line_num  == 2):
            score = line.strip()
        line_num = line_num + 1

