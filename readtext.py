
import re
data= open('templateText.txt', "r")

lines = data.readlines()
dict_main={}
value_dict={}
#print(lines)
i=0
for line in lines:
	line=line.rstrip("\n")
	#print(line)
	if(line.split(": ",1)[0]=='Category'):
		key=str(line.split(": ",1)[1])
		key=key.rstrip("\n")
		#print(key)

	if(line.startswith('[')):
		value_dict_key= re.findall(r"\[([A-Za-z0-9_ ]+)\]", line)[0]
		#print(value_dict_key)
		value_dict_value= re.findall(r"\(([A-Za-z0-9_ .]+)\)", line)[0]
		#print(value_dict_value)
		value_dict[value_dict_key]= value_dict_value

	if(line==''):
		dict_main.update({key: value_dict})
		#dict_main[key]
		value_dict={}

dict_main.update({key: value_dict})

print(dict_main)










