html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print soup.get_text()
print soup.find(string=re.compile("sisters"))
#print(soup.prettify())

for link in soup.find_all('a'):
	print link.get('href');

html_d1="""
<div tabindex="-1" class="zm-item-answer "

itemscope itemtype="http://schema.org/Answer"
data-aid="20616"
data-atoken="12253906"
data-collapsed="0"
data-created="1299688637"
data-deleted="0"
data-helpful="1"
data-isowner="0"
data-copyable="1"


>

</div>
<div tabindex="-1" class="zm-item-answer "

itemscope itemtype="http://schema.org/Answer"
data-aid="20616"
data-atoken="12253906"
data-collapsed="0"
data-created="1299688637"
data-deleted="0"
data-helpful="1"
data-isowner="0"
data-copyable="1"


>

</div>
"""
soup = BeautifulSoup(html_d1, 'html.parser')
print len(soup.find_all(attrs={"itemtype":"http://schema.org/Answer"}))