import telebot
import sqlite3

bot = telebot.TeleBot('')
name = None

@bot.message_handler(commands=['start'])
def start_message(message):
    conn = sqlite3.connect('NikiFes.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Привіт , це український бот підтримки, для реєстрації введіть своє імя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('NikiFes.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES ({name}, {password})')
    conn.commit()
    cur.close()
    conn.close()

    # bot.send_message(message.chat.id, 'Введите пароль')
    # bot.register_next_step_handler(message, user_pass)


bot.polling(none_stop=True)