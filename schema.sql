CREATE TABLE IF NOT EXISTS episodes (
    id INTEGER NOT NULL, 
    name VARCHAR(50) NOT NULL, 
    episode VARCHAR(20) NOT NULL, 
    air_date DATE NOT NULL, 
    favorite BOOLEAN, 
    PRIMARY KEY (id)
);
