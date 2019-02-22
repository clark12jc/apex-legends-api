class PlayerStats():
    def __init__(self, username, platform_id, kills, level, percentile):
        self.username = username
        self.platform_id = platform_id
        self.kills = kills
        self.level = level
        self.percentile = percentile
        self.date = ''
        self.time = ''

    def to_dict(self):
        dict = {
            'username': self.username,
            'platform_id': self.platform_id,
            'kills': self.kills,
            'level': self.level,
            'percentile': self.percentile,
            'date': self.date,
            'time': self.time
        }
        return dict


class Legend():
    def __init__(self, name, kills, rank, percentile):
        self.name = name
        self.kills = kills
        self.rank = rank
        self.percentile = percentile

    def to_dict(self):
        dict = {
            'name': self.name,
            'kills': self.kills,
            'rank': self.rank,
            'percentile': self.percentile
        }
        return dict
