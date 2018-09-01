# with parameters -> accepts inputs
#without parameters -> does not accept inputs
#fruitful function  -> returns data
# non-fruitful  --> does not return data

# function that removes - and replace with a .
# .replace( "-", ".")

def generateUrlSlug( titleOfBlog ):
    print( titleOfBlog)
    # remove spaces at the beginning and end of my input
    strippedTitle = titleOfBlog.strip()
    # replace all spaces inside with dashes
    dashedTitle = strippedTitle.replace(" ", "-")
    # make everything character lower case
    lowerCaseTitle = dashedTitle.lower()
    # return the result
    
    return lowerCaseTitle



def main():
    pass
    theTitle = input(" What is the tite of your blog: ")

    print( "Here is the url of the blog:" )
    urlReady = generateUrlSlug( theTitle )
    print( urlReady)

if __name__ == "__main__":

    main()