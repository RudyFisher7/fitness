SELECT 'Upper Body' AS type, * FROM exercise WHERE muscle_groups & 34815
UNION ALL
SELECT 'Lower Body', * FROM exercise WHERE muscle_groups & 30720
UNION ALL
SELECT 'Core', * FROM exercise WHERE muscle_groups & 1536
;