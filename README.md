# Restaurant Reviews




## *App Design:
I created a restaurant reviewing application, where users can access the homepage and add a restaurant to be reviewed by others, and/or  add their own review, which can be either updated or deleted. 

Users are prompted to click one of three links:
 * Home 
 * Make a new review
 * Add a new Restaurant

Once they have added a review, their review will be displayed on the homepage, along with an update button and a delete button. At the bottom of the page, the name and cuisine type of all restaurants that are in the database are shown.
 
#### Equity Relationship Diagram:
<img width="771" alt="Screenshot 2022-03-08 at 00 12 48" src="https://user-images.githubusercontent.com/99325840/157140102-b6b9c18b-2ddd-48de-8dbe-2d561e572c81.png">

To make my application, I needed a restaurants table and a reviews table. They have a one to many relationship between them as one restaurant can have many reviews about its food, whereas every review is referencing just one restaurant. I began with the ERD shown above, however, I made some changes to mine on day 3 of my project. I realised that the lengths of my fields was not suitable for my application, as 100 characters was too much for restaurant name and cuisine type, whilst 100 was too small for the body of someones review. I thus changed these lengths amd also added in my module validators so that I could use this table as a visual aid during development.

<img width="762" alt="Screenshot 2022-03-09 at 16 19 01" src="https://user-images.githubusercontent.com/99325840/157501000-c18498f8-790f-42a0-87e2-74c9cc1e34cf.png">


## *Planning:
### Day 1:
<img width="663" alt="JIRA Day 1" src="https://user-images.githubusercontent.com/99325840/157138738-03f7f315-9fa6-4cf6-b115-5d8b6e242c3d.png">

On day one of  beginning my project, I have created a kanban style board on Jira software. This visually depicts my workload at a glance and allows me to keep track of what has already been done and what is to do. I have split my ToDos into several sections. The first were the minimum viable product requirements that were needed for me to pass the project. I wanted these seperate as they were the most important tasks for me to consider. I also had User Stories, which helped me build my application by thinking in the eyes of the end user. I also had inprogress and done sections, which were not populated at this point in time.

### Day 3:

<img width="1425" alt="Screenshot 2022-03-09 at 16 46 42" src="https://user-images.githubusercontent.com/99325840/157779928-44ab69e1-8a01-4ae0-895c-6bc73f3f352a.png">


The visualisation of workload has allowed me to spot bottlenecks where they would potentially occur,for example, I had realised that I may not have much time to complete the testing and Jenkins sections of the project if I did not move at a faster pace.


## Final Day:

<img width="1158" alt="Screenshot 2022-03-11 at 01 48 20" src="https://user-images.githubusercontent.com/99325840/157786446-70408b92-5a4e-4a4f-8915-d26c37371a92.png">


## *CI Pipeline

<img width="409" alt="Screenshot 2022-03-09 at 17 43 02" src="https://user-images.githubusercontent.com/99325840/157500633-0830e397-f524-47ae-b990-61e5f5449816.png">
The purpose of the CI pipeline approach is to allow developers to integrate new code easily and continuously.

 I have demonstrated the usage of a CI pipeline in this project. Firstly, I begin by finding my ToDo tasks on my Jira board, followed by working on my application in python via visual studio code. When new features are made, id commit and push them to a remote repository using Git. This code is then automatically pulled, tested and deployed by a Jenkins server via a webhook, triggered by code commits in the version control repository or when prompted to run. Any test failures/issues can be seen in the Jenkins Console Output. 


## *Risk Assessment:

<img width="757" alt="Screenshot 2022-03-08 at 00 12 28" src="https://user-images.githubusercontent.com/99325840/157140053-385c7258-c166-47d9-9194-9ca1fa33274e.png">

As my project started coming along, I started to notice more and more potential risks which could be associated with my application, so I began to add those in to my risk assessment. I also realised that visually, having them listen in bullet points was not very engaging, and that there was no way of rating the severity each risk could have, thus prompting me to put my risks into a matrix style with numeric values for severity.

<img width="1162" alt="Screenshot 2022-03-11 at 01 02 32" src="https://user-images.githubusercontent.com/99325840/157782592-204bbe46-94e5-43c6-b3a4-9d5767a94329.png">


## *Testing

U
 I sought out to test the GET requests for all of my create, read, update and delete routes, as well as the POST requests for create and update routes, which led me to achieve 84% coverage initially. After further analysing which lines of code were not being excecuted by the tests, I realised that I had a lot of useless lines of code within my application, which I got rid of thus making my routes much easier to read and increasing my test coverage. 
 <img width="632" alt="Screenshot 2022-03-11 at 00 56 38" src="https://user-images.githubusercontent.com/99325840/157782510-ae751b02-c16b-493c-83c2-b595ad060670.png">




## **Known Issues/Areas Of Improvement**
* Individuals cannot delete/update restaurant entries that they make
* More time and attention could have been taken to making the website look visually more appealing
* Next time, I could perhaps add a 'search' route, so that they can search for a review by keyword
