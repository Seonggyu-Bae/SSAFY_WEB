-- 01. Querying data
SELECT LastName FROM employees;

SELECT LastName, FirstName FROM employees;


SELECT FirstName AS '이름' FROM employees;



SELECT * FROM employees;


SELECT
    Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks;

-- 02. Sorting data
-- ORDER BY

SELECT
    FirstName AS '이름'
FROM
    employees
ORDER BY
    FirstName;
    

-- DESC : 내림차순 정렬
SELECT
    FirstName AS '이름'
FROM
    employees
ORDER BY
    FirstName DESC;


-- country 기준으로는 city가 오름차순으로 정렬
SELECT
    Country, City
FROM
    customers
ORDER BY
    Country DESC,
    City;


SELECT
    Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
    tracks
ORDER BY
    Milliseconds DESC;



-- NULL 정렬 예시
-- NULL 값이 존재할 경우 오름차순 정렬시 결과에 NULL이 먼저 출력
SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo;


-- 03. Filtering data
    -- DISTINCT statement : 조회결과에서 중복된 레코드를 제거

SELECT DISTINCT
    Country
FROM
    customers
ORDER BY
    Country;


    -- WHERE syntax :

SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City = 'Prague';


SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City != 'Prague';

SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    Company IS NULL AND Country = 'USA';

SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    Company IS NULL OR Country = 'USA';


SELECT
    Name, Bytes
FROM
    tracks
WHERE
    Bytes BETWEEN 10000 AND 500000;


SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    Country IN ('Canada', 'Germany','France');
    --Country = 'Canada'
    --OR Country = 'Germany'
    --OR Country = 'France';


SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    Country NOT IN ('Canada', 'Germany','France');


-- 필드값이 'son'으로 끝나는
SELECT
    LastName, FirstName
FROM
    customers
WHERE
    LastName LIKE '%son';


-- 필드 값이 4자리이면서 'a'로 끝나는
SELECT
    LastName, FirstName
FROM
    customers
WHERE
    FirstName LIKE '___a'; -- _ ; 3개랑 a == 자리


-- LIMIT  활용
-- 조회 -> 정렬 -> 제한 순
SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    Bytes DESC
LIMIT 7;


SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    Bytes DESC
LIMIT 4 OFFSET 3;
-- LIMIT 3, 4;



-- 04. Grouping data
SELECT
    Country, COUNT(*)
FROM
    customers
GROUP BY
    Country;


SELECT
    Composer, AVG(Bytes)
FROM
    tracks
GROUP BY
    Composer
ORDER BY
    AVG(Bytes) DESC;


-- 집계 항목에 대한 세부조건은 HAVING 사용
SELECT
    Composer, AVG(Milliseconds/60000) AS avgOfMinute
FROM        
    tracks
--WHERE
    --avgOfMinute <  10
GROUP BY
    composer
HAVING
    avgOfMinute < 10
ORDER BY
    avgOfMinute DESC;


-- 에러


-- 에러 해결
