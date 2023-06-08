create table Users(
	userid SERIAL PRIMARY KEY,
	username varchar(50) NOT NULL,
	tip varchar(50) NOT NULL,
	passwd varchar(50) NOT NULL,
    unique(username)
);

select * from Users;

ALTER TABLE Users
ADD COLUMN id SERIAL PRIMARY KEY;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
ALTER TABLE Users ADD COLUMN random_string VARCHAR(5);

CREATE OR REPLACE FUNCTION generate_random_string()
  RETURNS TRIGGER AS $$
BEGIN
  NEW.random_string := substring(md5(random()::text), 1, 5);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER insert_random_string
  BEFORE INSERT ON Users
  FOR EACH ROW
  EXECUTE FUNCTION generate_random_string();


insert into Users(username,tip,passwd)
VALUES('username', 'tip', 'passwd');

delete from Users where username='sebi123'

drop table TipUsers;
drop table Users;

create table Univs(
	univid int NOT NULL,
	nume varchar(50) NOT NULL,
	locatie varchar(50) NOT NULL,
	rating int NOT NULL,
	rata_adm numeric(5,2) NOT NULL,
	primary key(univid),
    unique(univid),
	CHECK(rating BETWEEN 1 AND 5),
	CHECK(rata_adm >= 0 AND rata_adm <= 100)
);

create table Facs(
	facid int NOT NULL,
	univid int NOT NULL,
	nume varchar(50) NOT NULL,
	primary key(facid),
    unique(facid),
	CONSTRAINT fk_scenario
	   FOREIGN KEY(univid)
	     REFERENCES Univs(univid)
);

create table infoFacs(
	facid int NOT NULL,
	univid int NOT NULL,
	nume varchar(50) NOT NULL,
	primary key(facid),
    unique(facid),
	CONSTRAINT fk_scenario
	   FOREIGN KEY(univid)
	     REFERENCES Univs(univid)
);


SELECT * FROM Users WHERE 1 = 1;

create table Facs(
	facid SERIAL PRIMARY KEY,
	facName varchar(200) NOT NULL,
	univName varchar(200) NOT NULL,
	locatie varchar(200) NOT NULL,
	rating varchar(200) NOT NULL,
	durataLicenta varchar(200) NOT NULL,
	taxa varchar(200) NOT NULL,
	ultimaMedie varchar(200) NOT NULL,
	tipAdmitere varchar(200) NOT NULL,
	profilelev varchar(200) NOT NULL,
	domeniu varchar(200) NOT NULL,
	programestudiu varchar(200) NOT NULL,
	nivel_master varchar(200) NOT NULL,
	aspecte_domeniu_master varchar(200) NOT NULL,
	format_master varchar(200) NOT NULL,
	fac_link varchar(200) NOT NULL,
	alumni_jobs varchar(200) NOT NULL
);

ALTER TABLE Facs
ADD COLUMN facimg bytea;

drop table Facs;

select * from Facs;


SELECT distinct facName,univName,locatie,nivel_master,aspecte_domeniu_master,format_master FROM Facs where domeniu~'Inginerie' and (aspecte_domeniu_master~'Inovație și Cercetare' or aspecte_domeniu_master~'Dezvoltarea abilităților') and (locatie='București' or locatie='Iași') and (nivel_master='3' or nivel_master='4') and format_master='Hybrid'

SELECT distinct facName,univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu FROM Facs where profilelev='Matematică-Informatică' and (domeniu~'Știință & Tehnologie' or domeniu~'Arte & Umanism' or domeniu~'Afaceri & Științe Sociale'or domeniu~'Lingvistică & Cultură' or domeniu~'Inginerie' or domeniu~'Medicină & Sănătate') and (locatie='București' or locatie='Iași' or locatie='Cluj-Napoca' or locatie='Brașov'or locatie='Timișoara' or locatie='Craiova') and (tipAdmitere='Examen de admitere' or tipAdmitere='Pe bază de dosar') 
ALTER TABLE Facs
ADD COLUMN facimg bytea;


select * from Facs;
SELECT * FROM Facs WHERE 1 = 1 and domeniu ~ 'Inginerie'
delete *  from Users where username='Salut' and passwd='salut123'
select distinct username, tip, passwd from Users;
select * from Users;
SELECT distinct univName,facName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,nivel_master,aspecte_domeniu_master,format_master FROM Facs
SELECT distinct facName,univName FROM Facs where profilelev='Matematică-Informatică'

delete from Facs where facid=5;
create table DomeniiPoliBuc(
	domid int NOT NULL,
	numeDomeniu varchar(50) NOT NULL,
	licenta varchar(50) NOT NULL,
	master varchar(50) NOT NULL,
	doctorat varchar(50) NOT NULL,
	primary key(domid),
	unique(domid)
);

select * from DomeniiPoliBuc;

drop table Facs;

insert into DomeniiPoliBuc(domid,numedomeniu,licenta,master,doctorat)
VALUES(1, 'Inginerie','da','da','da');

insert into DomeniiPoliBuc(domid,numedomeniu,licenta,master,doctorat)
VALUES(2, 'Stiinta & Tehnologie','da','da','da');


insert into DomeniiPoliBuc(domid,numedomeniu,licenta,master,doctorat)
VALUES(3, 'Arte & Uman','nu','nu','nu');

insert into DomeniiPoliBuc(domid,numedomeniu,licenta,master,doctorat)
VALUES(4, 'Afaceri & Stiinte Sociale','nu','nu','nu');

insert into DomeniiPoliBuc(domid,numedomeniu,licenta,master,doctorat)
VALUES(5, 'Lingvistica & Cultura','nu','nu','nu');

insert into DomeniiPoliBuc(domid,numedomeniu,licenta,master,doctorat)
VALUES(6, 'Medicina & Sanatate','nu','nu','nu');
 