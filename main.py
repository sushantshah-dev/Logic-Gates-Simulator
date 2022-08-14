import sys, pickle, tkinter

def main(baseObject=None):
    pass

def save(baseObject, filename):
    pickle.dump(baseObject, open(filename, 'wb'))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(pickle.load(open(sys.argv[1], 'rb')))
    elif len(sys.argv) == 1:
        main()