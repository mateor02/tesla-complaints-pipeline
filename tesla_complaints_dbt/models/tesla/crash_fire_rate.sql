SELECT
    model,
    EXTRACT(YEAR FROM date_of_incident) AS complaint_year,
    COUNT(*) AS complaint_count,
    SUM(CASE WHEN crash THEN 1 ELSE 0 END) AS crash_count,
    SUM(CASE WHEN fire THEN 1 ELSE 0 END) AS fire_count,
    ROUND(
        (SUM(CASE WHEN crash THEN 1 ELSE 0 END)::NUMERIC / COUNT(*)) * 100.0, 2
    ) AS crash_rate,
    ROUND(
        (SUM(CASE WHEN fire THEN 1 ELSE 0 END)::NUMERIC / COUNT(*)) * 100.0, 2
    ) AS fire_rate
FROM {{ source('tesla', 'complaints') }}
WHERE EXTRACT(YEAR FROM date_of_incident) >= 2015
GROUP BY model, complaint_year
ORDER BY crash_rate DESC
