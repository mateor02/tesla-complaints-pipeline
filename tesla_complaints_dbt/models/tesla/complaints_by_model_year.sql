SELECT
    model,
    EXTRACT(YEAR FROM date_of_incident) AS complaint_year,
    COUNT(*) AS complaint_count
FROM {{ source('tesla', 'complaints') }}
WHERE EXTRACT(YEAR FROM date_of_incident) >= 2015
GROUP BY model, complaint_year
ORDER BY complaint_year, model
