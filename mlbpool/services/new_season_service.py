from mlbpool.data.seasoninfo import SeasonInfo
from mlbpool.data.dbsession import DbSessionFactory
import requests
from requests.auth import HTTPBasicAuth
import mlbpool.data.config as config


class NewSeasonService:
    @staticmethod
    def get_install():
        return []

    # TODO Add logging
    @classmethod
    def create_season(cls, season, all_star_game_date):
        """After first time installation or before a new season starts, this will update the season year
            in the database.  This is used to for the MySportsFeeds API to get the correct year of stats needed."""
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo)

        new_season = SeasonInfo()
        new_season.current_season = season
        new_season.all_star_game_date = all_star_game_date

        if season_row.count() == 0:
            print("New install, adding a season")

            response = requests.get('https://api.mysportsfeeds.com/v1.2/pull/mlb/' + str(season) +
                                    '-regular/full_game_schedule.json',
                                    auth=HTTPBasicAuth(config.msf_username, config.msf_pw))

            gameday_json = response.json()
            gameday_data = gameday_json["fullgameschedule"]["gameentry"][0]

            first_game_date = gameday_data["date"]
            first_game_time = gameday_data["time"]
            away_team = gameday_data["awayTeam"]["ID"]
            home_team = gameday_data["homeTeam"]["ID"]

            new_season = SeasonInfo(season_start_date=first_game_date, season_start_time=first_game_time,
                                    home_team=home_team, away_team=away_team, current_season=season,
                                    all_star_game_date=all_star_game_date)

            print(new_season)

            session.add(new_season)
            session.commit()
            session.close()
        else:
            print("Existing season found, updating to new year")

            response = requests.get('https://api.mysportsfeeds.com/v1.2/pull/mlb/' + str(season) +
                                    '-regular/full_game_schedule.json',
                                    auth=HTTPBasicAuth(config.msf_username, config.msf_pw))

            gameday_json = response.json()
            gameday_data = gameday_json["fullgameschedule"]["gameentry"][0]

            first_game_date = gameday_data["date"]
            first_game_time = gameday_data["time"]
            away_team = gameday_data["awayTeam"]["ID"]
            home_team = gameday_data["homeTeam"]["ID"]

            season_start_date = first_game_date

            update_row = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
            update_row.current_season = season
            update_row.season_start_date = season_start_date
            update_row.all_star_game_date = all_star_game_date
            update_row.first_game_time = first_game_time
            update_row.away_team = away_team
            update_row.home_team = home_team

            session.commit()
            session.close()
