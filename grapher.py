import networkx as nx
import plotly.graph_objs as go

def create_graph(data):
    G=nx.DiGraph()
    central_node=data['filename']
    G.add_node(central_node, content=[])
    for result in data['results']:
        node=result['file']
        G.add_node(node, content=result['content'])
        G.add_edge(central_node,node, score=result['score'])
    pos=nx.spring_layout(G)
    edge_x=[]
    edge_y=[]
    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    node_x=[]
    node_y=[]
    node_text=[]
    node_hover=[]
    for node in G.nodes(data=True):
        x,y = pos[node[0]]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node[0])
        content=node[1]['content']
        node_hover.append("Common Content: "+", ".join(content))
    edge_hover=[d['score'] for u,v,d, in G.edges(data=True)]
    edge_widths=[score*5 for score in edge_hover]
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1.5, color="#000"),
        hoverinfo='text',
         mode='lines',
         text=edge_hover)
    node_trace=go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
              showscale=True,
              colorscale='YlGnBu',
              size=10,
            )
    )
    node_trace.marker.color=[len(text) for text in G.nodes()]
    node_trace.text=node_text
    node_trace.hovertext=node_hover


    fig=go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )
    fig.show()
        
    