
''''Continue statement: bhai jase hi ye statement aatai h, loop wapas se uper chale jata h  '''



a=0
while a<=5:
    a=a+1              # step 1> a=1                        # step 2>  a=2                                                       # step 3>a=3
    if a%2==0:         # 1%2!=0 false ,skip if wala scope   # 2%2==0  true go inside if                                          # false
        continue                                            # dekh bhai ab continue statement h isliye uper bhag step 3 ke liye
    print(a)           # print 1 ab step 2 ke liye uper bhag                                                                     # print 3 or feer se up-er jao ab step 4 ke liye
print("end of loop")
