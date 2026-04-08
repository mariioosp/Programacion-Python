num1=float(input("Escribe un número: "))
if not num1<=0:
     print("El número es distinto y mayor que 0")
     if num1%2==0:
         print("El número es par")
     else:
         print("El número es impar")
else:
     print("Error")

num2=int(input("Escribe un número: "))
if not num2>0:
    print("Error")
elif num2==0:
    print("Error")
elif num2<10 and num2>0:
    print("El número tiene un dígito")
elif num2<100 and num2>=10:
    print("El número tiene dos dígitos")
    if num2%2==0:
        print("El número es par")
    else:
        print("El número es impar")
else:
    print("El número tiene 3 dígitos o más")
    if num2%2==0:
        print("El número es par y además su resto al dividirse entre 2 es 0")
    else:
        print("El número es impar y además su resto al dividirse entre 2 es 1")
    

     
