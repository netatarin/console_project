ar=list(input())
b=[]
print("Выберите тип шифрования")
print("1)Азбука Морзе")
print("2)Шифр Цезаря")
print("")
print("")
print("")
n=input()
if n=="2" or n=="Шифр Цезаря":
    cesar=['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
    for i in range(len(ar)):
        for j in range(len(cesar)):
            if ar[i]==cesar[j]:
                b.append(j+1)
                continue
print(*b)
