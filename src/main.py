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
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2K
#   6. Scenes
#   7. Conte        - 1/2: 4K
#   8. Layout
#   9. Draft        - 1/1: 8K
#
################################################################

# Constant
TITLE = "星が生まれる夜"
MAJOR, MINOR, MICRO = 0, 3, 0
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
def ep_dark_world(w: World):
    return w.episode("真っ暗な夜の世界",
            w.plot_setup("その世界ではいつからか星が見えなくなっていた"),
            w.plot_note("天文台から夜空を見上げていたが、星は全く見えない、暗闇だった"),
            w.plot_note("こっそりやってきた$chitoが$yazakiに星が消えた理由を尋ねる"),
            w.plot_note("この世界ではいつからか、星が見えなくなってしまった"),
            w.plot_note("天文台が廃棄になると通知があった"),
            w.plot_turnpoint("天文台が廃棄になると通知がきた"),
            )

def ep_creation(w: World):
    return w.episode("星を作ろう",
            w.plot_develop("$chitoが星を作ればいいと提案し、打ち上げロケットを作ることになる"),
            w.plot_note("$chitoが見えないなら星を作ればいいと提案する"),
            w.plot_note("$yazakiはそんなことできないと言うが、$chitoは無理じゃないと意地を張って自分で何とか考えようとする"),
            w.plot_note("$chitoが火薬で怪我をして、両親が怒鳴り込んでくる"),
            w.plot_note("計画は中止になり、天文台廃棄にむけて片付けを始める"),
            w.plot_turnpoint("打ち上げた星は光らなかった"),
            )

def ep_realized(w: World):
    return w.episode("気づき",
            w.plot_develop("天文台廃棄に向けて準備を進めつつ$yazakiは光らなかった理由を考える"),
            w.plot_note("小さい頃の自分の夢を書いたものが出てきて、いつの間にか夢を忘れていたことに気づく$yazaki"),
            w.plot_note("$chitoはこっそりやってきて、がんばって星を作ると言い出し、$yazakiはそれを手伝う"),
            w.plot_note("$chitoが作った一番小さいロケットだけは、何故か小さな星を一瞬だけ見せてくれた"),
            w.plot_note("$yazakiはあることに気づいた"),
            w.plot_turnpoint("$yazakiは星の原因に気づいた"),
            )

def ep_birth_star(w: World):
    return w.episode("星の生まれる夜",
            w.plot_resolve("星の光は人々の夢だった", "夢を打ち上げるとそれは星になった"),
            w.plot_note("天文台が廃棄になり、閉館式を行ったその夜、準備していたロケットを打ち上げた"),
            w.plot_note("今までは全部失敗だったが、夢を乗せたロケットは星の光になった"),
            w.plot_note("夢を失った人々がそれを見上げ、忘れていた自分の夢を思い出した"),
            w.plot_note("$yazakiは$shinoを誘い、夢を打ち上げる事業を始めると口にした"),
            )

def ep_future_world(w: World):
    return w.episode("未来の夢",
            w.plot_note("廃棄処分された天文台にこっそり忍び込む、老いた$yazaki"),
            w.plot_note("天文台は新しくなり、そこの職員として彼が、$chitoがやってくるらしい"),
            w.plot_note("$yazakiはおめでとうと、夢を忘れないようにというメッセージを宝箱に残した"),
            )

def ch_main(w: World):
    return w.chapter('main',
            ep_dark_world(w),
            ep_creation(w),
            ep_realized(w),
            ep_birth_star(w),
            ep_future_world(w),
            )


# Persons


# Note
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def abstract(w: World):
    return w.writer_note("概要",
            )

# Plot
def plot_notes(w: World):
    return ()


# Character
def chara_notes(w: World):
    return (chara_note(w),
            chara_yazaki(w),
            chara_chito(w),
            chara_shino(w),
            chara_chito_mam(w),
            chara_chito_dad(w),
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "$yazaki（博士）：主人公。天文台の職員で、夢を失った大人代表",
            "$chito（星好きな子ども）：誰もが星が見えないのを当たり前と思う中で、この子だけが星を見たいと夢を見る",
            "$shino（スタッフ）：天文台の職員。同僚の女性で、彼に夢を思い出させるきっかけを与える一人",
            "$mamと$dad（子どもの親）：他の子どもと違う自分の子のことを憂えている。そこから博士たちを快く思っていない",
            )

def chara_yazaki(w: World):
    return w.chara_note("$yazaki",
            "天文台の職員で、元は宇宙飛行士を目指していた",
            "教師の父とデザイナーの母の下に生まれる",
            "小さい頃から星を見るのが好きで、まだ漢字も読めないうちから星の図鑑や本をずっと眺めていた",
            "学生時代に色覚異常が発覚し、宇宙飛行士の夢を諦める",
            "それでも星好きから大学では天文学を学ぶ",
            "一旦大学を卒業し、印刷会社に勤務していたが、天文台職員募集を見て応募",
            "二十八歳の時に今の天文台勤務を始める",
            )

def chara_chito(w: World):
    return w.chara_note("$chito",
            "星が大好きな子ども",
            "昔の$yazakiに似ている",
            )

def chara_shino(w: World):
    return w.chara_note("$shino",
            "天文台の職員で、技術系スタッフ",
            "$yazakiのサポート的立場",
            "四人兄弟の三番目として生まれる",
            "賑やかな家庭で、大工の父とその手伝いの母の下、歳の離れた弟の面倒を見ながら育つ",
            "よく近所の子どもたちの世話をする母を見て育ち、小学校でも何かと面倒見のよい生徒だった",
            "工学系の大学に進学",
            "物理学や数学に興味を持つ",
            "しばらく大学院で研究助手の仕事をしていたが、天文台の募集があり、心機一転と応募してみる",
            )

def chara_chito_mam(w: World):
    return w.chara_note("$mam（$chitoの母）",
            )

def chara_chito_dad(w: World):
    return w.chara_note("$dad（$chitoの父）",
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
            *plot_notes(w),
            *chara_notes(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

