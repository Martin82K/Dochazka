-- vytvoreni databaze
CREATE DATABASE dochazka;

-- vytvoření tabulky s uživateli, která bude sloužit pro ověřování loginu
CREATE TABLE IF NOT EXISTS users ( 
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name VARCHAR(50), 
	surname VARCHAR(50),
	login_name VARCHAR(50),
	user_password VARCHAR(50),
	email VARCHAR(50),
	user_id INTEGER
);

-- vložení dat do tabulky uživatelů
INSERT INTO users (name, surname, login_name, user_password, user_id)
VALUES 
	('Martin', 'Nitram', 'martin', 'martin', '815'),
	('Petr', 'Svetr', 'jmeno', 'heslo', '007'),
	('Administrator', 'Systému', 'admin', 'system', '666');