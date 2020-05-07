from bs4 import BeautifulSoup

conent = open('./locations/zviglod_brist.xml').read()

soup = BeautifulSoup(conent, 'html.parser')

location = soup.find_all('location')

print(len(location))