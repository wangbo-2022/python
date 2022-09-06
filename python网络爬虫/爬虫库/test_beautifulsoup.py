from bs4 import BeautifulSoup

html='''
<html>
    <a class='test'>data</a>
    <a class='test1'>data1</a>
</html>
'''

soup =BeautifulSoup(html,'lxml')

a=soup.find(name='a')
print(a)
print(a.name)
print(a.attrs)
print(a.text)

b=soup.find(attrs={'class':'test'})
print(b)

c=soup.find(text='data')
print(c)

d=soup.findAll('a')
print(d)


















