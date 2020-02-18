"""



"""

import click

from .all_my_shut import do_my_super_path_stuff


@click.command()
@click.option('--graph-path', required=True, type=click.Path(dir_okay=False, file_okay=True), help='Path to networkx pickle file')
@click.option('--df-path', required=True, help='Path to TSV file')
@click.option('--output-path', required=True, help='Where to stick output TSV file')
@click.option('--dgxp-threshold', default=2.0, show_default=True, type=float, help='What makes a gene differentially expressed?')
def cli(graph_path: str, df_path: str, output_path: str, dgxp_threshold):
    print('Doing my super path stuff')
    print(graph_path)
    print(df_path)
    print(output_path)
    print(dgxp_threshold)
    do_my_super_path_stuff(graph_path, df_path, output_path)


if __name__ == '__main__':
    cli()
