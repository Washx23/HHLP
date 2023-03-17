-- creaet a databese whit table (cities)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT unique auto_increment,
    state_id INT,
    FOREIGN KEY (state_id) references states(id),
    name VARCHAR(256),
    PRIMARY KEY(id)
    );