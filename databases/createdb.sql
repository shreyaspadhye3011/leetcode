create table MOVIE (
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
    FOREIGN KEY (MID) REFERENCES MOVIE(MID) ON DELETE CASCADE
);
/

create table MOVIE_GENRE_LIST (
    MID varchar2(5),
    GENRE varchar2(15),
    FOREIGN KEY (MID) REFERENCES MOVIE(MID) ON DELETE CASCADE
);
/

INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M1', 'Scarface', 1988, 'P1');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M2', 'Scent of a women', 1995, 'P2');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M3', 'My big fat greek wedding', 2000, 'P4');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M4', 'The Devil''s Advocate', 1997, 'P1');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M5', 'Mr. and Mrs Smith', 1965, 'P1');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M6', 'Now You see me', 2013, 'P2');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M7', 'Barely Lethal', 2014, 'P4');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M8', 'The Man with one red shoe', 1984, 'P1');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M9', 'Polar Express', 2010, 'P2');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M10', 'Her', 2013, 'P2');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M11', 'Lucy', 2015, 'P4');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M12', 'The Da Vinci Code', 2005, 'P4');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M13', 'The God Father part II', 1975, 'P1');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M15', 'Angels and Daemons', 2009, 'P2');
INSERT INTO MOVIE(MID, NAME, YEAR, DIRECTOR) VALUES('M16', 'The Island', 2010, 'P4');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M1', 'P5');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M1', 'P6');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M2', 'P5');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M2', 'P6');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M3', 'P9');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M3', 'P7');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M4', 'P5');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M4', 'P6');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M4', 'P8');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M5', 'P7');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M5', 'P8');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M5', 'P5');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M6', 'P5');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M6', 'P6');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M6', 'P7');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M7', 'P5');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M7', 'P10');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M8', 'P9');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M8', 'P10');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M9', 'P9');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M9', 'P17');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M9', 'P19');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M10', 'P3');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M10', 'P5');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M10', 'P6');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M11', 'P3');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M11', 'P5');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M11', 'P8');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M11', 'P9');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M12', 'P9');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M12', 'P10');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M12', 'P3');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M13', 'P5');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M13', 'P6');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M13', 'P16');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M15', 'P12');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M15', 'P18');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M15', 'P9');

INSERT INTO MOVIE_ACTOR_LIST VALUES('M16', 'P10');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M16', 'P15');
INSERT INTO MOVIE_ACTOR_LIST VALUES('M16', 'P16');

INSERT INTO MOVIE_GENRE_LIST VALUES('M1', 'Action');



INSERT INTO MOVIE_GENRE_LIST VALUES('M2', 'Action');
INSERT INTO MOVIE_GENRE_LIST VALUES('M2', 'Comedy');
INSERT INTO MOVIE_GENRE_LIST VALUES('M3', 'Comedy');
INSERT INTO MOVIE_GENRE_LIST VALUES('M4', 'Thriller');

INSERT INTO MOVIE_GENRE_LIST VALUES('M5', 'Comedy');
INSERT INTO MOVIE_GENRE_LIST VALUES('M5', 'Action');
INSERT INTO MOVIE_GENRE_LIST VALUES('M6', 'Thriller');
INSERT INTO MOVIE_GENRE_LIST VALUES('M7', 'Action');
INSERT INTO MOVIE_GENRE_LIST VALUES('M8', 'Comedy');

INSERT INTO MOVIE_GENRE_LIST VALUES('M9', 'Comedy');
INSERT INTO MOVIE_GENRE_LIST VALUES('M10', 'Thriller');
INSERT INTO MOVIE_GENRE_LIST VALUES('M11', 'Thriller');
INSERT INTO MOVIE_GENRE_LIST VALUES('M12', 'Action');
INSERT INTO MOVIE_GENRE_LIST VALUES('M12', 'Thriller');

INSERT INTO MOVIE_GENRE_LIST VALUES('M13', 'Action');
INSERT INTO MOVIE_GENRE_LIST VALUES('M13', 'Thriller');

INSERT INTO MOVIE_GENRE_LIST VALUES('M15', 'Action');
INSERT INTO MOVIE_GENRE_LIST VALUES('M15', 'Thriller');

INSERT INTO MOVIE_GENRE_LIST VALUES('M16', 'Action');
INSERT INTO MOVIE_GENRE_LIST VALUES('M16', 'Comedy');


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

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P2', 'Martin Brest', TO_DATE('8/8/51', 'mm/dd/yyyy'), 'M', 'San Jose', 'Director');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P3', 'Scarlett Johanson', TO_DATE('11/22/84','mm/dd/yyyy'), 'F', 'Austin', 'Actor');


INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P4', 'Luc Besson', TO_DATE('5/30/75','mm/dd/yyyy'), 'F', 'Paris', 'Director');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P5', 'Morgan Freeman', TO_DATE('6/5/53','mm/dd/yyyy'), 'M', 'Canberra', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P6', 'Al Pacino', TO_DATE('11/12/26','mm/dd/yyyy'), 'M', 'Portland', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P7', 'Angelina Jolie', TO_DATE('3/3/70','mm/dd/yyyy'), 'F', 'Seattle', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P8', 'Brad Pitt', TO_DATE('4/4/75','mm/dd/yyyy'), 'M', 'London', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P9', 'Tom Hanks', TO_DATE('5/19/64','mm/dd/yyyy'), 'M', 'Perth', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P10', 'Jessica Alba', TO_DATE('8/7/83','mm/dd/yyyy'), 'F', 'Seoul', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P12', 'Alex Parish', TO_DATE('7/9/77','mm/dd/yyyy'), 'F', 'San Jose', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P13', 'Jack Nicholson', TO_DATE('11/13/58','mm/dd/yyyy'), 'M', 'Austin', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P15', 'Harrison Ford', TO_DATE('9/11/57','mm/dd/yyyy'), 'M', 'Canberra', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P16', 'Julia Roberts', TO_DATE('1/1/67','mm/dd/yyyy'), 'F', 'Portland', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P17', 'Matt Damon', TO_DATE('1/7/71','mm/dd/yyyy'), 'M', 'Seattle' 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P18', 'Jennifer Lawrence', TO_DATE('2/2/62','mm/dd/yyyy'), 'F', 'London', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P19', 'George clooney', TO_DATE('3/3/65','mm/dd/yyyy'), 'M', 'Perth', 'Actor');

INSERT INTO PERSON(PID, Name, Birthdate, Gender, birthplace, Attribute) VALUES('P20', 'Jennifer Aniston', TO_DATE('4/4/68','mm/dd/yyyy'), 'F', 'Seoul', 'Actor');


create table IMDB_USER (
    ID varchar2(5) PRIMARY KEY,
    EMAIL varchar2(80),
    FNAME varchar2(30),
    LNAME varchar2(30),
    DOB DATE,
    BIRTHPLACE varchar2(50),
    GENDER varchar2(1)
);

create table REVIEWS (
    MOVIE varchar2(5),
    AUTHOR varchar2(5),
    RATING number,
    VOTES number,
    PUBLISH_DATE TIMESTAMP,
    FOREIGN KEY (MOVIE) REFERENCES MOVIE(MID) ON DELETE CASCADE,
    FOREIGN KEY (AUTHOR) REFERENCES IMDB_USER(ID) ON DELETE CASCADE
);

INSERT INTO IMDB_USER VALUES('ID1', 'john@yahoo.com', 'John', 'Smith', TO_DATE('10/5/95','mm/dd/yyyy'), 'FL', 'M');

INSERT INTO IMDB_USER VALUES('ID2', 'juan@gmail.com', 'Juan', 'Carlos', TO_DATE('4/12/94','mm/dd/yyyy'), 'AK', 'M');

INSERT INTO IMDB_USER VALUES('ID3', 'Jane@gmail.com', 'Jane', 'Chapel', TO_DATE('11/2/93','mm/dd/yyyy'), 'IL', 'F');

INSERT INTO IMDB_USER VALUES('ID4', 'adi@yahoo.com', 'Aditya', 'Awasthi', TO_DATE('12/12/92','mm/dd/yyyy'), 'CA', 'M');

INSERT INTO IMDB_USER VALUES('ID5', 'james@hotmail.com', 'James', 'Williams', TO_DATE('5/5/91','mm/dd/yyyy'), 'NY', 'M');

INSERT INTO IMDB_USER VALUES('ID6', 'mike@yahoo.com', 'Mike', 'Brown', TO_DATE('3/1/88','mm/dd/yyyy'), 'NC', 'M');


INSERT INTO IMDB_USER VALUES('ID7', 'bob@yahoo.com', 'Bob', 'Jones', TO_DATE('2/7/88','mm/dd/yyyy'), 'NY', 'M');

INSERT INTO IMDB_USER VALUES('ID8', 'wei@gmail.com', 'Wei', 'Zhang', TO_DATE('8/12/85','mm/dd/yyyy'), 'NV', 'F');

INSERT INTO IMDB_USER VALUES('ID9', 'mark@gmail.com', 'Mark', 'Davis', TO_DATE('5/10/84','mm/dd/yyyy'), 'CA', 'M');

INSERT INTO IMDB_USER VALUES('ID10', 'daniel@yahoo.com', 'Daniel', 'Garcia', TO_DATE('6/1/80','mm/dd/yyyy'), 'NJ', 'M');

INSERT INTO IMDB_USER VALUES('ID11', 'maria@hotmail.com', 'Maria', 'Rodriguez', TO_DATE('3/18/75','mm/dd/yyyy'), 'CA', 'F');

INSERT INTO IMDB_USER VALUES('ID12', 'freya@yahoo.com', 'Freya', 'Wilson', TO_DATE('2/19/70','mm/dd/yyyy'), 'NJ', 'F');


INSERT INTO REVIEWS VALUES('M1', 'ID1', 7, 25, TO_DATE('10/02/07 09:10:54','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M2', 'ID2', 8, 35, TO_DATE('09/29/07 13:45:00','mm/dd/yyyy hh24:mi:ss'));




INSERT INTO REVIEWS VALUES('M2', 'ID3', 9, 24, TO_DATE('09/29/07 10:38:25','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M3', 'ID4', 10, 8, TO_DATE('10/02/13  13:05:56','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M3', 'ID5', 9, 11, TO_DATE('10/25/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M4', 'ID6', 8, 6, TO_DATE('09/26/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M4', 'ID7', 7, 23, TO_DATE('09/26/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M5', 'ID9', 9, 22, TO_DATE('09/28/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M6', 'ID10', 8, 26, TO_DATE('10/29/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M7', 'ID11', 8, 27, TO_DATE('09/30/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M7', 'ID12', 8, 18, TO_DATE('10/25/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M8', 'ID1', 7, 19, TO_DATE('09/25/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M9', 'ID2', 7, 16, TO_DATE('09/25/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M10', 'ID3', 8, 18, TO_DATE('09/29/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M11', 'ID4', 9, 22, TO_DATE('06/07/15 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M11', 'ID5', 10, 13, TO_DATE('05/05/15 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M12', 'ID6', 9, 50, TO_DATE('05/05/15 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M13', 'ID7', 5, 34, TO_DATE('10/25/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M13', 'ID1', 4, 34, TO_DATE('10/25/07 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M15', 'ID10', 8, 25, TO_DATE('05/05/15 17:15:00','mm/dd/yyyy hh24:mi:ss'));

INSERT INTO REVIEWS VALUES('M16', 'ID4', 7, 12, TO_DATE('05/05/15 17:15:00','mm/dd/yyyy hh24:mi:ss'));

create table ROLES (
    MOVIE varchar2(5),
    PERSON varchar2(5),
    ROLE varchar(25),
    FOREIGN KEY (MOVIE) REFERENCES MOVIE(MID) ON DELETE CASCADE,
    FOREIGN KEY (PERSON) REFERENCES PERSON(PID) ON DELETE CASCADE
);

INSERT INTO ROLES VALUES('M1', 'P5', 'Jessica');

INSERT INTO ROLES VALUES('M1', 'P6', 'Robert');
INSERT INTO ROLES VALUES('M2', 'P5', 'John');
INSERT INTO ROLES VALUES('M2', 'P6', 'Mark');
INSERT INTO ROLES VALUES('M3', 'P9', 'Alex');
INSERT INTO ROLES VALUES('M3', 'P7', 'Julie');
INSERT INTO ROLES VALUES('M4', 'P5', 'Jessica');
INSERT INTO ROLES VALUES('M4', 'P6', 'Matt');
INSERT INTO ROLES VALUES('M4', 'P8', 'Jennifer');

INSERT INTO ROLES VALUES('M5', 'P7', 'Jennifer');
INSERT INTO ROLES VALUES('M5', 'P8', 'Tom');
INSERT INTO ROLES VALUES('M5', 'P5', 'Milo');
INSERT INTO ROLES VALUES('M6', 'P6', 'Chris');
INSERT INTO ROLES VALUES('M6', 'P7', 'Rose');
INSERT INTO ROLES VALUES('M6', 'P5', 'Bill');
INSERT INTO ROLES VALUES('M7', 'P10', 'Jane');
INSERT INTO ROLES VALUES('M7', 'P5', 'Brad');
INSERT INTO ROLES VALUES('M8', 'P9', 'Lucas');
INSERT INTO ROLES VALUES('M8', 'P10', 'Juanita');

INSERT INTO ROLES VALUES('M9', 'P9', 'Clayne');
INSERT INTO ROLES VALUES('M9', 'P9', 'Jane');
INSERT INTO ROLES VALUES('M9', 'P9', 'Brad');
INSERT INTO ROLES VALUES('M9', 'P9', 'Lucas');
INSERT INTO ROLES VALUES('M9', 'P9', 'Bradley');
INSERT INTO ROLES VALUES('M9', 'P9', 'Justin');
INSERT INTO ROLES VALUES('M9', 'P17', 'Martin');
INSERT INTO ROLES VALUES('M9', 'P19', 'Mike');

INSERT INTO ROLES VALUES('M10', 'P3', 'Travis');
INSERT INTO ROLES VALUES('M10', 'P5', 'Alexander');
INSERT INTO ROLES VALUES('M10', 'P6', 'Justin');
INSERT INTO ROLES VALUES('M11', 'P3', 'Jessica');
INSERT INTO ROLES VALUES('M11', 'P5', 'Johny');
INSERT INTO ROLES VALUES('M11', 'P8', 'Rami');
INSERT INTO ROLES VALUES('M11', 'P9', 'Sam');

INSERT INTO ROLES VALUES('M12', 'P9', 'Gatek');
INSERT INTO ROLES VALUES('M12', 'P10', 'Rose');
INSERT INTO ROLES VALUES('M12', 'P3', 'maria');
INSERT INTO ROLES VALUES('M13', 'P5', 'Travis');
INSERT INTO ROLES VALUES('M13', 'P6', 'Alexander');
INSERT INTO ROLES VALUES('M13', 'P16', 'Pearl');
INSERT INTO ROLES VALUES('M15', 'P12', 'Sofia');
INSERT INTO ROLES VALUES('M15', 'P18', 'chrissy');

INSERT INTO ROLES VALUES('M15', 'P9', 'Mike');
INSERT INTO ROLES VALUES('M16', 'P10', 'Martin');
INSERT INTO ROLES VALUES('M16', 'P15', 'Bill');
INSERT INTO ROLES VALUES('M16', 'P16', 'Emilia');

create table SHOW (
    NAME varchar2(25),
    NETWORK varchar2(25),
    CATEGORY varchar2(10)
    PRIMARY KEY (NAME, NETWORK)
);

create table TV_SHOW_TEAM (
    NAME varchar2(25),
    NETWORK varchar2(25),
    ACTOR varchar2(5),
    PRODUCER varchar2(5),
    DIRECTOR varchar2(5),
    FOREIGN KEY (NAME, NETWORK) REFERENCES SHOW(NAME, NETWORK) ON DELETE CASCADE,
    FOREIGN KEY (ACTOR) REFERENCES PERSON(PID) ON DELETE CASCADE,
    FOREIGN KEY (DIRECTOR) REFERENCES PERSON(PID) ON DELETE CASCADE
);

create table FAVORITE_MOVIE_LIST (
    MID varchar2(5),
    ID varchar2(5),
    FOREIGN KEY (ID) REFERENCES IMDB_USER(ID) ON DELETE CASCADE,
    FOREIGN KEY (MID) REFERENCES MOVIE(MID) ON DELETE CASCADE
);

create table FAVORITE_SHOW_LIST (
    NAME varchar2(5),
    NETWORK varchar2(25),
    ID varchar2(5),
    FOREIGN KEY (NAME, NETWORK) REFERENCES SHOW(NAME, NETWORK) ON DELETE CASCADE,
    FOREIGN KEY (ID) REFERENCES IMDB_USER(ID) ON DELETE CASCADE
);

create table REVIEWED_MOVIE_LIST (
    MID varchar2(5),
    ID varchar2(5),
    FOREIGN KEY (ID) REFERENCES IMDB_USER(ID) ON DELETE CASCADE,
    FOREIGN KEY (MID) REFERENCES MOVIE(MID) ON DELETE CASCADE
);

create table TOWATCH_MOVIE_LIST (
    MID varchar2(5),
    ID varchar2(5),
    FOREIGN KEY (ID) REFERENCES IMDB_USER(ID) ON DELETE CASCADE,
    FOREIGN KEY (MID) REFERENCES MOVIE(MID) ON DELETE CASCADE
);

create table REVIEWED_SHOW_LIST (
    NAME varchar2(5),
    NETWORK varchar2(25),
    ID varchar2(5),
    FOREIGN KEY (NAME, NETWORK) REFERENCES SHOW(NAME, NETWORK) ON DELETE CASCADE,
    FOREIGN KEY (ID) REFERENCES IMDB_USER(ID) ON DELETE CASCADE
);

create table TOWATCH_SHOW_LIST (
    NAME varchar2(5),
    NETWORK varchar2(25),
    ID varchar2(5),
    FOREIGN KEY (NAME, NETWORK) REFERENCES SHOW(NAME, NETWORK) ON DELETE CASCADE,
    FOREIGN KEY (ID) REFERENCES IMDB_USER(ID) ON DELETE CASCADE
);

create table SEASONS (
    NAME varchar2(5),
    NETWORK varchar2(25),
    SEASON_NUMBER NUMBER,
    SDATE DATE,
    EDATE DATE,
    FOREIGN KEY (NAME, NETWORK) REFERENCES SHOW(NAME, NETWORK) ON DELETE CASCADE
);

create table EPISODES (
    NAME varchar2(5),
    NETWORK varchar2(25),
    EP_NUMBER NUMBER,
    TTILE varchar2(25),
    SEASON_NUMBER NUMBER,
    LENGTH varchar2(25),
    FOREIGN KEY (NAME, NETWORK) REFERENCES SHOW(NAME, NETWORK) ON DELETE CASCADE
);

create table SCENES (
    MID varchar2(5),
    Location varchar2(25),
    Scene_No number,
    FOREIGN KEY (MID) REFERENCES MOVIE(MID) ON DELETE CASCADE
);

create table AWARDS (
    INSTITUTION varchar2(50),
    YEAR NUMBER(5),
    CATEGORY varchar2(50),
    PRIMARY KEY (INSTITUTION, YEAR, CATEGORY)
);








