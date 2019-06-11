import re

with open('test.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = line.lower()
        # while line.count('lpad'):
        funcToReplace = re.search(r"lpad\(ltrim\(rtrim\(cast\((\w+) as varchar\(([0-9])\)+,([0-9]),'(\w)'\)", line)
        funcToReplace2 = re.search(r"lpad\(((\bsecond\b)|(\bminute\b)|(\bhour\b))\(cast\((\w+) as string\)\),([0-9]),'(\w)'\)", line)
        
        if funcToReplace:
            line = line.replace(funcToReplace.group(0), f"RIGHT(REPLICATE('{funcToReplace.group(4)}', {funcToReplace.group(3)}) + LTRIM(RTRIM(cast({funcToReplace.group(1)} as varchar({funcToReplace.group(2)}))), {funcToReplace.group(2)})")
        if funcToReplace2:
            line = line.replace(funcToReplace2.group(0), f"RIGHT(REPLICATE('{funcToReplace2.group(7)}', {funcToReplace2.group(6)}) + cast(datepart({funcToReplace2.group(1)}, {funcToReplace2.group(5)}) as varchar(max)), {funcToReplace2.group(6)})")

        with open('output.sql', 'a') as o:
            o.write(line)

# txt = "lpad(ltrim(rtrim(cast(car_dependencia as varchar(5)))),5,'0')"

# newTxt = re.search(r"lpad\(ltrim\(rtrim\(cast\((\w+) as varchar\(([0-9])\)+,([0-9]),'(\w)'\)", txt)

# if newTxt:
#     txt = txt.replace(newTxt.group(0), f"RIGHT(REPLICATE('{newTxt.group(4)}', {newTxt.group(3)}) + LTRIM(RTRIM(cast({newTxt.group(1)} as varchar({newTxt.group(2)}))), {newTxt.group(2)})")

# txt = 'select row1, row2 from table1 t1 inner join table2 t2 on (t1.row1 = t2.row1)'

# newTxt = re.search()