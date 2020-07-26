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
            yazaki.come("#$chitoを探していた"),
            yazaki.do("$Sは大声を上げながら茂みや木陰を見て歩いた",
                "一人で遊んでいるときは天文台の見える公園に行くという話を思い出したからだ"),
            yazaki.talk("$chito君！", "どこにいるんだ？"),
            yazaki.do("けれど返事はないし、消防団の人たちも既に何度も探した場所だと首を横に振って見せる"),
            yazaki.do("空を見上げれば日は随分と傾き、あと一時間もすれば日暮れだった",
                "あちこちで$chitoを探す声が響いていたが未だに誰もその姿や痕跡すら見つけられずにいるようだ"),
            shino.come("#ライトを手にやってくる"),
            shino.talk("主任、見つかりました？"),
            shino.do("白いバンから降りてきた$full_shinoの手にはライトが握られている",
                "外灯が点滅してから光り、町は夜の準備を始めてしまった"),
            yazaki.talk("いや",
                "今消防団の人たちが山手の方を探してくれてるけど、本当に朝から誰も$chito君の姿を見てないそうなんだ"),
            shino.talk("雨で川も増水してるって言ってたけど……大丈夫ですよね？"),
            yazaki.talk("子どもだからな", "どこに行くかは分からない", "せめて月でも浮かんでいてくれたら良かったんだけど"),
            yazaki.do("消えてしまったものを求めても仕方ない",
                "そう思いつつも、こんな時には闇夜の世界を恨んでしまう"),
            yazaki.talk("そうだ。$shino、", "ちょっと手伝ってもらえないかな？", "一つ試してみたいたことがあるんだ"),
            shino.talk("$yazakiさん？"),
            )


def launching(w: World):
    yazaki, shino = w.get('yazaki'), w.get('shino')
    dad, mam = w.get('dad'), w.get('mam')
    man = w.get('man')
    chito = w.get('chito')
    return w.scene("バルーンの打ち上げ",
            yazaki.be("その三十分後、$Sは$full_shinoと共に天文台の脇の駐車場へとやってきていた"),
            shino.be("#準備を手伝っている$S"),
            shino.talk("主任、これで全部です"),
            yazaki.talk("ありがとう。少し離れてくれ"),
            yazaki.do("アパートから持ち出したダンボール箱を並べると、その中から観測用の気球を取り出した",
                "いわゆるラジオゾンデだ",
                "目印になるよう$ledを取り付けたもので大学の研究助手をしていた頃に幾つも試作した"),
            shino.talk("こんなもの、どうするんですか？"),
            yazaki.talk("見てれば分かる……いや、見てくれたら、きっと伝わる"),
            yazaki.do("$full_shinoにそう言うと、ガスを入れてバルーンを膨らませていく",
                "見る間に綺麗な球形になると音もなく宙へと飛び出し、どんどん上昇する",
                "赤、黄色、白に緑と、膨らませる度に新しい光が夜空へと打ち上がっていく"),
            dad.come(),
            dad.talk("何してるんだ、こんな時に"),
            dad.do("大きな声でやってきたのは$chitoの父親だった",
                "ライトを向けると疲労の色が濃い表情できつく$yazakiを睨みつけていた"),
            yazaki.talk("星を、作ってるんです"),
            dad.talk("何を言ってるんだ？　うちの息子を探す気はないのか？"),
            yazaki.talk("彼はずっと星を見たがってた", "だから、偽物かも知れないけど星を作ったんです",
                "今でも彼がそれを探してるなら、きっとこれをどこかで見てくれているでしょう"),
            yazaki.do("その五分後、$Sの電話が鳴った",
                "相手は$chitoだった"),
            chito.talk("先生！　星！　星だよ！"),
            yazaki.talk("どこにいるんだ、$chito君"),
            chito.talk("どこって天文台の下のところの物置小屋！　$fn_nomuraが色々置いてる小屋！",
                "それより星！　見えないの？"),
            yazaki.talk("それは$meが打ち上げたバルーンの光だろう？"),
            chito.talk("違うよ！", "二時の方角！"),
            )
