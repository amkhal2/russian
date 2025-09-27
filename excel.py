from openpyxl import load_workbook
import os, random

base = os.path.abspath(os.path.dirname(__file__))
path  = base + '\\Russian Dictionary.xlsx'


def get_rows(path):
    wb = load_workbook(path)
    ws = wb["Sheet1"]
    rows = iter(list(ws.rows))
    a = next(rows)  # to skip the first row

    c = 0
    refined_rows = []
    for row in rows:
        if row[1].value and row[2].value and row[3].value: 
##            print(row[1].value)     # word
##            print(row[2].value)     # pronunciation
##            print(row[3].value)     # meaning
##            print()

            refined_rows.append((row[1].value, row[2].value, row[3].value))
            c = c + 1

##    print(c)
    return refined_rows

##get_rows(path)

##rows = get_rows(path)
##
##category = {}
##for row in rows:
##    print(row)
##    if row[1].strip() in category:
##        category[row[1].strip()] = category[row[1].strip()] + 1
##    else:
##        category[row[1].strip()] = 1   
##    print()
##
##print(category)    
##
### a list of sorted "key, value" pairs
##sorted_cat = sorted(category.items(), key=lambda x:x[1],reverse=True)
##print(sorted_cat)
##
##sample = random.sample(rows, 10)
##print(sample)


