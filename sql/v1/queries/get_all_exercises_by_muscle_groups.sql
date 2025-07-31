SELECT 'Upper Body' AS type, * FROM exercise WHERE muscle_groups & 15871
UNION ALL
SELECT 'Legs', * FROM exercise WHERE muscle_groups & 66846720
UNION ALL
SELECT 'Core', * FROM exercise WHERE muscle_groups & 229376
UNION ALL
SELECT 'Core (back)', * FROM exercise WHERE muscle_groups & 16384
;