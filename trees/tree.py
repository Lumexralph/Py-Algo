"""Define a tree ADT using the concept of a position as an abstraction for a node of a tree.

An element is stored at each position, and positions satisfy parent-child relationships that
define the tree structure. A position object for a tree supports the method:

p.element(): Return the element stored at position p.

The tree ADT then supports accessor methods,
allowing a user to navigate the various positions of a tree
"""

from linked_list.linked_queue import LinkedQueue

class Tree:
    """Abstract base class representing a tree structure."""

    # nested Position class
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)
        
    # abstract methods that concrete subclass must support
    def root(self):
        """Return Position representing the tree's root or None if empty."""
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        """Return Position representing p s parent or None if p is root."""
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')
    
    def __iter__(self):
        """Generate an iteration of the tree's element"""
        for p in self.positions():                  # use same order as positions()
            yield p.element()

    # concrete methods implemented
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0
    
    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    # def _height1(self):                                                                # O(nˆ2) worst-case time
    #     """Return the height of the tree."""
    #     depths_of_leaves = [self.depth(p) for p in self.positions() if self.is_leaf(p)]
    #     return max(depths_of_leaves)


    def _height2(self, p):                                                             # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            children_height = [self._height2(c) for c in self.children(p)]
            return 1 + max(children_height)

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)

    # ========= Traversal of the tree methods ==========
    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):       # start the recursive traversal
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        yield p                                                # visit the root p first
        for c in self.children(p):                             # for each child of p
            for other in self._subtree_preorder(c):            # do a preorder of c's subtree
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):      # start the recursion
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other                                     # yielding each child to our caller
        yield p                                                 # visit p after the subtrees

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()                              # known positions not yet yielded
            fringe.enqueue(self.root())                         # starting with the root on the queue
            while not fringe.is_empty():
                p = fringe.dequeue()                            # remove from front of the queue
                yield p                                         # report the position
                for c in self.children(p):                      # get the children of the current node/position
                    fringe.enqueue(c)                           # add children to back of queue
    
    
