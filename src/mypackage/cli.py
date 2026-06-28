"""Command-line interface for mypackage."""

import click

from mypackage.core import add


@click.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def main(a: int, b: int) -> None:
  """Add two integers A and B and print the result."""
  click.echo(add(a, b))


if __name__ == "__main__":
  main()
