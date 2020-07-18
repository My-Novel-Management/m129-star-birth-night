#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8
#   4. Spec
#   5. Plot         - 1/4
#   6. Scenes
#   7. Conte        - 1/2
#   8. Layout
#   9. Draft        - 1/1
#
################################################################

# Constant
TITLE = "星が生まれる夜"
MAJOR, MINOR, MICRO = 0, 1, 0
COPY = "星がなくなった世界"
ONELINE = "星が見えなくなってしまった世界で、少年たちは自作の星を打ち上げる"
OUTLINE = "約8000字のファンタジィ短編。星が見えなくなってしまった世界。用無しとなった天文台は廃棄される。その閉館記念日に星を詰めたロケットを打ち上げる"
THEME = "現実を夢は超えてくいく"
GENRE = "ファンタジィ"
TARGET = "10台から30台（男女）"
SIZE = "〜8K"
CONTEST_INFO = "妄想コンテスト「星降る夜に」"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (1, 1, 2020)


# Episodes
def ch_main(w: World):
    return w.chapter('main',
            "前提条件説明",
            "ある日突然星が見えなくなった",
            "星は宇宙の光を見ているもの",
            "天文台は廃棄になる",
            "星がどうしても見たいという子どもたち",
            "博士はそんな子どもらのために簡単なロケットを打ち上げることを考える",
            "天文台職員は（研究者＝教授など、技術職員、事務職員）",
            "閉鎖の前夜、博士は子どもたちを集めて、ロケット作りをする",
            "打ち上げたロケットは空に星を作ってくれた",
            "廃棄され、もう長く使われていない天文台に一人の老人がやってくる",
            "その老人はかつてそこに勤めていた職員だった",
            "今、空を見上げると、そこにはいくつかの星が見えた",
            "また一つ、星が増える",
            "成長した子どもたちが、星を作る事業を始めていたのだ",
            "人が夢を見なくなってから星は消えてしまった",
            "それが分かったから、彼は夢を語るようになった。かつては現実主義だったけれども",
            )


# Persons


# Note
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def abstract(w: World):
    return w.writer_note("概要",
            )


# main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            abstract(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

