import pandas as pd


def process_cashbacks_decorator(method):
    def wrapper(self, timestamp, *args, **kwargs):
        self.process_cashbacks(timestamp)
        return method(self, timestamp, *args, **kwargs)
    return wrapper


def store_balances_decorator(method):
    def wrapper(self, timestamp, account_id, *args, **kwargs):
        result = method(self, timestamp, account_id, *args, **kwargs)
        self.store_balance(timestamp, account_id)
        return result
    return wrapper


class BankTxns:
    def __init__(self):
        self.accounts = {}
        self.payment_counter = 0
        self.scheduled_cashbacks = {}
        self.historical_balances = {}

    @store_balances_decorator
    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.accounts:
            return False

        self.accounts[account_id] = {'balance': 0, 'outgoing': 0, 'payments': {}}
        return True

    @process_cashbacks_decorator
    @store_balances_decorator
    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        if account_id not in self.accounts:
            return None

        self.accounts[account_id]['balance'] += amount
        return self.accounts[account_id]['balance']

    @process_cashbacks_decorator
    @store_balances_decorator
    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None:
        if source_account_id not in self.accounts or target_account_id not in self.accounts:
            return None

        if source_account_id == target_account_id:
            return None

        if self.accounts[source_account_id]['balance'] < amount:
            return None

        self.accounts[source_account_id]['balance'] -= amount
        self.accounts[target_account_id]['balance'] += amount
        self.accounts[source_account_id]['outgoing'] += amount
        return self.accounts[source_account_id]['balance']

    def top_spenders(self, timestamp: int, n: int) -> list[str]:
        df = pd.DataFrame.from_dict(self.accounts, orient='index')
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'account_id'}, inplace=True)
        df_sorted = df.sort_values(by=['outgoing', 'account_id'], ascending=[False, True])
        return [f"{row['account_id']}({row['outgoing']})" for _, row in df_sorted.head(n).iterrows()]

    @process_cashbacks_decorator
    @store_balances_decorator
    def pay(self, timestamp: int, account_id: str, amount: int) -> str | None:
        if account_id not in self.accounts:
            return None

        if self.accounts[account_id]['balance'] < amount:
            return None

        self.payment_counter += 1
        payment_id = f"payment{self.payment_counter}"

        self.accounts[account_id]['balance'] -= amount
        self.accounts[account_id]['outgoing'] += amount
        self.accounts[account_id]['payments'][payment_id] = {'amount': amount, 'timestamp': timestamp,
                                                             'status': 'IN_PROGRESS'}
        cashback_amount = amount // 50
        cashback_time = timestamp + 86400000
        self.scheduled_cashbacks.setdefault(cashback_time, []).append((account_id, cashback_amount, payment_id))
        return payment_id

    def process_cashbacks(self, timestamp):
        _to_process = [x for x in self.scheduled_cashbacks if x <= timestamp]
        for t in _to_process:
            for account_id, cashback_amount, payment_id in self.scheduled_cashbacks[t]:
                if account_id in self.accounts:
                    self.accounts[account_id]['balance'] += cashback_amount
                    self.accounts[account_id]['payments'][payment_id]['status'] = 'CASHBACK_RECEIVED'
            del self.scheduled_cashbacks[t]

    @process_cashbacks_decorator
    def get_payment_status(self, timestamp: int, account_id: str, payment: str) -> str | None:
        if account_id not in self.accounts or payment not in self.accounts[account_id]['payments']:
            return None
        status = self.accounts[account_id]['payments'][payment]['status']
        return status

    def store_balance(self, timestamp, account_id):
        if account_id not in self.accounts:
            return None

        balance = self.accounts[account_id]['balance']
        if account_id in self.historical_balances:
            self.historical_balances[account_id].append((timestamp, balance))
        else:
            self.historical_balances[account_id] = [(timestamp, balance)]

    def get_balance(self, account_id, timestamp) -> int | None:
        if account_id not in self.accounts:
            return None

        closest_balance = None
        for time, balance in reversed(self.historical_balances[account_id]):
            if time <= timestamp:
                closest_balance = balance
                break
        if closest_balance is not None:
            return closest_balance
        else:
            return None


