

from roboflow import Roboflow
rf = Roboflow(api_key="nMBrOGYRRVnkXQj6Il9x")
project = rf.workspace("brad-dwyer").project("aquarium-combined")
version = project.version(6)
dataset = version.download("coco")
                