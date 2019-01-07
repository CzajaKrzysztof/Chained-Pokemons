pokemins = ['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon',
            'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig',
            'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune',
            'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone', 'mamoswine', 'nosepass',
            'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel',
            'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon',
            'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue',
            'vigoroth', 'vulpix', 'wailord', 'artortle', 'whismur', 'wingull', 'yamask']


def get_user_name(user):
    while True:
        try:
            user_name = input("{0}: Please enter your name. ".format(user))
        except ValueError:
            print("Please use only letters.")
        else:
            return user_name


def get_pokemon_name(user_name):
    while True:
        try:
            pokemon_name = input("Enter pokemon name: ")
        except ValueError:
            print("Please enter valid integers for the height.")
        else:
            break


def main():
    user_one_name = get_user_name("User one")
    user_two_name = get_user_name("User two")
    while True:
        get_pokemon_name("ser_one")
        get_pokemon_name("ser_one")


if __name__ == '__main__':
    main()
