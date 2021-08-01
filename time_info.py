"""
Class for time zone
"""
from datetime import tzinfo, timedelta


class SpbTime(tzinfo):
    """
    Class for Saint-Petersburg time zone
    """
    def utcoffset(self, dt):
        return timedelta(hours=3)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self,dt):
        return "+03:00"
    def  __repr__(self):
        return f"{self.__class__.__name__}()"
