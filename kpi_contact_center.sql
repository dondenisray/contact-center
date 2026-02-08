---Total calls per day 

SELECT 
	call_date,
	COUNT (*) AS total_calls
	FROM Calls
	GROUP BY call_date;


----Answered calls

SELECT 
	call_date,
	SUM(CASE WHEN  answered = 1 THEN 1 ELSE 0 END) AS answered_calls
	FROM calls
	GROUP BY call_date;


---Answered calls / total calls

SELECT
    call_date,
    COUNT(*) AS total_calls,
    SUM(CASE WHEN answered = 1 THEN 1 ELSE 0 END) AS answered_calls,
    CAST(SUM(CASE WHEN answered = 1 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) AS answer_rate
FROM Calls
GROUP BY call_date;



----- NOT VALID DURATION 

SELECT * FROM Calls WHERE duration_seconds <= 0; 


---- AVG DURATIONN 

SELECT 
	call_date,

	AVG (duration_seconds) AS average_duration

FROM Calls

WHERE duration_seconds > 0 
	
GROUP BY call_date;
