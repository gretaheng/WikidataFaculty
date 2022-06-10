##Wikidata Batch Prepare
####1. Data Cleaning and Preparation
####2. Data Refining
####3. Data Processing


###Data Cleaning and Preparation
`dataPrep.py`

In this step, the required data columns are added to the scrapped data. 
Fields like LCnum, web are not available and are required for future enhancements for data models. 
The scripts assign values for field like department, college and university to faulty. 
Assigns the website values in regard to base url provided to the script. 
Scripts also cleans up missing values which will result in it not getting processed in next steps.

####Data Refining
`openRefine.py`

Here, using automation and open refine application, the script load the data and setit up in a tabular format. 
Open refine using wikibot extracts the data that is closely related to the mentioned field and assigns it. 
At the end the scripts provides steps to user, which has to be manually performed inorder to finish the refinement.
Need open refine installed and started, and chrome driver exe in ./driver folder.

####Data Processing
`finalPrepareStep.py`

Finally, in Data Processing, there are 2 functions. 
One for tenure faculty and another for emeritus. 
Using pywikibot each function assigns the default values to each (e.g. University Name: San Diego State University). 
After this it creates a page for rows not having wikidata entry. 
And adding new values that are not present in already existing wikidata entries. 
The output of this script is the wikidata entry id for newly created items.