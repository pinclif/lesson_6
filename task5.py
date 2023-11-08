en_alphabet_lo = 'abcdefghijklmnopqrstuvwxyz'
en_alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_alphabet_lo = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ru_alphabet_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

print("Choose language: english - en, russian - ru")
language = input()
print("Choose encryption: encryption - ch, decryption - def")
encrypt = input()
print("Enter the encryption key")
step = int(input())
print("Enter a phrase")
message = input()

def chru(cipher, shag, lang,phrase):
    if lang == 'ru':
        letter = 32
    if lang == 'en':
        letter = 26
    if cipher== 'def':
        shag = -step
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            if phrase[i] == phrase[i].upper():
                for j in range (letter):
                    if letter == 32:
                        if phrase[i] == ru_alphabet_up[j]:
                            print(ru_alphabet_up[(j+shag)%letter], end = '')
                            break
                    if letter == 26:
                        if phrase[i] == en_alphabet_up[j]:
                            print(en_alphabet_up[(j+shag)%letter], end = '')
                            break
            elif phrase[i] ==phrase[i].lower():
                for j in range (letter):
                    if letter == 32:
                        if phrase[i] == ru_alphabet_lo[j]:
                           print(ru_alphabet_lo[(j+shag)%letter], end='')
                           break
                    if letter == 26:
                        if phrase[i] == en_alphabet_lo[j]:
                           print(en_alphabet_lo[(j+shag)%letter], end = '')
                           break
        else:
            print(phrase[i], end='')

chru(encrypt, step, language, message)