# NPE-Stanford
A repository for any and all scripts for working with the Stanford NPE Database


## patent_lookup.py

Potential Issues: The external API is buggy so I'll be taking a different approach from here on out. 

This script interfaces with the PatentView API at http://www.patentsview.org/api/patent.html. It looks up patents from a csv file that contains one line for every patent (created by line_per_patent.py). You can provide additional fields to lookup described in the above link using the -f argument. By default, it searches for ICP section and group.




## line_per_patent.py

This script takes in the cases csv downloaded at https://npe.law.stanford.edu/user/127, with one line per case, and creates a csv that contains one line for every patent. 


