class Tree:
    class _Node:
        def __init__(self, element, parent, child, sibling):
            self._element = element
            self._parent = parent
            self._child = child
            self._sibling = sibling

        def __str__(self):
            raise NotImplementedError

        def element(self):
            return self.element

        def parent(self):
            return self.parent

        def child(self):
            return self.child

        def sibling(self):
            return self.sibling

        def set_element(self, element):
            self._element = element

        def set_parent(self, parent):
            self._parent = parent

        def set_child(self, child):
            self._child = child

        def set_sibling(self, sibling):
            self._sibling = sibling

    def __init__(self, root=None):
        self._root = root

    def _subtree_len(self, p):
        raise NotImplementedError

    def __len__(self):
        return self._subtree_len(self.root())

    def _subtree_str(self, p):
        raise NotImplementedError

    def __str__(self):
        return self._subtree_str(self.root())

    def root(self):
        return self._root

    def is_root(self, p):
        return p == self._root

    def is_external(self, p):
        return self.num_children(p) == 0

    def is_internal(self, p):
        return not self.is_external(p)

    def is_empty(self):
        return self._root is None

    def children(self, p):
        if p.child():
            yield p.child()
            q = p.child().sibling()
            while q:
                yield q
                q = q.sibling()

    def num_children(self, p):
        count = 0
        for c in self.children(p):
            count += 1
        return count

    def depth(self, p):
        if p is self.root():
            return 1
        else:
            return 1+self.depth(p.parent())

    def _height(self, p):
        if self.is_external(p):
            return 1
        else:
            return 1 + max([self._height(c) for c in self.children(p)])

    def height(self):
        if self.is_empty():
            return 0
        else:
            return self._height(self.root())

    # Preorder : Visit parents first, after then visit children
    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    # Postorder : Visit child first, after then visit parents
    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    # Levelorder : Visit all nodes in order of level
    def _subtree_levelorder(self, p):
        queue = list()
        queue.append(p)
        while(len(queue)) != 0:
            p = queue.pop(0)
            yield p
            for c in self.children(p):
                queue.append(c)

    def levelorder(self):
        if not self.is_empty:
            for p in self._subtree_levelorder(self.root()):
                yield p
