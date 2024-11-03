from allpairspy import AllPairs

parameters = [
    ["720p", "1080p", "1440p", "4K", "8K"],
    ["None", "FXAA", "MSAA x2", "MSAA x4", "MSAA x8" ],
    ["Low", "Medium", "High", "Very High", "Ultra"],
    ["Low", "Medium", "High"],
    ["None", "Low", "High"],
]

print("PAIRWISE TEST CASE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))