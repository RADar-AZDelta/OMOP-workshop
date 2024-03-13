SELECT
  CONCAT('MEASUREMENT_', measurement_id) AS sourceCode,
  measurement AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.measurements
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC