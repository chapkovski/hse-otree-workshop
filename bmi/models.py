from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Philipp Chapkovski'

doc = """
Simple BMI app for HSE workshop (see Readme)
original bmi index chart is taken from here:
https://bmicalculator.mes.fm/bmi-chart
"""


class BMI:
    def __init__(self, name, left, right, alert):
        self.name = name
        self.left = left
        self.right = right
        self.alert = alert

    def check_if_in(self, val):
        if self.left <= val < self.right:
            return self


class Constants(BaseConstants):
    name_in_url = 'bmi'
    players_per_group = None
    num_rounds = 1
    bmi_info = [
        BMI('Underweight', 0, 18.5, 'alert-primary'),
        BMI('Normal', 18.5, 25, 'alert-success'),
        BMI('Overweight', 25, 30, 'alert-warning'),
        BMI('Obese', 30, 40, 'alert-danger'),
        BMI('Extremely Obese', 40, 1000, 'alert-danger')
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    weight = models.IntegerField(min=10, max=300)
    height = models.IntegerField(min=100, max=250)

    def get_bmi(self):
        return round(self.weight / (self.height / 100) ** 2, 2)

    def get_bmi_info(self):
        for c in Constants.bmi_info:
            if c.check_if_in(self.get_bmi()):
                return c

    def get_other(self):
        return self.get_others_in_group()[0]
