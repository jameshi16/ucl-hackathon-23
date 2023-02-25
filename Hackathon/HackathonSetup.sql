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
    Title varchar(64),
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

insert into SubTopics("SubTopic") values
("Abstraction"),
("Overloading"),
("Encapsulation"),
("Differentiation"),
("Integration");

insert into StInT("TID","STID") values
(1,1),
(1,2),
(1,3),
(2,4),
(3,5);

insert into Links("Title","Link") values
("Learning Abstraction","56743tyfgh45"),
("Learning Abstraction 2","16789tyfgh45"),
("Learning Overloading","45789tyfgh45"),
("Learning Encapsulation","67894gtyfgh45"),
("Learning Differentiation","56789t45"),
("Learning Differentiation 2","567yfgh45"),
("Learning Integration","56da33rtyfgh45");

insert into Content("STID","LID") values
(1,1),
(1,2),
(2,3),
(3,4),
(4,5),
(4,6),
(5,7);























