import random
import time

num_palabras = int(input("Numero de Palabras a Generar: "))

# Using open() function
file_path = "palabras.txt"

start_time = time.time()

# Open the file in write mode
with open(file_path, 'w') as file:

    for i in range(0, num_palabras):
        largo = random.randrange(1, 20)
        
        palabra = [0] * largo
        
        for j in range(0, largo):
            palabra[j] = random.randrange(1,4)
            if (palabra[j] == 1):
                palabra[j] = 'a'
            if (palabra[j] == 2):
                palabra[j] = 'b'
            if (palabra[j] == 3):
                palabra[j] = 'c'
                
        string = ''.join(palabra)
        
        if(i < num_palabras-1) :
            file.writelines(string + '\n')
        else:
            file.writelines(string)
        
end_time = time.time()
        
print("File '{file_path}' created successfully.")