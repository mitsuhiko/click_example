from __future__ import print_function

import click

@click.group()
@click.option('-d', '--debug', count=True, help="more debugging stuff")
@click.pass_context
def main(ctx, debug):
    ctx.obj['DEBUG'] = debug

@main.command()
@click.pass_context
@click.argument('name')
def hello(ctx, name):
    """Say hello name
    """
    if ctx.obj['DEBUG']:
        print("Assuming your name is {}...".format(name))
    print("hello {}!".format(name))

