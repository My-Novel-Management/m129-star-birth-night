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
    yazaki, shino = w.get('yazaki'), w.get('shino')
    dad, mam = w.get('dad'), w.get('mam')
    return w.scene('$chitoの捜索',
            w.cmd.change_stage('Town'),
            w.plot_note("行方不明になった$chitoをみんなで探して回る"),
            w.plot_note("しかし暗い夜では探しづらい"),
            w.plot_note("星があれば、と考えるが、そのとき、$chitoのために準備しておいたバルーン星を思い出す"),
            yazaki.come("$chitoを探していた"),
            yazaki.talk("$chito君！", "どこにいるんだ？"),
            yazaki.do("返事はない"),
            yazaki.do("他にも沢山の大人が出て探していた"),
            yazaki.do("日が徐々に傾き、暗がりになってくる"),
            shino.come("ライトを手にやってくる"),
            shino.talk("見つかりました？"),
            yazaki.talk("いや",
                "今消防団の人が山手の方を探してくれてる"),
            shino.talk("昨日は雨で川も増水してるって言ってたけど……大丈夫ですよね？"),
            yazaki.talk("子どもだからな", "どこに行くかは分からない"),
            yazaki.do("持ってきてもらったライトを手に探そうと歩き出し、何か思い出す"),
            yazaki.talk("そうだ", "ちょっとここを頼む", "アイデアがあるんだ"),
            shino.talk("$yazakiさん？"),
            yazaki.go("行ってしまう"),
            )


def launching(w: World):
    yazaki, shino = w.get('yazaki'), w.get('shino')
    dad, mam = w.get('dad'), w.get('mam')
    man = w.get('man')
    return w.scene("バルーンの打ち上げ",
            yazaki.be("打ち上げ準備をしている"),
            shino.be("準備を手伝っている$S"),
            shino.talk("これでいいですか？"),
            yazaki.talk("ありがとう。少し離れてくれ"),
            yazaki.do("$ledのついた観測気球に着火する",
                "バルーンは徐々に空へと上がり、暗い空に光を灯す"),
            dad.come(),
            dad.talk("何してるんだ、こんな時に"),
            yazaki.talk("星を、作ってるんです"),
            dad.talk("そんなことしてどうする？"),
            yazaki.talk("彼はずっと星を見たがってた", "だから、偽物かも知れないけど星を作ったんです",
                "今でも彼がそれを探してるなら、きっとこれをどこかで見てくれているでしょう"),
            man.come("消防団員が駆けてくる"),
            man.talk("$chito君が見つかりました！"),
            dad.talk("どこで？"),
            man.talk("天文台のすぐ傍の作業小屋のところです"),
            yazaki.think("$nomuraが機材や材料を置いているところだった"),
            )
