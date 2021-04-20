content='''
<html><head><title>Webpage Template</title></head>
<body>
Hello, {strname} !
</body></html>'''

strname = input('enter name: ')
htmlcontent = content.format(**locals())

outfile= open('template.html','w')
outfile.write(htmlcontent)
outfile.close()

import webbrowser, os.path
webbrowser.open('file:///'+os.path.abspath('template.html'))
