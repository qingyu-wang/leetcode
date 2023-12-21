-- 1527. Patients With a Condition
-- https://leetcode.com/problems/patients-with-a-condition/description/

SELECT
    patient_id,
    patient_name,
    conditions
FROM
    Patients
WHERE
    conditions like "% DIAB1%"
    OR conditions like "DIAB1%";

--

SELECT
    patient_id,
    patient_name,
    conditions
FROM
    Patients
WHERE
   conditions REGEXP '^DIAB1.*|.* DIAB1.*';