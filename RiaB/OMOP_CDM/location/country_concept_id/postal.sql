SELECT
  CONCAT('POSTAL_', country_code) AS sourceCode,
  country AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.postal
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC