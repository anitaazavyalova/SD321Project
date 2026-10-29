/*
lab09
m281134, c. l. chau
m287116, a. a. zavyalova
m282418, o. k. green
*/

/*
mysql -h 127.0.0.1 -u m281134 -p m281134 < team4_create.sql

mysql -h db.cs.usna.edu -u m281134 -pm281134 m281134 -fcvvv < lab09drop.sql
mysql -h db.cs.usna.edu -u m281134 -pm281134 m281134 < team4_create.sql

mysql -h db.cs.usna.edu -u m281134 -pm281134 m281134 -fcvvv < team4_create.sql > team4_create.sql.txt 2>&1
*/

CREATE TABLE institutions (
    unitid INT PRIMARY KEY,
    institution VARCHAR(255) NOT NULL,
    state VARCHAR(5),
    control INT,
    level INT
);

CREATE TABLE college_outcomes (
    unitid INT PRIMARY KEY,
    costt4_a DECIMAL(15,6),
    c150_4 DECIMAL(15,6),
    c150_l4 DECIMAL(15,6),
    first_gen DECIMAL(15,6),
    faminc DECIMAL(15,6),
    grad_debt_mdn DECIMAL(15,6),
    md_earn_wne_p10 DECIMAL(15,6),
    FOREIGN KEY (unitid) REFERENCES institutions(unitid)
);

CREATE TABLE college_aid (
    unitid INT PRIMARY KEY,
    pgrnt_p DECIMAL(15,6),
    pgrnt_a DECIMAL(15,6),
    loan_p DECIMAL(15,6),
    loan_a DECIMAL(15,6),
    FOREIGN KEY (unitid) REFERENCES institutions(unitid)
);

/*
SHOW CREATE TABLE institutions;
SHOW CREATE TABLE college_outcomes;
SHOW CREATE TABLE college_aid;

SELECT * FROM institutions LIMIT 20;
SELECT * FROM college_outcomes LIMIT 20;
SELECT * FROM college_aid LIMIT 20;
*/
