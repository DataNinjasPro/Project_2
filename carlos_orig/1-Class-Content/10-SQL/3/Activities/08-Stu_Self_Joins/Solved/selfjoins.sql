CREATE TABLE emps(
 employee_id int(8) NOT NULL,
 first_name varchar(125) NOT NULL,
 last_name varchar(125) NOT NULL,
 supervisor_id int(8),
 PRIMARY KEY(employee_id)
);

INSERT INTO emps VALUES (25, 'Sandy', 'Waxman', 100);
INSERT INTO emps VALUES (26, 'Yukio', 'Mishima', 100);
INSERT INTO emps VALUES (27, 'Serge', 'Gainsbourg', 100);
INSERT INTO emps VALUES (100, 'Sidney', 'Meiru', 100);

SELECT A.employee_id, A.first_name, B.last_name, CONCAT(B.first_name, ' ', B.last_name) AS 'Supervisor'
FROM emps A
JOIN emps B
ON (A.supervisor_id = B.employee_id);