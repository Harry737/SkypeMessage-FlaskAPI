# Project Title and Description
Skype Message Flask API

Skype Message is a project that allows users to send automated messages on Skype using a Python script. It provides both a command-line interface and a Flask web application.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/username/repo/blob/master/LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/username/repo/releases)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/username/repo/actions)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Overview](#project-overview)

## Installation
To install the project and its dependencies, follow these steps:

1. Clone the repository: `git clone https://github.com/Harry737/SkypeMessage-FlaskAPI.git`
2. Navigate to the project folder: `cd SkypeMessage-FlaskAPI`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage
The project provides two ways to send automated Skype messages: a command-line interface (CLI) and a Flask web application. 

### Command-line Interface (CLI)
To send a message using CLI, run the following command(set the skype credentials before running the application, then print or debug the chats and update the _chat_id variable also, the id of the person or group you want to send message):

```shell
python skypeMessage-python.py
```

### Flask Web Application
To run the Flask web application, execute the following command:

```cmd
set FLASK_APP=skeypMessage-flask.py
python -m flask run --host=0.0.0.0
```

```shell
export FLASK_APP=skeypMessage-flask.py
python -m flask run --host=0.0.0.0
```

Open your web browser and navigate to `http://localhost:5000/api/SendMessage?email=test@mail.com&password=test@%23123&groupid=8:live:.cid.dfs34...&message=Test123`. You must specify your skype email, skype password, group or chat id you fetched by first running python app & message to be sent.

## Project Overview
The project files are organized as follows:

- `skypeMessage-python.py`: This script provides the command-line interface for sending Skype messages.

- `skypeMessage-flask.py`: This script defines the Flask web application for sending Skype messages through a web interface.

- `requirements.txt`: This file contains the list of required Python packages and their versions.

- `Dockerfile`: This file is used to build a Docker image for the Flask web application.

- `assets/`: This directory contains example assets used in the project.

- `README.md`: This file is used to explain the details of this application.