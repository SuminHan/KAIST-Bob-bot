from bs4 import BeautifulSoup as bs
import re
import requests

URL_kaimaru = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=fclt'
URL_kyosu = 'https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=emp'

response = requests.get(URL_kaimaru)
response.encoding=None
TEXT_kaimaru = response.text


response = requests.get(URL_kyosu)
response.encoding=None
TEXT_kyosu = response.text

with open('text_kaimaru.html', 'w') as fp:
    fp.write(TEXT_kaimaru)
with open('text_kyosu.html', 'w') as fp:
    fp.write(TEXT_kyosu)

p = re.compile(r'\([^)]*\)')

today_title = ''
menu_dict = []
for TEXT in [TEXT_kaimaru, TEXT_kyosu]:
	soup = bs(TEXT, 'html.parser')
	main = soup.find('div', {'id': 'tab_item_1'})
	today_title = main.find('h3').text[9:]
	menu = main.find("table")
	three = [' '.join(re.sub(p, '', a.text).split()) for a in menu.find('tbody').find('tr').findAll('td')]
	menu_dict.append(three)

menu_text = today_title + '\n'
menu_text += '<점심>\n'
menu_text += '*카이마루*: ' + menu_dict[0][1] + '\n'
menu_text += '*교수회관*: ' + menu_dict[1][1] + '\n'
menu_text += '<저녁>\n'
menu_text += '*카이마루*: ' + menu_dict[0][2] + '\n'
menu_text += '*교수회관*: ' + menu_dict[1][2] + '\n'

print(menu_text)
with open('menu_text.txt', 'w') as wf:
	wf.write(menu_text)

#for m in menu_dict:
#	for t in m:
#		print(t)
#		print('\n\n\n')
#print(menu_dict)
