import click

@click.command()
@click.option('--count', default=1, help='Number of Greetings')
@click.argument('name')
def hello(count, name):
    for i in range(count):
        click.echo(f"Greetings {name}")

if __name__ == '__main__':
    hello()

