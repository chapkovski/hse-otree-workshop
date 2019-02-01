from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['height', 'weight']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(self):
        fat = self.player.get_bmi() > 30
        return {'fat': fat}


import random
import json


class Donation(Page):
    form_model = 'player'

    def get_form_fields(self):
        return ['donation']

    def donation_choices(self):
        choices = json.loads(self.player.choice_order)
        return choices

    def donation_max(self):
        return self.player.endowment

    def before_next_page(self):
        self.player.set_payoffs()


class TrustorPage(Page):
    def is_displayed(self):
        return self.player.role() == 'trustor'


class TrustorInstruction(TrustorPage):
    def is_displayed(self):
        return self.round_number == 1 and super().is_displayed()


class TrustorDecision(TrustorPage):
    pass


class TrustorResults(TrustorPage):
    pass


class TrusteeInstruction(Page):
    pass


class TrusteeDecision(Page):
    pass


class TrusteeResults(Page):
    pass


page_sequence = [
    Donation,
    # MyPage,
    # ResultsWaitPage,
    # Results,

]
