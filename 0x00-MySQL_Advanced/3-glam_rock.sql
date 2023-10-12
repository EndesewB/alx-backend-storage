-- List Glam rock bands ranked by longevity
SELECT
    band_name,
    IF(split > 0, 2022 - formed, 0) AS lifespan
FROM
    bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
