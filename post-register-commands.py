import click

@click.command()
def greet():
    click.echo('Greetings')

@click.group()
def group():
    pass

group.add_command(greet)

if __name__ == '__main__':
    group()
