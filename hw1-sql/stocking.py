import sqlite3
import pandas as pd

#TODO fill in
def connect(filename):
    con = sqlite3.connect(filename)
    return con


#TODO fill in
def inventory_dataset(con):
    query = "SELECT title FROM film GROUP BY film.film_id;"
    titles = con.execute(query)
    p_titles = []
    for i in titles:
        p_titles.append(i[0])
    #print("titles\n",len(p_titles))
    
    #query = "SELECT *, count(1) FROM film RIGHT JOIN inventory WHERE film.film_id = inventory.film_id GROUP BY film.film_id;"
    query = "SELECT film.film_id, count(1) FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id GROUP BY film.film_id;"
    inventory = con.execute(query)
    p_inventory = []
    for i in inventory:
        p_inventory.append(i[1])
    #print("invent\n",len(p_inventory))
    #print("inventory[0]",p_inventory[0])
    
    #query = "SELECT film.film_id, count(1) FROM film, inventory, rental WHERE film.film_id = inventory.film_id and inventory.inventory_id = rental.inventory_id GROUP BY film.film_id;"
    query = "SELECT film.film_id, count(1) FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id LEFT JOIN rental ON inventory.inventory_id = rental.inventory_id GROUP BY film.film_id;"
    rentals = con.execute(query)
    p_rentals = []
    for i in rentals:
        #print(i)
        p_rentals.append(i[1])
    #print("rentals\n",len(p_rentals))
    
    query = "SELECT rental_rate FROM film GROUP BY film.film_id;"
    rental_rates = con.execute(query)
    p_rental_rates = []
    for i in rental_rates:
        p_rental_rates.append(i[0])
    #print("rent rate\n",len(p_rental_rates))
    
    query = "SELECT replacement_cost FROM film GROUP BY film.film_id"
    replacement_costs = con.execute(query)
    p_replacement_costs = []
    for i in replacement_costs:
        p_replacement_costs.append(i[0])
    #print("rep cost\n",len(p_replacement_costs))
        
    data = pd.DataFrame({'name': p_titles, 'inv_copies': p_inventory, 'rentals': p_rentals, 'rental_rate': p_rental_rates, 'replacement_price': p_replacement_costs})
    
    data.set_index('name',inplace=True)
    return data


con = connect('sqlite-sakila.db')
df = inventory_dataset(con)
df.to_csv('inventory_dataset.csv')



