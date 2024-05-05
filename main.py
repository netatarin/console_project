import inputprog
import logic
import output

def main():
    output.show_start_message()
    output.text()
    while True:
        output.show_spisok()
        k = inputprog.answer()
        if k==4:
            print(output.the_end())
            break
        if k>4 or k<1:
            output.spisok_error()
            continue
        ar = list(input("Введите строчку для шифрования:"))
        if k==1:
            logic.morz(ar)
            print("")
        if k==2:
            logic.cesar(ar)
            print("")
        if k==3:
            logic.atbash()
            print("")
if __name__ == '__main__':
    main()