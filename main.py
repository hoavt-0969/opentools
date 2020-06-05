import argparse

def main():
    parse = argparse.ArgumentParser(prog="scan")
    parse.add_argument("-u","--url",required=True,help="Target url")
    parse.add_argument("-t","--threads",required=True,help="Number threads")
    dirb = parse.add_argument_group("dirb")
    xss = parse.add_argument_group("xss")
    dns = parse.add_argument_group("dns")
    dirb.add_argument("-e","--extensions",required=True)
    # xss.add_argument("")
    # dns = parse.add_argument("")
    parse.print_help()
if __name__ == "__main__":
    main()