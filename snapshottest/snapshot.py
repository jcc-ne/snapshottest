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
                    try:
                        cols = other.columns
                        if not other[k].reset_index().equals(
                            pd.DataFrame(self[k])[cols]):
                            return False
                    except AttributeError as e:
                        print 'Not dataframe'
                        print self
                        print other
            return True

