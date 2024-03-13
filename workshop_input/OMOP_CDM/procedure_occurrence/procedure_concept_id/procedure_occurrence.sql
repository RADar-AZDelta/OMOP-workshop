SELECT
  CONCAT('PROCEDURES_', procedure_source_code) AS sourceCode,
  PROCEDURE AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.procedures
WHERE
  PROCEDURE IN ('Digital rectal examination',
    'Transrectale echografie')
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC