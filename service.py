import random
import string

users_datas = []
new_users = []

def add(users_datas, new_users):    
    new_u = {
        "user": input("Add new user: ").lower(),
        "key": ''.join(random.choices(string.ascii_letters+ string.digits, k=8)),
    }
    users_datas.append(new_u)
    new_users.append(new_u)
    print(f"Added the new user as: {new_u["user"]} with this key: {new_u["key"]}")

def  finalize(db, new_users):
    contQ = input("Do you want to confirm the saves? (y/n): ").lower()
    if contQ == "y":
        for u in new_users:
            db.write(u)
        print("All user is saved.")
    else:
        db.close()
        print("No changes in the file.")

        

def main():
    db = open("db.txt",encoding="UTF-8")
    db.readline()
    for lines in db:
        datas = lines.strip().split(";")
        u = {
            "user": datas[0],
            "key": datas[1],
        }
        users_datas.append(u)

    for u in users_datas:
        print(u)

    contQ = input("Do you want to add data? (y/n): ").lower()
    if contQ == "y":
        add(users_datas, new_users)
        finalize(db, new_users)

    else:
        for u in users_datas:
            print(u)
        print()
        db.close()
        print("No changes in the file.")
    

main()
