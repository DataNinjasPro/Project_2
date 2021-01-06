use zoo_db;

INSERT INTO animals (name, endangered, numlegs, class, weight, nickname)
VALUES ("zebra", false, 4, "mammal", 500, "puzzle horse");

INSERT INTO animals (name, endangered, numlegs, class, weight, nickname)
VALUES ("centipede", false, 100, "bugz", 1, "tickle tube");

SELECT * FROM animals;
