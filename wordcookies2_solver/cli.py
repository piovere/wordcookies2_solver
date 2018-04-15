# -*- coding: utf-8 -*-

import click
from wordcookies2_solver.wordcookies2_solver import wordlist


@click.command()
@click.argument('letters')
@click.option('--length', default=None, type=int)
def main(letters, length=None):
    """Console script for wordcookies2_solver"""
    l = wordlist(letters, length=length)
    for w in l:
        click.echo(w)

@click.command()
def words(letters, length=None):
    l = wordlist(letters, length=length)
    for w in l:
        click.echo(w)

if __name__ == "__main__":
    main(letters, length=None)
