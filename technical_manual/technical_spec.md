# BetterTimetables - Technical Specification

## 1. Introduction
### 1.1 Overview
The system is an online timetable client for DCU students. It is designed to provide more ease of use, functionality, and accessibility than the legacy timetable system. Both the legacy system and the new alternative timetable system are limited in the feature that they offer and have quality of life issues for end users. The system allows DCU students to check their timetables with more ease. It offers functions which are not present within the legacy or newer timetable systems. Both existing systems also suffer from readability issues within the user interface, and the process of viewing a timetable is needlessly convoluted. 

The legacy timetables also exist in a very esoteric format. Our system remedies this by creating a database. Our server updates the database once every 24 hours.

Our system addresses these issues while also adding new functionality for users. It simplifies the process of finding a specific timetable down to entering a course code, year of study and the semester. Users are then able to view their timetable on a user interface prevented by the system, without any page redirection. The system stores the form information locally, and so users are able to bookmark their timetable and be able to revisit it at any time.

Our system also allows users to refine what they are searching for in the timetable. It allows users to filter by day, or by timetable object type.

The system is comprised of:
- A web app user client
- A server to parse the legacy timetables
- A database housing the parsed timetables
- A server hosting the legacy timetables for testing and demonstration

### 1.2 Glossary
#### React
Framework for the JavaScript programming language, used to develop user interfaces and web applications.

#### SQL
Structured Query Language is a standardised language used to create and from databases.

#### Flask
A framework of the Python programming language used to create web servers and APIs.

#### JSON
JavaScript Object Notation, a way of storing text that is readable by humans which describes data objects. This can be passed to many programming languages and interpreted by the program.

#### WCAG
The Web Content Accessbility Guidelines are a set of recommendations for making Web content more accessible, primarily for people with disabilities, but also for all user agents, including highly limited devices, such as mobile phones.

#### CSV
A comma-separated values file is a text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by comams.

#### API
An Application Programming Interface is a set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service.

## 2. System Architecture
### 2.1 Diagram
![](https://i.imgur.com/xGIDbM6.jpg)

**Fig 2.1** shows the three primary aspects of the system architecture. The first is the user-facing front end, which is a React app. This communicates with the Flask server. The Flask server contains the logic to parse the legacy timetables and populate the database. The React app sends a request to the Flask server, which gets the requisite timetable data from the database and sends it back to the React app. An external web server is used for testing and demonstration purposes.

### 2.2 React App
The user-facing component of the system is a React web app. It comprises a simple user interface where students enter their course code, year of study and semester. They are then shown the timetable they requested, if it exists in the database. If it does not, the React app returns an error message which indicates that the **Flask Server** was unable to find the timetable they requested in the database, it then prompts them to check the information they passed and to try again. Upon successfully retrieving a timetable, the user is given the option to filter their timetable by day and timetable object type, i.e. lecture, practical, tutorial.

### 2.3 Flask Server
The backend of the system is mainly handled by the Flask Server. This is where the logic is housed which scrapes and parses the legacy timetables into a common JSON format. Dynamic API routes are configured which allows the **React App** to fetch data from the Flask Server, which in turn pulls data from the SQLite relational database. The Flask Server is also responsible for updating the database using a special API request. This call could be managed by i.e. a cron job every 24 hours to update the timetables from the legacy site.

### 2.4 Database
The JSON timetables fetched by the **Flask Server** are housed in a relational SQLite database. Timetables are organised in the database by course code, year and semester, with each row also containing the JSON representation of the timetables which can be passed back through the **Flask Server** to the **React App**. 

### 2.5 Testing
#### 2.5.1 Continuous Integration

![](https://i.imgur.com/cB9SwXH.jpg)

#### Lint
Early on, we implemented a linting stage in our continuous integration pipeline. This allowed us to catch any errors, unused variables etc in the frontend component of the system, and conform to the semantic standards we decided on. We opted to use eslint for the linting process.

#### Test
The test stage runs our test suite for the Python backend. Methods and functions used by the Flask Server are tested automatically whenever a commit is pushed.

#### Build
Later on, we also added a simple build stage that simply executes `npm run build` on the frontend portion of the system. This lets us know whether the React App is building correctly using npm.

##### 2.5.2 User Testing
Considering that accessibility and readability were among the chief focuses of our project, we carried out extensive user testing to ensure that our project was usable by a wide audience. Once the major components of the user interface were completed, we presented it to fellow students for testing. We surveyed students from DCU only, as the timetable is aimed to upgrade on DCU's timetabling system. The feedback from these students helped us to ensure that we were providing a service that was easy to use by all students, not just those with a foundation of technological knowledge.

#### 2.5.3 Accessibility Testing
Although User Testing may have gathered some requirements for accessibility testing, it was essential that we also conform to the Web Content Accessbility Guidelines (WCAG). Testing for WCAG compliance was carried out using different accessibility testers on different browsers. On Chrome we used a plugin called Axe which integrated with the development tools and reports on any accessibility issues detected. To further this testing we also utilised Firefox's built in accessiblity tester, which covered the same basis as Axe.

## 3. High-Level Design
### 3.1 High Level Design Diagram
![](https://i.imgur.com/i6eA8AK.jpg)

### 3.2 High Level Design Description
* **Search for Timetable** Enter a course code, year of study and semester into the input fields to request a timetable
* **Request Timetable** The process of requesting a timetable from the Flask server. The Flask server retrieves the requested timetable from the database.
* **View Timetable on Graphical Interface** Users can use the web application to browse their timetable graphically
* **Filter Resultant Timetable** Users can choose to only see specific elements of their timetable, such as by day or by type.

## 4. Problems and Resolution
### 4.1 CSV to Table not working
#### Problem
We had initially found a React library which would take CSV input and convert it into a table. However, the installation of this library went awry, and we had to find an alternative solution for displaying the timetable in an easily readable manner. 
#### Solution
To resolve this issue we decided not to rely on a library and to instead build our own function which would instead take JSON objects and output those into a table which we formatted ourselves.

### 4.2 Google Calendar API integration
#### Problem
In our initial project proposal we had stated that we would integrate the Google Calendar API. However, we underestimated the time needed to implement this feature, and were somewhat behind schedule until close to the project deadline.
#### Solution
We eventually had to remove the planned feature from the project and instead focus on implementing other features that were lacking from the existing timetable systems, such as display filtering options. We estimate that if we had one extra week to work on the project we would have been able to implement it. In future projects, we will have to strive to stay more on schedule with our implementation phase.

## 5. Deployment
### 5.1 Manual Deployment
#### 5.1.1 Dependencies
The following libraries/programs must be installed for the application to work:
##### General Dependencies
* npm
* python3

##### Pip Dependencies
* Flask
* Flask-SQLalchemy
* BeautifulSoup 4
* Requests

#### Installing build dependencies
```
pip install Flask Flask-SQLAlchemy beautifulsoup4 requests
npm install
```

#### 5.1.2 Obtaining source code
Git clone through https:
```
git clone https://gitlab.computing.dcu.ie/henryo3/2020-ca326-ohenry-bettertimetables.git; cd 2020-ca326-ohenry-bettertimetables
```

#### 5.1.3 Build the Web-App
From the top-level directory:
```
cd bettertimetable-app
npm install
npm start
```
This will open the Web-App on port 3000, which can be accessed in a browser at:
```
localhost:3000/
```

#### 5.1.4 Run the Server
From the top-level directory:
```
cd python
python3 server.py
```
This will open the Flask server on port 5000, which can be accessed in a browser at:
```
localhost:5000/
```

The database is contained within the `python` folder and is addressed directly from `server.py`. The server should automatically address the correct path to the database using your operating system's path.
