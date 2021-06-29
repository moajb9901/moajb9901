import os
import sys
################
from time import sleep
os.system("clear")
###################
print ('''\033[1;33m
                   
                   
                              ___  ___   _____       
    /   |/   | /  _  \     /   |     | | |  _  \ 
   / /|   /| | | | | |    / /| |     | | | |_| | 
  / / |__/ | | | | | |   / / | |  _  | | |  _  { 
 / /       | | | |_| |  / /  | | | |_| | | |_| | 
/_/        |_| \_____/ /_/   |_| \_____/ |_____/ 

              Please.... % Wait.... %
                   BY MOAJB
                   black hat
    \033[1;33m                                             ''')
sleep(4)
##############
##############
##############
print ("\033[1;35mWELCOME TO moajb black hat")
print ("wait...%")
sleep(3)
##########
print ('''\033[1;31m


    +---------------------------------+
    | [+] www.lolko9610@gmail.com [+] |
    | [+]      moajb990          [+]  |
    | [+]      black hat         [+]  |
    | [+]      palestine         [+]  |
    +---------------------------------+
youtube:https://youtube.com/channel/UC6nD9UyRwgMMciIQTkP-ZOg
\033[1;31m                          ''')
sleep(2)
print ('''\033[1;35m
       1 > > > md5
       2 > > > sha1
       3 > > > sha224
       4 > > > sha256
       5 > > > sha384
       6 > > > sha512
       100 > > > exit
    \033[1;35m ''')
while True:
    select = input ("select : ")
    if select == '1':
            from hashlib import md5
            sos = input ("ENTER YOUR HASH... :")
            pop = md5(sos.encode()).hexdigest()
            print(pop)
            exit
###############################################
    elif select == '2' :
          from hashlib import sha1
          lol = input ("ENTER YOUR HASH... :")
          gog = sha1(lol.encode()).hexdigest()
          print(gog)
###############################################          
    elif select == '3' :
          from hashlib import sha224
          nn = input ("ENTER YOUR HASH... :")
          FOH = sha224(nn.encode()).hexdigest()
          print(FOH)
###############################################          
    elif select == '4' :
          from hashlib import sha256   
          ee = input ("ENTER YOUR HASH... :")
          CC = sha256(ee.encode()).hexdigest()
          print(CC)
###############################################          
    elif select == '5' :
          from hashlib import sha384
          df = input ("ENTER YOUR HASH... :")
          moa = sha384(df.encode()).hexdigest()
          print(moa)
###############################################          
    elif select == '6' :
          from hashlib import sha512
          dode = input ("ENTER YOUR HASH... :")
          loket = sha512(dode.encode()).hexdigest()
          print(loket)
###############################################          
    elif select == '100' :
          sleep(3)
          os.system("clear")
          print ("close :(")
          print (" ^_^  b.y    m.o.a.j.b  ^_^")
          sys.exit()
###############################################          
else :
    print("Error In Input !! \n\nPlease Try Again >>> .")
############################################### 
#
#