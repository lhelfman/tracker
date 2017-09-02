import sys
import pandas as pd


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")

    # import data
    path = '/home/ljh/Projects/tracker/data/'
    new_transactions = pd.read_csv(path + 'Transactions.csv')
    print(new_transactions)
    

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()

