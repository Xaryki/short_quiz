import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('6480180092:AAFmBo_J8keudQhxBvKJDMKCcOyKPHGUo_8')
correct_answers = 0
start_time = 0


@bot.message_handler(commands=['start', 'test'])
def start(message):
    global correct_answers
    global start_time
    correct_answers = 0
    start_time = 0
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='first_question')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='stop')
    keyboard.add(key_yes, key_no)
    bot.send_message(message.chat.id, text='Вы хотите пройти тест?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global correct_answers
    global start_time
    if call.data == "first_question":
        start_time = datetime.datetime.now()
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='5', callback_data='second_question')
        key_2 = types.InlineKeyboardButton(text='6', callback_data='second_question')
        key_3 = types.InlineKeyboardButton(text='3', callback_data='second_question')
        key_4 = types.InlineKeyboardButton(text='4', callback_data='second_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Сколько будет 2+2?", reply_markup=keyboard)
    elif call.data == "stop":
        bot.send_message(call.message.chat.id, 'Надо больше трудиться...')
    elif call.data == "second_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Слон', callback_data='third_question')
        key_2 = types.InlineKeyboardButton(text='Крокодил', callback_data='third_question')
        key_3 = types.InlineKeyboardButton(text='Жираф', callback_data='third_question')
        key_4 = types.InlineKeyboardButton(text='Черепаха', callback_data='third_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Как называют животное, которое имеет панцирь?", reply_markup=keyboard)
    elif call.data == "second_question_t":
        correct_answers += 1
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Слон', callback_data='third_question')
        key_2 = types.InlineKeyboardButton(text='Крокодил', callback_data='third_question')
        key_3 = types.InlineKeyboardButton(text='Жираф', callback_data='third_question')
        key_4 = types.InlineKeyboardButton(text='Черепаха', callback_data='third_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Как называют животное, которое имеет панцирь?", reply_markup=keyboard)
    elif call.data == "third_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='C++', callback_data='fourth_question')
        key_2 = types.InlineKeyboardButton(text='C', callback_data='fourth_question')
        key_3 = types.InlineKeyboardButton(text='Rust', callback_data='fourth_question_t')
        key_4 = types.InlineKeyboardButton(text='Ruby', callback_data='fourth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Какой язык программирования считается самым безопасным?", reply_markup=keyboard)
    elif call.data == "third_question_t":
        correct_answers += 1
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='C++', callback_data='fourth_question')
        key_2 = types.InlineKeyboardButton(text='C', callback_data='fourth_question')
        key_3 = types.InlineKeyboardButton(text='Rust', callback_data='fourth_question_t')
        key_4 = types.InlineKeyboardButton(text='Ruby', callback_data='fourth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Какой язык программирования считается самым безопасным?", reply_markup=keyboard)
    elif call.data == "fourth_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Python', callback_data='fifth_question_t')
        key_2 = types.InlineKeyboardButton(text='C#', callback_data='fifth_question')
        key_3 = types.InlineKeyboardButton(text='C++', callback_data='fifth_question')
        key_4 = types.InlineKeyboardButton(text='R', callback_data='fifth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="В каком языке полностью автоматический сборщик мусора (garbage collector)?",
                              reply_markup=keyboard)
    elif call.data == "fourth_question_t":
        correct_answers += 1
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Python', callback_data='fifth_question_t')
        key_2 = types.InlineKeyboardButton(text='C#', callback_data='fifth_question')
        key_3 = types.InlineKeyboardButton(text='C++', callback_data='fifth_question')
        key_4 = types.InlineKeyboardButton(text='R', callback_data='fifth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="В каком языке полностью автоматический сборщик мусора (garbage collector)?",
                              reply_markup=keyboard)
    elif call.data == "fifth_question":
        final_time = datetime.datetime.now() - start_time
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"Ура! Вы прошли тест!\nВаш результат: {correct_answers}/4")
        with open("score.txt", "a") as file:
            score_list = f"Результат: {correct_answers}/4, id: {call.from_user.id}, Имя: {call.from_user.first_name}, Время: {final_time}\n"
            file.write(score_list)

    elif call.data == "fifth_question_t":
        correct_answers += 1
        final_time = datetime.datetime.now() - start_time
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"Ура! Вы прошли тест!\nВаш результат: {correct_answers}/4")
        with open("score.txt", "a") as file:
            score_list = f"Результат: {correct_answers}/4, id: {call.from_user.id}, Имя: {call.from_user.first_name}, Время: {final_time}\n"
            file.write(score_list)


bot.polling(none_stop=True, interval=0)
