# import re

# line = "select lpad(hour(cast(carp_aprehendidofecha as string)),2,'0') from table1"

# funcToReplace = re.search(r"lpad\(((\bsecond\b)|(\bminute\b)|(\bhour\b))\(cast\((\w+) as string\)\),([0-9]),'(\w)'\)", line.lower())

# with open('test.txt', 'r') as f:
#     lines = f.readlines()

#     for line in lines:
#         line =  line.lower()
#         table = re.search(r"(from|join) (\w+.\w+)", line)
        
#         if(table):
#             with open('output.txt', 'a') as o:
#                 o.write(f'{table.group(2)}\n')

# print(f'0-{funcToReplace.group(0)}')
# print(f'1-{funcToReplace.group(1)}')
# print(f'2-{funcToReplace.group(2)}')
# print(f'3-{funcToReplace.group(3)}')
# print(f'4-{funcToReplace.group(4)}')
# print(f'5-{funcToReplace.group(5)}')
# print(f'6-{funcToReplace.group(6)}')
# print(f'7-{funcToReplace.group(7)}')

# line = line.replace(funcToReplace.group(0), f"RIGHT(REPLICATE('{funcToReplace.group(7)}', {funcToReplace.group(6)}) + cast(datepart({funcToReplace.group(1)}, {funcToReplace.group(5)}) as varchar(max)), {funcToReplace.group(6)})")
# print(line)

linesM = []
linesA = []
linesSS = []

with open('mapa_del_delito-tables.txt', 'r') as m:
    linesM = m.readlines()

with open('analisis_delictual-tables.txt', 'r') as a:
    linesA = a.readlines()

with open('snic_sat-tables.txt', 'r') as ss:
    linesSS = ss.readlines()

linesA.extend(linesM)
linesA.extend(linesSS)

linesA.sort()
linesA = list(dict.fromkeys(linesA))

with open('all_queries-tables.txt', 'a') as f:
    for x in linesA:
        f.write(f'{x}')