from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'donation_fixed',
        'display_name': "Donation - fixed endowment",
        'num_demo_participants': 1,
        'app_sequence': ['donation', ],
        'hetero': False,

    },
    {
        'name': 'donation_hetero',
        'display_name': "Donation - heterogeneous endowment",
        'num_demo_participants': 1,
        'app_sequence': ['donation', ],
        'hetero': True,
    },
    {
        'name': 'bmi_individ',
        'display_name': "BMI Index - Individual treatment",
        'num_demo_participants': 2,
        'app_sequence': ['bmi', ],
        'individual': True,
        'endowment': 90,
    },
    {
        'name': 'bmi_interpers',
        'display_name': "BMI Index - Interpersonal treatment",
        'num_demo_participants': 2,
        'app_sequence': ['bmi', ],
        'individual': False,
        'endowment': 90,
    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    {'name': 'hse',
     'display_name': 'HSE WORKSHOP'}
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'k*-$jw!t-0h+o7_3$rm=%68((^uo23^zud%mjmq96+c6a#s_cx'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
