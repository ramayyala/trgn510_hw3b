##import used modules
import phonenumbers as pn
import re
import sys
#takes in input text
filename = sys.argv[1]
#opens and reads text file to a string
text_file = open(filename, "r")
text = text_file.read()
text_file.close()
##extract numbers from text file into a list
matches=[]
for match in pn.PhoneNumberMatcher(text, "US"):
    matches.append(match)
##format numbers to correct output
for numbers in matches:
    if pn.format_number(numbers.number, pn.PhoneNumberFormat.E164)[0:2]=='+1': ##number is national
        test=re.split(' |-',pn.format_number(matches[1].number, pn.PhoneNumberFormat.NATIONAL))
        print(test[0]+test[1]+test[2])
    else: ##number is international
        test=pn.format_number(numbers.number, pn.PhoneNumberFormat.INTERNATIONAL).split(' ')
        print(test[0]+" (" + test[1]+") "+test[2]+test[3] )
