SELECT
  CONCAT('QUESTIONNAIRES_', question_id) AS sourceCode,
  CONCAT(question) AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.questionnaires
WHERE
  question IN ( 'Roken',
    'cT',
    'cN',
    'cM',
    'WHO-score bij diagnose',
    'Histologische diagnose',
    'Digital rectal examination',
    'Transrectale echografie',
    'Voorgaande prostaat biopsie',
    'Genetisch risico',
    'primaire tumorlokalisatie',
    'Primaire tumorlocalisatie')
  AND answer_id IS NOT NULL
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC