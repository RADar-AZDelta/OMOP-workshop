SELECT
  CONCAT('CLINICALINFO_', clinical_info) AS sourceCode,
  CAST(clinical_info AS string) AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.clinicalinfo
WHERE
  clinical_info like '%volume%'
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC