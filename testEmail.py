import makeEmails, secure


#contacts information
name = "Robin Cai"
contact = "robinrainup@gmail.com"


#email content
title = "Test Title"


content = '''\
<p><span style="color:#607d8b;font-family:Georgia, serif;">Hi {userName},</span><br><br><span style="color:#607d8b;font-family:Georgia, serif;">Recently I uploaded a note in my Notion page. Feel free to check it out!</span></p>
<p>&nbsp;</p>
<p><span style="color:#607d8b;font-family:Georgia, serif;">Yours,</span></p>
<p><span style="color:#607d8b;font-family:Georgia, serif;">Robin</span></p>
<p><span style="color:#607d8b;font-family:Georgia, serif;font-size:12px;">This email was sent via a Python email system I made</span></p>
'''


#secure system
secure.secure(name, contact, title, content)


#send email
makeEmails.send(contacts = contact, title = title, content = content.format(userName = name))

print("email successfully sent")