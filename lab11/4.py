import psycopg2 
 
conn = psycopg2.connect( 
    host="localhost", 
    database="phonebook", 
    user="user124", 
    password="3456753kk"
) 

cursor = conn.cursor() 

# sql7 = ''' 
#     create or replace function pagination(offset_ integer,limit_ integer) 
#     returns table 
#         ( 
#                     name varchar, 
#                     number  varchar 
#                 ) 
#     as 
#     $$ 
#     begin 
#         return query 
#             select ph.name,  ph.number  
#             from phonebook_2  as ph offset offset_ limit limit_; 
#     end 
#     $$ language plpgsql 
#     ''' 
# cursor.execute(sql7) 
# conn.commit() 
sql8 = "select * from pagination(1,2)" 

cursor.execute(sql8) 
results = cursor.fetchall() 
print(results) 
 
cursor.close() 
conn.close()