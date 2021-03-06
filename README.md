# Election Analysis

## Overview of Project:

In this project, I will be assisting a Colorado Board of Elections employee Tom in an election audit of the tabulated results for U.S Congressional Precinct in Colorado. 


#### Purpose of The Election Audit Analysis:

My task is to provide Colorado Board of Elections with following Audit Results:
* Total number of votes cast
* A complete list of candidates who received votes
* Total number of votes each candidate received
* Percentage of votes each candidate won
* The winner of the election based on popular vote

Eventually, present Winner of the Election based on Popular Vote. 

## Election Audit Results :

#### How many votes were cast in this congressional election?

The total number of valid votes were casted was 369,711 in this election which was calculated by adding each row as a vote with omitting the first row that is the header. 

<p align= "center">
           <img width="196" alt="Screen Shot 2022-02-14 at 10 24 55 AM" src="https://user-images.githubusercontent.com/98676400/153905985-2ad1f04c-53a6-4360-aeaa-9581cd33c41e.png">
           </p>

#### The number of votes and the percentage of total votes for each county in the precinct.

###### County Votes:
To calculate County votes,  scanned each row - first index that is second column of our csv file and find county match and the sum of votes for each county then we divided each county votes to total votes to find percent of each county. 

* Jefferson: 10.5% (38,855)

* Denver: 82.8% (306,055)

* Arapahoe: 6.7% (24,801)

<p align= "center">
<img width="178" alt="Screen Shot 2022-02-14 at 11 02 10 AM" src="https://user-images.githubusercontent.com/98676400/153911326-e9deb9e2-43eb-43e0-948c-c8acef212793.png">
           </p>


#### The county that had the largest number of votes:

In order to calculate which country had most of  the votes, we created a lines of code that scan the each row and first index that second column of csv file and find the sum of votes of each distinct county and compare them with a decision statement then determine the largest county by that comparison.

* Denver: 82.8% (306,055)

<p align= "center">
<img width="251" alt="Screen Shot 2022-02-14 at 11 17 24 AM" src="https://user-images.githubusercontent.com/98676400/153913525-2e14f680-1077-4b4a-83d4-7c07c7a37d9c.png"></p>

#### The number of votes and the percentage of the total votes each candidate received:

At this stage our script scanned each row - second index that is third column of our csv file and find name match and the sum of votes for each candidates then we divided each candidate votes to total votes to find percent of each candidate. 

* Charles Casper Stockham: 23.0% (85,213)

* Diana DeGette: 73.8% (272,892)

* Raymon Anthony Doane: 3.1% (11,606)

<p align= "center">
<img width="306" alt="Screen Shot 2022-02-14 at 11 15 39 AM" src="https://user-images.githubusercontent.com/98676400/153913339-4cdcabd8-0138-4aa1-84eb-0c9e67eec543.png"></p>

#### Winner of the Election :

In order to calculate which winner of the election, we created a decision statement on " total votes for each candidate received' then the script compared votes for each candidate to determine the winner of the election . 

* Name: Diana DeGette
    * Vote Count: 272,892
    * Percentage of total VOtes : 73.8%


<p align= "center">
<img width="267" alt="Screen Shot 2022-02-14 at 11 10 57 AM" src="https://user-images.githubusercontent.com/98676400/153912458-123c44b0-8cfe-486b-8fdb-9887dd7e74f2.png"> </p>

## Election-Audit Summary :

For this election, as it is predictable that the candidate who captured more votes from Denver County (the largest county) won the election with popular vote counts. As long as we are provided with resources,this script can be used for similar election types. 

<p align="center"> <img width="300" alt="Screen Shot 2022-02-15 at 8 22 11 AM" src="https://user-images.githubusercontent.com/98676400/154081641-bdf09327-5d34-4577-81b2-6f1edf8945e6.png"></p>

We can apply the script to State Elections for Governor and Lieutenant Governor using direct popular votes from districts as we did in this election. Also, by changing county votes to state, it is feasible to use this for Senates and House election. However, if we want to implement this script to Presidential election, there must be some refactoring of codes and changes on it due to Electoral versus Popular votes. Since U.S use winner takes all idea, Popular votes dose not always determine the winner as it happened in 2016 and 2000 election. 





