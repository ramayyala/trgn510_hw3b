# trgn510_hw3b
# extract_phonenum.py<br />
## Usage<br />
`python3 extract_phonenum.py mytextfile.txt`<br />
## Description<br />
* Extracts phone numbers from a text file, and prints formatted phone numbers.<br />
* One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number].<br />
* [+][country code] optional output if number is international. <br />
## Dependencies<br />
## Known issues<br />

# ensg2hugo.py<br />
## Usage<br />
` python3 ensg2hugo.py input.csv -fnumber`<br />
## Description>br />
* You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.<br />
## Dependencies<br />
## Known issues<br />

# histogram.py<br />
## Usage<br />
`python3 histogram.py input.tsv -fnumber`
## Description<br />
* Creates a histogram as a png from a file using the specified column in a tab delimited file.<br />
## Dependencies<br />
## Known issues<br />


# UNIT TESTS<br />
## ensg2hugo.py<br />
  Usage: `python3 ensg2hugo.py unit/unit_ensg2hugo.csv -f1`
  Usage: `python3 ensg2hugo.py unit/unit2_ensg2hugo.csv -f0`
