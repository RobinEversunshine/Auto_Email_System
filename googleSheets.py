from oauth2client.service_account import ServiceAccountCredentials
import gspread


scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

# access the json key downloaded from google api
credentials = ServiceAccountCredentials.from_json_keyfile_name("email-address-collection-590e72a46dcb.json", scopes)
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("Contacts (Responses)") # open google sheet and access to contacts
sheet = sheet.sheet1 # replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1


#get the column of email addresses
def getContacts():
    col = sheet.col_values(2)
    return col[1:]

def getNames():
    col = sheet.col_values(3)
    return col[1:]