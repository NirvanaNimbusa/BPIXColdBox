#!/usr/bin/env python
import os, re, sys, shutil
import math, ROOT

#sys.path.insert(1,os.path.dirname(os.path.abspath(__file__))+'/../')
from ConfigParser import *
from configure import *

class elComandante_ini(configure):

	def __init__(self, debug=False):
		self.className = "elComandante_ini"
		self.defaultOutput = "elComandante.ini"
		self.defaultConf = ""
		self.parser = SafeConfigParser()
		self.parser.optionxform = str
		self.hasDefault = False
		self.debug = debug

		# Pars list -  can be customily extended by fuctions 
		self.list_Sections = [
			"Modules",
			"ModuleType",
			"TestboardUse",
			"Cycle",
			"IV",
			"LeakageCurrent",
			"Keithley",
			"LowVoltage",
			"CoolingBox",
			"Xray",
			"Environment Xrf",
			"Environment Mo", 
			"Environment Ag",
			"Environment Ba",
			"Test Trim",
			"Analysis VcalCalibrationStepAnalysisMo",
			"Analysis VcalCalibrationStepAnalysisAg",
			"Analysis VcalCalibrationStepAnalysisBa",
			"Analysis VcalVsThresholdAnalysis",
			"Analysis VcalCalibrationAnalysis",
			"Tests",
			"OperationDetails",
		]
		# Default sections and options in elComandante_conf
		self.list_Default = {
			self.list_Sections[0]:["TB0", "TB1", "TB2", "TB3"],
			self.list_Sections[1]:["TB0", "TB1", "TB2", "TB3"],
			self.list_Sections[2]:["TB0", "TB1", "TB2", "TB3"],
			self.list_Sections[3]:["highTemp", "lowTemp", "nCycles"],
			self.list_Sections[4]:["Start", "Stop", "Step", "Delay"],
			self.list_Sections[5]:["Duration"],
			self.list_Sections[6]:["KeithleyUse", "BiasVoltage"],
			self.list_Sections[7]:["LowVoltageUse"],
			self.list_Sections[8]:["CoolingBoxUse"],
			self.list_Sections[9]:["XrayUse"],
			self.list_Sections[10]:["Temperature", "XrayVoltage", "XrayCurrent", "XrayTarget"],
			self.list_Sections[11]:["Temperature", "XrayVoltage", "XrayCurrent", "XrayTarget"],
			self.list_Sections[12]:["Temperature", "XrayVoltage", "XrayCurrent", "XrayTarget"],
			self.list_Sections[13]:["Temperature", "XrayVoltage", "XrayCurrent", "XrayTarget"],
			self.list_Sections[14]:["testParameters"],
			self.list_Sections[15]:["command"],
			self.list_Sections[16]:["command"],
			self.list_Sections[17]:["command"],
			self.list_Sections[18]:["command"],
			self.list_Sections[19]:["command"],
			self.list_Sections[20]:["TestDescription", "Test"],
			self.list_Sections[21]:["Hostname", "TestCenter", "Operator"],
		}
		# Pars map - containor
		self.Sections = { 
			# Default sections and options
			self.list_Sections[0]:{},
			self.list_Sections[1]:{},
			self.list_Sections[2]:{},
			self.list_Sections[3]:{},
			self.list_Sections[4]:{},
			self.list_Sections[5]:{},
			self.list_Sections[6]:{},
			self.list_Sections[7]:{},
			self.list_Sections[8]:{},
			self.list_Sections[9]:{},
			self.list_Sections[10]:{},
			self.list_Sections[11]:{},
			self.list_Sections[12]:{},
			self.list_Sections[13]:{},
			self.list_Sections[14]:{},
			self.list_Sections[15]:{},
			self.list_Sections[16]:{},
			self.list_Sections[17]:{},
			self.list_Sections[18]:{},
			self.list_Sections[19]:{},
			self.list_Sections[20]:{},
			self.list_Sections[21]:{},
			# Can be customily extended by fuction
		}


################ example ################
#elini = elComandante_ini(debug=True)
##elini = elComandante_ini()
#elini.getDefault("../elComandante.ini", True)
#elini.listSections()
#elini.listOptions("mySection")
#elini.makeNewSection("mySection1")
#elini.makeNewSection("mySection1")
#elini.makeNewSection("mySection2")
#elini.makeNewSection("mySection3")
#elini.listSections()
#elini.listOptions("mySection")
#elini.listOptions("mySection1")
#elini.listOptions("mySection2")
#elini.makeNewOption("mySection1", "Opt1", "Here")
#elini.makeNewOption("mySection1", "Opt2", "Here")
#elini.makeNewOption("mySection2", "Opt1", "Here")
#elini.listOptions("Transfer")
#elini.callOption("Transfer", "user" )
#elini.changeOptValue("mySection1", "Opt3", "There" )
#elini.changeOptValue("mySection1", "Opt1", "There" )
#elini.changeOptValue("Transfer", "user", "jtsai" )
#elini.callOption("Transfer", "user" )
#elini.callConfig()
#elini.makeConfig()