SELECT
  CONCAT('measurement_', unit) AS sourceCode,
  unit AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.measurements
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC