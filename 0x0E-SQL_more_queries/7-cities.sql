-- Write a script that creates DB hbtn_0d_usa & table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id int NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
name VARCHAR(256) NOT NULL);
