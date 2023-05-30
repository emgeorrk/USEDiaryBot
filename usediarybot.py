# -*- coding: utf-8 -*-

import telebot;
bot = telebot.TeleBot('2107102088:AAHRC1ycVtS0o3uzkC11e5906kIR_ja_z6I')


from telebot import types

score = {
	"mat":{
	"1":{},
	"2":{},
	"3":{},
	"4":{},
	"5":{},
	"6":{},
	"7":{},
	"8":{},
	"9":{},
	"10":{},
	"11":{},
	"12":{},
	"13":{},
	"14":{},
	"15":{},
	"16":{},
	"17":{},
	"18":{},
	"19":{},
	},
	"rus":{
	"1":{},
	"2":{},
	"3":{},
	"4":{},
	"5":{},
	"6":{},
	"7":{},
	"8":{},
	"9":{},
	"10":{},
	"11":{},
	"12":{},
	"13":{},
	"14":{},
	"15":{},
	"16":{},
	"17":{},
	"18":{},
	"19":{},
	"20":{},
	"21":{},
	"22":{},
	"23":{},
	"24":{},
	"25":{},
	"26":{},
	"27":{},
	},
	"inf":{
	"1":{},
	"2":{},
	"3":{},
	"4":{},
	"5":{},
	"6":{},
	"7":{},
	"8":{},
	"9":{},
	"10":{},
	"11":{},
	"12":{},
	"13":{},
	"14":{},
	"15":{},
	"16":{},
	"17":{},
	"18":{},
	"19":{},
	"20":{},
	"21":{},
	"22":{},
	"23":{},
	"24":{},
	"25":{},
	"26":{},
	"27":{},
	},
}

comment = {
	"mat":{
	"1":{},
	"2":{},
	"3":{},
	"4":{},
	"5":{},
	"6":{},
	"7":{},
	"8":{},
	"9":{},
	"10":{},
	"11":{},
	"12":{},
	"13":{},
	"14":{},
	"15":{},
	"16":{},
	"17":{},
	"18":{},
	"19":{},
	},
	"rus":{
	"1":{},
	"2":{},
	"3":{},
	"4":{},
	"5":{},
	"6":{},
	"7":{},
	"8":{},
	"9":{},
	"10":{},
	"11":{},
	"12":{},
	"13":{},
	"14":{},
	"15":{},
	"16":{},
	"17":{},
	"18":{},
	"19":{},
	"20":{},
	"21":{},
	"22":{},
	"23":{},
	"24":{},
	"25":{},
	"26":{},
	"27":{},
	},
	"inf":{
	"1":{},
	"2":{},
	"3":{},
	"4":{},
	"5":{},
	"6":{},
	"7":{},
	"8":{},
	"9":{},
	"10":{},
	"11":{},
	"12":{},
	"13":{},
	"14":{},
	"15":{},
	"16":{},
	"17":{},
	"18":{},
	"19":{},
	"20":{},
	"21":{},
	"22":{},
	"23":{},
	"24":{},
	"25":{},
	"26":{},
	"27":{},
	},
}

# первая меню клавиатура
if True:
	main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите действие")
	menu_button = types.KeyboardButton("/menu")
	main_keyboard.add(menu_button)

# клавиатура для выбора предмета
if True:
	subject_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True, input_field_placeholder = "Выберите предмет")
	math_button = types.KeyboardButton("Математика")
	inf_button = types.KeyboardButton("Информатика")
	rus_button = types.KeyboardButton("Русский язык")
	subject_keyboard.add(math_button, inf_button, rus_button)
	info_start = "Пока я умею записывать число (ваш условный балл), редактировать его и показывать по вашему запросу\nНадеюсь, в ближайшее я научусь большему"
	info_text = "Список команд:\n/menu - Меню"

# инлайн клавиатура для кнопки назад из результатов
if True:
	result_back = types.InlineKeyboardMarkup()
	result_back_button = types.InlineKeyboardButton(text = "Назад", callback_data = "back")
	result_back.add(result_back_button)

# реплай для ввода кол-ва баллов
forcereply_for_score = types.ForceReply(input_field_placeholder = "По десятибалльной шкале")
forcereply_for_comment = types.ForceReply(input_field_placeholder = "Ваш комментарий")

# цвета для инлайн клавиатур
color_math = {
	1:{},
	2:{},
	3:{},
	4:{},
	5:{},
	6:{},
	7:{},
	8:{},
	9:{},
	10:{},
	11:{},
	12:{},
	13:{},
	14:{},
	15:{},
	16:{},
	17:{},
	18:{},
	19:{},
	20:{},
}

color_rus = {
	1:{},
	2:{},
	3:{},
	4:{},
	5:{},
	6:{},
	7:{},
	8:{},
	9:{},
	10:{},
	11:{},
	12:{},
	13:{},
	14:{},
	15:{},
	16:{},
	17:{},
	18:{},
	19:{},
	20:{},
	21:{},
	22:{},
	23:{},
	24:{},
	25:{},
	26:{},
	27:{},
	28:{},
}

color_inf = {
	1:{},
	2:{},
	3:{},
	4:{},
	5:{},
	6:{},
	7:{},
	8:{},
	9:{},
	10:{},
	11:{},
	12:{},
	13:{},
	14:{},
	15:{},
	16:{},
	17:{},
	18:{},
	19:{},
	20:{},
	21:{},
	22:{},
	23:{},
	24:{},
	25:{},
	26:{},
	27:{},
	28:{},
}

subject = {}
problem_number = {}

# 
expected_result = {
	"mat":{},
	"rus":{},
	"inf":{},
}

from_score = {}
from_comment = {}

@bot.message_handler(commands = ['start'])
def start(message):
		bot.send_message(message.chat.id, "Привет!", reply_markup = subject_keyboard)
		bot.register_next_step_handler(message, subject_stats, False);

@bot.message_handler(commands = ['info'])
def info(message):
	bot.send_message(message.chat.id, info_text)

@bot.message_handler(commands = ['menu'])
def change(message):
	try:
		bot.edit_message_reply_markup(chat_id = message.chat.id, message_id = message.message_id - 1, reply_markup = '')
	except Exception:
		nothing = 1
	from_comment[message.chat.id] = False
	from_score[message.chat.id] = False
	bot.send_message(message.chat.id, "Какой предмет вы хотите отредактировать?", reply_markup = subject_keyboard)
	bot.register_next_step_handler(message, subject_stats, False)

@bot.message_handler(content_types=['photos'])
def get_text_messages(message):
	bot.send_message(message.chat.id, "Я вас не понимаю\n/info", reply_markup = subject_keyboard)
	bot.register_next_step_handler(message, subject_stats, False);

def subject_stats(message, prev_stats): # тут происходит формирование инлайн клавиатуры с кружочками
	global subject
	global problem_keyboard
	global expected_result
	global score
	subject[message.chat.id] = "-1"
	subject_rus = "-1"
	if message.text == "Математика":
		global color_math
		problem_keyboard = types.InlineKeyboardMarkup()
		for i in range(1, 20):
			try:
				color_math[20][message.chat.id] = color_math[i][message.chat.id]
			except Exception:
				color_math[i][message.chat.id] = u'\U000026AA'
		if True:
			math_inline_1 = types.InlineKeyboardButton(text = "1 " + color_math[1][message.chat.id], callback_data = "mat_1_")
			math_inline_2 = types.InlineKeyboardButton(text = "2 " + color_math[2][message.chat.id], callback_data = "mat_2_")
			math_inline_3 = types.InlineKeyboardButton(text = "3 " + color_math[3][message.chat.id], callback_data = "mat_3_")
			math_inline_4 = types.InlineKeyboardButton(text = "4 " + color_math[4][message.chat.id], callback_data = "mat_4_")
			math_inline_5 = types.InlineKeyboardButton(text = "5 " + color_math[5][message.chat.id], callback_data = "mat_5_")
			math_inline_6 = types.InlineKeyboardButton(text = "6 " + color_math[6][message.chat.id], callback_data = "mat_6_")
			math_inline_7 = types.InlineKeyboardButton(text = "7 " + color_math[7][message.chat.id], callback_data = "mat_7_")
			math_inline_8 = types.InlineKeyboardButton(text = "8 " + color_math[8][message.chat.id], callback_data = "mat_8_")
			math_inline_9 = types.InlineKeyboardButton(text = "9 " + color_math[9][message.chat.id], callback_data = "mat_9_")
			math_inline_10 = types.InlineKeyboardButton(text = "10 " + color_math[10][message.chat.id], callback_data = "mat_10_")
			math_inline_11 = types.InlineKeyboardButton(text = "11 " + color_math[11][message.chat.id], callback_data = "mat_11_")
			math_inline_12 = types.InlineKeyboardButton(text = "12 " + color_math[12][message.chat.id], callback_data = "mat_12_")
			math_inline_13 = types.InlineKeyboardButton(text = "13 " + color_math[13][message.chat.id], callback_data = "mat_13_")
			math_inline_14 = types.InlineKeyboardButton(text = "14 " + color_math[14][message.chat.id], callback_data = "mat_14_")
			math_inline_15 = types.InlineKeyboardButton(text = "15 " + color_math[15][message.chat.id], callback_data = "mat_15_")
			math_inline_16 = types.InlineKeyboardButton(text = "16 " + color_math[16][message.chat.id], callback_data = "mat_16_")
			math_inline_17 = types.InlineKeyboardButton(text = "17 " + color_math[17][message.chat.id], callback_data = "mat_17_")
			math_inline_18 = types.InlineKeyboardButton(text = "18 " + color_math[18][message.chat.id], callback_data = "mat_18_")
			math_inline_19 = types.InlineKeyboardButton(text = "19 " + color_math[19][message.chat.id], callback_data = "mat_19_")
			math_result = types.InlineKeyboardButton(text = "Ожидаемый результат", callback_data = "res_mat")
			problem_keyboard.add(math_inline_1, math_inline_2, math_inline_3, math_inline_4, math_inline_5, math_inline_6, math_inline_7, math_inline_8, math_inline_9, math_inline_10, math_inline_11, math_inline_12, math_inline_13, math_inline_14, math_inline_15, math_inline_16, math_inline_17, math_inline_18)
			problem_keyboard.row(math_result)
		subject[message.chat.id] = "mat"

		ans = float(0)
		for i in range(1, 20):
			try:
				zxc = score[subject[message.chat.id]][str(i)][message.chat.id]
			except Exception:
				zxc = 0
			else:
				if i <= 12:
					ans += zxc*0.1
				elif i >= 13 and i <= 14:
					zxc = zxc*0.1*2
					ans += zxc
				elif i >= 15 and i <= 17:
					zxc = zxc*0.1*3
					ans += zxc
				elif i >= 18:
					zxc = zxc*0.1*4
					ans += zxc
		expected_result[subject[message.chat.id]][message.chat.id] = ans

		subject_rus = "математике"
	if message.text == "Русский язык":
		global color_rus
		problem_keyboard = types.InlineKeyboardMarkup()
		for i in range (1, 28):
			try:
				color_rus[28][message.chat.id] = color_rus[i][message.chat.id]
			except Exception:
				color_rus[i][message.chat.id] = u'\U000026AA'
		if True:
			rus_inline_1 = types.InlineKeyboardButton(text = "1 " + color_rus[1][message.chat.id], callback_data = "rus_1_")
			rus_inline_2 = types.InlineKeyboardButton(text = "2 " + color_rus[2][message.chat.id], callback_data = "rus_2_")
			rus_inline_3 = types.InlineKeyboardButton(text = "3 " + color_rus[3][message.chat.id], callback_data = "rus_3_")
			rus_inline_4 = types.InlineKeyboardButton(text = "4 " + color_rus[4][message.chat.id], callback_data = "rus_4_")
			rus_inline_5 = types.InlineKeyboardButton(text = "5 " + color_rus[5][message.chat.id], callback_data = "rus_5_")
			rus_inline_6 = types.InlineKeyboardButton(text = "6 " + color_rus[6][message.chat.id], callback_data = "rus_6_")
			rus_inline_7 = types.InlineKeyboardButton(text = "7 " + color_rus[7][message.chat.id], callback_data = "rus_7_")
			rus_inline_8 = types.InlineKeyboardButton(text = "8 " + color_rus[8][message.chat.id], callback_data = "rus_8_")
			rus_inline_9 = types.InlineKeyboardButton(text = "9 " + color_rus[9][message.chat.id], callback_data = "rus_9_")
			rus_inline_10 = types.InlineKeyboardButton(text = "10 " + color_rus[10][message.chat.id], callback_data = "rus_10_")
			rus_inline_11 = types.InlineKeyboardButton(text = "11 " + color_rus[11][message.chat.id], callback_data = "rus_11_")
			rus_inline_12 = types.InlineKeyboardButton(text = "12 " + color_rus[12][message.chat.id], callback_data = "rus_12_")
			rus_inline_13 = types.InlineKeyboardButton(text = "13 " + color_rus[13][message.chat.id], callback_data = "rus_13_")
			rus_inline_14 = types.InlineKeyboardButton(text = "14 " + color_rus[14][message.chat.id], callback_data = "rus_14_")
			rus_inline_15 = types.InlineKeyboardButton(text = "15 " + color_rus[15][message.chat.id], callback_data = "rus_15_")
			rus_inline_16 = types.InlineKeyboardButton(text = "16 " + color_rus[16][message.chat.id], callback_data = "rus_16_")
			rus_inline_17 = types.InlineKeyboardButton(text = "17 " + color_rus[17][message.chat.id], callback_data = "rus_17_")
			rus_inline_18 = types.InlineKeyboardButton(text = "18 " + color_rus[18][message.chat.id], callback_data = "rus_18_")
			rus_inline_19 = types.InlineKeyboardButton(text = "19 " + color_rus[19][message.chat.id], callback_data = "rus_19_")
			rus_inline_20 = types.InlineKeyboardButton(text = "20 " + color_rus[20][message.chat.id], callback_data = "rus_20_")
			rus_inline_21 = types.InlineKeyboardButton(text = "21 " + color_rus[21][message.chat.id], callback_data = "rus_21_")
			rus_inline_22 = types.InlineKeyboardButton(text = "22 " + color_rus[22][message.chat.id], callback_data = "rus_22_")
			rus_inline_23 = types.InlineKeyboardButton(text = "23 " + color_rus[23][message.chat.id], callback_data = "rus_23_")
			rus_inline_24 = types.InlineKeyboardButton(text = "24 " + color_rus[24][message.chat.id], callback_data = "rus_24_")
			rus_inline_25 = types.InlineKeyboardButton(text = "25 " + color_rus[25][message.chat.id], callback_data = "rus_25_")
			rus_inline_26 = types.InlineKeyboardButton(text = "26 " + color_rus[26][message.chat.id], callback_data = "rus_26_")
			rus_inline_27 = types.InlineKeyboardButton(text = "27 " + color_rus[27][message.chat.id], callback_data = "rus_27_")
			rus_result = types.InlineKeyboardButton(text = "Ожидаемый результат", callback_data = "res_rus")
			problem_keyboard.add(rus_inline_1, rus_inline_2, rus_inline_3, rus_inline_4, rus_inline_5, rus_inline_6, rus_inline_7, rus_inline_8, rus_inline_9, rus_inline_10, rus_inline_11, rus_inline_12, rus_inline_13, rus_inline_14, rus_inline_15, rus_inline_16, rus_inline_17, rus_inline_18, rus_inline_19, rus_inline_20, rus_inline_21, rus_inline_22, rus_inline_23, rus_inline_24, rus_inline_25, rus_inline_26, rus_inline_27)
			problem_keyboard.row(rus_result)
		subject[message.chat.id] = "rus"

		ans = float(0)
		for i in range(1, 28):
			try:
				zxc = score[subject[message.chat.id]][str(i)][message.chat.id]
			except Exception:
				zxc = 0
			else:
				if i <= 7:
					ans += zxc*0.1
				elif i == 8:
					zxc = zxc*0.1*5
					ans += zxc
				elif i >= 9 and i <= 15:
					ans += zxc*0.1
				elif i == 16:
					zxc = zxc*0.1*2
					ans += zxc
				elif i >= 17 and i <= 25:
					ans += zxc*0.1
				elif i == 26:
					ans += zxc*0.1*4
				elif i == 27:
					ans == zxc*0.1*25

		expected_result[subject[message.chat.id]][message.chat.id] = ans

		subject_rus = "русскому"
	if message.text == "Информатика":
		global color_inf
		problem_keyboard = types.InlineKeyboardMarkup()
		for i in range (1, 28):
			try:
				color_inf[28][message.chat.id] = color_inf[i][message.chat.id]
			except Exception:
				color_inf[i][message.chat.id] = u'\U000026AA'
		if True:
			inf_inline_1 = types.InlineKeyboardButton(text = "1 " + color_inf[1][message.chat.id], callback_data = "inf_1_")
			inf_inline_2 = types.InlineKeyboardButton(text = "2 " + color_inf[2][message.chat.id], callback_data = "inf_2_")
			inf_inline_3 = types.InlineKeyboardButton(text = "3 " + color_inf[3][message.chat.id], callback_data = "inf_3_")
			inf_inline_4 = types.InlineKeyboardButton(text = "4 " + color_inf[4][message.chat.id], callback_data = "inf_4_")
			inf_inline_5 = types.InlineKeyboardButton(text = "5 " + color_inf[5][message.chat.id], callback_data = "inf_5_")
			inf_inline_6 = types.InlineKeyboardButton(text = "6 " + color_inf[6][message.chat.id], callback_data = "inf_6_")
			inf_inline_7 = types.InlineKeyboardButton(text = "7 " + color_inf[7][message.chat.id], callback_data = "inf_7_")
			inf_inline_8 = types.InlineKeyboardButton(text = "8 " + color_inf[8][message.chat.id], callback_data = "inf_8_")
			inf_inline_9 = types.InlineKeyboardButton(text = "9 " + color_inf[9][message.chat.id], callback_data = "inf_9_")
			inf_inline_10 = types.InlineKeyboardButton(text = "10 " + color_inf[10][message.chat.id], callback_data = "inf_10_")
			inf_inline_11 = types.InlineKeyboardButton(text = "11 " + color_inf[11][message.chat.id], callback_data = "inf_11_")
			inf_inline_12 = types.InlineKeyboardButton(text = "12 " + color_inf[12][message.chat.id], callback_data = "inf_12_")
			inf_inline_13 = types.InlineKeyboardButton(text = "13 " + color_inf[13][message.chat.id], callback_data = "inf_13_")
			inf_inline_14 = types.InlineKeyboardButton(text = "14 " + color_inf[14][message.chat.id], callback_data = "inf_14_")
			inf_inline_15 = types.InlineKeyboardButton(text = "15 " + color_inf[15][message.chat.id], callback_data = "inf_15_")
			inf_inline_16 = types.InlineKeyboardButton(text = "16 " + color_inf[16][message.chat.id], callback_data = "inf_16_")
			inf_inline_17 = types.InlineKeyboardButton(text = "17 " + color_inf[17][message.chat.id], callback_data = "inf_17_")
			inf_inline_18 = types.InlineKeyboardButton(text = "18 " + color_inf[18][message.chat.id], callback_data = "inf_18_")
			inf_inline_19 = types.InlineKeyboardButton(text = "19 " + color_inf[19][message.chat.id], callback_data = "inf_19_")
			inf_inline_20 = types.InlineKeyboardButton(text = "20 " + color_inf[20][message.chat.id], callback_data = "inf_20_")
			inf_inline_21 = types.InlineKeyboardButton(text = "21 " + color_inf[21][message.chat.id], callback_data = "inf_21_")
			inf_inline_22 = types.InlineKeyboardButton(text = "22 " + color_inf[22][message.chat.id], callback_data = "inf_22_")
			inf_inline_23 = types.InlineKeyboardButton(text = "23 " + color_inf[23][message.chat.id], callback_data = "inf_23_")
			inf_inline_24 = types.InlineKeyboardButton(text = "24 " + color_inf[24][message.chat.id], callback_data = "inf_24_")
			inf_inline_25 = types.InlineKeyboardButton(text = "25 " + color_inf[25][message.chat.id], callback_data = "inf_25_")
			inf_inline_26 = types.InlineKeyboardButton(text = "26 " + color_inf[26][message.chat.id], callback_data = "inf_26_")
			inf_inline_27 = types.InlineKeyboardButton(text = "27 " + color_inf[27][message.chat.id], callback_data = "inf_27_")
			inf_res = types.InlineKeyboardButton(text = "Ожидаемый результат", callback_data = "res_inf")
			problem_keyboard.add(inf_inline_1, inf_inline_2, inf_inline_3, inf_inline_4, inf_inline_5, inf_inline_6, inf_inline_7, inf_inline_8, inf_inline_9, inf_inline_10, inf_inline_11, inf_inline_12, inf_inline_13, inf_inline_14, inf_inline_15, inf_inline_16, inf_inline_17, inf_inline_18, inf_inline_19, inf_inline_20, inf_inline_21, inf_inline_22, inf_inline_23, inf_inline_24, inf_inline_25, inf_inline_26, inf_inline_27)
			problem_keyboard.row(inf_res)
		subject[message.chat.id] = "inf"
		subject_rus = "информатике"

		ans = float(0)
		for i in range(1, 28):
			try:
				zxc = score[subject[message.chat.id]][str(i)][message.chat.id]
			except Exception:
				zxc = 0
			else:
				if i <= 24:
					ans += zxc*0.1
				else :
					ans += zxc*0.1*2

		expected_result[subject[message.chat.id]][message.chat.id] = ans

	if subject_rus != "-1":
		bot.send_message(message.chat.id, "Выберите номер задания", reply_markup = problem_keyboard)
	if subject_rus == "-1":
		bot.send_message(message.chat.id, "Данный предмет не поддерживается", reply_markup = subject_keyboard)
		bot.register_next_step_handler(message, subject_stats, False)


@bot.message_handler(content_types = ['text'])
def score_edit(message):
	global score
	global subject
	global problem_number
	global color_math
	global color_rus
	global color_inf
	global from_comment
	global from_score
	try:
		qwe = from_score[message.chat.id]
	except Exception:
		from_score[message.chat.id] = False
	try:
		qwer = from_comment[message.chat.id]
	except Exception:
		from_comment[message.chat.id] = False
	if from_score[message.chat.id] == True:
		try:
			a = subject[message.chat.id]
		except Exception:
			subject[message.chat.id] = "-1"
		if subject[message.chat.id] != "-1":
			try:
				abc = int(message.text)
			except Exception:
				bot.send_message(message.chat.id, "Цифрами, пожалуйста", reply_markup = forcereply_for_score)
				bot.register_next_step_handler(message, score_edit)
			else:
				if abc > 10 or abc < 0:
					bot.send_message(message.chat.id, "По десятибалльной шкале, пожалуйста", reply_markup = forcereply_for_score)
					bot.register_next_step_handler(message, score_edit)
				else:
					score[subject[message.chat.id]][problem_number[message.chat.id]][message.chat.id] = abc
					bot.send_message(message.chat.id, "Done!", reply_markup = subject_keyboard)
					if score[subject[message.chat.id]][problem_number[message.chat.id]][message.chat.id] < 5:
						if subject[message.chat.id] == "mat":
							color_math[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f534'
						if subject[message.chat.id] == "rus":
							color_rus[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f534'
						if subject[message.chat.id] == "inf":
							color_inf[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f534'
					elif score[subject[message.chat.id]][problem_number[message.chat.id]][message.chat.id] >= 5 and score[subject[message.chat.id]][problem_number[message.chat.id]][message.chat.id] <= 7:
						if subject[message.chat.id] == "mat":
							color_math[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f7e1'
						if subject[message.chat.id] == "rus":
							color_rus[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f7e1'
						if subject[message.chat.id] == "inf":
							color_inf[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f7e1'
					else:
						if subject[message.chat.id] == "mat":
							color_math[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f7e2'
						if subject[message.chat.id] == "rus":
							color_rus[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f7e2'
						if subject[message.chat.id] == "inf":
							color_inf[int(problem_number[message.chat.id])][message.chat.id] = u'\U0001f7e2'
					if score[subject[message.chat.id]][problem_number[message.chat.id]][message.chat.id] == 10:
						if subject[message.chat.id] == "mat":
							color_math[int(problem_number[message.chat.id])][message.chat.id] = u'\u2705'
						if subject[message.chat.id] == "rus":
							color_rus[int(problem_number[message.chat.id])][message.chat.id] = u'\u2705'
						if subject[message.chat.id] == "inf":
							color_inf[int(problem_number[message.chat.id])][message.chat.id] = u'\u2705'
					subject[message.chat.id] = "-1"
					problem_number[message.chat.id] = "-1"
					from_score[message.chat.id] = False
					bot.register_next_step_handler(message, subject_stats, False);
	elif from_comment[message.chat.id] == True:
		comment[subject[message.chat.id]][problem_number[message.chat.id]][message.chat.id] = str(message.text)
		bot.send_message(message.chat.id, "Done!", reply_markup = subject_keyboard)
		from_comment[message.chat.id] = False
		bot.register_next_step_handler(message, subject_stats, False);
	else:
		bot.send_message(message.chat.id, "Выберите предмет\n", reply_markup = subject_keyboard)
		bot.register_next_step_handler(message, subject_stats, False);


@bot.callback_query_handler(func = lambda call: True)
def handler_for_subjects(call):
	bot.answer_callback_query(callback_query_id = call.id, show_alert=False)
	global score
	global subject
	global problem_number
	global color_math
	global color_rus
	global color_inf
	global from_comment
	global from_score
	global problem_keyboard
	global expected_result

	if subject[call.message.chat.id] == "mat":
		temp_subject_rus_sk = "математике"
	if subject[call.message.chat.id] == "rus":
		temp_subject_rus_sk = "русскому языку"
	if subject[call.message.chat.id] == "inf":
		temp_subject_rus_sk = "информатике"
	
	if call.data == "edit":
		bot.send_message(call.message.chat.id, "Насколько успешно вы решаете это задание?\nОцените себя по десятибалльной шкале", reply_markup = forcereply_for_score)
		from_score[call.message.chat.id] = True
		bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup= '')
	elif call.data == "edit_comment":
		bot.send_message(call.message.chat.id, "Введите новый комментарий", reply_markup = forcereply_for_comment)
		from_comment[call.message.chat.id] = True
		bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup= '')
	elif call.data == "back":
		from_comment[call.message.chat.id] = False
		from_score[call.message.chat.id] = False
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Выберите номер задания", reply_markup = problem_keyboard)
	elif str(call.data[0]) + str(call.data[1]) + str(call.data[2]) == "res":
		temp_subject = str(call.data[4]) + str(call.data[5]) + str(call.data[6])
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Ожидаемое количество первичных баллов по " + temp_subject_rus_sk + ": " + str(int(round(expected_result[subject[call.message.chat.id]][call.message.chat.id]))) + "\n" + str(int(int(round(expected_result[subject[call.message.chat.id]][call.message.chat.id]))/33 *100)) + "%", reply_markup = result_back)
	else:
		if call.data[5] == '_':
			temp_problem_number = str(call.data[4])
		else:
			temp_problem_number = str(call.data[4]) + str(call.data[5])
		problem_number[call.message.chat.id] = temp_problem_number
		temp_subject = str(call.data[0]) + str(call.data[1]) + str(call.data[2])
		subject[call.message.chat.id] = temp_subject

		edit_inline_keyboard = types.InlineKeyboardMarkup()
		edit_score_button = types.InlineKeyboardButton(text = "Изменить балл", callback_data = "edit")
		edit_comment_button = types.InlineKeyboardButton(text = "Изменить комментарий", callback_data = "edit_comment")
		back_button = types.InlineKeyboardButton(text = "Назад", callback_data = "back")
		edit_inline_keyboard.row(edit_score_button)
		edit_inline_keyboard.row(edit_comment_button)
		edit_inline_keyboard.row(back_button)

		if True:
			if temp_subject == "mat":
				temp_subject_rus = "Математика"
				temp_color_subject = color_math[int(problem_number[call.message.chat.id])][call.message.chat.id]
			if temp_subject == "rus":
				temp_subject_rus = "Русский язык"
				temp_color_subject = color_rus[int(problem_number[call.message.chat.id])][call.message.chat.id]
			if temp_subject == "inf":
				temp_subject_rus = "Информатика"
				temp_color_subject = color_inf[int(problem_number[call.message.chat.id])][call.message.chat.id]

		try:
			temp_comment = comment[subject[call.message.chat.id]][problem_number[call.message.chat.id]][call.message.chat.id]
		except Exception:
			temp_comment = "Пусто"
		try:
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = temp_subject_rus + "\nНомер " + problem_number[call.message.chat.id] + "\n" + temp_color_subject + " Балл: " + str(score[subject[call.message.chat.id]][problem_number[call.message.chat.id]][call.message.chat.id]) + "\n\U0001f4ac Комментарий: " + temp_comment, reply_markup = edit_inline_keyboard)
		except Exception:
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = temp_subject_rus + "\nНомер " + problem_number[call.message.chat.id] + "\n" + temp_color_subject + " Балл: " + "не установлен"  + "\n\U0001f4ac Комментарий: " + temp_comment, reply_markup = edit_inline_keyboard)

	#bot.answer_callback_query(callback_query_id = call.id, show_alert=False)


bot.polling(none_stop = True, interval = 0)
