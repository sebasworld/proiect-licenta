

create table Users(
	userid SERIAL PRIMARY KEY,
	username varchar(50) NOT NULL,
	tip varchar(50) NOT NULL,
	passwd varchar(50) NOT NULL,
    unique(username)
);

select * from Users;

insert into Users(username,tip,passwd)
VALUES('username', 'tip', 'passwd');

delete from Users where username='sebi123'

drop table Users;





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



