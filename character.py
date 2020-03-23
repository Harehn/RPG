class Character:
    def __init__(self):
        self.name = None
        self.nickname = None
        self.race = None
        self.age = None
        self.gender = None
        self.dob = None
        self.placeOfBirth = None
        self.occupation = None
        self.favouritePhrase = None
        self.shortDescription = None
        self.description = None
        self.easterEgg = None
        # Ethnicity:
        # Species:
        # -----------------------------
        self.height = None
        self.weight = None
        self.skintone = None
        self.facialShape = None
        self.eyeColour = None
        self.distinguishingFeature = None
        self.otherPhysicalFeatures = None
        self.hairstyle = None
        self.bodytype = None
        self.dress = None
        self.somethingAlwaysCarried = None
        self.tool = None
        self.accessories = None

    def __str__(self):
        toString=""
        for k, v in vars(self).items():
            #print((k if k else "None"), (v if v else "None"))
            toString += ( (k if k else "None") + ":" + (v if v else "None") + "\n")
        return toString



