import sensirion_driver_adapters.mocks.response_provider as rp


class Stcc4ResponseProvider(rp.ResponseProvider):

    RESPONSE_MAP = {}

    def get_id(self) -> str:
        return 'Stcc4ResponseProvider'

    def handle_command(self, cmd_id: int, data: bytes, response_length: int) -> bytes:
        return self.RESPONSE_MAP.get(cmd_id, rp.random_bytes(response_length))
