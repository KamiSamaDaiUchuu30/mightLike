import csv
import random


songLib = [row for row in csv.reader(open("ptSongLib.tsv", encoding='utf-8'),delimiter="\t")]
#change string into intger
def change(val):
  for song in range(len(songLib)):
    songLib[song][val] = int(songLib[song][val])
def lowercase(val):
  for song in range(len(songLib)):
    songLib[song][val].lower
 # compare intger                                               
def compare(user, ele, col, lis):
  for x in range(len(ele)):
    if (abs(user - ele[x][col]) < 2):
      lis.append(ele[x])
      #compare string
def compareSt(user, ele, col,lis):
  for x in range(len(ele)):
    if (user == ele[x][col]):
      lis.append(ele[x])
 #compare genre     
def comparegen(user, ele, col,lis):
  for x in range(len(ele)):
    if (user == ele[x][col] or (user == ele[x][col+1])):
      lis.append(ele[x])
#check amount of song
def length(length,ele):
  if(len(length) == 1):
    print(length[0][0])
    global t
    t = True
  elif(len(length) == 0):
    print("cant match any song")
    print("try these song")
    for x in range(len(ele)):
      print(ele[x][0])
    t = True
# ask question
def askintQ(check, uanswer, data):
    while check == False:
        try:
          print("Please rate the",data,"of your song.")
          uanswer = int(input("Rate it from 1 to 10.  "))
          #check if answer in range
          if 0 < uanswer < 11:           
            check = True
            global uAdd
            uAdd = uanswer
          #outside range
          else:
            print("your rating outside range of 1 to 10")   
    #check if user putted a string or float
        except ValueError:
            print("you inputted a letter. We do not aceapt letter")
 #ask year           
def askyearQ(check, uanswer, data):
    while check == False:
        try:
          print("Please put in the",data,"of your song.")
          uanswer = int(input("(1900 to 2019 only)"))
          #check if answer in range
          if 1900 < uanswer < 2020:           
            check = True
            global uAdd
            uAdd = uanswer
          #outside range
          else:
            print("your year outside range")   
    #check if user putted a string or float
        except ValueError:
            print("you inputted a letter. We do not aceapt letter")
#ask string question
def askstrQ(check, uanswer, data,choice):
    while check == False:
        try:
          print("Please put in the",data,"of your song.")
          uanswer = str(input(choice))
          #check if answer in range
          uanswer.lower
          global ustring
          ustring = uanswer
          check = True
            
    #check if user putted a string or float
        except ValueError:
            print("you inputted a letter. We do not aceapt letter")
songLib = tuple(songLib)
rhy = []
mel = []
temp = []
lyr = []
mood = []
year = []
lang = []
genre = []
a = 10

uRhy = 0 
uMel = 0
uTemp = 0
uLyr = 0
uMood = str("")
uYear = 0
uLang = str("")
uGenre = str("")
global t
global uAdd
global ustring
uAdd = 0
ustring = ("")
check = False
t = False
#choice
uMAnswer = str("depress, sad, happy, upbeat")
#ask int question
askintQ(check, uRhy, "rhythm")
uRhy += uAdd
askintQ(check, uMel, "melody")
uMel += uAdd
askintQ(check, uTemp, "tempo")
uTemp += uAdd
askintQ(check, uLyr, "lyric")
uLyr += uAdd
askyearQ(check,uYear,"year")
uYear += uAdd

#ask str question
askstrQ(check,uMood,"mood", uMAnswer)
uMood = ustring
askstrQ(check, uLang, "language", "offcial real language")
uLang = ustring
askstrQ(check, uGenre, "genre", "real offcial name of genre")
uGenre = ustring



#change string to intger
change(4)
lowercase(3)
lowercase(5)
lowercase(6)
lowercase(8)

for i in range(7):
  change(i+a)
while t == False:
  compare(uRhy, songLib, 14, rhy)
  length(rhy,songLib)
  compare(uMel, rhy, 13, mel)
  length(mel,rhy)
  compare(uTemp, mel, 16, temp)
  length(temp,mel)
  compare(uLyr, temp, 11, lyr)
  length(lyr,temp)
  compareSt(uMood, lyr, 8, mood)
  length(mood,lyr)
  compareSt(uYear, mood, 4, year)
  length(year,mood)
  compareSt(uLang, year, 3, lang)
  length(lang,year)
  comparegen(uGenre, lang, 5, genre)
  length(genre,lang)



 
    
    
