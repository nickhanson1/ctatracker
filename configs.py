class Config:

    DEST_SHORT_NAMES = {"Forest Park" : "FP", "UIC-Halsted" : "UIC", "95th/Dan Ryan" : "95th",
                        "Howard" : "How", "Linden" : "Lndn", "Midway" : "Mdwy",
                        "Loop" : "Loop", "O'Hare" : "OHare"}

    CONFIG_NAMES = ["HOME"]

    CONFIGS = {
        "HOME" : {
            "MAP_ID" : 40320,
            "STATION" : "Division",
            "ROUTE_DEST" : ["Forest Park", "UIC-Halsted"],
        }
    }

_inst = Config()
DEST_SHORT_NAMES = _inst.DEST_SHORT_NAMES
CONFIG_NAMES = _inst.CONFIG_NAMES
CONFIGS = _inst.CONFIGS