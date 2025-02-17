##  Python Assignment

### Objective

To design and implement solutions using python code using python packages such as requests, psycopg2 etc.
Raise pull request in your github branch and share with us for review.

### Scenario 1

Design a python solution to extract data from an API endpoint and load it into postgresql database.

---

### Tasks
1. Pick any API from here: https://github.com/public-apis/public-apis
2. Implement python code with classes, constructors and methods.
3. Focus on coding style, structure, performance and best practices.

**Reference Material**

* Understanding APIs: https://seattledataguy.substack.com/p/from-basics-to-challenges-a-data
* Python API Tutorial: https://realpython.com/tutorials/api/
* https://pypi.org/project/psycopg2/
* https://pypi.org/project/requests/

---

### Scenario 2
Design and Implement Webserver Log Parser and Calculate reporting metrics

### Tasks
1. Implement log parser for apache webserver logs, sample logs available here: https://github.com/elastic/examples/blob/master/Common%20Data%20Formats/apache_logs/apache_logs
2. Extract information from logs such as IP address, timestamp, HTTP Method, URL Path, Status code, Browser, OS and agent. Load this info to postgresql database.
3. Write SQL queries to answer following questions:

    a. Total Number of requests.

    b. Number of unique IP Addresses.
    
    c. TOP 10 most frequent IP addresses.
    
    d. Top 10 most requested URL paths.
    
    e. Busiest hour of the day(based on number of requests)

**Reference Material**

1. Understanding Webserver logs: https://www.sumologic.com/blog/apache-access-log/ or https://sematext.com/blog/apache-logs/
2. Learning Github: https://www.freecodecamp.org/news/git-and-github-for-beginners/ and https://www.freecodecamp.org/news/git-and-github-crash-course/


### Bonus Material
https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/
