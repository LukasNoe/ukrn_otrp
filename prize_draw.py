#This is a script to run a randomised prize raffle to select UKRN OTRP survey winners


import pandas as pd

def choose_winners_per_institution(csv_file, winners_file):
    df = pd.read_csv(csv_file)
    winners = []
    
    institutions = df['institution'].unique()
    for institution in institutions:
        institution_df = df[df['institution'] == institution]
        num_names = len(institution_df)
        sample_size = min(10, num_names)  # Adjust sample size if fewer than 10 names available
        institution_winners = institution_df.sample(n=sample_size, replace=False)['name'].tolist()
        winners.extend(institution_winners)

    return winners

# Example usage
csv_file = '../analysis/data/otrp_raffle_1805.csv'

winners_file = '../analysis/data/otrp_winners.csv'

choose_winners_per_institution(csv_file, winners_file)
print(f"The winners are saved to '{winners_file}'.")

