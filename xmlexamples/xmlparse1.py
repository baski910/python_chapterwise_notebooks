import xml.etree.ElementTree as ET

tree=ET.parse('movies.xml')

root=tree.getroot()

'''
print root.tag

print root.attrib
'''

#print the child of root
for child in root:
	print child.tag,child.attrib

#to display all the elements in the xml

print [ele.tag for ele in root.iter()]

#You can expand the use of the iter() function to help with finding particular elements of interest.

for movie in root.iter('movie'):
	print movie.tag,movie.attrib

for d in root.iter('description'):
	print d.text

# using xpath list filter items

for m in root.findall("./genre/decade/movie/[year='1992']"):
	print m.attrib
