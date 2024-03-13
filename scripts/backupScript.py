import os
from google.cloud import storage
import time


def create_bucket(bucket_name, location="europe-west1"):
    """Maak een nieuwe bucket aan op Google Cloud Storage met de opgegeven locatie."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    if not bucket.exists():
        bucket.create(location=location)
        print(f"Bucket {bucket_name} is succesvol aangemaakt in locatie {location}.")
    else:
        print(f"Bucket met de naam {bucket_name} bestaat al.")


def upload_files(bucket, folder_name, files):
    """Upload bestanden en submappen naar een specifieke map in de opgegeven bucket."""
    for file_name in files:
        file_path = os.path.join(folder_name, file_name)
        if os.path.isfile(file_path):
            start_time = time.time() * 1000  # omrekenen naar milliseconden
            blob = bucket.blob(folder_name + "/" + file_name)
            blob.upload_from_filename(file_path)
            end_time = time.time() * 1000  # omrekenen naar milliseconden
            duration = end_time - start_time
            print(
                f"Bestand {file_name} is succesvol geüpload naar map {folder_name} in bucket {bucket.name}. Duur: {duration:.2f} ms."
            )
        elif os.path.isdir(file_path):
            # Als het een directory is, roepen we de functie recursief aan voor die directory
            sub_files = os.listdir(file_path)
            sub_folder_name = os.path.join(folder_name, file_name)
            upload_files(bucket, sub_folder_name, sub_files)


if __name__ == "__main__":
    bucket_name = "summer-school-bucket-{projectnummer}-backup" # Vervang {projectnummer} door je projectnummer
    create_bucket(bucket_name, location="europe-west1")
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Lijst van bestanden in de map 'raw_data'
    files_in_raw_data = os.listdir("raw_data")
    upload_files(bucket, "raw_data", files_in_raw_data)

    # Lijst van bestanden in de map 'workshop_input'
    files_in_workshop_input = os.listdir("workshop_input")
    upload_files(bucket, "workshop_input", files_in_workshop_input)
