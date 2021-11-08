import Tree


class BinaryTree(Tree):
    class _Node:
        def __init(self, element, parent, left, right):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        def __repr__(self):
            return self._element

        def __str__(self):
            return str(self._element)

        def element(self):
            return self._element

        def parent(self):
            return self._parent

        def left(self):
            return self._left

        def right(self):
            return self._right

        def set_element(self, element):
            self._element = element

        def set_parent(self, parent):
            self._parent = parent

        def set_left(self, left):
            self._left = left

        def set_right(self, right):
            self._right = right

    def __init__(self, root=None):
        super().__init__(root)

    def _subtree_str(self, p):
        if p is None:
            return '[]'
        elif self.is_external(p):
            return f'[{str(p)}]'
        else:
            return f'[{str(p)} {str(self._subtree_str(p.left()))} {str(self._subtree_str(p.right()))}]'

    # Inorder : Visit Left->Root->Right
    def _subtree_inorder(self, p):
        if p.left():
            for other in self._subtree_inorder(p.left()):
                yield other
        yield p
        if p.right():
            for other in self._subtree_inorder(p.right()):
                yield other

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
