#suma de dos importes ingresados por el usuario
'''
n1=int(input('Escriba el primer numero: '))
n2=int(input('Escriba el segundo numero: '))

resultado=n1+n2

print('El resultado de la suma es: ',resultado)

dato1=float(input('Escriba el primer numero: '))
dato2=float(input('Escriba el segundo numero: '))

resultado2=dato1+dato2

print('El resultado de la suma es: ',resultado2)
'''

print('*** Este programa calcula y muestra el promedio de un alumno ***')

nombre=input('Ingrese el nombre del alumnos: ')
matematica=float(input('Ingrese la nota del curso de matematica: '))
fisica=float(input('Ingrese la nota del curso de fisica: '))
quimica=float(input('Ingrese la nota del curso de quimica: '))

promedio=(matematica+fisica+quimica)/3

if (promedio<11):
    print('El alumno ', nombre, 'desaprobo el curso con la nota : ',round(promedio,2))
else:
    print('El alumno ', nombre, 'aprobo el curso con la nota : ',round(promedio,2))