import plotly
import plotly.express as px
import pandas as pd
import numpy as np


# load the statehood data and prepare a "Year" column
df = pd.read_csv("https://bit.ly/44qtTyk")
df["Year"] = df["date_entered"].str[-4:].astype("int")
# print(df.head())
# print(df.tail())


# plot the dataframe as a static map
fig = px.choropleth(
    df,
    locations="abbr",
    locationmode="USA-states",
    color="Year",
    color_continuous_scale=px.colors.diverging.Portland,
    scope="usa",
    hover_data=["state", "order", "Year"],
    title="State by date of entry into union"
)

fig.update_layout(width=750, height=750)
# fig.show()


# plot the dataframe as an animation showing each state in order of admission
fig = px.choropleth(
    df,
    locations="abbr",
    locationmode="USA-states",
    color="Year",
    color_continuous_scale=px.colors.diverging.Earth,
    scope="usa",
    hover_data=["state", "order"],
    animation_frame="date_entered",
    range_color=(min(df.Year), max(df.Year)),
    title="The date each state entered the union"
)

fig.update_layout(width=750, height=500)

# fig.show()

# animate the states grouped by year of admission
fig = px.choropleth(
    df,
    locations="abbr",
    locationmode="USA-states",
    color="Year",
    color_continuous_scale=px.colors.diverging.Earth,
    scope="usa",
    hover_data=["state", "order"],
    animation_frame="Year",
    range_color=(min(df.Year), max(df.Year))
)

fig.update_layout(width=750, height=500)

# fig.show()

# animate the states grouped by large timeframes
conditions = [
    (df["Year"] >= 1787) & (df['Year'] <= 1790),
    (df["Year"] >= 1791) & (df["Year"] <= 1860),
    (df["Year"] >= 1861) & (df["Year"] <= 1900),
    (df["Year"] >= 1901) & (df["Year"] <= 1959)
]

values = ["Original 13 colonies", "Antebellum Expansion", "Westward expansion", "Twentieth century"]

df["Timespan"] = np.select(conditions, values)

# animate the states grouped by year of admission
fig = px.choropleth(
    df,
    locations="abbr",
    locationmode="USA-states",
    color="Year",
    color_continuous_scale=px.colors.diverging.Earth,
    scope="usa",
    hover_data = ["state", "order"],
    animation_frame = "Timespan",
    range_color=(min(df.Year), max(df.Year)),

)

fig.update_layout(width=750, height=500)

# fig.show()

# set the animation speed (in milliseconds)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"]= 2000
# fig.show()


# make static maps of the states grouped over large timeframes

# create new dataframes for designed time spans
original_13 = df[(df["Year"] >= 1787) & (df["Year"] <= 1790)].copy()
antebellum_expansion = df[(df["Year"] >= 1791) & (df["Year"] <= 1860)].copy()
western_expansion = df[(df['Year'] >= 1861) & (df['Year'] <= 1900)].copy()
twentieth_century = df[(df['Year'] >= 1901) & (df['Year'] <= 1959)].copy()

# print(original_13)
# print(antellebellum_expansion)
# print(western_expansion)
# print(twentieth_century)


# make a list of dataframes to loop through
time_frames = [original_13, antebellum_expansion, western_expansion, twentieth_century]


# make a list of the dates you want to see in the color bar
colorbar_dates = [[1787, 1788, 1789, 1790],
                  [1791, 1800, 1810, 1820, 1830, 1840, 1850, 1859],
                  [1861, 1870, 1880, 1890, 1896],
                  [1907, 1920, 1930, 1940, 1950, 1959]]


# make a list of of the figure titles for each dataframes
figure_titles = ["Original 13 Colonies (1787-1790)", 
                 "Antebellum Expansion (1791-1860)", 
                 "Western Expansion (1861-1900)", 
                 "Twentieth Century (1901-1959)"]


# loop through and plot the dataframes
for i, data_frame in enumerate(time_frames):
    fig = px.choropleth(
        data_frame,
        locations="abbr",
        locationmode="USA-states",
        color="Year",
        
    )