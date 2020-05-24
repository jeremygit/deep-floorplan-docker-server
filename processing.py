from  DeepFloorplan import demo
from utils.SimpleNamespace import SimpleNamespace
import json

class Processing:
    path = ''
    def __init__(self, path):
        self.path = path

    def process_json_array(self):
        flrpln = demo.main(SimpleNamespace(im_path=self.path))
        return json.dumps(flrpln.tolist())

    def hello_check(self):
        return 'world'