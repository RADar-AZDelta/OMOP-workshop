SELECT
  CONCAT("QUESTIONNAIRES_", question_id) AS sourceCode,
  CONCAT(question, " - ", questionnaire_name) AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.questionnaires
WHERE
  question = 'Datum'
  AND questionnaire_name = 'Bestraling specifiek'
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency desc