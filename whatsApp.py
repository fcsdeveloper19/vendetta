from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import sys

print('carregando o firefox')


class whatsApp():

    @classmethod
    def setUp(cls):
        """ Seta o webdriver para firefox """
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 600)
        #cls.driver.implicitly_wait(600)
        cls.driver.maximize_window
        cls.driver.get("https://web.whatsapp.com/")
    
    @classmethod
    def tearDown(cls):
        """ Fecha o browser """
        cls.driver.quit()

    @classmethod
    def enviandoMsgWhatsUp(cls, target, mensagem):

        # Replace 'Friend's Name' with the name of your friend 
        # or the name of a group 
        #target = '"Kaka"'

        # Replace the below string with your own message
        #string = 'Ola isto é um testes'

        print('Dentro do enviando mensagem whats up')
        print(target)
        print(mensagem)
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = cls.wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()

        print('passei')
        message = cls.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        print('message')

        message.send_keys(mensagem)

        #sendbutton = cls.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        #clicando o botão enviar do whatsapp
        sendbutton = cls.driver.find_element_by_class_name('_35EW6')
        sendbutton.click()
        print('enviei a mensagem')
        #driver.close()
        
    @classmethod
    def listaUsersWA(cls):
        users = []
        #user = driver.find_element_by_class_name('_1wjpf').text
        for i in range(len(users)+1):
        #users = cls.driver.find_elements_by_class_name('_1wjpf')
            try:
                users[i] = cls.driver.find_element_by_xpath("//*[@id='pane-side']/div/div/div/div['{}']/div/div/div[2]/div[1]/div[1]/span/span".format(str(i)))
            except NoSuchElementException:
                pass

        #for i in len(users):
        print('usuario ',users[0].text)
        print('usuario ',users[1].text)
        print('usuario ',users[2].text)
        print('usuario ',users[3].text)
        print('usuario ',users[4].text)
        print('usuario ',users[5].text)

        #print ('usuario ', users[0].text)
        #print (len(users))
        #n = 0
        #listauserswa = users[0].text
        #while (n < len(users)):
        #    listauserswa = listauserswa + str(n) #+'.'+users[n].text+'\n'
        #    print (users[n].text)

class teste:
    def funcaoTeste(self):
        print('Isto é um teste')
