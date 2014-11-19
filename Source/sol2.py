# sol
# @description: An algorithm that maximizes the total utility
#               of influencing people in a company hierarchy.
# @author: Nick Alekhine
# @version: 15-11-2014

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import fileinput
import sys
import os.path
import heapq
import bisect
from employee import Employee

# -----------------------------------------------------------------------------
# MAIN METHOD
# -----------------------------------------------------------------------------

# main()
def main():
  # parse and validate system arguments.
  inputFile, outputFile = parseArgs( sys.argv )
  # set employees, which employees are leaves, n, and k.
  employees, n, k = readAndSetFromInput( inputFile )
  print 'done with reading the file'
  
  oEmployees = []
  for e in employees:
    oEmployees.append( e )

  employees.pop(0)
  heapq.heapify( employees )
  print 'done with heapifying the employees'

  result = []
  # while employees and k > 0:
  while employees:
    # get the top element
    e = heapq.heappop( employees ) 
    eID = e.getID()
    # if the top element has already been used, find the next biggest
    while ( not oEmployees[ eID ] and employees ):
      e = heapq.heappop( employees )
      eID = e.getID()
    # print eID
    # get the highest child of the top element
    highestChild = e.getHighestChild()
    hC = oEmployees[ highestChild ]
    
    # if the highest child exists
    if ( hC ):
      # add highest child's utility result
      subResult = hC.getUtility()

      # add each element's utility in path to result.
      # remove all elements from highest child's path.
      path = hC.getInfluencePath()
      for p in path:
        curEmp = oEmployees[ p ]
        if ( curEmp ):
          subResult += curEmp.getUtility()
        oEmployees[ p ] = False

      # sorted insert into result
      bisect.insort( result, subResult )

      # decrement k
      # k = k - 1

    # else if the top element has no children, just add itself to the result
    elif ( highestChild == 0 ):
      bisect.insort( result, e.getUtility() )
      # k = k - 1

    # remove highest child and top element from oEmployees.
    oEmployees[ highestChild ] = False
    oEmployees[ eID ] = False

  i = len(result) - 1
  sumResult = 0
  while ( k > 0 ):
    sumResult += result[i]
    i = i - 1
    k = k - 1


  print sumResult

# -----------------------------------------------------------------------------
# PRE-COMPUTATION METHODS
# -----------------------------------------------------------------------------

# parseArgs()
# @description: parses system arguments from command-line
# @param: sysArgs - an array of system arguments
# @returns: two strings corresponding to the input file and output file.
# @author: Nick Alekhine
# @version: 15-11-2014 (DD-MM-YYYY)
def parseArgs( sysArgs ):
  if ( len(sysArgs) == 3 ):
    inputFile = sysArgs[1]
    outputFile = sysArgs[2]
    if ( not os.path.exists( inputFile ) ):
      print 'ERROR: input file does not exist. aborting.'
      sys.exit(1)
  else:
    print 'ERROR: Improper input. Please supply one input file and one output.'
    sys.exit(2)

  return inputFile, outputFile

# parseArgs()
# @description: reads and sets a bunch of stuff
# @param: inputFile - a string filepath to the input file
# @returns: employees [list of employees]
#           leafEmployees [list of boolean] (corresponds to employee id)
#           n (number of employees)
#           k (amount of employees the algo can use)
# @author: Nick Alekhine
# @version: 16-11-2014 (DD-MM-YYYY)
def readAndSetFromInput( inputFile ):
  # setting up the basics
  i = 0
  n = 0
  k = 0
  # the employees
  employees = []

  # read the lines from the input file
  for line in fileinput.input( inputFile ):
    spline = line.split()
    # if we're at the first line, read the n val and the k val
    if ( i == 0 ):
      n = int( spline[0] )
      k = int( spline[1] )
      employees = [False] * (n + 1)
      leafEmployees = [True] * (n + 1)
    # start setting the employees
    else:
      uid     = int( spline[0] )
      bossid  = int( spline[1] )
      utility = int( spline[2] )
      # init employee
      curEmp = Employee( uid, bossid, utility )
      # set the total utility, influence path, and children.
      if ( not bossid == 0 ):
        # setting the total utility.
        curEmp.setTotalUtility( utility + employees[bossid].getTotalUtility() )
        # setting the influence path.
        curEmp.appendToInfluence( employees[ bossid ].getInfluencePath() )
        # add this employee to the boss' children
        employees[ bossid ].appendChild( uid )

        # setting the highest child for everything in the influence path.
        infPath = curEmp.getInfluencePath()
        for e in infPath:
          hC = employees[ e ].getHighestChild()
          if ( hC == 0 ):
            employees[ e ].setHighestChild( curEmp.getID() )
          else:
            if ( employees[ hC ].getTotalUtility() < curEmp.getTotalUtility() ):
              employees[ e ].setHighestChild( curEmp.getID() )
      else:
        curEmp.setTotalUtility( utility )
      employees[ uid ] = curEmp

    i += 1

  return employees, n, k

# -----------------------------------------------------------------------------
# EXECUTION
# -----------------------------------------------------------------------------

# execute the main method (if it's not being imported by another module)
if __name__ == '__main__':
  # this program is being run by itself
  main()