from whatsApp import whatsApp
import telepot

class telegram:

    #def __init__(self, whatsApp):
    #    self.whatsApp = whatsApp

    @classmethod
    def setUp(cls, whatsApp):
        cls.bot = telepot.Bot('730873853:AAGfK5jud5AL3yxsI3FikNWh7ump3LeMv24')
        cls.wApp = whatsApp
        return cls.bot
        

    @classmethod
    def recebendoMsgTelegram(cls, msg):
        print('dentro do recebendo mensagem do telegram')
        print(msg['text'])
        mensagem = msg['text']
        chat_id = msg['chat']['id']
        if (mensagem == 'bom dia'):
            cls.bot.sendMessage(chat_id,'bom dia senhor')
        elif (mensagem == '/exit'):
            cls.wApp.tearDown
            exit()
        elif (mensagem == '/lw'):
            cls.wApp.listaUsersWA()
        else:
            cls.wApp.enviandoMsgWhatsUp('"Kaka"', msg['text'])
