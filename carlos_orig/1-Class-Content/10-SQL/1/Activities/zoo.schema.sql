drop database if exists zoo_db;

create database zoo_db;

use zoo_db;

drop table if exists animals;
create table animals (
    name VARCHAR(30) NOT NULL,
    endangered BOOLEAN NOT NULL,
    numlegs INTEGER(10),
    class VARCHAR(30),
    weight INTEGER(10),
    nickname VARCHAR(30)
);


create table animals (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    endangered BOOLEAN NOT NULL,
    numlegs INTEGER(10),
    class VARCHAR(30),
    weight INTEGER(10),
    nickname VARCHAR(30),
    PRIMARY KEY (id)
);
