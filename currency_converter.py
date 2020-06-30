with open('datacurrency.txt') as f:
    lines=f.readlines()

dictcurrency={}
for line in lines:
    params=list(line.split("\t"))
    dictcurrency[params[0]]=params[1]

countryname=list(dictcurrency.keys())
value=list(dictcurrency.values())

amount=float(input("ENTER YOUR AMOUNT : "))

[print(item) for item in countryname]

name=input('ENTER ANY OF CURRENCY TYPE: ')

i=countryname.index(name)
print(f"{amount} INR in {name} is : {amount*float(value[i])}")