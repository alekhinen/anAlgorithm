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
from employee import Employee

# -----------------------------------------------------------------------------
# MAIN METHOD
# -----------------------------------------------------------------------------

# main()
def main():
  # parse and validate system arguments.
  inputFile, outputFile = parseArgs( sys.argv )
  # set employees, which employees are leaves, n, and k.
  employees, leafEmployees, n, k = readAndSetFromInput( inputFile )
  print 'done with reading the file'
  # for e in employees:
  #   if ( e ):
  #     print e.getInfluencePath(), '\n'
  # get the leaves from the employees list (using the leafEmployees list).
  leaves = getLeaves( employees, leafEmployees )
  print 'done with getting the leaves'

  # start the main loop
  results = []
  # getting the results
  while ( not k == 0 ):

    maxLeaf = employees[1]
    for leaf in leaves:
      leaf.setTotalUtility( computeTotalUtility( leaf, employees ) )
      # leafBoss = employees[ leaf.getBossID() ]
      # leaf.setTotalUtility( leaf.getUtility() + leafBoss.getTotalUtility() )
      if ( leaf.getTotalUtility() > maxLeaf.getTotalUtility() ):
        maxLeaf = leaf

    # print maxLeaf.getTotalUtility()
    results.append(maxLeaf.getTotalUtility())

    # setting everything in maxLeaf's path to 0 (just total utility).
    maxLeaf.setUtility( 0 )
    path = maxLeaf.getInfluencePath()
    for p in path:
      pathEmp = employees[ p ]
      pathEmp.setUtility( 0 )
      pathEmp.setTotalUtility( 0 )
    # path = maxLeaf.getBossID()
    # while ( not path == 0 ):
    #   pathEmp = employees[path]
    #   pathEmp.setUtility( 0 )
    #   pathEmp.setTotalUtility( 0 )
    #   path = employees[path].getBossID()

    # remove maxLeaf from leaves
    leaves.remove( maxLeaf )
    # decrement k
    k -= 1

  sumResult = 0
  for r in results:
    sumResult += r

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
      sys.exit(2)
  else:
    print 'ERROR: Improper input. Please supply one input file and one output.'
    sys.exit(1)

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
  # boolean if employee at index is a leaf
  leafEmployees = []

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
      # set the total utility and influence path
      if ( not bossid == 0 ):
        # setting the total utility.
        curEmp.setTotalUtility( utility + employees[bossid].getTotalUtility() )
        leafEmployees[ bossid ] = False
        # setting the influence path.
        curEmp.appendToInfluence( employees[ bossid ].getInfluencePath() )
      else:
        curEmp.setTotalUtility( utility )
      employees[ uid ] = curEmp

    i += 1

  return employees, leafEmployees, n, k

# -----------------------------------------------------------------------------
# MAIN LOOP HELPER METHODS
# -----------------------------------------------------------------------------

# getLeaves()
def getLeaves( emps, leafEmps ):
  result = []
  empsLen = len(emps)
  leafEmpsLen = len(leafEmps)

  i = 0
  while ( i < empsLen and i < leafEmpsLen ):
    if ( leafEmps[ i ] and not i == 0 ):
      result.append( emps[ i ] )
    i += 1

  return result

# computeTotalUtility()
def computeTotalUtility( leaf, employees ):
  result = leaf.getUtility()

  path = leaf.getBossID()
  while ( not path == 0 ):
    pathEmp = employees[path]
    if ( pathEmp.getUtility() == 0 ):
      break
    else:
      result += pathEmp.getUtility()
      path = pathEmp.getBossID()

  return result

# -----------------------------------------------------------------------------
# EXECUTION
# -----------------------------------------------------------------------------

# execute the main method (if it's not being imported by another module)
if __name__ == '__main__':
  # this program is being run by itself
  main()