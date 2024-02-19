def nolasit_failu(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Fails '{file_path}' nav atrasts.")
def galvenais():
    try:
        file_name = input("Ievadi faila nosaukumu: ")
        file_extension = input("Ievadi faila paplašinājumu: ")
        file_path = f"{file_name}.{file_extension}"
        nolasit_failu(file_path)
    except Exception as e:
        print(f"Radās kļūda: {e}")

galvenais()