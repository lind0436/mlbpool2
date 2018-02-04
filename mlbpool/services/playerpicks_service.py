from mlbpool.data.dbsession import DbSessionFactory
from mlbpool.data.account import Account
from mlbpool.data.teaminfo import TeamInfo
from mlbpool.data.activeplayers import ActiveMLBPlayers
from mlbpool.data.seasoninfo import SeasonInfo
from mlbpool.data.player_picks import PlayerPicks
import datetime


class PlayerPicksService:
    """This class displays all of the drop down menus for the different picks pool players can make in
    submit_picks.pt"""
    @staticmethod
    def get_division_team_list(league_id, division_id):
        """Get a list of the five teams in a specific division in one of the two leagues (AL or NL)"""
        session = DbSessionFactory.create_session()

        division_team_list = session.query(TeamInfo).filter(TeamInfo.league_id == league_id)\
            .filter(TeamInfo.division_id == division_id).order_by(TeamInfo.name).all()

        return division_team_list

    @staticmethod
    def get_hitter_list(league_id, position):
        session = DbSessionFactory.create_session()

        # TODO Player list will be huge - need to add the team to the query to display on the picks page¡

        player_list = session.query(ActiveMLBPlayers.player_id, ActiveMLBPlayers.firstname, ActiveMLBPlayers.lastname).\
            join(TeamInfo, ActiveMLBPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.league_id == league_id) \
            .filter(ActiveMLBPlayers.position != position) \
            .filter(ActiveMLBPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveMLBPlayers.lastname).all()

        return player_list

    @staticmethod
    def get_pitcher_list(league_id, position):
        session = DbSessionFactory.create_session()

        player_list = session.query(ActiveMLBPlayers.player_id, ActiveMLBPlayers.firstname, ActiveMLBPlayers.lastname).\
            join(TeamInfo, ActiveMLBPlayers.team_id == TeamInfo.team_id) \
            .filter(TeamInfo.league_id == league_id) \
            .filter(ActiveMLBPlayers.position == position) \
            .filter(ActiveMLBPlayers.season == SeasonInfo.current_season) \
            .order_by(ActiveMLBPlayers.lastname).all()

        return player_list

    @staticmethod
    def get_al_wildcard():
        session = DbSessionFactory.create_session()

        al_wildcard_list = session.query(TeamInfo).filter(TeamInfo.league_id == 0).order_by(TeamInfo.name).all()

        return al_wildcard_list

    @staticmethod
    def get_nl_wildcard():
        session = DbSessionFactory.create_session()

        nl_wildcard_list = session.query(TeamInfo).filter(TeamInfo.league_id == 1).order_by(TeamInfo.name).all()

        return nl_wildcard_list

    @staticmethod
    def get_current_season():
        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
        season = season_row.current_season

        return season

    @classmethod
    def get_player_picks(cls, afc_east_winner_pick: int, afc_east_second: int, afc_east_last: int,
                         afc_north_winner_pick: int, afc_north_second: int, afc_north_last: int,
                         afc_south_winner_pick: int, afc_south_second: int, afc_south_last: int,
                         afc_west_winner_pick: int, afc_west_second: int, afc_west_last: int,
                         nfc_east_winner_pick: int, nfc_east_second: int, nfc_east_last: int,
                         nfc_north_winner_pick: int, nfc_north_second: int, nfc_north_last: int,
                         nfc_south_winner_pick: int, nfc_south_second: int, nfc_south_last: int,
                         nfc_west_winner_pick: int, nfc_west_second: int, nfc_west_last: int,
                         afc_qb_pick: int, nfc_qb_pick: int, afc_rb_pick: int, nfc_rb_pick: int,
                         afc_rec_pick: int, nfc_rec_pick: int,
                         afc_sacks_pick: int, nfc_sacks_pick: int,
                         afc_int_pick: int, nfc_int_pick: int,
                         afc_wildcard1_pick: int, afc_wildcard2_pick: int,
                         nfc_wildcard1_pick: int, nfc_wildcard2_pick: int,
                         afc_pf_pick: int, nfc_pf_pick: int,
                         specialteams_td_pick: int,
                         user_id: str):

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
        season = season_row.current_season

        dt = datetime.datetime.now()

#        player_picks = PlayerPicks(date_submitted=dt, user_id=user_id, afc_east_first=afc_east_winner_pick,
#                                   afc_east_second=afc_east_second, afc_east_last=afc_east_last,
#                                   afc_north_first=afc_north_winner_pick, afc_north_second=afc_north_second,
#                                   afc_north_last=afc_north_last,
#                                   afc_south_first=afc_south_winner_pick, afc_south_second=afc_south_second,
#                                   afc_south_last=afc_south_last,
#                                   afc_west_first=afc_west_winner_pick, afc_west_second=afc_west_second,
#                                   afc_west_last=afc_west_last,
#                                   nfc_east_first=nfc_east_winner_pick,
#                                   nfc_east_second=nfc_east_second, nfc_east_last=nfc_east_last,
#                                   nfc_north_first=nfc_north_winner_pick, nfc_north_second=nfc_north_second,
#                                   nfc_north_last=nfc_north_last,
#                                   nfc_south_first=nfc_south_winner_pick, nfc_south_second=nfc_south_second,
#                                   nfc_south_last=nfc_south_last,
#                                   nfc_west_first=nfc_west_winner_pick,
#                                   nfc_west_second=nfc_west_second,
#                                   nfc_west_last=nfc_west_last,
#                                   afc_passing_pick=afc_qb_pick,
#                                   nfc_passing_pick=nfc_qb_pick,
#                                   afc_rushing_pick=afc_rb_pick,
#                                   nfc_rushing_pick=nfc_rb_pick,
#                                   afc_receiving_pick=afc_rec_pick,
#                                   nfc_receiving_pick=nfc_rec_pick,
#                                   afc_sacks_pick=afc_sacks_pick,
#                                   nfc_sacks_pick=nfc_sacks_pick,
#                                   afc_int_pick=afc_int_pick,
#                                   nfc_int_pick=nfc_int_pick,
#                                   afc_wildcard1=afc_wildcard1_pick, afc_wildcard2=afc_wildcard2_pick,
#                                   nfc_wildcard2=nfc_wildcard2_pick, nfc_wildcard1=nfc_wildcard1_pick,
#                                   afc_pf=afc_pf_pick, nfc_pf=nfc_pf_pick,
#                                   specialteams_td=specialteams_td_pick,

 #                                  season=season)




#        session.add(player_picks)

#        session.commit()

        #new stuff here --------------------
        # Add AFC team picks
        afc_east_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=1, 
                                         rank=1, team_id=afc_east_winner_pick, pick_type=1)
        session.add(afc_east_winner_db)
        afc_east_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=1, 
                                         rank=2, team_id=afc_east_second, pick_type=1)
        session.add(afc_east_second_db)
        
        afc_east_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=1, 
                                       rank=4, team_id=afc_east_last, pick_type=1)

        session.add(afc_east_last_db)

        afc_north_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=2,
                                          rank=1, team_id=afc_north_winner_pick, pick_type=1)
        session.add(afc_north_winner_db)
        afc_north_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=2,
                                          rank=2, team_id=afc_north_second, pick_type=1)
        session.add(afc_north_second_db)

        afc_north_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=2,
                                        rank=4, team_id=afc_north_last, pick_type=1)

        session.add(afc_north_last_db)

        afc_south_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=3,
                                          rank=1, team_id=afc_south_winner_pick, pick_type=1)
        session.add(afc_south_winner_db)
        afc_south_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=3,
                                          rank=2, team_id=afc_south_second, pick_type=1)
        session.add(afc_south_second_db)

        afc_south_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=3,
                                        rank=4, team_id=afc_south_last, pick_type=1)

        session.add(afc_south_last_db)

        afc_west_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=4,
                                         rank=1, team_id=afc_west_winner_pick, pick_type=1)
        session.add(afc_west_winner_db)
        afc_west_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=4,
                                         rank=2, team_id=afc_west_second, pick_type=1)
        session.add(afc_west_second_db)

        afc_west_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=0, division_id=4,
                                       rank=4, team_id=afc_west_last, pick_type=1)

        session.add(afc_west_last_db)

        # Add AFC team picks
        nfc_east_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=1,
                                         rank=1, team_id=nfc_east_winner_pick, pick_type=1)
        session.add(nfc_east_winner_db)
        nfc_east_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=1,
                                         rank=2, team_id=nfc_east_second, pick_type=1)
        session.add(nfc_east_second_db)

        nfc_east_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=1,
                                       rank=4, team_id=nfc_east_last, pick_type=1)

        session.add(nfc_east_last_db)

        nfc_north_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=2,
                                          rank=1, team_id=nfc_north_winner_pick, pick_type=1)
        session.add(nfc_north_winner_db)
        nfc_north_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=2,
                                          rank=2, team_id=nfc_north_second, pick_type=1)
        session.add(nfc_north_second_db)

        nfc_north_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=2,
                                        rank=4, team_id=nfc_north_last, pick_type=1)

        session.add(nfc_north_last_db)

        nfc_south_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=3,
                                          rank=1, team_id=nfc_south_winner_pick, pick_type=1)
        session.add(nfc_south_winner_db)
        nfc_south_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=3,
                                          rank=2, team_id=nfc_south_second, pick_type=1)
        session.add(nfc_south_second_db)

        nfc_south_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=3,
                                        rank=4, team_id=nfc_south_last, pick_type=1)

        session.add(nfc_south_last_db)

        nfc_west_winner_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=4,
                                         rank=1, team_id=nfc_west_winner_pick, pick_type=1)
        session.add(nfc_west_winner_db)
        nfc_west_second_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=4,
                                         rank=2, team_id=nfc_west_second, pick_type=1)
        session.add(nfc_west_second_db)

        nfc_west_last_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, league_id=1, division_id=4,
                                       rank=4, team_id=nfc_west_last, pick_type=1)

        session.add(nfc_west_last_db)

        # Add AFC Player Picks

        afc_passing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_qb_pick,
                                     pick_type=4, league_id=0)
        session.add(afc_passing_db)

        afc_rushing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_rb_pick,
                                     pick_type=5, league_id=0)
        session.add(afc_rushing_db)

        afc_receiving_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_rec_pick,
                                       pick_type=6, league_id=0)
        session.add(afc_receiving_db)

        afc_sacks_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_sacks_pick,
                                   pick_type=7, league_id=0)
        session.add(afc_sacks_db)

        afc_int_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=afc_int_pick,
                                 pick_type=8, league_id=0)
        session.add(afc_int_db)
        
        # Add NFC Player Picks
        
        nfc_passing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_qb_pick,
                                     pick_type=4, league_id=1)
        session.add(nfc_passing_db)

        nfc_rushing_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_rb_pick,
                                     pick_type=5, league_id=1)
        session.add(nfc_rushing_db)

        nfc_receiving_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_rec_pick,
                                       pick_type=6, league_id=1)
        session.add(nfc_receiving_db)

        nfc_sacks_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_sacks_pick,
                                   pick_type=7, league_id=1)
        session.add(nfc_sacks_db)

        nfc_int_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, player_id=nfc_int_pick,
                                 pick_type=8, league_id=1)
        session.add(nfc_int_db)

        # Add the wildcard picks
        afc_wildcard1_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=afc_wildcard1_pick,
                                       pick_type=9, league_id=0)
        session.add(afc_wildcard1_db)

        afc_wildcard2_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=afc_wildcard2_pick,
                                       pick_type=9, league_id=0)
        session.add(afc_wildcard2_db)
        
        nfc_wildcard1_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=nfc_wildcard1_pick,
                                       pick_type=9, league_id=1)
        session.add(nfc_wildcard1_db)

        nfc_wildcard2_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=nfc_wildcard2_pick,
                                       pick_type=9, league_id=1)
        session.add(nfc_wildcard2_db)

        # Add the Points For picks
        afc_pf_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=afc_pf_pick,
                                pick_type=3, league_id=0)
        session.add(afc_pf_db)

        nfc_pf_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt, team_id=nfc_wildcard2_pick,
                                pick_type=3, league_id=1)
        session.add(nfc_pf_db)

        # Add the tiebreaker
        specialteams_tiebreaker_db = PlayerPicks(user_id=user_id, season=season, date_submitted=dt,
                                                 team_id=specialteams_td_pick, pick_type=10)
        session.add(specialteams_tiebreaker_db)
        session.commit()


class DisplayPlayerPicks:

    @staticmethod
    def display_picks(user_id):

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == 1).first()
        season = season_row.current_season

        user_query = session.query(PlayerPicks, TeamInfo.name).join(TeamInfo, PlayerPicks.afc_east_first == TeamInfo.team_id)\
            .filter(PlayerPicks.user_id == user_id) \
            .filter(PlayerPicks.season == season).all()

#        print(user_query)
#        print(type(user_query[0]))

        return user_query
