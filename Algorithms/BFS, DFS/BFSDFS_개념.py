def dfs(start_node):
    stack = [start_node,]

    while True:
        if len(stack) == 0:
            print('All node searched')
            return None
        node = stack.pop()
        if node == TARGET:
            print('The target found.')
            return node
        children = expand(node)
        stack.extend(children)
        