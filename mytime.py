# mytime.py
# 2019-14505 엄세희



class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        minutes += seconds//60
        seconds = seconds%60
        hours += minutes//60
        minutes = minutes%60
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, hours):
        self.__hours = hours

    @minutes.setter
    def minutes(self, minutes):
        self.__minutes = minutes

    @seconds.setter
    def seconds(self, seconds):
        self.__seconds = seconds


    def __repr__(self):
        return 'Time({:d},{:d},{:f})'.format(self.hours, self.minutes, self.seconds)
    
    def __add__(self, other):
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        return Time(h, m, s)
    
    def __sub__(self, other):
        h = self.hours - other.hours
        m = self.minutes - other.minutes
        s = self.seconds - other.seconds
        return Time(h, m, s)


    def __mul__(self, x):
        return Time(self.hours*x, self.minutes*x, self.seconds*x)

    def __rmul__(self, x):
        return self.__mul__(x)
    
    def __lt__(self, other):
        selftime = 3600*self.hours + 60*self.minutes + self.seconds
        othertime = 3600*other.hours + 60*other.minutes + other.seconds
        if selftime < othertime :
            return 'True'
        else:
            return 'False'
    def __eq__(self, other):
        selftime = 3600*self.hours + 60*self.minutes + self.seconds
        othertime = 3600*other.hours + 60*other.minutes + other.seconds
        if selftime == othertime:
            return 'True'
        else:
            return 'False'

