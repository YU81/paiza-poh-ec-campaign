# coding: utf-8

import sys
import bisect

input_lines = sys.stdin
item_count = 0
campaign_count = 0

item_prices = list()
thresholds = list()
ans_price = list()
line_count = 0

def bisect_search(price_list, threshold, bigger_index, max_pair_sum):
    '''
    :param list price_list: 商品の価格リスト。ソート済み前提
    :param int threshold: 商品の設定価格
    :param int bigger_index: 商品のペアの内、価格が高い方の商品候補。
    :param int max_pair_sum: 比較対象とするこれまでで最大の合計価格候補
    '''

    # 設定価格と高い方の商品の差額 
    residue = threshold - price_list[bigger_index]
    # 設定価格に最も近くなる安い商品の候補のインデックス
    smaller_candidate_index = bisect.bisect_left(price_list, residue + 1) - 1 
    if smaller_candidate_index < 0 or bigger_index == smaller_candidate_index:
        return max_pair_sum

    # 条件を満たす2商品の合計価格候補
    max_pair_sum_new_candidate = price_list[smaller_candidate_index] + price_list[bigger_index]
    # 引数で渡ってきた最大価格候補と、ここで求めた2商品合計価格のうち大きい方を返す。
    max_pair_sum = max_pair_sum_new_candidate if max_pair_sum - max_pair_sum_new_candidate <= 0 and max_pair_sum_new_candidate <= threshold else max_pair_sum

    return max_pair_sum

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
    cnt = bisect.bisect_right(item_prices, threshold) - 1
    ans = 0

    for i in xrange(cnt,0,-1):
        if ans == threshold:break
        ans_candidate = bisect_search(item_prices, threshold, i, ans)
        if ans_candidate <= threshold and ans_candidate != None:
            if ans < ans_candidate:
                ans = ans_candidate

    if ans == 0 or ans == None:
        ans_price.append(0)
    else:
        ans_price.append(ans)

for ans in ans_price:
    print ans
