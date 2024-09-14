def export_figs(export_dir: str, fig: str, fig_number: int, filename: str) -> None:
    """function to export figures generated with matplotlib/seaborn.

    Converts figures to png format and saves them to a specified directory.

    Args:
        export_dir (str): the directory to export the figure to.
        fig (str): the figure generated to export.
        fig_number (str): the number of the figure based on it's position in the list.
        filename (str): the name you want to give the figure.
    """

    import os

    formatted_number: str = f"fig_{fig_number:03d}"
    prefixed_filename: str = f"{formatted_number}_{filename}"
    filepath: str = os.path.join(export_dir, prefixed_filename)
    fig.savefig(filepath)
