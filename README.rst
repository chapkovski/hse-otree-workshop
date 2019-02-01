.. class:: center

This paragraph will be centered.

.. image:: https://www.hse.ru/data/2012/01/19/1263884289/logo_%D1%81_hse_cmyk_e.png
    :width: 100px





oTree Workshop
==============

HSE-Moscow, 30 January 2019
---------------------------



We developed two very simple games on the course of the workshop.

1. BMI index

2. Donation (Dictator's game)

BMI
---

This app consists of two stages:

1. A person inserts their height and weight

2.1. In ``individual`` treatment a person can see their BMI index only
2.2. In ``interpersonal`` treatment a person can see their partner's BMI index as well.

Treatments can be changed using a parameter ``individual`` in
``settings.py`` file or when you start a new session.

Donation
--------

This game consists of one stage only.

A person has to donate a certain share of their endowment
to a charity. A person's individual endowment can be fixed
(in ``fixed`` treatment) or heterogeneous - randomly generated
within certain limits (``hetero`` treatment).



Tests
-----

In each app there is a file named ``tests.py``.
You can check if the code works properly by typing::

    otree test

or for the specific configuration and number of bots::

    otree test bmi_interpers 100 --export

The code above will run a test session for BMI game with ``interpersonal``
treatment for 100 bots and will save the data in  a temporary export folder.
The ``bmi_interpers`` is just a name of this configuration from
``settings.py``.




:Authors:
    Philipp Chapkovski, HSE-Moscow, chapkovski@gmail.com


:Version: 1.0 of 01/02/2019


