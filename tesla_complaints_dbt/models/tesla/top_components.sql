SELECT
    model,
    components,
    EXTRACT(YEAR FROM date_of_incident) AS complaint_year,
    COUNT(*) AS complaint_count
FROM {{ source('tesla', 'complaints') }}
WHERE
    EXTRACT(YEAR FROM date_of_incident) >= 2015
    AND components IS NOT NULL
    AND components <> 'Unknown'
GROUP BY model, complaint_year, components
ORDER BY complaint_count DESC
