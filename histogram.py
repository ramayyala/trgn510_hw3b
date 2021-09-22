import argparse
import seaborn as sns
import sys
import pandas as pd
import matplotlib.pyplot as plt
##usage: python3 histogram.py input.tsv -fnumber
##Parse arguments given and check if -f arg is included
## if -f arg included, set index to whatever value given in -f input
if len(sys.argv) == 3:
    parser = argparse.ArgumentParser(description='Column Choice')
    # Positional mandatory arguments
    parser.add_argument('input_file',help='input tsv')
    # Optional arguments
    parser.add_argument('-f', dest='column', type=int, help='Column Choice')
    args = parser.parse_args()
    index=args.column
#if -f arg not included, set index to 2 by default
else:
    index=2
#CHECKS:
#check to see if index is inbewteen acceptable range of column indexes: 0-9.
if index not in range(10):
    print ("ERROR: Column Index Given is out of range, please choose value bewteen 0-9")
    sys.exit()
#load in data given in first input
data=sys.argv[1]
dataframe = pd.read_csv(data,sep='\t')
#Plot histogram and save to histogram.png in directory running in
sns.histplot(data=dataframe, x=dataframe.iloc[:, index])
plt.savefig('histogram.png')
