-- script that lists all cities contained in the database hbtn_0d_usa
Select cities_id, cities.name, states.name From cities
Inner Join states On cities.state_id = states.id;
