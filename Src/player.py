
class Player(object):
    def __init__(self,_color = "empty",_x = 0 ,_y = 0,_asset = "empty"):
        self.color = _color
        self.coordinate = (_y,_x)
        self.asset = _asset 
    