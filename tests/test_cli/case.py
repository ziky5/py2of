from pathlib import Path


case = {
    Path("system/controlDict"): {"endTime": 0.05},
    Path("constant/turbulenceProperties"): {"simulationType": "laminar"},
}
