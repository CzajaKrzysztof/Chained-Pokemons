import pokemon_names


def get_user_name(user):
    user_name = input("{0}: Please enter your name. ".format(user))
    return user_name


def get_pokemon_name(user_name):
    pokemon_name = input("{0} enter pokemon name: ".format(user_name))
    return pokemon_name


def add_used_pokemon_name(pokemon_name, pokemons_names_used):
    pokemons_names_used.append(pokemon_name)


def check_if_pokemon_correct(pokemon_name, pokemons_names_used, pokemon_names_list):
    if pokemon_name not in pokemon_names_list or pokemon_name in pokemons_names_used:
        is_answer_correct = False
    else:
        is_answer_correct = True
        add_used_pokemon_name(pokemon_name, pokemons_names_used)
    return is_answer_correct


def main():
    user_one_name = get_user_name("User one")
    user_two_name = get_user_name("User two")
    pokemons_names_used = []
    while True:
        pokemon_name = get_pokemon_name(user_one_name)
        is_answer_correct = check_if_pokemon_correct(pokemon_name, pokemons_names_used,
                                                     pokemon_names.pokemons_name_list)


if __name__ == '__main__':
    main()
