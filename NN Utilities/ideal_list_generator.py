# -*- coding: utf-8 -*-
"""
ideal_list_generator()

@author: methylDragon

                                   .     .
                                .  |\-^-/|  .
                               /| } O.=.O { |\
                              /´ \ \_ ~ _/ / `\
                            /´ |  \-/ ~ \-/  | `\
                            |   |  /\\ //\  |   |
                             \|\|\/-""-""-\/|/|/
                                     ______/ /
                                     '------'
                       _   _        _  ___
             _ __  ___| |_| |_ _  _| ||   \ _ _ __ _ __ _ ___ _ _
            | '  \/ -_)  _| ' \ || | || |) | '_/ _` / _` / _ \ ' \
            |_|_|_\___|\__|_||_\_, |_||___/|_| \__,_\__, \___/_||_|
                               |__/                 |___/
            -------------------------------------------------------
                           github.com/methylDragon

Description:
Module for generating lists to simulate ideal outputs of simple classification
neural networks

Functions:
- ideal_list_generator(labels, sublabels, correct_label[, randomise = False])
"""

import random
from pprint import pprint

def ideal_list_generator(labels, sublabels, correct_label, randomise = False):
    """
    Generates a nested list that simulates the ideal outputs of NNs

    ideal_list_generator(labels, sublabels, correct_label[, randomise = False])

    It generates a labels x sublabels matrix of outputs!

    If you want to group batches of inputs together, increase the number of
    sub-labels!

    It also supports completely randomiseised outputs!
    In that case, the probability across each batch
    (each sub-label batch across the overall list) sums to 1!

    Parameters
    ----------
    - labels : int
        The number of output classes

    - sublabels : int
        The size of each output

    - correct_label : int
        The index of the label with 1 classification probability

    - randomise : bool, optional
        If you want randomised outputs instead
        
    Returns
    -------
    - output : list
        The desired list of size labels x sublabels that simulates the output
        matrix of a classification neural network
    """

    # Initialise output list
    output = []

    # If randomisation was not checked
    if randomise == False:

        # For each label/class, generate a list
        for index, label in enumerate(range(labels)):

            # If there are no multiple sublabels,
            # Populate output with ints, not lists
            if sublabels == 1:
                # If the index is the index of the specified correct label
                # Append a 1
                if index == correct_label:
                    output.append(1)
                # Otherwise, append a 0
                else:
                    output.append(0)

            # Otherwise, populate it with lists
            else:
                # If the index is the index of the specifed correct label,
                # Populate the output with a sublist of 1s
                if index == correct_label:
                    output.append([1] * sublabels)
                # Otherwise, populate the output with a sublist of 0s
                else:
                    output.append([0] * sublabels)

    # If randomisation is activated
    else:

        # Append sublists if there are multiple sublabels
        if sublabels != 1:
            for label in range(labels):
                output.append([])

        for sublabel in range(sublabels):

            # Initialise the total probability
            remaining_probability = 1.0

            # If there isn't multiple sublabels
            if sublabels != 1:

                # Iterate through the horizontal group of sublabels
                # (Index [0][0], [1][0], [2][0], so on...)
                for index, sub_label_list in enumerate(output):

                    # If we're not on the very last sub-label
                    if index != len(output) - 1:

                        # Generate a random probability within range
                        sub_label_probability = random.uniform(0.0, remaining_probability)
                        remaining_probability -= sub_label_probability

                        # Then append the generated random probability
                        sub_label_list.append(sub_label_probability)

                    # If we are on the last sub-label
                    else:

                        # Just append whatever is left
                        sub_label_list.append(remaining_probability)

            # Otherwise, append floats if there are multiple sublabels
            else:

                # Iterate through each label index
                for index, sub_label_list in enumerate(range(labels)):

                    # If we're not on the last label
                    if index != labels - 1:

                        # Generate a random probability within range
                        # And update the remaining probability left to distribute
                        sub_label_probability = random.uniform(0.0, remaining_probability)
                        remaining_probability -= sub_label_probability

                        # Then append the generated random probability
                        output.append(sub_label_probability)

                    # If we are on the last sub-label
                    else:

                        # Just append whatever is left
                        output.append(remaining_probability)

        # Shuffle for good measure if we're randomising
        random.shuffle(output)


    return output

# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    pprint(ideal_list_generator(3, 1, 1, True))