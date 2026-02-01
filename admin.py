from admin_features import add_patient,view_patient,update_berth,delete_patient,check_berth_availability,fee_details
def admin():
    print("\nChoose your option to proceed")
    print("-----------------------------")
    print("1.Add Patient")
    print("2.Check Berth Availability")
    print("3.View patient details")
    print("4.Update Berth")
    print("5.Delete Patient")
    print("6.Check Fee Details")

    op=int(input("Choose your option (1/2/3/4/5/6) :- "))
    if op==1:
        print("\n-----You are Adding Patient-----")
        add_patient()
    elif op==2:
        print("\nChecking Berth Availability...")
        check_berth_availability()
    elif op==3:
        print("\n----View Patient Details----")
        view_patient()
    elif op==4:
        print("\n-----Updating Berth-----")
        update_berth()
    elif op==5:
        print("\n-----Removing Patient-----")
        delete_patient()
    elif op==6:
        print("\n----Checking Fee Details----")
        fee_details()
