from CubeStories import storyTeller

metdadataparameters={
    "sparqlEndPointUrl":"http://macjan.datascienceinstitute.ie:8080/sparql", #endpoint of url
    "jsonMetaDataFile":"JSON_Metadata_Structure.json" #JSON file with metadata
}

cubeparameters={
    "cube":"PersonsIndustry",  #Key value of cube
    "dimensions":["Gender", "Industry"], #Dimensions from cube
    "measures":["PersonsAtWork"] #Measures
}

#cubeparameters=dict()

AnalysisPipeline={  ##Dictionary pair: [Pattern Key]:[List of Pattern Parameters]

    "StBigDrillDown":{
        "hierdim_drill_down":{
          "DimKey":["PR","ED","CTY"]
        }
    },

    "LeagueTab": {
       "columns_to_order":["PersonsAtWork"],
       "order_type":"asc",
       "number_of_records":1
   }

}
#######DO NOT CHANGE########################
a=storyTeller(metadataparameters=metdadataparameters,
                cubeparameters=cubeparameters,
                patternparameters=AnalysisPipeline)


a.tellStory()
#############################################
x=(a.showStory())

print(x)