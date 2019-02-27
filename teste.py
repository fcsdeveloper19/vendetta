from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import sys
import telepot

bot = telepot.Bot('730873853:AAGfK5jud5AL3yxsI3FikNWh7ump3LeMv24')

driver = webdriver.Firefox()

print('carregando o firefox')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
print('carregando o whatsup')

def enviandoMsgWhatsUp(target, mensagem):

	# Replace 'Friend's Name' with the name of your friend 
	# or the name of a group 
	#target = '"Kaka"'

	# Replace the below string with your own message
	#string = 'Ola isto é um testes'

	print('Dentro do enviando mensagem whats up')
	print(target)
	print(mensagem)
	x_arg = '//span[contains(@title,' + target + ')]'
	group_title = wait.until(EC.presence_of_element_located((
		By.XPATH, x_arg)))
	group_title.click()

	print('passei')
	message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
	print('message')

	message.send_keys(mensagem)

	sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
	sendbutton.click()

	#driver.close()

def listaUsersWA():
	#user = driver.find_element_by_class_name('_1wjpf').text
	users = driver.find_elements_by_class_name('_1wjpf')

	print ('usuario ', users[0].text)
	print (len(users))
	n = 0
	listauserswa = users[0].text
	while (n < len(users)):
		listauserswa = listauserswa + str(n) #+'.'+users[n].text+'\n'
		print (users[n].text)
		

def recebendoMsgTelegram(msg):
	print('dentro do recebendo mensagem do telegram')
	print(msg['text'])
	mensagem = msg['text']
	chat_id = msg['chat']['id']
	if (mensagem == 'bom dia'):
		bot.sendMessage(chat_id,'bom dia senhor')
	elif (mensagem == '/exit'):
		driver.close()
		exit()
	elif (mensagem == '/lw'):
		listaUsersWA()
	else:
		enviandoMsgWhatsUp('"Kaka"', msg['text'])


if __name__ == '__main__':
		# Replace below path with the absolute path
	# to chromedriver in your computer

	 bot.message_loop(recebendoMsgTelegram)	
	 print('chamando recebendo mensagem do telegram')

while True:
	pass

	