-- Script to list all privileges for users 'user_0d_1' and 'user_0d_2' on localhost
SELECT 
    GRANTEE, 
    PRIVILEGE_TYPE
FROM 
    information_schema.user_privileges
WHERE 
    GRANTEE = "'user_0d_1'@'localhost'";

-- Query privileges for user_0d_2
SELECT 
    GRANTEE, 
    PRIVILEGE_TYPE
FROM 
    information_schema.user_privileges
WHERE 
    GRANTEE = "'user_0d_2'@'localhost'";


