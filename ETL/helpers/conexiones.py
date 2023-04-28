import pandas as pd
import bson
import io
import os

# Para conexion con API de Google Drive:
from google.oauth2 import service_account
from googleapiclient.discovery import build


def bson_to_dataframe(file_name):
    # Replace with the path to your service account file
    SERVICE_ACCOUNT_FILE = './adicional/basto-ganaderia-659c06703bdf.json'

    # Replace with the ID of the folder you want to list files for
    FOLDER_ID = '1VG0t3IeI7RX1PEDateMDuHqieVdhKij3'

    # Authenticate and create the Drive API client
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=creds)

    # Call the Drive API to list files in the specified folder
    results = service.files().list(q="'{}' in parents".format(FOLDER_ID), fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found in the specified folder')
    else:
        for item in items:
            if item['name'] == file_name:
                # Get the file ID and download URL
                file_id = item['id']
                file_url = 'https://drive.google.com/uc?id={}&export=download'.format(file_id)

                # Download the file content
                file_content = service.files().get_media(fileId=file_id).execute()

                # Convert the file content from bytes to BSON and then to a pandas DataFrame
                bson_data = io.BytesIO(file_content)
                df = pd.DataFrame(bson.decode_all(bson_data.getvalue()))

                return df

