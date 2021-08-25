import os
import dropbox
from pkg_resources import Distribution

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)


        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode("overwrite"))

def main():
    access_token = 'sl.A3PhT1N9fFsVcsMnzzqwoSoH_3PHHcXDP8SDSOwjPUv8cA25bWrnpCkmG9LNxaaqelpfJG6BcAyZUj0ns01LDB0BOxr1dcvnRVKPiJoSZz7B4Z-XeKxuD1XHpyll7yh-Vjk2nwO6BCs'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to transfer")
    file_to = input("Enter the path to upload to the dropbox")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

if __name__ == '__main__':
    main()