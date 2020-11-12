import argparse

def get_args():
    parser = argparse.ArgumentParser(description='idk lets parse some args')
    parser.add_argument("-input",help="insert input txt file (mandatory)" , dest="input", type=str, required=True)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    print(args.input)