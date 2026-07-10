from social_media.laser.evalunit.evaltree.substitutetable import SubstituteTable
class Stream(object):
    def __init__(self):
        pass
    def getNumberOfTuplesAt(self, t):
        raise ValueError("Subclass must implement this routine")
    def parse_tuples(self, tuples, t, c):
        raise ValueError("Subclass must implement this routine")
    def hasTimePoint(self, t):
        raise ValueError("Subclass must implement this routine")
    def get(self, t):
        raise ValueError("Subclass must implement this routine")
