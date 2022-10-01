# Напишите программу, удаляющую из текста все слова, содержащие ""abc"".

mytext = input("Enter your text separated by a space:\n")
find_txt = "abc"
newtext = [i for i in mytext.split() if find_txt not in i]
print(f'New text is: {" ".join(newtext)}')
