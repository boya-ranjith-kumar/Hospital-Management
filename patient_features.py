from db_connection import db_conn_func
SQ=db_conn_func()
crobj=SQ.cursor()
def adm_number():
    criteria=input("\nEnter patient name : ")
    query="SELECT admission_number,patient_name FROM patients WHERE patient_name LIKE %s"
    crobj.execute(query,("%"+criteria+"%",))
    aaa=crobj.fetchall()
    print("-----------------------------")
    print("Admission Number-",aaa[0][0])
    print("Patient Name -",aaa[0][1])

def pending_fee():
    enter=int(input("Enter Admission number to check pending fee : "))
    crobj.execute("select pending_fee from patients where admission_number=%s",(enter,))
    bbb=crobj.fetchall()
    var1=0
    for i in bbb:
        for j in i:
            var1+=j
            print("Pending Fee :",j)
    
    if var1!=0:
        print("\nYou want to pay Pending Fee ?")
        print("-----------------------------")
        op=input("Enter Yes/No :")
        if op=="yes":
            criteria1=int(input("Enter amount you want to pay : "))
            criteria2=int(input("Enter patient admission number : "))
            query="update patients set amount_paid=amount_paid+%s where admission_number=%s"
            crobj.execute(query,(criteria1,criteria2))
            SQ.commit()
            print("Fee paid successfully..")
        elif op=="no":
            print("Pay as early as possible, Thank you!")
            
def berth_assigned():
    criteria=input("\nEnter patient name :")
    crobj.execute("select patient_name,berth_number from patients where patient_name like %s",(criteria,))
    ccc=crobj.fetchall()
    print("-------------------------")
    print("Patient Name-",ccc[0][0])
    print("Berth Number-",ccc[0][1])