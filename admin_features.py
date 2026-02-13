from db_connection import db_conn_func
import pandas as pd
a= db_conn_func()
x=a.cursor()
def view_patient():
    print("\nYou want all patients data or few?")
    op=input("Enter All or Few : ")
    print("----------------------")
    if op.lower()=="all":
        query="select * from patients"
        df = pd.read_sql(query, a)
        print(df)
        # x.execute(query)
        # aaa=x.fetchall()
        # for i in aaa:
        #    print(i)
    elif op.lower()=="few":
        criteria1=int(input("Enter patient admission number : "))
        print("---------------------------------")
        query="select * from patients where admission_number=%s"
        df = pd.read_sql(query, a,params=(criteria1,))
        print(df)
        # x.execute(query,(criteria1,))
        # bbb=x.fetchall()
        # for i in bbb:
        #    print(i)

def update_berth():
    admission=int(input("Enter patient admission number : "))
    change=int(input("Enter patient new berth number : "))
    query="update patients set berth_number=%s where admission_number=%s"
    x.execute(query,(change,admission))
    a.commit()
    print("Berth number updated successfully...")

def delete_patient():
    admission=int(input("Enter Admission Number to remove patient : "))
    query="delete from patients where admission_number=%s"
    x.execute(query,(admission,))
    a.commit()
    print("Data removed successfully...")

def add_patient():
    p_name=input("Enter patient name : ")
    p_admno=int(input("Enter admission number : "))
    p_age=int(input("Enter patient age : "))
    p_gender=input("Enter patient gender (m/f) : ")
    p_berth=int(input("Enter patient berth number : "))
    p_guardian=input("Enter patient guardian name : ")
    total_fee=int(input("Enter total amount : "))
    amount_paid=int(input("Enter amount paid : "))

    query="insert into patients(admission_number,patient_name,patient_age,gender,berth_number,guardian_name,total_fee,amount_paid) " \
    "values(%s,%s,%s,%s,%s,%s,%s,%s)"
    x.execute(query,(p_admno,p_name,p_age,p_gender,p_berth,p_guardian,total_fee,amount_paid))
    berth_query="UPDATE berths SET is_occupied = TRUE WHERE berth_number=%s"
    x.execute(berth_query,(p_berth,))
    a.commit()
    print("Data uploaded successfully....")

def check_berth_availability():

    query = """
        SELECT b.berth_number,
        CASE 
            WHEN p.berth_number IS NOT NULL THEN 'Occupied'
            ELSE 'Available'
        END AS status
        FROM berths b
        LEFT JOIN patients p
        ON b.berth_number = p.berth_number
        ORDER BY b.berth_number;
    """
    x.execute(query)
    data = x.fetchall()

    print("\n--- Berth Status ---")
    for berth, status in data:
        print(f"Berth {berth}: {status}")

def fee_details():
    criteria=int(input("Enter Admission Number: "))
    query="select patient_name,total_fee,amount_paid,pending_fee from patients where admission_number=%s"
    x.execute(query,(criteria,))
    aaa=x.fetchall()
    if not aaa:
        print("No patient found.")
        return
    print("----------------------------")
    print("Patient Name-",aaa[0][0])
    print("Total Fee -",aaa[0][1])
    print("Amount Paid -",aaa[0][2])
    print("Pending Fee -",aaa[0][3])

