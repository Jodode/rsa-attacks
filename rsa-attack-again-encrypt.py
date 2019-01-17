from gmpy2 import powmod
from binascii import unhexlify, hexlify
import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument('-n', action='store', type=int, help='Module (integer number)')
    parser.add_argument('-e', action='store', type=int, help='Public Exponent (integer number)')
    parser.add_argument('-c', action='store', type=int, help='Ciphertext (integer number)')
    parser.add_argument('--pattern', action='store', type=str, default="flag", help='pattern search (default "flag")')
    parser.add_argument('--max-depth', action='store', type=int, default=200, help='Max depth while program can search flag (default 200)')

    return parser

def main(argv):

    for opt, arg in opts:
        if opt == '-h':
            print('rsa-attack-again-encrypt.py -n -e -c')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    if namespace.c is None and namespace.n is None and namespace.e is None:
        print("""usage: rsa-attack-again-encrypt.py [-h] [-n N] [-e E] [-c C]
                                   [--pattern PATTERN] [--max-depth MAX_DEPTH]

optional arguments:
  -h, --help            show this help message and exit
  -n N                  Module (integer number)
  -e E                  Public Exponent (integer number)
  -c C                  Ciphertext (integer number)
  --pattern PATTERN     pattern search (default "flag")
  --max-depth MAX_DEPTH
                        Max depth while program can search flag (default 200)""")
    else:
        e = namespace.e
        n = namespace.n
        c = namespace.c
        pattern = namespace.pattern


        for i in range(namespace.max_depth):
            try:
                ans = unhexlify(hex(powmod(c, e ** i, n))[2:]).decode("utf-8")
                if pattern in ans:
                    print(ans)
                    break
            except:
                print("", end="")