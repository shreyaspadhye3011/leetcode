create or replace table MOVIE (
    MID varchar2(5) not null constraint movie_pk primary key,
    NAME varchar2(50),
    YEAR number,
    DIRECTOR varchar2(50),
    LANGUAGE varchar2(20),
    COST number,
    COUNTRY varchar2(25)
);
/

create table MOVIE_ACTOR_LIST (
    MID varchar2(5),
    ACTOR varchar2(5),
    FOREIGN KEY (MID) REFERENCES MOVIE(MID)
);
/

create table MOVIE_GENRE_LIST (
    MID varchar2(5),
    GENRE varchar2(15),
    FOREIGN KEY (MID) REFERENCES MOVIE(MID)
);
/

INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M1', 'Scarface', 1988);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M2', 'Scent of a women', 1995);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M3', 'My big fat greek wedding', 2000);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M4', 'The Devil''s Advocate', 1997);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M5', 'Mr. and Mrs Smith', 1965);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M6', 'Now You see me', 2013);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M7', 'Barely Lethal', 2014);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M8', 'The Man with one red shoe', 1984);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M9', 'Polar Express', 2010);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M10', 'Her', 2013);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M11', 'Lucy', 2015);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M12', 'The Da Vinci Code', 2005);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M13', 'The God Father part II', 1975);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M15', 'Angels and Daemons', 2009);
INSERT INTO MOVIE(MID, NAME, YEAR) VALUES('M16', 'The Island', 2010);

create table PERSON (
    PID varchar2(5) not null constraint person_pk primary key,
    Name varchar2(50),
    Birthdate date,
    Gender varchar2(1),
    birthplace varchar2(25),
    Attribute varchar2(15),
    state varchar2(25),
    nation varchar2(25)
);
/

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P1', 'Brian de foma', TO_DATE('9/11/40', 'mm/dd/yyyy'), 'M', 'New York', 'Director');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P2', 'Martin Brest', '8/8/51', 'M', 'San Jose', 'Director');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P3', 'Scarlett Johanson', '11/22/84', 'F', 'Austin', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('', '', '', '', '');







