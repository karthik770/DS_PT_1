# if expression1:
#    statement(s)
#    if expression2:
#       statement(s)
#    elif expression3:
#       statement(s)
#    elif expression4:
#       statement(s)
#    else:
#       statement(s)
# else:
#    statement(s)

var = 200
if (var <= 200):
   print ("Value is less than 200")
   if var == 150:
      print ("Which is 150")
   elif var == 100:
      print ("Which is 100")
   elif var == 50:
      print ("Which is 50")
   elif var < 50:
      print ("Value is less than 50")
else:
   print ("Gretaer than 200")
