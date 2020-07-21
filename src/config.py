# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("yazaki", "ヤザキ", "", 30,(1,1), "male", "研究員", "me:僕"),
            ("shino", "シノ", "", 27,(1,1), "female", "スタッフ", "me:わたし"),
            ("chito", "チト", "", 10,(1,1), "male", "子ども", "me:オレ"),
            ("mam", "チトの母", "", 35,(1,1), "female", "親", "me:私"),
            ("dad", "チトの父", "", 40,(1,1), "male", "親", "me:俺"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Toyama", "富山県", "", (50,50)),
            ("Observatory", "天文台", "Toyama"),# 富山市天文台をモデル
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

