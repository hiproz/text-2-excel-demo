#!/usr/bin/env python
# -*- coding:utf-8 -*-
  
import csv

with open('info.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile,dialect='excel')
    # init the title line 
    spamwriter.writerow(['Territory', 'Federation\'s Name', 'Address', 'City/State/Zip', 'Tel', 'Website', 'Chairman', 'Director', 'email'])

    # open the source file
    file = open("./input.txt")

    # init var
    lineindex = 0 #line index of block
    # excel cell var
    territory = ''
    federation = ''
    addr = ''
    city = ''
    tel = ''
    website = ''
    chairman = ''
    director = ''
    email = ''
        
    # content block process
    while 1:
        # start
        line = file.readline() 

        # check the end of file
        if not line:
            # write the cell to excel
            spamwriter.writerow([territory, federation, addr, city, tel, website, chairman, director, email])
            break

        # for print issue
        line=line.strip('\n')

        # find the end of a block
        if line.strip()=='':
            print 'line is null\n'
            # write the cell to excel
            spamwriter.writerow([territory, federation, addr, city, tel, website, chairman, director, email])

            lineindex = 0 
            territory = ''
            federation = ''
            addr = ''
            city = ''
            tel = ''
            website = ''
            chairman = ''
            director = ''
            email = ''
            continue

        # case 1: the feed line
        if line.endswith(r' &  '):
            line += file.readline()
            line=line.strip('\n')

        # case 2: tel
        if "Tel:" in line:
            tel = line
            print "tel:%s" % tel
        elif "Website:" in line:
            website = line
            print "website:%s" % website
        elif "@" in line:
            email = line   
            print "email:%s" % email
        # todo: need confirm the all case 
        elif " Chair of the Board " in line or " Chair of the Board " in line or " Chair " in line or " Board Chair " in line or " Board of Directors " in line or " Chairman of the Board " in line :
            # why the belowe use +=, bcz of the repeated type info such as more than 1 chairman
            chairman += line  
            print "chairman:%s" % chairman
        # todo: need confirm the all case     
        elif " Executive Director " in line or "CEO" in line or " President " in line or " Chief Executive Officer " in line or " Executive Vice President " in line or " Co-President " in line:
            # why the belowe use +=, bcz of the repeated type info such as more than 1 chairman
            director += line   
            print "director:%s" % director
        elif lineindex == 0:
            territory = line
            print "territory:%s" % territory
            lineindex = lineindex + 1
        elif lineindex == 1:
            federation = line
            print "federation:%s" % federation
            lineindex = lineindex + 1
        elif lineindex == 2:
            addr = line
            print "addr:%s" % addr
            lineindex = lineindex + 1
        elif lineindex == 3:
            city = line
            print "city:%s" % city
            lineindex = lineindex + 1

        
