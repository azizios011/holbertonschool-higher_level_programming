-- Check if the user user_0d_1 already exists
SELECT 1 FROM mysql.user WHERE user = 'user_0d_1';

-- If the user does not exist, create it and grant all privileges
IF NOT FOUND_ROWS() THEN
  CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
  GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
  FLUSH PRIVILEGES;
END IF;
