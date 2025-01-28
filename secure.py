import html2text


#secure system
def secure(names, contacts, title, content):
    namesTitle = None

    if isinstance(names, list):
        namesTitle = [name.title() for name in names]
    elif isinstance(names, str):
        namesTitle = names.title()


    print(f'''\033[3;30;47m The names are: \033[0;0m {namesTitle}
\033[3;30;47m The email addresses are: \033[0;0m {contacts}
\033[3;30;47m Is that right? \033[0;0m
''')
    result1 = input("\033[3;30;47m Enter Y or N: \033[0;0m").lower()

    if result1 != "y":
        exit(0)

    print()

    print(f'''\033[3;30;47m The email content is: \033[0;0m
{html2text.html2text(content)}
\033[3;30;47m The email title is: \033[0;0m {title}
\033[3;30;47m Is that right? \033[0;0m
''')
    result2 = input("\033[3;30;47m Enter Y or N: \033[0;0m").lower()

    if result2 != "y":
        exit(0)
