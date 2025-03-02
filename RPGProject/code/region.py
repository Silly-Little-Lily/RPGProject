## Region Class

class Region:

  def __init__(self,Id,BackgroundMusic,BaseMap,TopMap,DisplayName):
    self.Id = Id
    self.BackgroundMusic = BackgroundMusic
    self.BaseMap = BaseMap
    self.TopMap = TopMap
    self.DisplayName = DisplayName

def Default():
  return Region(1,None,[[],[]],[[],[]],"Display Name")
