#prime number generator
from time import sleep
from os import system
from sys import platform
from datetime import datetime
from github import Github

examine_number=1
if_prime_number=True
file_name="prime_numbers.txt"
last_update="2022-11-06"
repo_name="wleng2001/PNG-Prime_Number_Generator"
#update check

def update_check(last_update, repo_name):
    last_date=datetime.fromisoformat(last_update)
    g=Github()
    for i in g.search_repositories("wleng2001/PNG-Prime_Number_Generator"):
        repo=i
    date=repo.pushed_at
    if date.date()==last_date.date():
        return False
    else:
        return True

#prime number search
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


print("Check version...")
if update_check(last_update, repo_name)==True:
    print("New version is available!")
else:
    print("App is current")

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


