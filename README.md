# Vendée Globe 


![vendee_globe_logo](https://user-images.githubusercontent.com/98779723/186888333-b800131f-8713-4bc0-a199-22d76a705ad9.jpg)


Project by Hira Zaidi, Valentine Favrod, Helena Mason and Pooja Bhardwaj

### Introduction
The Vendée Globe is a solo non-stop round the world yacht race founded by Philippe Jeantot in 1989. The race takes place every four years and is considered an extreme
quest of individual endurance and the ultimate test in ocean racing. For this race we are building a technology for tracking the boats in real-time so that spectators
can follow the action live on an online racing dashboard.



## Table of Content

1. [Project Goals](#project-goals)
    1. [Challenge](#challenge)
    2. [Goal](#goal)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requrements-and-expectations)
3. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
4. [Features in Power BI](#features)
5. [Testing](#validation)
    1. [Device testing](#performing-tests-on-various-devices)
    2. [Browser compatibility](#browser-compatability)
6. [Bugs](#Bugs)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)

## Project Goals 


### Challenge
For this project we will have to build a cloud based Lambda Architecture to process the telemetry data from the sailing boats. 
The architecture should run in Azure and contain a real-time path for processing sailing boat data in real-time, and a batch-processing path for collecting sailing
boat data in batches and performing calculations on those batches. As this race is not live during our project we will use a Python application that will simulate boat 
telemetry data from a fleet of 10 race participants.


### Goal
The Lambda Architecture should send all boat data to a PowerBI dashboard. The dashboard should display a world map with the current position of each boat, and a table
with a ranking of racing teams. The ranking table should be sorted by who is currently in the lead.


## User Experience



### Target Audience
Our audience are all the people who want to track the participants and follow the contest.

### User Requirements and Expectations
The audience would require to see the exact location of the boat. They would also want to know the ranking of the participants.


## Technologies Used

### Languages
- Python
- SQL

### Frameworks & Tools
- Azure Stream Analytics
- Databricks
- Power BI


## Features in Power BI



## Validation



### Performing tests on various devices 


### Browser compatability



## Bugs


## Credits

### Code




## Acknowledgements
