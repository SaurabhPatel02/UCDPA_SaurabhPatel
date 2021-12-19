# https://regex101.com/

import re
#findall
regexresult=re.findall(r"Test1 present","Test1 present...test1...TEst1..Test2 present")
print (regexresult)

#split
regexresult=re.split(r"@","Test1 present@test1@TEst1@Test2 present")
print (regexresult)

#substitute
regexresult=re.sub(r"@","#","Test1 present@test1@TEst1@Test2 present")
print (regexresult)

#findall with meta characters
regexresult=re.findall(r"\w\spresent","Test1 present...test1...TEst1..Test2 present")
print (regexresult)
regexresult=re.findall(r"\dpresent","Test1present...test1...TEst1..Test2present")
print (regexresult)
regexresult=re.findall(r"present\D","Test1presentfirstinst...test1...TEst1..Test2presentsecondinst")
print (regexresult)
regexresult=re.findall(r"\wpresent","Test1present...test1...TEst1..Test2present")
print (regexresult)
regexresult=re.findall(r"present\w","Test1presentfirstinst...test1...TEst1..Test2presentsecondinst")
print (regexresult)
regexresult=re.findall(r"present\W","Test1present$firstinst...test1...TEst1..Test2present@secondinst")
print (regexresult)
regexresult=re.sub(r"pre\Ssent","pre-sent","Test1pre.sent$firstinst...test1...TEst1..Test2pre.sent@secondinst")
print (regexresult)
regexresult=re.sub(r"pre\Wsent","pre.sent","Test1pre.sent$firstinst...test1...TEst1..Test2pre.sent@secondinst")
print (regexresult)

#quantifier
regexq=re.findall(r"use?r","the search string : user1,usr2,usr4,usern,useer$")
print (regexq)
regexq=re.findall(r"use*r","the search string : user1,usr2,usr4,usern,useer$")
print (regexq)
regexq=re.findall(r"use+r","the search string : user1,usr2,usr4,usern,useer$")
print (regexq)

#find all email address
regexq=re.findall(r"\w+.\w+@\w+.\w+","abc@gmail.com saurabh.patel@gmail.com asdh.dfg@gmail.com")
print (regexq)

#find all phone no
regexq=re.findall(r"\+\d+\s\d+","abc@gmail.com +91 9540657890 saurabh.patel@gmail.com +91 8998765678 asdh.dfg@gmail.com")
print (regexq)

#find all phone no with defined range
regexq=re.findall(r"\+\d{2}\s\d{10}","abc@gmail.com +91 9540657890 saurabh.patel@gmail.com +91 8998765678 asdh.dfg@gmail.com")
print (regexq)

#find all different type phone no with defined range
regexq=re.findall(r"\+\d{2}\s?\d+\s?\d*\s?\d+","abc@gmail.com +91 9540657890 saurabh.patel@gmail.com +91 8998765678 asdh.dfg@gmail.com +919540657890 abc@yahoo.in +91 9540 6578 90")
print (regexq)

#find all IPs
regexq=re.findall(r"\d{1,3}:\d{1,3}:\d{1,2}.\d{1}/\d{2}","192:168:12.1/20 234:345:45.6/30 +9195402004")
print (regexq)

#find range
regexq=re.findall(r"\d+-\d+","The range is 7-8. The other required range is 70-80 700-800 4000-5000 500-980")
print (regexq)