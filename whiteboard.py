# ---------- Counting Sheep... ----------
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# EXPLANATION:
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like None.
# EXAMPLES:
# counting_sheep([]), --> 0
# counting_sheep([True, True, None, True, None, False]) --> 3
# counting_sheep([False, False, False, None, None, None]) --> 0

def sheepPresent(alist):
    present = 0
    for sheep in alist:
        if sheep == True:
            present += 1
    return present

print(sheepPresent([False, False, False, None, None, None]))
            
    