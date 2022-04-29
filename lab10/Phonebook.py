import psycopg2

connection = psycopg2.connect(dbname='postgres', user='user124', password='3456753kkk', host='localhost')
cursor = connection .cursor()
tname="ph_b"
cursor.execute("CREATE TABLE IF NOT EXISTS "+tname+"(name text, number text)")
run=True
print("for ADDING new contact enter 'add name_of_contact number_of_contact'")
print("for UPDATING contact enter 'up name_of_contact new_number'")
print("for SHOWING the phone number list enter 'sh'")
print("for EXIT enter 'ex'")

def insert(name, num):
    cursor.execute("INSERT INTO "+tname+" VALUES ('"+name+"' , '"+num+"')")

def update(name, newnum):
    cursor.execute("SELECT name FROM "+tname+" WHERE EXISTS (SELECT name FROM "+tname+" WHERE name = '"+name+"')")
    f=cursor.fetchall()
    #print(f)
    if f:
        if f[0][0]==name:
            cursor.execute("UPDATE "+tname+" SET number = '"+newnum+"' WHERE name = '"+name+"'")
        else:
            insert(name , newnum)
    else:
        insert(name , newnum)
def delete(name):
    cursor.execute("DELETE FROM "+tname+" WHERE name = '"+name+"'")
def show():
    cursor.execute("SELECT * FROM "+tname+" ")
    print("****")
    for i in cursor.fetchall():
        print(str(i[0])+" "+str(i[1]))
        print("_____")
        print(" ")
    print("****")

while run:
    n=input()
    gg=n.split()
    if gg[0]=="add":
        update(gg[1], gg[2])
    elif gg[0]=="up":
        update(gg[1],gg[2])
    elif gg[0]=="sh":
        show()
    elif gg[0]=="ex":
        cursor.execute("COMMIT")
        run=False
    elif gg[0] == "del":
        delete(gg[1]