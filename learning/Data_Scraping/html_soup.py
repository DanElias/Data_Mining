
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

fd = open("index.html", 'r')
html_doc = fd.read()

soup = BeautifulSoup(html_doc, 'html.parser')
type(soup)
print(soup.prettify())

print("The title with tags is: %s" % soup.title)
print("The title is: %s" % soup.title.string)
print("The parent tag of the title tag is: %s" % soup.title.parent.name)
print("The p tag is: %s" % soup.p)
print("The a tag text is: %s" % soup.a.string)
print("The p tag class is: %s" % soup.p['class'])
print("The array of p tags is: %s" % soup.find_all('p'))
print("Get Tag by Id: %s" % soup.find(id="link3"))
for link in soup.find_all('a'):
    print("Found a link: %s" % link.get('href'))
print("The text in the html is: %s" % soup.get_text())








