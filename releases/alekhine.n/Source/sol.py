#!/usr/bin/env python
# sol
# @description: An algorithm that maximizes the total utility
#               of influencing people in a company hierarchy.
# @author: Nick Alekhine
# @version: 15-11-2014

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import sys
import heapq
import bisect
from employee import Employee

# -----------------------------------------------------------------------------
# MAIN METHOD
# -----------------------------------------------------------------------------

# main()
def main():
  # parse and validate system arguments.
  # inputFile, outputFile = parseArgs( sys.argv )
  # set employees, n, and k.
  employeesPQ, n, k = readAndSetFromInput()

  # employees is a list of employees (index == employee id)
  employees = []
  for e in employeesPQ:
    employees.append( e )

  # remove the 0th employee
  employeesPQ.pop(0)
  # heapify the employees priority queue
  heapq.heapify( employeesPQ )

  # get all the total utilities (sorted by total utility ascending)
  result = getAllTotalUtilities( employeesPQ, employees )

  # get the top k total utilities
  i = len(result) - 1
  sumResult = 0
  while ( k > 0 ):
    sumResult += result[i]
    i = i - 1
    k = k - 1

  # write the result
  sys.stdout.write( str(sumResult) + '\n' )

# getAllTotalUtilities()
# @param: employeesPQ - a priority queue of employees
# @param: employees - a list structure of employees
# @description: adds the total utility of the highest child of every employee
#               to a sorted list.
# @returns: list of numbers (sorted)
def getAllTotalUtilities( employeesPQ, employees ):
  result = []

  # while there are employees in the priority queue:
  while employeesPQ:
    # pop the top element
    e = heapq.heappop( employeesPQ ) 
    eID = e.getID()

    # if the top element has already been used, find the next biggest
    while ( not employees[ eID ] and employeesPQ ):
      e = heapq.heappop( employeesPQ )
      eID = e.getID()

    # get the highest child of the top element
    highestChild = e.getHighestChild()
    hC = employees[ highestChild ]
    
    # if the highest child exists
    if ( hC ):
      # add highest child's utility to the subresult
      subResult = hC.getUtility()

      # add each element's utility in path to the subresult.
      # remove all elements from highest child's path 
      # (by setting them to false).
      path = hC.getInfluencePath()
      for p in path:
        curEmp = employees[ p ]
        if ( curEmp ):
          subResult += curEmp.getUtility()
        employees[ p ] = False

      # sorted insert into result
      bisect.insort( result, subResult )

    # else if the top element has no children, just add itself to the result
    elif ( highestChild == 0 ):
      bisect.insort( result, e.getUtility() )

    # remove highest child and top element from employees.
    employees[ highestChild ] = False
    employees[ eID ] = False

  return result

# -----------------------------------------------------------------------------
# PRE-COMPUTATION METHODS
# -----------------------------------------------------------------------------

# parseArgs()
# @description: reads and sets a bunch of stuff
# @param: inputFile - a string filepath to the input file
# @returns: employees [list of employees]
#           n (number of employees)
#           k (amount of employees the algo can use)
# @author: Nick Alekhine
# @version: 16-11-2014 (DD-MM-YYYY)
def readAndSetFromInput():
  # setting up the basics
  i = 0
  n = 0
  k = 0
  # the employees
  employees = []

  # read the lines from the input file
  for line in sys.stdin:
    spline = line.split()
    # if we're at the first line, read the n val and the k val
    if ( i == 0 ):
      n = int( spline[0] )
      k = int( spline[1] )
      employees = [False] * (n + 1)
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
        # setting the highest child for everyone in the influence path.
        infPath = curEmp.getInfluencePath()
        for e in infPath:
          hC = employees[ e ].getHighestChild()
          # if there's no highest child, set it to the current employee.
          if ( hC == 0 ):
            employees[ e ].setHighestChild( curEmp.getID() )
          # else if the current highest child has a lesser value than the
          # current employee, set the employee's highest child to the current
          # employee.
          elif ( employees[ hC ].getTotalUtility() < curEmp.getTotalUtility() ):
            employees[ e ].setHighestChild( curEmp.getID() )
      # else we're at the CEO, set the total utility to be the utility.
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
