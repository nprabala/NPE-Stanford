# NPE-Stanford
A repository for ongoing projects related to and scripts that work with the Stanford NPE Database

## Projects

### IPC Classifications of Patent Trolls' IP Over Time -- Nikhil Prabala

My idea is to use the Stanford NPE database's list of 1's and 5's and cross reference that with Google's BigQuery Patent database. I hope to look at the IPC classifcations of the patents that PAE's are litigating from year to year and determine in which technological sector the bulk of malicious litigation is occurring. This could be a good jumping off point for examining relevant legislation, policies, or approaches to approving these patents and in turn suggesting future work.

## Script Overview

### patent_lookup.py

Potential Issues: The external API is buggy so I'll be taking a different approach from here on out. 

This script interfaces with the PatentView API at http://www.patentsview.org/api/patent.html. It looks up patents from a csv file that contains one line for every patent (created by line_per_patent.py). You can provide additional fields to lookup described in the above link using the -f argument. By default, it searches for ICP section and group.




### line_per_patent.py

This script takes in the cases csv downloaded at https://npe.law.stanford.edu/user/127, with one line per case, and creates a csv that contains one line for every patent. 


