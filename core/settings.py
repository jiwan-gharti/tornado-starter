import os
import pathlib



settings = dict(
    template_path = os.path.join(pathlib.Path(__file__).parent.parent, "templates"),
    static_path = os.path.join(pathlib.Path(__file__).parent.parent, "static"),
    debug = True,
    autoreload=True,
)