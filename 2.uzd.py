import csv 
def nolasit_datus():
    try:
        with open("darbs.csv","r", encoding="utf8") as file:
            saturs = csv.reader(file)
            for row in saturs:
                print(row[3])
    except FileNotFoundError:
        print("Fails nav atrasts!")
if __name__=="__main__":
    nolasit_datus()