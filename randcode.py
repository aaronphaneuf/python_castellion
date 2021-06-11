import calmap
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

today = date.today()
def create_dfs():
    try:
        df = pd.read_pickle("./castellion_stats.pkl")
        df2 = pd.read_pickle("./castellion_winloss.pkl")
    except:
        df = pd.DataFrame({'Date': today, 'Count' : 1}, index=[0])
        df2 = pd.DataFrame({'Wins': 0, 'Games' : 1}, index=[0])
    dates = [today]
    if df.Date.isin(dates).any():
        df.loc[df.Date.isin(dates), 'Count'] += 1
    else:
        df = df.append({'Date': today, 'Count' : 1}, ignore_index=True)
    df2['Games'][0] += 1
    print(df2['Games'])
    df['Date']= pd.to_datetime(df['Date'])
    df.to_pickle("./castellion_stats.pkl")
    df2.to_pickle("./castellion_winloss.pkl")
    df.set_index('Date', inplace=True)
    plt.figure(figsize=(16,10), dpi=80)
    calmap.calendarplot(df['2021']['Count'], fig_kws={
        'figsize': (16,10)}, yearlabel_kws={'color':'black', 'fontsize':14},
        subplot_kws={'title':'Days Played'}, cmap='YlOrRd')
    plt.savefig('heatmap.png', bbox_inches='tight')
    return df2

def create_pi(df2):
    labels = ['Games Played', 'Victories']
    sizes = [df2['Games'][0], df2['Wins'][0]]
    colors = ['#7b0c52','#bd1831']
    explode = [0, 0.1]
    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(sizes, explode=explode, colors
        = colors, labels=labels, autopct='%1.1f%%', startangle=60, shadow=True,
        textprops={'fontsize': 16})

    for text in texts:
        text.set_color('#414141')
    for autotext in autotexts:
        autotext.set_color('white')
    ax1.axis('equal')
    plt.tight_layout()
    ax1.patch.set_alpha(0.5)
    ax1.patch.set_facecolor('#4c1b25')
    ax1.set_facecolor("#4c1b25")
    plt.savefig('piechart.png', bbox_inches='tight')
