from whatsApp import whatsApp
from telegram import telegram

wUp = whatsApp()
wUp.setUp()

telegram = telegram()


if __name__ == '__main__':
	 #enviando a mensagem via telegram pra o whatsapp
     telegram.setUp(wUp).message_loop(telegram.recebendoMsgTelegram)
     print('chamando recebendo mensagem do telegram')
while True:
	pass




