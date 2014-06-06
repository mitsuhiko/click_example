from __future__ import print_function

import click

pass_dict = click.make_pass_decorator(dict, ensure=True)

@click.group()
@click.option('-d', '--debug', count=True, help="more debugging stuff")
@pass_dict
def main(obj, debug):
    obj['DEBUG'] = debug

@main.command()
@click.argument('name')
@pass_dict
def hello(obj, name):
    """Say hello name
    """
    if obj['DEBUG']:
        print("Assuming your name is {}...".format(name))
    print("hello {}!".format(name))

