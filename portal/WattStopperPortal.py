
def lightsChanged(val):
    print "Switch on is "+str(val)
    
def occupancyDetected(val):
    print "Occupancy detected"
    
import wx

def tryMeLater():
    wx.CallLater(10000, doMeLater)
    
def doMeLater():
    print "I GOT DONE LATER"