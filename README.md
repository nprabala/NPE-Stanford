# NPE-Stanford
A repository for ongoing projects related to and scripts that work with the Stanford NPE Database

## Projects

### Art Units of Patent Trolls' IP Over Time -- Nikhil Prabala

My idea is to use the Stanford NPE database's list of 1's and 5's and cross reference that with Google's BigQuery Patent database. I hope to look at the art unit classifcations of the patents that PAE's are litigating from year to year and determine in which technological sector the bulk of malicious litigation is occurring. This could be a good jumping off point for examining relevant legislation, policies, or approaches to approving these patents and in turn suggesting future work.


## Patent Data Collection Overview

If you want to collect data using BigQuery, there are a few things you need to do.

First, download the source data from the https://npe.law.stanford.edu site after logging in with your user. Then, run the line_per_patent.py script on that file as described in the "Script Overview" section. Afterwards, you will have a csv that has one line per patent. 

Google has limits on how much data you're allowed to upload into a table in BigQuery from your machine, so you have two options at this stage. You can run future queries on the entire dataset by uploading the generated file to Google Cloud Storage, or you can first trim the data to make it small enough to allow a local upload. One way to trim the data is to filter it by asserter code using filter_by_code.py.

No matter which you choose, you'll need a free account and a project created on BigQuery. You can select your project, create a dataset, and then within that dataset, select create table. It will then prompt you for where to look for the file you want to use to populate that table. Select either Google Cloud Storage or a local file on your machine depending on which option you chose before. 

You can then run SQL Queries on that data, and whichever datasets that BigQuery has that you want to reference.

Reference the pto-PEDS_sample_query.sql file for an example on how this can be done once you've set up your own BigQuery account and project. More details are provided within the file, and below.


## Script Overview

The below scripts were all written in Python 2.7. When run for the first time you might need to install relevant libraries, or even Python itself. 

For Python:

https://www.python.org/download/releases/2.7/

To maintain a clean environment, where your libraries aren't all overlapping, consider virtualenv.

https://docs.python-guide.org/dev/virtualenvs/

For other libraries:

First, grab the installer: https://pypi.org/project/pip/

Then, install the relevant libraries until no errors pop up (I'll add a simpler way to do this with a requirements file later)

***
pip install MISSING LIBRARY
***


### line_per_patent.py

This script takes in the cases csv downloaded at https://npe.law.stanford.edu, with one line per case, and creates a csv that contains one line for every patent. It assumes you haven't changed the name of the cases file from the default, as it writes a new csv with the same datestamp, so you can be certain which file corresponds to which source data. 

If the source data has been changed (ie, the patents column in the cases file is no longer in the same place because columns have been removed or added) then this file will need to be edited.

You call it in Mac or Ubuntu as follows:

***
python line_per_patent.py -filename CASES_FILE_NAME_HERE
***

And in windows like below:

***
line_per_patent.py -filename CASES_FILE_NAME_HERE
***


### filter_by_code.py

This script takes in the file output from line_per_patent.py, along with a list of codes you want to filter by, and returns a csv file that has only patents with asserters that belong in that list of codes. I used this script to filter down a list of patents for upload into Google's BigQuery so I could compare them to their existing patent dataset.


You call it in Mac or Ubuntu as follows:

***
python filter_by_code.py -filename PATENTS_NAME_HERE -codes CODE NUMBERS HERE
***

And in windows like below:

***
filter_by_code.py -filename PATENTS_FILE_NAME_HERE -codes CODE NUMBERS HERE
***

### pto-PEDS_sample_query.sql

This file contains a query I used to collect the art unit, national classifications, and business categories for each litigated patent in our database. Copy the code inside into the query editor in BigQuery, making edits to names and fields as necessary to match your project's name, and to match exactly what fields and databsases you are trying to examine.

### patent_lookup.py

Potential Issues: The external API is buggy so I'll be taking a different approach from here on out. This script is no longer in usage, and should not be referenced for, well, anything.

This script interfaces with the PatentView API at http://www.patentsview.org/api/patent.html. It looks up patents from a csv file that contains one line for every patent (created by line_per_patent.py). You can provide additional fields to lookup described in the above link using the -f argument. By default, it searches for ICP section and group.




