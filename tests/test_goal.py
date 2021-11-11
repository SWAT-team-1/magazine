from magazine.goal import *
import mock

def test_team():
    goal_url ='https://www.goal.com/en/fixtures/2021-11-10'
    # goal_url = f'{domain}'
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

def test_get_all_data1():
    expected = "I hope you get the infromtion you need"
    domain ='https://www.goal.com/en/fixtures/2021-11-10'
    with mock.patch('builtins.input', return_value='q'):
        assert get_all_data1(domain) == expected