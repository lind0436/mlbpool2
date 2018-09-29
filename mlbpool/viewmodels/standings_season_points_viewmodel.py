from mlbpool.viewmodels.viewmodelbase import ViewModelBase


class StandingsPointsViewModel(ViewModelBase):
    def __init__(self):
        self.season = None
        self.season_id = None
        self.is_get = True

    def from_dict(self, data_dict):
        # reset_code will be third part of URL:
        #      /account/reset_password/f8489375729a
        # that is always id in our routing scheme
        self.season_id = data_dict.get("id")
