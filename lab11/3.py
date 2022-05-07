import psycopg2 
 
conn = psycopg2.connect( 
    host="localhost", 
    database="phonebook", 
    user="user124", 
    password="3456753kk"
) 

cursor = conn.cursor()

# sql = ''' 
#     create or replace procedure task3(list varchar[][] ,size integer) as 
#     $$ 
#     begin 
#     for i in 1..size loop 
#     if (list[i][2] like '%7777%') then 
#     insert into phonebook_2(name,number) 
#     values (list[i][1], list[i][2]); 
#     end if; 
#     end loop; 
#     end; 
#     $$ 
#     language plpgsql 
#     ''' 
# cursor.execute(sql) 
# conn.commit() 
sql2 = "call task3 ('{ {'Bbn', '87083907226'}, {'ak', '87077779221'} }', 2)" 
cursor.execute(sql2) 
conn.commit() 


cursor.close() 
conn.close()