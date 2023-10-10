-- 1. users 테이블 생성 쿼리문
CREATE TABLE users(
    pk TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    name  TEXT NOT NULL,
    age   INTEGER NOT NULL,
    phoneNumber NOT NULL,
    genter INTEGER,
    address NOT NULL DEFAULT 'no address'
);

-- 2. users테이블의 phoneNumber 컬럼 이름을 number로 변경하는 쿼리문
-- 칼럼 이름 변경
ALTER TABLE users
RENAME COLUMN phoneNumber TO number;

-- 3. users 테이블을 데이터베이스에서 제거하는 쿼리문
DROP TABLE users;