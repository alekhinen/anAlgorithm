
# Employee
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
    self.uID      = uID
    self.bossID   = bossID
    self.utility  = utility
    if ( not bossID == 0 ):
      self.influencePath = [bossID]
      self.children = []
      self.highestChild = 0
    else:
      self.influencePath = []
      self.children = []
      self.highestChild = 0

  def __cmp__( self, other ):
    return cmp( len( self.influencePath ), len( other.influencePath ) )

  def getID( self ):
    return self.uID

  def getBossID( self ):
    return self.bossID

  def getUtility( self ):
    return self.utility

  def getTotalUtility( self ):
    return self.totalUtility

  def getHighestChild( self ):
    return self.highestChild

  def getInfluencePath( self ):
    return self.influencePath

  def getChildren( self ):
    return self.children

  def setTotalUtility( self, n ):
    self.totalUtility = n

  def setUtility( self, n ):
    self.utility = n

  def setHighestChild( self, c ):
    self.highestChild = c

  def setInfluencePath( self, path ):
    self.influencePath = path

  def appendToInfluence( self, path ):
    if ( type(path) is list ):
      self.influencePath.extend( path )
    else:
      self.influencePath.append( path )

  def appendChild( self, child ):
    self.children.append( child )

  def removeChild( self, child ):
    self.children.remove( child )

