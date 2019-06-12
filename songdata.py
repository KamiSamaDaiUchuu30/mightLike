import csv
import random


songLib = [row for row in csv.reader(open("ptSongLib.tsv", encoding='utf-8'),delimiter="\t")]
def change(val):
  for song in range(len(songLib)):
    songLib[song][val] = int(songLib[song][val])
                                                
def compare(user, ele, col, lis):
  for x in range(len(ele)):
    if (abs(user - ele[x][col]) < 2):
      print(ele[x][0])
      lis.append(ele[x])
def compareSt(user, ele, col,lis):
  for x in range(len(ele)):
    if (user == ele[x][col]):
      print(ele[x][0])
      lis.append(ele[x])
      
def comparegen(user, ele, col,lis):
  for x in range(len(ele)):
    if (user == ele[x][col] or (user == ele[x][col+1])):
      print(ele[x][0])
      lis.append(ele[x])
def length(length):
  if(len(length) == 1):
    print(length[0][0])
    global t
    t = True
  if(len(length) == 0):
    print("cant match any song")
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
uRhy = 7
uMel = 8
uTemp = 7
uLyr = 6
uMood = str("sad")
uYear = 2017
uLang = str("English")
uGenre = str("kpop")
global t
t = False
change(4)
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





print(len(genre))
    
    
