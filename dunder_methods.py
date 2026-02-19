import uuid


class APIClient:
    # class-level defaults shared across all instances
    DEFAULT_RETRY_MAX = 7
    DEFAULT_SLEEP_TIME_SECONDS = 1.25

    def __init__(self, client_id: str, client_secret: str, **kwargs):
        # standard construction: authenticate with credentials
        print("standard construction")
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self._create_token()

        self._common_attributes(**kwargs)

    def _common_attributes(self, **kwargs):
        self.retry_max = kwargs.get("retry_max", self.DEFAULT_RETRY_MAX)
        self.sleep_time_seconds = kwargs.get(
            "sleep_time_seconds", self.DEFAULT_SLEEP_TIME_SECONDS
        )

    def _create_token(self):
        # imagine this uses id and secret to get token
        return uuid.uuid4().hex

    @classmethod
    def from_token(cls, token: str, **kwargs):
        print("alternative approach")
        instance = cls.__new__(cls)  # allocate without calling __init__
        instance.client_id = None
        instance.client_secret = None
        instance.token = token
        instance._common_attributes(**kwargs)
        return instance


some = APIClient(client_id="somme_id", client_secret="some_secret", retry_max=0)
print(vars(some))

some2 = APIClient.from_token(token="some-token")
print(vars(some2))
