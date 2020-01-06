# coding=utf-8

from __future__ import print_function, unicode_literals

import logging
import sys

import click

from faker import VERSION, Faker, documentor
from faker.config import AVAILABLE_LOCALES, DEFAULT_LOCALE, META_PROVIDERS_MODULES


def print_doc(provider_or_field=None, lang=DEFAULT_LOCALE):
    fake = Faker(locale=lang)
    print(fake.format(provider_or_field),
          end='')


@click.group(invoke_without_command=True)
@click.option('-l', '--lang',
              default=DEFAULT_LOCALE,
              type=click.Choice(AVAILABLE_LOCALES, case_sensitive=True),
              help="specify the language for a localized provider (e.g. de_DE)")
@click.option('-r', '--repeat',
              default=1,
              type=int,
              help="generate the specified number of outputs")
@click.option('-s', '--sep',
              default='\n',
              help="use the specified separator after each output")
@click.option('-v', '--verbose',
              is_flag=True,
              default=False,
              help="""
Show INFO logging events instead of CRITICAL, which is the default. These logging events provide insight into
localization of specific providers
""")
@click.option('--version',
              is_flag=True,
              default=False)
@click.argument('fake',
                required=False)
def cli(fake, lang, repeat, sep, verbose, version):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.CRITICAL)

    if version:
        click.echo("faker {}".format(VERSION))

    if fake:
        for i in range(repeat):
            print_doc(fake, lang=lang)
            print(sep)
