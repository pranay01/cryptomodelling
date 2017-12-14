import matplotlib.pyplot as plt
import numpy as np
#Model Indium parameters

#Coin issue schedule 
'''
Players  - Indium token issuer, Indium grantee, 
Expected prediction outcomes - optimum release schedule, expected pricing

-- What are the other frameworks for modelling games
-- Check sweetbridge modelling
'''

initial_issue = 10000

growth_rate = 0.03 # per year ( assuming inflation rate)

#for simulating constant supply

#modelling for 20 yrs
no_of_years = 20
token_supply= np.zeros(no_of_years)

#Setting the token supply in first year equal to initial_supply
token_supply[0] = initial_issue


# Number of grantees - 10 per year, with 40 tokens each grantee
no_of_grantees_per_year = 10
reward_per_grantee = 40


for i in range(1,no_of_years):
	print(i)
	token_supply[i] = (token_supply[i-1]-(no_of_grantees_per_year*reward_per_grantee))*(1+growth_rate)**1 #replacing i with 1

print(token_supply)
plt.plot(token_supply,'r', label='3% inflation')

#####

growth_rate = 0.04 ## a 4% inflation rate almost compensates for the coin issue to startups 40*10/10000 = 0.04
token_supply[0] = initial_issue

for i in range(1,no_of_years):
	print(i)
	token_supply[i] = (token_supply[i-1]-(no_of_grantees_per_year*reward_per_grantee))*(1+growth_rate)**1 #replacing i with 1

print(token_supply)
plt.plot(token_supply,'b',label='4% inflation')
legend = plt.legend(loc='center right', shadow=True, fontsize='x-large')

plt.grid()

#price of any product depends upon supply vs demand
# Demand - by Indium foundation to give to startup projects
# Supply Issue schedule of the Indium foundation
# Why will there be value for the token unless its backed by something or it can provide some service which can be valued


plt.show()

#Value derivation for Indium token

