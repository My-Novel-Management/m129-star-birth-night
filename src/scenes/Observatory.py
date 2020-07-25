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
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    return w.scene('謎の老人',
            # NOTE: ここはomit
            w.cmd.change_stage("Observatory"),
            w.plot_note("苔むした天文台に忍び込んだ老人は、その望遠鏡のところまできてそこに宝箱を発見して、微笑する。夢と書かれた紙切れが入っていた"),
            )


def missing_star_world(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    return w.scene("星が消えた世界で",
            w.cmd.change_camera("yazaki"),
            w.cmd.change_stage("Observatory"),
            w.plot_note("まだ天文台が稼働していた頃、夜空を見上げてはため息をついていた$yazaki"),
            w.plot_note("この世界ではいつからか星が見えなくなっていた"),
            w.plot_note("夜、天文台にいつものように忍び込んできた$chitoがやってきて「今日も星が見えないね」と残念そうに言う"),
            w.plot_note("$yazakiは彼に星というのは遠くの光が観測できるようになったもので、ひょっとすると全ての星が消滅してしまったのかも知れないと言う"),
            w.plot_note("$chitoはどうしても図鑑で見た星空が見たくて、$yazakiに星を作って欲しいとお願いする"),
            w.plot_note("しかし$yazakiは「星なんて作れるはずがない」と断言する"),
            w.plot_note("翌日、天文台には閉鎖通知が届いた"),
            "天文台構造：B1fが展示室／１ｆ事務室・エントランスホール／２ｆ観測室・展望所",
            "天文台の描写。時間帯は夜。夜空は真っ暗な様も",
            yazaki.be("観測室で望遠鏡を覗いている$S"),
            "$yazakiの見た目。服は白衣をだらりと着て。髪は自分でカットしていて、不正確",
            yazaki.do("今日も宇宙に星は見えない"),
            yazaki.explain("曇っているとか望遠鏡が壊れているとかではなく、",
                "純粋に宇宙に観測可能な星の光がないのだ"),
            shino.come("$chitoと一緒にやってくる"),
            chito.come(),
            "$chitoの外見。天然パーマで目がくりっとしている。鼻の頭が汚れていて、泥遊びでもしていたのかと思わせる",
            "$nomuraに小屋で色々機械のことを教わったりしていた",
            chito.talk("先生！"),
            yazaki.talk("先生じゃないと言ってるだろう、$chito"),
            chito.talk("学校の先生よりよっぽど先生だから先生でいいの！", "それより星見つかった？"),
            yazaki.do("苦笑で答える"),
            shino.talk("それで先生、今日はどうします？"),
            yazaki.talk("$shino君までそうやってからかう",
                "そうだな", "今日は一旦今までのまとめをしようかな"),
            yazaki.do("事務室に移動する"),
            "事務室に移動がてら、天文台の構造を簡単に説明",
            "事務室描写。いろいろと予算がなさそうな有様",
            yazaki.do("事務室には大量の資料が積み上がっているが、プリンタは故障中と張られている"),
            yazaki.talk("これだ"),
            yazaki.do("星についての書籍を取り出して、それを$chitoに見せる"),
            yazaki.talk("星と呼んでいるのは宇宙に浮かぶ大きな塊で、それ自身が燃えたり、",
                "別の燃えている星の光を反射したその光が長い時間をかけて観測可能なところまで届いたもので、",
                "夜空を見上げると肉眼でも多くの星を見つけることができた"),
            chito.talk("先生は見たことあるの？"),
            yazaki.talk("ああ", "ちょうど$chitoくらいの頃だったかな", "その頃までは本当に沢山の星を観測することができた",
                "手作りのちっぽけな望遠鏡で毎晩空を見上げたものさ"),
            shino.do("郵便で届いた封筒を受け取り、持ってきて開封する"),
            shino.talk("$yazaki主任、これを"),
            yazaki.do("それは天文台の閉館通知書だった"),
            )


def create_star(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
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
            yazaki.be(),
            shino.be(),
            chito.be(),
            chito.talk("どうしたの？　ここ、なくなるの？"),
            yazaki.talk("星が観測できないなら、天文台は必要ないからね", "いずれこういう日が来るとは思っていたよ",
                "そうならないようにプラネタリウムなんかも準備していたのだけれど、予算も削られて"),
            chito.talk("星がなければ作ればいいんだよ！"),
            "星誕生の流れ。分子雲が形成＞濃い部分が原始星になる＞ガスの塊で核融合反応を始めて光る",
            yazaki.talk("$chito、君は今まで何を勉強してきたんだい？",
                "星というのは人間が作れるようなものではなくてね"),
            chito.talk("先生がいつも言う科学の力ってそんなものかよ！", "駄目というんじゃなくて創意工夫とトライアンドエラーなんだろ？"),
            yazaki.talk("星は作れないかも知れないが、光を星に見立てて空に上げるくらいなら"),
            chito.talk("それでも充分だよ！", "先生、$me、星が見たいんだ",
                "いつも真っ暗な夜しか知らない$meたちが、本当なら見てたかもしれない、あのプラネタリウムみたいな星空を！"),
            yazaki.explain("こうして簡単なロケットを製作することになった"),
            )


def chitos_creation(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    nomura = w.get('nomura')
    return w.scene("$chitoの工作",
            w.plot_note("それから$chitoは毎日天文台に通ってきてはロケット工作をするようになる"),
            w.plot_note("図鑑などで勉強して、火薬を使えばいいという知識を手に入れた$chito"),
            yazaki.be("$chitoとペットボトルロケットを作っている"),
            chito.be("気難しい顔で取り組んでいる"),
            chito.talk("痛っ"),
            yazaki.talk("気をつけないとカットした断面は結構皮膚を傷つけやすくなっているから"),
            chito.talk("これくらい大丈夫だよ"),
            chito.do("真剣に取り組んでいる"),
            nomura.come("やってくる髭面の男性"),
            nomura.talk("おお、先生。やってるねー"),
            chito.talk("$nomura！"),
            nomura.talk("おっす", "工作教えてもらってんのか？"),
            chito.talk("工作じゃないやい", "星を作ってんだ"),
            nomura.talk("星とはまた大きく出たな", "で先生", "こいつ置いとくな"),
            nomura.do("メンテ用の部品を持ってきた$S"),
            nomura.talk("しかしいくら予算削られてるからって望遠鏡の整備まで先生がやんなくたってさ"),
            yazaki.talk("貧乏なのは慣れてますから", "大学の研究室にいたときも色々自作させられてたし"),
            nomura.talk("そういやプラネタリウム直さないのかい？", "学校の先生も星が見えない今、星を見せてあげられる唯一のものだって言ってましたよ"),
            yazaki.talk("投影機構は$nomuraさんたちでも何とかなるかも知れないけど、さすがに恒星原盤は職人の領域ですよ",
                "今は修理に応じてくれるメーカーも一社になってしまって、うちではちょっと手が出せませんね"),
            chito.talk("$meが星を作るから大丈夫だよ！", "先生、次は！"),
            yazaki.talk("ああ、ごめんごめん"),
            yazaki.do("水と空気による推進力を得るという原理を説明しつつ、一番シンプルなペットボトルロケットを製作する"),
            )


def chito_burned(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    dad, mam = w.get('dad'), w.get('mam')
    return w.scene("$chitoの火傷",
            w.cmd.change_stage("Observatory"),
            w.plot_note("ある日、天文台に$chitoの両親がやってくる"),
            w.plot_note("家でこっそり実験していて$chitoが火傷をしたというのだ"),
            w.plot_note("もうやめさせてください、と言い、二度と天文台には近づかせないと宣言された"),
            w.plot_note("誰も来なくなった天文台で、$yazakiたちは閉館の準備を始めていた"),
            yazaki.be("事務室で事務仕事をしている"),
            shino.be("コーヒーを淹れようと席を立つ"),
            shino.talk("コーヒー飲みますけど主任も淹れましょうか？"),
            yazaki.talk("ああ、頼む", "最近ずっと$chitoに付き合ってたから色々仕事溜まっちゃっててね"),
            shino.do("はい、と微笑み"),
            dad.come("そこに大柄な男が乗り込んでくる"),
            dad.talk("おい！"),
            yazaki.talk("ああ、$chito君のお父さん", "どうされました？"),
            dad.talk("あんたのせいでうちの息子が火傷を負ったんだよ！"),
            yazaki.talk("え？　どういうことです？"),
            yazaki.explain("ペットボトルロケットでは火薬を使うようなことは教えていなかったが、",
                "$chitoの父親から聞いたところ、図書館で借りてきたロケットの作り方を見て、",
                "火薬を使えばもっと空高くまでペットボトルロケットを飛ばせるんじゃないかと考えたらしい",
                "火薬は花火から取り出したものを使ったそうだが、誤って引火し、それで火傷を負ったようだ"),
            yazaki.talk("数日前から見なくなったと思ったらそんなことをしていたんですね",
                "一度ペットボトルロケットを作ってあまり高く飛ばないことに意気消沈していたんですが、",
                "あの子がそこまで考えるとは思っていませんでした",
                "申し訳ありません"),
            dad.talk("これがあんたの言う科学ってやつの結果か？", "うちの子には幸せにする技術だと教えているそうじゃないか",
                "聞いて呆れるな"),
            dad.go("怒ったまま出ていってしまう"),
            yazaki.do("苦笑する"),
            )


def planetarium(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    nomura = w.get('nomura')
    return w.scene("プラネタリウム",
            w.cmd.change_stage("Observatory"),
            "予算が削られすぎて、古くなって稼働しなくなっていたものを復旧させる、という風に",
            w.plot_note("天文台が閉鎖になる前に、せめて町の子どもたちに星を見せようと、プラネタリウムを作ることを考える"),
            w.plot_note("知り合いの技術者に連絡を取り、助手の$shinoの力も借りて、ホールに天幕を張り巡らし、そこにプラネタリウムを作り出す"),
            yazaki.be("天文台のホールにあるプラネタリウムを修理していた"),
            shino.come("書類を手にやってくる$S"),
            shino.talk("もうここ閉館になるんですよ、主任", "分かってます？"),
            yazaki.talk("ああ"),
            nomura.be("一緒に作業している"),
            nomura.talk("ここ、全部$ledに取り替えればいいんだな？", "光量とか強度とかは？"),
            yazaki.talk("そこの資料に計算して書いてある"),
            nomura.talk("どれだよ？"),
            yazaki.do("床に手書きの紙が散乱している"),
            yazaki.explain("自分たちで直せる部分は直して、原盤は修理を知古の町工場に出して直してもらうことになった"),
            yazaki.do("ただ$chitoは一度も姿を見せないまま、閉館式の日を迎えてしまった"),
            )


def closing_ceremony(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    mam, dad = w.get('mam'), w.get('dad')
    nomura = w.get('nomura')
    return w.scene("閉館式",
            w.plot_note("閉館式当日、なんとかプラネタリウムが完成した。多くの人が手伝ってくれるようになっていた"),
            w.plot_note("だがそこに$chitoの姿はなかった"),
            w.cmd.change_stage("Observatory"),
            yazaki.be("閉館式当日"),
            nomura.be("機械整備をしている"),
            yazaki.do("プラネタリウムの準備をしていた$S"),
            shino.be("準備を手伝っている"),
            dad.come("慌てて駆け込んでくる$S"),
            dad.talk("おい！　うちの息子はどこだ？"),
            yazaki.talk("ああ、$dadさん", "ここ最近ずっと見てません", "家か学校じゃないんですか？"),
            mam.come(),
            mam.talk("どこにもいないのよ", "$chito、どこにいってしまったの"),
            yazaki.talk("すみません！　$chito君がいなくなったそうなんです",
                "みなさんで探すのを手伝ってもらえないでしょうか？"),
            nomura.talk("こっちはどうする？　準備が間に合わないぞ？"),
            yazaki.talk("じゃあ$nomuraさんたちはここをお願いします",
                "とにかく$meらは$chito君を探しにいきます"),
            yazaki.go("あとを任せて外に走り出る"),
            )


def ovserbation(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    return w.scene("星の観測",
            w.plot_note("慌てて$yazakiは天文台に戻り、それを観測した"),
            w.plot_note("それは今までに見たことのない星だった"),
            w.plot_note("すぐに連絡を入れる", "しかし一度決まったものは覆らないと役所の人間に言われてしまった"),
            w.plot_note("$yazakiは$shinoを誘い、夢を打ち上げる事業を始めると口にした"),
            w.cmd.change_stage("Observatory"),
            yazaki.come("慌てて観測室に入り、方向を確かめる"),
            yazaki.do("今まで何も観測できなかった座標にあわく星の光が見えた",
                "それは$chitoが見つけた星だ"),
            yazaki.do("すぐに今までの星の住所と見比べて、新しい星らしいと分かった"),
            shino.talk("どうしたらいいんでしょうか", "こんなこと、初めてで"),
            yazaki.talk("連絡する", "それでここを残してもらおうと思う",
                "だってまだこの世界に星は存在するんだから"),
            yazaki.do("しかし翌日、天文台は閉鎖された"),
            "ラストは変更。星が生まれて、存続が認められたと",
            )


def future_observatory(w: World):
    yazaki, shino, chito = w.get('yazaki'), w.get('shino'), w.get('chito')
    return w.scene("天文台の未来",
            w.plot_note("廃棄処分された天文台にこっそり忍び込む、老いた$yazaki"),
            w.plot_note("天文台は新しくなり、そこの職員として彼が、$chitoがやってくるらしい"),
            w.plot_note("$yazakiはおめでとうと、夢を忘れないようにというメッセージを宝箱に残した"),
            w.cmd.change_stage("Observatory"),
            yazaki.be("苔むした天文台の事務室で、古いノートが置かれている"),
            yazaki.do("そのノートの埃を払い、手に取る$S"),
            yazaki.do("老人の正体は$Sだった"),
            yazaki.think("昔、夢を思い出したときの話を回想していた"),
            "宝箱はかつて$chitoから貰ったもの",
            yazaki.do("今度近くに新しい天文台が作られ、そこに職員として彼が来るらしい",
                "その彼にこのノートのページを入れた宝箱を渡そうと準備した"),
            yazaki.do("夢を忘れない、とマジックで書かれたその下に「$chitoへ」と書き加えた"),
            )
