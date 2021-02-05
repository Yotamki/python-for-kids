# ייבוא ספריות חיצוניות
import pickle
import sys

# הגדרת קבועים
FILE_NAME = "pokemon-db.pkl"

# הגדרת משתנים
kids = {'Yarden': 'Charizard', 'Liya': 'Pikachu'}


def print_dict(dictionary):
    print(dictionary)


# אכלס את המילון מהקובץ אם קיים
try:
    output_file = open(FILE_NAME, "rb")
    kids = pickle.load(output_file)
    output_file.close()
except IOError:
    pass

# קבלת קלט מהמשתמש
while True:
    print("הכנס את הפקודה בבקשה:")
    line = sys.stdin.readline().rstrip()
    if not line:
        continue

    input = line.split(' ')

    # הדפס את תוכן המילון
    if input[0][0] == 'l':
        print_dict(kids)

    # הוסף רשומה חדשה למילון
    elif input[0] == 'a':
        kids[input[1]] = input[2]
        print_dict(kids)

    # מחיקת רשומה מהמילון
    elif input[0] == 'd':
        kids.pop(input[1], None)
        print_dict(kids)

    # הדפס את הפוקימון ששייך לרשומה
    elif input[0] == 'g':
        pokemon = kids.get(input[1], None)
        print(pokemon)

    # שמור את תוכן המילון לקובץ
    elif input[0] == 's':
        try:
            output_file = open(FILE_NAME, "wb")
            pickle.dump(kids, output_file)
            output_file.close()
        except IOError:
            pass

    elif input[0] == 'q':
        break