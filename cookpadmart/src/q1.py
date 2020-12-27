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
    print(input_dict)

    for key, value in (input_dict):
        # 全てのトラックに順当に積載する
        if i < 3:
            print(input_dict[i+1])
            weight_list[i] += input_dict[i+1]
            truck_list[i].append(i)
        # 3つ全てのトラックに積載し終わった場合
        else:
            lightest_idx = weight_list.index(min(weight_list))  # 最も積載重量が軽いトラックを取得
            weight_list[lightest_idx] += input_dict[i+1]  # 重量を追加
            truck_list[lightest_idx].append(i)

    for i in range(len(truck_list)):
        print('truck_', i, ':', truck_list[i])

    # for i in range(len(input_dict)):
    #     # 全てのトラックに順当に積載する
    #     if i < 3:
    #         print(input_dict[i+1])
    #         weight_list[i] += input_dict[i+1]
    #         truck_list[i].append(i)
    #     # 3つ全てのトラックに積載し終わった場合
    #     else:
    #         lightest_idx = weight_list.index(min(weight_list))  # 最も積載重量が軽いトラックを取得
    #         weight_list[lightest_idx] += input_dict[i+1]  # 重量を追加
    #         truck_list[lightest_idx].append(i)
    #
    # for i in range(len(truck_list)):
    #     print('truck_', i, ':', truck_list[i])




if __name__ == '__main__':
    input_dict = {}
    input_list = input().split()  # 1:50 2:30 3:40 4:10
    print(input_list)
    input_list = [str.strip().split(':') for i, str in enumerate(input_list)]
    print(input_list)
    input_dict = dict((input_list))
    print(input_dict)
    print(len(input_dict))
    print(input_dict['1'])
    main(input_dict)
