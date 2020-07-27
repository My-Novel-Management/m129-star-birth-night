# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("yazaki", "ヤザキ", "", 30,(1,1), "male", "研究員", "me:僕:shino:サエキ君"),
            ("shino", "シノ", "サエキ,シノ", 27,(1,1), "female", "スタッフ", "me:わたし"),
            ("chito", "チト", "", 10,(1,1), "male", "子ども", "me:ボク:nomura:ノームラ"),
            ("mam", "チトの母", "", 35,(1,1), "female", "親", "me:私"),
            ("dad", "チトの父", "", 40,(1,1), "male", "親", "me:俺"),
            ("nomura", "ノムラ", "", 45,(1,1), "male", "技術者", "me:俺"),
            ("sugi", "スギ", "", 50,(1,1), "male", "消防団", "me:オレ"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Toyama", "富山県", "", (50,50)),
            ("Town", "天文台の町", "Toyama"),
            ("Observatory", "天文台", "Town"),# 富山市天文台をモデル
            ("Apart", "ヤザキのアパート", "Town"),
            ("ChitoHome", "チトの家", "Town"),
            ("Shed", "物置小屋", "Town"),
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
            ("led", "ＬＥＤ"),
            ("pc", "ＰＣ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ("儚い幻", "儚《はかな》い幻《まぼろし》"),
            ),
        }

