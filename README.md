# Frankendama Sharing

## Contents
* [Introduction](#introduction)
	* [Objective](#objective)
	* [Proposal](#proposal)
* [Architecture](#architecture)
	* [Risk Assessment](#risk-assessment)
	* [Trello Board](#Trello-Board)
	* [Entity Relationship Diagram](#entity-relationship-diagram)
	* [Test Analysis](#analysis-of-testing)
	* [Continuous Integration](#continuous-integration)
* [Development](#development)
	* [Unit Testing](#unit-testing)
	* [Integration Testing](#integration-testing)
* [Footer](#footer)
	* [Future Improvements](#future-improvements)
	* [Author](#author)
	* [Acknowledgements](#acknowledgements)


## Introduction

### Objective

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

This objective requies the following:

<li>Functioning CRUD application created in Python</li>
<li>Functioning front-end to website using Flask</li>
<li>Trello board or equivalent</li>
<li>Relational database - must contain at least one one-to-many relationship</li>
<li>Clear documentation</li>
<li>Detailed risk assessment</li>
<li>Automated tests</li>
<li>Fully integrated into Github or other VCS</li>

### Proposal

A kendama is a japanese skilltoy that looks like this:
<br>
<br>
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/Kendama.png" alt="A kendama"/>

Which is made up of five parts:
<li>Tama (The ball)</li>
<li>Sarado (The top cups)</li>
<li>Sword (The long part with the spike)</li>
<li>String (Attaches the ball to the ken</li>
<li>Bearing/Bead (Stops the ball coming off the string)</li>
<br/>
When a user of this toy creates a setup with each 5 parts from different companies, that is called a Frankendama.

I have created a Frankendama Sharing site, where users can upload thier favourite setups and builds in a neat format.
Below i demonstrate how my site covers the required CRUD capability.

Create: <br>
User can create a Frankendama made from 5 parts.

Read:<br>
User enters the homepage where all the builds are availible in a table to read.

Update:<br>
User has an update button on the same row as the entry needing updated.

Delete:<br>
User has a delete button on the ame row as the entry needing deleted.


## Architecture

### Risk Assessment
My Risk Assessment for this project can be seen below, it has a list of risks that the project may have and has an assigned Risk/Impact value.
<br>
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/RiskAssessment3.png" alt="Risk Assessment"/>
As you can see as the project went on risks were discovered and I therefore added a date column.

### Trello Board
The way i documented the progress of my project overall was to use a Trello Board.

Since the project is small scale and it has a more visual representation of progress i decided Trello was better to use over other tools such as Jira.
<br>
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/UserStories.png" alt="User Stories"/>
My full Trello Board can be found <a href="https://trello.com/b/L9cnnpHA/user-story-qaproject">here</a>

Overtime i added a few extra steps to the trello board for quality of life features such as custom form validators.


### Entity Relationship Diagram

My outdated ERD can be seen below, followed by the updated version.
<br>
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/QAprojectERDdraft1.png" alt="Old ERD"/>
<br/>
My original ERD was a 1-1 relationship-diagram which is not suitable for this project so i remade the ERD as follows:
<div style="block;"> 
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/QAprojectERDcomplete.png" alt="ERD Image"/>
This is the current ERD for this project.

I decided a simple 1-to-Many relationship was best suited for this project. Originally I would have a table for the frankendama holding the title and description and a parts table taht held all the information on the parts of the build. However, after beginning implementation of the database relationship, I realised that my original ERD was a 1-to-1 and did not cover the specifications of the project. Therefore I created a new ERD that had two tables with a 1-to-Many, frankendama table holds everything to do with the build, all the part names, title and description. Table two is called Companies and stores all the names of the companies used in the build with a foreign key to frankendama, this allows for further implementation of a list of top five most commonly used companies for their parts.

### Analysis of Testing

As this is a much smaller scale project, the only testing implemented is unit testing and integration testing. Out of scope testing not implemented would include, system and acceptance testing. As I utilized a test-driven method of development, I had created tests for each part of CRUD in advanced so that during development my program would follow this. One of the biggest reliefs during the development stage was that my unit test for the Update route returned a fail once I had finished that module. Due tot eh fact that my unit test displayed a fail I was able to find the error almost immediately and fix it. The error was when a user wanted to update their entry with a different part to their build, when they changed the list of companies associate with the build and press submit, none of the previous company names where removed. 

<img srv="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/TestingAnalysis.png" alt="Error found during development.">

This failed unit test identified and error that if it had slipped would have caused a huuge formating error on the homepage.

### Continuous Integration
### Jenkins Script

## Development

### Unit Testing
### Integration Testing

## Footer

### Future Improvements
### Author
Marius Saunders
### Acknowledgements
My QA Trainers:
Ryan Wright
Oliver Nichols
Victoria Sacre
Savannah Vaithilingam

<a href="https://stackoverflow.com/questions/68489027/sorting-and-deleting-a-1-to-many-relatiionship-in-sqlalchemy-and-flask">Stack Overflow</a> for the assistance on one SQLALchemy query 

### Versions
26/07/21 - v1.0.0
