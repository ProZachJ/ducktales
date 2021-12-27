#!/usr/bin/python3
## Written by Robert "RSnake" Hansen to fix the nanissue for Python
## It makes certain primatives like addition, subtraction, etc. available
## so that one can safely perform operations on ints and floats without 
## producing NaN and inf inadvertantly, or doing unsafe operations on 
## them. 
##
## Whereerver you see "safe" if it is True it will crash as opposed to 
## continuing as safely as it can while throwing an error.

## Identifies the presence of NaN by asking if the variable equals itself
def identify_nan(variable):
  try:
    if float(variable) == float(variable):
      return 0
    else:
      return 1
  except:
    return 0
 
## Identifies the presence of an inf or negative inf by adding a float and seeing if it equals itself
def identify_inf(variable):
  try:
    if float(variable) + 1 != float(variable):
      return 0
    else:
      return 1
  except:
    return 0
 
## Attempts to see if variable is either an inf -inf or NaN
def test_var_safety(test_variable, returntype, safe):
  try:
    if returntype == 'float':
      return_var = float(test_variable)
    else:
      float(test_variable)
      return_var = test_variable
  except:
    if safe:
      raise RuntimeError ("Variable cannot safely be converted to float.")

  error = 0
  if identify_nan(return_var):
    if safe:
      raise RuntimeError ("Encountered a NaN in safe mode.")
    else:
      error = 1

  if identify_inf(return_var):
    if safe:
      raise RuntimeError ("Encountered an inf in safe mode.")
    else:
      error = 1

  return return_var, error

## Safely allows the user to sum two or more integers/floats together in a list
def safely_sum (thelist, safe):
  testsum = 0
  for thisvar in thelist:
    testsum = testsum + thisvar
  return test_var_safety(testsum, type(testsum), safe)

## Safely allows the user to subtract two or more integers/floats together in a list
def safely_subtract (thelist, safe):
  testsum = 0
  for thisvar in thelist:
    testsum = testsum - thisvar
  return test_var_safety(testsum, type(testsum), safe)

## Safely allows the user to average two or more integers/floats together in a list
def safely_average (thelist, safe):
  sum, error = safely_sum(thelist, safe)
  return sum/len(thelist), error

## Safely allows the user to multiply two integers/floats together in a list
def safely_multiply (first, second, safe):
  testsum = first * second
  return test_var_safety(testsum, type(testsum), safe)

## Safely allows the user to divide two integers/floats together 
def safely_divide (first, second, safe):
  test = 0
  try:
    test = first / second
  except:
    if safe:
      raise RuntimeError ("Non float/integer found in safe mode.")
    else:
      return 0, 1

  if type(test) is float:
    returnvar, error = test_var_safety(test, 'float', safe)
  else:
    returnvar, error = test_var_safety(test, 'int', safe)

  return returnvar, error


## Some examples:
# asdf = 'inf'
# returnvar, error = test_var_safety(asdf, 'float', True)
#
# asdf = [123, float('Nan'), 4]
# returnvar, error = safely_average(asdf, True)
#
# returnvar, error = safely_divide(3e3333, 1, True)
# print (returnvar)
# print (error)
