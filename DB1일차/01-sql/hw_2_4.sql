CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);


-- zoo 테이블에서 weight가 100 이하인 것을 지우는데
-- ROLLBACK을 했으니 다시 원상복구를 한다
-- 다음은 zoo 테이블에서 eat 컬럼의 값이 omnivore인 레코드를 지우는데
-- 커밋되서 진짜 지워짐
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

-- 그래서 zoo 테이블의 레코드를 카운트하면 3이나옴
SELECT COUNT(*)
FROM zoo;
