def nolasit_datni():
    try:
        with open("darbs.txt","r", encoding='utf8') as datne:
            saturs=datne.read()
            print(saturs)
    except FileNotFoundError:
        print("Datne nav atrasta")
if __name__=="__main__":
    nolasit_datni()