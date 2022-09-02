# Vendée Globe 


![vendee_globe_logo](https://user-images.githubusercontent.com/98779723/186888333-b800131f-8713-4bc0-a199-22d76a705ad9.jpg)

[Live link](https://app.powerbi.com/groups/me/reports/2318ef68-6d39-4b51-9e54-bb0528cd20d3/ReportSection?ctid=cf36141c-ddd7-45a7-b073-111f66d0b30c)


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
    1. [Architecture] (#Architecture)
    2. [Languages](#languages)
    3. [Frameworks & Tools](#frameworks-&-tools)
4. [Testing User Stories](#validation)
    1. [Live tracking](#performing-tests-on-various-devices)
    2. [Ranking](#browser-compatability)
5. [Credits](#credits)
6. [Acknowledgements](#acknowledgements)

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

### Architecture

The architecture chosen is illustrated below
![Architecture_Databricks](https://user-images.githubusercontent.com/61182631/188172942-90834541-a6e1-42a9-9425-d612470b5d25.jpg)

### Languages
- Python
- SQL

### Frameworks & Tools
- Azure Stream Analytics
- Databricks
- Power BI




## Testing User Stories
While testing user stories we want to ensure that we meet the the requirements and expectation of the target audience.

### Live Tracking 
As a user I want to be able to see the positions of the boats.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Map | Navigate to the Tracking tab in Power BI | Live locations of the boats | Works as expected |


<details><summary>Screenshots</summary>
![tracking](https://user-images.githubusercontent.com/98779723/187908441-093b5685-af68-4149-a7c6-26215d9c3de6.png)
</details>

### Ranking
As a user I want to know what the ranking is.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Map | Navigate to the Ranking tab in Power BI | Live locations of the boats | Works as expected |


<details><summary>Screenshots</summary>
![ranking](https://user-images.githubusercontent.com/98779723/187908687-dbc3fa22-01d3-4221-bac6-f4e39a50ab18.png)

</details>


## Credits

### Code
We have written the code by ourselves but took inspiration and examples from:
- Google
- Youtube Tutorials
- Stack Overflow



## Acknowledgements
We would like to thank Techionista Academy that provided us with this challenging project and Avanade.
