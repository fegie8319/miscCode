import pickle

with open('snp500.pickle', 'rb') as f:
    tickers = pickle.load(f)

print(tickers)
