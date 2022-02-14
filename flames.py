def flames(name1, name2):
    """
main flames functions
    """
    for i in range(len(name1)):
        for j in range(len(name2)):
            # if common character is found
            # then remove that character
            # and return list of concatenated
            # list with True Flag
            if name1[i] == name2[j]:
                matching_word = name1[i]
        # remove character from the list
                name1.remove(matching_word)
                name2.remove(matching_word)

        # concatenation of two list elements with *
        # * is act as border mark here
                remaining_name = name1 + ["*"] + name2

        # return the concatenated list with True flag
                return [remaining_name, True]

    # no common characters is found
    # return the concatenated list with False flag
    remaining_name = name1 + ["*"] + name2
    return [remaining_name, False]


def clean_up(name_cleaning):
    """
    this cleans up the name
    """
    name_cleaning = name_cleaning.lower()
    name_cleaning = name_cleaning.replace(" ", "")
    name_cleaning_list = list(name_cleaning)
    return name_cleaning_list


def matching(name_cleaning_list, name_cleaning_list2):

    proceed = True

    # keep calling remove_match_char function
    # until common characters is found or
    # keep looping until proceed flag is True
    while proceed:

        # function calling and store return value
        ret_list = flames(name_cleaning_list, name_cleaning_list2)

        # take out concatenated list from return list
        con_list = ret_list[0]

        # take out flag value from return list
        proceed = ret_list[1]

        # find the index of "*" / border mark
        star_index = con_list.index("*")

        # list slicing perform

        # all characters before * store in name_cleaning_list
        name_cleaning_list = con_list[: star_index]

        # all characters after * store in name_cleaning_list2
        name_cleaning_list2 = con_list[star_index + 1:]

    # count total remaining characters
    count = len(name_cleaning_list) + len(name_cleaning_list2)

    # list of FLAMES acronym
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # keep looping until only one item
    # is not remaining in the result list
    while len(result) > 1:

        # store that index value from
        # where we have to perform slicing.
        split_index = (count % len(result) - 1)

        # this steps is done for performing
        # anticlock-wise circular fashion counting.
        if split_index >= 0:

            # list slicing
            right_list = result[split_index + 1:]
            left_list = result[: split_index]
            result = right_list + left_list

        else:
            result = result[: len(result) - 1]

    # print final result
    print("Relationship status :", result[0])
    return result[0]


if "__main__" == __name__:
    player1_name = input("Enter the name of the first person:")
    player2_name = input("Enter the name of the second person: ")
    player2_name = clean_up(player2_name)
    player1_name = clean_up(player1_name)
    FLAMES_RESULT = matching(player2_name, player1_name)
