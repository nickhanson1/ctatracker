class Config:

    DISPLAY_WIDTH = 25
    DISPLAY_HEIGHT = 2

    UPDATE_TIME = 30

    LETTER_WIDTH = 5
    LETTER_HEIGHT = 7

    DEST_SHORT_NAMES = {"Forest Park" : "FP", "UIC-Halsted" : "UIC", "95th/Dan Ryan" : "95th",
                        "Howard" : "How", "Linden" : "Lndn", "Midway" : "Mdwy",
                        "Loop" : "Loop", "O'Hare" : "OHare"}
    
    MAP_IDS = {
            "18th" : 40830,
            "35th-Bronzeville-IIT" : 41120,
            "35th/Archer" : 40120,
            "43rd" : 41270,
            "47th (Green Line)" : 41080,
            "47th (Red Line)" : 41230,
            "51st" : 40130,
            "54th/Cermak" : 40580,
            "63rd" : 40910,
            "69th" : 40990,
            "79th" : 40240,
            "87th" : 41430,
            "95th" : 40450,
            "Adams/Wabash" : 40680,
            "Addison (Blue Line)" : 41240,
            "Addison (Brown Line)" : 41440,
            "Addison (Red Line)" : 41420,
            "Argyle" : 41200,
            "Armitage" : 40660,
            "Ashland/63rd" : 40290,
            "Ashland (Green, Pink Lines)" : 40170,
            "Ashland (Orange Line)" : 41060,
            "Austin (Blue Line)" : 40010,
            "Austin (Green Line)" : 41260,
            "Belmont (Red, Brown, Purple Lines)" : 41320,
            "Belmont (Blue Line)" : 40060,
            "Berwyn" : 40340,
            "Bryn Mawr" : 41380,
            "California (Pink Line)" : 40440,
            "California (Green Line)" : 41360,
            "California (Blue Line-O'Hare Branch)" : 40570,
            "Central Park" : 40780,
            "Central (Green Line)" : 40280,
            "Central (Purple Line)" : 41250,
            "Cermak-Chinatown" : 41000,
            "Cermak-McCormick Place" : 41690,
            "Chicago (Blue Line)" : 41410,
            "Chicago (Brown Line)" : 40710,
            "Chicago (Red Line)" : 41450,
            "Cicero (Pink Line)" : 40420,
            "Cicero (Blue Line-Forest Park Branch)" : 40970,
            "Cicero (Green Line)" : 40480,
            "Clark/Division" : 40630,
            "Clark/Lake" : 40380,
            "Clinton (Blue Line)" : 40430,
            "Clinton (Green Line)" : 41160,
            "Conservatory" : 41670,
            "Cumberland" : 40230,
            "Damen (Brown Line)" : 40090,
            "Damen (Green Line)" : 41710,
            "Damen (Pink Line)" : 40210,
            "Damen (Blue Line-O'Hare Branch)" : 40590,
            "Davis" : 40050,
            "Dempster" : 40690,
            "Dempster-Skokie" : 40140,
            "Diversey" : 40530,
            "Division" : 40320,
            "Cottage Grove" : 40720,
            "Forest Park" : 40390,
            "Foster" : 40520,
            "Francisco" : 40870,
            "Fullerton" : 41220,
            "Garfield (Green Line)" : 40510,
            "Garfield (Red Line)" : 41170,
            "Grand (Blue Line)" : 40490,
            "Grand (Red Line)" : 40330,
            "Granville" : 40760,
            "Halsted (Green Line)" : 40940,
            "Halsted (Orange Line)" : 41130,
            "Harlem (Blue Line-Forest Park Branch)" : 40980,
            "Harlem (Green Line)" : 40020,
            "Harlem (Blue Line-O'Hare Branch)" : 40750,
            "Harold Washington Library-State/Van Buren" : 40850,
            "Harrison" : 41490,
            "Howard" : 40900,
            "Illinois Medical District" : 40810,
            "Indiana" : 40300,
            "Irving Park (Blue Line)" : 40550,
            "Irving Park (Brown Line)" : 41460,
            "Jackson (Blue Line)" : 40070,
            "Jackson (Red Line)" : 40560,
            "Jarvis" : 41190,
            "Jefferson Park" : 41280,
            "Kedzie (Brown Line)" : 41180,
            "Kedzie (Pink Line)" : 41040,
            "Kedzie (Green Line)" : 41070,
            "Kedzie-Homan (Blue Line)" : 40250,
            "Kedzie (Orange Line)" : 41150,
            "Kimball" : 41290,
            "King Drive" : 41140,
            "Kostner" : 40600,
            "Lake" : 41660,
            "Laramie" : 40700,
            "LaSalle" : 41340,
            "LaSalle/Van Buren" : 40160,
            "Lawrence" : 40770,
            "Linden" : 41050,
            "Logan Square" : 41020,
            "Loyola" : 41300,
            "Main" : 40270,
            "Midway" : 40930,
            "Monroe (Blue Line)" : 40790,
            "Monroe (Red Line)" : 41090,
            "Montrose (Blue Line)" : 41330,
            "Montrose (Brown Line)" : 41500,
            "Morgan" : 41510,
            "Morse" : 40100,
            "North/Clybourn" : 40650,
            "Noyes" : 40400,
            "Oak Park (Blue Line)" : 40180,
            "Oak Park (Green Line)" : 41350,
            "Oakton-Skokie" : 41680, 
            "O'Hare" : 40890,
            "Paulina" : 41310,
            "Polk" : 41030,
            "Pulaski (Pink Line)" : 40150,
            "Pulaski (Blue Line-Forest Park Branch)" : 40920,
            "Pulaski (Green Line)" : 40030,
            "Pulaski (Orange Line)" : 40960,
            "Quincy/Wells" : 40040,
            "Racine" : 40470,
            "Ridgeland" : 40610,
            "Rockwell" : 41010,
            "Roosevelt" : 41400,
            "Rosemont" : 40820,
            "Sedgwick" : 40800,
            "Sheridan" : 40080,
            "South Boulevard" : 40840,
            "Southport" : 40360,
            "Sox-35th" : 40190,
            "State/Lake" : 40260,
            "Thorndale" : 40880,
            "UIC-Halsted" : 40350,
            "Washington/Wabash" : 41700,
            "Washington/Wells" : 40730,
            "Washington (Blue Line)" : 40370,
            "Wellington" : 41210,
            "Western (Brown Line)" : 41480,
            "Western (Pink Line)" : 40740,
            "Western (Blue Line-Forest Park Branch)" : 40220,
            "Western (Blue Line-O'Hare Branch)" : 40670,
            "Western (Orange Line)" : 40310,
            "Wilson" : 40540
    }



    CONFIG_NAMES = ["HOME"]

    CONFIGS = {
        "HOME" : {
            "STATION" : "Division",
            "MAP_ID" : MAP_IDS["Division"],
            "ROUTE_DEST" : ["Forest Park", "UIC-Halsted"],
        }
    }


_inst = Config()
DEST_SHORT_NAMES = _inst.DEST_SHORT_NAMES
CONFIG_NAMES = _inst.CONFIG_NAMES
CONFIGS = _inst.CONFIGS
DISPLAY_WIDTH = _inst.DISPLAY_WIDTH
DISPLAY_HEIGHT = _inst.DISPLAY_HEIGHT
LETTER_WIDTH = _inst.LETTER_WIDTH
LETTER_HEIGHT = _inst.LETTER_HEIGHT
UPDATE_TIME = _inst.UPDATE_TIME