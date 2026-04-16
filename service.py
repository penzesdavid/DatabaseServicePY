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

def delete(datas):
    while True:
        contQ = input("Do you want to delete another user (y/n): ").lower()
        if contQ == "y":
            user_name = input("Delete user: ").lower()
            if user_name:
                for d in datas:
                    if d["user"] == user_name:
                        datas.remove(d)
                        print(f"Deleted the user: {user_name}")
                        with open(fajl, "w", encoding="UTF-8") as f:
                            json.dump(datas, f, indent=4, ensure_ascii=False)
            else:
                print("User not found.")
        else:
            break

def newkey(datas):
    while True:
        contQ = input("Do you want a new key for user (y/n): ").lower()
        if contQ == "y":
            user_name = input("user: ").lower()
            if user_name:
                for d in datas:
                    if d["user"] == user_name:
                        print(f"Current key for this user: {d["key"]}")
                        new = input("Input the custom key: ")
                        if new:
                            d["key"] = new
                            #error: not working because i dont do to write over the existed file
            else:
                print("User not found.")
        else:
            break
    

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
  
    print(datas)
    print()
    contQ = input("Add data or delete? (add/del/get new key (key!get) ) or Exit: ").lower()
    if contQ == "add":
        add(datas)
    elif contQ == "del":
        delete(datas)
    elif contQ == "key!get":
        newkey(datas)
    else:
        print("No changes in the file.")

main()
