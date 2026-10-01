from PIL import Image
from PIL import ImageChops

def FindBestImage(target, samples):
    ans=-1
    maxi=0
    #for i in range(len(samples)):
    #    diff=ImageChops.difference(target, samples[i])
    #    if maxi>diff:
    #        maxi=diff
    #        ans=i
    return ans