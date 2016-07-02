
buttonCount = 0
ledState = False
coilAState = False
coilBState = False
lightOn = False

CONTROLLER = '\x00\x00\x20'   # RPi
#CONTROLLER = '\x00\x00\x01'  # Portal

#                  RF100   RF200
PIN_BUTTON = 28  # 15      28
PIN_LED    = 29  # 16      29
PIN_CAS    = 30  # 17      30
PIN_CBS    = 31  # 18      31

@setHook(HOOK_STARTUP)
def _startupEvent():
    setPinDir(PIN_BUTTON,False)
    writePin(PIN_BUTTON,False)

def _switchTurnedOn():
    global lightOn
    lightOn = True
    rpc(CONTROLLER,'lightsChanged',True)    

def _switchTurnedOff():
    global lightOn
    lightOn = False
    rpc(CONTROLLER,'lightsChanged',False)

def _occupancyDetected():    
    rpc(CONTROLLER,'occupancyDetected',True)

def pushButton():
    global buttonCount
    setPinDir(PIN_BUTTON,True)
    buttonCount = 300
    
def setSwitch(on):
    global lightOn
    if on != lightOn:
        pushButton()    
        
@setHook(HOOK_1MS)
def _timer1msEvent(currentMs):
    global buttonCount, ledState, coilAState, coilBState
    if buttonCount>0:
        buttonCount = buttonCount - 1
        if buttonCount ==0:
            setPinDir(PIN_BUTTON,False)
            
    ls  = readPin(PIN_LED)
    cas = readPin(PIN_CAS)
    cbs = readPin(PIN_CBS)
    
    if ls != ledState:        
        ledState = ls
        if not ls:
            print "LED STATE"
            _occupancyDetected()
    
    if cas != coilAState:
        print "COIL A"
        coilAState = cas
        if cas:
            _switchTurnedOn()
        
    if cbs != coilBState:
        print "COIL B"
        coilBState = cbs
        if cbs:
            _switchTurnedOff()
        
