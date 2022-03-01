import re
#programa que revisa si una contraseña cumple los requisitos

# Debe contener 2 letras mayusculas
def check_mayus(string):
    mayus = []
    list = string
    for i in range(len(list)):
        if ord(list[i]) in range(65, 91):
            mayus.append(list[i])
       
    if len(mayus) == 2:
        return True
    else:
        print("Error la contraseña debe tener 2 letras mayusculas")

# Debe contener 3 números no repetidos
def check_number(string):
    number = []
    list1 = string
    for i in range(len(list1)):
        if ord(list1[i]) in range(48, 58):
            number.append(list1[i])
    
    if len(number) == 3:
        for i in range(len(number)):
            if number[i] == number[i+1]:
                print("Error la contraseña debe tener 3 números diferentes")
            else:
                return True
    else:
        print("La contraseña debe tener minimo 3 números")

# Debe contener un caracter especial
def check_special_character(string):
    result = re.search(r"[^a-zA-Z0-9]", string)
    if result:
        return True
    else:
        print("Error la contraseña debe tener al menos un carácter especial *_-¿¡?#$")

# Debe contener un espacio en blanco
def check_blank_space(string):
    x = re.search("\s", string)
    #print(x)
    if x == None:
        return True
    else:
        print("Error la contraseña tiene espacios en blanco")

# Debe tener una longitud entre 8 y 15 caracteres
def check_lengh(string):
    if len(string) >= 8 and len(string) <= 15:
        return True
    else:
        print("Error la contraseña debe tener minimo 8 caracteres máximo 15")

password = input("Ingresa una contraseña para verificar que cumple los requisitos: ")
check_mayus(password)
check_number(password)
check_special_character(password)
check_blank_space(password)
check_lengh(password)
