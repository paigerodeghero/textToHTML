content='''
<html><head><title>Webpage Template</title></head>
<body>
{strname}
{htmlpage_data}
</body></html>'''

htmlpage_data =''

def printItems(dictObj, indent, htmlpage):

    for key in dictObj:
        htmlpage = htmlpage+ '<h2>'+ key +  '</h2>'
        htmlpage = htmlpage +   '<ul>'
        for k, v in dictObj[key].items() :
            htmlpage = htmlpage +'<li>' + k + ' : ' + str(v) + '</li>'
        htmlpage = htmlpage +'</ul>'
    return htmlpage        



name = input('enter name: ') #optional 
strname = '<h1>' 'Hello '+ name + '!!' + '</h1>' #optional
dict = {'category 1 : cooking':{'apple':1,'banana': 2 ,'bread':1} , 'category 2 : activity':{'yoga': 'url','park': 'url' ,'painting': 'url'} , 'category 3 : aaa':{'yoga': 'url','park': 'url' ,'painting': 'url'} }
htmlpage_data = printItems(dict, 0, htmlpage_data)
htmlcontent = content.format(**locals())

outfile= open('template.html','w')
outfile.write(htmlcontent)
outfile.close()

import webbrowser, os.path
webbrowser.open('file:///'+os.path.abspath('template.html'))
