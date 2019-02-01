from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import random


class Donation(Page):
    form_model = 'player'

    def get_form_fields(self):
        f = ['donation', 'charity']
        random.shuffle(f)
        return f

    def charity_choices(self):
        choices = json.loads(self.player.choice_order)
        return choices
    def donation_choices(self):
        choices = list(range(0, int(self.player.endowment), Constants.step))
        return choices

    def donation_max(self):
        # actually we don't need this taken into account we provide a set of choices which we generated
        # using as max a user's endowment
        # so the player is unable to select more than they have. but just for didactic reason, here it:
        return self.player.endowment

    def before_next_page(self):
        self.player.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Donation,
    Results,

]
