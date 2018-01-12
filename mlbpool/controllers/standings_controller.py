import pyramid_handlers
from mlbpool.controllers.base_controller import BaseController
from mlbpool.viewmodels.standings_viewmodel import StandingsViewModel
from mlbpool.services.standings_service import StandingsService
from mlbpool.data.dbsession import DbSessionFactory
from mlbpool.data.seasoninfo import SeasonInfo
from mlbpool.data.weekly_player_results import WeeklyPlayerResults


class StandingsController(BaseController):

    @pyramid_handlers.action(renderer='templates/standings/standings.pt')
    def index(self):
        current_standings = StandingsService.display_weekly_standings()

        session = DbSessionFactory.create_session()
        season_row = session.query(SeasonInfo.current_season).filter(SeasonInfo.id == '1').first()
        season = season_row.current_season

        week_query = session.query(WeeklyPlayerResults.week).order_by(WeeklyPlayerResults.week.desc()).first()
        week = week_query[0]

        return {'current_standings': current_standings, 'season': season, 'week': week}

    @pyramid_handlers.action(renderer='templates/standings/player-standings.pt',
                             request_method='GET',
                             name='player-standings')
    def player_standings_get(self):
        vm = StandingsViewModel()
        vm.from_dict(self.data_dict)

        player = self.request.matchdict['id']

        player_standings = StandingsService.display_player_standings(player)

        first_name = (player_standings[0]['first_name'])
        last_name = (player_standings[0]['last_name'])

        return {'first_name': first_name, 'last_name': last_name, 'player_standings': player_standings}