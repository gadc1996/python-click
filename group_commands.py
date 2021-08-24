import click

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    click.echo('Database Initialized')

@cli.command()
def drop_db():
    click.echo('Database Droped')

if __name__ == '__main__':
    cli()
