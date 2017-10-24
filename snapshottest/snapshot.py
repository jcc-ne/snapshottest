from collections import OrderedDict


class Snapshot(OrderedDict):
    def __eq__(self, other):
        try:
            return super(Snapshot, self).__eq__(other)
        except ValueError:
            import pandas as pd
            for k in self:
                try:
                    if not self[k] == other[k]:
                        return False
                except ValueError:
                    if not other[k].equals(pd.DataFrame(self[k])):
                        return False
            return True

