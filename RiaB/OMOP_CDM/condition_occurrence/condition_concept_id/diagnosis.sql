SELECT
  CONCAT("DIAGNOSES_", d.diagnosis_sourcecode) AS sourceCode,
  d.diagnosis AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.diagnosis d
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC