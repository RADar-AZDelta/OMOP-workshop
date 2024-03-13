from google.cloud import bigquery
import subprocess
import json

def load_data_from_gcs_to_bq(project_id, dataset_name, bucket_path, location, source_format):
    # List files in a specific folder in the bucket
    bucket_files_command = f"gsutil ls {bucket_path}*.parquet"
    bucket_files = subprocess.check_output(bucket_files_command, shell=True).decode().splitlines()
    print(f"Files in {bucket_path}:")
    for file in bucket_files:
        print(file)

    # Iterate through files and create tables
    for file in bucket_files:
        table_name = file.split('/')[-1].replace(".parquet", "")
        
        # Check if the table exists, create it if not
        table_exists_command = f"bq show {project_id}:{dataset_name}.{table_name}"
        table_exists = subprocess.run(table_exists_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0
        
        if not table_exists:
            create_table_command = f"bq --location={location} mk --autodetect {project_id}:{dataset_name}.{table_name}"
            subprocess.run(create_table_command, shell=True)
            print(f"Table {table_name} created.")
        
        # Load data into the table
        bq_command = f"bq --location={location} load --source_format={source_format} {project_id}:{dataset_name}.{table_name} {file}"
        print(f"Executing: {bq_command}")
        
        # Execute the bq command
        subprocess.run(bq_command, shell=True)

def create_bigquery_dataset(project_id, dataset_id):
    # Create a BigQuery client
    client = bigquery.Client(project=project_id)

    # Check if the dataset already exists
    dataset_ref = client.dataset(dataset_id)

    try:
        client.get_dataset(dataset_ref)
        print(f"Dataset {dataset_id} already exists.")
    except Exception as e:
        # If the dataset doesn't exist, create it
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "europe-west1"
        dataset = client.create_dataset(dataset)
        print(f"Dataset {dataset.dataset_id} created.")


def create_multiple_datasets(project_id, user_number, datasets_to_create):

    for dataset_id in datasets_to_create:
        create_bigquery_dataset(project_id, dataset_id)

    load_data_from_gcs_to_bq(project_id, "raw_data", f"gs://summer-school-bucket-{user_number}/raw_data/", "europe-west1", "PARQUET")

def delete_bigquery_dataset(project_id, dataset_id):
    # Create a BigQuery client
    client = bigquery.Client(project=project_id)

    # Check if the dataset exists
    dataset_ref = client.dataset(dataset_id)

    try:
        client.get_dataset(dataset_ref)
        client.delete_dataset(dataset_ref, delete_contents=True)
        print(f"Dataset {dataset_id} deleted.")
    except Exception as e:
        print(f"Dataset {dataset_id} does not exist.")


def delete_multiple_datasets(project_id, datasets_to_delete):
    for dataset_id in datasets_to_delete:
        delete_bigquery_dataset(project_id, dataset_id)
  
def get_user_number(project_name):
    try:
        project_name_split = project_name.split(".")
        user_number = project_name_split[0][-1]
        return user_number
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
        
def get_project_info():
    try:
        result = subprocess.run(['gcloud', 'config', 'list', '--format=json'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        config_data = result.stdout.strip()
        if config_data:
            config_json = json.loads(config_data)
            project_id = config_json.get('core', {}).get('project')
            account = config_json.get('core', {}).get('account')
            user_number = get_user_number(account)
            return project_id, user_number
        else:
            print("No project configured.")
            return None, None
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")
        return None, None


if __name__ == "__main__":
    project_id, user_number = get_project_info()
    print(f"Start configuring Big Query of user {user_number}, project {project_id} ...")
    # List of datasets to create if they don't exist
    datasets = ["achilles", "dqd", "omop", "raw_data", "work"]
    delete_multiple_datasets(project_id, datasets)
    create_multiple_datasets(project_id, user_number, datasets)
