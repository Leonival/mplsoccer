"""
============
Bumpy Charts
============

* ``mplsoccer``, ``bumpy_chart`` module helps one to plot bumpy charts in a few lines of code.

* Inspired By `CJ Mayes <https://public.tableau.com/profile/cj.mayes#!/vizhome/PremierLeagueStandings201920/PREMIERLEAGUE201920>`_

* Here we will show some examples of how to use ``mplsoccer`` to plot bumpy charts.
"""

from mplsoccer import Bumpy, FontManager, add_image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import json
from highlight_text import fig_text

##############################################################################
# Making A Bumpy Chart
# ----------------------------
# A Bump Chart is a special form of a line plot. This chart is well-suited for exploring changes in rank over time.
# Using this chart, you can easily compare the position, performance or rankings of multiple observations with 
# respect to each other rather than the actual values itself. We are going to make use of the weekwise standing data for Premier League 2019/20.
#
# `Link To The Data
# <https://github.com/Slothfulwave612/data/blob/master/football/season_2019_20/Premier_League.json>`__,
# `Link To The Image
# <https://github.com/Slothfulwave612/data/blob/master/football/logo/epl.png>`__.

# download fonts
font_normal = FontManager(
    "https://github.com/google/fonts/blob/main/apache/roboto/static/Roboto-Regular.ttf?raw=true"
)
font_italic = FontManager(
    "https://github.com/google/fonts/blob/main/apache/roboto/static/Roboto-Italic.ttf?raw=true"
)
font_bold = FontManager(
    "https://github.com/google/fonts/blob/main/apache/roboto/static/Roboto-Medium.ttf?raw=true"
)

# load the data
season_dict = json.load(open("epl.json"))

# match-week
match_day = ["Week " + str(num) for num in range(1, 39)]

# highlight dict --> team to highlight and their corresponding colors
highlight_dict = {
    "Liverpool": "crimson", 
    "Man City": "skyblue", 
    "Man Utd": "gold"
}

# instantiate object
bumpy = Bumpy(
    scatter_color="#282A2C", line_color="#252525", # scatter and line colors
    rotate_xticks=90, # rotate x-ticks by 90 degrees
    ticklabel_size=17, label_size=30, # ticklable and label font-size
    scatter_primary='D',  # marker to be used
    show_right=True,  # show position on the rightside
    plot_labels=True, # plot the labels 
    alignment_yvalue=0.1,  # y label alignment
    alignment_xvalue=0.065  # x label alignment
)

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=match_day,  # match-day or match-week 
    y_list=np.linspace(1,20,20).astype(int), # position value from 1 to 20
    values=season_dict,  # values having positions for each team
    secondary_alpha=0.5,   # alpha value for non-shaded lines/markers
    highlight_dict=highlight_dict, # team to be highlighted with their colors
    figsize=(20,16),  # size of the figure
    x_label='Week', y_label='Position',  # label name
    ylim=(-0.1, 23),  # y-axis limit
    lw=2.5,   # linewidht of the connecting lines
    fontproperties=font_normal.prop,   # fontproperties for labels
)

# title and subtitle
title = "Premier League 2019/20 week-wise standings:"
sub_title = "A comparison between <Liverpool>, <Manchester City> and <Manchester United>"

# add title
fig.text(0.09, 0.95, title, size=27, color="#F2F2F2", fontproperties=font_bold.prop)

# add subtitle
fig_text(
    0.09, 0.92, sub_title, color="#F2F2F2",
    highlight_textprops=[{"color": 'crimson'}, {"color": 'skyblue'}, {"color": 'gold'}],
    size=23, fig=fig, fontproperties=font_bold.prop
)

# add credits
fig.text(
    0.94, 0.01, "graphic: @slothfulwave612", size=13, 
    color="#F2F2F2", fontstyle="italic", 
    ha="right", fontproperties=font_italic.prop
)

# add image
image = Image.open("epl.png")
fig = add_image(
     image,
     fig,  # figure
     0.02, 0.9, # left and bottom dimensions
     0.08, 0.08 # height and width values
)

# if space is left in the plot use this
plt.tight_layout(pad=0.5)

##############################################################################
# Flip The y-axis
# ----------------------------
# If you want to plot positions from the bottom, i.e. the 1st position will
# be at the bottom and the 20th position will be at the top. You can do it easily.
# You just have to pass ``upside_down=True`` inside ``plot`` function.

# instantiate object
bumpy = Bumpy(
    scatter_color="#282A2C", line_color="#252525", # scatter and line colors
    rotate_xticks=90, # rotate x-ticks by 90 degrees
    ticklabel_size=17, label_size=30, # ticklable and label font-size
    scatter_primary='D',  # marker to be used
    show_right=True,  # show position on the rightside
    plot_labels=True, # plot the labels
    alignment_yvalue=0.1,  # y label alignment
    alignment_xvalue=0.065  # x label alignment
)

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=match_day,  # match-day or match-week 
    y_list=np.linspace(1,20,20).astype(int), # position value from 1 to 20
    values=season_dict,  # values having positions for each team
    secondary_alpha=0.5,   # alpha value for non-shaded lines/markers
    highlight_dict=highlight_dict, # team to be highlighted with their colors
    figsize=(20,16),  # size of the figure
    x_label='Week', y_label='Position',  # label name
    ylim=(-0.1, 23),  # y-axis limit
    lw=2.5,   # linewidht of the connecting lines
    fontproperties=font_normal.prop,   # fontproperties for labels
    upside_down=True,    # <--- to flip the y-axis
)

# title and subtitle
title = "Premier League 2019/20 week-wise standings:"
sub_title = "A comparison between <Liverpool>, <Manchester City> and <Manchester United>"

# add title
fig.text(0.09, 0.95, title, size=27, color="#F2F2F2", fontproperties=font_bold.prop)

# add subtitle
fig_text(
    0.09, 0.92, sub_title, color="#F2F2F2", 
    highlight_textprops=[{"color": 'crimson'}, {"color": 'skyblue'}, {"color": 'gold'}],
    size=23, fig=fig, fontproperties=font_bold.prop
)

# add credits
fig.text(
    0.94, 0.01, "graphic: @slothfulwave612", size=13, 
    color="#F2F2F2", fontstyle="italic", 
    ha="right", fontproperties=font_italic.prop
)

# add image
image = Image.open("epl.png")
fig = add_image(
     image,
     fig,  # figure
     0.02, 0.9, # left and bottom dimensions
     0.08, 0.08 # height and width values
)

# if space is left in the plot use this
plt.tight_layout(pad=0.5)

##############################################################################
# Light Theme
# ----------------------------
# You can use ``background_color``, ``scatter_color``, ``label_color``, and ``line_color`` arguments
# to change the whole theme of the plot. Below is the code demonstrating how to make a light-theme
# bumpy chart using ``mplsoccer``.
# Below you can also use ``scatter_points``, ``scatter_primary``, and ``scatter_size`` arguments inside ``Bumpy`` method to change markers
# and thier sizes.

# highlight dict --> team to highlight and their corresponding colors
highlight_dict = {
    "Man Utd": "crimson", 
    "Chelsea": "blue"
}

# instantiate object
bumpy = Bumpy(
    background_color="#F6F6F6", scatter_color="#808080", 
    label_color="#000000", line_color="#C0C0C0",
    rotate_xticks=90, # rotate x-ticks by 90 degrees
    ticklabel_size=17, label_size=30, # ticklable and label font-size
    scatter_points='D',   # other markers
    scatter_primary='o',  # marker to be used for teams
    scatter_size=150,   # size of the marker
    show_right=True,  # show position on the rightside
    plot_labels=True, # plot the labels
    alignment_yvalue=0.1,  # y label alignment
    alignment_xvalue=0.065  # x label alignment
)

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=match_day,  # match-day or match-week 
    y_list=np.linspace(1,20,20).astype(int), # position value from 1 to 20
    values=season_dict,  # values having positions for each team
    secondary_alpha=0.2,   # alpha value for non-shaded lines/markers
    highlight_dict=highlight_dict, # team to be highlighted with their colors
    figsize=(20,16),  # size of the figure
    x_label='Week', y_label='Position',  # label name
    ylim=(-0.1, 23),  # y-axis limit
    lw=2.5,   # linewidht of the connecting lines
    fontproperties=font_normal.prop,   # fontproperties for labels
)

# title and subtitle
title = "Premier League 2019/20 week-wise standings:"
sub_title = "A comparison between <Manchester United> and <Chelsea>"

# add title
fig.text(0.03, 0.95, title, size=27, color="#222222", fontproperties=font_bold.prop)

# add subtitle
fig_text(
    0.03, 0.92, sub_title, color="#222222", 
    highlight_textprops=[{"color": 'crimson'}, {"color": 'blue'}],
    size=23, fig=fig, fontproperties=font_bold.prop
)

# add credits
fig.text(
    0.94, 0.01, "graphic: @slothfulwave612", 
    size=13, color="#222222", fontstyle="italic", 
    ha="right", fontproperties=font_italic.prop
)

# if space is left in the plot use this
plt.tight_layout(pad=0.5)

##############################################################################
# Player Percentile Rank Viz
# ----------------------------
# Here we will create a bumpy-chart that will compare two players based on their percentile rank.
# `Link To The Data
# <https://github.com/Slothfulwave612/data/blob/master/football/percentile.json>`_

# load the data
player_dict = json.load(open("percentile.json"))

# attributes and highlight dict
attribute = [
    "xA", "Passes\nInto Pen", "Passes\nInto Final 1/3", "Progressive\nPass Distance", "Pass\nReceive%", "Progressive\nCarry Distance"
]
highlight_dict = {
    "Cristián Zapata": "crimson", 
    "Francesco Acerbi": "cornflowerblue"
}

# instantiate object
bumpy = Bumpy(
    rotate_xticks=0, ticklabel_size=17, label_size=25, scatter="value",
    show_right=True, alignment_yvalue=0.15, alignment_xvalue=0.06
) 

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=attribute, y_list=np.linspace(1, 100, 11).astype(int), values=player_dict, 
    secondary_alpha=0.05, highlight_dict=highlight_dict, 
    figsize=(20,12), 
    x_label="Attributes", y_label="Percentile Rank", ylim=(0.5, 12),
    fontproperties=font_normal.prop, 
    upside_down=True
)

# title and subtitle
title = "Comparison Between <Cristián Zapata> and <Francesco Acerbi>"

# add title
fig_text(
    0.02, 0.95, title, color="#F2F2F2",
    highlight_textprops=[{"color": 'crimson'}, {"color": 'cornflowerblue'}],
    size=34, fig=fig, fontproperties=font_bold.prop
)

# add credits
fig.text(
    0.99, 0.01, "graphic: @slothfulwave612", 
    size=15, color="#F2F2F2", fontstyle="italic", 
    ha="right", fontproperties=font_italic.prop
)

# if space is left in the plot use this
plt.tight_layout(pad=0.5)
