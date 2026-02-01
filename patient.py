from patient_features import adm_number,pending_fee,berth_assigned
def patient():
    print("Choose options below: ")
    print("1.Get Admission Number")
    print("2.Check assigned berth ")
    print("3.Check Pending Fee & Pay")
    op=int(input("\nEnter option (1/2/3) : "))
    if op==1:
        print("\n---Getting Admission Number---")
        adm_number()
    elif op==2:
        print("\n----Getting Berth Number----")
        berth_assigned()
    elif op==3:
        print("\n---Getting pending fee details---")
        pending_fee()
        
