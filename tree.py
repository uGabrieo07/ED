ROOT = 'root'

class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.left = None
    self.right = None
  def __str__(self) -> str:
    return str(self.data)
  
class BinaryTree:
  def __init__(self,data=None) -> None:
    if data:
      node = Node(data)
      self.root = node
    else:
      self.root = None
  
  #percurso em ordem simétrica: filhos à direita -> raíz -> filhos à esquerda
  def simetric_traversal(self, node = None):
    if node is None:
      node = self.root #para percorrer a partir da raíz
    if node.left:
      self.simetric_traversal(node.left)
    print(node)
    if node.right:
      self.simetric_traversal(node.right)

  #percurso em pós ordem: todos os filhos --> raíz
  def postorder_traversal(self, node=None):
    if node == None:
      node = self.root
    if node.left:
      self.postorder_traversal(node.left)
    if node.right:
      self.postorder_traversal(node.left)
    print(node)
  
  #percurso em pré ordem: raíz -> filhos à esquerda -> filhos à direita
  def preorder_traversal(self,node=None):
    if node is None:
      node = self.root
    print(node)
    if node.left:
      return self.preorder_traversal(node.left)
    if node.right:
      return self.preorder_traversal(node.right)
  
  def level_traversal(self,node=None):
    pass
      


class BinarySearchTree(BinaryTree):
  def __init__(self, data=None) -> None:
    super().__init__(data)
  
  def insert(self,value):
    parent = None
    x = self.root
    while (x):
      parent = x
      if value < x.data:
        x = x.left
      else:
        x = x.right
    if parent is None:
      self.root = Node(value)
    elif value < parent.data:
      parent.left = Node(value)
    else:
      parent.right = Node(value)
  
  def _search(self,value,node):
    if node is None:
      return node
    elif node.data == value:
      return BinarySearchTree(node)
    elif value < node.data:
      return self._search(value,node.left)
    else:
      return self._search(value,node.right)
  def search(self,value):
    return self._search(value,self.root)
  
  def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

  def max(self, node=ROOT):
      if node == ROOT:
          node = self.root
      while node.right:
          node = node.right
      return node.data
  
  def remove(self,value,node=ROOT):
    if node == ROOT: #apenas indica se a função será executada a partir da raíz
      node = self.root
    if node is None:
      return node
    elif value < node.data:
      node.left = self.remove(value,node.left)
    elif value > node.data:
      node.right = self.remove(value,node.right)
    else:
      if node.left and node.right is None: #posso simplificar !
        return None
      elif node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      else:
        sub = self.min(node.right)
        node.data = sub
        node.right = self.remove(sub,node.right)
    return node
  

  def delete_tree(self):
        self._delete_tree(self.root)
        self.root = None

  def _delete_tree(self, node=ROOT):
      if node:
          #primeiro deleta as subsarvores direta e esquerda
          self._delete_tree(node.left)
          self._delete_tree(node.right)

          #depois deleta o próprio nó(raíz)
          del node  