from enum import Enum

class Color(Enum):
    EMPTY = 0 
    YELLOW = 1
    GREEN = 2
    BLUE = 3
    RED = 4

class  Mission(Enum):
    EMPTY = 0
    SQUARE = 1
    STAR = 2
    TRIANGLE = 3
    CIRCLE = 4

ASSET_MAP = {
     (Color.EMPTY, Mission.EMPTY): "empty",
     (Color.YELLOW, Mission.EMPTY): "../Asset/yellow_robot.png",
     (Color.YELLOW, Mission.SQUARE): "../Asset/yellow_square_mission.png",
     (Color.YELLOW, Mission.STAR): "../Asset/yellow_star_mission.png",
     (Color.YELLOW, Mission.TRIANGLE): "../Asset/yellow_triangle_mission.png",
     (Color.YELLOW, Mission.CIRCLE): "../Asset/yellow_circle_mission.png",
     (Color.RED, Mission.EMPTY): "../Asset/red_robot.png",
     (Color.RED, Mission.SQUARE): "../Asset/red_square_mission.png",
     (Color.RED, Mission.STAR): "../Asset/red_star_mission.png",
     (Color.RED, Mission.TRIANGLE): "../Asset/red_triangle_mission.png",
     (Color.RED, Mission.CIRCLE): "../Asset/red_circle_mission.png",
     (Color.GREEN, Mission.EMPTY): "../Asset/green_robot.png",
     (Color.GREEN, Mission.SQUARE): "../Asset/green_square_mission.png",
     (Color.GREEN, Mission.STAR): "../Asset/green_star_mission.png",
     (Color.GREEN, Mission.TRIANGLE): "../Asset/green_triangle_mission.png",
     (Color.GREEN, Mission.CIRCLE): "../Asset/green_circle_mission.png",
     (Color.BLUE, Mission.EMPTY): "../Asset/blue_robot.png",
     (Color.BLUE, Mission.SQUARE): "../Asset/blue_square_mission.png",
     (Color.BLUE, Mission.STAR): "../Asset/blue_star_mission.png",
     (Color.BLUE, Mission.TRIANGLE): "../Asset/blue_triangle_mission.png",
     (Color.BLUE, Mission.CIRCLE): "../Asset/blue_circle_mission.png",
 }
class Player_Mission(object):
    def __init__(self,_color = Color(0),_mission=Mission(0),_i = 0 ,_j= 0):
        self.color = _color
        self.mission = _mission
        self.coordinate = (_j,_i)
        self.update_asset()

    def set_color(self, new_color):
        self.color = new_color
        self.update_asset()

    def set_mission(self, new_mission):
        self.mission = new_mission
        self.update_asset()

    def update_asset(self):
        self.asset = ASSET_MAP.get((self.color, self.mission),"empty")

