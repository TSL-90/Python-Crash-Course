"""
This is just practice
"""
bands = ('tool', 'a perfect circle', 'puscifer')
for band in bands:  # associate 'band' with 'bands' for every band in the
    # list of bands, print the bands name
    # could also be "for maynard in bands: print(maynard)"
    print(f"{band.title()}, that was a great show!")
    print(f"I can't wait to see, {band.title()} again!\n")

print("Thank you all for putting on such a great show!")
