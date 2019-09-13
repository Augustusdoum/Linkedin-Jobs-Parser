# Linedin Jobs Parser

This bit of code lets you parse through all of Linkedin Job Offers and have the results sent to you by mail (through Gmail API) with a bit of job titles keywords filtering to increase profile fitting accuracy. 

I wrote it to find any new job posted in the sutainable developpment area.

To use it :

In the LinkedinJobsParser.py file :
- Replace the keywords list with keywords of your interest
- Change the keywords in the 'to_exclude' list (within the get_relevance function) to filter out any job postings that include these words.
- Add any keywords that you need to see appear in the job listing in the keywords list (within the get_relevance function).

This code will save the listing in your code's folder.

In the GmailAPI.py file : 
- Change the from/to addresses, body, subject and attachment path to the file named 'recent_top_results' stored in the folder where you saved this code.
- Add your gmail password in the '#Authentification' to let the API send the email containing the listings on your behalf.
