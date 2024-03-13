SELECT
  CONCAT('CLINICALINFO_', 'ml') AS sourceCode,
  'ml' AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.clinicalinfo
--GROUP BY
--  sourceCode,
--  sourceName
--ORDER BY
--  sourceFrequency DESC