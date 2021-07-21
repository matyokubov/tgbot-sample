# Telegram bot yaratish uchun kutubxonani chaqiramiz
import telebot
bot = telebot.TeleBot("1916449557:AAEvDG8f4MoXHOSOh0rb9vJWmn28wqD2P5s")

#bot uchun tugmalar yaratamiz
#bu darlar bo'ladi
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Python', 'C++')
keyboard.row('Java')
keyboard.row('NodeJS')
keyboard.row('Dasturchi', 'Kanal')

# Endi yangilik!
# Botga kirganda kanalga a'zo bo'ldirishni qo'samiz
# Bu funksiya odam kanalga obuna bo'lganligini tekshiradi
def is_joined(user_id):
  try:
    member = bot.get_chat_member("@coding_quizz", user_id).status
    print(member)
    if(member == 'member' or member == 'creator' or member == 'administrator'):
      return True
  except:
    return False

# Start bosilgandagi funksiya
@bot.message_handler(commands=['start'])
def welcome(message):
    global keyboard
    # Sticker yuboramiz
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Salom "+message.from_user.first_name)
    # Bu yerda obuna qildiriladi
    if is_joined(message.chat.id):
      # Obuna bo'linga yani menyu ochiladi
      bot.send_message(message.chat.id, "Botdan foydalanishingiz mumkin😊", reply_markup=keyboard)
    else:
      keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
      keyboard1.row('Dasturchi', 'Kanal')
      bot.send_message(message.chat.id, "Iltimos @coding_quizz kanaliga a'zo bo'ling...\nKeyin qayta /start buyrug'ini bosing", reply_markup=keyboard1)

# Ochilgan menyudan tugma bosilganda ishlaydigan shartlar
@bot.message_handler(content_types=['text'])
def send_text(message):
  if message.text == "Python":
    # bu yerda video yuborilmoqda
    # video shuncha misol va qiymatga ega emas
    # o'zingizning fayl yoki video darsligingiz bo'lsa yo'naltirib olasiz
    bot.send_document(message.chat.id, open('video.mp4', 'rb'), caption="Python darslari")
    bot.send_message(message.chat.id, "Tayyor")
  elif message.text == "C++":
    bot.send_document(message.chat.id, open('video.mp4', 'rb'), caption="C++ darslari")
    bot.send_message(message.chat.id, "Tayyor")
  elif message.text == "Dasturchi":
    bot.send_message(message.chat.id, "Dasturchi: FirdavsDev\n👉 @junior_coder_2007")
  elif message.text == "Kanal":
    bot.send_message(message.chat.id, "Kanalimizga obuna bo'ling\n👉 https://t.me/python_dasturlash_darslari")

# Oxirgi ish botni yurgizish
bot.polling(none_stop=True)

# bir narsani aytib o'tay
# botni azo bo'ldiradigan qilish uchun
# uni o'sha kanalga admin qilish kk
