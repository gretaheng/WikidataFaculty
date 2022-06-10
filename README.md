<h1>Wikidata Batch Prepare</h1>
<h4>1. Data Cleaning and Preparation</h4>
<h4>2. Data Refining</h4>
<h4>3. Data Processing</h4>


<h3>Data Cleaning and Preparation</h3>
`dataPrep.py` <br/>

In this step, the required data columns are added to the scrapped data. 
Fields like LCnum, web are not available and are required for future enhancements for data models. 
The scripts assign values for field like department, college and university to faulty. 
Assigns the website values in regard to base url provided to the script. 
Scripts also cleans up missing values which will result in it not getting processed in next steps.

<h3>Data Refining</h3>
`openRefine.py` <br/>

Here, using automation and open refine application, the script load the data and setit up in a tabular format. 
Open refine using wikibot extracts the data that is closely related to the mentioned field and assigns it. 
At the end the scripts provides steps to user, which has to be manually performed inorder to finish the refinement.
Need open refine installed and started, and chrome driver exe in ./driver folder.

<h3>Data Processing</h3>
`finalPrepareStep.py` <br/>

Finally, in Data Processing, there are 2 functions. 
One for tenure faculty and another for emeritus. 
Using pywikibot each function assigns the default values to each (e.g. University Name: San Diego State University). 
After this it creates a page for rows not having wikidata entry. 
And adding new values that are not present in already existing wikidata entries. 
The output of this script is the wikidata entry id for newly created items.