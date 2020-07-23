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
    return w.scene('夢のノート',
            w.cmd.change_stage("Apart"),
            w.plot_note("自宅アパートで片付けと天文台閉鎖後の自分の行き先を考えていると、そこに小さい頃の夢と題したノートを見つけた"),
            w.plot_note("そこには星が大好きでいつか自分で色々な星に行ってこの目で見たいと大きな字で書かれていた"),
            w.plot_note("いつの間にか現実的なことばかり言いすぎて、そんな夢も希望も失っていたことを思い出す"),
            )


def balloon_star(w: World):
    return w.scene("バルーン星",
            w.plot_note("バルーン星を打ち上げる$yazaki"),
            w.plot_note("それは空へと上がり、小さな光を夜空に作る"),
            )
