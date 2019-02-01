from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        choices = list(range(0, int(self.player.endowment), Constants.step))
        yield (pages.Donation, {'donation': random.choice(choices),
                                'charity': random.choice(Constants.CHARITY_CHOICES)})
        yield (pages.Results)
