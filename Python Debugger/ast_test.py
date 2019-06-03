def visit_Import(self, node):
    for alias in node.names:
        self.stats["import"].append(alias.name)
    self.generic_visit(node)

def visit_ImportFrom(self, node):
    for alias in node.names:
        self.stats["from"].append(alias.name)
    self.generic_visit(node)
