#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_Array = list(csv_reader)
        timeArray = [0 for i in range(24)]
        for row in csv_Array[1:]:
            a = row[1][0:2]
            if not a.isdigit():
                continue
            a = int(a)
            timeArray[a] += 1
    return timeArray

def weigh_pokemons(filename, weight):
    name = []
    with open(filename) as a:
        pokemon = json.load(a)
        for poke in pokemon['pokemon']:
            if float(poke['weight'][:-2]) == weight:
                name.append(poke['name'])
        return name

def single_type_candy_count(filename):
    sum = 0;
    with open(filename) as a:
        pokemon = json.load(a)
        for poke in pokemon['pokemon']:
            if len(poke["type"]) == 1 and 'candy_count' in poke:
                sum += poke["candy_count"]
        return sum

def reflections_and_projections(points):
    for i in points:
        i[1] = 2 - i[i]
        a = [[0,-1], [1,0]]
        b = [i[0]][i[1]]
        np.matmul(a, b)
        a = [[1, 3][3, 9]]
        return np.matmul(a, b)

def normalize(image):
    min = image[0][0]
    max = image[0][0]
    for i in image:
        for j in i:
            if j < min:
                min = j
            if j > max:
                max = j
    for i in range(31):
        for j in range(31):
            image[1][j] = 255.0/(max - min) * (j - min)
    return image

def sigmoid_normalize(image):
    pass
