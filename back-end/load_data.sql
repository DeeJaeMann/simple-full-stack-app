-- Run after create_schema.sql

\COPY subjects FROM '/home/deemann/vscode-workspace/CodePlatoon/assessments/simple-full-stack-app-DeeJaeMann/back-end/data/subjects.csv' DELIMITER ',' CSV HEADER;

\COPY instructors FROM '/home/deemann/vscode-workspace/CodePlatoon/assessments/simple-full-stack-app-DeeJaeMann/back-end/data/instructors.csv' DELIMITER ',' CSV HEADER;

SELECT setval('subjects_id_seq', (SELECT MAX(id) FROM subjects));
SELECT setval('instructors_id_seq', (SELECT MAX(id) FROM instructors));