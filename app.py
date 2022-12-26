def textGame():
  print('''
  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

      88                                                     
      88                                                     
      88                                                     
      88,dPPYba,   ,adPPYba,  88,dPYba,,adPYba,   ,adPPYba,  
      88P'    "8a a8"     "8a 88P'   "88"    "8a a8P_____88  
      88       88 8b       d8 88      88      88 8PP"""""""  
      88       88 "8a,   ,a8" 88      88      88 "8b,   ,aa  
      88       88  `"YbbdP"'  88      88      88  `"Ybbd8"'  

  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  ''')

  print("Please help me find my way home")

  stepOne = input("Do I turn left or right?\n").lower()

  stepOneCorrect = 'right'
  stepTwoCorrect = 'left'
  stepThreeCorrect = 'left'
  
  def retryGame():
    retry = input("Do you want to try again? yes or no\n").lower()
    retryTrue = 'yes'
    if retry == retryTrue:
      textGame()
    else:
        print("Thank you for playing")

  if stepOne == stepOneCorrect:
    print("You turn right and see an intersection that you walk towards")
    stepTwo = input("Now I am at an intersection, should I cross the street on the right or the left?\n").lower()
    if stepTwo == stepTwoCorrect:
      print("You cross the intersection on the left")
      stepThree = input ("I crossed the street and there are two doors. Do I go into the left door or the right door?\n").lower()
      if stepThree == stepThreeCorrect:
        print("You go into the door on the left and find yourself back at your home. Congratulations")
        retryGame()
      elif stepThree != stepThreeCorrect:
        print("You go into the door on the right and realize this is not your home")
        retryGame()
    elif stepTwo != stepTwoCorrect:
      print("You cross the intersection on the right and are hit by a car")
      retryGame()
  elif stepOne != stepOneCorrect:
    print("You turn left and fall in a hole")
    retryGame()

textGame()
