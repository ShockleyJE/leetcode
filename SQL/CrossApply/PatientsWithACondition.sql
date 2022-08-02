/* Write your T-SQL query statement below */
--https://leetcode.com/problems/patients-with-a-condition/submissions/
SELECT 
patient_id
,patient_name
,conditions
FROM Patients
WHERE patient_id IN (
SELECT patient_id
FROM (
	SELECT patient_id, value AS condition 
	FROM Patients  
		CROSS APPLY STRING_SPLIT(conditions, ' ')  
) AS subq
WHERE condition like 'DIAB1%'
)