import random
import json
import string

fajl = "db.json"

def add(datas):   
    new_u = {
        "user": input("Add new user: ").lower(),
        "key": ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
    }
    datas.append(new_u)
    print(f"Added the new user as: {new_u["user"]} with this key: {new_u["key"]}")
    with open(fajl, "w", encoding="UTF-8") as f:
        json.dump(datas, f, indent=4, ensure_ascii=False)
        

def main():
    with open(fajl, "r", encoding="UTF-8") as f:
        try:
            datas = json.load(f)
        except json.JSONDecodeError:
            datas = []

    if datas: 
        for elem in datas:
            for kulcs, ertek in elem.items():
                print(f"{kulcs}: {ertek}", end="  ")
            print()
  
    contQ = input("Do you want to add data? (y/n): ").lower()
    if contQ == "y":
        add(datas)
    else:
        print("No changes in the file.")

main()
