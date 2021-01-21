"""
Q1
大きさは同じで重さが異なる商品が複数あるとします。この商品N個を、以下の条件にそって3つのトラックに分配するアルゴリズムを実装してください。

- この問いの条件 -

1. すべての商品は同一の大きさ、重さの箱に入り、箱は個別のIDを持つものとする

2. プログラム実行時は、コマンドライン引数で「箱ID」と「重さ」の情報を与え、プログラムの結果には各トラックに積載する「箱ID」を出力してください。たとえば 1:50 の文字列をコマンドライン引数で渡したときは、箱ID=1, 重さ=50kg の商品とする

3. 商品は箱に入った状態で列となって連続で運び込まれ、重さは持ち上げるまでわからず、尚且つ同時に1つしか持ち上げられない

4. それぞれのトラックには、なるべく重さが均等になるように分配する必要がある

5. それぞれのトラックの積載可能重量に制限はない
"""


def main(input_dict):
    truck_list = [[], [], []]  # トラックの積載箱IDリスト
    weight_list = [0, 0, 0]  # トラックの積載重量状態リスト

    for i, (key, value) in enumerate(input_dict.items()):
        # 最初は全てのトラックに順当に積載する
        if i < 3:
            weight_list[i] += int(value)
            truck_list[i].append(int(key))
        # 3つ全てのトラックに積載し終わった場合
        else:
            lightest_idx = weight_list.index(min(weight_list))  # 最も積載重量が軽いトラックを取得
            weight_list[lightest_idx] += int(value)  # 重量を追加
            truck_list[lightest_idx].append(int(key))

    # 積み終わった荷物を標準出力
    for i in range(len(truck_list)):
        print('truck_{}:'.format(i+1), end='')
        print(*truck_list[i], sep=',')


if __name__ == '__main__':
    input_dict = {}
    input_list = input().split()  # 1:50 2:30 3:40 4:10
    input_list = [str.strip().split(':') for i, str in enumerate(input_list)]
    input_dict = dict((input_list))
    main(input_dict)
