SELECT
  CONCAT('CARESITE_', place_of_service_source_value) AS sourceCode,
  place_of_service_source_value AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.caresite
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC