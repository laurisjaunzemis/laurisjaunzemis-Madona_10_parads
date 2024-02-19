def lasit_datni():
    try:
        with open("darbs.txt","r", encoding='utf8') as datne:
            saturs=datne.readlines()
            print(saturs)
        if len(saturs)>=4:
            print("Trešās rindas saturs: ")
            print(saturs[2])
            print("Ceturtās rindas saturs: ")
            print(saturs[3])
        else:
            print("Failā nav pietiekami dudz rindu!")
    except FileNotFoundError:
        print("Datne nav atrasta")
if __name__=="__main__":
    lasit_datni()