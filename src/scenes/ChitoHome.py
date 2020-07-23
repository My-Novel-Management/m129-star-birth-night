# -*- coding: utf-8 -*-
'''
Stage: "チトの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def pursuade(w: World):
    return w.scene('$chitoの両親の説得',
            w.plot_note("それと並行して、$chitoを閉館式になんとか招くため、毎日通って父親に科学の知識は危険ではないことを説く"),
            )

