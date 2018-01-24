from mlbpool.data.dbsession import DbSessionFactory
from mlbpool.data.account import Account
from mlbpool.data.player_picks import PlayerPicks
from mlbpool.data.teaminfo import TeamInfo
from mlbpool.data.leagueinfo import LeagueInfo
from mlbpool.data.divisioninfo import DivisionInfo
from mlbpool.data.activeplayers import ActiveMLBPlayers
from sqlalchemy import and_


class ViewPicksService:
    @classmethod
    def get_account_info(cls, user_id):
        session = DbSessionFactory.create_session()

        account_info = session.query(Account).filter(Account.id == user_id).all()

        return account_info

    @classmethod
    def seasons_played(cls, user_id):
        session = DbSessionFactory.create_session()

        seasons_played = session.query(PlayerPicks.season).distinct(PlayerPicks.season).filter(Account.id == user_id)

        return seasons_played

    @staticmethod
    def display_picks(user_id, season):

        session = DbSessionFactory.create_session()

        picks_query = session.query(PlayerPicks.pick_type, ConferenceInfo.conference, DivisionInfo.division,
                                    TeamInfo.name, PlayerPicks.rank,
                                    ActiveNFLPlayers.firstname, ActiveNFLPlayers.lastname, PlayerPicks.multiplier) \
            .outerjoin(ConferenceInfo)\
            .outerjoin(DivisionInfo) \
            .outerjoin(TeamInfo)\
            .outerjoin(ActiveNFLPlayers, and_(PlayerPicks.player_id == ActiveNFLPlayers.player_id,
                                              PlayerPicks.season == ActiveNFLPlayers.season)).\
            filter(PlayerPicks.user_id == user_id,
                   PlayerPicks.season == season)

        return picks_query
