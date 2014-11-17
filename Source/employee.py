
# Employee
class Employee: 
    
  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  uID     = 0
  bossID  = 0
  utility = 0
  totalUtility = 0
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
    else:
      self.influencePath = []
      self.children = []

  def getID( self ):
    return self.uID

  def getBossID( self ):
    return self.bossID

  def getUtility( self ):
    return self.utility

  def getTotalUtility( self ):
    return self.totalUtility

  def getInfluencePath( self ):
    return self.influencePath

  def getChildren( self ):
    return self.children

  def setTotalUtility( self, n ):
    self.totalUtility = n

  def setUtility( self, n ):
    self.utility = n

  def appendToInfluence( self, path ):
    if ( type(path) is list ):
      self.influencePath.extend( path )
    else:
      self.influencePath.append( path )

  def appendChild( self, child ):
    self.children.append( child )

