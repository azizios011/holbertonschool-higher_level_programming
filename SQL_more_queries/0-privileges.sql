-- list all the privileges of two users.
SELECT * FROM user_privileges WHERE grantee IN ('user_0d_1@localhost', 'user_0d_2@localhost');
