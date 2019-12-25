from Linked_list.DoublyLinkedList.DoublyLinkedBase import _DoublyLinkedBase, LinkedDeque
import random

class PositionalList (_DoublyLinkedBase):

  class Position:

      __slots__ = ['_container', '_node']

      def __init__(self, container, node):

          self._container = container
          self._node = node

      def element(self):
          return self._node._element

      def __eq__(self, other):
           # Diğer aynı konumu temsil eden bir konum ise true döndürür
           return  type(other) is type(self) and other._node is self._node

      def __ne__(self, other):
          # Diğer farklı konumu temsil eden bir konum ise true döndürür
           return  not (self == other)  # _eq_  karşıtı

      def _validate(self, p):
          # Dönüş konumu s düğümü veya geçersiz ise uygun hatayı kaldırın.

          if not isinstance(p, self.Position):
              raise TypeError("data uygun pozisyon tipi olmalıdır")

          if p._container is not self:
              raise ValueError("Data bu alana ait değil")

          if p._node._next is None:
              raise ValueError("data artık geçerli değil")

          return p._node

      def _make_position(self, node):
          # Verilen düğüm için dönüş konumu
          if node is self._header or node is self._trailer:
              return None

          else:
              return self.Position

      def first(self):
          return self._make_position(self._header._next)

      def last(self):
          return self._make_position(self._trailer._next)

      def before(self,data):
          node =self._validate(data)
          return self._make_position(node._prev)

      def after(self, data):
          node = self._validate(data)
          return self._make_position(node._prev)

      def iter(self):
          cursor = self.first()
          while cursor is not None:
              yield cursor.element()
          cursor = self.after(cursor)

      # düğüm yerine konum döndürmek için devralınan sürümü geçersiz kıl
      def _insert_between(self, data, prev_node, next_node):
          # Mevcut düğümler arasında yeni Düğüm ekleme ve yeni konum döndürme
          node = super()._insert_between(data, prev_node, next_node)
          return self._make_position(node)

      def add_first(self, data):
          return self._insert_between(data, self._header, self._header._next )

      def add_last(self, data):
          return self._insert_between(data, self._trailer._prev, self._trailer)

      def add_before(self, p, data):
          orginal =self._validate(p)
          return self._insert_between(data, orginal._prev, orginal)

      def add_after(self, p, data):
          orginal = self._validate(p)
          return self._insert_between(data, orginal._next, orginal)

      def delete(self, p):
          orginal = self._validate(p)
          return self.delete_node(orginal)

      def replace(self, p, data):
          orginal = self._validate(p)
          old_value = orginal._element
          orginal._element = data
          return old_value

if __name__ == '__main__':
     list = LinkedDeque()
     list_control = PositionalList()
     for i in range(0, 10):
         x = random.randint(1, 100)
         list.insert_first(x)

     for j in range(0, 10):
         y = random.randint(1, 100)
         list.insert_last(y)











