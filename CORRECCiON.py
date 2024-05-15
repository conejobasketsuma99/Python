def Ej4():
    ladoX = float(input("Ingrese el largo del cuadrado: "))
    area = ladoX * ladoX
    print("La superficie es igual a :", area)

Ej4()

def Ej5():
    horas = int(input("Hora: "))
    mins = int(input("Minutos: "))
    segs = int(input("Segundos: "))
    totalHoras = horas * 3600
    totalMinutos = mins * 60
    totalSegundos = totalHoras + totalMinutos + segs
    print("Traducido a segundos serian:", totalSegundos)

Ej5()

def Ej6():
    base = int(input("¿Cuánto mide la base? "))
    altura = int(input("¿Cuánto mide la altura? "))
    areaTriangulo = base * altura / 2
    print("El triangulo posee una superficie de:", areaTriangulo)

Ej6()

def Ej7():
    numero1 = int(input("Ingresa tu primer cifra: "))
    numero2 = int(input("Ingresa tu segunda cifra: "))
    numero3 = int(input("Ingresa tu tercer cifra: "))
    numero4 = int(input("Ingresa tu cuarta cifra: "))
    numero5 = int(input("Ingresa tu quinta cifra: "))
    numero6 = int(input("Ingresa tu cifra final: "))
    sumaTotal = numero1 + numero2 + numero3 + numero4 + numero5 + numero6
    elpromedio = sumaTotal / 6
    print("Tu promedio es:", elpromedio)

Ej7()

def Ej8():
    num1 = int(input("Dime un número: "))
    num2 = int(input("Dime un número máss: "))
    numporcentaje= num1 / 100
    porcentaje = num2 / numporcentaje
    print("El porcentaje es:", porcentaje)

Ej8()

def Ej9():
    lafecha = int(input("Tu DDMMAAAA: "))
    dia = lafecha // 1000000
    mes = (lafecha // 10000) % 100
    año = lafecha % 10000
    print("Fue el día:", dia, "del mes:", mes, "del año:",año)
    

Ej9()

def Ej10():
    examen = int(input("La nota de tu examen: "))
    tps = int(input("La nota de tus Trabajos: "))
    recuperatorio = int(input("La nota de tu recuperatorio: "))
    notaexamen = examen * 0.3
    notatps = tps * 0.2
    notarecuperatorio = recuperatorio * 0.5
    promedioFinal = notaexamen + notatps + notarecuperatorio
    print("Tu valoracion es de:", promedioFinal)

Ej10()

def Ej11():
    listaAutos = []
    entradaUsuario = " "
    while entradaUsuario != "CANCELAR":
        entradaUsuario = input("Ingresar el precio del auto o CANCELAR: ")
        if entradaUsuario != "CANCELAR":
            precioAuto = float(entradaUsuario)
            listaAutos.append(precioAuto)
    totalIngresos = sum(listaAutos)
    comisionFinal = totalIngresos * 0.05
    print("El salario del vendedor es:", comisionFinal)
Ej11()

def Ejext():
# Pedimos la fecha de nacimiento de la persona 1
print("Persona 1:")
dia_persona1 = int(input("Ingrese el día de nacimiento: "))
mes_persona1 = int(input("Ingrese el mes de nacimiento: "))
anio_persona1 = int(input("Ingrese el año de nacimiento: "))

# Ahora pedimos el nacimiento de la persona 2
print("\nPersona 2:")
dia_persona2 = int(input("Ingrese el día de nacimiento: "))
mes_persona2 = int(input("Ingrese el mes de nacimiento: "))
anio_persona2 = int(input("Ingrese el año de nacimiento: "))

# Vamos a comparar las fechas de nacimiento y determinar cuál es mayor
if anio_persona1 > anio_persona2:
    primera_persona = "Persona 1"
elif anio_persona2 > anio_persona1:
    primera_persona = "Persona 2"
else:  # En caso de que el año de nacimiento sea igual, comparamos el mes
    if mes_persona1 > mes_persona2:
        primera_persona = "Persona 1"
    elif mes_persona2 > mes_persona1:
        primera_persona = "Persona 2"
    else:  # En caso de que el mes de nacimiento también sea igual, comparamos el día
        if dia_persona1 > dia_persona2:
            primera_persona = "Persona 1"
        elif dia_persona2 > dia_persona1:
            primera_persona = "Persona 2"
        else:  # Pero si el día como el mes y el año son iguales, ambas personas tienen la misma edad
            primera_persona = "Ambas personas tienen la misma edad"

# Resultado final poshoooooo
print("La primera persona en la fila es:", primera_persona)
Ejext()