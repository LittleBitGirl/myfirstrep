def main():
    print "Проверка простых чисел!"
    a=input("введите ваше число:")
    i=0#Простое число
    for p in range(2,a-1):
        if a%p==0:
            i=i+1
            print "Число не простое"
            break;
    if i==0:
        print "Число простое!"
main()
