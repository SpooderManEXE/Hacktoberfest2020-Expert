#python program to shutdown computer

import os;
check = input("want to shut down your computer? (y/n): " );
if check == 'n':
    exit ();
else:
    os.system("shutdown/s /t 1");
