import json

f = open('anscombe.json')

data = json.load(f)

for i in data:
    print(i['X'])

f.close()