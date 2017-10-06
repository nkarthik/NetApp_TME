import plotly.plotly as py
import plotly.graph_objs as go

x = ['WordCount', 'TerraSort', 'READ', 'WRITE', 'Aggregation', 'Join', 'Scan', 'Bayes', 'Kmeans', 'Pagerank']
y1 = [1.3, 279.9, 242.2, 314.1, 168.6, 30.2, 635.8, 117.6, 5.3, 333]
y2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

trace1 = go.Bar(
    x=x,
    y=y1,
    name = '12 mount points',
    #text=y,
    textposition = 'auto',
    marker=dict(
        color='rgb(123,192,247)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.8
)

trace2 = go.Bar(
    x=x,
    y=y2,
    name = '6 mount points',
    #text=y2,
    textposition = 'auto',
    marker=dict(
        color='rgb(59,138,217)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.8
)

trace3 = go.Bar(
    x=x,
    y=y3,
    name = '2 mount points',
    #text=y3,
    textposition = 'auto',
    marker=dict(
        color='rgb(241,130,38)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.8
)

trace4 = go.Bar(
    x=x,
    y=y4,
    name = '1 mount point',
    #text=y4,
    textposition = 'auto',
    marker=dict(
        color='rgb(255,219,105)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.8
)

data = [trace1, trace2, trace3, trace4]

layout = go.Layout(
    title='Average IN network (MB/sec)',
    yaxis=dict(
        title='IN network (MB/sec)',
        titlefont=dict(
            family='Courier New, monospace',
            size=16,
            color='rgb(107, 107, 107)'
        )
    )
)
'''
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)
'''

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='JBOD_Testing_Network')

