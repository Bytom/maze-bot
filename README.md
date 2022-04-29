# maze-bot


# Liunx && Mac

```shell
#first:
git clone git@github.com:Bytom/mov-mmdk.git ./mov-mmdk
cd mov-mmdk
sudo python3 setup.py install
cd ..


pip3 install -r requirements.txt


#then you can import like below:
```

# Use Example

```python
python3 maze.py create-account "btm_test_net" '{"password":"123", "filepath":"account.json"}'
python3 maze.py update-account
python3 maze.py query-account "btm_test_net" '{"address": "0x673f03b59a0484cb3e601b46f0f017a0757446c7"}'
python3 maze.py query-account-income "btm_test_net" '{"address": "0x673f03b59a0484cb3e601b46f0f017a0757446c7"}'
python3 maze.py buy-nft "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":23, "deposit":10, "filepath":"account.json", "password":"123"}'

python3 maze.py adjust-nft-deposit "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":23, "deposit":5, "password":"123", "filepath":"account.json"}'
python3 maze.py apply-offer "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":23, "price": 123, "deposit": 10, "password": "123", "filepath":"account.json"}'
python3 maze.py cancel-offer "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":23, "password": "123", "filepath":"account.json"}'
python3 maze.py give-nft "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":23, "toAddress": "0x2B522cABE9950D1153c26C1b399B293CaA99FcF9", "password":"123", "filepath":"account.json"}'
python3 maze.py query-nft-detail "btm_test_net" '{"erc721Address":"0x1819bfe00c0c0aee24b88ace7bff36d574d70180","tokenId":6}'
python3 maze.py query-nft-detail "btm_test_net" '{"erc721Address":"0x1819bfe00c0c0aee24b88ace7bff36d574d70180","tokenId":20}'
python3 maze.py query-author "btm_test_net" '{"address":"0x1819bfe00c0c0aee24b88ace7bff36d574d70180"}'
python3 maze.py query-author "btm_test_net" '{"address":"0x673f03b59a0484cb3e601b46f0f017a0757446c7"}'
python3 maze.py query-market-info "btm_test_net" '{"market_type":"trade","limit":10}'
python3 maze.py query-market-info "btm_test_net" '{"market_type":"high_price","limit":10}'
python3 maze.py query-market-info "btm_test_net" '{"market_type":"low_price","limit":10}'

python3 maze.py query-offers "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId": 6}'

# 乔
python3 maze.py buy-nft "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":6, "deposit":7, "filepath":"account.json", "password":"123"}'
python3 maze.py buy-nft "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":26, "deposit":7, "filepath":"account.json", "password":"123"}'

python3 maze.py apply-offer "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":6, "price": 1, "deposit": 10, "password": "123", "filepath":"account.json"}'
python3 maze.py cancel-offer "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":6, "password": "123", "filepath":"account.json"}'

python3 maze.py apply-offer "btm_test_net" '{"erc721Address":"0x1819BFe00C0c0aEe24B88aCE7bff36d574d70180", "tokenId":21, "price": 1, "deposit": 10, "password": "123", "filepath":"account.json"}'

```

