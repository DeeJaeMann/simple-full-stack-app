-- Schema

-- Drop tables if they exist
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS instructors;

-- Create tables (csv as reference)
CREATE TABLE subjects (
    id                  serial PRIMARY KEY,
    title               varchar(30) NOT NULL,
    difficulty_level    int NOT NULL,
    description         varchar(255) NOT NULL
);

CREATE TABLE instructors (
    id                  serial PRIMARY KEY,
    first_name          varchar(30) NOT NULL,
    last_name           varchar(30) NOT NULL,
    age                 int NOT NULL,
    description         varchar(255) NOT NULL
);