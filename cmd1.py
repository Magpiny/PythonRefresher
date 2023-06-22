#!/usr/bin/python

# $ python -c "print('Real Python')" 
import os
import sys
import platform
import click
import datetime

@click.command()
# @click.option("--name")
def sysinfo(name=platform.release()):
    click.echo(f"Time: {datetime.datetime.now()}")
    click.echo(f"Python version: {platform.python_version()}")
    click.echo(f"Operating System: {name}")
    
if __name__ == "__main__":
    sysinfo()


