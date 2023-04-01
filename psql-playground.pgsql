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