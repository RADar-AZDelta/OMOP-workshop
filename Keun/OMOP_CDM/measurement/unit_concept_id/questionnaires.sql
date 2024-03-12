SELECT
  CASE question
    WHEN "BMI (ophalen)" THEN CONCAT("QUESTIONNAIRES_",'kg/m2')
    WHEN "Lengte (ophalen)" THEN CONCAT("QUESTIONNAIRES_",'cm')
    WHEN "Gewicht (ophalen)" THEN CONCAT("QUESTIONNAIRES_",'kg')
    WHEN "Lengte (cm)" THEN CONCAT("QUESTIONNAIRES_",'cm')
    WHEN "Gewicht" THEN CONCAT("QUESTIONNAIRES_",'kg')
  END AS sourceCode,
  CASE question
    WHEN "BMI (ophalen)" THEN "kg/m2"
    WHEN "Lengte (ophalen)" THEN "cm"
    WHEN "Gewicht (ophalen)" THEN "kg"
    WHEN "Lengte (cm)" THEN "cm"
    WHEN "Gewicht" THEN "kg"
  END AS sourceName,
  COUNT(*) AS sourceFrequency
FROM
  phidess-student1.phidess_raw_dataset.questionnaires
WHERE
  question IN ("BMI (ophalen)",
    "Lengte (ophalen)",
    "Gewicht (ophalen)",
    "Lengte (cm)",
    "Gewicht")
GROUP BY
  sourceCode,
  sourceName
ORDER BY
  sourceFrequency DESC