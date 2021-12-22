# -------------- Find patterns using reg ex -----------------------
# data source URL : https://www.kaggle.com/rtatman/fraudulent-email-corpus

# import library
import re  # to use reg ex functions
import email  # to work on email body

# ----------Use of iterator - print all name and address using For Loop as iterator---------------

emails = []  # an empty list to store dictionaries and each dictionary will contain the details of each email.
fe_file = open(r"Input Data/Fraudulent_emails.txt", "r").read()  # read text file

file_content = re.split(r"From r", fe_file)
file_content.pop(0)  # get rid of the first element (an empty string at index 0) in the list

for item in file_content:
    emails_dict = {}

    # Print sender's email address and name......................
    # Step 1: find the whole line beginning with "From:".
    sender = re.search(r"\nFrom:.*", item)
    # Step 2: find the email address and name.
    if sender is not None:
        s_email = re.search(r"\S+@\S+", sender.group())
        s_name = re.search(r":.*<", sender.group())
    else:
        s_email = None
        s_name = None
    # Step 3A: check email is none and if yes, assign email address as string to a variable.
    if s_email is not None:
        sender_email = s_email.group()
    else:
        sender_email = None
    # Add email address to dictionary.
    emails_dict["sender_email"] = sender_email
    # Step 3B: check name is none and if yes, name as string to a variable.
    if s_name is not None:
        sender_name = re.sub("\s*<", "", re.sub(":\s*", "", s_name.group()))
    else:
        sender_name = None
    # Add sender's name to dictionary.
    emails_dict["sender_name"] = sender_name

    # Print recipient's email address and name.....................
    # Step 1: find the whole line beginning with "To:".
    recipient = re.search(r"\nTo:.*", item)
    # Step 2: find the email address and name.
    if recipient is not None:
        r_email = re.search(r"\S+@\S+", recipient.group())
        r_name = re.search(r":.*<", recipient.group())
    else:
        r_email = None
        r_name = None
    # Step 3A: check email is none and if yes, assign email address as string to a variable.
    if r_email is not None:
        recipient_email = r_email.group()
    else:
        recipient_email = None
    # Add recipient's email to dictionary.
    emails_dict["recipient_email"] = recipient_email
    # Step 3B: check name is none and if yes, assign name as string to a variable.
    if r_name is not None:
        recipient_name = re.sub("s*<", "", re.sub(":s*", "", r_name.group()))
    else:
        recipient_name = None
    # Add recipient's name to dictionary.
    emails_dict["recipient_name"] = recipient_name

    # Print date of the email.........................
    # Step 1: find the whole line beginning with "Date:".
    date_field = re.search(r"Date:.*", item)
    # Step 2: find the date.
    if date_field is not None:
        date = re.search(r"\d+\s\w+\s\d+", date_field.group())
    else:
        date = None
    # Step 3: check date is none and if yes, assign date as string to a variable.
    if date is not None:
        date_sent = date.group()
    else:
        date_sent = None
    # Add date to dictionary.
    emails_dict["date_sent"] = date_sent

    # Print email subject...............................
    # Step 1: find the whole line beginning with "Subject:".
    subject_field = re.search(r"Subject: .*", item)
    # Step 2: find the subject.
    # Step 3: check subject is none and if yes, assign subject as string to a variable.
    if subject_field is not None:
        subject = re.sub(r"Subject: ", "", subject_field.group())
    else:
        subject = None
    # Add subject to dictionary.
    emails_dict["subject"] = subject

    # Print body of the email...................................
    # Step 1: separate header from body
    full_email = email.message_from_string(item)
    # Step 2: isolates the body of the email
    body = full_email.get_payload()
    # Add body to dictionary.
    emails_dict["email_body"] = body
    # append the dictionary to list.
    emails.append(emails_dict)

# Print number of key attributes in a dictionary within list
print("Number of key attributes: " + str(len(emails_dict)))
# Print number of lists
print("Number of lists: " + str(len(emails)))

# Print and export all values against each dictionary key for all emails list
with open('Output Data/3_Parsed_Fraudulent_Emails.text', 'w') as fe:
    for key in range(len(emails)):
        print(str(key) + ": " + str(emails[key]))
        fe.write('\n%s\n\n' % (str(key) + ": " + str(emails[key])))
# close the file
fe.close()

# # ............. Practice regular expression to find pattern in real time data set ..............

# # print the email senders (from) by simple python code
# for line in fe_file.split("n"):
#     if "From:" in line:
#         print(line)
# # not getting desired result
#
# # print the email senders (from) by using python's reg ex
# for line in re.findall("From:.*", fe_file):
#     print(line)
# # got desired output
#
# # find sender name
# find_name = re.findall("From:.*", fe_file)
# for line in find_name:
#     print(re.findall('\".*\"', line))
#
# # find email address
# find_email = re.findall("From:.*", fe_file)
# for line in find_email:
#     print(re.findall('\w\S*@*.\w', line))
#
# # find domain name of the email addresses
# find_add = re.findall("From:.*", fe_file)
# for item in find_add:
#     for line in re.findall("\w\S*@.*\w", item):
#         username, domain_name = re.split("@", line)
#         print("{}, {}".format(username, domain_name))
#
# # print full From: field in the email header
# sender_name = re.search("From:.*", fe_file)
# sender_address = sender_name.group()
# email = re.sub("From", "Email", sender_address)
# print(sender_address)
# print(email)


# # ............. Practice regular expression to find pattern .........................
# # https://regex101.com/
# # https://www.dataquest.io/blog/regex-cheatsheet/
# # r - converts to raw string to be readable by/at all means
# findall() matches all instances of a pattern in a string and returns them in a list
# search() matches the first instance of a pattern in a string, and returns it as a re match object.
# sub() substitutes parts of a string
# split() split the string

# # findall
# regex_result = re.findall(r"Test1 present", "Test1 present...test1...TEst1..Test2 present")
# print(regex_result)
#
# # split
# regex_result = re.split(r"@", "Test1 present@test1@TEst1@Test2 present")
# print(regex_result)
#
# # substitute
# regex_result = re.sub(r"@", "#", "Test1 present@test1@TEst1@Test2 present")
# print(regex_result)
#
# # findall with meta characters
# regex_result = re.findall(r"\w\spresent", "Test1 present...test1...TEst1..Test2 present")
# print(regex_result)
# regex_result = re.findall(r"\dpresent", "Test1present...test1...TEst1..Test2present")
# print(regex_result)
# regex_result = re.findall(r"present\D", "Test1presentfirstinst...test1...TEst1..Test2presentsecondinst")
# print(regex_result)
# regex_result = re.findall(r"\wpresent", "Test1present...test1...TEst1..Test2present")
# print(regex_result)
# regex_result = re.findall(r"present\w", "Test1presentfirstinst...test1...TEst1..Test2presentsecondinst")
# print(regex_result)
# regex_result = re.findall(r"present\W", "Test1present$firstinst...test1...TEst1..Test2present@secondinst")
# print(regex_result)
# regex_result = re.sub(r"pre\Ssent", "pre-sent", "Test1pre.sent$firstinst...test1...TEst1..Test2pre.sent@secondinst")
# print(regex_result)
# regex_result = re.sub(r"pre\Wsent", "pre.sent", "Test1pre.sent$firstinst...test1...TEst1..Test2pre.sent@secondinst")
# print(regex_result)
#
# # quantifier
# regex_q = re.findall(r"use?r", "the search string : user1,usr2,usr4,usern,useer$")
# print(regex_q)
# regex_q = re.findall(r"use*r", "the search string : user1,usr2,usr4,usern,useer$")
# print(regex_q)
# regex_q = re.findall(r"use+r", "the search string : user1,usr2,usr4,usern,useer$")
# print(regex_q)
#
# # find all email address
# regex_q = re.findall(r"\w+.\w+@\w+.\w+", "abc@gmail.com 1234 saurabh.patel@gmail.com 4567 asdh.dfg@gmail.com")
# print(regex_q)
#
# # find all phone no
# regex_q = re.findall(r"\+\d+\s\d+", "abc@gmail.com +91 9540657890 saurabh.patel@gmail.com https://www.dataquest.io /blog/ regular-expressions -data-scientists/ +91 8998765678 asdh.dfg@gmail.com")
# print(regex_q)
#
# # find all phone number with defined range
# regex_q = re.findall(r"\+\d{2}\s\d{10}", "abc@gmail.com +91 9540657890 saurabh.patel@gmail.com +91 8998765678 asdh.dfg@gmail.com")
# print(regex_q)
#
# # find all different type phone number with defined range
# regex_q = re.findall(r"\+\d{2}\s?\d+\s?\d*\s?\d+", "abc@gmail.com +91 9540657890 saurabh.patel@gmail.com +91 8998765678 asdh.dfg@gmail.com +919540657890 abc@yahoo.in +91 9540 6578 90")
# print(regex_q)
#
# # find all IPs
# regex_q = re.findall(r"\d{1,3}:\d{1,3}:\d{1,2}.\d{1}/\d{2}", "192:168:12.1/20 234:345:45.6/30 +9195402004")
# print(regex_q)
#
# # find range
# regex_q = re.findall(r"\d+-\d+", "The range is 7-8. The other required range is 70-80 700-800 4000-5000 500-980")
# print(regex_q)
