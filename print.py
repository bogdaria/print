def print_readable_balance(balance, decimals, token):
    balance_readable = convert_token_units(balance, decimals)
    if balance_readable > 0:
        balance_formatted = format(balance_readable, ".2f")
        print(f"{token}: {balance_formatted}")
