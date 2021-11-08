import requests
from bs4 import BeautifulSoup

domain = "https://www.goal.com/en/live-scores"
goal_url = f"{domain}"
response = requests.get(goal_url)
html_text = response.text

"get competition function take the url as an argument and return the competition string"
def get_competition_name(url):
    soup = BeautifulSoup(html_text, "html.parser")
    competition_result = soup.find_all("span", class_="competition-name")
    competition_string = ""
    for competition in competition_result:
     competition_string+= f"{competition.parent.text}\n"
    return competition_string

"get team function take the url as an argument and return the team list"
def get_team_name(url):
    soup = BeautifulSoup(html_text, "html.parser")
    team_result = soup.find_all("span", class_="match-row__team-name")
    team_list = []
    for team in team_result:
     team_list.append(team.parent.text)
    match=''
    for x in range(0, len(team_list), 2):
      match+=('Home Team:{} Away Team: {}\n'.format(team_list[x], team_list[x+1]))
    return match

"get goals function take the url as an argument and return the goal list"
def get_goals(url):
    soup= BeautifulSoup(html_text, "html.parser")
    goal_result =soup.find_all("b", class_="match-row__goals")
    goal_list = []
    for team in goal_result:
     goal_list.append(team.parent.text)
    score=''
    for x in range(0, len(goal_list), 2):
      score+=('Home Team Score:{} Away Team Score: {}\n'.format(goal_list[x], goal_list[x+1]))
    return score

"get all data function take the tow arguments and return the result of tow function "

def get_all_data(fun1,fun2):
    print(fun1)
    print(fun2)
    
"this function get  competition_name and team names and the scores "
def get_all_data1(url):
    soup= BeautifulSoup(html_text, "html.parser")
    competition_list=[]
    result =soup.find_all("div", class_="competition-matches")
    team_list=""
    Competition_string=''
    team_string=''
    score_string=''
    match_time=""
    competition_list=[]
    clean_data={}
    """for loop to get the competition name """
    for x in result:
        competition_name = x.find("span", class_="competition-name").text.strip().title()
        match = x.find_all("div", class_="match-row")
        if match:
            competition_list.append(competition_name)
        """for loop to get the teames name socre and match time """
        for j in match:
            if j==0 : continue
            team_away=j.find_all("span",class_="match-row__team-name")[1].text
            team_home=j.find_all("span",class_="match-row__team-name")[0].text
            goal_result_team_away =j.find_all("b", class_="match-row__goals")[1].text
            goal_result_team_home =j.find_all("b", class_="match-row__goals")[0].text
            time=j.find("span",class_="match-row__date").text
            football="\U000026BD"*2
            trophy="\U0001F3C6"
            date="\U000023F3"+"\U0000231B"
            team_list+= f"****** {football} Macth Time {football} ******"
            Competition_string+=f"****** {trophy} Competition {competition_name} {trophy} ******" 
            match_time+=f" ****** {date} {time} {date} ******"
            team_string+=f"****** Away Team Name > {team_away} < vs Home Team Name > {team_home} < ******"
            score_string+=f"****** score Away Team: {goal_result_team_away}  score Home Team : {goal_result_team_home} ******"
            data = {
             "competition_name": competition_name,
             }
            
        
#     print('''   
#  ************************************************************************
#  ****** Welcome from the sport section\U000026BD \U0001F3BE \U0001F3C0 **************************
#  ************************************************************************''')
#     for i in range(len(competition_list)):
#         print(''' ****** competition list ******''')
#         print(f' ****** {trophy} {competition_list[i]} {trophy}******')

#     response = input(' ****** type competition name or q for quiting > ').strip().title()
#     while response != 'Q':
#        found=True
#        for competition_item in competition_list:
#             if competition_item == response:
#                  found=False
#                  print(f" {Competition_string} ")
#                  print(f" {team_list} ")
#                  print(f"{match_time}")
#                  print(f" {team_string} ")
#                  print(f" {score_string} ")
                 
#             if found:  
#                 print(f" ****** {response}  this competition not found  ******")     
#        response=input(' ****** search for anther competition or q for quiting  >').strip().title()
#     print("I hope you get the infromtion you need")

              
    return competition_list



if __name__ =='__main__':
 
    
    print(get_all_data1(goal_url))
   

   
