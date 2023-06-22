# $ python -c "print('Real Python')"
import os
import sys
import platform
import click
import datetime


@click.command()
# @click.option("--name")
def sysinfo():
    click.echo(datetime.datetime.today())
    click.echo(platform.python_version())
    click.echo(os.name)
    
if __name__ == "__main__":
    sysinfo()
