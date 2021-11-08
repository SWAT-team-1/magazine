from magazine.goal import *
def test_report():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = get_all_data1(goal_url)
    assert 'Competition Premier League Away Team  Watford score: 0 against Home Team  Arsenal score: 1' in excepted
def test_string():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = get_all_data1(goal_url)
    assert ['Fa Cup'] in excepted