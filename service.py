import random
import json
import string

fajl = "db.json"

def add(datas):
    while True:
        contQ = input("Do you want to add another user (y/n): ").lower()
        if contQ == "y":
            user_name = input("Add new user: ").lower()
            if user_name:
                new_u = {
                    "user": user_name,
                    "key": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
                }
                datas.append(new_u)
                print(f"Added the new user as: {new_u["user"]} with this key: {new_u["key"]}")
                with open(fajl, "w", encoding="UTF-8") as f:
                    json.dump(datas, f, indent=4, ensure_ascii=False)
        else:
            print("All changes is saved.")
            break

def delete():
    pass
        

def main():
    with open(fajl, "r", encoding="UTF-8") as f:
        try:
            datas = json.load(f)
        except json.JSONDecodeError:
            datas = []

    print()
    if datas: 
        for d in datas:
            for user, key in d.items():
                print(f"{user}: {key}", end="  ")
            print()
  
    print()
    contQ = input("Add data or delete? (add/del): ").lower()
    if contQ == "add":
        add(datas)
    elif contQ == "del":
        pass
    else:
        print("No changes in the file.")

main()
