import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random
from logging import basicConfig, info, INFO, Formatter, FileHandler
from datetime import datetime
from pytz import timezone

def timetz(*args):
    return datetime.now(tz).timetuple()

tz = timezone('Asia/Kolkata')

Formatter.converter = timetz

basicConfig(handlers=[FileHandler(filename="./log.txt", encoding='utf-8', mode='a+')],level=INFO, format="%(asctime)s %(message)s")

def log(message, text: str):
    '''
    log() function needs two variables as input message and text.
    :param message: variable that you got from the telebot decorators
    :type message: message
    :param text: text you want to log
    :type text: :obj:`str`
    '''
    if message.chat.username:
        info(f"[{message.chat.id}][{message.chat.first_name}][{message.chat.username}] | {text}")
    else:
        info(f"[{message.chat.id}][{message.chat.first_name}] | {text}")

API_KEY = ""# Enter the API provided to you by Telegram Bot Father here
bot = telebot.TeleBot(API_KEY)
bukhari_pdf = [
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.1-Ahadith1-875.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.2-Ahadith876-1772.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.3-Ahadith1773-2737.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.4-Ahadith2738-3648.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.5-Ahadith3649-4473.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.6-Ahadith4474-5062.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.7-Ahadith5063-5969.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.8-Ahadith5970-6860.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Bukhari/english/SahihAl-bukhariVol.9-Ahadith6861-7563.pdf"
]

muslim_pdf = [
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Muslim/english/SahihMuslimVol.1-Ahadith1-1160.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Muslim/english/SahihMuslimVol.2-Ahadith1161-2262.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Muslim/english/Sahihmuslimvol.3-ahadith2263-33971.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Muslim/english/SahihMuslimVol.4-Ahadith3398-4518.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Muslim/english/SahihMuslimVol.5-Ahadith4519-5645.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Muslim/english/SahihMuslimVol.6-Ahadith5646-6722.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Saheh%20Al-Muslim/english/SahihMuslimVol.7-Ahadith6723-7563.pdf"
]

nasai_pdf = [
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Al-Nisai/english/Sunan-an-Nasa-i-Vol-1-English.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Al-Nisai/english/Sunan-an-Nasa-i-Vol-2-English.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Al-Nisai/english/Sunan-an-Nasa-i-Vol-3-English.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Al-Nisai/english/Sunan-an-Nasa-i-Vol-4-English.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Al-Nisai/english/Sunan-an-Nasa-i-Vol-5-English.pdf"

]

abu_pdf = [
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Abe-Dawood/english/Sunan-Abu-Dawud-Vol-1-1-1160.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Abe-Dawood/english/Sunan-Abu-Dawud-Vol-2-1161-2174.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Abe-Dawood/english/Sunan-Abu-Dawud-Vol-3-2175-3241.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Abe-Dawood/english/Sunan-Abu-Dawud-Vol-4-3242-4350.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Sunan%20Abe-Dawood/english/Sunan-Abu-Dawud-Vol-5-4351-5274.pdf"

]

tirmidhi_pdf = [
    "https://www.ahlesunnatpak.com/uploads/books/Jamia%20Tirmazi%20Mutarjam/english/Jami-at-Tirmidhi-Vol-1-1-543.pdf",
    "https://www.ahlesunnatpak.com/uploads/books/Jamia%20Tirmazi%20Mutarjam/english/Jami-at-Tirmidhi-Vol-2-544-1204.pdf", 
    "https://www.ahlesunnatpak.com/uploads/books/Jamia%20Tirmazi%20Mutarjam/english/Jami-at-Tirmidhi-Vol-3-1205-1896.pdf", 
    "https://www.ahlesunnatpak.com/uploads/books/Jamia%20Tirmazi%20Mutarjam/english/Jami-at-Tirmidhi-Vol-4-1897-2605.pdf", 
    "https://www.ahlesunnatpak.com/uploads/books/Jamia%20Tirmazi%20Mutarjam/english/Jami-at-Tirmidhi-Vol-5-2606-3290.pdf", 
    "https://www.ahlesunnatpak.com/uploads/books/Jamia%20Tirmazi%20Mutarjam/english/Jami-at-Tirmidhi-Vol-6-3291-3956.pdf"
]

ibn_pdf = [
    "http://futureislam.files.wordpress.com/2011/12/sunan-ibn-majah-volume-1.pdf",
    "http://futureislam.files.wordpress.com/2011/12/sunan-ibn-majah-volume-2.pdf",
    "http://futureislam.files.wordpress.com/2011/12/sunan-ibn-majah-volume-3.pdf",
    "http://futureislam.files.wordpress.com/2011/12/sunan-ibn-majah-volume-4.pdf",
    "http://futureislam.files.wordpress.com/2011/12/sunan-ibn-majah-volume-5.pdf"
]
ahmad_pdf = [
        "http://futureislam.files.wordpress.com/2013/03/musnad-imam-ahmad-bin-hanbal-volume-1.pdf",
        "http://futureislam.files.wordpress.com/2013/03/musnad-imam-ahmad-bin-hanbal-volume-2.pdf",
        "http://futureislam.files.wordpress.com/2013/03/musnad-imam-ahmad-bin-hanbal-volume-3.pdf"
]
def send_message(chat_id, text):
    MAX_LENGTH = 4096
    chunks = [text[i:i+MAX_LENGTH] for i in range(0, len(text), MAX_LENGTH)]
    for chunk in chunks:
        bot.send_message(chat_id, chunk)

def verify_hadith(book, hadith):
    out = None
        
    url = f"https://sunnah.com/{book}:{hadith}"
    content = requests.get(url)
    htmlContent = content.content

    soup = BeautifulSoup(htmlContent, "html.parser")
    #print(soup.prettify)
    try:                
        if book == "bukhari" or book == "muslim":
            try:
                HRS = soup.find("div",class_='hadith_reference_sticky').get_text()+'\n'
                AHF = soup.find("div",class_='arabic_hadith_full arabic').get_text()+'\n'
                HN = soup.find("div",class_='hadith_narrated').get_text()+'\n'
                TD = soup.find("div",class_='text_details').get_text()+'\n'
                H = HRS+AHF+HN+TD
                out = H
            except:
                out = "Sorry Sahih Muslim is only available upto Hadith No. 3033 currently."
        elif book == "ahmad":
            try:
                HRS = soup.find("div",class_='hadith_reference_sticky').get_text()+'\n'
                AHF = soup.find("div",class_='arabic_hadith_full arabic').get_text()+'\n'
                EHF = soup.find("div",class_='english_hadith_full').get_text()+'\n'
                H = HRS+AHF+EHF
                out = H
                try:
                    out = H + "\n\n" + soup.find("div", class_="hadith_annotation").get_text()
                except:
                    pass  
            except:
                out = "Sorry Musnad Ahmad is currently only available upto Hadith No. 1438.\n\nPress /help for seeing instructions and query submission details again.\nPress /random to see a random hadith."
        else:
            HRS = soup.find("div",class_='hadith_reference_sticky').get_text()+'\n'
            AHF = soup.find("div",class_='arabic_hadith_full arabic').get_text()+'\n'
            EHF = soup.find("div",class_='english_hadith_full').get_text()+'\n'
            H = HRS+AHF+EHF
            out = H
            
            try:
                out = H + "\n\n"+soup.find("div", class_="hadith_annotation").get_text()
            except:
                pass
    except Exception as e:
        out = "SORRY, HADITH NUMBER DOES NOT EXIST OR INPUT FORMAT WAS WRONG.\nText the Hadith number with book in this format [Name_of_book { SPACE } Hadith_number](like this \"Sahih Bukhari 1035\" or \"abu dawood 1\" write name of book before the hadith number) and this bot will send the full hadith back to you with its Grade(Sahih, Dai'f, Maudu, etc.) if it is not from Sahihain.\nSend your Hadith to get Started. If you are facing this issue continuously text @abdulmuizz0903 or mail us at saeedabdulmuizz@gmail.com"
        print(e)
        out = "WRONG INPUT TRY AGAIN.\nText the Hadith number with book in this format [Name_of_book { SPACE } Hadith_number](like this \"Sahih Bukhari 1035\" or \"abu dawood 1\" write name of book before the hadith number) and this bot will send the full hadith back to you with its Grade(Sahih, Dai'f, Maudu, etc.) if it is not from Sahihain.\nSend your Hadith to get Started. If you are facing this issue continuously text @abdulmuizz0903 or mail us at saeedabdulmuizz@gmail.com"
    # print("Verifying hadith for " + str(id))
    return out
def sendHadithpdf(id, link):
    bot.send_document(id, link)

def download_book(message):
    had_code = {'bukhari':bukhari_pdf, 'muslim': muslim_pdf, 'nasai':nasai_pdf, 'abu':abu_pdf, 'tirmidhi':tirmidhi_pdf, 'ahmad':ahmad_pdf, 'ibn': ibn_pdf, 'ahmed':ahmad_pdf}
    splitted = message.text.split()
    for q in had_code:
        for i in splitted:
            if q in i.lower():
                book = had_code[q]
    for q in book:
        sendHadithpdf(message.chat.id, q)
    return "The books have been downloaded."

def show_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Verify Hadith 🔍", "Download Book 📖")
    bot.send_message(chat_id, "What would you like to do next?", reply_markup=markup)

def show_down_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    row = [
        markup.row("Sahih Bukhari", "Sahih Muslim"),
        markup.row("Sunan Nasai", "Sunan Tirmidhi"),
        markup.row("Sunan Abu Dawood", "Sunan Ibn Majah"),
        markup.row("Musnad Ahmad")
        ]
    
    bot.send_message(chat_id, "Select the book that you want to download.", reply_markup=markup)
@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id,
                    "Assalamualaikum "+ message.chat.first_name+", \nWelcome to Hadith Verification bot v2.0 . In this bot you can verify grade or authenticity of a hadith from the following books:\n\n1) Sahih Bukhari\n2) Sahih Muslim\n3) Sunan Nasai\n4) Sunan Abu Dawood\n5)Sunan Tirmidhi\n6) Sunan Ibn Majah\n7) Musnad Ahmad (only upto Hadith No. 1438)\n8) Al-Adab Al-Mufrad\n\nYou can also download PDFs of following books \n1) Sahih Bukhari\n2) Sahih Muslim\n3) Sunan Nasai\n4) Sunan Abu Dawood\n5)Sunan Tirmidhi\n6) Sunan Ibn Majah\n7) Musnad Ahmad (3 Volumes)\n\nType or click on:\n/help to see instructions and query submissions details again.\n/random to see a random hadith.\nat anytime.\n\nContact @abdulmuizz0903 or mail us at saeedabdulmuizz@gmail.com for any queries or suggestions.\n\nTo get started Click on Verify Hadith and send the Hadith number with book (like this <i><b>Sahih Bukhari 1035</b></i>) and this bot will send the full hadith back to you with its Grade(Sahih, Dai'f, Maudu, etc.) IF IT IS NOT FROM SAHIHAIN(Bukhari and Muslim).\n\nTo support us please share this bot and make Dua of hidayah for the creator of this bot\n\nClick the required button to Get Started",
                    parse_mode='HTML'
                    )
    show_menu(message.chat.id)
    log(message, "Started")
    id = open("id.txt", "+a")
    id.write("," + str(message.chat.id))
    id.close()

@bot.message_handler(commands=["random"])
def randomHadith(message):
    send_message(message.chat.id, verify_hadith('bukhari', random.randrange(1, 7563, 1)))
    log(message, "Random Hadith")

@bot.message_handler(func=lambda message: "Verify Hadith" in message.text)
def receive_hadith(message):
    bot.send_message(message.chat.id, 'Please send the Hadith name and Number. For example <i>"Sahih Bukhari 100"</i>', parse_mode='HTML')

@bot.message_handler(func=lambda message: "Download Book" in message.text)
def receive_book_request(message):
    show_down_menu(message.chat.id)

    
@bot.message_handler(func=lambda message: True)
def receive_input(message):
    if message.text == "Verify Hadith":
        bot.send_message(message.chat.id, "Please send me the hadith name and number.")
    elif message.text == "Download Book":
        bot.send_message(message.chat.id, "Please send me the book text.")
    else:
        try:
            had_code = {'bukhari':'bukhari', 'muslim': 'muslim', 'nasai':'nasai', 'abu':'abudawud', 'adab': 'adab', 'tirmidhi':'tirmidhi', 'ahmad':'ahmad', 'ibn': 'ibnmajah', 'ahmed':'ahmad'}
            splitted = message.text.split()
            for q in had_code:
                for i in splitted:
                    if q in i.lower():
                        book = had_code[q]
            for q in splitted:
                if q.isdigit() == True:
                    hadith = q
            verified_hadith = verify_hadith(book, hadith)
            log(message, "Verified Hadith")
            send_message(message.chat.id, verified_hadith)
            show_menu(message.chat.id)
        except:
            try:
                downloaded_book = download_book(message)
                log(message, "Downloaded Book")
                bot.send_message(message.chat.id, downloaded_book)
                show_menu(message.chat.id)
            except:
                bot.send_message(message.chat.id, "Wrong Input. Enter Correct Input. To verify hadith please select verify hadith and then send the hadith details.")
                show_menu(message.chat.id)
                log(message, "Wrong Input")
bot.infinity_polling()

