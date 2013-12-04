# -*- coding: utf-8 -*-

import sys
import math

input_lines = sys.stdin
item_count = 0
campaign_count = 0

item_prices = list()
thresholds = list()
ans_price = list()
line_count = 0

# TODO : 二分法で再帰的に最適解を探査する

def get_neighbor_combination(price_list, threshold, smaller_index, bigger_index, result_list):
    '''
    :param list price_list: 商品価格リスト
    :param int threshold: 設定価格
    :param int smaller_index: price_listのうち組み合わせの低い方の要素候補のINDEX
    :param int bigger_index: price_listのうち組み合わせの高い方の要素候補のINDEX。再帰で呼ぶ間不変
    :param list result_list: 商品の組み合わせリスト
    '''
    if len(result_list) == 0:
        result_list.append(price_list[bigger_index])

    if bigger_index - smaller_index <= 1 or (smaller_index + bigger_index) / 2 == smaller_index or len(
            result_list) > math.log(bigger_index, 2):
        return result_list

    # 低い方の候補と高い方の候補の和が閾値を超えていたら、より安い候補を探査する。
    if price_list[smaller_index] + price_list[bigger_index] > threshold:
        get_neighbor_combination(price_list, threshold, smaller_index / 2, bigger_index, result_list)

    # 低い方の候補と高い方の候補の和が閾値を超えていない場合、これが一時的な最適解候補となる。
    if price_list[smaller_index] in result_list:
        return result_list

    result_list.append(price_list[smaller_index])

    # さらなる最適解を探査するため、smaller_indexとbigger_indexの中点の価格で再帰する。
    if bigger_index - smaller_index <= 1 or (smaller_index + bigger_index) / 2 == smaller_index or len(
            result_list) > 30:
        get_neighbor_combination(price_list, threshold, (smaller_index + bigger_index) / 2, bigger_index,
                                        result_list)

    return result_list

def sum_price(price_pair):
    '''
    :param list price_pair: 商品の組み合わせリスト
    '''
    if price_pair == None:
        return 0

    if len(price_pair) >= 2:
        return price_pair[0] + price_pair[len(price_pair) - 1]


def max_price_index_within_threshold(price_list, threshold):
    for p in price_list:
        if p >= threshold:
            return price_list.index(p)
    return len(price_list) - 1


for line in input_lines:
    l = line.rstrip().split(" ")
    if item_count == 0 and campaign_count == 0:
        item_count = int(l[0])
        campaign_count = int(l[1])
    elif 0 < line_count <= item_count:
        item_prices.append(int(l[0]))
    elif item_count < line_count:
        thresholds.append(int(l[0]))
    line_count += 1

item_prices.sort()

for threshold in thresholds:
    cnt = max_price_index_within_threshold(item_prices, threshold)
    ans_diff = 10000000
    ans = 10000000

    for i in xrange(0, cnt + 1):
        res_list = list()
        price_ans_list = get_neighbor_combination(item_prices, threshold, i / 2, i, res_list)
        ans_candidate = sum_price(price_ans_list)
        if ans_candidate <= threshold:
            ans = ans_candidate

    if ans == 10000000:
        ans_price.append(0)
    else:
        ans_price.append(ans)

for ans in ans_price:
    print ans

