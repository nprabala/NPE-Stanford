SELECT 

# These are the fields you want to grab from the Google BigQuery Table you're examining
# Make sure you spell the names as they are listed when you click on the BigQuery Table's name
patentCaseMetadata.groupArtUnitNumber.electronicText AS Art_Unit , patentCaseMetadata.patentGrantIdentification.patentNumber AS Google_Patent_Number, patentCaseMetadata.businessEntityStatusCategory as Business_Category, 

# I had to do something called an unnest to access these individual values from their parent array in the table.
# This is necessary to access the results as a csv.
classification.mainNationalClassification.nationalClass as National_Class,
classification.mainNationalClassification.nationalSubclass as National_Subclass,

# These are relevant fields from the NPE database. Add or Remove according to your needs. 
# Make sure spelling matches here as well.
patents as NPE_Patent_Number, Filing_Date as Case_Filing_Date, Asserter_Category, Case_Title, Venue, DJ, Alleged_Infringer, Patent_Asserter


# This is the name of the database you want to query that is hosted by Google in BigQuery
# I've added in an UNNEST function to access individual values inside a RECORD type object in the table (an Array)
FROM `patents-public-data.uspto_peds.applications`  as Application , UNNEST(patentCaseMetadata.patentClassificationBag.cpcClassificationBagOrIPCClassificationOrECLAClassificationBag) as classification

# This is the project name of the NPE database (or whatever data that you provided)
# Be sure to match the project name to what YOUR project's name is. It's not necessarily as I have it here.
# Here Inner Join Means to merge the two databases where the condition (the next line) applies
INNER JOIN `npe-stanford.npe_patents.all_patents` as ALL_PATENTS 


# This is the condition that when true, merges a row in table one with a row in table two
# In this case, rows from both tables are merged when they have matching patent numbers.
ON Application.patentCaseMetadata.patentGrantIdentification.patentNumber = ALL_PATENTS.patents;


