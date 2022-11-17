from dash import html, dcc
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

        dataexplorerfilter_button = lambda aio_id: {
            "component": "DataExplorerFilterAIO",
            "subcomponent": "dataexplorerfilter_button",
            "aio_id": aio_id,
        }

        dataexplorerfilter_body = lambda aio_id: {
            "component": "DataExplorerFilterAIO",
            "subcomponent": "dataexplorerfilter_body",
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
        label="",
        items=[],
        expanded=False,
        selected=None,
        lbl_sel_all="All",
    ):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        accordion = dbc.Button(
            id=self.ids.dataexplorerfilter_button(aio_id),
            type="button",
            color="link",
            className="row col-12",
            children=[label],
        )

        # is expanded? Show
        classname = "row col-12 div_de_filter"
        if expanded:
            classname = classname + " d-block"
        else:
            classname = classname + " d-none"

        # Is expanded? Create the items tree
        tree = None

        if expanded:
            start_time = time.time()
            tree_items = DataExplorerFilterAIO._get_tree_items(items)

            print(
                "--- %s seconds taken by the filter selection tree ---"
                % (time.time() - start_time)
            )
            
            print("selected")
            print(selected)

            tree = dash_treeview_antd.TreeView(
                id={"type": "filter_tree", "index": aio_id},
                checkable=True,
                multiple=True,
                checked=selected,
                expanded=["_root_" + aio_id],
                data={
                    "title": lbl_sel_all,
                    "key": "_root_" + aio_id,
                    "children": tree_items,
                },
            )

        acc_body = html.Div(
            id=self.ids.dataexplorerfilter_body(aio_id),
            className=classname,
            children=[tree],
        )

        # title = html.Div(children=[label])

        super().__init__(children=[accordion, acc_body])
