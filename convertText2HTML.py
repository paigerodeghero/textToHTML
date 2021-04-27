import re
import json

header = '''<!DOCTYPE html>
<html>
	<head>
		<title>Text to HTML Converter</title>
	</head>
	<body>{0}
	</body>
</html>'''

data= open('templateText.txt', "r")

htmlpage_data =''

lines = data.readlines()
dict_main={}
value_dict={}
i=0
for line in lines:
	line=line.rstrip("\n")
	print(line)
	if(line.split(": ",1)[0]=='Category'):
		key=str(line.split(": ",1)[1])
		key=key.rstrip("\n")
		print(key)

	if(line.startswith('[')):
		value_dict_key= re.findall(r"\[([A-Za-z0-9_ ]+)\]", line)[0]
		value_dict_value= re.findall(r"\(([A-Za-z0-9_ .]+)\)", line)[0]
		value_dict[value_dict_key]= value_dict_value

	if(line==''):
		dict_main.update({key: value_dict})
		dict_main[key]
		value_dict={}

dict_main.update({key: value_dict})

def printItems(dictObj, indent, htmlpage):

    for key in dictObj:
        htmlpage = htmlpage+ "\n"+'\t\t<h2>'+ key +  '</h2>'
        htmlpage = htmlpage + "\n"+  '\t\t<ul>'
        for k, v in dictObj[key].items() :
            htmlpage = htmlpage +"\n"+'\t\t\t<li>' + k + ': ' + '<a href="'+str(v)+ '"></a></li>'
        htmlpage = htmlpage +"\n" + '\t\t</ul>'
    return htmlpage  

htmlpage_data = printItems(dict_main, 0, htmlpage_data)

with open("index.html", "w") as e:
	e.write(header.format(htmlpage_data))