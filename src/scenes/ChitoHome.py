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
    yazaki = w.get('yazaki')
    dad, mam = w.get('dad'), w.get('mam')
    sugi = w.get('sugi')
    return w.scene('$chitoの両親の説得',
            w.cmd.change_stage("ChitoHome"),
            w.plot_note("それと並行して、$chitoを閉館式になんとか招くため、毎日通って父親に科学の知識は危険ではないことを説く"),
            yazaki.come("$chitoの家を菓子折りを持って訪ねた"),
            dad.be(),
            mam.be(),
            sugi.be(),
            yazaki.talk("あー、すみません", "天文台の$Sですが"),
            yazaki.hear("話し声が聞こえる"),
            mam.talk("$chitoなら学校ですよ"),
            yazaki.talk("はい。分かってます。今日はご両親に"),
            dad.talk("何用だってんだよ", "あんたのせいで学校でも浮いちまってるんだぞ？"),
            yazaki.talk("昼間からお酒ですか？"),
            sugi.talk("まあかてえこと言いなさんな、先生さんよ",
                ""),
            # TODO
            )

