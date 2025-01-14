import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('SF Trees')
st.write(
    """This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW"""
)

trees_df = pd.read_csv('trees.csv')
st.write(trees_df.head())

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)

# the following bit of code turns the index into its own column and then graphs a line chart
st.write("Graphing the index turned into column")
trees_df2 = pd.read_csv("trees.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"]).reset_index()
df_dbh_grouped.columns = ["dbh", "tree_count"]
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")

# we are going to sample 1,000 random rows from our DataFrame, remove null values, and try out
# st.map() using the following code
trees_df3 = pd.read_csv('trees.csv')
trees_df3 = trees_df3.dropna(subset=['longitude', 'latitude'])
trees_df3 = trees_df3.sample(n = 1000)
st.map(trees_df3)

# We’ll test this out by making a histogram of the height of trees
# in SF, essentially the same graph that we’ve made before.
st.subheader('Plotly Chart')
trees_df = pd.read_csv('trees.csv')
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

# The following code creates a new column called age, which is the
# difference in days between the tree planting date and today’s date,
# and then graphs the histogram of the age using both Seaborn and
# Matplotlib.
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

st.write("# Seaborn and Matplotlib Charts:")

trees_df = pd.read_csv('trees.csv')
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days
st.subheader('Seaborn Chart')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_sb)

st.subheader('Matploblib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_mpl)

# we run the following code, we will not see a new x axis title at all
# COMENTADO POR APRESENTAR ERRO NA VERSÃO RECENTE DO STREAMLIT NA DATA DESTE REPOSITÓRIO
#from bokeh.plotting import figure

#st.subheader('# Bokeh Chart')
#trees_df = pd.read_csv('trees.csv')
#scatterplot = figure(title = 'Bokeh Scatterplot')
#scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
#st.bokeh_chart(scatterplot)
#scatterplot.xaxis.axis_label = "dbh"

# The following code groups our DataFrame by caretaker, and then
# uses that grouped DataFrame from within Altair.
import altair as alt

st.write('# Altair Chart')
trees_df = pd.read_csv('trees.csv')
df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x = 'caretaker', y = 'tree_count')
st.altair_chart(fig)

# Altair also allows us to summarize our data directly within the
# y value of mark_bar(), so we can simplify this by instead using
# the following code
trees_df = pd.read_csv('trees.csv')
fig = alt.Chart(trees_df).mark_bar().encode(x = 'caretaker', y =
'count(*):Q')
st.altair_chart(fig)