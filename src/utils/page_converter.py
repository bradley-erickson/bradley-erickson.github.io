def convert_layout(layout):
    if isinstance(layout, str):
        return layout
    new = layout.to_plotly_json()
    children = new['props']['children']
    if children:
        new['props']['children'] = [convert_layout(x) for x in children] if isinstance(children, list) else convert_layout(children)
    return new
