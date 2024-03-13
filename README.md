# OMOP-workshop


## Installatie

Ga naar je Google Cloud-account en log in. Controleer vervolgens of het project waarin je gaat werken correct is ingesteld. Het project moet je gebruikersnummer bevatten.

![Ga naar of dat je het juiste project geselecteerd hebt](/static/check_project.png)

Open de Cloud Shell en zodra deze is geladen, voer dan het volgende commando uit:

```bash
    gsutil cp gs://summer-school-bucket-USER_NUMBER/workshop_input/configure_big_query.py - | python
```
**Let op:** in dit commando moet je nog je gebruikersnummer aanpassen.

Dit commando zal BigQuery configureren met de benodigde datasets en in de 'raw_data'-dataset tabellen aanmaken met de vereiste gegevens.

De Cloud Shell kun je terugvinden rechts in je navigatiebalk:
![Hier vind je de Cloud Shell terug](/static/open_cloud_shell.png)

Eenmaal dit gelukt is, moet je naar de pagina met buckets navigeren op een van de volgende manieren:

![Eerste manier om te navigeren naar de Buckets](/static/navigate_to_bucket_1.JPG)

of

![Tweede manier om te navigeren naar de Buckets](/static/navigate_to_bucket_2.JPG)

Ga naar de `summer-school-bucket` met jouw gebruikersnummer. De bucket bevat het volgende:

- De map **raw_data** bevat alle gegevens die aanvankelijk zijn geladen in BigQuery.
- De map **workshop_input** bevat alle bestanden die je nodig zult hebben.

Download de map workshop_input. Plaats deze naar keuze op je apparaat.

![Download de map workshop_input](/static/download_workshop_input.png)

Als volgende stap zetten we de `riab.ini` klaar. Dit configuratiebestand maakt het mogelijk om lokaal op ons apparaat te werken met Rabbit in a Blender en tegelijkertijd de gegevens aan te passen in onze BigQuery.

```ini
[riab]
db_engine=bigquery

[bigquery]
credentials_file={credentials_file}.json
; The credentials file must be a service account key, stored authorized user credentials, external account credentials, or impersonated service account credentials. (see https://google-auth.readthedocs.io/en/master/reference/google.auth.html#google.auth.load_credentials_from_file)
; Alternatively, you can also use 'Application Default Credentials' (ADC) (see https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login)
location=europe-west1
; Location where to run the BigQuery jobs. Must match the location of the datasets used in the query. (important for GDPR)
project_raw={project_id}
; Can be handy if you use jinja templates for your ETL queries (ex if you are using development-staging-production environments). Must have the following format: PROJECT_ID
dataset_work={project_id}.work
; The dataset that will hold RiaB's housekeeping tables. Must have the following format: PROJECT_ID.DATASET_ID
dataset_omop={project_id}.omop
; The dataset that will hold the OMOP tables. Must have the following format: PROJECT_ID.DATASET_ID
dataset_dqd={project_id}.dqd
; The dataset that will hold the data quality tables. Must have the following format: PROJECT_ID.DATASET_ID
dataset_achilles={project_id}.achilles
; The dataset that will hold the data achilles tables. Must have the following format: PROJECT_ID.DATASET_ID
bucket=gs://summer-school-bucket-{user_number}/upload
; The Cloud Storage bucket uri, that will hold the uploaded Usagi and custom concept files. (the uri has format 'gs://{bucket_name}/{bucket_path}') 
```

Hier moeten de volgende dingen worden aangepast:

- **credentials_file**: Dit moet de naam zijn van de service key, het JSON-bestand dat te vinden is in de workshop_input-map die je hebt gedownload.
- **project_id**: Dit is het project-ID van het Google Cloud Project waarin je werkt. Je kunt dit vinden door op je project te klikken in de navigatiebalk. Er verschijnt een pop-up waarin je zowel de naam als het ID van het project zult zien.
- **user_number**: Dit is het nummer van het account dat je gebruikt. Je kunt dit vinden in het e-mailadres of in de naam van het Google Cloud Project.

Dit kun je handmatig invullen of je kunt gebruiken maken van de script `configure_ini.py`. In deze script kun je de nodige zaken aanvullen en de script uitvoeren in een terminal met de volgende command:

```bash
    python configure_ini.py
```
**Let op**: Om dit script te laten werken moeten de script en de riab.ini file op hetzelfde path liggen.

Zorg er als volgende stap voor dat je [Python versie 3.12](https://www.python.org/downloads/release/python-3120/) op je apparaat hebt geïnstalleerd. Je kunt de huidige versie die op je apparaat wordt gebruikt controleren door het volgende commando in een terminal in te voeren:

```bash
    python --version
```

Als de Python-versie correct is ingesteld, moet je de Python-package van Rabbit in a Blender installeren met het volgende commando:

```bash
    pip install Rabbit-in-a-Blender
```

Controleer of dit correct is gelukt door het volgende commando uit te voeren in je terminal:

```bash
    riab --version
```