from road import Road


class Simulator:
    def __init__(self):
        self.frame_count = None
        self.t = None
        self.dt = None
        self.roads = None

    def __int__(self, config={}):
        self.set_default_config()

        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0

        self.frame_count = 0

        self.dt = 1 / 60

        self.roads = []

    def createRoad(self, start, end):
        the_road = Road(start, end)
        self.roads.append(the_road)
        return the_road

    def createRoad(self, roadList):

        for the_road in roadList:
            self.createRoad(* the_road)
