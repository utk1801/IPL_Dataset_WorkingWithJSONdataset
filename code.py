# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data) 
 
# Code starts here
#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.

def get_delivery_faced_by_batsman(desired_batsman,data):
    count=0
    inn_deliveries=data['innings'][0]['1st innings']['deliveries']
    for deli in inn_deliveries:
        for deli_num,deli_info in deli.items():
            batsman=deli_info['batsman']
            if(batsman==desired_batsman):
                count+=1
    return count            

print(get_delivery_faced_by_batsman('SC Ganguly',data)," deliveries were faced by SC Ganguly")



#  Who was man of the match and how many runs did he scored ?

mom=data['info']['player_of_match'][0]
print(mom," was the Man of the Match and he scored ")

def get_runs_scored_by_batsman(desired_batsman,data):
    runs_scored=0
    inn_deliveries=data['innings'][0]['1st innings']['deliveries']
    for deli in inn_deliveries:
        for deli_num,deli_info in deli.items():
            batsman=deli_info['batsman']
            if(batsman==desired_batsman):
                #print(deli_info)
                runs_scored+=deli_info['runs']['batsman']
                
    return runs_scored            

print(get_runs_scored_by_batsman(mom,data)," runs")


#  Which batsman played in the first inning?
def get_batsman_by_inning(data):
    batsman_array=[]
    inn_deliveries=data['innings'][0]['1st innings']['deliveries']
    for deli in inn_deliveries:
        for deli_num,deli_info in deli.items():
            batsman_array.append(deli_info['batsman'])     
    return set(batsman_array)

print(get_batsman_by_inning(data)," batted in the first innings.")


# Which batsman had the most no. of sixes in first inning ?
sixes=[]
inn_deliveries=data['innings'][0]['1st innings']['deliveries']
for deli in inn_deliveries:
    for deli_num,deli_info in deli.items():
        if(deli_info['runs']['batsman']==6):
            sixes.append(deli_info['batsman'])
batsman_sixes=(Counter(sixes))
print(max(batsman_sixes,key=batsman_sixes.get), "hit the max no. of sixes in first innings")

# Find the names of all players that got bowled out in the second innings.
wicket=[]
inn_deliveries=data['innings'][1]['2nd innings']['deliveries']
for deli in inn_deliveries:
    for deli_num,deli_info in deli.items():
        if('wicket' in deli_info and deli_info['wicket']['kind']=='bowled'):
            wicket.append(deli_info['wicket']['player_out'])
print(wicket, "got bowled out in the 2nd innings.")
    


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_count_inn1=0
extras_count_inn2=0
inn_deliveries=data['innings'][0]['1st innings']['deliveries']
for deli in inn_deliveries:
    for deli_num,deli_info in deli.items():
        if('extras' in deli_info):
            extras_count_inn1+=1

inn_deliveries=data['innings'][1]['2nd innings']['deliveries']
for deli in inn_deliveries:
    for deli_num,deli_info in deli.items():
        if('extras' in deli_info):
            extras_count_inn2+=1

print(extras_count_inn2-extras_count_inn1," more extras were bowled in the 2nd innings.")

# Code ends here


