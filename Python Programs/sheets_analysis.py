import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name('', scope) #Enter the service account credentials here taken from google fdevelopers console
gc = gspread.authorize(credentials)
spreadsheet_key = '' #Enter the spreadsheet key here taken from sheet url
book = gc.open_by_key(spreadsheet_key)

worksheet = book.worksheet("Sheet1")

table = worksheet.get_all_values()

print (table)
