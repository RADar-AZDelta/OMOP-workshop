SELECT
  CONCAT('PATIENT_', gender) AS sourceCode,
  gender AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.pdj_phidess_raw_dataset.patient
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC
