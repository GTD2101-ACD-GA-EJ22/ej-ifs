import os

def main():
    os.system("clear")

    print("CLASIFICADOR DE TRIANGULOS")
    print("==========================")

    angulo = float(input("Ángulo en grados:"))

    if angulo < 90:
        print("El ángulo es Agudo...")
    elif angulo == 90:
        print("El ángulo es Recto ...")
    elif (angulo > 90) and (angulo < 180):
        print("El ángulo es Obtuso ...")
    elif angulo==180:
        print("El ángulo es Llano ...")
    else:
        print("El ángulo es Cóncavo...")
    

if __name__=='__main__':
    main()
