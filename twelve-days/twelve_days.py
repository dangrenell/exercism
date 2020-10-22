def recite_one(verse: int) -> list:
    num_dict = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth',
                7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}
    verse_list = ['twelve Drummers Drumming,',
                  'eleven Pipers Piping,',
                  'ten Lords-a-Leaping,',
                  'nine Ladies Dancing,',
                  'eight Maids-a-Milking,',
                  'seven Swans-a-Swimming,',
                  'six Geese-a-Laying,',
                  'five Gold Rings,',
                  'four Calling Birds,',
                  'three French Hens,',
                  'two Turtle Doves,',
                  'and a Partridge in a Pear Tree.']
    intro = f'On the {num_dict[verse]} day of Christmas my true love gave to me:'

    output = [intro]
    output.extend([vrs for vrs in verse_list[12-verse:]]
                  if verse > 1 else ['a Partridge in a Pear Tree.'])
    return ' '.join(output)


def recite(start_verse, end_verse):
    output = []
    output.extend([recite_one(verse)
                   for verse in range(start_verse, end_verse+1)])
    return output
