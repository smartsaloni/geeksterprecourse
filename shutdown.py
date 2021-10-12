import os 
shutdown = input("do you wish to shutdown your computer? (YES/NO): ")
if shutdown == 'NO':
    exit()
else:
        os.system("shutdown/s/t 1")
