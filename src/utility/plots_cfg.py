import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

colors = cycler(color=plt.get_cmap("tab10").colors)  # ["b", "r", "g"]

mpl.style.use("ggplot")
mpl.rcParams["figure.figsize"] = (16, 9)
mpl.rcParams["axes.facecolor"] = "white"
mpl.rcParams["axes.grid"] = False
mpl.rcParams["grid.color"] = "lightgray"
mpl.rcParams["axes.prop_cycle"] = colors
mpl.rcParams["axes.linewidth"] = 1
mpl.rcParams["xtick.color"] = "black"
mpl.rcParams["ytick.color"] = "black"
mpl.rcParams["font.size"] = 12
mpl.rcParams["figure.titlesize"] = 24
mpl.rcParams["figure.dpi"] = 100
