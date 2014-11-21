# sol
# @module: Employee
# @description: an Employee class structure
# @author: Nick Alekhine
# @version: 15-11-2014

class Employee: 
    
  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  uID     = 0
  bossID  = 0
  utility = 0
  totalUtility = 0
  highestChild = 0
  influencePath = []
  children = []

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  def __init__( self, uID, bossID, utility ):
    self.uID = uID
    self.bossID = bossID
    self.utility = utility
    self.highestChild = 0
    self.children = []

    if ( not bossID == 0 ):
      self.influencePath = [bossID]
    else:
      self.influencePath = []

  # cmp()
  # @param: other - another instance of Employee
  # @description: compares this and another employee by looking at the 
  #               length of their influence path (the shorter the better)
  # @returns: number (1, 0, or -1)
  def __cmp__( self, other ):
    return cmp( len( self.influencePath ), len( other.influencePath ) )

  # -------------
  # -  GETTERS  -
  # -------------

  # getID()
  # @description: gets the unique id
  # @returns: number
  def getID( self ):
    return self.uID

  # getBossID()
  # @description: gets the boss' unique id
  # @returns: number
  def getBossID( self ):
    return self.bossID

  # getUtility()
  # @description: gets the utility value
  # @returns: number
  def getUtility( self ):
    return self.utility

  # getTotalUtility()
  # @description: gets the total utility starting from this
  #               (total utility is the sum of the utility from infl. path)
  # @returns: number
  def getTotalUtility( self ):
    return self.totalUtility

  # getHighestChild()
  # @description: gets the highest child of this employee (unique id)
  # @returns: number
  def getHighestChild( self ):
    return self.highestChild

  # getInfluencePath()
  # @description: gets the list of employees that this employee can influence.
  # @returns: list of number
  def getInfluencePath( self ):
    return self.influencePath

  # getChildren()
  # @description: gets the children of this employee
  # @returns: list of number
  def getChildren( self ):
    return self.children

  # -------------
  # -  SETTERS  -
  # -------------

  # setTotalUtility()
  # @param: n - number
  # @description: sets the utility
  # @returns: void
  def setUtility( self, n ):
    self.utility = n

  # setTotalUtility()
  # @param: n - number
  # @description: sets the total utility 
  # @returns: void
  def setTotalUtility( self, n ):
    self.totalUtility = n

  # setHighestChild()
  # @param: c - number (corresponding to unique id)
  # @description: sets the highest child
  # @returns: void
  def setHighestChild( self, c ):
    self.highestChild = c

  # setInfluencePath()
  # @param: path - list of number
  # @description: sets the influence path
  # @returns: void
  def setInfluencePath( self, path ):
    self.influencePath = path

  # appendToInfluence()
  # @param: path - list of number OR number
  # @description: appends to the influence path
  # @returns: void
  def appendToInfluence( self, path ):
    if ( type(path) is list ):
      self.influencePath.extend( path )
    else:
      self.influencePath.append( path )

  # appendChild()
  # @param: child - number
  # @description: appends to the list of children
  # @returns: void
  def appendChild( self, child ):
    self.children.append( child )

  # removeChild()
  # @param: child - number
  # @description: remove a child from the list (if they exist)
  # @returns: void
  def removeChild( self, child ):
    self.children.remove( child )

