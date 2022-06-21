import pandas as pd
import re
from . import SdmxApi


class Dataflow:

    def __init__(self):
        self.endpoint = None
        self.agency = None
        self.dataflow_id = None
        self.version = None
        self.df = None
        self.structure = None
        self.concepts = None
        self.codelists = None

    def download_dataflow_structure(self, endpoint, agency, dataflow_id, version, dataquery=None):
        """
        Downloads the dataflow
        :param api_endpoint: The SDMX registry endpoint
        :param agency: the SDMX agency
        :param dataflow_id: the dataflow id
        :param version: the dataflow version
        :param dataquery: Optinal dataquery
        """

        self.api_endpoint = endpoint
        self.agency = agency
        self.dataflow_id = dataflow_id
        self.version = version

        sdmx_api = SdmxApi.SdmxApi(self.api_endpoint)
        self.structure = sdmx_api.get_structure(self.agency, self.dataflow_id, self.version)
        # self.df = sdmx_api.get_dataflow_as_dataframe(self.agency, self.dataflow_id, self.version, dataquery=dataquery,
        #                                              labels="id")

        self.__parse_structure()

    # Parses the structure
    def __parse_structure(self):
        # parse and organize the concepts
        self.concepts = self.__parse_concepts()
        self.codelists = self.__parse_codelists()

    def __get_concept(self, concept_identity):
        """
        Returns the concept given the concept identity
        :param concept_identity: the concept Identity string
        :return: The concept
        """
        conc_keys = ["agencyID", "id", "version"]
        conc_id = concept_identity.split("=")[1]
        # the concept_identity is: UNICEF:UNICEF_CONCEPTS(1.0).AGE
        # this regex splits matching: ":" "(" and ").". It will produce 4 tokens
        conc_id = re.split(":|\(|\).", conc_id)
        conc_id = {"agencyID": conc_id[0],
                   "id": conc_id[1],
                   "version": conc_id[2],
                   "concept": conc_id[3]
                   }

        conc_scheme = [x for x in self.concepts if Dataflow.__compare_obj(
            x, conc_id, conc_keys)]
        if len(conc_scheme) > 0:
            if conc_id["concept"] in conc_scheme[0]["concepts"]:
                return conc_scheme[0]["concepts"][conc_id["concept"]]
        return None

    def __get_codelist(self, enumeration_id):
        """
        Returns the codelists as a PD dataframe given the enumeration id
        :param enumeration_id: the enum id
        :return: the codelist as a PD Dataframe
        """
        enum_keys = ["agencyID", "id", "version"]
        enum_id = enumeration_id.split("=")[1]
        # the enumeration id is: UNICEF:CL_INDICATORS(1.0)
        # this regex splits matching: ":" "(" and ")". It will produce 4 tokens
        enum_id = re.split("[:()]", enum_id)
        enum_id = {"agencyID": enum_id[0],
                   "id": enum_id[1],
                   "version": enum_id[2]
                   }

        cl = [x for x in self.codelists if Dataflow.__compare_obj(
            x, enum_id, enum_keys)]
        if len(cl) > 0:
            return cl[0]["cl_df"]
        return None

    # util function: given the list of dims or attribs returns the list of id-labels (labels pulled from the concetps)
    def __dims_attr_create(self, node):
        ret = []
        for item in node:
            name = item["id"]
            concept = self.__get_concept(item["conceptIdentity"])
            if concept is not None:
                name = concept["name"]
            ret.append({
                "id": item["id"],
                "name": name
            })
        return ret

    def get_dimensions(self):
        """
        :return: the list of dimensions
        """
        dims_node = self.structure["data"]["dataStructures"][0]["dataStructureComponents"]["dimensionList"][
            "dimensions"]
        return self.__dims_attr_create(dims_node)

    def get_attributes(self):
        """
        The list of attrbutes
        :return:
        """
        attrs_node = self.structure["data"]["dataStructures"][0]["dataStructureComponents"]["attributeList"][
            "attributes"]
        return self.__dims_attr_create(attrs_node)

    # Creates a pandas dataframe containing the codelist
    # @staticmethod
    # def __codelist_to_pd(codes):
    #     ret = pd.DataFrame(columns=["id", "name", "description", "parent"])
    #     for c in codes:
    #         to_add = {"id": c["id"], "name": c["name"]}
    #         if "parent" in c:
    #             to_add["parent"] = c["parent"]
    #         if "description" in c:
    #             to_add["description"] = c["description"]
    #         # ret = ret.append(to_add, ignore_index=True)
    #         to_add = pd.DataFrame(to_add, index=[0])
    #         ret = pd.concat([ret, pd.DataFrame(to_add)], ignore_index=True)
    #     return ret

    # Parses the concepts and puts them in a more convenient structure
    def __parse_concepts(self):
        ret = []
        concept_schemes = self.structure["data"]["conceptSchemes"]

        # Create an entry for each concept scheme (group of concepts)
        for cs in concept_schemes:
            to_add = {
                "agencyID": cs["agencyID"],
                "id": cs["id"],
                "version": cs["version"],
                "concepts": {}}
            # each concept scheme contains multiple concepts, loop through them and add to the dict
            for c in cs["concepts"]:
                to_add["concepts"][c["id"]] = {
                    "name": c["name"],
                    "names": c["names"]
                }
            ret.append(to_add)
        return ret

    # util function compares the passed keys(keys_to_compare) in two objects
    @staticmethod
    def __compare_obj(o1, o2, keys_to_compare):
        for k in keys_to_compare:
            if k not in o1 or k not in o2 or o1[k] != o2[k]:
                return False
        return True

    # Parses the codelists, returns a list containing the codelists' id and the codelists as a pd dataframe
    def __parse_codelists(self):
        ret = []
        for cl in self.structure["data"]["codelists"]:
            to_add = {
                "agency": cl["agencyID"],
                "id": cl["id"],
                "version": cl["version"],
                # "cl_df": self.__codelist_to_pd(codes=cl["codes"])
                "cl_df": pd.DataFrame(cl["codes"])
            }
            ret.append(to_add)
        return ret
