SELECT
  "Phidess" AS cdm_source_name,
  "Phidess" AS cdm_source_abbreviation,
  "BigQuery" AS cdm_holder,
  "Phidess summerschool" AS source_description,
  CAST(NULL AS STRING) AS source_documentation_reference,
  CAST(NULL AS STRING) AS cdm_etl_reference,
  CURRENT_DATE() AS source_release_date,
  CURRENT_DATE() AS cdm_release_date,
  "5.4.0" AS cdm_version,
  "OMOPCDM5.4" AS cdm_version_concept_id,
  "v5.0 03-SEP-23" AS vocabulary_version
