"Programa para determinar el mayor de 3 numeros enteros"

print("""-------------------------------------""")
print("""---------numero mayor----------------""")
print("""-------------------------------------""")

#input

x = int(input("Digite el primer numero"))
y = int(input("Digite el segundo numero"))
z = int(input("Digite el tercer numero"))

#processing

if x > y and x > z: 
    print("El numero mayor es: ", x)
elif y > x and y > z:
    print("El numero mayor es: ", y )
elif z > x and z > y:
    print("El numero mayor es: ", z)
else:
    print("No se puede determinar el mayor")

