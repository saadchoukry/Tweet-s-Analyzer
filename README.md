
<p align="center">
  <img src="https://github.com/saadchoukry/Tweet-s-Analyzer/blob/master/static/images/Tweets_analyzer.png?raw=true">
</p>

This repository contains the source code of a twitter analysis solution. It consists of using a graph-oriented database to design and build a tweet's analysis solution. Its main functionalities are:
  - Collect data from Tweets 
  - Analyze and process the data using a graph-oriented database
  - View/visualize the results

## Data Model
Once the data has been collected, we obtain a JSON format file that must be used to generate the graph associated with the research.
The diagram below represents the model that was defined in order to perform this task:

<p align="center">
  <img  src="https://media.discordapp.net/attachments/616373618976358563/790170637830062090/NEO_SCHEMA.png?raw=true">
</p>

## Requirements
```
pip install requirements.txt
```

## Running the project
Tweet's Analyzer visualizations are made using chartJs and django, to start the server, execute the following command:
```
python manage.py runserver
```
