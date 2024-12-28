"""ネット通販モジュール

Copyright (c) 2024 Author. All Rights Reserved.
Released under the MIT license
https://opensource.org/licenses/mit-license.php

"""



def total_amaunt(amaunt: int, pstage: int, tax_rate: float) -> int:
    """ 支払合計を計算

    Args:
        amaunt (int): 購入料金
        pstage (int): 送料
        tax_rate (float): 税率

    Returns:
        int: 支払い合計金額
    """
    total = (amaunt + pstage) * (1 + tax_rate)
    return int(total)


class Custormer:
    """顧客クラス
    """
    def __init__(self, name: str, adress: str):
        self.name = name
        self.adress = adress


    def print_name(self):
    print(f"{self.name}様")
