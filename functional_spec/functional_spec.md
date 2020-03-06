

# BetterTimetables - Functional Specifications

## 0. Table of Contents


- [1. Introduction](#1-introduction)
  * [1.1 Overview](#11-overview)
  * [1.2 Glossary](#12-glossary)
    + [React](#react)
    + [SQL](#sql)
    + [Flask](#flask)
- [2. General Description](#2-general-description)
  * [2.1 System Function](#21-system-function)
  * [2.2 User Characteristics and Objectives](#22-user-characteristics-and-objectives)
  * [2.3 Operational Scenarios](#23-operational-scenarios)
  * [2.4 Constraints](#24-constraints)
- [3. Functional Requirements](#3-functional-requirements)
  * [3.1 Serve Web Application](#31-serve-web-application)
    + [Description](#description)
    + [Criticality](#criticality)
    + [Technical Issues](#technical-issues)
    + [Dependencies with other requirements](#dependencies-with-other-requirements)
  * [3.2 Parse Timetables from Legacy System](#32-parse-timetables-from-legacy-system)
    + [Description](#description-1)
    + [Criticality](#criticality-1)
    + [Technical Issues](#technical-issues-1)
    + [Dependencies with other requirements](#dependencies-with-other-requirements-1)
  * [3.3 Search and View Timetable](#33-search-and-view-timetable)
    + [Description](#description-2)
    + [Criticality](#criticality-2)
    + [Technical Issues](#technical-issues-2)
    + [Dependencies with other requirements](#dependencies-with-other-requirements-2)
  * [3.4 Export Timetables](#34-export-timetables)
    + [Description](#description-3)
    + [Criticality](#criticality-3)
    + [Technical Issues](#technical-issues-3)
    + [Dependencies with other requirements](#dependencies-with-other-requirements-3)
- [4. System Architecture](#4-system-architecture)
  * [4.1 Diagram](#41-diagram)
  * [4.2 React App](#42-react-app)
  * [4.3 Flask Server](#43-flask-server)
  * [4.4 Database](#44-database)
- [5. High Level Design](#5-high-level-design)
  * [5.1 High Level Design Diagram](#51-high-level-design-diagram)
  * [5.2 High Level Design Description](#52-high-level-design-description)
- [6. Preliminary Schedule](#6-preliminary-schedule)
  * [6.1 Task List](#61-task-list)
    + [Documentation](#documentation)
    + [Implementation](#implementation)
  * [6.2 Gantt Chart](#62-gantt-chart)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## 1. Introduction
### 1.1 Overview

The system is an online timetable client for DCU students. It is aimed to provide more functionality, ease of use, and accessibility than the legacy timetable system. Both the legacy timetable system and the new alternative are limited in the features that they offer and have quality of life issues for end users. The system aims to allow DCU students to check their timetables with more ease. It will offer many functions which are not present within the legacy systems. With the current system, students cannot bookmark their timetable as the page is fully dynamic. The current system also offers no functionality for students to export their timetable, either as an image, or as a CSV into an external calendar or planner. Both existing systems also suffer from readability issues within the user interface, and the process of viewing a timetable being needlessly convoluted. The new timetable service also suffers badly when viewed on a mobile device.

The legacy timetables also exist in a very esoteric format. Our system aims to remedy this by creating a database. Each time a user requests a new unique timetable, it will be parsed by our server into a common format and added to a database within the system. If a user requests a timetable which we have already parsed, it will simply be presented from the database.

Our system aims to address all these issues while also adding new functionality for users. It will simplify the process of finding a specific timetable down to entering a course code and one click. Users will then be able to view their timetable on a user interface presented by the system. 

The system will also be integrated with the Google Calendar API, allowing users to easily export their timetable for an entire semester into their own personal calendar. 

The system will comprise:
- A web app user client
- A server to parse the legacy timetables
- A database to house the parsed timetables
- A server to host the legacy timetables for testing and demonstration

### 1.2 Glossary
#### React
Framework of the Javascript programming language, used to develop user interfaces and web applications.
#### SQL
Structured Query Language is a standardised language used to create and read from databases.
#### Flask
A framework of the Python programming language used to create web servers and APIs.
#### CSV
A comma-separated values file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. 


## 2. General Description
### 2.1 System Function

*User Functionality*
The user will access the BetterTimetables website through a web browser on a desktop or mobile device. They will be prompted to enter their DCU course code and year of study. The user will then be able to view their timetable on a graphical interface or export it into their personal calendar. The system will also allow exporting in other formats such as images.

*Server Database Interaction*
When a user requests a timetable, the system will run a check to see if the specific timetable requested has been accessed before. If it has not, the system will access the requisite page of the legacy timetable system. It will scrape the data from this page and run it through a general-purpose parsing algorithm. This will return CSV data representing the timetable. The system will then add this timetable to a relational database on a server. If a timetable is requested which the system has already accessed and parsed, it will be presented directly from this database.

*Note on scraping*
Due to permissions issues, and to avoid making excessive numbers of requests to DCU servers, we will be working from a subset of the legacy timetables for testing and demonstration purposes. These will be hosted on a server of our own creation. They will be the exact HTML files served by the legacy timetables. The aim of this is to show that the legacy timetables URL could be plugged in to the system and it would remain fully functional.

*Google Calendar Integration*
The Google Calendar API will be used to allow users to export their timetable to their personal Google account. The API can receive CSV data and add it to a user’s account. The user will enter their personal or student Google account information and the system will export their entire semester directly into their calendar. This allows users to not have to rely on accessing and navigating a specific website daily just to view their timetable.


### 2.2 User Characteristics and Objectives
The user community will essentially fit a single definition – DCU students. We can assume a reasonable level of technical literacy from this user group but will still be emphasising simplicity and usability within the system. 

The amount of interactions with the system available to the user will be quite limited. As a result, using the system should be very straightforward. We can also assume that DCU students are used to (but not necessarily satisfied with) the experience of using both the legacy timetable platform and the Open Timetables alternative. With this information in mind, we can simply aim to make BetterTimetables more straightforward and simple to use than both pre-existing options.

### 2.3 Operational Scenarios

*View Timetable*
The user will enter their course code and year and select the option to view the timetable. The graphical user interface will be presented to the user with their timetable. If the user enters an invalid year or course code they will be prompted to do so again.

*Export Timetable*
The option to export timetable will be presented both as an alternative to viewing it, and as an option on the viewing screen. The user will choose to export as an image, CSV, or using Google Calendar. Image or CSV will prompt a download of the requisite file. Choosing Google Calendar will call a secure Google Calendar portal where the user can enter their credentials and then import the data into their account. This portion of the system will be handled by the Google API.

### 2.4 Constraints
*Time Constraint*
The final implementation deliverable has a due date for DCU. This is the 6th of March 2020. This means all schedules will be composed around completing the entire system and all documentation by this date.

*Scraping*
Due to permissions issues, and the fact that the testing and demonstration process will involve excessive amounts of scraping requests, we will be using a server of our own creation to host a subset of the legacy timetables, which are publically available. The aim of this is to be functionally identical to scraping off the actual timetable server, and to show that the correct URL could simply be plugged in to the system.

## 3. Functional Requirements

### 3.1 Serve Web Application

#### Description
The system will serve a graphical front-end for users to interact with it. This will be presented in the form of a ReactJS web application.

#### Criticality
Essential.

#### Technical Issues
The web app should communicate effectively with the Flask server.

#### Dependencies with other requirements
This requirement is a dependency of all other requirements.


### 3.2 Parse Timetables from Legacy System
#### Description
When a specific timetable is requested for the **first time**, it must be run through a parsing algorithm to convert it from esoteric to common format (CSV). The system must then add the timetable to a database. If a timetable has been requested before, it will be presented from the database.

#### Criticality
Essential.

#### Technical Issues
Ensure consistency within the database. Ensure timetables are parsed correctly and added to database if not already present.

#### Dependencies with other requirements
This requirement is a dependency of **3.2** and **3.3**.



### 3.3 Search and View Timetable
#### Description
Users should be able to input their course code and year in a straightforward user interface. They should be able to then view their timetable on a graphical interface within the application.

#### Criticality
Essential.

#### Technical Issues
The system needs to run a check to see if the specific timetable has been requested before. If it has not, it must be parsed from the legacy timetables and added to a database. If it has, it must be presented directly from the database.

#### Dependencies with other requirements
Depends on **3.1 Serve Web Application**.
Depends on **3.2 Parse Timetables from Legacy System**.


### 3.4 Export Timetables
#### Description
Having searched for their timetable, users should be able to export it. The bulk of this requirement is the ability to export to Google Calendar. Other formats such as PNG or CSV may also be desirable.

#### Criticality
- Google Calendar: Essential
- Other formats: High

#### Technical Issues
Google Calendar API calls must be integrated into the system. Extra complexity associated with this, but important to keep things straightforward for the user.

#### Dependencies with other requirements
Depends on **3.1 Serve Web Application**.
Depends on **3.2 Parse Timetables from Legacy System**.

## 4. System Architecture

### 4.1 Diagram

![](https://i.imgur.com/vAj7weH.png)



**Fig 4.1** shows the three primary aspects of the system architecture. The first is the user-facing front end, which will be a React app. This will communicate with both of the other components. The first of these is a Flask Server/API, where the logic to parse the legacy timetables and populate the database will be contained. The second is the database itself. Calls will also be made to the Google Calendar API, however this is not a primary component of the system. An external web server will also be used for testing and demonstration purposes. 

### 4.2 React App
The user-facing component of the system will be a React web app. It will comprise a simple user interface where students can enter their course code and year of study. They will then be prompted to either view their timetable within the web application or immediately export it to Google Calendar or other formats. The React app will make calls to the **Flask Server** which will be parsing the timetables or serving them straight from the **Database** as required.

### 4.3 Flask Server
The backend of the system will be mainly handled by the Flask server. This will be where the logic is housed which scrapes and parses the legacy timetables into a common CSV format. It will also be storing previously requested timetables in the **Database**. 

### 4.4 Database
The CSV timetables fetched by the **Flask Server** will be housed in a relational SQL database. This will allow for less workload when fetching previously requested timetables.

## 5. High Level Design

### 5.1 High Level Design Diagram
![](https://i.imgur.com/UvknQNB.png)


### 5.2 High Level Design Description
- **Search for timetable**
Enter a course code and year of study in the requisite text fields to request a timetable.

- **Request unique timetable**
The process of requesting a timetable which has not previously been accessed. Must be parsed from the legacy timetables and entered into the database.

- **Request previously viewed timetable**
Presented directly from the database.

- **View timetable on graphical interface**
Users can use the web application to browse their timetable graphically.

- **Export timetable to Google Calendar**
Call the Google Calendar API and allow users to import the timetable into their personal schedule.

- **Export timetable in other formats**
Allow users to export their timetable in PNG, CSV formats.

## 6. Preliminary Schedule

### 6.1 Task List
#### Documentation
- Proposal
- Functional Specifications
- Technical Specifications
- User Guide
- Blog
- Video Walkthrough

#### Implementation
- React Client
- Flask Server and API
- Relational Database
- Client Server Communication
- Server Database Communication
- External Server to host test legacy timetables

### 6.2 Gantt Chart

![](https://i.imgur.com/escsOX8.png)








