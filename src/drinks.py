# drinks.py

ML = 1      # 1ml = 1g
CL = 10     # 1cl = 10g

# syrup
MLs = 1.4   # 1ml = 1.4g
CLs = 14   # 1cl = 14g

# "NAME":("NICENAME", ISWITHALCOHOL)
ingredients = {
    "vodka": ("Wodka", True),
    "rum": ("Rum", True),
    "peach": ("Creme de Peche", True),
    "cachaca": ("Cachaca", True),
    "apricot": ("Arpicot Brandy", True),

    "porno": ("Porno", True),

    "grenadine": ("Grenadinensirup", False),
    "orange": ("Orangensaft", False),
    "lemon": ("Zitronensaft", False),
    "pineapple": ("Ananassaft", False),
    "maracuja": ("Maracujasaft", False),
    "soda": ("Soda", False),

}


drink_list = [
    {
        "name": "Touch Down Big",
        "recipe": [
            ("vodka", 6*CL),
            ("apricot", 3*CL),
            ("grenadine", 1.5*CLs),
            ("lemon", 3*CL),
            ("maracuja", 22.5*CL)
        ]
    },
    {
        "name": "Touch Down Light",
        "recipe": [
            ("vodka", 4 * CL),
            ("apricot", 2 * CL),
            ("grenadine", 1 * CLs),
            ("lemon", 2 * CL),
            ("maracuja", 15 * CL)
        ]
    },
    {
        "name": "Planter's Wonder",
        "recipe": [
            ("grenadine", 2*CLs),
            ("lemon", 2*CL),
            ("pineapple", 6*CL),
            ("orange", 6*CL),
            ("maracuja", 6*CL)
        ]
    }, {
        "name": "Wodka Twist",
        "recipe": [
            ("vodka", 4*CL),
            ("lemon", 2*CL),
            ("grenadine", 1*CLs),
        ]
    }, {
        "name": "Hawaii Cool",
        "recipe": [
            ("rum", 8*CL),
            ("pineapple", 10*CL),
            ("grenadine", 4*CLs),
        ]
    }, {
        "name": "Lucky Driver",
        "recipe": [
            ("orange", 10*CL),
            ("maracuja", 6*CL),
            ("lemon", 2*CL),
            ("grenadine", 1.5*CLs),
        ]
    }, {
        "name": "The Beach",
        "recipe": [
            ("vodka", 4*CL),
            ("peach", 3*CL),
            ("lemon", 1*CLs),
            ("orange", 4*CL),
            ("grenadine", 1.5*CLs),
            ("maracuja", 14*CL),
        ]
    }, {
        "name": "Peach Sling Light",
        "recipe": [
            ("vodka", 2*CL),
            ("peach", 2*CL),
            ("pineapple", 8*CL),
            ("orange", 8*CL),
        ]
    }, {
        "name": "911 Targa",
        "recipe": [
            ("orange", 6*CL),
            ("pineapple", 3*CL),
            ("lemon", 3*CL),
            ("grenadine", 3*CLs),
            ("maracuja", 6*CL),
        ]
    }, {
        "name": "Havana Sail",
        "recipe": [
            ("rum", 4*CL),
            ("grenadine", 2*CLs),
            ("maracuja", 8*CL),
        ]
    }, {
        "name": "Nordic Summer",
        "recipe": [
            ("vodka", 4*CL),
            ("maracuja", 4*CL),
            ("lemon", 1*CL),
            ("orange", 8*CL),
            ("grenadine", 0.5*CLs),
        ]
    }, {
        "name": "Grenadine Shake",
        "recipe": [
            ("lemon", 2*CL),
            ("pineapple", 2*CL),
            ("grenadine", 2*CLs),
            ("soda", 4*CL),
        ]
    }, {
        "name": "Tropical Sunshine",
        "recipe": [
            ("vodka", 2*CL),
            ("maracuja", 6*CL),
            ("orange", 6*CL),
            ("grenadine", 0.2 * CLs),
        ]
    }, {
        "name": "Wodka Maracuja",
        "recipe": [
            ("vodka", 4*CL),
            ("maracuja", 12*CL),
        ]
    }, {
        "name": "Wodka Sunrise",
        "recipe": [
            ("vodka", 4*CL),
            ("orange", 12*CL),
            ("lemon", 1*CL),
            ("grenadine", 1*CLs)
        ]
    }, {
        "name": "Waikiki",
        "recipe": [
            ("vodka", 4*CL),
            ("pineapple", 12*CL),
        ]
    }, {
        "name": "Finlady",
        "recipe": [
            ("vodka", 4*CL),
            ("apricot", 2*CL),
            ("lemon", 1*CL),
        ]
    }, {
        "name": "Sixteen",
        "recipe": [
            ("grenadine", 2*CLs),
            ("lemon", 2*CL),
            ("pineapple", 4*CL),
            ("orange", 8*CL),
            ("maracuja", 2*CL),
        ]
    }, {
        "name": "Bora Bora",
        "recipe": [
            ("grenadine", 1*CLs),
            ("lemon", 1*CL),
            ("pineapple", 10*CL),
            ("maracuja", 6*CL),
        ]
    }, {
        "name": "Ananasia",
        "recipe": [
            ("vodka", 2*CL),
            ("peach", 3*CL),
            ("pineapple", 2*CL),
        ]
    }, {
        "name": "Golden Girl",
        "recipe": [
            ("vodka", 2*CL),
            ("apricot", 3*CL),
            ("orange", 6*CL),
        ]
    }, {
        "name": "Screwdriver",
        "recipe": [
            ("vodka", 5*CL),
            ("orange", 10*CL),
        ]
    }, {
        "name": "Apricot Fizz",
        "recipe": [
            ("apricot", 4*CL),
            ("lemon", 2*CL),
            ("orange", 4*CL),
            ("soda", 8*CL),
        ]
    }, {
        "name": "Red One",
        "recipe": [
            ("grenadine", 1*CLs),
            ("lemon", 1*CL),
            ("pineapple", 5*CL),
            ("orange", 5*CL),
        ]
    }, {
        "name": "Los Angeles",
        "recipe": [
            ("vodka", 4*CL),
            ("grenadine", 2*CLs),
            ("lemon", 5*CL),
            ("pineapple", 2*CL),
            ("orange", 9*CL),
            ("maracuja", 2*CL),
        ]
    }, {
        "name": "Upton",
        "recipe": [
            ("rum", 2*CL),
            ("lemon", 1*CL),
            ("pineapple", 2*CL),
            ("orange", 1*CL),
        ]
    }, {
        "name": "National",
        "recipe": [
            ("rum", 3*CL),
            ("apricot", 1*CL),
            ("pineapple", 2*CL),
        ]
    }, {
        "name": "Brasilian Sunrise",
        "recipe": [
            ("cachaca", 4*CL),
            ("grenadine", 2*CLs),
            ("lemon", 1*CL),
            ("orange", 10*CL),
        ]
    }
]


def check_drinks():
    keys = ingredients.keys()
    for d in drink_list:
        for r in d["recipe"]:
            if r[0] not in keys:
                print("ERROR in %s: %s" % (d["name"], r[0]))
