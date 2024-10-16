# Marinera League #
## The Champions League of Marinera Norteña ##

### Brief context: ###
Marinera norteña is a traditional and competitive dance from Perú - it is a couple-dance. Every weekend competitions are held which judges that evaluate each couple performance. 
It is a tournament type, with different phases and a final where the winner is decided. 

This whole world is quite traditional and there are no good website or platform to see the results. 
Each competition publishes the results in a different way (mainly Excel sheets, PDFs, images) on their facebook pages/ website. All the results are 'static' - not searchable in any way. 

### Problems I want to solve with this project ###

- it's hard to find out the competition result
- it's hard/impossible to find a list of the active dancers and know the results they have
- there is no way to know who are the 'best dancers'

## What I'm building here ##

1. A unified database of all competition results and dancers (SQLite for now)
2. Function website for easy search (flask web app)

## How: ##
### New data input system ###

- input: Excels file published by a competition.
  The Excels are not properly formatted to build a database

Steps: 
* Export each excel sheet to separate .csv with relevant name `process-source.py`
* Pass the csv to an OpenAI assistant to clean and format the result in a desired way `ai_process_csv.py`
   
Steps to get all the participants from that competion:
* Extract all the participants couple names, extract participant names and create a csv with a list of all participant `separate_names_couple_processing.py`
* Import the csv with all the competition participants to the SQL table `people`

Steps to organize the competition results:
* Combine all the competition results in a single csv, create a mapping between the names in the results and the unique id of every couple and participant (created in the SQL table) `results_processing_withids.py`
* Load all the results to a SQl table

- ouput: `marinera_league_1.db` with participants and competitions results

### Check the databse from a web app ###

1. Using cs50 sql library
2. Dropdown and Input type search. Results in basic tables
3. .js scripts `web_app/statis/js` to send the requests, process the response of the database query and modify the html of `index.html`
4. `app.py` to query the database and jsonify the results into java script objects

## AI details ##

I'm using an OpenAI assistant that:
- get the csv of the messy input
- identify the context
- determine relevant information
- filter data
- format it to a clean csv
- ouput only the final csv

*system prompt:* `openai_assistant_prompt`

Steps to process data with AI `ai_process_csv.txt`:
1. Retrieve the assistant
2. Create a new thread
3. Loop through the csv files in the input folder
4. Extract the csv content an pass it as an user message
5. Call the model to get a response
6. Extract the csv content with regex
7. Write it to a new csv file





