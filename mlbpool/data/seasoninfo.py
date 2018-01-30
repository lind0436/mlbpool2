from mlbpool.data.modelbase import SqlAlchemyBase
import sqlalchemy


class SeasonInfo(SqlAlchemyBase):
    __tablename__ = 'SeasonInfo'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    current_season = sqlalchemy.Column(sqlalchemy.Integer)
    season_start_date = sqlalchemy.Column(sqlalchemy.Integer)
    all_star_game_date = sqlalchemy.Column(sqlalchemy.Integer)



