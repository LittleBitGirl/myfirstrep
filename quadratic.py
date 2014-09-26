def main():
    print "Нахождение корней квадратного уравнения"
    a=input ("Введите старший коэффициент ур-я:")
    b=input ("Введите коэффицент первой степени:")
    c=input ("Введите коэффициент нулевой степени:")
    D=b**2-(4*a*c)
    
    if D>0:
        import math
        x1=(-b+math.sqrt(D))/2*a
        x2=(-b-math.sqrt(D))/2*a
        import math
        print(x1,x2)
    if D<0:
        print ("Корней нет")
main()
    
def main():
    print "Вычисление теоремы Пифагора"
    a=input ("Введите длину катета:")
    b=input ("Введите длину 2-го катета:")
    import math
    c= math.sqrt((a**2)+(b**2))
    print c
main()
