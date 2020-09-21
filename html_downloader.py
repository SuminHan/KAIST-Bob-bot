from bs4 import BeautifulSoup as bs
import re
import requests

URL_kaimaru = 'https://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=fclt'
URL_kyosu = 'https://www.kaist.ac.kr/_prog/fodlst/index.php?site_dvs_cd=kr&menu_dvs_cd=050303&dvs_cd=emp'

response = requests.get(URL_kaimaru)
response.encoding=None
TEXT_kaimaru = response.text

with open('text_kaimaru.html', 'w') as wf:
	wf.write(TEXT_kaimaru)

response = requests.get(URL_kyosu)
response.encoding=None
TEXT_kyosu = response.text

with open('text_kyosu.html', 'w') as wf:
	wf.write(TEXT_kyosu)
	p = re.compile(r'\([^)]*\)')
	TEXT_kaimaru, TEXT_kyosu = '', ''
	with open('text_kaimaru.html') as rf:
		TEXT_kaimaru = rf.read()
	with open('text_kyosu.html') as rf:
		TEXT_kyosu = rf.read()

	today_title = ''
	menu_dict = []
	for TEXT in [TEXT_kaimaru, TEXT_kyosu]:
		soup = bs(TEXT, 'html.parser')
		date = soup.find('div', {'class': 'resTit'})
		today_title = date.find('div').text
		menu = soup.find("table", {"class": "menuTb"})
		three = [' '.join(re.sub(p, '', a.text).split()) for a in menu.find('tbody').find('tr').findAll('td')]
		menu_dict.append(three)

	menu_text = today_title + '\n'
	menu_text += '<점심>\n'
	menu_text += '카이마루: ' + menu_dict[0][1] + '\n'
	menu_text += '교수회관: ' + menu_dict[1][1] + '\n'
	menu_text += '<저녁>\n'
	menu_text += '카이마루: ' + menu_dict[0][2] + '\n'
	menu_text += '교수회관: ' + menu_dict[1][2] + '\n'

	print(menu_text)

	#for m in menu_dict:
	#	for t in m:
	#		print(t)
	#		print('\n\n\n')
	#print(menu_dict)
