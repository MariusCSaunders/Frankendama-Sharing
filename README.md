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

Create:
User can create a Frankendama made from 5 parts.

Read:
User enters the homepage where all the builds are availible in a table to read.

Update:
User has an update button on the same row as the entry needing updated.

Delete:
User has a delete button on the ame row as the entry needing deleted.


## Architecture

### Risk Assessment
My Risk Assessment for this project can be seen below, it has a list of risks that the project may have and has an assigned Risk/Impact value.
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/RiskAssessment3.png" alt="Risk Assessment"/>
As you can see as the project went new risks were discovered and I therefore added a date column.

### Trello Board
The way i documented the progress of my project overall was to use a Trello Board.

Since the project is small scale and it has a more visual representation of progress i decided Trello was better to use over other tools such as Jira.
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/UserStories.png" alt="User Stories"/>
My full trello Board can be found <a href="https://trello.com/b/L9cnnpHA/user-story-qaproject">here</a>


### Entity Relationship Diagram

My outdated ERD can be seen below, followed by the updated version.
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/QAprojectERDdraft1.png" alt="Old ERD"/>
<br/>
My original ERD was a Many-toMany relationship-diagram which is not suitable for this project so i remade the ERD as follows:
<div style="block;"> 
<img src="https://github.com/MariusCSaunders/qa-individual-project/blob/master/images/QAprojectERDdraft22.png" alt="ERD Image"/>
This is the current ERD for this project.

Each Frankendama will have the 5 main parts for a build and each Frankendama has many companies assosciated to the full build.

### Analysis of Testing
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
