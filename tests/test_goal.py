from magazine.goal import *

def test_team():
    domain ='https://www.goal.com/en/fixtures/2021-11-10'
    goal_url = f'{domain}'
    excepted = " Jordan " 
    get_team_name(goal_url)
    actual=get_team_name(goal_url)[3]
    assert excepted==actual
def test_competition_name():
    domain ='https://www.goal.com/en/fixtures/2021-11-10'
    goal_url = f'{domain}'
    excepted = " Friendlies " 
    get_competition_name(goal_url)
    actual=get_competition_name(goal_url)[0]
    assert excepted==actual
def test_score():
    domain ='https://www.goal.com/en/fixtures/2021-11-10'
    goal_url = f'{domain}'
    excepted = " 0 " 
    get_competition_name(goal_url)
    actual=get_goals(goal_url)[0]
    assert excepted==actual