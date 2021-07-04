counties=["Arapahoe","Denver","Jefferson"]
if counties[1]== 'Denver':
    print(counties[1])
if counties[2]!='Jefferson':
    print(counties[2])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
for key, value in counties_dict.items():
    print(key,value)
for key, value in counties_dict.items():
    print(key,"county has",value)
for key, value in counties_dict.items():
    print(key,"county has",value, "registered voters")
voting_data=[{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Dener", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for county in range(len(voting_data)):
    print(voting_data[county]['county'])
#print both directories 
for county_dict in voting_data:
    print(county_dict['registered_voters'])
for county_dict in voting_data:
    print(county_dict['county'])
for county, voters in counties_dict.items():
    print(county + "county has" + str(voters) + "registered voters")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
candidate_votes= int(input("How many did the candidate get in the election?"))
total_votes= int(input("What is the total number of votes in the election?"))
message_to_candidate=(
f"You received {candidate_votes:,} number of votes."
f"The total number of votes in the election was {total_votes:,}."
f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
counties_dict={"Arapahoe": 422829, "Denver": 463353, "Jefferson": 422438}









