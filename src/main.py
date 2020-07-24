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
from scenes import Apart
from scenes import ChitoHome
from scenes import Observatory
from scenes import Shed
from scenes import Town


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
MAJOR, MINOR, MICRO = 0, 7, 0
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
            Observatory.mystery_oldman(w).omit(),# NOTE: 冒頭シーンから未来＝現在の描写は削除
            Observatory.missing_star_world(w),
            w.plot_turnpoint("天文台が廃棄になると通知がきた"),
            )

def ep_creation(w: World):
    return w.episode("星を作ろう",
            w.plot_develop("$chitoが星を作ればいいと提案し、打ち上げロケットを作ることになる"),
            Observatory.create_star(w),
            Observatory.chitos_creation(w),
            Observatory.chito_burned(w),
            w.plot_turnpoint("打ち上げた星は光らなかった"),
            )

def ep_planetarium(w: World):
    return w.episode("プラネタリウム",
            w.plot_develop("天文台廃棄に向けて準備を進めつつ$yazakiは光らなかった理由を考える"),
            Apart.dream_note(w),
            w.plot_develop("$yazakiはプラネタリウムを作ることを考案する"),
            Observatory.planetarium(w),
            ChitoHome.pursuade(w).omit(),
            w.plot_turnpoint("閉館式に$chitoが訪れない"),
            )

def ep_birth_star(w: World):
    return w.episode("星の生まれる夜",
            w.plot_resolve("星の光は人々の夢だった", "夢を打ち上げるとそれは星になった"),
            Observatory.closing_ceremony(w),
            Town.searching(w),
            Apart.balloon_star(w),
            Town.launching(w),
            Shed.find_chito(w),
            Observatory.ovserbation(w),
            )

def ep_future_world(w: World):
    return w.episode("未来の夢",
            Observatory.future_observatory(w),
            ).omit()

def ch_main(w: World):
    return w.chapter('main',
            ep_dark_world(w),
            ep_creation(w),
            ep_planetarium(w),
            ep_birth_star(w),
            ep_future_world(w),
            w.symbol("（了）"),
            )


# Persons


# Note
def writer_note(w: World):
    return w.writer_note("覚書",
            "星というのはその距離の分だけ時間をかけて到達した光を我々の目が捉えているだけであり、",
            "ひょっとすると既に消滅してしまっている星の光を見ているのかも知れない",
            "それはある意味で夢のようなものだ",
            "人々は夢を語りながらも、現実にはリアルを求める",
            "その現実にまみれ、やがて夢を忘れてしまう",
            "これはそんな大人たちに対して、いつも子どもが「どうして？」という彼らの純粋な疑問をぶつけてくるその姿勢と、",
            "まだ夢や希望に満ちた彼らの魂の輝きに触発され、忘れていた夢を思い出す大人の物語である",
            "読後にさわやかな感動と、夢を忘れていた人に夢を思い出させる何かであれば嬉しい",
            )

def abstract(w: World):
    return w.writer_note("概要",
            "星が見えなくなってしまった世界",
            "そこでは天文台が不要になり、廃棄されようとしていた",
            "そんな中で星好きな男の子は星を作ればいいと言い出して、ロケットで星もどきを打ち上げようとがんばる",
            "できないと分かりながらも見守っていた天文台の職員の男性は、彼のがんばりに、やがて自分が忘れていた夢を思い出す",
            "天文台が閉鎖される、まさにそのとき、彼は男の子、いや、自分自身のために星を生み出そうとロケットを飛ばした",
            )

# Plot


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
            "役場の職員と塾教師の母の下に一人っ子として生まれる",
            "保育園時代、天文台の見学に行ってからずっと星を見てみたい、星のことを知りたいと、天文台に通うようになった",
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
            "塾教師",
            "厳格な両親の下、二人の姉の下で自分の好きなことができずに育つ",
            "学校を出たら、さっさと嫁いでしまった二人の姉に代わり、母親がやっていた塾を手伝うようになった",
            )

def chara_chito_dad(w: World):
    return w.chara_note("$dad（$chitoの父）",
            "役場の職員",
            "父親は町議員で、母は役場勤務の事務員",
            "何の取り柄もない次男として、自分のことは二の次に、いつも誰かの尻拭いをして育つ",
            "学生時代は副委員長など、あまり他人がやりたがらない仕事をやらされる",
            "妻とは見合い結婚で、上司の勧めだった",
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
            *chara_notes(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

