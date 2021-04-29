from generated.synthetics_http_client.synthetics import ApiClient
from generated.synthetics_http_client.synthetics import Configuration
from generated.synthetics_http_client.synthetics import ApiException
from generated.synthetics_http_client.synthetics.api.synthetics_admin_service_api import SyntheticsAdminServiceApi
from generated.synthetics_http_client.synthetics.api.synthetics_data_service_api import SyntheticsDataServiceApi


class KentikAPI:
    def __init__(self, email: str, token: str, synthetics_url: str = "https://synthetics.api.kentik.com") -> None:
        configuration = Configuration(host=synthetics_url)
        configuration.api_key["email"] = email
        configuration.api_key["token"] = token
        client = ApiClient(configuration)
        self.synthetics = SyntheticsDataServiceApi(client)
