from xml.dom import minidom

xmldoc = minidom.parse('nowy_kod.xml')
choices = xmldoc.getElementsByTagName('CHOICE')
for i in range(len(choices)):
    print(choices[i].firstChild.data)
