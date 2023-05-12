from dash import html, dcc, callback
from dash.dependencies import MATCH, Input, Output, State, ALL
import dash_bootstrap_components as dbc
import uuid
import dash_treeview_antd

import time


class DataExplorerFilterAIO(html.Div):
    class ids:
        dataexplorerfilter = lambda aio_id: {
            "component": "DataExplorerFilterAIO",
            "subcomponent": "dataexplorerfilter",
            "aio_id": aio_id,
        }

    ids = ids

    # Not efficient: to review, it loops the whole codelist each time
    def _add_tree_level(tree_node, parent_code, items):
        # check if the current code is a child of the parent code
        for c in items:
            if "parent" in c and c["parent"] == parent_code:
                if "children" not in tree_node:  # create a new tree node
                    tree_node["children"] = []
                tree_node["children"].append({"key": c["id"], "title": c["name"]})
                DataExplorerFilterAIO._add_tree_level(
                    tree_node["children"][-1], c["id"], items
                )

    def _get_tree_items(items):
        ret = []
        for c in items:
            # it is a root node, add it and start the recursion
            if "parent" not in c or c["parent"] == "":
                ret.append({"key": c["id"], "title": c["name"]})
                # recursion
                DataExplorerFilterAIO._add_tree_level(ret[-1], c["id"], items)
        return ret

    def __init__(
        self,
        aio_id=None,
        filters=None,
        expanded=False,
        selected=None,
        lbl_sel_all="All",
    ):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        accordionItems = []

        for f in filters:
            sel = []
            if f["id"] in selected:
                sel = selected[f["id"]]
            tree_items = DataExplorerFilterAIO._get_tree_items(f["codes"])
            tree = dash_treeview_antd.TreeView(
                id={"type": "filter_tree", "index": aio_id},
                checkable=True,
                multiple=True,
                checked=sel,
                expanded=["_root_" + aio_id],
                data={
                    "title": lbl_sel_all,
                    "key": "_root_" + aio_id,
                    "children": tree_items,
                },
            )
            tree_div = html.Div(
                className="overflow-auto m-0 p-0 div_de_filter",
                children=tree,
            )
            accitem = dbc.AccordionItem(
                title=f["name"],
                children=tree_div,
                class_name="accordion-no-padding",
                item_id=f"de_acc_{f['id']}",
            )
            accordionItems.append(accitem)

        accordion = dbc.Accordion(
            accordionItems, id="_de_acc", flush=True
        )

        super().__init__(children=[accordion], className="p-0 m-0")
