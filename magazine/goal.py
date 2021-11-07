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
    result =soup.find_all("div", class_="competition-matches")
    team_list=""
    
    for x in result:
        competition_name = x.find("span", class_="competition-name").text.strip()
        match = x.find_all("div", class_="match-row")
        
        for j in match:
            if j==0 : continue
            team_away=j.find_all("span",class_="match-row__team-name")[1].text
            team_home=j.find_all("span",class_="match-row__team-name")[0].text
            goal_result_team_away =j.find_all("b", class_="match-row__goals")[1].text
            goal_result_team_home =j.find_all("b", class_="match-row__goals")[0].text
            team_list+= f"Competition {competition_name} Away Team  {team_away} score: {goal_result_team_away} against Home Team  {team_home} score: {goal_result_team_home}\n"
            
    return team_list


if __name__ =='__main__':

    get_all_data1(goal_url)
    