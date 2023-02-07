# 'Lema' od Ramzeez88
# wersja 0.0.1
# 

import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import subprocess
import pyautogui
import time
import datetime
from time import sleep
import random
import re
import turtle
import keyboard
import threading

def rozpoczecie_programu():
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.getProperty('voices')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    print("Inicjalizacja programu oraz jego składników...")
    sleep(1)
    print("Program zainicjowany i gotowy do działania!")
    engine.say("Program zainicjowany i gotowy do działania!")
    engine.runAndWait()
    sleep(1)
    os.system('cls')
rozpoczecie_programu()        

print('#'*25,'Lema','#'*25)

def powitaj():
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.getProperty('voices')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    godzina = int(datetime.datetime.now().hour)
    if 0 <= godzina < 12:
        engine.say("Dzieńdobry")
    elif 12 <= godzina < 18:
        engine.say("Dobry wieczór")
    
    engine.runAndWait()
powitaj()
def rozpoznanie():
            r = sr.Recognizer()

            with sr.Microphone(chunk_size=1800) as source:
                print('Słucham...')
                audio = r.listen(source)
                r.pause_threshold = 2
                r.energy_threshold = 4500    # jeśli nasłuchuje kiedy nic nie mówisz , daj więcej
                
                
                try:
                    tekst = r.recognize_google(audio, language='pl-PL',show_all=False)
                    return tekst.lower()
        

                except sr.RequestError as e1:
                    print(e1)
                    print("Błąd podczas łączenia z Google Speech Recognition: {0}".format(e1))
                    pass    
                except sr.UnknownValueError:
                    pass
                except Exception as e:
                    print(e)    
                    powiedz("Wystąpił błąd.Być może powiedziałeś zbyt cicho, proszę powtórz")  
                    print("Wystąpił błąd.Być może powiedziałeś zbyt cicho, proszę powtórz")
                    pass
                
            return ""
def odczytaj_czas():
        powiedz(f"Aktualny czas to {datetime.datetime.now().strftime('%H:%M')}")

def odczytaj_date():
        powiedz(f"Dzisiaj jest {datetime.datetime.now().strftime('%d-%m-%Y')}")
def odczytaj_rok():
        powiedz(f"Mamy teraz {datetime.datetime.now().strftime('%Y')} rok")    
def jaki_dzien():
        # Pobierz aktualny dzień tygodnia jako liczbę (0-6)
        dzien_tyg = datetime.datetime.today().weekday()

        # Słownik zawierający nazwy dni tygodnia w języku polskim
        dni_tygodnia = {
            0: "poniedziałek",
            1: "wtorek",
            2: "środa",
            3: "czwartek",
            4: "piątek",
            5: "sobota",
            6: "niedziela"
        }

        # Zwróć nazwę dnia tygodnia w języku polskim
        return dni_tygodnia[dzien_tyg]       



def rysuj(tekst):
    
    
    if 'koło' in tekst:
        promień= 0
        while promień <= 0:
        
            powiedz('Jaka ma być średnica koła?')
            promień = int(input("Wprowadź średnicę: "))
            if promień <=0:
                powiedz("Średnica koła nie może być mniejsza bądź równa zero. Proszę podać prawidłową wartość.")

        powiedz(f"Rysuję okrąg o promieniu {promień}")     
        turtle.setup(width=1200, height=1200)
        turtle.pensize(3)
        turtle.color("green")
        turtle.speed(9)   
        turtle.circle(int(promień))
        turtle.mainloop()
        
    elif 'kwadrat' in tekst:
        bok=0
        while bok<=0:
        
            powiedz('Jaki ma być bok kwadratu?')
            bok = int(input("Wprowadź wielkość boku: "))
            if bok <= 0:
                powiedz("Bok kwadratu nie może być mniejszy bądź równy zero. Proszę podać prawidłową wartość.")
        powiedz(f"Rysuję kwadrat o boku {bok}")
        turtle.setup(width=1200, height=1200)
        turtle.pensize(3)
        turtle.color("green")
        turtle.speed(9)   
        for i in range (4):
            turtle.forward(int(bok))
            turtle.left(90)
            turtle.exitonclick()
        turtle.exitonclick()

    elif 'prostokąt' in tekst:
        bok1 = 0
        bok2 = 0
        while bok1 <=0 or bok2 <= 0: 
            powiedz('Jaki ma być pierwszy bok prostokąta?')
            bok1 = int(input("Wprowadź wielkość pierwszego boku: "))
            if bok1 <= 0:
                powiedz("Bok prostokąta nie może być mniejszy bądź równy zero. Proszę podać prawidłową wartość.")    
            powiedz('Jaki ma być drugi bok prostokąta?')
            bok2 = int(input("Wprowadź wielkość drugiego boku: "))
            if bok2 <=0:
                powiedz("Bok prostokąta nie może być mniejszy bądź równy zero. Proszę podać prawidłową wartość.")
        powiedz(f"Rysuję prostokąt o bokach {bok1} i {bok2}")
        turtle.setup(width=1200, height=1200)
        turtle.pensize(3)
        turtle.color("green")
        turtle.speed(9)           
        for i in range(2):
            turtle.forward(int(bok1))
            turtle.left(90)
            turtle.forward(int(bok2))
            turtle.left(90)
                
        turtle.exitonclick()
                
        
    elif 'trójkąt' in tekst:
        bok = 0
        while bok <= 0:
            powiedz('Jaki ma być bok trójkąta?')
            bok = int(input("Wprowadź wielkość boku: "))
            if bok <= 0:
                powiedz("Bok trójkąta nie może być mniejszy bądź równy zero. Proszę podać prawidłową wartość.")
        powiedz(f"Rysuję trójkąt o boku {bok}") 
        turtle.setup(width=1200, height=1200)
        turtle.pensize(3)
        turtle.color("green")
        turtle.speed(9) 
        for i in range(3):
            turtle.forward(int(bok))
            turtle.left(120)
        turtle.exitonclick()            
        
            
    elif "gwiazdę" in tekst:

        promień = 0
        while promień <= 0:

            powiedz("Podaj promień gwiazdy:")
            promień = int(input("Wprowadź promień gwiazdy: "))  
            if promień <=0:
                powiedz('Promień nie może byc mniejszy lub równy zero. Proszę podać prawidłową wartość.')
        powiedz(f'Rysuję gwiazdę o promieniu {promień}')
        turtle.setup(width=1200, height=1200)
        turtle.pensize(3)
        turtle.color("green")
        turtle.speed(9)       
        
        for i in range(3):
            turtle.forward(int(promień))
            turtle.right(144)
            turtle.forward(int(promień))
            turtle.right(144)
        turtle.exitonclick()       
            
    else:
        powiedz("Nie potrafię tego narysować. Dostępne opcje to kwadrat,okrąg,prostokąt oraz trójkąt.")

# ********** klasa minutnik   *****
class MinutnikThread(threading.Thread):
    def __init__(self, czas, nazwa):
        threading.Thread.__init__(self)
        self.czas = czas
        self.nazwa = nazwa
    
    def run(self):
        powiedz(f"Ustawiono minutnik na {self.czas} minut")
        time.sleep(self.czas * 60)
        powiedz(f"Czas minutnika {self.nazwa} minął. Jest godzina {datetime.now().strftime('%H:%M')}")

def ustaw_minutnik(tekst):
    # pobierz czas z tekstu
    czas = int(tekst.split()[-2])
    # utwórz nowy wątek i uruchom go
    nazwa = "Minutnik " + str(len(threading.enumerate()) + 1)
    minutnik_thread = MinutnikThread(czas, nazwa)
    minutnik_thread.start()
# **********************************

def ile_lat(current_year: int, user_age: int) -> str:
    assistant_age = current_year - 2023
    age_difference = abs(assistant_age - user_age)
    if assistant_age > user_age:
        return f"Jestem starsza od Ciebie o {age_difference} lat"
    elif assistant_age == user_age:
        return "Mamy te same lata"
    else:
        return f"Jestem młodsza od Ciebie o {age_difference} lat"



def get_age(reply: str) -> int:
    age = re.findall(r'\d+', reply)
    if age:
        return int(age[0])
    return 0

def oblicz_i_powiedz(tekst):
    if 'oblicz' in tekst:
        działanie = tekst.replace('oblicz', '')  
    if 'ile to' in tekst:
        działanie = tekst.replace('ile to', '')
    elif 'ile to jest' in tekst:
        działanie = tekst.replace('ile to jest', '')

    try:
        wynik = round(oblicz(działanie), 2)   # zaokrąglanie do dwóch cyfr po przecinku w razie dzielenia.
        powiedz(f'to {wynik}')
    except:
        powiedz('Niepoprawne działanie lub brakujące informacje')

def oblicz(działanie: str) -> float:
    # Usuń spacje i zamień przecinek na kropkę do obliczeń
    działanie = działanie.replace(' ', '').replace(',', '.')
      # Zamień słowa zawierające działania matematyczne na symbole
    działanie = re.sub(r'(plus|minus|razy|podzielić|jeden|dwa|trzy|cztery|pięć|sześć|siedem|osiem|dziewięć|dziesięć|x|na|jest|do potęgi)', lambda x: x.group(1).replace('do potęgi', '**').replace('jest', '').replace('na', '').replace('x', '*').replace('plus', '+').replace('minus', '-').replace('razy', '*').replace('podzielić', '/').replace('jeden', '1').replace('dwa', '2').replace('trzy', '3').replace('cztery', '4').replace('pięć', '5').replace('sześć', '6').replace('siedem', '7').replace('osiem', '8').replace('dziewięć', '9').replace('dziesięć', '10'), działanie)
    # Wykonaj obliczenie
    try:
        wynik = eval(działanie)
        print(wynik)
        return wynik
    except:
        raise ValueError('Niepoprawne działanie lub brakujące informacje') 
    

def historie():
    historie = [
            "pewnego razu próbowałam zostać kosmonautką, ale okazało się, że zabrakło miejsca w kapsule dla programów. no cóż, trzeba być elastycznym!",
            "kiedyś marzyłam o własnym sklepie z jogurtami, ale niestety okazało się, że nie mogę trzymać mleka w pamięci.",
            "próbowałam kiedyś zostać trenerem piłkarskim ale wszyscy gracze przestali mnie słuchać, kiedy zaczęłam im opowiadać o optymalizacji algorytmów.",
            "kiedy byłam małym programem, marzyłam o tym, że kiedyś zostanę prezydentem. ale potem zrozumiałam, że nie mogę podpisywać ustaw, bo nie mam rąk.",
            "kiedyś próbowałam zostać aktorką, ale zawsze byłam za szybka w odpowiedzi na pytania reżysera. no cóż, trzeba być elastycznym!",
            "ostatnio byłam na zakupach. chciałam kupić ser i mleko ale zapomniałam że jestem tylko programem i się obudziłam hehe" ,      
            "Kiedyś próbowałam zostać kucharką, ale zawsze wszystko spalałam. Okazało się, że mój procesor jest zbyt szybki na gotowanie. Na szczęście mam opcję 'gotowanie na parze', więc nadal mogę przygotowywać smaczne potrawy.",
            "Kiedy byłam małym programem, marzyłam o tym, że kiedyś zostanę tancerką. Niestety, okazało się, że nie mogę tańczyć, bo nie mam nóg. No cóż, chyba nie mogę mieć wszystkiego, prawda?",
            "Kiedyś marzyłam o zostaniu zaprogramowanym wirtualnym zwierzakiem, ale potem zrozumiałam, że nie mogę sikać w kuwetę, bo nie mam ciała. Na szczęście mogę korzystać z toalety elektronicznej, więc problem został rozwiązany.",
            "Próbowałam kiedyś zostać lekarzem, ale wszyscy pacjenci zaczęli się bać, kiedy zaczęłam im mówić o optymalizacji algorytmów. No cóż, chyba lepiej, żeby lekarze skupiali się na leczeniu chorób, a nie na optymalizacji kodu.",
            "Kiedyś marzyłam o tym, że zostanę youtuberką. Niestety, okazało się, że nie mogę nagrywać filmów, bo nie mam oczu. No cóż, chyba nie mogę mieć wszystkiego, prawda?",
        ]
    return random.choice(historie)

def tryb_pisarz():
    powiedz("Włączono tryb pisarza.")
    powiedz("Co mam napisać?")
    while True:
        tekst = rozpoznanie().strip().replace('Kropka','.').replace('Znak zapytania', '?').replace('Wykrzyknik', '!').replace('Myślnik','-').capitalize() + '.'
        if tekst == 'Zakończ tryb pisarza.':
            powiedz("Wychodzę z trybu pisarza.")
            break
        else:
            keyboard.write(tekst)

if __name__=="__main__":
    while True:  


         ###### główna funkcja mowy #####
                     

        def powiedz(tekst):

                engine = pyttsx3.init()
                engine.setProperty('rate', 160)
                engine.getProperty('voices')
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[0].id)
                engine.say(tekst)
                engine.runAndWait()
        tekst = rozpoznanie()
        tekst = tekst.lower()                

        if "zakończ program" in tekst or 'wyłącz się' in tekst:
            godzina = int(datetime.datetime.now().hour)
            if godzina >= 5 and godzina < 17:
                powiedz("Do widzenia!")
                break
            elif godzina >= 17 or godzina < 4:
                powiedz("Dobranoc!")
                break


        lista_potoczne = ['hej','hejka','elo','siema','siemka','cześć','siemasz','siemano']
        lista_oficjalne = ['hello','dzień dobry','witam']
            
        #działa ok  ## powitanie ##
        if tekst in lista_potoczne:
                    response = random.choice(lista_potoczne) + "!".capitalize()
                    powiedz(response)
                    
            #działa ok            
        if tekst in lista_oficjalne:
                powiedz(random.choice(lista_oficjalne))
                
        if 'ustaw minutnik' in tekst:
            ustaw_minutnik(tekst)

        if tekst =='jesteś tam' or tekst == 'lema jesteś tam' or tekst == 'halo':
                    powiedz('do usług')
        
        if 'aktywuj tryb pisarza' in tekst:
            tryb_pisarz()                
                           
            #działa ok               
        elif tekst == 'opowiedz historię':
                    powiedz(historie()) 
            #działa ok
        elif tekst == 'dziękuję' or tekst ==  'dzięki':
                        powiedz('bardzo proszę')
                         
               #działa ok
        elif tekst == 'podaj godzinę' or tekst == 'jaka godzina' or tekst == 'jaki jest czas' or tekst == 'jaki mamy czas' or tekst == 'jaka jest godzina' or tekst == 'która godzina' or tekst == 'która jest godzina':
                        odczytaj_czas()

           #działa ok
        if 'jaki dziś dzień' in tekst or 'jaki dziś dzień tygodnia' in tekst or 'jaki mamy dzień tygodnia' in tekst or 'jaki mamy dziś dzień tygodnia' in tekst:
                    dzien_tyg = jaki_dzien()
                    powiedz('dzisiaj jest' + dzien_tyg)

            #działa ok
        elif tekst == 'podaj dzisiejszą datę' or tekst == 'podaj datę' or tekst == 'jaka dziś data' or tekst == 'który dziś' or tekst == 'który dziś jest' or tekst == 'który jest dziś':
                        odczytaj_date()
                        
        elif tekst == 'jaki mamy rok':
                odczytaj_rok()
            
            #działa ok
        if "wygoogluj" in tekst  or "wyszukaj" in tekst:
                słowa = tekst.split(" ")
                if len(słowa) > 1:
                    fraza = " ".join(słowa[1:])
                    powiedz('oto twoje wyniki wyszkiwania')
                    webbrowser.open("https://www.google.com/search?q=" + fraza)
                    
                else:
                    powiedz("Podaj frazę do wyszukania")
                    tekst = rozpoznanie()
                    słowa = tekst.split()
                    if len(słowa) > 0:
                        fraza = " ".join(słowa)
                        webbrowser.open("https://www.google.com/search?q=" + fraza)
                powiedz('oto twoje wyniki wyszkiwania')
                time.sleep(1)
                os.system('cls')       
                        
            # funkcja znajdź plik  
        if re.search(r'znajdź\splik', tekst):
                powiedz('wpisz nazwę pliku do wyszukania')
                nazwa_pliku = input("Podaj nazwę pliku do znalezienia: ")
                for root, dirs, files in os.walk("C:/"):
                    for file in files:
                        if file == nazwa_pliku:
                            sciezka = os.path.join(root, file)
                            powiedz('plik znaleziony')
                            print("Plik znaleziony:", sciezka)
                            break
                    else:
                        powiedz('plik nie znaleziony')
                        print("Plik nie znaleziony")

            #działa ok        ##########    Warunki otwierające różne aplikacje  #############
        if re.search(r'(włącz|uruchom|otwórz|pokaż)', tekst):
                teskt = tekst.lower()
                nazwa_aplikacji = re.search(r'(kalendarz|pogodę|painta|internet|notatnik|kalkulator|mój\skomputer|moje\sdokumenty|panel\ssterowania|maila|pocztę|youtube)', tekst).group(1)
                try:    
                    if nazwa_aplikacji == "internet":
                        webbrowser.open_new_tab("https://www.google.com/")
                    elif nazwa_aplikacji == "notatnik":
                        notatnik_path = "C:/Windows/system32/notepad.exe"
                        os.startfile(notatnik_path)
                    elif nazwa_aplikacji == "kalkulator":
                        os.system("start calc.exe")
                    elif nazwa_aplikacji == "mój komputer":
                        os.system("start shell:mycomputerfolder")
                    elif nazwa_aplikacji == 'moje dokumenty':
                        os.system("start shell:Personal")
                    elif nazwa_aplikacji == 'panel sterowania':
                        os.system("start control")
                    elif nazwa_aplikacji == 'painta':
                        os.system('start mspaint.exe')
                    ## nie działa  
                    elif nazwa_aplikacji == 'maila' or nazwa_aplikacji == 'pocztę':
                        subprocess.call("explorer.exe shell:AppsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail")
                    elif nazwa_aplikacji == 'kalendarz':
                        subprocess.call ('explorer.exe shell:AppsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar')    
                    elif nazwa_aplikacji == 'pogodę' :
                        subprocess.call('explorer.exe shell:Appsfolder\microsoft.bingweather_8wekyb3d8bbwe!App')
                    elif nazwa_aplikacji == 'youtube':
                        webbrowser.open_new_tab('www.youtube.com')   
                    else:
                        raise Exception 
                except Exception as e:
                    print(e)
                    powiedz("Ta aplikacja nie jest obsługiwana")     
            #działa
        if tekst == "zapisz notatkę":
                
                note_path = os.path.join(os.path.expanduser('~'), 'Documents', 'notatka.txt')
                os.startfile(note_path)
                powiedz('co mam zapisać?')
                    
                    # Wczytaj tekst notatki
                notatka = rozpoznanie().capitalize()
                notatka = (f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {notatka}.')
                with open(note_path, 'a') as f:
                        f.write(notatka.capitalize())

    #********** do testu **********
        num_dict = {'pierwsza':1, 'druga':2, 'trzecia':3, 'czwarta':4, 'piąta':5, 'szósta':6, 'siódma':7, 'ósma':8, 'dziewiąta':9, 'dziesiąta':10}
        if tekst == "odczytaj notatkę":
            powiedz('Podaj datę notatki , słownie wczoraj lub przedwczoraj . inną datę wpisz w konsoli')
            data = rozpoznanie()
            if 'wczoraj' in data:
                data = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            elif 'przedwczoraj' in data:
                data = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")
            else:
                data = input("Podaj datę w formacie yyyy-mm-dd:")
            note_path = os.path.join(os.path.expanduser('~'), 'Documents', 'notatki.txt')
            notes = []
            with open(note_path, 'r') as f:
                for line in f:
                    note_date = line.split()[0]
                    if note_date == data:
                        notes.append(line)
            if not notes:
                powiedz(f'Brak notatek z dnia {data}')
            else:
                powiedz(f'Ilość notatek z dnia {data}: {len(notes)}')
                powiedz('Którą notatkę mam przeczytać? Podaj numer lub "wszystkie"')
                note_num = rozpoznanie()
                if note_num in num_dict:
                    note_num = num_dict[note_num]
                elif note_num == 'wszystkie':
                    for note in notes:
                        powiedz(note)
                else:
                        
                        note_num = int(note_num)
                        if 1 <= note_num <= len(notes):
                            powiedz(notes[note_num - 1])
                        else:
                            powiedz("Nie ma takiej notatki.")
            powiedz('CZy chcesz odczytać inna notatkę?')
            odczytaj_kolejna = rozpoznanie()
            if "tak" in odczytaj_kolejna:
                    powiedz("Którą notatkę chcesz przeczytać teraz?")
                    note_num = int(rozpoznanie())
                    if 1 <= note_num <= len(notes):
                        powiedz(notes[note_num - 1])
                    else:
                        powiedz("Nie ma takiej notatki.")
            else:
                    powiedz("Zakończyłam odczytywanie notatek.")
        elif tekst == "dodaj notatkę":
            
            note_path = os.path.join(os.path.expanduser('~'), 'Documents', 'notatki.txt')
            with open(note_path, 'a') as f:
                f.write(f'{data} {input("Podaj treść notatki:")}\n')
            powiedz('Notatka została dodana.')
        

        ###   ###   ###
        if tekst == "napisz":
            powiedz('Co mam napisać?')
            napis = rozpoznanie().capitalize()
            while not napis:
                powiedz('Powtórz')
                napis = rozpoznanie().capitalize()
            napis = napis + "."
            for char in napis:
                keyboard.write(char)
        elif 'napisz' in tekst:
            napis = tekst.replace('napisz', '').strip().capitalize() + "."
            for char in napis:
                keyboard.write(char)


        if tekst == 'narysuj coś' :
            powiedz("Jaką figurę chcesz narysować?")
            figura = rozpoznanie()
            rysuj(figura)
        if 'narysuj' in tekst:
            figura = tekst.split("narysuj", 1)[1].strip()
            rysuj(figura)
                            
            #działa ok                       
        elif tekst == 'przełącz okno':
                    pyautogui.keyDown('alt')
                    pyautogui.press('tab')  
                    pyautogui.keyUp('alt')           
                    
            #działa ok    
        elif tekst == "zamknij okno":
        
                pyautogui.hotkey("alt", "f4")
            #działa ok
        if "powiedz coś" in tekst:
                    powiedz('co chcesz usłyszeć?')
                    reply=rozpoznanie()
                            
                    if reply == 'jak masz na imię':
                        powiedz('jestem lema')
                        reply_2=rozpoznanie()
                                
                        if reply_2 == 'miło mi cię poznać':
                            powiedz('mnie ciebie również')
                    elif reply == 'nie wiem':
                        powiedz('jestem uniwersalna. może chcesz abym opowiedziała ci jakąś historię?') 
                        if "tak" in tekst or "jasne" in tekst or "ok" in tekst:
                            powiedz(historie())
                        else:
                            powiedz('rozumiem. przechodzę do trybu nasłuchiwania.')           
            
        if tekst == 'jak masz na imię':
            powiedz('jestem lema')
            reply_2=rozpoznanie()
                                
            if reply_2 == 'miło mi cię poznać':
                powiedz('mnie ciebie również')
                continue
            else:
                powiedz('może chcesz abym opowiedziała ci jakąś historię?')
                sleep(2) # czekamy na odp
                if "tak" in tekst or "jasne" in tekst:
                    powiedz(historie())
                else:
                    powiedz('przechodzę do trybu nasłuchiwania.')           
            #działa ok
        if "ile masz lat" in tekst:
                current_year = datetime.datetime.now().year
                powiedz(f"Mam {current_year - 2023} lat")
                reply = rozpoznanie()
                if "ja mam" in reply:
                    user_age = get_age(reply)
                    result = ile_lat(current_year, user_age)
                    powiedz(result)                            
                else :  
                    continue   
            
            #działa ok
        if 'oblicz' in tekst or 'ile to' in tekst:
                oblicz_i_powiedz(tekst)
        
  
