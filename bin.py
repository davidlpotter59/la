
numbToConvert = int(input("Enter your number: "))
remainingNumb = numbToConvert
remainingNumbMod = remainingNumb
print(numbToConvert)
binList = []
while remainingNumbMod:
    if remainingNumb:
        remainingNumb = numbToConvert // 2
        remainingNumbMod = numbToConvert % 2
        numbToConvert = remainingNumb
        binList += str(remainingNumbMod)
    else:
        remainingNumbMod = False

    print("*"*70)
    print(binList)
    print(remainingNumb)
    print(remainingNumbMod)
    print("*"*70)
    
    # break 
    