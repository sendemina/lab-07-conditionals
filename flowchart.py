move = input("Does it move? (yes/no) ")
if (move == "yes"):
   should = input("Should it? (yes/no) ")
   if (should == "yes"):
    print("No problem")
   elif (should == "no"):
    print("Then use duct tape!")
   else:
    print("You didn't answer my question! Type yes or no.")
elif (move == "no"):
   should = input("Should it? (yes/no) ")
   if (should == "yes"):
    print("Then use the mysterious bottle!")
   elif (should == "no"):
    print("No problem")
   else:
    print("You didn't answer my question! Type yes or no.")
else:
  print("You didn't answer my question! Type yes or no.")
