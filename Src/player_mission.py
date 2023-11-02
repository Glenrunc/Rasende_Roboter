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

class Player(object):
    def __init__(self,_color = Color(0),_i = 0 ,_j= 0):
        self.color = _color
        self.coordinate = (_j,_i)
        self.update_asset()

    def set_color(self, new_color):
        self.color = new_color
        self.update_asset()

    def update_asset(self):
        self.asset = ASSET_MAP.get((self.color, Mission.EMPTY),"empty")

mission_tab = []

# Add RED
mission_tab.append((13,14,Color.RED,Mission.SQUARE))
mission_tab.append((5,7,Color.RED,Mission.TRIANGLE))
mission_tab.append((4,14,Color.RED,Mission.CIRCLE))
mission_tab.append((13,1,Color.RED,Mission.STAR))

# Add YELLOW
mission_tab.append((6,1,Color.YELLOW,Mission.SQUARE))
mission_tab.append((9,4,Color.YELLOW,Mission.TRIANGLE))
mission_tab.append((11,9,Color.YELLOW,Mission.CIRCLE))
mission_tab.append((6,12,Color.YELLOW,Mission.STAR))

# Add BLUE
mission_tab.append((3,9,Color.BLUE,Mission.SQUARE))
mission_tab.append((9,13,Color.BLUE,Mission.TRIANGLE))
mission_tab.append((10,6,Color.BLUE,Mission.CIRCLE))
mission_tab.append((2,5,Color.BLUE,Mission.STAR))

# Add GREEN
mission_tab.append((15,3,Color.GREEN,Mission.SQUARE))
mission_tab.append((1,13,Color.GREEN,Mission.TRIANGLE))
mission_tab.append((4,2,Color.GREEN,Mission.CIRCLE))
mission_tab.append((14,10,Color.GREEN,Mission.STAR))