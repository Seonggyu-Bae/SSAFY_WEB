-- pk, email, name, age
CREATE TABLE contacts(
-- column data_type constraints
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);