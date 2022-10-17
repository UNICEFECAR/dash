from abc import ABC, abstractmethod
import pandas as pd
from typing import Union


class Data_access(ABC):
    def __init__(self, data_endpoint_id, data_endpoint_url):
        self.data_endpoint_id = data_endpoint_id  # Used by pandasdmx
        if data_endpoint_url.endswith("/"):
            self.data_endpoint_url = data_endpoint_url
        else:
            self.data_endpoint_url = data_endpoint_url + "/"

    # @abstractmethod
    # def get_codelists(self) -> dict:
    #     pass

    @abstractmethod
    def get_dataflow_info(
        self, agency: str, id: str, ver: str, print_stats=False
    ) -> dict:
        pass

    @abstractmethod
    def get_data(
        self,
        agency: str,
        id: str,
        ver: str,
        dq: Union[dict, str] = None,
        startperiod=None,
        endperiod=None,
        lastnobs=None,
        print_stats=False,
        labels="both",
    ) -> pd.DataFrame:
        pass
