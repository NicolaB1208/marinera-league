SELECT name FROM people WHERE id IN (
    SELECT couple_id_2 FROM couples WHERE couple_id_1 IN (
        SELECT id FROM people WHERE name = 'Alessandro Ramos')
)
OR id IN (
    SELECT couple_id_1 FROM couples WHERE couple_id_2 IN (
        SELECT id FROM people WHERE name = 'Alessandro Ramos')
);
