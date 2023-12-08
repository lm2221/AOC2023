import pandas as pd


def parse_file(filename):
    column_names = ['hand', 'bid']
    df = pd.read_csv(filename, header=None, names=column_names, sep=' ')
    return df


def count_character_occurrences(input_string):
    # Initialize an empty dictionary to store character counts
    char_counts = {}

    # Iterate through each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_counts[char] = 1
    return char_counts


def hand_type(input_string):

    count_cards = count_character_occurrences(input_string)
    hand_counts = count_cards.values()
    if 5 in hand_counts:
        return "Five of a kind"
    if 4 in hand_counts:
        return "Four of a kind"
    if 2 in hand_counts and 3 in hand_counts:
        return "Full house"
    if 3 in hand_counts and 2 not in hand_counts:
        return "Three of a kind"
    if 2 in hand_counts:
        result = [element == 2 for element in count_cards.values()]
        if sum(result) == 2:
            return "Two pair"
    if 2 in hand_counts:
        result = [element == 2 for element in count_cards.values()]
        if sum(result) == 1:
            return "One pair"
    if 1 in hand_counts and 4 not in hand_counts and 3 not in hand_counts and 2 not in hand_counts:
        return "High card"

def generate_ranking(hand_type):
    if hand_type == "High card":
        return 0
    elif hand_type == "One pair":
        return 1000
    elif hand_type == "Two pair":
        return 10000
    elif hand_type == "Three of a kind":
        return 100000
    elif hand_type == "Full house":
        return 1000000
    elif hand_type == "Four of a kind": 
        return 10000000
    elif hand_type == "Five of a kind":
        return 100000000
    
def map_card_to_values(card):
    if '2' == card:
        return 0
    if '3' == card:
        return 1
    if '4' == card:
        return 2
    if '5' == card:
        return 3
    if '6' == card:
        return 4
    if '7' == card:
        return 5
    if '8' == card:
        return 6
    if '9' == card:
        return 7
    if 'T' == card:
        return 8
    if 'J' == card:
        return 9
    if 'Q' == card:
        return 10
    if 'K' == card:
        return 11
    if 'A' == card:
        return 12


 ## Modified functions for solution 2   

def map_card_to_values_q2(card):
    if '2' == card:
        return 1
    if '3' == card:
        return 2
    if '4' == card:
        return 3
    if '5' == card:
        return 4
    if '6' == card:
        return 5
    if '7' == card:
        return 6
    if '8' == card:
        return 7
    if '9' == card:
        return 8
    if 'T' == card:
        return 9
    if 'J' == card:
        return 0
    if 'Q' == card:
        return 10
    if 'K' == card:
        return 11
    if 'A' == card:
        return 12
    

def hand_type_q2(input_string):

    count_cards = count_character_occurrences(input_string)

    if 'J' in count_cards:
        num_J = count_cards['J']
        count_cards.pop('J')
        try:
            max_key = max(count_cards, key=lambda k: count_cards[k])
            count_cards[max_key] += num_J
        except:
            count_cards['J'] = 5

    hand_counts = count_cards.values()

    if 5 in hand_counts:
        return "Five of a kind"
    if 4 in hand_counts:
        return "Four of a kind"
    if 2 in hand_counts and 3 in hand_counts:
        return "Full house"
    if 3 in hand_counts and 2 not in hand_counts:
        return "Three of a kind"
    if 2 in hand_counts:
        result = [element == 2 for element in count_cards.values()]
        if sum(result) == 2:
            return "Two pair"
    if 2 in hand_counts:
        result = [element == 2 for element in count_cards.values()]
        if sum(result) == 1:
            return "One pair"
    if 1 in hand_counts and 4 not in hand_counts and 3 not in hand_counts and 2 not in hand_counts:
        return "High card"

def break_ties(df):
    df['hand_type'] = df.apply(lambda x: hand_type(x['hand']), axis=1)
    df['rough_rank'] = df.apply(lambda x: generate_ranking(x['hand_type']), axis=1)
    df_expanded = df['hand'].apply(lambda x: pd.Series(list(x))).add_prefix('card')
    df_combined = pd.concat([df, df_expanded], axis=1)

    for col in ['card0', 'card1', 'card2', 'card3', 'card4']:
        df_combined['num_'+col] = df_combined[col].apply(lambda x: map_card_to_values(x))


    all_dataframes = []
    for htype in df_combined['hand_type'].unique():
        filtered_df = df_combined[df_combined['hand_type'] == htype]
        # Sort values by columns
        df_sorted = filtered_df.sort_values(by=['num_card0', 'num_card1', 'num_card2', 'num_card3', 'num_card4'])

        # Create a new column 'Rank' with the rank of each row in the sorted order
        df_sorted['rank'] = range(1, len(df_sorted) + 1)
        df_sorted['intermediate_rank'] = df_sorted['rank'] + df_sorted['rough_rank']

        all_dataframes.append(df_sorted)
        # print(df_sorted)
    
    result_df = pd.concat(all_dataframes, ignore_index=True)

    ## do the final sort
    result_df_sorted = result_df.sort_values(by=['intermediate_rank'])
    result_df_sorted['rank'] = range(1, len(result_df_sorted) + 1)
    return result_df_sorted


def break_ties_q2(df):
    df['hand_type'] = df.apply(lambda x: hand_type_q2(x['hand']), axis=1)
    df['rough_rank'] = df.apply(lambda x: generate_ranking(x['hand_type']), axis=1)
    df_expanded = df['hand'].apply(lambda x: pd.Series(list(x))).add_prefix('card')
    df_combined = pd.concat([df, df_expanded], axis=1)

    for col in ['card0', 'card1', 'card2', 'card3', 'card4']:
        df_combined['num_'+col] = df_combined[col].apply(lambda x: map_card_to_values_q2(x))


    all_dataframes = []
    for htype in df_combined['hand_type'].unique():
        filtered_df = df_combined[df_combined['hand_type'] == htype]
        # Sort values by columns
        df_sorted = filtered_df.sort_values(by=['num_card0', 'num_card1', 'num_card2', 'num_card3', 'num_card4'])

        # Create a new column 'Rank' with the rank of each row in the sorted order
        df_sorted['rank'] = range(1, len(df_sorted) + 1)
        df_sorted['intermediate_rank'] = df_sorted['rank'] + df_sorted['rough_rank']

        all_dataframes.append(df_sorted)
        # print(df_sorted)
    
    result_df = pd.concat(all_dataframes, ignore_index=True)

    ## do the final sort
    result_df_sorted = result_df.sort_values(by=['intermediate_rank'])
    result_df_sorted['rank'] = range(1, len(result_df_sorted) + 1)
    return result_df_sorted



def main():
    filename = '../data/7.txt'
    # filename = '../data/test_file_7.txt'
    df = parse_file(filename)

    # question 1
    final_df = break_ties(df)
    final_rank = final_df['bid'] * final_df['rank']
    print('q1', sum(final_rank))

    # question 2
    final_df_q2 = break_ties_q2(df)
    final_rank_q2 = final_df_q2['bid'] * final_df_q2['rank']
    print('q2', sum(final_rank_q2))


if __name__ == '__main__':
    main()