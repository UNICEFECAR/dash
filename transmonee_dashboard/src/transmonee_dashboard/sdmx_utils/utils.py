import requests
import json


def get_codelist(url, lang=None):
    codelist_get_params = {"format": "sdmx-json", "detail": "full", "references": "none"}
    if lang is None:
        r = requests.get(url, params=codelist_get_params)
    else:
        r = requests.get(url, params=codelist_get_params, headers={"Accept-Language": lang})

    if r.ok:
        ret = []
        # jsondata = r.content.decode("utf-8")
        # jsondata = json.loads(jsondata)
        jsondata = r.json()
        for c in jsondata['data']['codelists'][0]['codes']:
            ret.append({"id": c["id"], "name": c["name"]})
            if "description" in c:
                ret[-1]["description"] = c["description"]
            if "parent" in c:
                ret[-1]["parent"] = c["parent"]
        return ret
    else:
        raise (ConnectionError(
            "Error downloading " + url + " status code: " + str(r.status_code) + r.raise_for_status()))


'''
def _json_codelist_to_dataframe(codelist_sdmx_json, lang = None, force_any_language_when_no_lang = True):
  ret = pd.DataFrame(columns=["id", "name", "desc", "parent"], dtype=str)

  for i in codelist_sdmx_json['data']['codelists'][0]['codes']:
    #toAdd = {"id": i["id"], "name": i["names"].items()[0]}
    toAdd = {"id": i["id"]}
    if lang is not None and lang in i["names"]:
      toAdd["name"] = i["names"][lang]
    elif force_any_language_when_no_lang: #fallback
      toAdd["name"] = list(i["names"].values())[0]
    else: toAdd["name"] = None
      
    if "description" in i:
      toAdd["desc"] = i["description"]
    if "parent" in i:
      toAdd["parent"] = i["parent"]
    ret = ret.append(toAdd, ignore_index=True)
  return ret
  
  '''
