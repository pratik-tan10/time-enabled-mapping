import os
mxd = arcpy.mapping.MapDocument("CURRENT")
df1 = arcpy.mapping.ListDataFrames(mxd, 'Contiguous')[0]
df2 = arcpy.mapping.ListDataFrames(mxd, 'Alaska')[0]
df3 = arcpy.mapping.ListDataFrames(mxd, 'Hawaii')[0]

timeStep = 5

df1.time.currentTime = df1.time.startTime
df2.time.currentTime = df1.time.currentTime
df3.time.currentTime = df1.time.currentTime

while df1.time.currentTime <= df1.time.endTime:
	fname = "Population_" + str(df1.time.currentTime.year)+ ".png"
	arcpy.mapping.ExportToPNG(mxd, os.path.join(r"simgs", fname), resolution = 300)
	df1.time.currentTime = df1.time.currentTime + timeStep*df1.time.timeStepInterval
	df2.time.currentTime = df1.time.currentTime
	df3.time.currentTime = df1.time.currentTime
	print(df1.time.currentTime, df2.time.currentTime, df3.time.currentTime)
