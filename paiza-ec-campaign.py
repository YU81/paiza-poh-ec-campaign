# -*- coding: utf-8 -*-

import sys

input_lines = sys.stdin
item_count = 0
campaign_count = 0

item_prices = list()
thresholds = list()
ans_price = list()
line_count = 0

# TODO : 二分法で再帰的に最適解を探査する
# def get_neighbor_combination(price_list,threshold,list_count,start_index, result_list):
#     # 指定INDEXの値が設定価格より大きければ、そのINDEXの半値でこれを再帰実行
#     if price_list[start_index] > threshold:
#         get_neighbor_combination(price_list,threshold,list_count,start_index / 2)
#     # 指定INDEXの値が設定価格以下なら、
#     elif price_list[start_index] < threshold:
#         if price_list.count() == 0:
#             result_list.append(price_list[start_index])
#         elif result_list[0] + price_list[start_index] < threshold:
#
#

def sum_price(price_pair):
    return price_pair[0] + price_pair[1]

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
        for j in xrange(0, cnt + 1):
            if threshold < (item_prices[i] + item_prices[j]):
                break

            if i != j and ans_diff > abs(threshold - (item_prices[i] + item_prices[j])):
                ans = item_prices[i] + item_prices[j]
                ans_diff = abs(threshold - (item_prices[i] + item_prices[j]))

            if ans_diff == 0:
                break

    if ans == 10000000:
        ans_price.append(0)
    else:
        ans_price.append(ans)

for ans in ans_price:
    print ans

