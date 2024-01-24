import pandas
import plotly.graph_objects as go


def generate():
    DATE = '3/22/20'
    read_df = pandas.read_csv('data/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

    df = pandas.DataFrame()
    df['country'] = read_df['Country/Region']
    df['province'] = read_df['Province/State']
    df['lat'] = read_df['Lat']
    df['lon'] = read_df['Long']
    df['value'] = read_df[DATE]
    df['text'] = df['country'] + '<br>Confirmed ' + (df['value']).astype(str)

    fig = go.Figure()
    limits = [(0, 99), (100, 499), (500, 999), (1000, 9999), (10000, 99999)]
    colors = ["#00FF00", "#55FF00", "#AAAA00", "#FF5500", "#FF0000"]

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df.loc[df['value'] >= lim[0]]
        df_sub = df_sub.loc[df['value'] <= lim[1]]
        fig.add_trace(go.Scattergeo(
            name=f'{lim[0]} - {lim[1]}',
            locationmode='ISO-3',
            lon=df_sub['lon'],
            lat=df_sub['lat'],
            text=df_sub['text'],
            marker=dict(
                size=df_sub['value'] / 10,
                color=colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode='area'
            )
        ))

    fig.update_layout(
            title_text=f'COVID-19 ({DATE})',
            showlegend=True,
            geo=dict(
                scope='world',
                landcolor='rgb(217, 217, 217)',
            )
        )

    fig.show()
