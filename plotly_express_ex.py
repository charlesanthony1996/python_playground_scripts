import plotly
import plotly.express as px
import pandas as pd


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
    (df["Year"] >= 1791 )
]