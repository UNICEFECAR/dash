import plotly.express as px

from .base_page import get_base_layout


indicators_dict = {
    "PARTICIPATION": {
        "NAME": "Education access and participation",
        "CARDS": [
            {
                "name": "Who are Out-of-School",
                "indicator": "REPROV_EFFINAL_MUNICIPAL",
                "suffix": "Primary to upper secondary aged Children and Adolescents",
                "age": "_T",
            },
        ],
    },
}


main_title = "Education"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)