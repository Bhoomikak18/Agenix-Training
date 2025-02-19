-- Total Number of Requests
SELECT COUNT(*) FROM logs;

-- Number of Unique IP Addresses
SELECT COUNT(DISTINCT ip) FROM logs;

-- Top 10 Most Frequent IP Addresses
SELECT ip, COUNT(*) as request_count
FROM logs
GROUP BY ip
ORDER BY request_count DESC
LIMIT 10;

-- Top 10 Most Requested URL Paths
SELECT url, COUNT(*) as request_count
FROM logs
GROUP BY url
ORDER BY request_count DESC
LIMIT 10;

 -- Busiest Hour of the Day (Based on Number of Requests)
SELECT DATE_TRUNC('hour', timestamp) AS timestamp_hour, 
       COUNT(*) AS request_count
FROM logs
GROUP BY timestamp_hour
ORDER BY request_count DESC
LIMIT 5;