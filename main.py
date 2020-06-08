import argparse
# from core import scanxss,dirb
def banner():
    print('''
 ____               ____ ____  ____  
/ ___| _   _ _ __  / ___/ ___||  _ \ 
\___ \| | | | '_ \| |   \___ \| |_) |
 ___) | |_| | | | | |___ ___) |  _ < 
|____/ \__,_|_| |_|\____|____/|_| \_\ 

''')
def main():
    parser = argparse.ArgumentParser(prog="scan")
    parser.add_argument("-u","--url",required=True)
    args = parser.parse_args()
    print(vars(args))
if __name__ == "__main__":
    main()