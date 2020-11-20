from typing import List, Dict

from .search import BatchSearch
from .config import api_token_version, wrapper_version, api_base_url


class MoleculeOneWrapper:
    """
    Wrapper for MoleculeOne Batch Scoring REST API
    """

    def __init__(
        self,
        api_token: str,
        api_base_url: str = api_base_url
    ):
        self.api_token = api_token
        self.api_base_url = f'{api_base_url}/' # ensure base_url ends with '/'
        self.request_headers = self.__prepare_request_headers()

    def __prepare_request_headers(self) -> dict:
        return {
            'Content-Type': 'application/json',
            'User-Agent': f'api-wrapper-python/{wrapper_version}',
            'Authorization': f'ApiToken-{api_token_version} {self.api_token}'
        }

    def run_batch_search(
            self,
            targets: List[str],
            parameters: Dict = None
    ) -> BatchSearch:
        return BatchSearch(
                self.api_base_url,
                self.request_headers,
                targets=targets,
                parameters=parameters
            )

    def get_batch_search(self, search_id: str) -> BatchSearch:
        return BatchSearch.from_id(
                self.api_base_url,
                self.request_headers,
                search_id
        )

    def delete_batch_search(self, search_id: str):
        search = BatchSearch.from_id(
                self.api_base_url,
                self.request_headers,
                search_id
        )
        return search.delete()

