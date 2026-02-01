from admin import admin
from patient import patient
from db_connection import db_conn_func

print("\n1.Admin")
print("2.Patient")
op=int(input("Choose option (1/2) :- "))
if op==1:
    print("\n---Welcome to Admin Panel---")
    admin()
elif op==2:
    print("\n---Welcome to user panel---")
    patient()
