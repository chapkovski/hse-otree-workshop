from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'firstapp'
    players_per_group = None
    num_rounds = 1
    endowment = 100

class Subsession(BaseSubsession):
    endowment = models.IntegerField()
    def creating_session(self):
        self.endowment = self.session.config.get('endowment',
                                                 Constants.endowment)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=18, max=100)
