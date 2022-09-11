----------- CONVERT CSV FROM DELIM= ',' TO '\t' -----------

.to_csv(f'twitter/{handle}_followers_data.txt', index=False, sep='\t')
