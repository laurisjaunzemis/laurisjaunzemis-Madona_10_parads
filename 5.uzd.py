koks=input("Ievadi tekstu")
def uzraksti_vardu():
    try:
        with open("Teksts.txt","a", encoding="utf8") as datne:
            datne.write(koks+'\n')
            print("Ir ierakstīts")
    except Exception as e:
        print(f"Kļūda: {e}")
if __name__=="__main__":
    uzraksti_vardu()