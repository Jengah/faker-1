# coding=utf-8

from __future__ import print_function, unicode_literals

import click

from faker import VERSION, Faker, documentor
from faker.config import AVAILABLE_LOCALES, DEFAULT_LOCALE, META_PROVIDERS_MODULES


@click.group()
@click.option('--version', default=False)
def cli(version):
    if version:
