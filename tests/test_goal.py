from magazine.goal import *
def test_report():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = get_all_data1(goal_url)
    assert '****** ⚽⚽ Macth Time ⚽⚽ ******' in excepted
def test_team():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = " Chelsea " 
    get_team_name(goal_url)
    actual=get_team_name(goal_url)[1]
    assert excepted==actual
def test_competition_name():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = " UEFA Women's Champions League " 
    get_competition_name(goal_url)
    actual=get_competition_name(goal_url)[0]
    assert excepted==actual
def test_score():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = " 0 " 
    get_competition_name(goal_url)
    actual=get_goals(goal_url)[0]
    assert excepted==actual