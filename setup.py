from setuptools import setup, find_packages

import blahcli

setup_options = dict(
    name = 'blah',
    version = blahcli.__version__,
    packages = find_packages(),
    #scripts = ['blah'],
    entry_points = '''
                [console_scripts]
                blah=blahcli.blah:main
                   '''
)


setup(**setup_options)

