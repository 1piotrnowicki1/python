def __str__(self):
    return f'Gruszka odmiany {self.get_odmiana()}, w smaku {self.get_smak()}, o wadze {self.get_waga()} gram'


def __repr__(self):
    return f'Gruszka: {self.get_odmiana()}, smak: {self.get_smak()}, waga: {self.get_waga()} gram'