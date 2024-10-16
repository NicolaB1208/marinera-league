CREATE TABLE people_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    names TEXT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE couples_new (
id INTEGER PRIMARY KEY AUTOINCREMENT,
names TEXT,
couple_id_1 INTEGER NOT NULL,
couple_id_2 INTEGER NOT NULL,
FOREIGN KEY(couple_id_1) REFERENCES people(id),
FOREIGN KEY(couple_id_2) REFERENCES people(id)
);

SELECT eliminatoria_madrid_adulto.names,eliminatoria_madrid_adulto.couple_number,eliminatoria_madrid_adulto.total_score,eliminatoria_madrid_adulto.qualified,couples_new.id
FROM eliminatoria_madrid_adulto
JOIN couples_new
ON eliminatoria_madrid_adulto.names = couples_new.names;

SELECT name FROM people WHERE id IN (
    SELECT couple_id_2 FROM couples WHERE couple_id_1 IN (
        SELECT id FROM people WHERE name = 'Alessandro Ramos')
)
OR id IN (
    SELECT couple_id_1 FROM couples WHERE couple_id_2 IN (
        SELECT id FROM people WHERE name = 'Alessandro Ramos')
);

SELECT * FROM eliminatoria_madrid
  JOIN couples on couples.id = eliminatoria_madrid.couple_id
  WHERE qualified = 1;

SELECT category,couple_number,total_score,qualified FROM eliminatoria_madrid
  JOIN couples on couples.id = eliminatoria_madrid.couple_id
  WHERE qualified = 1;

SELECT category, total_score, qualified, names FROM eliminatoria_madrid JOIN couples ON eliminatoria_madrid.couple_id = couples.id WHERE qualified = 1;

SELECT category,total_score,qualified,names FROM eliminatoria_madrid
JOIN couples on couples.id = eliminatoria_madrid.couple_id
WHERE qualified = 1;

SELECT * FROM couples 
JOIN people on (couples.couple_id_1,couples.couple_id_1) = (people.id,people.id)
LIMIT 10;

SELECT category,total_score,name,qualified FROM eliminatoria_madrid_couples WHERE couple_id IN (
SELECT id FROM couples WHERE couple_id_1 IN (
SELECT id FROM people WHERE name = 'Mayaluz Carrera Villar'));

SELECT category,total_score,name,qualified,names FROM eliminatoria_madrid_single 
JOIN couples ON eliminatoria_madrid_single.person_id = couples.id
JOIN people ON couples.couple_id_1 = people.id
WHERE name = 'Ami Kennice Rodríguez';


### SEARCH RESULT OF A PERSON IN A COUPLE
SELECT category,total_score,name,qualified,names FROM final_madrid_couples 
JOIN couples ON final_madrid_couples.couple_id = couples.id
JOIN people ON couples.couple_id_1 = people.id
WHERE name = 'Victoria Cárdenas';

### SEARCH RESULT OF A PERSON SINGLE
SELECT category,total_score,name,qualified FROM final_madrid_single
JOIN people ON final_madrid_single.person_id = people.id
WHERE name = 'Nicola Battoia';

### SEARCH RESULT OF A PERSON SINGLE
SELECT * FROM final_madrid_couples
JOIN couples ON final_madrid_couples.couple_id = couples.id
WHERE category = 'infantil';


## SEARCH RESULTS OF A CONCURSO PHASE
SELECT * FROM ?_madrid_couples
JOIN couples ON ?.


SELECT * FROM final_madrid_single JOIN people ON final_madrid_single.person_id = people.id WHERE category = 'juvenil' ORDER BY total_score DESC

SELECT * FROM final_madrid_couples JOIN couples ON final_madrid_couples.couple_id = couple.id WHERE category = 'juvenil' ORDER BY total_score DESC;

SELECT * FROM final_madrid_couples JOIN couples ON final_madrid_couples.couple_id = couples.id WHERE category LIKE 'juvenil' ORDER BY total_score DESC;

SELECT * FROM final_madrid_couples JOIN couples ON final_madrid_couples.couple_id = couples.id WHERE names LIKE '%A%';

SELECT * FROM final_madrid_single JOIN people ON final_madrid_single.person_id = people.id WHERE name LIKE '%Nico%';