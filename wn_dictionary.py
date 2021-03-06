"""
Handles the projection between words and classes in the dataset.
"""
wn_lexicon = {
    "Chalet": "<http://linkedgeodata.org/ontology/Chalet>",
    "Night Club": "<http://linkedgeodata.org/ontology/Nightclub>",
    "Preserved Railway": "<http://linkedgeodata.org/ontology/PreservedRailway>",
    "Terrace": "<http://linkedgeodata.org/ontology/Terrace>",
    "Miniature Golf": "<http://linkedgeodata.org/ontology/MiniatureGolf>",
    "Railway Station": "<http://linkedgeodata.org/ontology/TrainStation>",
    "Clinic": "<http://linkedgeodata.org/ontology/Clinic>",
    "Vending Machine": "<http://linkedgeodata.org/ontology/VendingMachine>",
    "Sports Pitch": "<http://linkedgeodata.org/ontology/Pitch>",
    "Allotments": "<http://linkedgeodata.org/ontology/Allotments>",
    "Ferry Terminal": "<http://linkedgeodata.org/ontology/FerryTerminal>",
    "Farm": "<http://linkedgeodata.org/ontology/Farm>",
    "Confectionery Shop": "<http://linkedgeodata.org/ontology/Confectionery>",
    "Raceway": "<http://linkedgeodata.org/ontology/Raceway>",
    "Motorway Services": "<http://linkedgeodata.org/ontology/ServiceStation>",
    "Hostel": "<http://linkedgeodata.org/ontology/Hostel>",
    "Grave Yard": "<http://linkedgeodata.org/ontology/GraveYard>",
    "Moor": "<http://linkedgeodata.org/ontology/Moor>",
    "Hunting Stand": "<http://linkedgeodata.org/ontology/HuntingStand>",
    "Food Shop": "<http://linkedgeodata.org/ontology/Food>",
    "Bureau de Change": "<http://linkedgeodata.org/ontology/BureauDeChange>",
    "School": "<http://linkedgeodata.org/ontology/School>",
    "Tertiary Road": "<http://linkedgeodata.org/ontology/TertiaryHighway>",
    "Islet": "<http://linkedgeodata.org/ontology/Islet>",
    "Vineyard": "<http://linkedgeodata.org/ontology/Vineyard>",
    "Car Shop": "<http://linkedgeodata.org/ontology/CarShop>",
    "Reef": "<http://linkedgeodata.org/ontology/Reef>",
    "Bay": "<http://linkedgeodata.org/ontology/Bay>",
    "Stream": "<http://linkedgeodata.org/ontology/Stream>",
    "Car Wash": "<http://linkedgeodata.org/ontology/CarWash>",
    "School Building": "<http://linkedgeodata.org/ontology/BuildingSchool>",
    "Laundry": "<http://linkedgeodata.org/ontology/Laundry>",
    "Pre-School": "<http://linkedgeodata.org/ontology/Preschool>",
    "Village Hall": "<http://linkedgeodata.org/ontology/VillageHall>",
    "Historic Railway Station": "<http://linkedgeodata.org/ontology/HistoricStation>",
    "Train Stop": "<http://linkedgeodata.org/ontology/RailwayHalt>",
    "Sports Shop": "<http://linkedgeodata.org/ontology/Sports>",
    "Suburb": "<http://linkedgeodata.org/ontology/Suburb>",
    "Retail Building": "<http://linkedgeodata.org/ontology/BuildingRetail>",
    "Pedestrian Way": "<http://linkedgeodata.org/ontology/PedestrianUse>",
    "Locality": "<http://linkedgeodata.org/ontology/Locality>",
    "Cycle Parking": "<http://linkedgeodata.org/ontology/BicycleParking>",
    "Running Track": "<http://linkedgeodata.org/ontology/Track>",
    "Viewpoint": "<http://linkedgeodata.org/ontology/Viewpoint>",
    "Subdivision": "<http://linkedgeodata.org/ontology/Subdivision>",
    "Hairdresser": "<http://linkedgeodata.org/ontology/HairdresserShop>",
    "River": "<http://linkedgeodata.org/ontology/NaturalRiver>",
    "Pet Shop": "<http://linkedgeodata.org/ontology/Pet>",
    "Electronics Shop": "<http://linkedgeodata.org/ontology/Electronics>",
    "Lock Gate": "<http://linkedgeodata.org/ontology/LockGate>",
    "Toilets": "<http://linkedgeodata.org/ontology/Toilets>",
    "Motorway Junction": "<http://linkedgeodata.org/ontology/MotorwayJunction>",
    "Unclassified Road": "<http://linkedgeodata.org/ontology/UnclassifiedHighway>",
    "Reservoir": "<http://linkedgeodata.org/ontology/Reservoir>",
    "Community Centre": "<http://linkedgeodata.org/ontology/CommunityCentre>",
    "Car Rental": "<http://linkedgeodata.org/ontology/CarRental>",
    "WiFi Access": "<http://linkedgeodata.org/ontology/Wifi>",
    "Hamlet": "<http://linkedgeodata.org/ontology/Hamlet>",
    "Railway Points": "<http://linkedgeodata.org/ontology/RailwaySwitch>",
    "Museum": "<http://linkedgeodata.org/ontology/Museum>",
    "Motorway Road": "<http://linkedgeodata.org/ontology/MotorwayLink>",
    "Greenfield Land": "<http://linkedgeodata.org/ontology/Greenfield>",
    "Feature": "<http://linkedgeodata.org/ontology/Feature>",
    "Steps": "<http://linkedgeodata.org/ontology/Steps>",
    "House": "<http://linkedgeodata.org/ontology/House>",
    "Recycling Point": "<http://linkedgeodata.org/ontology/RecyclingFacility>",
    "Outdoor Shop": "<http://linkedgeodata.org/ontology/Outdoor>",
    "Point": "<http://linkedgeodata.org/ontology/Point>",
    "Farmyard": "<http://linkedgeodata.org/ontology/Farmyard>",
    "Grocery Shop": "<http://linkedgeodata.org/ontology/Grocery>",
    "Estate Agent": "<http://linkedgeodata.org/ontology/EstateAgent>",
    "Brownfield Land": "<http://linkedgeodata.org/ontology/Brownfield>",
    "Trunk Road": "<http://linkedgeodata.org/ontology/TrunkLink>",
    "Fish Shop": "<http://linkedgeodata.org/ontology/Fish>",
    "Common Land": "<http://linkedgeodata.org/ontology/Common>",
    "Peak": "<http://linkedgeodata.org/ontology/Peak>",
    "Motel": "<http://linkedgeodata.org/ontology/Motel>",
    "Industrial Area": "<http://linkedgeodata.org/ontology/IndustrialLanduse>",
    "College": "<http://linkedgeodata.org/ontology/College>",
    "Canal": "<http://linkedgeodata.org/ontology/Canal>",
    "Memorial": "<http://linkedgeodata.org/ontology/Memorial>",
    "Nursing Home": "<http://linkedgeodata.org/ontology/NursingHome>",
    "Residential": "<http://linkedgeodata.org/ontology/ResidentialHighway>",
    "Supermarket": "<http://linkedgeodata.org/ontology/Supermarket>",
    "Club": "<http://linkedgeodata.org/ontology/Club>",
    "Municipality": "<http://linkedgeodata.org/ontology/Municipality>",
    "Prison": "<http://linkedgeodata.org/ontology/Prison>",
    "Light Rail": "<http://linkedgeodata.org/ontology/LightRail>",
    "Market": "<http://linkedgeodata.org/ontology/Market>",
    "Level Crossing": "<http://linkedgeodata.org/ontology/LevelCrossing>",
    "Social Club": "<http://linkedgeodata.org/ontology/SocialClub>",
    "Subway Station": "<http://linkedgeodata.org/ontology/Subway>",
    "Office": "<http://linkedgeodata.org/ontology/Office>",
    "Guided Bus Lane": "<http://linkedgeodata.org/ontology/BusGuideway>",
    "Farm Building": "<http://linkedgeodata.org/ontology/BuildingFarm>",
    "Restaurant": "<http://linkedgeodata.org/ontology/Restaurant>",
    "Hi-Fi": "<http://linkedgeodata.org/ontology/Hifi>",
    "Music Shop": "<http://linkedgeodata.org/ontology/Music>",
    "State": "<http://linkedgeodata.org/ontology/State>",
    "Ruins": "<http://linkedgeodata.org/ontology/Ruins>",
    "Water": "<http://linkedgeodata.org/ontology/Water>",
    "Subway Entrance": "<http://linkedgeodata.org/ontology/SubwayEntrance>",
    "Crematorium": "<http://linkedgeodata.org/ontology/Crematorium>",
    "Pub": "<http://linkedgeodata.org/ontology/Pub>",
    "Stadium": "<http://linkedgeodata.org/ontology/Stadium>",
    "Beach Resort": "<http://linkedgeodata.org/ontology/BeachResort>",
    "Mooring": "<http://linkedgeodata.org/ontology/Mooring>",
    "Beauty Shop": "<http://linkedgeodata.org/ontology/BeautyShop>",
    "Information": "<http://linkedgeodata.org/ontology/TourismInformation>",
    "Picnic Site": "<http://linkedgeodata.org/ontology/PicnicSite>",
    "Marsh": "<http://linkedgeodata.org/ontology/Marsh>",
    "Convenience Store": "<http://linkedgeodata.org/ontology/Convenience>",
    "Railway under Construction": "<http://linkedgeodata.org/ontology/RailwayConstruction>",
    "Embassy": "<http://linkedgeodata.org/ontology/Embassy>",
    "Carpet Shop": "<http://linkedgeodata.org/ontology/Carpet>",
    "Sports Centre": "<http://linkedgeodata.org/ontology/SportsCentre>",
    "Residential Area": "<http://linkedgeodata.org/ontology/ResidentialLanduse>",
    "Highway under Construction": "<http://linkedgeodata.org/ontology/HighwayConstruction>",
    "Emergency Access Point": "<http://linkedgeodata.org/ontology/EmergencyAccessPoint>",
    "Do-It-Yourself": "<http://linkedgeodata.org/ontology/Doityourself>",
    "Cliff": "<http://linkedgeodata.org/ontology/Cliff>",
    "Cafe": "<http://linkedgeodata.org/ontology/Cafe>",
    "Fishing Area": "<http://linkedgeodata.org/ontology/Fishing>",
    "Tramway": "<http://linkedgeodata.org/ontology/Tramway>",
    "Abandoned Railway": "<http://linkedgeodata.org/ontology/AbandonedRailway>",
    "Fell": "<http://linkedgeodata.org/ontology/Fell>",
    "Youth Centre": "<http://linkedgeodata.org/ontology/YouthCentre>",
    "Swimming Pool": "<http://linkedgeodata.org/ontology/SwimmingPool>",
    "Bus Station": "<http://linkedgeodata.org/ontology/BusStation>",
    "Boatyard": "<http://linkedgeodata.org/ontology/Boatyard>",
    "Insurance": "<http://linkedgeodata.org/ontology/Insurance>",
    "Guest House": "<http://linkedgeodata.org/ontology/GuestHouse>",
    "Fountain": "<http://linkedgeodata.org/ontology/Fountain>",
    "Video Shop": "<http://linkedgeodata.org/ontology/Video>",
    "Cave Entrance": "<http://linkedgeodata.org/ontology/CaveEntrance>",
    "Village Green": "<http://linkedgeodata.org/ontology/VillageGreen>",
    "Byway": "<http://linkedgeodata.org/ontology/Byway>",
    "Glacier": "<http://linkedgeodata.org/ontology/Glacier>",
    "Cape": "<http://linkedgeodata.org/ontology/Cape>",
    "Strait": "<http://linkedgeodata.org/ontology/Strait>",
    "Brothel": "<http://linkedgeodata.org/ontology/Brothel>",
    "Health Centre": "<http://linkedgeodata.org/ontology/HealthCentre>",
    "Golf Course": "<http://linkedgeodata.org/ontology/GolfCourse>",
    "Off License": "<http://linkedgeodata.org/ontology/AlcoholShop>",
    "Icon": "<http://linkedgeodata.org/ontology/Icon>",
    "Bridleway": "<http://linkedgeodata.org/ontology/Bridleway>",
    "Studio": "<http://linkedgeodata.org/ontology/Studio>",
    "Lock": "<http://linkedgeodata.org/ontology/WaterwayLock>",
    "Fast Food": "<http://linkedgeodata.org/ontology/FastFood>",
    "Coastline": "<http://linkedgeodata.org/ontology/Coastline>",
    "Ford": "<http://linkedgeodata.org/ontology/HighwayFord>",
    "Organic Food Shop": "<http://linkedgeodata.org/ontology/Organic>",
    "Airport": "<http://linkedgeodata.org/ontology/Airport>",
    "Waste Basket": "<http://linkedgeodata.org/ontology/WasteBasket>",
    "Path": "<http://linkedgeodata.org/ontology/Path>",
    "Fjord": "<http://linkedgeodata.org/ontology/Fjord>",
    "Mud": "<http://linkedgeodata.org/ontology/Mud>",
    "Crater": "<http://linkedgeodata.org/ontology/Crater>",
    "Clothes Shop": "<http://linkedgeodata.org/ontology/Clothes>",
    "Ridge": "<http://linkedgeodata.org/ontology/Ridge>",
    "Public Telephone": "<http://linkedgeodata.org/ontology/Telephone>",
    "Disused Railway Station": "<http://linkedgeodata.org/ontology/DisusedStation>",
    "Motorway": "<http://linkedgeodata.org/ontology/Motorway>",
    "Fitness Centre / Gym": "<http://linkedgeodata.org/ontology/Gym>",
    "Artwork": "<http://linkedgeodata.org/ontology/Artwork>",
    "Commercial Building": "<http://linkedgeodata.org/ontology/BuildingCommercial>",
    "Valley": "<http://linkedgeodata.org/ontology/NaturalValley>",
    "Track": "<http://linkedgeodata.org/ontology/Track>",
    "Fire Hydrant": "<http://linkedgeodata.org/ontology/FireHydrant>",
    "University Building": "<http://linkedgeodata.org/ontology/BuildingUniversity>",
    "Cinema": "<http://linkedgeodata.org/ontology/Cinema>",
    "Manor": "<http://linkedgeodata.org/ontology/Manor>",
    "Monument": "<http://linkedgeodata.org/ontology/Monument>",
    "Quarry": "<http://linkedgeodata.org/ontology/Quarry>",
    "Park": "<http://linkedgeodata.org/ontology/Park>",
    "Rock": "<http://linkedgeodata.org/ontology/NaturalRock>",
    "Attraction": "<http://linkedgeodata.org/ontology/Attraction>",
    "Bicycle Shop": "<http://linkedgeodata.org/ontology/BicycleShop>",
    "Service Road": "<http://linkedgeodata.org/ontology/HighwayService>",
    "Forest": "<http://linkedgeodata.org/ontology/Forest>",
    "Primary Road": "<http://linkedgeodata.org/ontology/HighwayPrimaryLink>",
    "Driving School": "<http://linkedgeodata.org/ontology/DrivingSchool>",
    "Garden Centre": "<http://linkedgeodata.org/ontology/GardenCentre>",
    "Optician": "<http://linkedgeodata.org/ontology/OpticianShop>",
    "Car Repair": "<http://linkedgeodata.org/ontology/CarRepairShop>",
    "Geyser": "<http://linkedgeodata.org/ontology/Geyser>",
    "Dam": "<http://linkedgeodata.org/ontology/Dam>",
    "Newsagent": "<http://linkedgeodata.org/ontology/Newsagent>",
    "Dry Cleaning": "<http://linkedgeodata.org/ontology/DryCleaning>",
    "Military Area": "<http://linkedgeodata.org/ontology/MilitaryLanduse>",
    "Mineral Spring": "<http://linkedgeodata.org/ontology/MineralSpring>",
    "Playground": "<http://linkedgeodata.org/ontology/Playground>",
    "Car Parts": "<http://linkedgeodata.org/ontology/CarParts>",
    "Marketplace": "<http://linkedgeodata.org/ontology/Marketplace>",
    "Building": "<http://linkedgeodata.org/ontology/HistoricBuilding>",
    "Department Store": "<http://linkedgeodata.org/ontology/DepartmentStore>",
    "Discount Items Shop": "<http://linkedgeodata.org/ontology/Discount>",
    "Commercial Area": "<http://linkedgeodata.org/ontology/CommercialLanduse>",
    "Public Market": "<http://linkedgeodata.org/ontology/PublicMarket>",
    "Railway Platform": "<http://linkedgeodata.org/ontology/RailwayPlatform>",
    "Alpine Hut": "<http://linkedgeodata.org/ontology/AlpineHut>",
    "Island": "<http://linkedgeodata.org/ontology/Island>",
    "Scrub": "<http://linkedgeodata.org/ontology/Scrub>",
    "Construction": "<http://linkedgeodata.org/ontology/ConstructionLanduse>",
    "Railway": "<http://linkedgeodata.org/ontology/RailwayLanduse>",
    "Channel": "<http://linkedgeodata.org/ontology/Channel>",
    "Tree": "<http://linkedgeodata.org/ontology/Tree>",
    "Kiosk Shop": "<http://linkedgeodata.org/ontology/Kiosk>",
    "Bench": "<http://linkedgeodata.org/ontology/Bench>",
    "Computer Shop": "<http://linkedgeodata.org/ontology/Computer>",
    "Hotel": "<http://linkedgeodata.org/ontology/Hotel>",
    "Bakery": "<http://linkedgeodata.org/ontology/Bakery>",
    "Railway Junction": "<http://linkedgeodata.org/ontology/RailwayJunction>",
    "Farm Shop": "<http://linkedgeodata.org/ontology/FarmShop>",
    "Ice Cream": "<http://linkedgeodata.org/ontology/IceCream>",
    "Marina": "<http://linkedgeodata.org/ontology/Marina>",
    "Residential Building": "<http://linkedgeodata.org/ontology/BuildingResidential>",
    "Bunker": "<http://linkedgeodata.org/ontology/BuildingBunker>",
    "Dentist": "<http://linkedgeodata.org/ontology/Dentist>",
    "Apparel Shop": "<http://linkedgeodata.org/ontology/Apparel>",
    "Land": "<http://linkedgeodata.org/ontology/Land>",
    "Spring": "<http://linkedgeodata.org/ontology/Spring>",
    "Retirement Home": "<http://linkedgeodata.org/ontology/RetirementHome>",
    "Scree": "<http://linkedgeodata.org/ontology/Scree>",
    "Drugstore": "<http://linkedgeodata.org/ontology/Drugstore>",
    "Wetland": "<http://linkedgeodata.org/ontology/Wetland>",
    "Living Street": "<http://linkedgeodata.org/ontology/LivingStreet>",
    "Shoe Shop": "<http://linkedgeodata.org/ontology/Shoes>",
    "Fire Station": "<http://linkedgeodata.org/ontology/FireStation>",
    "Garage": "<http://linkedgeodata.org/ontology/BuildingGarage>",
    "Caravan Site": "<http://linkedgeodata.org/ontology/CaravanSite>",
    "Cycle Path": "<http://linkedgeodata.org/ontology/Cycleway>",
    "Copy Shop": "<http://linkedgeodata.org/ontology/Copyshop>",
    "Charity Shop": "<http://linkedgeodata.org/ontology/CharityShop>",
    "Meadow": "<http://linkedgeodata.org/ontology/Meadow>",
    "Fashion Shop": "<http://linkedgeodata.org/ontology/Fashion>",
    "Bar": "<http://linkedgeodata.org/ontology/Bar>",
    "Chemist": "<http://linkedgeodata.org/ontology/Chemist>",
    "Hardware Store": "<http://linkedgeodata.org/ontology/Hardware>",
    "Hall": "<http://linkedgeodata.org/ontology/BuildingHall>",
    "Florist": "<http://linkedgeodata.org/ontology/FloristShop>",
    "Doctors": "<http://linkedgeodata.org/ontology/Doctors>",
    "Wood": "<http://linkedgeodata.org/ontology/LanduseWood>",
    "Taxi": "<http://linkedgeodata.org/ontology/Taxi>",
    "Post Office": "<http://linkedgeodata.org/ontology/PostOffice>",
    "Mall": "<http://linkedgeodata.org/ontology/Mall>",
    "Hill": "<http://linkedgeodata.org/ontology/Hill>",
    "Cycle Rental": "<http://linkedgeodata.org/ontology/BicycleRental>",
    "Funeral Directors": "<http://linkedgeodata.org/ontology/FuneralDirectors>",
    "Arts Centre": "<http://linkedgeodata.org/ontology/ArtsCentre>",
    "Jewelry Shop": "<http://linkedgeodata.org/ontology/Jewelry>",
    "Dormitory": "<http://linkedgeodata.org/ontology/BuildingDormitory>",
    "Tower": "<http://linkedgeodata.org/ontology/HistoricTower>",
    "Fuel": "<http://linkedgeodata.org/ontology/FuelStation>",
    "Garden": "<http://linkedgeodata.org/ontology/Garden>",
    "Farmland": "<http://linkedgeodata.org/ontology/Farmland>",
    "Theatre": "<http://linkedgeodata.org/ontology/Theatre>",
    "Region": "<http://linkedgeodata.org/ontology/Region>",
    "Water Point": "<http://linkedgeodata.org/ontology/WaterPoint>",
    "Building Entrance": "<http://linkedgeodata.org/ontology/BuildingEntrance>",
    "Pharmacy": "<http://linkedgeodata.org/ontology/Pharmacy>",
    "Slipway": "<http://linkedgeodata.org/ontology/Slipway>",
    "Hospital Building": "<http://linkedgeodata.org/ontology/BuildingHospital>",
    "Church": "<http://linkedgeodata.org/ontology/HistoricChurch>",
    "Waterfall": "<http://linkedgeodata.org/ontology/Waterfall>",
    "Weir": "<http://linkedgeodata.org/ontology/Weir>",
    "Emergency Phone": "<http://linkedgeodata.org/ontology/EmergencyPhone>",
    "Casino": "<http://linkedgeodata.org/ontology/Casino>",
    "Town": "<http://linkedgeodata.org/ontology/Town>",
    "Monorail": "<http://linkedgeodata.org/ontology/Monorail>",
    "Gift Shop": "<http://linkedgeodata.org/ontology/Gift>",
    "Ditch": "<http://linkedgeodata.org/ontology/Ditch>",
    "Landfill": "<http://linkedgeodata.org/ontology/Landfill>",
    "County": "<http://linkedgeodata.org/ontology/County>",
    "Water Park": "<http://linkedgeodata.org/ontology/WaterPark>",
    "Art Shop": "<http://linkedgeodata.org/ontology/ArtShop>",
    "Book Shop": "<http://linkedgeodata.org/ontology/BookShop>",
    "Riverbank": "<http://linkedgeodata.org/ontology/Riverbank>",
    "University": "<http://linkedgeodata.org/ontology/University>",
    "Village": "<http://linkedgeodata.org/ontology/Village>",
    "Parking": "<http://linkedgeodata.org/ontology/Parking>",
    "Archaeological Site": "<http://linkedgeodata.org/ontology/ArchaeologicalSite>",
    "Drain": "<http://linkedgeodata.org/ontology/Drain>",
    "Theme Park": "<http://linkedgeodata.org/ontology/ThemePark>",
    "Shopping Centre": "<http://linkedgeodata.org/ontology/ShoppingCentre>",
    "Volcano": "<http://linkedgeodata.org/ontology/Volcano>",
    "Salon": "<http://linkedgeodata.org/ontology/Salon>",
    "Dock": "<http://linkedgeodata.org/ontology/Dock>",
    "Chapel": "<http://linkedgeodata.org/ontology/BuildingChapel>",
    "Cemetery": "<http://linkedgeodata.org/ontology/Cemetery>",
    "Greengrocer": "<http://linkedgeodata.org/ontology/Greengrocer>",
    "Heath": "<http://linkedgeodata.org/ontology/Heath>",
    "Disused Railway": "<http://linkedgeodata.org/ontology/DisusedRailway>",
    "Nursery": "<http://linkedgeodata.org/ontology/Nursery>",
    "Reception Area": "<http://linkedgeodata.org/ontology/ReceptionArea>",
    "Beach": "<http://linkedgeodata.org/ontology/Beach>",
    "Shelter": "<http://linkedgeodata.org/ontology/Shelter>",
    "Rapids": "<http://linkedgeodata.org/ontology/Rapids>",
    "Nature Reserve": "<http://linkedgeodata.org/ontology/NatureReserve>",
    "Basin": "<http://linkedgeodata.org/ontology/Basin>",
    "Gallery": "<http://linkedgeodata.org/ontology/GalleryShop>",
    "Narrow Gauge Railway": "<http://linkedgeodata.org/ontology/NarrowGauge>",
    "Veterinary Surgery": "<http://linkedgeodata.org/ontology/Veterinary>",
    "Ice Rink": "<http://linkedgeodata.org/ontology/IceRink>",
    "Library": "<http://linkedgeodata.org/ontology/Library>",
    "Kindergarten": "<http://linkedgeodata.org/ontology/Kindergarten>",
    "Recreation Ground": "<http://linkedgeodata.org/ontology/RecreationGround>",
    "Drinking Water": "<http://linkedgeodata.org/ontology/DrinkingWater>",
    "Photo Shop": "<http://linkedgeodata.org/ontology/Photo>",
    "Castle": "<http://linkedgeodata.org/ontology/Castle>",
    "Tram Stop": "<http://linkedgeodata.org/ontology/TramStop>",
    "Motorcycle Shop": "<http://linkedgeodata.org/ontology/Motorcycle>",
    "Sauna": "<http://linkedgeodata.org/ontology/Sauna>",
    "Apartment Block": "<http://linkedgeodata.org/ontology/ApartmentBuilding>",
    "Camp Site": "<http://linkedgeodata.org/ontology/CampSite>",
    "Town Hall": "<http://linkedgeodata.org/ontology/Townhall>",
    "Travel Agency": "<http://linkedgeodata.org/ontology/TravelAgency>",
    "Bus Stop": "<http://linkedgeodata.org/ontology/BusStop>",
    "Bank": "<http://linkedgeodata.org/ontology/Bank>",
    "Funicular Railway": "<http://linkedgeodata.org/ontology/FunicularRailway>",
    "Car Sharing": "<http://linkedgeodata.org/ontology/CarSharing>",
    "Courthouse": "<http://linkedgeodata.org/ontology/Courthouse>",
    "Public Building": "<http://linkedgeodata.org/ontology/PublicBuilding>",
    "Place of Worship": "<http://linkedgeodata.org/ontology/PlaceOfWorship>",
    "Car Dealer": "<http://linkedgeodata.org/ontology/CarDealer>",
    "Mine": "<http://linkedgeodata.org/ontology/LanduseMine>",
    "Cosmetics Shop": "<http://linkedgeodata.org/ontology/Cosmetics>",
    "Administrative Boundary": "<http://linkedgeodata.org/ontology/AdministrativeBoundary>",
    "Hospital": "<http://linkedgeodata.org/ontology/Hospital>",
    "Stationery Shop": "<http://linkedgeodata.org/ontology/Stationery>",
    "Grass": "<http://linkedgeodata.org/ontology/GrassLanduse>",
    "General Store": "<http://linkedgeodata.org/ontology/General>",
    "Butcher": "<http://linkedgeodata.org/ontology/Butcher>",
    "Furniture": "<http://linkedgeodata.org/ontology/Furniture>",
    "Mountain Rescue": "<http://linkedgeodata.org/ontology/MountainRescue>",
    "Footpath": "<http://linkedgeodata.org/ontology/Footway>",
    "Police": "<http://linkedgeodata.org/ontology/Police>",
    "Beverages Shop": "<http://linkedgeodata.org/ontology/BeverageMarket>",
    "Flats": "<http://linkedgeodata.org/ontology/Flats>",
    "Toy Shop": "<http://linkedgeodata.org/ontology/Toys>",
    "Country": "<http://linkedgeodata.org/ontology/Country>",
    "Shopping": "<http://linkedgeodata.org/ontology/Shopping>",
    "City": "<http://linkedgeodata.org/ontology/City>",
    "Shop": "<http://linkedgeodata.org/ontology/Shop>",
    "ATM": "<http://linkedgeodata.org/ontology/Atm>",
    "Post Box": "<http://linkedgeodata.org/ontology/PostBox>",
    "Bed and Breakfast": "<http://linkedgeodata.org/ontology/BedAndBreakfast>",
    "Zoo": "<http://linkedgeodata.org/ontology/Zoo>",
    "Office Building": "<http://linkedgeodata.org/ontology/BuildingOffice>",
    "Retail": "<http://linkedgeodata.org/ontology/RetailLanduse>",
    "Shoal": "<http://linkedgeodata.org/ontology/Shoal>",
    "Road": "<http://linkedgeodata.org/ontology/Road>",
    "Mobile Phone Shop": "<http://linkedgeodata.org/ontology/MobilePhone>",
}
