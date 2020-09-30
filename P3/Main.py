# Authors: Kenneth Grinyan
# Date: 21/05/2020
# Description: Genera un projecte anomenat P3, crea un programa que consti de les funcions
#              necessàries per resoldre els següents problemes:

#importem la llibreria date per el calcul del anys
from datetime import date

# 1) Donades dues paraules dir si rimen o no.
#     Si coincideixen les tres últimes lletres vol dir que rimen,
#     si coincideixen només les dos últimes ha de dir que rimen una mica i,
#     si no es compleix cap dels dos casos, que no rimen.
def buscaRima():
    # almacenamos las 2 palabras
    paraula1 = input("Escribe una palabra: ")
    paraula2 = input("Escribe otra palabra: ")
    # arrays para almacenar las 3 ultimas letras
    arrayParaula1 = []
    arrayParaula2 = []
    # almacenamos las 3 ultimas letras de la palabra 1
    for x in range(1, 4):
        letra = paraula1[(len(paraula1) - x)]
        arrayParaula1.append(letra)
    # almacenamos las 3 ultimas letras de la palabra 2
    for x in range(1, 4):
        letra = paraula2[(len(paraula2) - x)]
        arrayParaula2.append(letra)

    if arrayParaula1[0] == arrayParaula2[0] and arrayParaula1[1] == arrayParaula2[1] and arrayParaula1[2] == \
            arrayParaula2[2]:
        print("Riman")
    else:
        print("No Riman")


# 2) Els números de les claus de dues caixes fortes estan barrejades en un número sencer anomenat clau mestra.
#     Trobar les dues claus, la  primera clau es construeix amb els dígits senars de la clau mestra
#     i la segona amb els parells.
#     Exemple: Clau Mestra= 12345, clau1=135, clau2=24.
def trobaClaus1i2():
    mestre = (input("Introduce la llave maestra"))
    clau1 = []
    clau2 = []
    print("Desxifran les claus . . .")
    for x in range(0, len(mestre)):
        if int(mestre[x]) % 2 != 0:  # senar
            clau1.append(mestre[x])
        else:  # parell
            clau2.append(mestre[x])

    print("Clau_1:", end=" ")
    for x in clau1:
        print(x, end=" ")
    print("\n")

    print("Clau_2:", end=" ")
    for x in clau2:
        print(x, end=" ")
    print("\n")


# 3) Donada una llista de números obtenir una nova llista on el primer element és el mateix,
#     el segon element és la suma del primer amb el segon, el tercer element és la suma del
#     resultat anterior amb el següent element i així successivament.
#     Per exemple, la suma acumulada de [1,2,3] es [1, 3, 6].
def sumaElements():
    numeros = [1, 2, 3, 4, 5, 6]
    print("Llista de numeros: " + str(numeros))
    print("Nova llista en forma de sumatori succesiu del seu elements:")

    i = 0  # iterador
    sumatori = 0
    nouNumeros = []
    for x in numeros:
        sumatori += x
        nouNumeros.append(sumatori)
        i += 1

    print("Llista resultant: " + str(nouNumeros))


# 4) Demanant l'any en curs, el nom i l'any de naixement de tres persones es vol calcular quants anys compliran durant l'any en curs.
# retorna el numero de dies totals entre 2 dates, en valor absolut
def calculaDies(d1, d2):
    return abs(d2 - d1).days

# DEMANEM LES DADES PER TECLAT E INVOQUEM A CALCULA DIES
def calculaAnys():
    indexAny = 0
    indexMes = 1
    indexDia = 2

    dataActual = []
    dataActual.append(int(input("Introdueix l`any actual")))
    dataActual.append(int(input("Introdueix el mes actual")))
    dataActual.append(int(input("Introdueix el dia actual")))

    nomP1 = input("Introdueix nom de la primera persona:")
    dataP1 = []
    dataP1.append(int(input("Introdueix l`any de naixamen:")))
    dataP1.append(int(input("Introdueix el mes de naixamen:")))
    dataP1.append(int(input("Introdueix el dia de naixamen:")))

    nomP2 = input("Introdueix nom de la segona persona:")
    dataP2 = []
    dataP2.append(int(input("Introdueix l`any de naixamen:")))
    dataP2.append(int(input("Introdueix el mes de naixamen:")))
    dataP2.append(int(input("Introdueix el dia de naixamen:")))

    nomP3 = input("Introdueix nom de la tercera persona:")
    dataP3 = []
    dataP3.append(int(input("Introdueix l`any de naixamen:")))
    dataP3.append(int(input("Introdueix el mes de naixamen:")))
    dataP3.append(int(input("Introdueix el dia de naixamen:")))

    sumatoriDies = 0

    # pasem les dades introduides per teclat a variables tipus date
    tipusDataActual = date(dataActual[indexAny], dataActual[indexMes], dataActual[indexDia])
    tipusDataP1 = date(dataP1[indexAny], dataP1[indexMes], dataP1[indexDia])
    tipusDataP2 = date(dataP2[indexAny], dataP2[indexMes], dataP2[indexDia])
    tipusDataP3 = date(dataP3[indexAny], dataP3[indexMes], dataP3[indexDia])

    sumatoriDies += calculaDies(tipusDataP1, tipusDataActual)
    sumatoriDies += calculaDies(tipusDataP2, tipusDataActual)
    sumatoriDies += calculaDies(tipusDataP3, tipusDataActual)

    anysTotal = sumatoriDies / 365

    print("Entre " + nomP1 + ", " + nomP2 + ", " + nomP3 + " cumpliran un total de " + str(anysTotal) + " anys")


# 5) Donada una llista de paraules i un sencer n, trobar les paraules que tinguin més de n caràcters.
def buscaMesGrans():
    llista = ["casa", "hola", "cotxe", "ordinador", "biblioteca", "electrocardiograma"]
    print("La llista te les seguents paraules: " + str(llista))
    n = int(input('Introdueix el numero per trobar les paraules amb mes caracters que el numero'))
    contador = True
    for x in range(len(llista)):
        if len(llista[x]) > n:
            print(llista[x])
            contador = False
    if contador:
        print("No s`han trobat paraules amb mes de " + str(n) + " caràcters")
    print("\n")


def menuPrincipal():
    while 1:
        print("\n* * * * * * * * * MENU PRINCIPAL * * * * * * * * *")
        print("QUINA FUNCIO VOLS CRIDAR?")
        print("[1] = Donades dues paraules dir si rimen o no.")
        print("[2] = Desxifra les claus a partir de la clau mestre.")
        print("[3] = Obtenir una nova llista amb el sumatori del elements a cada posicio.")
        print("[4] = Calcular quants anys compliran durant l'any en curs tres persones.")
        print("[5] = Troba les paraules amb mes caracters que el numero n.")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        opcio = int(input('Introdueix el numero corresponent i prem intro\n'))

        if opcio == 0:
            print("FINS AVIAT ! ! !")
            break
        elif opcio == 1:
            buscaRima()
        elif opcio == 2:
            trobaClaus1i2()
        elif opcio == 3:
            sumaElements()
        elif opcio == 4:
            calculaAnys()
        elif opcio == 5:
            buscaMesGrans()
        else:
            print("Error, numero no valid")

# Cal lliurar un arxiu amb el nom P3_Nom_Cognom_M04.zip, .rar o 7z amb el projecte.

# M A I N
menuPrincipal()
