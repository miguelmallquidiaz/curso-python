# SpringCourseManagerApi

This project is an API developed using Spring Boot that manages students, professors, enrollments, and courses.

## Languages and Tools:
<p>
  <img src="https://www.vectorlogo.zone/logos/springio/springio-icon.svg" alt="spring boot" width="40" height="40"/> 
  Spring Boot: Is a framework used to develop Java applications quickly and easily, simplifying the creation of web applications and APIs.
</p>
<p>
  <img src="https://www.vectorlogo.zone/logos/mysql/mysql-official.svg" alt="mysql" width="40" height="40"/> 
  MySQL: Is a relational database management system used to store and manage data.
</p>
<p>
  <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> 
  Postman: Is a tool used to test APIs, allowing you to make HTTP requests and verify responses.
</p>
<p>
  <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> 
  Git: Is a distributed version control system used for tracking changes in source code and collaborating on software development projects.
</p>

## Scrum Information
- Duration: 2 weeks
- Current Sprint: Spritn 1

## EndPoints:

| Method | Route                      | Description                            | Sprint      |
| ------ | -------------------------- | -------------------------------------- | ----------- |
| POST   | /api/student               | Register a new student                | Sprint 1    |
| GET    | /api/student               | Get all students                      | Sprint 1    |
| GET    | /api/student/{id}          | Get details of a student by ID        | Sprint 1    |
| PUT    | /api/student/{id}          | Update details of a student by ID     | Sprint 1    |
| DELETE | /api/student/{id}          | Delete a student by ID                | Sprint 1    |
| POST   | /api/professor             | Register a new professor              |             |
| POST   | /api/enrollment            | Register a new enrollment             |             |
| DELETE | /api/enrollment/{id}       | Delete an enrollment by ID            |             |
| GET    | /api/enrollment            | Get all enrollments                   |             |
| POST   | /api/course                | Register a new course                 |             |
| GET    | /api/course                | Get all courses                       |             |
| GET    | /api/course/{id}           | Get details of a course by ID         |             |
| PUT    | /api/course/update/{id}    | Update details of a course by ID      |             |
| DELETE | /api/course/{id}           | Delete a course by ID                 |             |


