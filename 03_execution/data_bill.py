def exceed_allowance(data_gb):
    return data_gb > 10

def main():
    Monthlydata = float(input("enter data used (gb): "))
    Baseplan = float(input("enter the base plan cost: "))

    if exceed_allowance(Monthlydata):
        overage = Monthlydata - 10
        print(f"you are{overage:.1f}gb over the limit ")

        if overage <= 5:
            print("Moderate extra usage ")
        
        else:
            print("high extra usage")
          
        Total = Baseplan + overage * 2

    else:
        print("within data limit ")
        Total = Baseplan
       
    print(f"total bill is: ${Total:.2f}")

    
main()
    



    



    