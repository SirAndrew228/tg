import telebot
import config
from telebot import types
import requests
from bs4 import BeautifulSoup as BS


n = requests.get('https://www.cybersport.ru/base/teams/natus-vincere/navi-cs-go')
html1 = BS(n.content, 'html.parser')
naviscore = html1.select('.facts__progress.team-points > .team-points__total')
naviscore1 = html1.select('.team-points__footer > .team-points__title.team-points__title--winner')


v = requests.get('https://www.cybersport.ru/base/teams/team-vitality/team-vitality-1')
html2 = BS(v.content, 'html.parser')
vitscore = html2.select('.facts__progress.team-points > .team-points__total')
vitscore1 = html2.select('.team-points__footer > .team-points__title.team-points__title--winner')


a = requests.get('https://www.cybersport.ru/base/teams/astralis/astralis')
html3 = BS(a.content, 'html.parser')
asscore = html3.select('.facts__progress.team-points > .team-points__total')
asscore1 = html3.select('.team-points__footer > .team-points__title.team-points__title--winner')


tl = requests.get('https://www.cybersport.ru/base/teams/team-liquid/team-liquid-cs-go')
html4 = BS(tl.content, 'html.parser')
tlscore = html4.select('.facts__progress.team-points > .team-points__total')
tlscore1 = html4.select('.team-points__footer > .team-points__title.team-points__title--winner')


print(naviscore[0].get_text())
print(naviscore1[0].get_text())
print(vitscore[0].get_text())
print(vitscore1[0].get_text())
print(asscore[0].get_text())
print(asscore1[0].get_text())
print(tlscore[0].get_text())
print(tlscore1[0].get_text())


bot=telebot.TeleBot(config.TOKEN, parse_mode="Markdown")


keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=(True), row_width=3)
keyboard1.row('Привет', 'CS:GO','Спасибо, пока!')


@bot.message_handler(commands = ['url'])
@bot.message_handler(commands=['start'])



def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text', 'document', 'audio', 'photo'])
@bot.message_handler(content_types=["url"])



def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет, все слова пиши с большой буквы")
    elif message.text == "Спасибо, пока!":
        bot.send_message(message.from_user.id, "Пока! Хорошего дня!")





    elif message.text == 'CS:GO':
        keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=(True), row_width=3)
        keyboard2.row('Информация о командах', 'Ближайшие матчи', 'Вернуться Назад')
        bot.send_message(message.from_user.id,'О чем вы хотите узнать?', reply_markup=keyboard2)

    elif message.text == 'Информация о командах':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=(True), row_width=3)
        keyboard3.row('navi','astralis','vitality', 'team liquid', 'Назад')
        bot.send_message(message.from_user.id, 'Выберите команду: navi, australis, vitality, team liquid', reply_markup=keyboard3)


    elif message.text == "Назад":
        bot.send_message(message.from_user.id, "Чем я могу быть полезен?", reply_markup=keyboard1)


    elif message.text == 'navi':
        nv = open('nv.jpg', 'rb')
        bot.send_photo(message.from_user.id, nv)
        bot.send_message(message.from_user.id, "Статистика Команды Natus Vincere: " + '\n\n' + naviscore[0].get_text() + ' \n\n Процент побед: ' + naviscore1[0].get_text())
        
        

    elif message.text == 'vitality':
        vit = open('vit.jpg', 'rb')
        bot.send_photo(message.from_user.id, vit)
        bot.send_message(message.from_user.id, "Статистика Команды Vitality: " + '\n\n' + vitscore[0].get_text() + ' \n\n Процент побед: ' + vitscore1[0].get_text())


    elif message.text == 'astralis':
        ast = open('ast.jpg', 'rb')
        bot.send_photo(message.from_user.id, ast)
        bot.send_message(message.from_user.id, "Статистика Команды Astralis: " + '\n\n' + asscore[0].get_text() + ' \n\n Процент побед: ' + asscore1[0].get_text())


    elif message.text == 'team liquid':
        team = open('team.jpeg', 'rb')
        bot.send_photo(message.from_user.id, team)
        bot.send_message(message.from_user.id, "Статистика Команды Team Liquid: " + '\n\n' + tlscore[0].get_text() + ' \n\n Процент побед: ' + tlscore1[0].get_text())


    elif message.text == "Вернуться Назад":
        bot.send_message(message.from_user.id, "Чем я могу быть полезен?", reply_markup=keyboard1)


    else:
        photo = open('babo.jpg', 'rb')
        bot.send_message(message.from_user.id, "Это секретная информация")
        bot.send_photo(message.from_user.id, photo)
bot.polling()