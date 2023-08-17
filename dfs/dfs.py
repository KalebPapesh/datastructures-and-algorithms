class DepthFirstSearch:
    def __init__(self):
        self.stack = set()
        self.max_depth = 0
        self.depth = 0
        self.visible_stack = set()
        self.root = None

    def dfs(self, graph, node):
        self.stack.add(node)
        if not self.root:
            self.root = node
            self.visible_stack.add(node)

        print(node, end=' ')

        # this depends on the graphs structure as it's passed in
        # with the left node on the left and the right node on the right
        # we could use a more complex route by creating a node class and building a graph
        # using a graph object instead of a dictionary of arrays, we would code the following:
        # self.pre_order(node.left)
        # self.pre_order(node.right)
        # however this is sufficient given the input
        self.__child_looper(graph, node)

    # Print the max depth count
    def tree_max_depth(self, graph, node):
        self.__clear_instance_variables()
        self.dfs(graph, node)
        return self.max_depth

    # any node that is >= root is visible
    def visible_nodes(self, graph, node):
        self.__clear_instance_variables()
        self.dfs(graph, node)
        return self.visible_stack

    # convert the structure in a format that can be transmitted and reconstructed

    # private variables
    def __child_looper(self, graph, node):
        for child in graph[node]:
            if child not in self.stack:
                self.__traverse(graph, child)

    def __traverse(self, graph, child):
        self.depth += 1
        self.dfs(graph, child)
        self.max_depth = max(self.max_depth, self.depth)
        if self.__is_visible(child): self.visible_stack.add(child)

    def __is_visible(self, node):
        is_visible = False
        if node >= self.root: is_visible = True

        return is_visible

    def __clear_instance_variables(self):
        self.stack = set()
        self.max_depth = 0
        self.depth = 0
        self.visible_stack = set()
        self.root = None
