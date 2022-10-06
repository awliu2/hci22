import os
import sys
from random import uniform
import time
from datetime import datetime

def main():    
    with open('out.csv', "w") as f:
        for i in range(30):
            os.system('clear')
            sys.stdout.write("\r {}: Ready?".format(i + 1))
            time.sleep(uniform(1,2))
            tstart = datetime.now()
            input("\r press enter")
            tend = datetime.now()

            f.write(str(int((tend - tstart).total_seconds() * 1000)))
            if i < 29: f.write(", ") 

if __name__ == "__main__":
    main()
