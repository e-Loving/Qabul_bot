import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
from datetime import datetime

token = "5033083369:AAGjjfE3Uf5pRbwPHN7mN962WjWjq0oyOFQ"
bot = telebot.TeleBot(token)
son = 0
allstarts = []
admins = []


@bot.message_handler(commands=['start', "create", "remove"])
def get_text_messages(message):
    if message.text == "/create":
        if str(message.chat.id) == "1980653792":
            kivy = bot.send_message(message.chat.id, "Admin id raqamini kiriting...")
            bot.register_next_step_handler(kivy, create_admin)
        else:
            pass
    elif message.text == "/remove":
        if str(message.chat.id) == "1980653792":
            kivy = bot.send_message(message.chat.id, "Admin id raqamini kiriting...")
            bot.register_next_step_handler(kivy, remove_admin)
    else:
        if message.text == "/start":
            try:
                join = bot.get_chat_member("@eLoving_daily", message.chat.id)
                if join.status == "kicked" or join.status == "left":
                    markup3 = types.InlineKeyboardMarkup()
                    item1 = types.InlineKeyboardButton("➕ Kanalimiz", url="https://t.me/testforinteger")
                    item2 = types.InlineKeyboardButton("✅ Tekshirish", callback_data='check')
                    markup3.add(item1)
                    markup3.add(item2)
                    bot.send_message(message.chat.id,
                                     "Assalomu alekum botdan foydalanish uchun kanalimizga obuna bo'ling !",
                                     reply_markup=markup3)
                else:
                    show_menu(message)
            except:
                markup3 = types.InlineKeyboardMarkup()
                item1 = types.InlineKeyboardButton("➕ Kanalimiz", url="https://t.me/testforinteger")
                item2 = types.InlineKeyboardButton("✅ Tekshirish", callback_data='check')
                markup3.add(item1)
                markup3.add(item2)
                bot.send_message(message.chat.id,
                                 "Assalomu alekum botdan foydalanish uchun kanalimizga obuna bo'ling !",
                                 reply_markup=markup3)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if is_subscribed(call) == True:

        #   Go back

        if call.data == "back":
            show_menu(call)

        #   About us

        elif call.data == "check":
            try:
                join = bot.get_chat_member("@eLoving_daily", call.message.chat.id)
                if join.status in ["left", "kicked"]:
                    bot.answer_callback_query(call.id,
                                              "ℹ️ Obuna bo'lgandan so'ng tekshirish tugmasini bosing ✅ ",
                                              show_alert=True)
                else:
                    global allstarts
                    if call.message.chat.id in allstarts:
                        pass
                    else:
                        allstarts.append(call.message.chat.id)

                    #   Main menu

                    show_menu(call)
            except:
                show_menu(call)

        elif call.data == "us":
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🔙Ortga", callback_data="back")
            markup.add(item1)
            bot.send_location(call.message.chat.id, latitude="40.765832", longitude="72.355716")

            #   Fill the blank

        elif call.data == "start":
            lst = []

            #   Send the form to admin

            def sendto(message):
                try:
                    if int(message.text) <= 999999999 and int(message.text) >= 333333333:
                        telefon = message.text
                        lst.append(telefon)
                        q, w, e, r = lst
                        # bot.send_message(1507426796, f"📝 Ism: {q}\n✍️ Familiya: {w}\n📖 Kurs: {e}\n☎️ Telefon: {r}")
                        global son
                        son += 1
                        bot.send_message(1507426796,
                                         f"📝 Ism: {q}\n✍️ Familiya: {w}\n📖 Kurs: {e}\n☎️ Telefon: {r}\n🎊 Ro'yxatdan o'tganlar soni : {son}")
                        lst.clear()
                        bot.send_message(call.message.chat.id, "✅ Siz muvaffaqiyatli ro'yxatdan o'tdingiz !")
                    else:
                        bot.send_message(call.message.chat.id,
                                         "👎 Siz noto'g'ri raqam kiritdingiz\n♻️ Iltimos qayta ro'yxatdan o'tish tugmasini bosing !")
                except:
                    bot.send_message(call.message.chat.id,
                                     "👎 Siz noto'g'ri tanlov qildingiz\n♻️ Iltimos qayta ro'yxatdan o'tish tugmasini bosing !")

            #   Get the lastname

            def get_familiya(message):
                try:
                    if message.text == "🧨 Boshlash..." or message.text == "🛑 To'xtatish !" or "/" in message.text or not f"{message.text}".isalpha():
                        bot.send_message(call.message.chat.id,
                                         "👎 Siz noto'g'ri tanlov qildingiz\n♻️ Iltimos qayta ro'yxatdan o'tish tugmasini bosing !")
                    else:
                        ism = message.text
                        lst.append(ism)
                        familiya = bot.send_message(call.message.chat.id,
                                                    f"😊 Ismingiz chiroyli ekan {ism} 💫\n\n✍️ Familiyangizni kiriting")
                        bot.register_next_step_handler(familiya, why)
                except:
                    bot.send_message(call.message.chat.id,
                                     "👎 Siz noto'g'ri tanlov qildingiz\n♻️ Iltimos qayta ro'yxatdan o'tish tugmasini bosing !")

            #   User chooses the subject

            def why(message):
                try:
                    familiya = message.text
                    lst.append(familiya)
                    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                    item1 = types.KeyboardButton("🔌 Robototexnika")
                    item2 = types.KeyboardButton("🐍 Python dasturlash")
                    item3 = types.KeyboardButton("📈 Foundation")
                    item4 = types.KeyboardButton("🕸 Web Dasturlash")
                    item5 = types.KeyboardButton("🤖 Android Development")
                    item6 = types.KeyboardButton("🍏 iOS Development")
                    markup.row(item1, item2)
                    markup.row(item3, item4)
                    markup.row(item5, item6)
                    kurs = bot.send_message(call.message.chat.id,
                                            f"🤔 Xurmatli {familiya} !\n\n📖 Qaysi kurs uchun ro'yxatdan o'tmoqchisiz ?",
                                            reply_markup=markup)
                    bot.register_next_step_handler(kurs, get_number)
                except:
                    bot.send_message(call.message.chat.id,
                                     "👎 Siz noto'g'ri tanlov qildingiz\n♻️ Iltimos qayta ro'yxatdan o'tish tugmasini bosing !")

            #   Get phone number

            def get_number(message):
                try:
                    if "/" not in message.text:
                        why = message.text
                        lst.append(why)
                        telefon = bot.send_message(call.message.chat.id, "☎️ Raqamingizni kiriting\nMisol : 901234567")
                        bot.register_next_step_handler(telefon, sendto)
                    else:
                        show_menu(call)
                except:
                    bot.send_message(call.message.chat.id,
                                     "👎 Siz noto'g'ri tanlov qildingiz\n♻️ Iltimos qayta ro'yxatdan o'tish tugmasini bosing !")

            #   Check are they really want to register

            def proc1(message):
                try:
                    if message.text == "🧨 Boshlash...":
                        shuyer = bot.send_message(call.message.chat.id,
                                                  "ℹ️ Sizdan kerakli ma'lumotlarni olishimga izn bering...\n\n"
                                                  "📝 Ismingizni kiriting")
                        bot.register_next_step_handler(shuyer, get_familiya)
                    elif message.text == "🛑 To'xtatish !":
                        markup3 = types.InlineKeyboardMarkup()
                        item1 = types.InlineKeyboardButton("👨‍🏫 Biz haqimizda", callback_data='us')
                        item2 = types.InlineKeyboardButton("📌 Ro'yxatdan o'tish", callback_data='start')
                        item3 = types.InlineKeyboardButton("📲 Admin bilan bog'lanish", callback_data="admin")
                        item4 = types.InlineKeyboardButton("🔧 Shikoyat va takliflar", callback_data="punish")
                        markup3.add(item1, item2)
                        markup3.add(item3, item4)
                        bot.send_message(call.message.chat.id, "🛠 Siz asosiy menyuga qaytdingiz, {} !\n\n"
                                                               "🤝 Sizga qanday yordam bera olaman...".format(
                            call.from_user.first_name),
                                         reply_markup=markup3)
                except:
                    bot.send_message(call.message.chat.id,
                                     "👎 Siz noto'g'ri tanlov qildingiz\n♻️ Iltimos qayta ro'yxatdan o'tish tugmasini bosing !")

            #   Show the alert message

            alert = bot.answer_callback_query(call.id,
                                              "ℹ️ Iltimos ma'lumotlarni to'g'riligiga ishonch xosil qilgandan so'ng tanlovni amalga oshiring !✅ ",
                                              show_alert=True)
            if alert is True:
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                item1 = types.KeyboardButton("🧨 Boshlash...")
                item2 = types.KeyboardButton("🛑 To'xtatish !")
                markup.row(item1)
                markup.row(item2)
                processing = bot.send_message(call.message.chat.id, "♻️ Amalga oshirilmoqda...", reply_markup=markup)
                bot.register_next_step_handler(processing, proc1)
        #   To type about the bugs and debugging

        elif call.data == "punish":
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🔙Ortga", callback_data="back")
            markup.add(item1)
            punish = bot.send_message(call.message.chat.id,
                                      f"😇Xurmatli {call.from_user.first_name}\nAgar sizda biror taklif va shikoyat bo'lsa yozib qoldirishingiz mumkin. "
                                      "Biz bundan albatta xursand bo'lamiz !\nXurmat bilan o'quv markaz ma'muriyati",
                                      reply_markup=markup)

            def punishment(message):
                if message.text != "🧨 Boshlash..." and message.text != "🛑 To'xtatish !":
                    bot.send_message(1507426796,
                                     f"✅ {message.from_user.first_name}dan xabar:\n-----\n    {message.text}\n-----\n🧨 Username = @{message.from_user.username}")
                    # bot.send_message(1507426796, f"{message.from_user.first_name}dan:\n{message.text}\nUsername = {message.from_user.username}")
                    bot.send_message(message.chat.id,
                                     f"😃 Xurmatli {call.from_user.first_name} ! Sizning xabaringiz adminga jo'natildi !\n"
                                     "🔑 Fikr va takliflaringiz uchun raxmat !")
                else:
                    pass

            bot.register_next_step_handler(punish, punishment)
        #   About teachers

        elif call.data == "admin":
            bot.send_message(call.message.chat.id, "👨‍🏫 Admin :\n\n"
                                                   "🧸 Telegram  -  @integer_admin\n\n"
                                                   "📲 Telefon  -  +998555006070")

        #   Show startuppers

        elif call.data == "startup":
            bot.send_message(call.message.chat.id,
                             f"🥳 Janob Boss xozirchalik biz {len(allstarts)} nafar startchilarga egamiz!\n\n🥳 Tabriklayman")
        #   Formed members
        elif call.data == "filledForm":
            bot.send_message(call.message.chat.id,
                             f"😃 Boss! bizda {son} nafar ro'yxatdan o'tganlar bor.\n\n☺️ Yomon emas shundaymi?")
        #   Weather for admin section

        elif call.data == "weather":
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                resp = requests.get('https://www.gismeteo.ru/weather-andijan-5333/now/', headers=headers).text
                soup = BeautifulSoup(resp, "html.parser")
                havo = soup.find("span", class_="unit unit_temperature_c")
                bot.send_message(call.message.chat.id, f"🌤 Hozir harorat {havo.get_text()}.")
            except:
                error = bot.send_message(call.message.chat.id, "😢 Ma'lumotlar xozircha mavjud emas")
                bot.register_next_step_handler(error, get_text_messages)
        #   Namaz time
        elif call.data == "namoz":
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                resp = requests.get('https://namozvaqti.uz/', headers=headers).text
                soup = BeautifulSoup(resp, "html.parser")
                bomdod = soup.find("p", class_="time", id="bomdod")
                quyosh = soup.find("p", class_="time", id="quyosh")
                peshin = soup.find("p", class_="time", id="peshin")
                asr = soup.find("p", class_="time", id="asr")
                shom = soup.find("p", class_="time", id="shom")
                xufton = soup.find("p", class_="time", id="hufton")
                bot.send_message(call.message.chat.id, f"🌄 Bomdod namozi vaqti  {bomdod.get_text()}\n\n"
                                                       f"☀️ Quyosh chiqish vaqti    {quyosh.get_text()}\n\n"
                                                       f"🏙 Peshin namozi vaqti     {peshin.get_text()}\n\n"
                                                       f"🌆 Asr namozi vaqti           {asr.get_text()}\n\n"
                                                       f"🎇 Shom namozi vaqti       {shom.get_text()}\n\n"
                                                       f"🌃 Xufton namozi vaqti     {xufton.get_text()}\n\n")
                minutes = int(datetime.now().strftime("%H")) * 60 + int(datetime.now().strftime("%M"))
                bom = list(bomdod.get_text().split(":"))
                bomdod_uchun = int(bom[0]) * 60 + int(bom[1])
                pesh = list(peshin.get_text().split(":"))
                peshin_uchun = int(pesh[0]) * 60 + int(pesh[1])
                a = list(asr.get_text().split(":"))
                a_uchun = int(a[0]) * 60 + int(a[1])
                sho = list(shom.get_text().split(":"))
                sho_uchun = int(sho[0]) * 60 + int(sho[1])
                xuf = list(xufton.get_text().split(":"))
                xuf_uchun = int(xuf[0]) * 60 + int(xuf[1])
                if minutes < bomdod_uchun:
                    target = bomdod_uchun - minutes
                    soat = int(target / 60)
                    minut = target - soat * 60
                    bot.send_message(call.message.chat.id,
                                     f"🌄 Bomdod namoziga {soat}:{minut} vaqt qoldi, Boss.\n🕋 Namoz har bir musulmon uchun farz !")
                elif minutes > bomdod_uchun and minutes < peshin_uchun:
                    target = peshin_uchun - minutes
                    soat = int(target / 60)
                    minut = target - soat * 60
                    bot.send_message(call.message.chat.id,
                                     f"🏙 Peshin namoziga {soat}:{minut} vaqt qoldi, Boss.\n🕋 Namoz har bir musulmon uchun farz !")
                elif minutes > peshin_uchun and minutes < a_uchun:
                    target = a_uchun - minutes
                    soat = int(target / 60)
                    minut = target - soat * 60
                    bot.send_message(call.message.chat.id,
                                     f"🌆 Asr namoziga {soat}:{minut} vaqt qoldi, Boss.\n🕋 Namoz har bir musulmon uchun farz !")
                elif minutes > a_uchun and minutes < sho_uchun:
                    target = sho_uchun - minutes
                    soat = int(target / 60)
                    minut = target - soat * 60
                    bot.send_message(call.message.chat.id,
                                     f"🎇 Shom namoziga {soat}:{minut} vaqt qoldi, Boss.\n🕋 Namoz har bir musulmon uchun farz !")
                elif minutes > sho_uchun and minutes < xuf_uchun:
                    target = xuf_uchun - minutes
                    soat = int(target / 60)
                    minut = target - soat * 60
                    bot.send_message(call.message.chat.id,
                                     f"🌃 Xufton namoziga {soat}:{minut} vaqt qoldi, Boss.\n🕋 Namoz har bir musulmon uchun farz !")
            except:
                error = bot.send_message(call.message.chat.id, "😢 Ma'lumotlar xozircha mavjud emas")
                bot.register_next_step_handler(error, get_text_messages)
        #   Today's holiday
        elif call.data == "today":
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
                resp = requests.get('https://nationaltoday.com/what-is-today/', headers=headers).text
                soup = BeautifulSoup(resp, "html.parser")
                holiday = soup.find("h3", class_="holiday-title")
                bot.send_message(call.message.chat.id, f"🎉 Today is {holiday.get_text()}\n\n")
            except:
                error = bot.send_message(call.message.chat.id, "😢 Ma'lumotlar xozircha mavjud emas")
                bot.register_next_step_handler(error, get_text_messages)

    else:
        bot.answer_callback_query(call.id,
                                  "ℹ️ Obuna bo'lgandan so'ng tekshirish tugmasini bosing ✅ ",
                                  show_alert=True)
    #   Entering to admin section


@bot.message_handler()
def welcome(message):
    #   Admin section
    if str(message.chat.id) in admins or str(message.chat.id) == "1980653792":
        if message.text == "Admin":
            markup3 = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("📮 Jami bot foydalanuvchilar soni", callback_data='startup')
            item2 = types.InlineKeyboardButton("🎊 Ro'yxatdan o'tganlar soni", callback_data='filledForm')
            item3 = types.InlineKeyboardButton("🕋 Namoz vaqtlari", callback_data="namoz")
            item4 = types.InlineKeyboardButton("🌦 Obi-havo ma'lumotlari", callback_data="weather")
            item5 = types.InlineKeyboardButton("💎 Bugun qanday kun", callback_data="today")
            item6 = types.InlineKeyboardButton("🔙 Ortga", callback_data="back")
            markup3.add(item1)
            markup3.add(item2)
            markup3.add(item3, item4)
            markup3.add(item5)
            markup3.add(item6)
            bot.send_message(message.chat.id, "😇 Boss sizga qanday yordam bera olaman...", reply_markup=markup3)


def create_admin(message):
    if str(message.chat.id) == "1980653792":
        if message.text.isdigit():
            admins.append(message.text)
            bot.send_message(message.chat.id, "✅ Boss siz adminni muvaffiqayatli qo'shdingiz !")
        else:
            plus = bot.send_message(message.chat.id, "❌ Iltimos faqat mavjud bo'lgan id jo'nating !")
            bot.register_next_step_handler(plus, create_admin)


def remove_admin(message):
    if str(message.chat.id) == "1980653792":
        if message.text.isdigit():
            if message.text in admins:
                admins.remove(message.text)
                bot.send_message(message.chat.id, "✅ Boss siz adminni muvaffiqayatli olib tashladingiz !")
            else:
                bot.send_message(message.chat.id, "❌ Bunday odam mavjud emas")
        else:
            plus = bot.send_message(message.chat.id, "❌ Iltimos faqat mavjud bo'lgan id jo'nating !")
            bot.register_next_step_handler(plus, create_admin)


def show_menu(id):
    markup3 = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("📍 Bizning manzil", callback_data='us')
    item2 = types.InlineKeyboardButton("📌 Ro'yxatdan o'tish", callback_data='start')
    item3 = types.InlineKeyboardButton("📲 Admin bilan bog'lanish", callback_data="admin")
    item4 = types.InlineKeyboardButton("🔧 Shikoyat va takliflar", callback_data="punish")
    markup3.add(item1, item2)
    markup3.add(item3, item4)
    bot.send_message(id.message.chat.id, "🛠 Siz asosiy menyudasiz, {} !\n\n"
                                         "🤝 Sizga qanday yordam bera olaman...".format(id.from_user.first_name),
                     reply_markup=markup3)


def is_subscribed(id):
    try:
        join = bot.get_chat_member("@eLoving_daily", id.message.chat.id)
        if join.status in ["kicked", "left"]:
            return False
        else:
            return True
    except:
        return False


bot.polling(none_stop=True)
