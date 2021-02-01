import requests
import psycopg2
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup ##Εισαγωγή απαραίτητων βιβλιοθηκών

conn = psycopg2.connect("dbname=aptoide user=postgres password=boss") ##Σύνδεση με την βάση δεδομένων
#ADVENTURE GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/adventure") ##Αίτηση του html κώδικα της συγκεκριμένης ιστοσελίδας
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0 ##Αρχικοποίηση του i
for h2_tag in soup.find_all('div',class_='apps-list-container'): 
	links = h2_tag.findAll('a') ##Έυρεση όλων των tag "a" μέσα στην κλαση "apps-list-container" του html κώδικα
for a in links:
        mystring2 = a['href']
##Το href αναφέρεται σε ιστοσελίδες που περιέχονται μέσα στο "a" tag. Στην συγκεκριμένη περίπτωση οι 50 κορυφαίες εφαρμογές της κατηγορίας adventure και εκχωρούνται στην μεταβλητή "mystring2" 
        try:
                if urllib.request.urlopen(mystring2).read(): ##Έλεγχος αν ανοίγει η κάθε ιστοσελίδα που περιλαμβάνει το "mystring2"
                        mystring = mystring2 ##Εκχώρηση της "mystring2" στην "mystring"
                duthgr = urllib.request.urlopen(mystring).read() ##Άνοιγα της ιστοσελίδας που περιέχεται στην "mystring" και εκχώρηση στην μεταβλητή "duthgr"
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'): ##Έυρεση των "h1" tag που περιλαμβάνει τα ονόματα των εφαρμογών
                        appname = h3_tag.text ##Παίρνουμε μόνο το κείμενο που περιλαμβάνεται μέσα στο "h1" tag
                        print(appname) ##Εκτύπωση του κειμένου δηλαδή του ονόματος της εφαρμογής
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
##Έυρεση της κλάσσης "table" με id "app-view-information-table" που περιλαμβάνει τα δικαιώματα που απαιτει η κάθε εφαρμογή
                div=newshtml[1] ##Επειδή υπήρχαν δύο κλάσεις με το ίδιο όνομα παίρνουμε μόνο αυτήν που χρειαζόμαστε
                inner_text = div.text
                strings = inner_text.split("  ") ##Παίρνουμε μόνο το κείμενο των δικαιωμάτων 
                for line in strings: ##Βρόγχος ώστε να βρει όλα τα δικαιώματα
                        print(line) ##Εκτύπωση των δικαιωμάτων
                        i=i+1 ##Μέτρηση των δικαιωμάτων
                cur = conn.cursor() ##Σύνδεση με την βάση
                cur.execute("INSERT INTO adventure_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname)) ##Εισαγωγή στοιχείων στην βάση
                i=0
        except: ##Σε περίπτωση που δεν ανοίξει κάποια ιστοσελίδα να μην σταματήσει να τρέχει ο κώδικας αλλά να βγάλει ένα κενό
                print("")
conn.commit() ##Εμφάνιση στοιχείων μέσα στην βάση


#STRATEGY GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/strategy")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO strategy_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()


#CASUAL GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/casual")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO casual_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()


#SIMULATION GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/simulation")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO simulation_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()


#ACTION GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/action")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO action_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()


#ARCADE GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/arcade")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO arcade_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()


#PUZZLE GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/puzzle")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO puzzle_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#EDUCATIONAL GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/educational")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO educational_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#ROLE_PLAYING GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/role-playing")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO role_playing_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#TRIVIA GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/trivia")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO trivia_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#WORD GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/word")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO word_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#SPORTS GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/sports-games")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO sports_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#BOARD GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/board")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO board_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#RACING GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/racing")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO racing_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#CARD GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/card")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO card_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#CASINO GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/casino")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO casino_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()




#BRAIN_PUZZLE GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/brain-puzzle")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO brain_puzzle_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#MUSIC GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/music")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO music_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#FAMILY GAMES
result = requests.get("https://gr.aptoide.com/group/games/sub/family")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO family_games(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#COMMUNICATION APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/communication")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO communication_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#EDUCATION APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/education")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO education_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()




#PRODUCTIVITY APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/productivity")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO productivity_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#BUSINESS APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/business")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO business_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#FOOD AND DRINK APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/food-drink")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO food_drink_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#TOOLS APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/tools")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO tools_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#SHOPPING APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/shopping")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO shopping_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#LIFESTYLE APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/lifestyle")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO lifestyle_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#TRAVEL AND LOCAL APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/travel-local")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO travel_local_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()




#PERSONALIZATION APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/personalization")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO personalization_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()


#SOCIAL APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/social")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO social_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#HEALTH AND FITNESS APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/health-fitness")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO health_fitness_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#PHOTOGRAPHY APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/photography")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO photography_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()


#MEDIA AND VIDEO APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/media-video")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO media_video_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#FINANCE APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/finance")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO finance_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#NEWS AND MAGAZINES APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/news-magazines")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO news_magazines_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#ENTERTAINMENT APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/entertainment")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO entertainment_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()




#WEATHER APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/weather")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO weather_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()




#SPORTS APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/sports")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO sports_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#COMICS APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/comics")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO comics_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()




#MUSIC AND AUDIO APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/music-audio")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO music_audio_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#VIDEO PLAYERS AND EDITORS APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/video-players-editors")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO video_players_editors_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#DATING APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/dating")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO dating_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#MAPS AND NAVIGATION APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/maps-navigation")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO maps_navigation_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#LIBRARIES AND DEMO APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/libraries-demo")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO libraries_demo_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#BOOKS AND REFERENCE APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/books-reference")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO books_reference_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#AUTO AND VEHICLES APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/auto-vehicles")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO auto_vehicles_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#MEDICAL APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/medical")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO medical_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#ART AND DESIGN APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/art-design")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO art_design_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#MULTIMEDIA APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/multimedia")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO multimedia_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()




#THEMES APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/themes")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO themes_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#TRANSPORT APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/transport")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO transport_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#PARENTNG APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/parenting")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO parenting_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#HOUSE AND HOME APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/house-home")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO house_home_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#HEALTH APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/health")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO health_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()



#EVENTS APPS
result = requests.get("https://gr.aptoide.com/group/applications/sub/events")
src = result.content
soup = BeautifulSoup(src, 'lxml')
i=0
for h2_tag in soup.find_all('div',class_='apps-list-container'):
	links = h2_tag.findAll('a')
for a in links:
        mystring2 = a['href']
        try:
                if urllib.request.urlopen(mystring2).read():
                        mystring = mystring2
                duthgr = urllib.request.urlopen(mystring).read()
                soup2 = BeautifulSoup(duthgr, 'html.parser') 
                for h3_tag in soup2.find_all('h1'):
                        appname = h3_tag.text
                        print(appname)
                duthgr = urllib.request.urlopen(mystring).read()
                soup = BeautifulSoup(duthgr, 'html.parser') 
                newshtml = soup.find_all('table',class_='table',id='app-view-information-table')
                div=newshtml[1]
                inner_text = div.text
                strings = inner_text.split("  ")
                for line in strings:
                        print(line)
                        i=i+1
                cur = conn.cursor()
                cur.execute("INSERT INTO events_apps(url,permi,numofperm,name) VALUES (%s,%s,%s,%s)", (mystring,inner_text,format(i),appname))
                i=0
        except:
                print("")
conn.commit()
