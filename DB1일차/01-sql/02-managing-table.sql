-- id, title, content
CREATE TABLE article(
-- column data_type constraints
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    userid INTEGER NOT NULL,
    FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE TABLE user(
-- column data_type constraints
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(30) NOT NULL UNIQUE,
    email varchar(30) UNIQUE
);

INSERT INTO user (username, email)
    VALUES
    ('홍길동', 'hong@email.com'),
    ('이순신', 'lee@email.com'),
    ('유관순', 'ryu@email.com');




-- 삭제 : DROP
DROP TABLE article;


-- 데이터를 넣는 방법 : INSERT

INSERT INTO article (title, content,userid)
    VALUES ('제목1','데이터를 넣어봅시다.',50);


-- ALTER TABLE
-- 테이블 및 컬럼 수정

-- 칼럼 추가
ALTER TABLE article
ADD COLUMN created_at DATE NOT NULL DEFAULT '';

-- 칼럼 이름 변경
ALTER TABLE article
RENAME COLUMN contents TO content;

-- 칼럼 삭제
ALTER TABLE article
DROP created_at;

-- DML (Data Manipulation Language) : INSERT, UPDATE, DELETE

-- 데이터를 넣는 방법 : INSERT
INSERT INTO article(title,content,userid)
    VALUES ('제목1','user3이 쓴 글',3);


-- 기존의 레코드를 수정하기 : UPDATE
UPDATE article
SET created_at = '1910-01-01'
WHERE id = 4;

UPDATE article
SET title = 'Updated title'
WHERE id = 1;

-- 레코드 삭제 :DELETE
DELETE FROM article
WHERE id = 3;

-- article 테이블에서 작성일이 오래된 순으로 레코드 2개 삭제
DELETE FROM article
WHERE id IN (
    SELECT id FROM article
    ORDER BY created_at
    LIMIT 2
);


SELECT *
    FROM article
WHERE id = (
    SELECT id
        FROM article
    ORDER BY id
    LIMIT 1
);



-- article 테이블에 userid가
-- user 테이블에 존재하지 않는 경우 데이터삭제

DELETE
    FROM article
WHERE userid not in(
    SELECT id FROM user
);