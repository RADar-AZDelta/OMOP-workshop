SELECT
  CONCAT('DOCTORS_', gender) AS sourceCode,
  gender AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.doctors
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency desc