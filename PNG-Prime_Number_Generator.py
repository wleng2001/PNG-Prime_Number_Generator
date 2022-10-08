#prime number generator
from time import sleep
from os import system
from sys import platform

examine_number=1
if_prime_number=True
file_name="prime_numbers.txt"

def read_last_number(file_name):
    count = -1
    try:
        for count, wiersz in enumerate(open(file_name, 'r')):
            count += 1
        file=open(file_name, 'r')
        table=file.read()
        number=(table.split('\n'))[-2]
        return int(number)
    except:
        return 1

def write_file(file_name, data):
    file=open(file_name, 'a')
    file.write(str(data)+'\n')
    file.close()



print("Read last prime number")
examine_number=read_last_number(file_name)+1
print(f"Last prime number is: {examine_number}")

while True:
    for j in range(2,int(examine_number/2+1)):
        if examine_number%j==0:
            if_prime_number=False
            
            break
        
    if if_prime_number==True:
        write_file(file_name, examine_number)
    examine_number+=1
    if_prime_number=True


