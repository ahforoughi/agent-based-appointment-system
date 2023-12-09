

<h1>WellBook: Agent-Based Appointment System</h1>

<p>
An Appointment system for students of the University of Calgary
</p>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-overview">Project Overview</a></li>
        <li><a href="#key-benefits">Key Benefits</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#database-creation">Database Creation</a></li>
        <li><a href="#agent-description">Agent Description</a></li>
        <li><a href="#prosody-im">Prosody IM</a></li>
      </ul>
    </li>
    <li>
      <a href="#test-agents">Test Agents</a>
    </li>
    <li>
      <a href="#run-project">Run Project</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Project Overview:

In response to the healthcare challenges faced by students in Canada, our project introduces a centralized appointment system for international students who are far from their support networks. Our system aims to alleviate this burden by providing a reliable and accessible platform for scheduling appointments, catering to the diverse mental and physical health needs of students.

### Key Benefits:

By implementing this centralized appointment system within the university's student wellness center, we seek to empower students to focus on their studies and personal growth without the added worry of accessing healthcare services. This initiative represents a crucial step toward improving the healthcare landscape for students, fostering a supportive environment for academic success and well-being.




### Built With

This section lists any major frameworks/libraries used in this project. 

* Spade 
* Vue.js 
* FastAPI 
* SQL Alchemy 

<br>


<!-- GETTING STARTED -->
## Getting Started

In order to run the project, follow the instructions below.

### Prerequisites

First, we need the **python version 3.7** or lower to run spade, and create a virtual environment for our project.
```sh
python3.7 -m venv $spade 
source spade/bin/activate
```

To install the requirements of this projects we created a `requirements.txt` file. Run the code below to install the requirements.

```sh
pip install -r requirements.txt 
```

### Database Creation
in order to run the project, we must first create our dataset.
Our database consists of 3 tables.
1. **Patient**: This table contains the personal information of each patient like first name, last name, and phone number.

2. **Doctor**: This table contains the personal information of each doctor along with their specialization and availability.

3. **Appointment**: This table contains the information of each appointment set for a specific doctor and patient with the date and time of it.

Now in order to insert data to the dataset we need to run the code below.

  ```sh
  python3.7 ./models/data_generator.py
  ```


### Agent Description
Our system consists of ***5*** agents: client, register, login, scheduler, and email generator.

1. **Client Agent**: This agent is responsible to be the interaction point for users and also interacts with with other agents to retreive information.

2. **Register Agent**: The Registration Agent, upon communication from the Client Agent, verifies that the provided user does not pre-exist in the database; if not, the Registration Agent initiates the creation of a user record in the database.

3. **Login Agent**: This agent checks the user data shared by the Client Agent to see if the user exists in the database and is eligible to login.

4. **Scheduler Agent**: The Scheduling Agent checks with the Appointments database and collects all the available appointments for the selected doctor with date and time from the Client Agent. 

5. **Email Generator Agent**: The Email Service Agent sends a confirmation email to the user, affirming the scheduled appointment. Also, it will send a reminder to the user within 24 hours before the appointment.


### Prosody IM
Prosody is a modern **XMPP** communication server. It aims to be easy to set up and configure, and efficient with system resources. To install it, we have to run the code below.

```sh
sudo apt install prosody
```

We have to create it before building our first agent as a server to have connection between our agents. Run the code below for each agent that is created.

```sh
sudo prosodyctl register $AGENT_NAME $HOST $PASSWORD
```

## Test Agents
To see if the agents are working fine, we can run the `main.py` file. For each agent we defined a specific flag as follows:

**Register**
```sh
python3.7 main.py --register $username $password $phone $first_name $last_name $address
```

**Login**
```sh
python3.7 main.py --register $username $password 
```

**Schedule**

Get All Appointments
```sh
python3.7 main.py --get_appoinments_times all
```
Get Appointment Info
```sh
python3.7 main.py --get_appoinments_times $appointment_info
```

## Run Project
Finally, in order to run the project just run the code below.

```sh
uvicorn api:app --reload
```

After running the web server we must run the vue.js code for our frontend to run. 

```sh
cd frontend/
npm install
npm run
```
