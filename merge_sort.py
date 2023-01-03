class MergeSort(object):
    """Popular divide and conquer algorithm."""

    def merge_sort(self, lista):
        """Divide the list."""
        if len(lista) <= 1:
            return lista
        mid = len(lista) / 2
        left = self.merge_sort(lista[:mid])
        right = self.merge_sort(lista[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        """Combine the elements in sorted order."""
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + self._merge(left[1:], right)
        return [right[0]] + self._merge(left, right[1:])


m = MergeSort()
print(m.merge_sort([3, 2, 1, 9, 4, 7, 3, 0, -4]))