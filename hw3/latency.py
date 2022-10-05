import os
import sys
from random import uniform
import time
from datetime import datetime

def main():
    os.system('clear')
    with open('out.csv', "w") as f:
        for i in range(30):
            sys.stdout.flush()
            sys.stdout.write("\r Ready?")
            time.sleep(uniform(1,2))    
            tstart = datetime.now()
            reaction = input("\r press enter")
            tend = datetime.now()
            os.system('clear')
            
            f.write(str(int((tend - tstart).total_seconds() * 1000)))
            if i < 29:
                f.write(", ") 


if __name__ == "__main__":
    main()
