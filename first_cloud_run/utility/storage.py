from google.cloud import storage
import os


class GCSStorageHandler:
    def __init__(self):
        self.__storage_client = storage.Client()
        self.__bucket_name = os.environ.get('BUCKET_NAME')
        self.bucket = self.__storage_client.bucket(self.__bucket_name)

    def download_file(self, blob_name: str, local_file_path: str) -> str:
        blob = self.bucket.blob(blob_name)
        blob.download_to_filename(local_file_path)
        return local_file_path

    def upload_file(self, blob_name: str, local_file_path: str) -> (str, str):
        blob = self.bucket.blob(blob_name)
        blob.upload_from_filename(local_file_path, timeout=3000)
        return blob_name, blob.public_url
