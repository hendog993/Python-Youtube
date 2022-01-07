from pprint import pprint as prt 
# Note: ArincRecord.txt last line must be complete - delete the last msg if it doesn't have a complete timestamp. 

class ARINCWord:
    ''' Single Arinc Word Class for creating ARINC word objects ''' 
    def __init__(self, label, name):
        # self.labelConfig = labelConfig TODO TODO 
        self.label = label # in Hex string format
        self.name = name
        self.timeStamp = []  # Empty array of timestamps
        self.numOccurrances = 0
        self.averageOccurrance = 0 
        pass

    def RoundARINCValues(self):
        self.numOccurrances = round ( self.numOccurrances,2)
        self.averageOccurrance = round ( self.averageOccurrance, 2)
        return  

    pass

class ARINCLabelConfig:
    
    def __init__(self, msgType, numSigBits, resolution):
        self.msgType = msgType
        self.numSigBits = numSigBits
        self.resolution = resolution
        pass 
    pass 


class RxMessageArray:
    ''' Array of ARINC Word objects used for iterating through ARINC Words '''
    def __init__(self, arincWordArray):
        self.arincWordArray = arincWordArray
        self.numARINCWords = len(arincWordArray)
        pass
    pass

class Application:
    ''' Application class composed of application methods and encapsulated with the ARINC RxMsg array ''' 
    def __init__(self, rxMsgArray):
        self.rxMsgArray = rxMsgArray
        pass

    def ProcessMessage(self, textEntry):
        ''' Called for each text entry within the list of received ARINC messages (from the .txt file) ''' 
        strLabel = textEntry[6:8]
        intTimeStampInMicroseconds = int( textEntry[9:25], 16)

        # Search the list of rxMsgs for a label match
        for i in range(self.rxMsgArray.numARINCWords):
            thisRxMsg = self.rxMsgArray.arincWordArray[i]
            if ( thisRxMsg.label == strLabel ):
                thisRxMsg.timeStamp.append(intTimeStampInMicroseconds)
                thisRxMsg.numOccurrances += 1
                break
        pass

    def CreateMessageReport(self):
        ''' Creates message report for all processed messages ''' 
        self.CalculateIntervalTimestamp()
        for i in range ( self.rxMsgArray.numARINCWords):
            thisMsg = self.rxMsgArray.arincWordArray[i]
            thisMsg.RoundARINCValues()
            prt( thisMsg.name + "  " + " num Occurrances: " + str(thisMsg.numOccurrances) + " Average Interval: " + str(thisMsg.averageOccurrance))
        pass

    # For each message, calculate the average transmit interval for each message
    def CalculateIntervalTimestamp(self):

        for i in range ( self.rxMsgArray.numARINCWords):
            # Calculate the "derivativves of the n + n+1 elements and average them
            numValuesToCalculate = self.rxMsgArray.arincWordArray[i].numOccurrances
            if ( numValuesToCalculate != 0):
                tempAverageArray = []
                for j in range ( numValuesToCalculate - 1):
                    tempAverageArray.append ( self.rxMsgArray.arincWordArray[i].timeStamp[j+1] - self.rxMsgArray.arincWordArray[i].timeStamp[j])
                self.rxMsgArray.arincWordArray[i].averageOccurrance = self.AverageList(tempAverageArray)/1000
        pass


    @staticmethod
    def AverageList(listToAverage):
        ''' Helper function to calculate average array value ''' 
        return sum(listToAverage)/len(listToAverage)

    pass


windOnNose = ARINCWord('73','windOnNose')
slipSkid = ARINCWord('A8','slipSkid')
windSpeed = ARINCWord('CD','windSpeed')
magHeading = ARINCWord('D0','magHeading')
pitchAngle = ARINCWord('D4','pitchAngle')
rollAngle = ARINCWord('D5','rollAngle')
bodyPRate = ARINCWord('D6','bodyPRate')
bodyRRate = ARINCWord('D7','bodyRRate')
bodyYRate = ARINCWord('D8','bodyYRate')
bodyLongAccel = ARINCWord('D9','bodyLongAccel')
bodyLatAccel = ARINCWord('DA','bodyLatAccel')
bodyNormAccel = ARINCWord('DB','bodyNormAccel')
turnRate = ARINCWord('E0','turnRate')
windDir = ARINCWord('FA','windDir')
AHRSS1 = ARINCWord('BA','AHRSS1')
AHRSS2 = ARINCWord('BC','AHRSS2')
AHRSS3 = ARINCWord('BD','AHRSS3')
airspeedRate = ARINCWord('80','airspeedRate')
mach = ARINCWord('85','mach')
tat = ARINCWord('89','tat')
sat = ARINCWord('8B','sat')
correctedIP = ARINCWord('8D','correctedIP')
deltaPAlpha = ARINCWord('92','deltaPAlpha')
UncorImpactPressure = ARINCWord('93','UncorImpactPressure')
aoaRate = ARINCWord('94','aoaRate')
totalP = ARINCWord('A2','totalP')
staticP = ARINCWord('A6','staticP')
indicatedOAT = ARINCWord('99','indicatedOAT')
baroCorrection = ARINCWord('9D','baroCorrection')
adcStatus = ARINCWord('B9','adcStatus')
equipmentID = ARINCWord('FF','equipmentID')
pressureALT = ARINCWord('83','pressureALT')
baroCAlt = ARINCWord('84','baroCAlt')
equivAirspeed = ARINCWord('86','equivAirspeed')
trueAirspeed = ARINCWord('88','trueAirspeed')
altitudeRate = ARINCWord('8A','altitudeRate')
angleOfAttack = ARINCWord('91','angleOfAttack')
swConfig = ARINCWord('FE','swConfig')
gpsAlt = ARINCWord('3E','gpsAlt')
gpsLat = ARINCWord('48','gpsLat')
gpsLong = ARINCWord('49','gpsLong')
gpsLatFine = ARINCWord('50','gpsLatFine')
gpsLongFine = ARINCWord('51','gpsLongFine')
positionUTC = ARINCWord('60','positionUTC')
gpsStatus = ARINCWord('BB','gpsStatus')
UTC = ARINCWord('68','UTC')
vertUncertLevel = ARINCWord('6E','vertUncertLevel')
gpsVertVel = ARINCWord('75','gpsVertVel')
nsVel = ARINCWord('76','nsVel')
ewVel = ARINCWord('7C','ewVel')
horizUncLevel = ARINCWord('9F','horizUncLevel')
horizFOM = ARINCWord('A7','horizFOM')
date = ARINCWord('B0','date')
horizProt = ARINCWord('58','horizProt')
vertProt = ARINCWord('5B','vertProt')
vfom = ARINCWord('5E','vfom')
gwssFaultSum = ARINCWord('EA','gwssFaultSum')
phaseOfFlight = ARINCWord('54','phaseOfFlight')

listOfARINCWords = [
windOnNose,
slipSkid,
windSpeed,
magHeading,
pitchAngle,
rollAngle,
bodyPRate,
bodyRRate,
bodyYRate,
bodyLongAccel,
bodyLatAccel,
bodyNormAccel,
turnRate,
windDir,
AHRSS1,
AHRSS2,
AHRSS3,
airspeedRate,
mach,
tat,
sat,
correctedIP,
deltaPAlpha,
UncorImpactPressure,
aoaRate,
totalP,
staticP,
indicatedOAT,
baroCorrection,
adcStatus,
equipmentID,
pressureALT,
baroCAlt,
equivAirspeed,
trueAirspeed,
altitudeRate,
angleOfAttack,
swConfig,
gpsAlt,
gpsLat,
gpsLong,
gpsLatFine,
gpsLongFine,
positionUTC,
gpsStatus,
UTC,
vertUncertLevel,
gpsVertVel,
nsVel,
ewVel,
horizUncLevel,
horizFOM,
date,
horizProt,
vertProt,
vfom,
gwssFaultSum,
phaseOfFlight,
]


if __name__ == '__main__':
    rxArray = RxMessageArray (listOfARINCWords)
    app = Application(rxArray)

    with open("ArincRecord.txt", "r") as file:
        for x in file:
            app.ProcessMessage(x)
        file.close()
    app.CreateMessageReport()
    pass