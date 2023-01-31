# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:53:09 2023

@author: victor
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:53:11 2023

@author: victor
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:03:46 2023

@author: victor
"""

from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer
import time
import datetime
nodeID="37052693-fccf-4a43-b9e8-f3b89d2a69a3"
apiURL="https://api-dccs-ensaas.education.wise-paas.com/"
CredentialKEY="6f4c4b5d89db8cc94fd1402b3c970eom"
edgeAgentOptions = EdgeAgentOptions(nodeId = nodeID)#nodeID
edgeAgentOptions.connectType = constant.ConnectType['DCCS']
dccsOptions = DCCSOptions(apiUrl = apiURL, credentialKey = CredentialKEY)
edgeAgentOptions.DCCS = dccsOptions
_edgeAgent = EdgeAgent(edgeAgentOptions)
_edgeAgent.connect()


#creat data connect

def creatdataconnect(_edgeAgent):
    config = __generateConfig()
    _edgeAgent.uploadConfig(action = constant.ActionType['Create'], edgeConfig = config)
def updateconfig(_edgeAgent):
    config = __generateConfig()
    _edgeAgent.uploadConfig(action = constant.ActionType['Update'], edgeConfig = config)

def __generateConfig():
    config = EdgeConfig()
    nodeConfig = NodeConfig(nodeType = constant.EdgeType['Gateway'])
    config.node = nodeConfig
    for i in range(11):
        deviceConfig = DeviceConfig(id = 'Floor'+str(i+1),
          name = 'Floor'+str(i+1),
          description = 'Floor'+str(i+1),
          deviceType = 'Smart Device',
          retentionPolicyName = '')
        for j in range(20):
            analog = AnalogTagConfig(name = 'x'+str(j+1),
                description = 'x'+str(j+1),
                readOnly = False,
                arraySize = 0,
                spanHigh = 1000,
                spanLow = 0,
                engineerUnit = '',
                integerDisplayFormat = 4,
                fractionDisplayFormat = 2)
            deviceConfig.analogTagList.append(analog)
        for j in range(20):
            analog = AnalogTagConfig(name = 'y'+str(j+1),
                description = 'y'+str(j+1),
                readOnly = False,
                arraySize = 0,
                spanHigh = 1000,
                spanLow = 0,
                engineerUnit = '',
                integerDisplayFormat = 4,
                fractionDisplayFormat = 2)
            deviceConfig.analogTagList.append(analog)      
            
        config.node.deviceList.append(deviceConfig)
    
    return config 
def __generateData():
      edgeData = EdgeData()
      for i in range(11):
        for j in range(20):
            deviceId = 'Floor'+str(i+1)
            tagName = 'x'+str(j+1)
            value = int(2)
            
            tag = EdgeTag(deviceId, tagName, value)
            edgeData.tagList.append(tag)
        for j in range(20):
            deviceId = 'Floor'+str(i+1)
            tagName = 'y'+str(j+1)
            value = int(1)
            tag = EdgeTag(deviceId, tagName, value)
            edgeData.tagList.append(tag)
      edgeData.timestamp = datetime.datetime.now()
      return edgeData
def senddata(_edgeAgent):
     data = __generateData()
     _edgeAgent.sendData(data)


################creat#####################
#creatdataconnect(_edgeAgent)   #creatconnect
#_edgeAgent.disconnect()
################update####################
#updateconfig(_edgeAgent)
#while(1):
        
#    senddata(_edgeAgent)
#    time.sleep(300)


