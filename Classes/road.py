from scipy.spatial import distance


class Road:

    def __init__(self):
        self.traffic_signal = None
        self.traffic_signal_group = None
        self.has_traffic_signal = None
        self.angleSin = None
        self.angleCos = None
        self.length = None

    def __int__(self, start, end):
        self.start = start
        self.end = end
        self.initProperties()

    def initProperties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.angleSin = (self.end[1] - self.start[1]) / self.length
        self.angleCos = (self.end[0] - self.start[0]) / self.length
        self.has_traffic_signal = False

    def set_traffic_signal(self, signal, group):
        self.traffic_signal = signal
        self.traffic_signal_group = group
        self.has_traffic_signal = True

    def traffic_signal_state(self):
        if self.has_traffic_signal:
            i = self.traffic_signal_group
            return self.traffic_signal.current_cycle[i]
        return True

    def update(self, dt):
        n = len(self.vehicles)

        if n > 0:
            self.vehicles[0].update(None, dt)
            for i in range(1, n):
                lead = self.vehicale[i - 1]
                self.vehicles[i].update(lead, dt)

            if self.traffic_signal_state:
                self.vehicles[0].unstop()
                for vehicle in self.vehicles:
                    vehicle.unslow()
            else:
                if self.vehicales[0].x >= self.length - self.traffic_signal.slow_distance:
                    self.vehicles[0].slow(self.traffic_signal.slow_factor * self.vehicles[0]._v_max)


