from CubeStories import storyTeller

metdadataparameters={
    "sparqlEndPointUrl":"http://macjan.datascienceinstitute.ie:8080/sparql", #endpoint of url
    "jsonMetaDataFile":"JSON_Metadata_Structure.json" #JSON file with metadata
}

cubeparameters={
    "cube":"PopulationPrinicipalStatus",  #Key value of cube
    "dimensions":["EconomicStatus","Gender"], #Dimensions from cube
    "measures":["Population"], #Measures
    "hierdimensions": #Hierachical Dimension with granularity level
        {"RefArea":{ #Dimension key
            "selected_level":"CTY" # selected level
            }
        }
}

#cubeparameters=dict()

AnalysisPipeline={  ##Dictionary pair: [Pattern Key]:[List of Pattern Parameters]
    
    "LeagueTab":{   
       "columns_to_order":["Population"],
       "order_type":"desc",
       "number_of_records":10
   },
   "DissFact":{
        "dim_to_dissect":"RefArea"
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