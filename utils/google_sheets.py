from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# Google Sheets authentication and data retrieval
def authenticate_sheets():
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    flow = InstalledAppFlow.from_client_secrets_file("path/to/credentials.json", scopes=scopes)
    creds = flow.run_local_server(port=0)
    service = build("sheets", "v4", credentials=creds)
    return service

def get_sheet_data(sheet_id, range_name):
    service = authenticate_sheets()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    return result.get("values", [])