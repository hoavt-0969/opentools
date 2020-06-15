from core import dirb

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(prog="scan")
    subparsers = parser.add_subparsers(dest='command')

    dirb_parser = subparsers.add_parser("dirb")
    xss_parser = subparsers.add_parser("xss")
    sub_parser = subparsers.add_parser("sub")

    dirb_parser.add_argument('-u','--url',required=True,type=str,default=None)
    dirb_parser.add_argument('-w','--wordlist',type=str,required=True,default="/home/sun/opentools/subdomains.txt")
    dirb_parser.add_argument("-e","--extensions",type=str,required=True,default=".php,.html,.txt")
    dirb_parser.add_argument("-t", "--threads",default=10,type=int,help="Set number threads", required=False)
    dirb_parser.add_argument('--cookies', required=False,type=str)

    xss_parser.add_argument('-u','--url',required=True,type=str)
    xss_parser.add_argument('--cookies', required=False,type=str)

    sub_parser.add_argument('-d', '--domain', required=True, type=str)
    sub_parser.add_argument('-t', '--threads', required=False, type=int, default=10)
    return parser.parse_args()
def banner():
    print('''
 ____               ____ ____  ____  
/ ___| _   _ _ __  / ___/ ___||  _ \ 
\___ \| | | | '_ \| |   \___ \| |_) |
 ___) | |_| | | | | |___ ___) |  _ < 
|____/ \__,_|_| |_|\____|____/|_| \_\ 

''')

def main():
    banner()
    args = parse_args()
    args = parse_args()
    print(vars(args))
    if args.command == "dirb":
        if args.url[-1] == "/":
            url = args.url[:-1]
        else:
            url = args.url
    # print(url[-1])
    # print(url)
        threads = args.threads
        cookies = args.cookies
        wordlist = args.wordlist
        extensions = args.extensions.split(",")
        scanner = dirb.Dirb(url=url, extensions=extensions, wordlist=wordlist, threads=threads,cookies=cookies)
        scanner.run()
    # print(vars(args))
if __name__ == "__main__":
    main()