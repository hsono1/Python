-- What query would you run to get all the customers inside city_id = 312? 
-- Your query should return customer first name, last name, email, and address.

select customer.first_name, customer.last_name, customer.email, address,postal_code, city.city_id
from address
join customer on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where city.city_id = 312;


-- What query would you run to get all comedy films? Your query should return
-- film title, description, release year, rating, special features, and genre (category).

select film.title, film.description, film.release_year, film.rental_rate, film.special_features, category.name
from film_category
join category on film_category.category_id = category.category_id
join film on film_category.film_id = film.film_id
where category.name= "comedy";


-- What query would you run to get all the films joined by actor_id=5?
-- Your query should return the film title, description, and release year.

select actor.first_name, actor.last_name,  film.title, film.description, film.release_year
from film_actor
join actor on actor.actor_id = film_actor.actor_id
join film on film.film_id = film_actor.film_id
where actor.actor_id = 5;


-- What query would you run to get all the customers in store_id = 1 and inside 
-- these cities (1, 42, 312 and 459)? Your query should return 
-- customer first name, last name, email, and address.
select customer.first_name, customer.last_name, customer.email
from customer
join store on store.store_id = customer.store_id
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where store.store_id = 1 or city.city_id in (1, 42, 312, 459);



-- What query would you run to get all the films with a "rating = G" 
-- and "special feature = behind the scenes", joined by actor_id = 15? 
-- Your query should return the film title, description, release year, rating, 
-- and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.

select film.title, film.description, film.release_year, film.rating, film.special_features
from film
where rating = "G" and special_features like "%behind the scenes%";



-- What query would you run to get all the actors that joined in the film_id = 369? 
-- Your query should return the film_id, title, actor_id, and actor_name.
select film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
from film_actor
join film on film.film_id = film_actor.film_id
join actor on actor.actor_id = film_actor.actor_id
where film.film_id = 369;


-- What query would you run to get all drama films with a rental rate of 2.99? 
-- Your query should return film title, description, release year, rating, special features, 
-- and genre (category).

select film.title, film.description, film.release_year, film.rental_rate, film.special_features, category.name
from film_category
join film on film.film_id = film_category.film_id
join category on category.category_id = film_category.category_id
where category.name = "drama" and film.rental_rate = 2.99












-- What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.