userresponselist = []

genreList = [ 
        [ 1, "Hip Hop" ],
        [ 2, "pop" ],
        [ 3, "rock" ],
        [ 4, "heavy metal" ],
]

countryList = [ 
        [ 1, "use" ],
        [ 2, "japan" ],
        [ 3, "Europe" ],
        [ 4, "germany" ],
]

erralist = [ 
        [ 1, "1990" ],
        [ 2, "2000" ],
        [ 3, "2023" ],
        [ 4, "2014" ],
]

def introduceGame():
    print( "This game ...." )

def main():
    introduceGame()

    userName = input( "What is your name: " )
    generatedName = ""

    generatedName = generatedName + userName
    
    # Asking for the Genre
    for currentGenreNameIndex in range( len( genreList ) ):
        print( currentGenreNameIndex + 1, genreList[ currentGenreNameIndex ][1] )
    
    userGenreResponse = int( input( "Please select a genre: " ) )

    # Asking for the country
    for currentCountryNameIndex in range( len( countryList ) ):
        print( currentCountryNameIndex + 1, countryList[ currentCountryNameIndex ][1] )
    
    userCountryResponse = int( input( "Please select a country: " ) )

    # Asking for the era
    for currentErraNameIndex in range( len( erralist ) ):
        print( currentErraNameIndex + 1, erralist[ currentErraNameIndex ][1] )
    
    userErraResponse = int( input( "Please select an erra: " ) )

    genreNamePart = genreList[ userGenreResponse - 1 ][ 1 ]
    generatedName += genreNamePart

    countryNamePart = countryList[ userCountryResponse - 1 ][ 1 ]
    generatedName += countryNamePart


    erraNamePart = erralist [ userErraResponse - 1 ][ 1 ]
    generatedName += erraNamePart

    print( f" Your generated name is {generatedName}" )

main()


# print( userresponselist[0])
# print(userresponselist[2])
# userresponselist[0]="some other chips"
# print(userresponselist[0])
# mygrades = (50, 100, 45, 60)
# print(mygrades [0])
# mygrades[0]= 6 

