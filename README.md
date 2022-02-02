# DatabaseMigrationHelper
The idea of Database migration helper project came up when there is a database migration activity from SQL server database to Snowflake.
The project has multiple databases with over 500 tables, 200+ stored procedures, views with schema binding 
and function with custom logic which returns single valued as well as table valued parameters.
The team, however identified objects manually but I thought of writing a python program which automates the entire process.

For this project, I'm using Microsoft sql server sample database "WorldWideImporters" and mapped it to my local folder.

The program creates an excel file which will contain tables, procedures, views and functions sheets.

tables sheet lists all the tables given in the source folder and marks if the table has primary key, foreign key and indexes

procedures sheet lists all the stored procedures in the source folder and marks if the code has while loop, cursor implemented also indentifying the number of lines in procedure

views sheet lists all the views in the source folder and marks if the view has schema binding or joins which specifies that view is dependent on more than one table

functions sheet lists all the functions in the source folder and marks if a function has joins and the return type is table valued

we can pass the source folder, control which parts of the program to run like only tables or only procedures through the config file along with changing excel file name and destination folder.

This program can be extended to read data from online git location rather than cloning and reading it from local folders.
Can be extended to fetch all the security roles created in the database.