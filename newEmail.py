import makeEmails, googleSheets, secure


#contacts information
names = googleSheets.getNames()
contacts = googleSheets.getContacts()


#email content
title = "Test Title"


contentMain = '''
<p><span style="color:#607d8b;font-family:Georgia, serif;">Hi {userName},</span><br><br><span style="color:#607d8b;font-family:Georgia, serif;">Recently I uploaded a note in my Notion page. Feel free to check it out!</span></p>
<p>&nbsp;</p>
<p><span style="color:#607d8b;font-family:Georgia, serif;">Yours,</span></p>
<p><span style="color:#607d8b;font-family:Georgia, serif;">Robin</span></p>
<p><span style="color:#607d8b;font-family:Georgia, serif;font-size:12px;">This email was sent via a Python email system I made</span></p>
'''


#secure system
secure.secure(names, contacts, title, contentMain)


#send emails to everyone
for i, name in enumerate(names):
    contact = contacts[i]
    content = contentMain.format(userName = name.title())

    makeEmails.send(contacts = contact, title = title, content = content)

print(f"{len(names)} emails successfully sent")