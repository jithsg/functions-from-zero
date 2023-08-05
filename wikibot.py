# use click cli tool to create a command line interface to the bot
import click

# import the scrape function from mylib/bot.py
from mylib.bot import scrape


@click.command()
@click.option(
    "--name",
    help="The name of the entity to scrape from Wikipedia.",
)
def cli(name="facebook"):
    """Simple program that scrapes a specified number of sentences from Wikipedia."""

    result = scrape(name)
    click.echo(result)


if __name__ == "__main__":
    cli()
