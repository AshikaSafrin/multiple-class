class elegibilityForMarriage():
    def Elegible():
        name=input("Your gender:")
        age=int(input("your age:"))
        if(age<=18):
            print("not eligible")
            marriage="not eligible"
            return marriage
        else:
            print("eligible")
            marriage="eligible"
            return marriage