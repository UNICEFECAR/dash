from . import SdmxApi


class Codelist:

    def __init__(self):
        self.api_endpoint = None
        self.agency = None
        self.id = None
        self.version = None
        self.codes = None

    def download_codelist(self, endpoint, agency, id, version="latest"):
        self.api_endpoint = endpoint
        self.agency = agency
        self.id = id
        self.version = version

        sdmx_api = SdmxApi.SdmxApi(self.api_endpoint)
        cl = sdmx_api.get_codelist(self.agency, self.id, self.version)
        self.codes = cl["data"]["codelists"][0]["codes"]
        for c in self.codes:
            del c["links"]


    def get_codes(self):
        return self.codes
