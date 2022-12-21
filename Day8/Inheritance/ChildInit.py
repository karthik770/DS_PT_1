class DellCompany: # Parent Class 
	def __init__ (self,versionname, Year):
		self.versionname= versionname
		self.Year =Year
	def GetLapData(self):
		print('Lap Data ' + self.versionname, self.Year)
  
class SubCompany(DellCompany):  # Child Class 
    def __init__ (self,versionname, Year):
	    DellCompany.__init__(self, versionname, Year)
    def AllData(self): # New Method /function
        print(self.Year)

SubV2= SubCompany('V2',2023) 
SubV2.AllData()

