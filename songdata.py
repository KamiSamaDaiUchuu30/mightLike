import csv
import random


songLib = [row for row in csv.reader(open("ptSongLib.tsv", encoding='utf-8'),delimiter="\t")]
#change string into intger
def change(val):
  for song in range(len(songLib)):
    songLib[song][val] = int(songLib[song][val])
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
def length(length):
  if(len(length) == 1):
    print(length[0][0])
    global t
    t = True
  elif(len(length) == 0):
    print("cant match any song")
# ask question
def askintq(check, uanswer, data):
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
uMood = str("sad")
uYear = 2017
uLang = str("English")
uGenre = str("pop")
global t
global uAdd
uAdd = 0
check = False
t = False

#ask question
askintq(check, uRhy, "rhythm")
uRhy += uAdd
askintq(check, uMel, "melody")
uMel += uAdd
askintq(check, uTemp, "tempo")
uTemp += uAdd
askintq(check, uLyr, "lyric")
uLyr += uAdd





change(4)
print(uRhy)

for i in range(7):
  change(i+a)
while t == False:
  compare(uRhy, songLib, 14, rhy)
  length(rhy)
  compare(uMel, rhy, 13, mel)
  length(mel)
  compare(uTemp, mel, 16, temp)
  length(temp)
  compare(uLyr, temp, 11, lyr)
  length(lyr)
  compareSt(uMood, lyr, 8, mood)
  length(mood)
  compareSt(uYear, mood, 4, year)
  length(year)
  compareSt(uLang, year, 3, lang)
  length(lang)
  comparegen(uGenre, lang, 5, genre)
  length(genre)



 
    
    
