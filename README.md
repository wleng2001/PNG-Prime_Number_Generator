# PNG-Prime_Number_Generator
 It's simply program written in python, which generate prime numbers and save them to file. It starts in last position!
## Last found number
I want to create ranking the biggest prime number found by the program. You can send your score to the e-mail: *ki.serwer@gmail.com* with your nick and file, which certiy your score.

The ranking:
####
```
nr nick       score
1. Wleng2001  1026811
2. Wleng2001  2
3.
4.
5.
6.
7.
8.
9.
10.
```

## Instalation
### Linux device
You can clone it in linux devices: 

#### `git clone https://github.com/wleng2001/PNG-Prime_Number_Generator.git ./PNG`

or download as a zip file on the github webpage.

Next you must check, that you have python downloaded. You can check it by writting the information in terminal: 

#### `python3 --version` to check if you have python

You should get information similary to that:

#### `Python 3.9.7`

If you don't have downloaded python you can do it <a href="https://www.python.org/downloads/">here</a> or you can write the text in terminal:

#### `sudo apt install python3`

In next step you must install pip by:

#### `sudo apt install python3-pip`

When you install pip you must install gitpython library by typing the command in the terminal:

#### 'sudo pip3 install pygithub'

### Windows device

On the windows devices you can download zip file from github and unpack it.
Next you must check, that you have python download. You can check it by writting the information in cmd (you can open it by writting *cmd* confirm it after clicking **win**): 

#### `python --version` to check if you have python

You should get information similary to that:

#### `Python 3.9.7`

If you don't have downloaded python you can do it <a href="https://www.python.org/downloads/">here</a>.

if you don't have pip you can install it by writing the command in cmd:

#### `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

after download you must typing the information in cmd:

#### `python get-pip.py`

Next you must write the command in the cmd to download pygithub library:

#### `pip install pygithub`

## Usage
In linux devices you can run program by writing the command in terminal:
#### `sudo python3 [file_path]/PNG/PNG-Prime_Number_Generator.py` where [file_path] is file path to the PNG folder
In windows devices you can run program by clicking **PNG-Prime_Number_Generator.py** in file explorator.
After run program first time you should see the information:
####
```
Read last prime number
Last prime number is: 2
```
Program starts looking for prime numbers. Found numbers are saves to file **prime_numbers.txt**. From the file it loads last found prime number. 
If you want to stop program in linux or windows you must click **ctr** + **c** or close the terminal. 
