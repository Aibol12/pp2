import psycopg2 
 
conn = psycopg2.connect( 
    host="localhost", 
    database="phonebook", 
    user="user124", 
    password="3456753kk"
) 

cursor = conn.cursor() 

# sql3 = ''' 
#     create procedure addph(name_ varchar,number_ varchar) 
#     as 
#     $$ 
#     begin 
#         if  exists(select * from phonebook_2 where name = name_) then 
#           update phonebook_2 set number = number_ where name = name_; 
#         else  
#           insert into phonebook_2(name,number) values (name_, number_); 
#         end if; 
#     end; 
#     $$ 
#     LANGUAGE plpgsql 
#     ''' 
# cursor.execute(sql3) 
# conn.commit() 

# It's a procedure for new user
# sql4 = "call addph('Aan', '87086563625')" 
# cursor.execute(sql4) 
# conn.commit()

#It's a procedure for existing user

sql5 = "call addph('Aan', '87080000001')"
cursor.execute(sql5) 
conn.commit()

cursor.close() 
conn.close()