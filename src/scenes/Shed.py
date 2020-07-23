# -*- coding: utf-8 -*-
'''
Stage: "物置小屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def find_chito(w: World):
    return w.scene('$chitoの発見',
            w.plot_note("それを見て、$chitoは出てきた"),
            w.plot_note("天文台に行かせてくれない両親に反発し、天文台の近くの小屋に隠れていて、寝てしまっていたのだ"),
            w.plot_note("と、$chitoが夜空を指差す"),
            w.plot_note("夜空には小さく星が光っている"),
            )

