"""
Q2

任意の数のモンスターがいます。APIサーバーにそのうちの2匹を指定すると、対戦をさせた結果を得ることができます。モンスターの強さは決まっていて、同じモンスター同士であれば、対戦の結果は常に変わりません。また、三すくみのような状態は考えないものとします。このAPIサーバーをつかって、モンスターを強い順に並べてください。

API アクセス例

$ curl https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/dragon+griffin
{"winner":"dragon","loser":"griffin"}

実行例
$ ruby solve.rb griffin vampire dragon troll medusa
"""

import requests

import ast

url_root = \
    'https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/'


def main(input_list):

    # モンスター名をキーに持つモンスターごとのインデックス辞書
    monster_dic = {key: i for i, key in enumerate(input_list)}
    # モンスターの強い順グラフ, 最初の要素を頂点として設定, 低いほど強い
    monster_rank = [0] * len(input_list)
    # モンスターの強さ順インデックスリスト
    # monster_idx = [i for i in range(len(input_list))]

    for i, monster in enumerate(input_list[:-1]):
        for j in range(len(input_list) - 1 - i):
            url = url_root + monster + '+' + input_list[i + j + 1]

            req = requests.get(url)  # 指定したURLからレスポンスを取得
            req_dic = ast.literal_eval(req.text)  # テキストから辞書型に変換

            # winnerとloserのモンスターのインデックスを辞書から取得
            winner = req_dic['winner']
            loser = req_dic['loser']
            winner_idx = monster_dic[winner]
            loser_idx = monster_dic[loser]
            # winnerとloserのモンスターの強さ値を取得
            winner_rank = monster_rank[winner_idx]
            loser_rank = monster_rank[loser_idx]

            # loserの値をwinnerより下位とする
            monster_rank[loser_idx] = loser_rank + 1
            # monster_idx[winner_idx], monster_idx[loser] = monster_idx[loser], monster_idx[winner]

    # 強さ順のリストを基にmonsterのリストを並び替える
    sorted_list = \
        [monster for _, monster in sorted(zip(monster_rank, input_list))]
    print(*sorted_list)


if __name__ == '__main__':
    input_dict = {}
    input_list = input().split()  # griffin vampire dragon troll medusa
    main(input_list)

