import argparse
from word2belt import Word2Belt

prog = "word2belt"
desc = "Script to vectorize a word"

def main():
    parser = argparse.ArgumentParser(prog=prog, description=desc)
    parser.add_argument('word',
        help='Word to be vectorized')
    parser.add_argument('--url', required=True,
        help='URL')
    parser.add_argument('--username', required=True,
        help='Username for Basic Auth')
    parser.add_argument('--password', required=True,
        help='Password for Basic Auth')
    parser.add_argument('--filename', required=True,
        help='Filename of a Word2Vec model')

    args = parser.parse_args()

    w2b = Word2Belt(args.url, args.username, args.password, args.filename)
    v = w2b.get(args.word)
    print(" ".join(map(str, v)))
