# Comercio
We present Comercio, a live order matching application that can be used for trading of different financial securities.

# What it is
The live market simulation is at the heart of the Comercio trading application. 

It simulates a real time stock exchange, with true to life trends in the bid prices with the sole aim of emulating real world demand-supply. The application houses a  random order generator which  generates new orders intelligently, that can be traded and matched by the system. 

There are several customisable and adjustable attributes of an order that the user places like type (market or limit), bid price and quantity. Volatility checks are performed on these orders regarding the tick size of 0.05 and the circuit checks which reject orders which vary more than 10% compared to the last traded price.

# Structure
A MySQL database is used to store these orders into appropriate tables. The database maintains these following tables:

* Securities Table,  a table that holds the attributes of a security in the market.

* Orders Table, which holds all the orders generated through the application.

* Manual Orders Table, a table which contains all the manual orders placed by the user.

* My Portfolio Table, this table holds the amount of the various securities owned by the user.

* Rejected Orders Table, contains all the orders that did not pass the circuit checks.

A live feed of all these tables is provided at various points in the Comercio application. 

# Requirements:
* Operating system: Windows 7/8/10, MacOS, Linux.

* MySQL Community Server 8.0.21 or later, Download.

*Python v3.8.5 or later, Download.

* Node.js v12.18.4 or later, Download.

# Installation Instructions:
* Clone this repo.

* Open a terminal, navigate to order_matching_system\backend

* Run pip install -r requirements.txt

* Open a terminal, navigate to order_matching_system\frontend

* Run, npm i

# To Run:
* Open a terminal and navigate to order_matching_system\backend and run the command flask run.

* Open another terminal and navigate to order_matching_system\frontend and run the command npm start.

