# events-app-tkinter-mysql

An example conference schedule app built using the tkinter module in python. Uses the mysql-connector driver for python.

![Screenshot](docs/screen.png)

## Prerequisites

1. Python 3

2. MySQL Server

3. mysql connector driver for Python

    ```sh
    # install via pip or pip3
    pip install mysql-connector
    # or from here https://dev.mysql.com/downloads/connector/python/
    ```

## Steps to Run

1. Import the database

    ```sh
    mysql -u root -p < data.sql
    ```

2. Run the project

    ```sh
    python main.py # or python3 depending on your install
    ```
