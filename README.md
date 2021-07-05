# **Election_Analysis**

## Overview of the Election Audit

The project goal is to assist a Colorado Board of Elections employee with the election audit of the tabulated results of the US congressional precinct election in Colorado. Our task was to help our client automized the analysis by utilizing Python for future elections audits. The analysis has the following tasks:

- Calculate the total number of votes cast in the congressional election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. 
- Determine the county with the largest number of votes. 
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Determine the winner of the election, their vote count and their percentage of the total votes

### Resources

Data Source: [election_analysis](https://github.com/chocoplace/election_analysis/blob/main/election_analysis/Resources/election_results.csv).

Software: Python 3.7.6, Visual Studio Code 1.57.1, among other technical tools such as Git Bash. 

### Election-Audit Results:

The code for the analysis of the election can be found here [PyPoll_Challenge](https://github.com/chocoplace/election_analysis/blob/main/PyPoll_Challenge.py), and the results show that:

- There were 369,711 votes cast in the election. 

- The counties voter turnout were:
	County 1: Jefferson with 10.5% of the vote and 38,855 number of the votes
	County 2: Denver with 82.8% of the vote and 306,055 number of the votes
	County 3: Arapahoe with 6.7% of the vote and 24,801 number of the votes

- The county with the largest turnout:
*Denver was the county with the largest turnout with 82.8% of the vote and 306,055 number of the votes. 

- The candidates results were:
	- Candidate 1: Charles Casper Stockham received 23.0% of the vote and 85,213 number of the votes.
	- Candidate 2: Diana DeGette received 73.8% of the vote and 272,892 number of the votes.
	- Candidate 3: Raymon Anthony Doane received 3.1% of the vote and 11,606 number of the votes.

- The winner of the election was:
	*Candidate Diana DeGette (2), who received 73.8% of the vote and 272,892 number of the votes.*

To help our client visualize the results, we created the following report [Election_Results](https://github.com/chocoplace/election_analysis/blob/main/election_analysis/analysis/election_results.txt) : 
![Election_Results](https://github.com/chocoplace/election_analysis/blob/main/election_analysis/Resources/Deliverable1.png)


### Election Audit Summary

To the election commission, the results of this analysis will support not only this election audit but in addition can be a starting point for future analysis for example by: 

- Calculating the number of votes received by each candidate per county. 
- Creating a comparative report by conducting an analysis per congressional elections calendar, focusing on the turnout of the counties. The analysis can provide a background of the party's popularity in each county. 
- The code can be applied to any election audit following the structure and comments available on the code. 
