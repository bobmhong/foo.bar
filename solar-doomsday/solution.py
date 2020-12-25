#!/bin/env python

def solution(area):

    available_material = int(area)
    planned_panel_areas = []

    while available_material > 0:
        largest_side = int(available_material ** .5)
        largest_panel_area = largest_side ** 2
        planned_panel_areas.append(largest_panel_area)
        available_material = available_material - largest_panel_area

    # print(planned_panel_areas)

    return planned_panel_areas


print(solution(15324))
print(solution(12))
print(solution(100))
print(solution(1000000))
print(solution(1283463))
