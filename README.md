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
1. Export each excel sheet to separate .csv with relevant name `process-source.py`
2. Pass the csv to an OpenAI assistant to clean and format the result in a desired way `ai_process_csv.py`
3. Steps to get all the participants from that competion:
  4. Extract all the participants couple names, extract participant names and create a csv with a list of all participant `separate_names.py`
  5. Import the csv with all the competition participants to the SQL table `people`
6. Steps to organize the competition results:
  7. 



