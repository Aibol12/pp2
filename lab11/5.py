import psycopg2 
 
conn = psycopg2.connect( 
    host="localhost", 
    database="phonebook", 
    user="user124", 
    password="3456753kk"
) 

cursor = conn.cursor() 

sql = ''' 
    create or replace procedure deleteph(name_ varchar) 
    as 
    $$ 
    begin 
        delete from phonebook where name = name_; 
    end; 
    $$ 
        LANGUAGE plpgsql; 
    ''' 
cursor.execute(sql) 
conn.commit() 
sql2 = "call  deleteph('Daulet')" 
cursor.execute(sql2) 
conn.commit() 
 
cursor.close() 
conn.close()