import networkx as nx
import plotly.graph_objs as go
import random

def create_graph(data):
    G=nx.DiGraph()
    central_node=data['filename']
    central_node=central_node.split('/')[-1]
    G.add_node(central_node, content=[])
    sres=sorted(data['results'], key=lambda x: x['score'], reverse=True)
    for result in sres:
     if len(result['content'])>0:
        node=result['file']
        node=node.split('/')[-1]
        G.add_node(node, content=result['content'])
        G.add_edge(central_node,node, score=result['score'])
    pos=nx.spring_layout(G)
    edge_x=[]
    edge_y=[]
    edge_labels=[]
    for edge in G.edges(data=True):
        #print(edge)
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_labels.append(f"Weight of the Edge is: {edge[2]['score']}")
    node_x=[]
    node_y=[]
    node_text=[]
    node_hover=[]
    node_sizes=[]
    for node in G.nodes(data=True):
        x,y = pos[node[0]]
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"<b>{node[0]}</b>")
        content=node[1]['content']
        node_hover.append("Common Content: <br>"+"<br>".join(content))
        node_sizes.append(len(content)*5)
    edgeTexts=[]
    text_x=[]
    text_y=[]
    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        text_x.extend([(x0+x1)/2])
        text_y.extend([(y0+y1)/2])
        edgeTexts.extend([f"<b>{str(int(edge[2]['score'] * 100))}%</b>"])
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color="#000"),
        hoverinfo='text',
         mode='lines',
         text=edge_labels)
    #edge_trace.hovertext=edge_labels

    text_trace=go.Scatter(
        x=text_x, y=text_y,
        mode='markers+text',
        showlegend=False,
        marker=go.Marker(opacity=0),
        text=edgeTexts,
        textposition="top center"
    )
    node_trace=go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
              showscale=True,
              colorscale='YlGnBu',
              size=70,
            ),
            textposition="bottom center"
    )
    colorlen=[]
    for node in G.nodes(data=True):
        lentext=len(node[1]['content'])
        colorlen.append(lentext)
    node_trace.marker.color=colorlen
    node_trace.text=node_text
    node_trace.hovertext=node_hover

    fig=go.Figure(data=[edge_trace, node_trace, text_trace])
    fig.update_layout(
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )
    fig.show()
        

def interconnected_graph(data):
   filename=data['filename'] 
   results=data['results']
   sres=sorted(results, key=lambda x:len(x['content']), reverse=True)
   max2=sres[:4]
   I=nx.DiGraph()
   lonodes=[]
   filenode={'file':filename, 'score':random.random(), 'content':[]}
   lonodes.append(filenode)
   for node in max2:
      lonodes.append(node)
   for node in lonodes:
      I.add_node(node['file'], content=node['content'], score=node['score'])
   for i in range(len(lonodes)):
      for j in range(len(lonodes)):
         I.add_edge(lonodes[i]['file'], lonodes[j]['file'])
   pos=nx.spring_layout(I)
   edge_x=[]
   edge_y=[]
   for edge in I.edges(data=True):
      x0,y0=pos[edge[0]]
      x1,y1=pos[edge[1]]
      edge_x.extend([x0, x1, None])
      edge_y.extend([y0, y1, None])
   edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1.5, color="#000"),
        hoverinfo='text',
         mode='lines')
   node_x=[]
   node_y=[]
   node_text=[]
   node_hover=[]
   for node in I.nodes(data=True):
        x,y = pos[node[0]]
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"<b>{node[0]}</b>")
        content=node[1]['content']
        score=node[1]['score']
        node_hover.append("Common Content: "+", ".join(content)+"\n"+"Score: "+str(score))
   node_trace=go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
              showscale=True,
              colorscale='YlGnBu',
              size=50,
            )
    )
   colorlen=[]
   for node in I.nodes(data=True):
        lentext=len(node[1]['content'])
        colorlen.append(lentext)
   node_trace.marker.color=colorlen
   node_trace.text=node_text
   node_trace.hovertext=node_hover
   fig=go.Figure(data=[edge_trace, node_trace])
   fig.update_layout(
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )
   fig.show()

   
