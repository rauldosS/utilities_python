class Bank:
    def __init__(self):
        self.agencies = [1111, 2222, 3333]
        self.clients = []
        self.accounts = []

    def insertClient(self, client):
        self.clients.append(client)

    def insertAccount(self, account):
        self.accounts.append(account)

    def authenticate(self, client):
        if client not in self.clients:
            return False

        if client.account not in self.accounts:
            return False

        if client.account.agency not in self.agencies:
            return False

        return True
