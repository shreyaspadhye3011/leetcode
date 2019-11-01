# Amazon
# Status: Brute force. Working but had run time error in few cases that were not shown. Security checks may need to be applied

# TODO: Optimize
import operator
def popularNToys(numToys, topToys, toys, 
                    numQuotes, quotes):
    result = []
    while(topToys > 0):
        toyFrequency = {}
        for quote in quotes:
            for toy in toys:
                if toy in quote.split():
                    toyFrequency[toy] = toyFrequency.get(toy, 0) + 1
        topToy = max(toyFrequency.items(), key=operator.itemgetter(1))[0]
        result.append(topToy)
        toys.remove(topToy)
        topToys -= 1
    return result