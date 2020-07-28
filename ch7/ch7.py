import pyperclip, re

phone_regex = re.compile(r'''(
    (\()?       #front bracket
    (\d{2})?    #area code
    (\)|-)?     #last bracket or seperator
    (\d{3,4})   #the former part of phone number
    (-|\s)?     #seperator
    (\d{3,4})   #last part of phone number
)''', re.VERBOSE)

cellphone_regex = re.compile(r'''(
    09\d{2}  
    (-|\s)?    #seperator
    \d{3}
    (-|\s)?    #seperator
    \d{3}
)''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-=]+   #username
    @                    #@symbol
    [a-zA-Z0-9.-]+         #domain name
    (\.[a-zA-Z0-9]{2,4})+    #not fixed length of email address
    )''', re.VERBOSE)

text = str(pyperclip.paste())
#text = '02-27075832 is my personal email hsuanyin81@gmail.com'

phone = phone_regex.findall(text)    
#print(phone)
matches = []
for i in phone:
    phonenum = '-'.join([i[2], i[4], i[6]])
    matches.append(phonenum)

email = email_regex.findall(text)
#print(email)
for mail in email:
    emailadd = mail[0]
    matches.append(emailadd)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('The informaiton copy to clipboard:')
    print('\n'.join(matches))
else:
    print('There is no match.')
    
    

