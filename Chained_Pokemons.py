import os
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
    while True:
        pokemons_names_used = []
        os.system('clear')
        while True:
            pokemon_name = get_pokemon_name(user_one_name)
            os.system('clear')
            is_answer_correct = check_if_pokemon_correct(pokemon_name, pokemons_names_used,
                                                         pokemon_names.pokemons_name_list)
            if is_answer_correct:
                pokemon_name = get_pokemon_name(user_two_name)
                os.system('clear')
                is_answer_correct = check_if_pokemon_correct(pokemon_name, pokemons_names_used,
                                                             pokemon_names.pokemons_name_list)
                if is_answer_correct is not True:
                    print("{0} your anser was wrong. You lose.".format(user_two_name))
                    break
            else:
                print("{0} your anser was wrong. You lose.".format(user_one_name))
                break

        repeat_game = input("\nDo you want to play again (y/n)? ")
        if repeat_game == 'y':
            continue
        else:
            os.system('clear')
            break


if __name__ == '__main__':
    main()
