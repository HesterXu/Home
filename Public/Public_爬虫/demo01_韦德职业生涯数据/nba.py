from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import requests
import pandas as pd

def parse_html():
    url = "https://www.basketball-reference.com/players/w/wadedw01.html"
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        html = reponse.text
        extract_htm(html)

def extract_htm(html):
    doc = pq(html)
    Dwyane_Wade_data = []
    data_items = doc.find("#div_per_game #per_game tbody tr").items()
    for itme in data_items:
        season = itme.find("th[data-stat='season'] a").text()
        age = itme.find("td[data-stat='age']").text()
        team = itme.find("td[data-stat='team_id'] a").text()
        league = itme.find("td[data-stat='lg_id'] a").text()
        position = itme.find("td[data-stat='pos']").text()
        games = itme.find("td[data-stat='g']").text()
        games_started = itme.find("td[data-stat='gs']").text()
        minutes_played_per_game = itme.find("td[data-stat='mp_per_g']").text()
        field_goals_per_game = itme.find("td[data-stat='mp_per_g']").text()
        field_goals_attempts_per_game = itme.find("td[data-stat='fga_per_g']").text()
        field_goal_percentage = itme.find("td[data-stat='fg_pct']").text()
        point_3_field_goal_per_game = itme.find("td[data-stat='fg3_per_g']").text()
        point_3_field_goal_percentage = itme.find("td[data-stat='fg3_pct']").text()
        point_2_filed_goals_per_game = itme.find("td[data-stat='fg2_per_g']").text()
        point_2_filed_goals_attempts_per_game = itme.find("td[data-stat='fg2a_per_g']").text()
        fg2_pct = itme.find("td[data-stat='fg2_pct']").text()
        efg_pct = itme.find("td[data-stat='efg_pct']").text()
        ft_per_g = itme.find("td[data-stat='ft_per_g']").text()
        fta_per_g = itme.find("td[data-stat='fta_per_g']").text()
        ft_pct = itme.find("td[data-stat='ft_pct']").text()
        orb_per_g = itme.find("td[data-stat='orb_per_g']").text()
        drb_per_g = itme.find("td[data-stat='drb_per_g']").text()
        trb_per_g = itme.find("td[data-stat='trb_per_g']").text()
        ast_per_g = itme.find("td[data-stat='ast_per_g']").text()
        stl_per_g = itme.find("td[data-stat='stl_per_g']").text()
        blk_per_g = itme.find("td[data-stat='blk_per_g']").text()
        tov_per_g = itme.find("td[data-stat='tov_per_g']").text()
        pf_per_g = itme.find("td[data-stat='pf_per_g']").text()
        pts_per_g = itme.find("td[data-stat='pts_per_g']").text()
        item_data = {'season': season, "age": age, "team": team, "league": league, "position": position, "games": games,
                "games_started": games_started, "minutes_played_per_game": minutes_played_per_game, "field_goals_per_game": field_goals_per_game,
                "field_goals_attempts_per_game": field_goals_attempts_per_game, "field_goal_percentage": field_goal_percentage,
                "point_3_field_goal_per_game": point_3_field_goal_per_game, "point_3_field_goal_percentage": point_3_field_goal_percentage,
                "point_2_filed_goals_per_game": point_2_filed_goals_per_game, "point_2_filed_goals_attempts_per_game": point_2_filed_goals_attempts_per_game,
                "fg2_pct": fg2_pct, "efg_pct": efg_pct, "ft_per_g": ft_per_g, "fta_per_g": fta_per_g, "ft_pct": ft_pct,
                "orb_per_g": orb_per_g, "drb_per_g": drb_per_g, "trb_per_g": trb_per_g, "ast_per_g": ast_per_g, "stl_per_g": stl_per_g,
                "blk_per_g": blk_per_g, "tov_per_g": tov_per_g, "pf_per_g": pf_per_g, "pts_per_g": pts_per_g}
        print(item_data)
        Dwyane_Wade_data.append(item_data)
    data = pd.DataFrame(Dwyane_Wade_data)
    data.to_csv("Dwyane_Wade_data.csv", encoding='utf_8_sig')


if __name__ == '__main__':
    parse_html()
