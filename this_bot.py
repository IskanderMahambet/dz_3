import telebot
import dz_a
import dz_b
import dz_c

token = '485606860:AAFC1eSP_LksyJSRHsDK0Z9b49Rt4u_YzEI'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def check_message(message):
    if message.text == 'города Казахстана':
        for gorod in dz_a.get_goroda_RK():
            bot.send_message(message.chat.id,gorod)
    elif message.text == 'ученики класса':
        for student in dz_b.get_list_students():            
            bot.send_message(message.chat.id,student)
    elif message.text == 'достопримечательности Астаны':
        for dostop in dz_c.get_dostop():            
            bot.send_message(message.chat.id,dostop)

bot.polling(none_stop=True)
