import sys
import re
import csv
import argparse
import pandas as pd
##usage: python3 ensg2hugo.py input.csv -fnumber
if len(sys.argv) == 3:
    parser = argparse.ArgumentParser(description='Column Choice')
    # Positional mandatory arguments
    parser.add_argument('input_file',help='input tsv')
    # Optional arguments
    parser.add_argument('-f', dest='column', type=int, help='Column Choice')
    args = parser.parse_args()
    index=args.column
#if -f arg not included, set index to 0 by default
else:
    index=0
data=sys.argv[1]
#CHECKS:
#check to see if index is inbewteen acceptable range of column indexes: 0-9.
if index not in range(10):
    print ("ERROR: Column Index Given is out of range, please choose value bewteen 0-9")
    sys.exit()

## First build dictionary
ens2gene={}
with open ("Homo_sapiens.GRCh37.75.gtf", 'r') as file:
    for line in file:
        matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
        if matches:
            ens2gene[matches[0][0]]=matches[0][1]

##Replacing ENSEMBLEID with HUGOID
list=[]
with open(data,'r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    #Grab header for modified output file
    reader = csv.DictReader(csv_file)
    header = reader.fieldnames
    for row in csv_reader:
        ENSID=row[index].split('.')[0]
        row[index]=ENSID
        if row[index] in ens2gene:
            row[index]=ens2gene[row[index]]
            list.append(row)
##convert list of HUGOID rows to a dataframe to be exported into csv named original_filename.csv
df = pd.DataFrame(list,columns=header)
df.to_csv(str(sys.argv[1]+".hugo.csv"),index=False)
