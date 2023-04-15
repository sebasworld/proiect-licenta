create table Users(
	username varchar(50) NOT NULL,
	tip varchar(50) NOT NULL,
	passwd varchar(50) NOT NULL,
	primary key(username),
    unique(username)	
);

select * from Users;

insert into Users(username,tip,passwd)
VALUES('username', 'tip', 'passwd');

delete from Users where username='deelayy'

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
	facid int NOT NULL,
	facName varchar(100) NOT NULL,
	univName varchar(100) NOT NULL,
	locatie varchar(100) NOT NULL,
	rating numeric(2,1) NOT NULL,
	durataLicenta int NOT NULL,
	taxa varchar(100) NOT NULL,
	ultimaMedie numeric(3,2) NOT NULL,
	tipAdmitere varchar(100) NOT NULL,
	profilelev varchar(100) NOT NULL,
	primary key(facid),
    unique(facid)
);

drop table Facs;

insert into Facs(facid,facName,univName,locatie,
			rating,durataLicenta,taxa,ultimaMedie,tipAdmitere,profilelev)
VALUES(1, 'Facultatea de Automatică și Calculatoare - Ingineria Sistemelor', 'Universitatea Politehnica din București','București',
		 4.4, 4, 'taxa', 8.28, 'examen', 'mate-info');

insert into Facs(facid,facName,univName,locatie,
			rating,durataLicenta,taxa,ultimaMedie,tipAdmitere,profilelev)
VALUES(3, 'Facultatea de Automatică și Calculatoare - Ingineria Sistemelor', 'Universitatea Politehnica din București','București',
		 4.4, 4, 'buget', 8.37, 'examen', 'mate-info');

insert into Facs(facid,facName,univName,locatie,
			rating,durataLicenta,taxa,ultimaMedie,tipAdmitere,profilelev)
VALUES(4, 'Facultatea de Automatică și Calculatoare - Calculatoare și Tehnologia Informației', 'Universitatea Politehnica din București','București',
		 4.4, 4, 'taxa', 8.46, 'examen', 'mate-info');

insert into Facs(facid,facName,univName,locatie,
			rating,durataLicenta,taxa,ultimaMedie,tipAdmitere,profilelev)
VALUES(5, 'Facultatea de Automatică și Calculatoare - Calculatoare și Tehnologia Informației', 'Universitatea Politehnica din București','București',
		 4.4, 4, 'buget', 9.14, 'examen', 'mate-info');


select * from Facs;

delete all from Facs where facid=1;
create table Domenii(
	domid int NOT NULL,
	numeDomeniu varchar(50) NOT NULL,
	tipDegree varchar(50) NOT NULL,
	primary key(domid),
	unique(domid)
);

select * from Domenii;