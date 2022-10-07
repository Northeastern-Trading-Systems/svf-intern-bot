import dropbox
import os
from dotenv import load_dotenv
from dropbox.exceptions import ApiError, AuthError


class DropboxUtils:

    def __init__(self):
        load_dotenv()
        try:
            self.dbx = dropbox.Dropbox(os.environ['DBX_TOKEN'])
        except AuthError as e:
            self.dbx = None

    def upload_and_link(self, current: str, destination: str):
        with open(current, "rb") as doc:
            contents = doc.read()
            try:
                self.dbx.files_upload(contents, destination)
            except ApiError as e:
                return "Failed to upload file. Please contact bot admins."
            except AttributeError as e:
                return "Dropbox token failed, please contact bot admins."
            doc.close()
        link_object = self.dbx.files_get_temporary_link(destination)
        return f"Link to DCF (please download immediately): {link_object.link}"
