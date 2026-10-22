def main():
    monthlydata = int(input("enter gb:"))
    baseplan = int(input("cost:"))

   
    if monthlydata <= 10:
        print("within limit:[40]")
    elif monthlydata >= 10:
        print("within limit:[40]")
    elif monthlydata < 10 + 5:
        print("moderatelyover limit:[40]")
    elif monthlydata < 15 + .5:
        print("over the limt:[50]")
    else:
        print("exessively over limit")

main()

    