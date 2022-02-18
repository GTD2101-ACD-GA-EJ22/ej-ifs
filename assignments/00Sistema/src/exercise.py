import os

def main():
    os.system("clear")

    print("SOLUCION DE SISTEMA DE ECS 2X2")
    print("==============================")

    print("PRIMER ECUACIÓN....")
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))

    print("SEGUNDA ECUACIÓN....")
    d=float(input("d:"))
    e=float(input("e:"))
    f=float(input("f:"))

    determinante = a*e - b*d 

    if determinante == 0.0:
        print("EL SISTEMA DE ECUACIONES NO TIENE SOLUCIÓN ÚNICA...")
    else:
        x=(c*e - b*f)/(a*e - b*d)
        y=(a*f - c*d)/(a*e - b*d)

        print(f"x={x:.2f}")
        print(f"y={y:.2f}")

if __name__=='__main__':
    main()
