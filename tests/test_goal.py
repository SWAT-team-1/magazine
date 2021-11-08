from magazine.goal import *
def test_report():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = get_all_data1(goal_url)
    assert '****** ⚽⚽ Macth Time ⚽⚽ ******' in excepted
def test_string():
    domain ='https://www.goal.com/en/live-scores'
    goal_url = f'{domain}'
    excepted = ['Fa Cup']
    get_all_data1(goal_url)
    actual=get_all_data1(goal_url)
    assert excepted==actual