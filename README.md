# Marinera League #
## The Champions League of Marinera Norteña ##

### Brief context: ###
Marinera norteña is a traditional and competitive dance from Perú. It is a couple's dance. Every weekend, competitions are held with judges evaluating each couple's performance. 
The competitions are tournament-style, with different phases and a final where the winner is decided.

This world is quite traditional, and there are no good websites or platforms to see the results. 
Each competition publishes the results in a different way (mainly Excel sheets, PDFs, or images) on their Facebook pages or websites. All the results are 'static'—not searchable in any way.

### Problems I want to solve with this project ###

- It's hard to find competition results.
- It's hard or impossible to find a list of active dancers and know their results.
- There is no way to know who the 'best dancers' are.

## What I'm building here ##

### 1. A unified database of all competition results and dancers (SQLite for now) ###
  ![marinera_league_database_schema](https://github.com/user-attachments/assets/57780668-effb-40dd-928c-1858accda836)

### 2. Functional website for easy search (Flask web app) ###
#### UI Interface ####
  ![marinera_league_UI](https://github.com/user-attachments/assets/ae26d2ee-d4be-4876-a95b-463023d085d4)
#### Search Example for competition ####
  ![marinera_league_competition_search](https://github.com/user-attachments/assets/5bac089e-f943-41cb-a43e-04b45c6bfe45)
### Search Example for participant ###
  ![marinera_league_participant_search](https://github.com/user-attachments/assets/a7343ca4-5cd6-4012-ad8c-debb00f2fbf1)

## How: ##
### New data input system ###

- Input: Excel files published by a competition.
  The Excels are not properly formatted to build a database.

Steps: 
* Export each Excel sheet to a separate .csv with a relevant name using `process-source.py`.
* Pass the .csv to an OpenAI assistant to clean and format the results in the desired way with `ai_process_csv.py`.
   
Steps to get all the participants from that competition:
* Extract all the couples' names, extract individual participant names, and create a .csv with a list of all participants using `separate_names_couple_processing.py`.
* Import the .csv with all the competition participants to the SQL table `people`.

Steps to organize the competition results:
* Combine all the competition results into a single .csv, create a mapping between the names in the results and the unique ID of every couple and participant (created in the SQL table) using `results_processing_withids.py`.
* Load all the results into an SQL table.

- Output: `marinera_league_1.db` with participants and competition results.

### Check the database from a web app ###

1. Using the CS50 SQL library.
2. Dropdown and input type search. Results appear in basic tables.
3. .js scripts in `web_app/static/js` send the requests, process the database query response, and modify the HTML of `index.html`.
4. `app.py` queries the database and jsonify the results into JavaScript objects.

## AI details ##

I'm using an OpenAI assistant that:
- Gets the .csv of the messy input.
- Identifies the context.
- Determines relevant information.
- Filters data.
- Formats it into a clean .csv.
- Outputs only the final .csv.

*System prompt:* `openAI_assistant_systemprompt.txt`

Steps to process data with AI (`ai_process_csv.py`):
1. Retrieve the assistant.
2. Create a new thread.
3. Loop through the .csv files in the input folder.
4. Extract the .csv content and pass it as a user message.
5. Call the model to get a response.
6. Extract the .csv content with regex.
7. Write it to a new .csv file.
