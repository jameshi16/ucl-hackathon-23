drop table if exists Accounts;
create table Accounts(
    AID integer primary key,
    UserName varchar(64) unique,
    Password varchar(64)
);

drop table if exists Topics;
create table Topics(
    TID integer primary key,
    Topic varchar(64)
);

drop table if exists Progress;
create table Progress(
    PID integer primary key,
    AID integer,
    TID integer,
    foreign key (AID) references Accounts,
    foreign key (TID) references Topics
);

drop table if exists SubTopics;
create table SubTopics(
    STID integer primary key,
    SubTopic varchar(64)
);

drop table if exists Links;
create table Links(
    LID integer primary key,
    Link varchar(64)
);

drop table if exists StInT;
create table StInT(
    TID integer,
    STID integer,
    foreign key (TID) references Topics,
    foreign key (STID) references SubTopics
);

drop table if exists Content;
create table Content(
    STID integer,
    LID integer,
    foreign key (STID) references Subtopics,
    foreign key (LID) references Links
);

--Insert Dummy data, Comment out for live test
Insert into Accounts("UserName","Password") values
("user","pass"),
("user2","pass");

insert into Topics("Topic") values
("Object-Oriented Programming"),
("Calculus");

insert into Progress("AID","TID") values
(1,1),
(1,2),
(2,1);

SELECT Topic FROM Topics WHERE TID IN (1,2);
























