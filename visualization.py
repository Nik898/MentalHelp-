from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
#from plotly.offline import iplot, init_notebook_mode
#init_notebook_mode(connected = True)



def visual(request):
    labels = ['14-16', '17-19', '20-22', '23-25', '25+']
    values = [27, 138, 129, 35, 26]
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.5, 0.5],
        row_heights=[0.5],
        specs=[[{"type": "pie"}, {"type": "bar"}]])

    fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        legendgroup="group",
        marker=dict(colors=colors, line=dict(color='#000000', width=2)),
        textinfo='percent+label',
        hole=.4,
        pull=[0, 0, 0, 0, 0],
        hoverinfo="label+percent+name",
        name="Age"),
        row=1, col=1)

    fig.add_trace(go.Bar(
        y=labels,
        x=values,
        legendgroup="group",
        marker_line_color='#000000',
        name="Age",
        orientation='h',
        marker_color=colors),
        row=1, col=2)

    # fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
        showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        xaxis=dict(
            title='Frequency',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="AGE")

    g1 = fig.to_html()

    labels = ['Male', 'Female']
    values = [181, 174]
    colors = ['darkorange', 'mediumturquoise']
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.5, 0.5],
        row_heights=[0.5],
        specs=[[{"type": "pie"}, {"type": "bar"}]])

    fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        legendgroup="group",
        marker=dict(colors=colors, line=dict(color='#000000', width=2)),
        textinfo='percent+label',
        hole=.4,
        pull=[0, 0, 0, 0, 0],
        hoverinfo="label+percent+name",
        name="Gender"),
        row=1, col=1)

    fig.add_trace(go.Bar(
        y=labels,
        x=values,
        legendgroup="group",
        marker_line_color='#000000',
        name="Gender",
        orientation='h',
        marker_color=colors),
        row=1, col=2)

    # fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
        showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        xaxis=dict(
            title='Frequency',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="GENDER")

    g2 = fig.to_html()

    labels = ['School', 'Jr.College', 'Graduation', 'Post Grad', 'Others']
    values = [27, 55, 214, 32, 27]
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.5, 0.5],
        row_heights=[0.5],
        specs=[[{"type": "pie"}, {"type": "bar"}]])

    fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        legendgroup="group",
        marker=dict(colors=colors, line=dict(color='#000000', width=2)),
        textinfo='percent+label',
        hole=.4,
        pull=[0, 0, 0, 0, 0],
        hoverinfo="label+percent+name",
        name="Education"),
        row=1, col=1)

    fig.add_trace(go.Bar(
        x=labels,
        y=values,
        legendgroup="group",
        marker_line_color='#000000',
        name="Education",
        marker_color=colors),
        row=1, col=2)

    # fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
        showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        xaxis=dict(
            title='Frequency',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="OCCUPATION")


    g3 = fig.to_html()

    return render(request,'visualization.html',{"graph1":g1,"graph2":g2,"graph3":g3})

def waa(request):
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots
    dict_ = {}
    dict_['Male'] = [56, 125]
    dict_['Female'] = [71, 103]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Yes", 1: "No"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    fig = go.Figure()
    colors = ['mediumturquoise', 'lightgreen']
    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color='mediumturquoise',
            name="Yes"
        )
    )
    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color='lightgreen',
            name='No'
        ))
    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Drastic Weight Change")

    colors = ['mediumturquoise', 'lightgreen']
    labels = ["Male", "Female"]
    fig11 = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Have Had Drastic Weight Change ', "Haven't had Drastic Weight Change"])
    fig11.add_trace(go.Pie(labels=labels, values=[56, 71], pull=[0, 0.2],
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig11.add_trace(go.Pie(labels=labels, values=[125, 103], pull=[0.2, 0],
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig11.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    dict2_ = {}
    dict2_['Male'] = [70, 111]
    dict2_['Female'] = [85, 89]
    df2 = pd.DataFrame(dict2_)
    df2.rename(index={0: "Yes",
                     1: "No"},
              inplace=True)
    df2 = df2.transpose()
    a1 = df2[[df2.columns[0]]]
    b1 = df2[[df2.columns[1]]]
    aa1 = a1[[a1.columns[0]]].values
    bb1 = b1[[b1.columns[0]]].values
    fig2 = go.Figure()
    colors = ['mediumturquoise', 'lightgreen']

    fig2.add_trace(
        go.Bar(
            x=a.index,
            y=[aa1[0][0], aa1[1][0]],
            marker_line_color='#000000',
            marker_color='mediumturquoise',
            name="Yes"
        )
    )

    fig2.add_trace(
        go.Bar(
            x=b.index,
            y=[bb1[0][0], bb1[1][0]],
            marker_line_color='#000000',
            marker_color='lightgreen',
            name='No'
        ))

    fig2.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Appetite Change")

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['mediumturquoise', 'lightgreen']
    labels = ["Male", "Female"]
    fig22 = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Have Had Drastic Change in appetite',
                                        "Haven't had drastic change in appetite"])
    fig22.add_trace(go.Pie(labels=labels, values=[70, 85], pull=[0, 0.2],
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig22.add_trace(go.Pie(labels=labels, values=[111, 89], pull=[0.2, 0],
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig22.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    graph1 = fig.to_html()
    graph2 = fig11.to_html()
    graph3 = fig2.to_html()
    graph4 = fig22.to_html()

    return render(request,'weight_appetite.html',{"g1":graph1,"g2":graph2,"g3":graph3,"g4":graph4})

def graph3(request):
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots
    dict_ = {}
    dict_['Male'] = [17, 22, 88, 42, 11]
    dict_['Female'] = [9, 17, 74, 58, 17]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Irritation/Annoyance")

    g1 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Irritation/Annoyance in Male', 'Irritation/Annoyance in Female'])
    fig.add_trace(go.Pie(labels=labels, values=[17, 22, 88, 42, 11], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[9, 17, 74, 58, 17], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g11 = fig.to_html()

    dict_ = {}
    dict_['Male'] = [35, 66, 44, 26, 9]
    dict_['Female'] = [11, 32, 61, 52, 19]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Emotional Breakdown")


    g2 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Emotional Breakdowns in Male', 'Emotional Breakdowns in Female'])
    fig.add_trace(go.Pie(labels=labels, values=[35, 66, 44, 26, 9], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[11, 32, 61, 52, 19], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g22 = fig.to_html()

    dict_ = {}
    dict_['Male'] = [37, 43, 69, 20, 11]
    dict_['Female'] = [23, 27, 86, 23, 16]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Feeling Unhappy and Blue")

    g3 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Male', 'Female'])
    fig.add_trace(go.Pie(labels=labels, values=[35, 66, 44, 26, 9], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[11, 32, 61, 52, 19], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g33 = fig.to_html()

    return render(request,'graph3.html',{"graph1":g1,"graph11":g11,"graph2":g2,"graph22":g22,"graph3":g3,"graph33":g33})

def graph4(request):
    dict_ = {}
    dict_['14-16'] = [0, 9, 0, 18, 0]
    dict_['17-19'] = [20, 35, 46, 30, 7]
    dict_['20-22'] = [23, 22, 42, 30, 12]
    dict_['23-25'] = [6, 4, 13, 8, 4]
    dict_['25+'] = [8, 3, 6, 6, 3]

    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0], aa[2][0], aa[3][0], aa[4][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0], bb[2][0], bb[3][0], bb[4][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0], cc[2][0], cc[3][0], cc[4][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0], dd[2][0], dd[3][0], dd[4][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0], ee[2][0], ee[3][0], ee[4][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Losing Interest in things they enjoy")
    g1 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["14-16", "17-19", "20-22", "23-25", "25+"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Losing Interest', 'Not losing Interest'])
    fig.add_trace(go.Pie(labels=labels, values=[9, 55, 55, 10, 11], pull=[0, 0, 0, 0, 0], hole=.4, name="Yes",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[18, 37, 42, 12, 9], pull=[0, 0, 0, 0, 0], hole=.4, name="No",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[23,22,42,30,12],pull=[0,0,0,0,0.2],hole=.4,name="20-22",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    # fig.add_trace(go.Pie(labels=labels, values=[6,4,13,8,4],pull=[0,0,0,0,0.2],hole=.4,name="23-25",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[8,3,6,6,3],pull=[0,0,0,0,0.2],hole=.4,name="25+",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g11 = fig.to_html()

    dict_ = {}
    dict_['14-16'] = [0, 13, 24, 8, 8]
    dict_['17-19'] = [0, 40, 19, 1, 3]
    dict_['20-22'] = [0, 48, 44, 24, 6]
    dict_['23-25'] = [27, 25, 28, 2, 7]
    dict_['25+'] = [0, 12, 14, 0, 2]

    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0], aa[2][0], aa[3][0], aa[4][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0], bb[2][0], bb[3][0], bb[4][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0], cc[2][0], cc[3][0], cc[4][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0], dd[2][0], dd[3][0], dd[4][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0], ee[2][0], ee[3][0], ee[4][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Time Management")

    g2 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["14-16", "17-19", "20-22", "23-25", "25+"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Lacking in Time Management', 'Having Good Time Management'])
    fig.add_trace(go.Pie(labels=labels, values=[0, 53, 43, 19, 11], pull=[0, 0, 0, 0, 0], hole=.4, name="Yes",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[27, 37, 42, 14, 12], pull=[0, 0, 0, 0, 0], hole=.4, name="No",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[23,22,42,30,12],pull=[0,0,0,0,0.2],hole=.4,name="20-22",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    # fig.add_trace(go.Pie(labels=labels, values=[6,4,13,8,4],pull=[0,0,0,0,0.2],hole=.4,name="23-25",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[8,3,6,6,3],pull=[0,0,0,0,0.2],hole=.4,name="25+",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g22 = fig.to_html()

    dict_ = {}
    dict_['14-16'] = [0, 11, 10, 5, 3]
    dict_['17-19'] = [0, 16, 19, 3, 6]
    dict_['20-22'] = [9, 46, 37, 14, 8]
    dict_['23-25'] = [18, 45, 39, 9, 3]
    dict_['25+'] = [0, 20, 24, 4, 6]

    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0], aa[2][0], aa[3][0], aa[4][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0], bb[2][0], bb[3][0], bb[4][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0], cc[2][0], cc[3][0], cc[4][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0], dd[2][0], dd[3][0], dd[4][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0], ee[2][0], ee[3][0], ee[4][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Loss of Concentration")

    g3 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["14-16", "17-19", "20-22", "23-25", "25+"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Not having loss of concentration', 'Loss of concentration'])
    fig.add_trace(go.Pie(labels=labels, values=[9, 45, 29, 15, 13], pull=[0, 0, 0, 0, 0], hole=.4, name="Yes",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[18, 65, 63, 20, 13], pull=[0, 0, 0, 0, 0], hole=.4, name="No",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[23,22,42,30,12],pull=[0,0,0,0,0.2],hole=.4,name="20-22",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    # fig.add_trace(go.Pie(labels=labels, values=[6,4,13,8,4],pull=[0,0,0,0,0.2],hole=.4,name="23-25",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[8,3,6,6,3],pull=[0,0,0,0,0.2],hole=.4,name="25+",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g33 = fig.to_html()

    dict_ = {}
    dict_['14-16'] = [0, 14, 17, 4, 12]
    dict_['17-19'] = [0, 18, 11, 4, 0]
    dict_['20-22'] = [9, 42, 35, 5, 6]
    dict_['23-25'] = [0, 40, 23, 9, 2]
    dict_['25+'] = [18, 24, 43, 13, 6]

    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0], aa[2][0], aa[3][0], aa[4][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0], bb[2][0], bb[3][0], bb[4][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0], cc[2][0], cc[3][0], cc[4][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0], dd[2][0], dd[3][0], dd[4][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0], ee[2][0], ee[3][0], ee[4][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Loss of Concentration")

    g4 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["14-16", "17-19", "20-22", "23-25", "25+"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Not having Fear', 'Having Fear'])
    fig.add_trace(go.Pie(labels=labels, values=[9, 32, 28, 13, 12], pull=[0, 0, 0, 0, 0], hole=.4, name="Yes",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[18, 64, 66, 22, 14], pull=[0, 0, 0, 0, 0], hole=.4, name="No",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[23,22,42,30,12],pull=[0,0,0,0,0.2],hole=.4,name="20-22",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    # fig.add_trace(go.Pie(labels=labels, values=[6,4,13,8,4],pull=[0,0,0,0,0.2],hole=.4,name="23-25",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[8,3,6,6,3],pull=[0,0,0,0,0.2],hole=.4,name="25+",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g44 = fig.to_html()

    dict_ = {}
    dict_['14-16'] = [0, 15, 12, 6, 3]
    dict_['17-19'] = [0, 26, 25, 6, 6]
    dict_['20-22'] = [18, 54, 46, 13, 10]
    dict_['23-25'] = [9, 31, 27, 5, 3]
    dict_['25+'] = [0, 12, 19, 5, 4]

    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0], aa[2][0], aa[3][0], aa[4][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0], bb[2][0], bb[3][0], bb[4][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0], cc[2][0], cc[3][0], cc[4][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0], dd[2][0], dd[3][0], dd[4][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0], ee[2][0], ee[3][0], ee[4][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Difficulty in making important decisions")

    g5 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["14-16", "17-19", "20-22", "23-25", "25+"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Not having Fear', 'Having Fear'])
    fig.add_trace(go.Pie(labels=labels, values=[18, 41, 37, 12, 14], pull=[0, 0, 0, 0, 0], hole=.4, name="Yes",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[9, 43, 46, 10, 12], pull=[0, 0, 0, 0, 0], hole=.4, name="No",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[23,22,42,30,12],pull=[0,0,0,0,0.2],hole=.4,name="20-22",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    # fig.add_trace(go.Pie(labels=labels, values=[6,4,13,8,4],pull=[0,0,0,0,0.2],hole=.4,name="23-25",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    # fig.add_trace(go.Pie(labels=labels, values=[8,3,6,6,3],pull=[0,0,0,0,0.2],hole=.4,name="25+",marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g55 = fig.to_html()

    return render(request,'graph4.html',{"graph1":g1,"graph11":g11,"graph2":g2,"graph22":g22,"graph3":g3,"graph33":g33,"graph4":g4,"graph44":g44,"graph5":g5,"graph55":g55})

def graph5(request):
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    dict_ = {}
    dict_['Male'] = [31, 26, 52, 41, 30]
    dict_['Female'] = [24, 25, 59, 38, 29]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Difficulty in Sleeping/Getting out of bed")

    g1 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Trouble sleeping in Male', 'Trouble sleeping in Female'])
    fig.add_trace(go.Pie(labels=labels, values=[31, 26, 52, 41, 30], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[24, 25, 59, 38, 29], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g11 = fig.to_html()

    dict_ = {}
    dict_['Male'] = [30, 39, 58, 33, 20]
    dict_['Female'] = [22, 42, 66, 33, 12]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Feeling Fatigued")

    g2 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Fatigue in Male', 'Fatigue in Female'])
    fig.add_trace(go.Pie(labels=labels, values=[30, 39, 58, 33, 20], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[22, 42, 66, 33, 12], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g22 = fig.to_html()

    dict_ = {}
    dict_['Male'] = [11, 30, 57, 40, 42]
    dict_['Female'] = [12, 47, 49, 33, 34]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Lack of Sleep")

    g3 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Fatigue in Male', 'Fatigue in Female'])
    fig.add_trace(go.Pie(labels=labels, values=[11, 30, 57, 40, 42], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[12, 47, 49, 33, 34], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")


    g33 = fig.to_html()

    dict_ = {}
    dict_['Male'] = [118, 25, 29, 5, 3]
    dict_['Female'] = [87, 30, 40, 12, 6]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Thoughts of Harming Self/Others")

    g4 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Self Harm in Male', 'Self Harm in Female'])
    fig.add_trace(go.Pie(labels=labels, values=[118, 25, 29, 5, 3], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[87, 30, 40, 12, 6], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g44 = fig.to_html()

    dict_ = {}
    dict_['Male'] = [47, 38, 56, 25, 14]
    dict_['Female'] = [36, 34, 53, 42, 10]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Difficulty Maintaining Relationships")

    g5 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Male', 'Female'])
    fig.add_trace(go.Pie(labels=labels, values=[47, 38, 56, 25, 14], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[36, 34, 53, 42, 10], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g55 = fig.to_html()

    dict_ = {}
    dict_['Male'] = [17, 36, 72, 35, 20]
    dict_['Female'] = [8, 52, 61, 35, 19]
    df = pd.DataFrame(dict_)
    df.rename(index={0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}, inplace=True)
    df = df.transpose()
    a = df[[df.columns[0]]]
    b = df[[df.columns[1]]]
    c = df[[df.columns[2]]]
    d = df[[df.columns[3]]]
    e = df[[df.columns[4]]]
    aa = a[[a.columns[0]]].values
    bb = b[[b.columns[0]]].values
    cc = c[[c.columns[0]]].values
    dd = d[[d.columns[0]]].values
    ee = e[[e.columns[0]]].values

    fig = go.Figure()
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']

    fig.add_trace(
        go.Bar(
            x=a.index,
            y=[aa[0][0], aa[1][0]],
            marker_line_color='#000000',
            marker_color=colors[0],
            name="Never"
        )
    )

    fig.add_trace(
        go.Bar(
            x=b.index,
            y=[bb[0][0], bb[1][0]],
            marker_line_color='#000000',
            marker_color=colors[1],
            name='Rarely'
        ))
    fig.add_trace(
        go.Bar(
            x=c.index,
            y=[cc[0][0], cc[1][0]],
            marker_line_color='#000000',
            marker_color=colors[2],
            name='Sometimes'
        ))
    fig.add_trace(
        go.Bar(
            x=d.index,
            y=[dd[0][0], dd[1][0]],
            marker_line_color='#000000',
            marker_color=colors[3],
            name='Often'
        ))
    fig.add_trace(
        go.Bar(
            x=e.index,
            y=[ee[0][0], ee[1][0]],
            marker_line_color='#000000',
            marker_color=colors[4],
            name='Always'
        ))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        # legend_title_font_color="green",
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Gender',
            titlefont_size=16,
            tickfont_size=14,
        ),
        title_text="Self Care")

    g6 = fig.to_html()

    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'pink']
    labels = ["Never", "Rarely", "Sometimes", "Often", "ALways"]
    fig = make_subplots(1, 2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=['Male', 'Female'])
    fig.add_trace(go.Pie(labels=labels, values=[17, 36, 72, 35, 20], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Male",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 1)
    fig.add_trace(go.Pie(labels=labels, values=[8, 52, 61, 35, 19], pull=[0, 0, 0, 0, 0.2], hole=.4, name="Female",
                         marker=dict(colors=colors, line=dict(color='#000000', width=2))), 1, 2)
    fig.update_layout(
        # showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        title_text="")

    g66 = fig.to_html()


    return render(request,'graph5.html',{"graph1":g1,"graph11":g11,"graph2":g2,"graph22":g22,"graph3":g3,"graph33":g33,"graph4":g4,"graph44":g44,"graph5":g5,"graph55":g55,"graph6":g6,"graph66":g66})
