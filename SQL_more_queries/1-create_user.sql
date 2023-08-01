-- script that creates the MySQL server user user_0d_1.
create user if not exists 'user_0d_1'@'localhost' 
IDENTIFIED BY 'user_0d_1_pwd';
GRANT all privileges on *.* to 'user_0d_1'@'localhost';
FLUSH privileges;
