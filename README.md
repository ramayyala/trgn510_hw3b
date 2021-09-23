# About
* Documentation for three scripts:<br />
    * [extract_phonenum.py](https://github.com/ramayyala/trgn_assignment3b#extract_phonenumpy)<br />
    * [ensg2hugo.py](https://github.com/ramayyala/trgn_assignment3b#ensg2hugopy)<br />
    * [histogram.py](https://github.com/ramayyala/trgn_assignment3b#histogrampy)
# extract_phonenum.py<br />
## Usage<br />
`python3 extract_phonenum.py text.txt`<br />
* **Unit Test**<br />
  * `python3 extract_phonenum.py unit/unit_extract_phonenum.txt`<br />
  * **Output**: `+44 (20) 71838750`<br />
                `(480)4480157`<br />
## Description<br />
* Extracts phone numbers from a text file, and prints formatted phone numbers.<br />
* Outputs one-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number].<br />
* [+][country code] optional output if number is international. <br />
* Works on both international and US numbers
## Dependencies<br />
* **phonenumbers**:<br />
  * Need to install the python library **phonenumbers**:<br />
    * `pip install --user phonenumbers`
    * Used to extract the phone numbers from the text file easily
## Known issues<br />
* Built with the intent to output US numbers as follows: **([AreaCode]) [local phone number]**
* Built with the intent to output International numbers as follows: **[+][country code] ([AreaCode]) [local phone number]
* Treats all numbers without the country code [+1] as International, but should work with most phone phone numbers
* Its important to install the phonenumbers library, otherwise the whole script will fail. Make sure to install it using the user parameter on pip, if you lack sudo priveleges.
# ensg2hugo.py<br />
## Usage<br />
` python3 ensg2hugo.py input.csv -f[0-9]`<br />
* **`-f`:** parameter is an optional parameter that takes in values from 0 to 9, and will pick the column of the inputted csv based on that parameter. For example, if `-f2` is given, then the script will pick the 2nd column. By default, if no -f parameter is given, then the first column or column[0] will be used.<br />
* **Unit Test**<br />
  * `python3 ensg2hugo.py unit/unit_ensg2hugo.csv -f1`<br />
  * Output: Will output a **unit_ensg2hugo.csv.hugo.csv** into the directory of the input file, which in this case will be the unit folder.<br />
  * `python3 ensg2hugo.py unit/unit2_ensg2hugo.csv -f0`<br />
  * **Output**: Will output a **unit2_ensg2hugo.csv.hugo.csv** into the directory of the input file, which in this case will be the unit folder.<br />
## Description<br />
* Takes in a csv, and replaces the ENSEMBL gene names of the genes with their respective HUGO name.<br />
* Creates a dictionary using regex whereby, we can lookup the ENSEMBL name and pair it with the HUGO name. This is used to replace the input file's ENSEMBL gene names with HUGO names.<br />
* The script will match ENSEMBL gene names up the `.`. For example, the script will match uo to in ENSG00000248546 in ENSG00000248546.3, as the number after the `.` is just the build. So, “ENSG00000248546.3”, “ENSG00000248546.31”, and ENSG00000248546 will all yield ANP32C in this script.<br />
* You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the ENSEMBL name and replace it with the HUGO name.<br />
## Dependencies<br />
* You will need to download the **Homo_sapiens.GRCh37.75.gtf** yourself as it is too big to keep on the github.<br />
  * `wget http://ftp.ENSEMBL.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz | gunzip`<br />
  * Make sure this file is located in the root directory of the of this repository, otherwise the script will not know were to find it. <br />
* **pandas<br />**
  * This script requires the use of the pandas library in order to output the new dataframe with HUGO names into a csv.<br />
  * Install pandas if you do not have it already via:<br />
  * `pip install --user pandas`<br />
## Known issues<br />
* If a column index given out of the 0 to 9 range is given, then the script will display an error message and automatically quit, which is intentional, as we only account for up to 10 columns
* The script will fail if the column inputted or the first column of the inputted data is not ENSEMBL gene name.
* This script is only built for using **csv** files, not **tsv** files.
* This script does take a while to run, as each time its run, it recreates the dictionary which takes a while. For the future, it may be best to figure out a way to store the dictionary locally in the folder when first one, to allow quicker runtime.
* Input file must be placed first when calling the script, otherwise the script will treat the `-f` parameter as the input data.
# histogram.py<br />
## Usage<br />
`python3 histogram.py input.tsv -f[0-9]`<br />
**`-f`:** parameter is an optional parameter that takes in values from 0 to 9, and will pick the column of the inputted csv that will be plotted based on that parameter. For example, if `-f2` is given, then the script will pick the 2nd column. By default, if no -f parameter is given, then the first column or column[0] will be used.<br />
* **Unit Test**<br />
  * `python3 histogram.py unit/unit_histogram.tsv -f3`<br />
  * **Output**: This will output a **`histogram.png`** file in the directory from which the script was run<br />

## Description<br />
* Creates a histogram as a png from a file using the specified column in a tab delimited file.<br />
## Dependencies<br />
* **seaborn**:<br />
  * Need to install the python library **seaborn**:<br />
    * `pip install --user seaborn`
    * Used to create the histogram
* **pandas**:<br />
  * Need to install the python library **pandas**:<br />
    * `pip install --user pandas`
    * Used to read and select a column given by the `-f` parameter
* **matplotlib**:<br />
  * Need to install the python library **matplotlib**:<br />
    * `pip install --user matplotlib`
    * Used to save the histogram to a png
## Known issues<br />
* This script is built to only handle **`.tsv`** files, and nothing else.
* Input file must be placed first when calling the script, otherwise the script will treat the `-f` parameter as the input data.
* If a column index given out of the 0 to 9 range is given, then the script will display an error message and automatically quit, which is intentional, as we only account for up to 10 columns
