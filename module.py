from gtts import gTTS
import os
sonastik={}
riigid=[]
linnad=[]
file=open("riigid_pealinnad.txt","r")
for line in file:
    k, v=line.strip().split("-")
    sonatik[k.strip()]=v.strip()
    Countries.append(k)
    Capitals.append(sonatik[k.strip()])
file.close()
print(sonastik)
print("Riigid: ")
print(riigid)
print("Pealinnad: ")
print(linnad)
s=gTTS(text=linnad[8],lang="et",slow=False).save("heli.mp3")
os.system("heli.mp3")
a=input()