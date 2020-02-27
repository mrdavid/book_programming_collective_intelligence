#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt
# A dictionary of movie critics and their ratings of a small set of movies
critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
    'empty': {},
}
# Above dictionary copied from https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter2/recommendations.py

# Sample commands
print("print(critics['Toby']['Superman Returns'])")
print(critics['Toby']['Superman Returns'])

def sim_distance(prefs, person1, person2):
    # Get the list of shared items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0: return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item],2) for
        item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sum_of_squares)

print("Sample distance")
print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))

def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rate items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)
    # if they have no ratings in common, return 0
    if n == 0: return 0

    #  Add up all of the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it],2) for it in si])

    # Sum up the products
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # Calculate pearson score
    num=pSum - (sum1*sum2)/n
    den=sqrt((sum1Sq - pow(sum1,2)/n) * (sum2Sq-pow(sum2,2)/n))
    if den == 0: return 0

    r = num/den
    return r

print("Pearson score")
print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))

# Tanimoto score
# See https://en.wikipedia.org/wiki/Jaccard_index#Tanimoto_similarity_and_distance
# Implement Jaccard Index instead
def sim_jaccard(prefs, p1, p2):
    # Get the list of mutually rate items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    p1_A_p2 = len(si)
    cardinality_p1 = len(prefs[p1])
    cardinality_p2 = len(prefs[p2])

    if cardinality_p1 == 0 and cardinality_p2 == 0:
        return 0

    return 1.0 * p1_A_p2 / (cardinality_p1 + cardinality_p2 - p1_A_p2)

print("Jaccard index")
print(sim_jaccard(critics, 'Lisa Rose', 'Gene Seymour'))
print(sim_jaccard(critics, 'Lisa Rose', 'Michael Phillips'))
print(sim_jaccard(critics, 'Lisa Rose', 'empty'))
