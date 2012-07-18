class Sequence:
    """Sequence of sonic atoms, our 'UnitGrain' classes"""
    def __init__(self, ordered_unit_grains=[UnitGrain()]*3):
        self.ordered_unit_grains=ordered_unit_grains
        self.unit_count=len(ordered_unit_grains)
        self.active_grains=range(self.unit_count)
