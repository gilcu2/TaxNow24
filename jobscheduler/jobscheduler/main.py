"""Console script for jobscheduler."""
import sys
import click


@click.command()
def main(args=None) -> int:
    """Console script for jobscheduler."""
    click.echo(
        "Replace this message by putting your code into jobscheduler.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
