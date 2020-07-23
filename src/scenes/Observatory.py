# -*- coding: utf-8 -*-
'''
Stage: "天文台"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def mystery_oldman(w: World):
    return w.scene('謎の老人',
            w.cmd.change_stage("Observatory"),
            w.plot_note("苔むした天文台に忍び込んだ老人は、その望遠鏡のところまできてそこに宝箱を発見して、微笑する。夢と書かれた紙切れが入っていた"),
            )


def missing_star_world(w: World):
    return w.scene("星が消えた世界で",
            w.plot_note("まだ天文台が稼働していた頃、夜空を見上げてはため息をついていた$yazaki"),
            w.plot_note("この世界ではいつからか星が見えなくなっていた"),
            w.plot_note("夜、天文台にいつものように忍び込んできた$chitoがやってきて「今日も星が見えないね」と残念そうに言う"),
            w.plot_note("$yazakiは彼に星というのは遠くの光が観測できるようになったもので、ひょっとすると全ての星が消滅してしまったのかも知れないと言う"),
            w.plot_note("$chitoはどうしても図鑑で見た星空が見たくて、$yazakiに星を作って欲しいとお願いする"),
            w.plot_note("しかし$yazakiは「星なんて作れるはずがない」と断言する"),
            w.plot_note("翌日、天文台には閉鎖通知が届いた"),
            )


def create_star(w: World):
    return w.scene("星を作ろう",
            w.plot_note("天文台にやってきた$chitoは閉鎖通知を知り、それなら尚の事、星を作るべきだと主張する"),
            w.plot_note("星があれば天文台は存続できるし、自分も星を見れていいからと"),
            w.plot_note("仕方なく$yazakiは簡単にできる打ち上げ式の発光体で誤魔化すことにした"),
            "ペットボトルを使ったロケットでは２００ｍくらいは簡単に上がる。最高記録はカーボンファイバを使ったもので８３０ｍ",
            w.plot_note("$yazakiが作ったのは２００ｍほど打ち上がるペットボトルロケットで、その先にＬＥＤライトの先端を取り付けた"),
            w.plot_note("実験の日、こっそりやってきた$chitoは両親に色々と叱られているという。本人は気にしていないが、噂で天文台が悪い場所だと吹聴していると聞いた"),
            w.plot_note("ロケットを打ち上げると$chitoはそれに感動するが、光はすぐに消えてしまった"),
            w.plot_note("それを見せて「星は無理だよ、$chito」と諭す"),
            w.plot_note("けれど$chitoはもっと大きなロケットでいっぱい星を乗せればいいと考え、自作すると言い出した"),
            )


def chitos_creation(w: World):
    return w.scene("$chitoの工作",
            w.plot_note("それから$chitoは毎日天文台に通ってきてはロケット工作をするようになる"),
            w.plot_note("図鑑などで勉強して、火薬を使えばいいという知識を手に入れた$chito"),
            )


def chito_burned(w: World):
    return w.scene("$chitoの火傷",
            w.plot_note("ある日、天文台に$chitoの両親がやってくる"),
            w.plot_note("家でこっそり実験していて$chitoが火傷をしたというのだ"),
            w.plot_note("もうやめさせてください、と言い、二度と天文台には近づかせないと宣言された"),
            w.plot_note("誰も来なくなった天文台で、$yazakiたちは閉館の準備を始めていた"),
            )


def planetarium(w: World):
    return w.scene("プラネタリウム",
            "予算が削られすぎて、古くなって稼働しなくなっていたものを復旧させる、という風に",
            w.plot_note("天文台が閉鎖になる前に、せめて町の子どもたちに星を見せようと、プラネタリウムを作ることを考える"),
            w.plot_note("知り合いの技術者に連絡を取り、助手の$shinoの力も借りて、ホールに天幕を張り巡らし、そこにプラネタリウムを作り出す"),
            )


def closing_ceremony(w: World):
    return w.scene("閉館式",
            w.plot_note("閉館式当日、なんとかプラネタリウムが完成した。多くの人が手伝ってくれるようになっていた"),
            w.plot_note("だがそこに$chitoの姿はなかった"),
            )


def ovserbation(w: World):
    return w.scene("星の観測",
            w.plot_note("慌てて$yazakiは天文台に戻り、それを観測した"),
            w.plot_note("それは今までに見たことのない星だった"),
            w.plot_note("すぐに連絡を入れる", "しかし一度決まったものは覆らないと役所の人間に言われてしまった"),
            w.plot_note("$yazakiは$shinoを誘い、夢を打ち上げる事業を始めると口にした"),
            )


def future_observatory(w: World):
    return w.scene("天文台の未来",
            w.plot_note("廃棄処分された天文台にこっそり忍び込む、老いた$yazaki"),
            w.plot_note("天文台は新しくなり、そこの職員として彼が、$chitoがやってくるらしい"),
            w.plot_note("$yazakiはおめでとうと、夢を忘れないようにというメッセージを宝箱に残した"),
            )
