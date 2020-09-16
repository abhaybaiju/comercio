CREATE TABLE Order_Index (
	id	varchar(30),
	ISIN	varchar(30),
	price	INT,
	qty	INT,
	aon	varchar(30),
	identifier	INT NOT NULL DEFAULT 0,
	BOS	varchar(30) NOT NULL DEFAULT 'b',
	LOM	varchar(30),
	PRIMARY KEY(id ),
	FOREIGN KEY(ISIN) REFERENCES Securities_Index(ISIN)
);

CREATE TABLE Rejected_Order (
	sr_no	INT AUTO_INCREMENT,
	ISIN	varchar(30) NOT NULL,
	price	INT NOT NULL,
	BOS	TEXT NOT NULL,
	qty	INT NOT NULL,
	aon	varchar(30) NOT NULL,
	LOM	varchar(30) NOT NULL,
	FOREIGN KEY(ISIN) REFERENCES Securities_Index(ISIN),
	PRIMARY KEY(sr_no) 
);

CREATE TABLE Securities_Index (
	ISIN varchar(30) PRIMARY KEY,
	name	varchar(30),
	type	varchar(30),
	ltprice INT
);

