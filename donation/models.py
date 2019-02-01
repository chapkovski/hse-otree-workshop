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
    name_in_url = 'donation'
    players_per_group = None  # please pay attention that if there is a single player per group we insert None, not 1
    num_rounds = 1
    my_constant = 95
    lb = 50
    ub = 100
    step = 10
    endowment = 100
    CHARITY_CHOICES = ['Red cross', 'World Wide Fund for Nature', 'Salvation army']


class Subsession(BaseSubsession):
    # this variable is to store the info from our treatment. If true, each player will have their own endowment
    # otherwise it will be fixed (using endowment from settings, and if it not set - from constants).
    hetero_endowment = models.BooleanField(initial=False)

    def creating_session(self):

        # NB: if you use a list and then shuffle it you need to create a copy of the original list
        # because otherwise we will modify original list.
        # to know more about it, read this: https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
        charities = Constants.CHARITY_CHOICES.copy()
        hetero = self.session.config.get('hetero', False)

        for p in self.get_players():
            if hetero:
                p.endowment = random.randint(Constants.lb, Constants.ub)
            else:
                p.endowment = self.session.config.get('endowment', Constants.endowment)

            random.shuffle(charities)
            p.choice_order = json.dumps(charities)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice_order = models.StringField()
    charity = models.StringField(label='Please choose charity to donate to')
    donation = models.CurrencyField(widget=widgets.RadioSelect, label='How much you would like to donate')
    endowment = models.CurrencyField()

    def set_payoffs(self):
        self.payoff = self.endowment - self.donation
