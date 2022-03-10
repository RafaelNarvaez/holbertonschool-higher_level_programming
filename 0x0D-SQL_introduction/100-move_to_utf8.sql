-- converts hbtn_0c_0 DB to 
-- utf8mb4 collate utf8mb4_unicode_ci
use hbtn_0c_0
ALTER TABLE first_table CONVERT TO CHARACTER
SET utf8mb4 COLLATE utf8mb4_unicode_ci;
