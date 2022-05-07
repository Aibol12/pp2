import psycopg2 
 
conn = psycopg2.connect( 
    host="localhost", 
    database="phonebook", 
    user="user124", 
    password="3456753kk"
) 

cursor = conn.cursor() 

sql = ''' 
    create or replace function getAll() 
        returns table 
            ( 
                name varchar, 
                surname varchar, 
                number  varchar 
            ) 
    as 
    $$ 
    begin 
        return query 
            select ph.name, ph.surname, ph.number 
            from phonebook  as ph; 
    end 
    $$ language plpgsql 
    ''' 
cursor.execute(sql) 
conn.commit() 

sql2 = "select * from getAll()" 
cursor.execute(sql2) 
get_all = cursor.fetchall() 
print(get_all) 

cursor.close() 
conn.close()