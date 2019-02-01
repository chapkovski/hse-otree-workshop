from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""
import json


class Constants(BaseConstants):
    name_in_url = 'firstapp'
    players_per_group = 2
    num_others = players_per_group - 1
    num_rounds = 1
    my_constant = 95
    lb = 50
    ub = 100
    don_choices = [10, 20]


class Subsession(BaseSubsession):
    def creating_session(self):
        choices = Constants.don_choices.copy()
        for p in self.get_players():
            p.endowment = random.randint(Constants.lb, Constants.ub)
            random.shuffle(choices)
            p.choice_order = json.dumps(choices)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice_order = models.StringField()
    donation = models.CurrencyField(choices=[10, 20],
                                    widget=widgets.RadioSelectHorizontal)
    age = models.IntegerField()
    endowment = models.CurrencyField()

    def set_payoffs(self):
        self.payoff = self.endowment - self.donation
