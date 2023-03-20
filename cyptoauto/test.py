import pyupbit

access = "gK4VZzLzm39FNsfvMRrZc18b0DorK78JmM0G2zJx"          # 본인 값으로 변경
secret = "dIQCjDnrHH2I37UxdUgwFH7YAKupM2KQktnBsSIK"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회