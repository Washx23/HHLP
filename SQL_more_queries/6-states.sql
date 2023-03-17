-- Cretae a database whit a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE auto_increment,
    name VARCHAR(256),
    PRIMARY KEY(id)
    );