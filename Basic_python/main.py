#snake_case
nombre_completo = 'cody banks'
print('*********************PRUEBAS*********************')
print(nombre_completo)
print(type(nombre_completo))
nombre_completo = 10
print(type(nombre_completo))
#empaquetado
name, last_Name, age = 'doko', 'libra', 22
print(name)
print(last_Name)
print(age)
print(name, last_Name, age)
#string/int/tuple inmutables
namex= 'ama'
namey= 'ama'
print (id(namex))
print (id(namey))

#input_age = input('ingresa tu edad: ')
#input_age = int(input_age)
input_age = 11
print(input_age)
print(type(input_age))

#condicionales
MESSAJE = """este es un mensaje con salto de linea
su variable al estar con mayusculas es considerada una
constante por parte del desarrollador""" 
if input_age >= 10:
    print('estas mayor💚')
else:
    print('estas joven🤎')
    print(MESSAJE)

#and or not
#score = input('ingresa tu score: ')
#score = int(score)
score = 8

if score == 10:
    print('you re awesome💥')
elif score == 9 or score == 8:
    print('you re meh➰')
else:
    print('disapointed💤')

# expresar falso = false, 0, (), [], {}. none, false, 

# listas
languajes = ['python', 'java', 'rust', 'c#', 'ruby', 'mongo']
print(languajes)
first_idx = languajes[0]
first_idx_rev = languajes[-1]
print(first_idx)   
print(first_idx_rev)

#start : end
first_to_third = languajes[1:3]
print(first_to_third)
zero_to_fourth = languajes[:4]
print(zero_to_fourth)
first_to_third_inv = languajes[:]
print(first_to_third_inv)
jumps= languajes[::1]
print(jumps)
jumps2= languajes[::2]
print(jumps2)

# tuplas **Mas de lectura no crecen, inmutables

config = (True, 8080, 'localhohst', 20, False, 2, 4, 1, 10)
config_first = config[0]
config_second = config[1]
config_last = config[-1]
print (config_first, config_second, config_last)

first_tupla, second_tupla, *_, last_tupla = config
print (first_tupla, second_tupla, last_tupla)

# diccionarios representar estructuras llave: valor
# NO llaves duplicadas
user = {
    'id': 9,
    'nombre': 'cody',
    'email': 'info@apren.com',
    'courses': [
        {
            'id': 1,
            'name': 'python'
        },
        {
            'id' : 2,
            'name': 'numpy'
        },
        {
            'id' : 3,
            'name': 'pandas'
        },
        {
            'id' : 4,
            'name': 'js'
        },
        {
            'id' : 5,
            'name': 'RRR'
        }
    ]  
}
print (user)
user['age'] = 20 #creo nuevo
print (user)
user['email'] = 'infodoko@xxxx' #asigno nuevo
print (user)

print (#pedir valors con get y si no existe, por defecto mostrar none OR lo q colocas
    user.get ('courses', ['python', 'mongo', 'java'])
)

#ciclos foreach, while
print("""***********************
      ***************ciclos***********
      *************************""")
courses = user.get('courses', [])
for course in courses:
    #pass crea bloques vacios o 3 puntos sguidos ...
    ...
    print(course)

for course in courses:
    if course.get('name'): #none
        ...
        print('El nombre del curso es:', course['name'])

cont = 0
while cont <= 10:
    cont += 1
    print(cont)
else:
    print('el contador es igual a 11༼ つ ◕_◕ ༽つ')
  
#funciones

def suma_dos_numeros():
    ...
    print('funcion q suma 2 numeros')

suma_dos_numeros()
suma_dos_numeros()

#funciones parametros
def suma_dos_numeros_parametros(valor1, valor2):
    """esto es un docstring 1 linea q define lo q hace la funcion"""
    result = valor1 + valor2
    return result

print(suma_dos_numeros_parametros(10, 20))


# vectors numpy y pandas RECOMENDADO        




