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
            yazaki.be("自分のアパートで閉鎖後について考えていた"),
            yazaki.think("自分の父親も一人っ子だった$Sのことをあまり危険に近づけたがらなかった",
                "そのために本を買い与えて家にいさせようとしたが、それが逆に宇宙大好き科学少年を育てることになった"),
            yazaki.think("母親は勉強をする息子のことを喜んだ"),
            yazaki.do("そんな$Sは小さい頃から何かとノートに書き付けていた"),
            yazaki.talk("懐かしいな"),
            yazaki.do("荷物を整理していて、そこから古びたノートを発見する"),
            yazaki.do("そこにはまだ小学生の頃に書いた夢があった",
                "宇宙飛行士になって星を見て回りたい"),
            yazaki.do("もうそれは叶わない夢だ",
                "いつの間にか諦めてしまった"),
            yazaki.do("最後くらい、$chitoたちに夢を見せてみようか"),
            yazaki.do("自分の貯金を確認して、電話を掛けた"),
            yazaki.talk("あ、もしもし", "夜分にすみません", "そちらでまだ原盤て扱ってますかね？"),
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
