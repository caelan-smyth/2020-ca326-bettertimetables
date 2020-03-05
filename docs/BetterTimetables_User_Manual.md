# BetterTimetables User Manual
## 0. Table of Contents
- [1. Overview](#1-overview)
- [2. Searching for a Timetable](#2-searching-for-a-timetable)
- [3. Retrieving the Timetable](#3-retrieving-the-timetable)
- [4. Timetable Display Filtering](#4-timetable-display-filtering)
  * [4.1 Filtering by Day](#41-filtering-by-day)
  * [4.2 Filtering by Type](#42-filtering-by-type)
  * [4.3 Filtering by Day and Type](#43-filtering-by-day-and-type)


## 1. Overview
This web-app is intended to be used as a substitute for DCU's currently offered timetable services. The aim of this web-app is to provide a more widely accessible and easier to use version of the timetable services.

## 2. Searching for a Timetable
To search for a timetable, a user must fill out three fields on the following form:
![](https://i.imgur.com/Ijje0tI.png)
The Programme Code is the same code used to search the currently offered timetable services (e.g. Computer Applications and Software Engineering = CASE).
The Year of Study is the current year that you are in, in the range 1-4.
The Semester is the semester for which you are trying to view the timetable. This can be selected from a drop-down menu within the form.
![](https://i.imgur.com/J79eqkV.png)
The Search button then sends a request to the server and gets back the relevant timetable.
Below is an example of the form with data filled in.
![](https://i.imgur.com/XSH27in.png)

## 3. Retrieving the Timetable
When the form is filled in and the user clicks the search button, the application tries to retrieve the timetable. If it is successful, a screen like this will appear.
![](https://i.imgur.com/ePQYSBZ.png)
On the timetable, the items in blue are practical slots such as labs, the items in pink are lectures, and the items in orange are tutorials.

If the application cannot find the timetable requested, an error like this will show up:
![](https://i.imgur.com/YawQiVf.png)
This error either means that one of the form fields was filled out incorrectly, or that the specified course timetable is not contained within the database. If it is the former, simply re-enter the form information. If it is the latter, the database is updated once every 24 hours, and should contain the timetable within 24 hours.

## 4. Timetable Display Filtering
Once the timetable has been retrieved, there are options to filter down what the timetable displays.

### 4.1 Filtering by Day
This is a drop-down menu which, upon selection, allows the user to just show the selected day's timetable entry.
![](https://i.imgur.com/25TyAAs.png)

When the day is selected, the timetable will look something like this:
![](https://i.imgur.com/TzfmCvI.png)

### 4.2 Filtering by Type
This is a drop-down menu which, upon selection, allows the user to just show timetable entries of the selected type (e.g. lecture).
![](https://i.imgur.com/tT91Pd5.png)

When the type is selected, the timetable will look something like this:
![](https://i.imgur.com/StJnyvT.png)

### 4.3 Filtering by Day and Type
The application allows users to filter by day and type simultaneously. If the user just wants to see lectures on Monday, the timetable will look something like this:
![](https://i.imgur.com/ZfQLRFx.png)
