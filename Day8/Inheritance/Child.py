class DellCompany: # Parent Class 
	def __init__ (self,versionname, Year):
		self.versionname= versionname
		self.Year =Year
	def GetLapData(self):
		print('Lap Data ' + self.versionname, self.Year)
  
class SubCompany(DellCompany):  # Child Class 
  pass

SubV2= SubCompany('V2',2023) 
SubV2.GetLapData()
