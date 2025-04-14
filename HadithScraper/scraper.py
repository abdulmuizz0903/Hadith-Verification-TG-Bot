import requests
from bs4 import BeautifulSoup

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