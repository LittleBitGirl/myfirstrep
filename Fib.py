def main():
    print "Числа Фибоначчи"
    x1=1
    x2=1
    n=input("Введите порядковый номер вашего числа:")
    y=2
    while y<n:
        summa=x1+x2
        x1=x2
        x2=summa
        y=y+1
    print summa
main()
