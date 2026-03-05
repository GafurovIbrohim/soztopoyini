# So'z topish oyini

import random as r
from uzwords import words
print("Bu o'yin quyidagicha : Kompyuter tasodifiy bir soz oylaydi , siz bu so'zni harflarini kiritish orqali topshingiz kerak . ")

def getword():
    """Tasodifiy so'z tanlaydigan funksiya """
    word=r.choice(words)
    while "-" in word or " " in word:
        word=r.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter+=letter
        else:
            display_letter+='-'
    return display_letter


def play():
    word=getword().upper()
    word_letters=set(word)
    user_letters=""
    print(f"Kompyuter {len(word)} uzunlikdagi so'z o'yladi")

    while len(word_letters) > 0 :
        print(display(user_letters,word))
        if len(user_letters) > 0:
            print(f"Shu vaqtgacha kiritgan harflaringiz {user_letters}")
        letter=input("Harf kiriting : ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz !")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print("Bu harf sozda bor !")
        else:
            print("Bu harf so'zda yo'q")
        user_letters+=letter
    print(f"Tabriklayman siz {word} so'zini {len(user_letters) } urinishda topdingiz .")
play()