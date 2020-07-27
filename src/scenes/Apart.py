# -*- coding: utf-8 -*-
'''
Stage: "主人公のアパート"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def dream_note(w: World):
    yazaki = w.get('yazaki')
    return w.scene('夢のノート',
            w.cmd.change_stage("Apart"),
            w.plot_note("自宅アパートで片付けと天文台閉鎖後の自分の行き先を考えていると、そこに小さい頃の夢と題したノートを見つけた"),
            w.plot_note("そこには星が大好きでいつか自分で色々な星に行ってこの目で見たいと大きな字で書かれていた"),
            w.plot_note("いつの間にか現実的なことばかり言いすぎて、そんな夢も希望も失っていたことを思い出す"),
            yazaki.be("天文台の閉鎖まで一週間と迫り、$Sは自宅アパートの六畳半の部屋でぼんやりと今後のことを考えながら片付けをしていた"),
            yazaki.do("大学の研究室からここに移ってきて五年になるけれど、部屋のダンボールは大半がそのままで、",
                "服以外の必要なものは事務室やロッカーに持ち出してしまっている",
                "一番重量のある本も事務室や図書コーナーに置いてあるし、",
                "$Sの生活の八割はあの天文台という巨大な観測装置に馴染んでいた"),
            yazaki.think("あれから$chitoも彼の父親も天文台には現れていない",
                "$nomuraさんのところにも顔を出していないそうだ").omit(),
            yazaki.think("火傷はずっと残るほど酷いものではなかったそうだが、",
                "大切な一人息子のことですごい剣幕で怒鳴り込んできた父親の姿に、",
                "$Sは自分の父のことを思い出した",
                "同じように一人っ子だった$Sのことを父はあまり危険に近づけたがらなかった",
                "そのために本を買い与えて家にいさせようとしたが、それが結果的に宇宙大好き科学少年を育てることになったのは父親にとって皮肉だったのかどうか、",
                "未だに分からないままだ"),
            yazaki.talk("あ……懐かしいな、これ"),
            yazaki.do("隙間を埃が埋めていたダンボールの一つに古びたノートを見つけた",
                "まだ小学生の頃につけていた、日記とすら呼べない代物だ",
                "ページを捲ると今とは比べ物にならないくらい大きな字で『ぼくのゆめ』と書かれているのが目に飛び込む"),
            yazaki.talk("夢、か"),
            yazaki.do(
                "宇宙飛行士になって星を見て回りたい",
                "それが宇宙を、星を、天文学を好きになった$Sが思い描いた最初の夢だった",
                "けれどそれはもう叶わない",
                "自分から降りてしまった、儚い幻だ"),
            yazaki.talk("そうだな"),
            yazaki.do("最後くらい、$chitoたちに夢の一つでも見せてみようか"),
            yazaki.do("そう思い立つと自分の通帳を確認してから電話を手に取る"),
            yazaki.talk("あ、もしもし", "夜分にすみません", "そちらでまだ恒星原板て扱ってますかね？"),
            )


def balloon_star(w: World):
    yazaki = w.get('yazaki')
    return w.scene("バルーン星",
            w.cmd.change_stage("Apart"),
            w.plot_note("バルーン星を打ち上げる$yazaki"),
            w.plot_note("それは空へと上がり、小さな光を夜空に作る"),
            yazaki.come("慌てて暗がりのアパートに戻ってくる$S"),
            yazaki.do("部屋の片隅に置いてあったバルーンを確認する"),
            yazaki.talk("よし。ちゃんと動くぞ"),
            yazaki.go("それを手に出かけていく"),
            )
