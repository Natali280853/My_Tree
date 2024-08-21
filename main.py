class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, level=0):
    print(' ' * level + node.data)
    for child in node.children:
        print_tree(child, level + 1)

# Создаем корневой узел
root = Node('Root')

# Создаем дочерние узлы
child1 = Node('Child1')
child2 = Node('Child2')
child3 = Node('Child3')

# Добавляем дочерние узлы к корневому узлу
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

# Добавляем еще один дочерний узел
grandchild = Node('Grandchild')
child2.add_child(grandchild)

# Выводим дерево объектов
print_tree(root)
