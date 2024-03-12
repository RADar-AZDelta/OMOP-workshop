import subprocess

user_number=6   # Change this to your user number
project_id = f"user-project-{user_number}"
dataset_name = "raw_data"
bucket_path = f"gs://summer-school-bucket-{user_number}/{dataset_name}/"
location = "europe-west1"
source_format = "PARQUET"

# Check if the dataset exists, create it if not
dataset_exists_command = f"bq show {project_id}:{dataset_name}"
dataset_exists = subprocess.run(dataset_exists_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0

if not dataset_exists:
    create_dataset_command = f"bq --location={location} mk --dataset {project_id}:{dataset_name}"
    subprocess.run(create_dataset_command, shell=True)
    print(f"Dataset {dataset_name} created.")

# Get list of tables in the dataset
table_list_command = f"bq ls {project_id}:{dataset_name}"
table_list = subprocess.check_output(table_list_command, shell=True).decode().splitlines()

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
