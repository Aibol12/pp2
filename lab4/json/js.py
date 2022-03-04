import json
with open('sample-data.json') as json_file:
	data = json.load(json_file)
#print(json.dumps(data, indent = 4))
print('Interface Status')
print('='*89)
names = ['DN', 'Description', 'Speed', 'MTU']
form = "{:<46}  {:<14}  {:<9}  {:<7}";
print(form.format(*names))
print('-'*46 + '  ' + '-'*14 + '  ' + '-'*9+ '  ' + '-'*7)
n = data["totalCount"]
for i in data['imdata']:
	dat = i['l1PhysIf']['attributes']
	print(form.format(*(dat['dn'], '' if dat.get('description') == None else dat['description'], dat['speed'], dat['mtu'])))
