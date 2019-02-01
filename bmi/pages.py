from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Input(Page):
    form_model = 'player'
    form_fields = ['height', 'weight']


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return not self.session.config.get('individual')

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Input,
    ResultsWaitPage,
    Results
]
