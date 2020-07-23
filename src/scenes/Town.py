# -*- coding: utf-8 -*-
'''
Stage: "町"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def searching(w: World):
    return w.scene('$chitoの捜索',
            w.plot_note("行方不明になった$chitoをみんなで探して回る"),
            w.plot_note("しかし暗い夜では探しづらい"),
            w.plot_note("星があれば、と考えるが、そのとき、$chitoのために準備しておいたバルーン星を思い出す"),
            )

