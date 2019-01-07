import pokemon_names


def get_user_name(user):
    user_name = input("{0}: Please enter your name. ".format(user))
    return user_name


def get_pokemon_name(user_name):
    pokemon_name = input("{0} enter pokemon name: ".format(user_name))
    return pokemon_name


def check_if_pokemon_correct(pokemon_name, pokemons_names_used, pokemon_names_list):
    print(pokemon_names_list)


def main():
    user_one_name = get_user_name("User one")
    user_two_name = get_user_name("User two")
    pokemons_names_used = []
    while True:
        pokemon_name = get_pokemon_name(user_one_name)
        check_if_pokemon_correct(pokemon_name, pokemons_names_used, pokemon_names.pokemons_name_list)


if __name__ == '__main__':
    main()
