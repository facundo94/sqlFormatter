import re

txt = "selec lpad(ltrim(rtrim(cast(car_dependencia as varchar(5)))),5,'0') from unoTabla"

newTxt = re.search(r"lpad\(ltrim\(rtrim\(cast\((\w+) as varchar\(([0-9])\)+,([0-9]),'(\w)'\)", txt)

# if newTxt:
    # print(f"RIGHT(REPLICATE('{newTxt.group(4)}', {newTxt.group(3)}) + LTRIM(RTRIM(cast({newTxt.group(1)} as varchar({newTxt.group(2)}))), {newTxt.group(2)})")

if(newTxt):
    txt = txt.replace(newTxt.group(0), f"RIGHT(REPLICATE('{newTxt.group(4)}', {newTxt.group(3)}) + LTRIM(RTRIM(cast({newTxt.group(1)} as varchar({newTxt.group(2)}))), {newTxt.group(2)})")

print(txt)