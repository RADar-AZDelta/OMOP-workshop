SELECT
  CONCAT("QUESTIONNAIRES_", question_id) AS sourceCode,
  question AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.questionnaires
WHERE
  question LIKE '%Gewicht%'
  OR question LIKE '%Lengt%'
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC