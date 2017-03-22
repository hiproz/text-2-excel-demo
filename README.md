# text_2_excel_demo
a demo that convert text to excel

This example includes the following:
1. how to read a line from a text file
2. how to preprocess the line content
3. how to find a keyword in the line
4. how to deel with the out of order of the line in a block
5. how to deel with the similar repeated content line
6. how to find the end of input text file
7. how to write a line to the excel

# how to read a line from a text file
```
# open the source file
file = open("./input.txt")

line = file.readline()
```
# how to preprocess the line content
```
line=line.strip('\n')
```
# how to find a keyword in the line
```
if " Chair of the Board " in line:
  #todo something
```
# how to deel with the out of order of the line in a block
1. use keywords,such as  @, Tel, Email ect.
2. the left line of block use defaut sort, and just get needed sum of line ,ignor the more lines

# how to deel with the similar repeated content line
add it after to the similar line,make sure all the similar content in one excel cell
```
if " Executive Director " in line :
  # why the belowe use +=, bcz of the repeated type info such as more than 1 chairman
  director += line   
  print "director:%s" % director
```
#  how to find the end of input text file
```
# check the end of file
if not line:
    # todo something
```

# how to write a line to the excel
```
import csv

with open('info.csv', 'wb') as csvfile:
  spamwriter = csv.writer(csvfile,dialect='excel')
  spamwriter.writerow(['Territory', 'Federation\'s Name', 'Address', 'City/State/Zip', 'Tel', 'Website', 'Chairman', 'Director', 'email'])
  spamwriter.writerow([territory, federation, addr, city, tel, website, chairman, director, email])
```
