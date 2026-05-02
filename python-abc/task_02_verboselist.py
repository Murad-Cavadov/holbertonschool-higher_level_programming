#!/usr/bin/env python3
"""
Bu modulda Python-un list sinfini genişləndirən VerboseList sinfi yerləşir.
"""


class VerboseList(list):
    """
    Siyahıya element əlavə edildikdə və ya silindikdə 
    bildiriş verən xüsusi siyahı sinfi.
    """

    def append(self, item):
        """Element əlavə edir və bildiriş çap edir."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Siyahını genişləndirir və neçə element əlavə edildiyini çap edir."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Elementi silməzdən əvvəl bildiriş çap edir."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Elementi çıxarmazdan əvvəl bildiriş çap edir."""
        # pop ediləcək elementi tapmaq üçün index-dən istifadə edirik
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
