# Drop the fifth row to delete all repeated rows
fifa_no_rep = fifa_players.drop(4, axis=0)

# Print fifa_pivot
print(fifa_no_rep)]

# Discard the fifth row to delete all repeated rows
fifa_drop = fifa_players.drop(4, axis=0).reset_index(drop="True")

# Use pivot method to get all scores by name and movement
fifa_pivot = fifa_drop.pivot(index="name", columns="movement") 

# Print fifa_pivot
print(fifa_pivot)  

# Use pivot table to get all scores by name and movement
fifa_pivot_table = fifa_players.pivot_table(index="name", 
                                     columns="movement", 
                                     aggfunc="mean")
# Print fifa_pivot_table
print(fifa_pivot_table)

# Use pivot table to display mean age of players by club and nationality 
mean_age_fifa = fifa_players.pivot_table(index="nationality", 
                                  columns="club", 
                                  values="age", 
                                  aggfunc="mean")

# Print mean_age_fifa
print(mean_age_fifa)
