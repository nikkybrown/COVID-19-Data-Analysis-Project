1. Retrieve the cumulative counts of confirmed, deceased, and recovered cases.

%%sql
select sum(confirmed) As confirmed,sum(deaths) AS deaths,sum(recovered) AS recovered from covid_19_data;

2.Extract the aggregate counts of confirmed, deceased, and recovered cases for
the first quarter of each observation year.

%%sql
select observationdate AS year ,sum(deaths) AS dc ,sum(confirmed) AS cc ,sum(recovered) AS rc
from covid_19_data
WHERE extract(quarter from observationdate) =1
AND extract (year from observationdate) in (2019,2020)
GROUP BY year

3.Formulate a comprehensive summary encompassing the following for each
country:
Total confirmed cases
Total deaths
Total recoveries

%%sql
select country ,sum(confirmed) AS total_confirmed_case ,sum(deaths) AS total_deaths,sum(recovered) AS total_recovered
from covid_19_data
GROUP BY country
ORDER BY total_confirmed_case DESC

4.Determine the percentage increase in the number of death cases from 2019
to 2020.

%%sql
SELECT (
    (SUM(CASE WHEN EXTRACT(YEAR FROM observationdate )= 2020 THEN deaths ELSE 0 END) - SUM(CASE WHEN EXTRACT(YEAR FROM observationdate )= 2019 THEN deaths ELSE 0 END)) / SUM(CASE WHEN EXTRACT(YEAR FROM observationdate )= 2019 THEN deaths ELSE 0 END)) * 100 AS percentage_increase
FROM covid_19_data
WHERE EXTRACT(YEAR FROM observationdate) IN (2019, 2020);

5.Compile data for the top 5 countries with the highest confirmed cases.

%%sql
SELECT country,max(confirmed) AS confirmed FROM covid_19_data GROUP BY country ORDER BY confirmed DESC limit 5


6.Calculate the net change (increase or decrease) in confirmed cases on a
monthly basis over the two-year period.

%%sql
WITH monthly_cases AS (
  SELECT 
    DATE_TRUNC('month', observationdate) AS month,
    COUNT(*) AS confirmed
  FROM covid_19_data
  WHERE observationdate >= '2019-01-01 00:00:00' AND observationdate < '2021-01-01 00:00:00'
  GROUP BY month
  ORDER BY month
)
SELECT
  observationdate, confirmed - LAG(confirmed) OVER (ORDER BY observationdate) AS net_change
FROM covid_19_data;