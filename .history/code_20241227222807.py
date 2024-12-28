"""ネット通販モジュール

Copyright (c) 2024 Author. All Rights Reserved.
Released under the MIT license
https://opensource.org/licenses/mit-license.php

"""


def total_amaunt(amaunt: int, pstage: int, tax_rate: float) -> int:
    """_summary_

    Args:
        amaunt (int): _description_
        pstage (int): _description_
        tax_rate (float): _description_

    Returns:
        int: _description_
    """
    total = (amaunt + pstage) * (1 + tax_rate)
    return int(total)


class Custormer:
    def __init__(self, name: str, adress: str):
        self.name = name
        self.adress = adress


def print_name(self):
    print(f"{self.name}様")
