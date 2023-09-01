# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:31:41 2023

@author: forrest
"""

import re

company_regexes = {
    "3M": r"(?im)(\b3M\b)",
    "AB InBev (CCD)": r"(?im)(\bAB InBev|CCD\b)",
    "Abbott": r"(?im)(\bAbbott\b)",
    "Abbvie": r"(?im)(\bAbbvie\b)",
    "ABI": r"(?im)(\bABI\b)",
    "Adidas": r"(?im)(\bAdidas\b)",
    "Ahold Delhaize": r"(?im)(\bAhold Delhaize\b)",
    "AIG": r"(?im)(\bAIG\b)",
    "Airbnb": r"(?im)(\bAirbnb\b)",
    "Albertsons": r"(?im)(\bAlbertsons\b)",
    "Aldi": r"(?im)(\bAldi\b)",
    "AllBirds": r"(?im)(\bAllBirds\b)",
    "Allstate": r"(?im)(\bAllstate\b)",
    "Altria (BRS + Avail)": r"(?im)(\bAltria\b)",
    "Altria (Avail)": r"(?im)(\b((Altria)\W+(?:\w+\W+){0,9}?(Avail))|((Avail)\W+(?:\w+\W+){0,9}?(Altria))\b)",
    "Amazon": r"(?im)(\bAmazon\b)",
    "Amazon Whole Foods": r"(?im)(\bWhole Foods\b)",
    "AMERICA MOVIL": r"(?im)(\bAMERICA MOVIL\b)",
    "American Alliance of Museums": r"(?im)(\bAmerican Alliance of Museums\b)",
    "American Express": r"(?im)(\bAmerican Express\b)",
    "AmGen": r"(?im)(\bAmGen\b)",
    "Antenna Group": r"(?im)(\bAntenna Group\b)",
    "Anthem": r"(?im)(\bAnthem\b)",
    "Apple": r"(?im)(\bApple\b)",
    "Applied Research and Analysis Consulting": r"(?im)(\bApplied Research and Analysis Consulting\b)",
    "Appvion": r"(?im)(\bAppvion\b)",
    "Archer Daniels Midland": r"(?im)(\bArcher Daniels Midland\b)",
    "Aristocrat Gaming": r"(?im)(\bAristocrat Gaming\b)",
    "Arla Food": r"(?im)(\bArla Food\b)",
    "AstraZeneca": r"(?im)(\bAstraZeneca\b)",
    "ASURION LLC": r"(?im)(\bASURION LLC\b)",
    "AT and T": r"(?im)(\bAT\&T\b)",
    "Ateeco": r"(?im)(\bAteeco\b)",
    "Autodesk": r"(?im)(\bAutodesk\b)",
    "Bacardi": r"(?im)(\bBacardi\b)",
    "Bally Sports": r"(?im)(\bBally Sports\b)",
    "Bank of America": r"(?im)(\bBank of America\b)",
    "Bayer": r"(?im)(\bBayer\b)",
    "Becton, Dickinson and Co.": r"(?im)(\bBecton\, Dickinson \& Co\.\b)",
    "BYTEDANCE": r"(?im)(\bBYTEDANCE\b)",
    "CALERES": r"(?im)(\bCALERES\b)",
    "Campari USA": r"(?im)(\bCampari USA\b)",
    "CAMPBELL SOUP": r"(?im)(\bCAMPBELL SOUP\b)",
    "CAPITAL ONE FINANCIAL": r"(?im)(\bCAPITAL ONE FINANCIAL\b)",
    "Cardinal Health": r"(?im)(\bCardinal Health\b)",
    "Cargill": r"(?im)(\bCargill\b)",
    "Carnival Cruise Lines": r"(?im)(\bCarnival Cruise Lines|Carnival\b)",
    "CASEY'S": r"(?im)(\bCASEY\'S\b)",
    "Cash App": r"(?im)(\bCash App\b)",
    "Caterpillar": r"(?im)(\bCaterpillar\b)",
    "CDC": r"(?im)(\bCDC\b)",
    "Celerion": r"(?im)(\bCelerion\b)",
    "Celestial Hain": r"(?im)(\bCelestial Hain\b)",
    "Centene": r"(?im)(\bCentene\b)",
    "Centre for Substance Use Regulation": r"(?im)(\bCentre for Substance Use Regulation\b)",
    "Charles Schwab": r"(?im)(\bCharles Schwab\b)",
    "Cheerain HK Limited": r"(?im)(\bCheerain HK Limited\b)",
    "CHEVRON": r"(?im)(\bCHEVRON\b)",
    "Chow Now": r"(?im)(\bChow Now\b)",
    "CHS": r"(?im)(\bCHS\b)",
    "Church and Dwight": r"(?im)(\bChurch \& Dwight\b)",
    "CIRCLE K CONVENIENCE STORES": r"(?im)(\bCIRCLE K CONVENIENCE STORES|Circle K\b)",
    "Cisco": r"(?im)(\bCisco\b)",
    "CITIGROUP": r"(?im)(\bCITIGROUP\b)",
    "CITIZENS BANK": r"(?im)(\bCITIZENS BANK\b)",
    "CKE Restaurants": r"(?im)(\bCKE Restaurants\b)",
    "Clorox": r"(?im)(\bClorox\b)",
    "COCA COLA": r"(?im)(\bCOCA\-COLA\b)",
    "Colgate": r"(?im)(\bColgate\b)",
    "COMCAST NBC UNIVERSAL": r"(?im)(\bCOMCAST NBC UNIVERSAL\b)",
    "Compassion International": r"(?im)(\bCompassion International\b)",
    "Con Edison": r"(?im)(\bCon Edison\b)",
    "ConAgra": r"(?im)(\bConAgra\b)",
    "Conair/Cuisinart": r"(?im)(\bConair/Cuisinart\b)",
    "ConocoPhillips": r"(?im)(\bConocoPhillips\b)",
    "CONSTELLATION BRANDS": r"(?im)(\bCONSTELLATION BRANDS\b)",
    "Consumer Cellular": r"(?im)(\bConsumer Cellular\b)",
    "Convoy": r"(?im)(\bConvoy\b)",
    "Costco": r"(?im)(\bCostco\b)",
    "Coterie": r"(?im)(\bCoterie\b)",
    "COTY": r"(?im)(\bCOTY\b)",
    "COUCHE TARD": r"(?im)(\bCOUCHE TARD\b)",
    "COX CABLE": r"(?im)(\bCOX CABLE\b)",
    "Cracker Barrel": r"(?im)(\bCracker Barrel\b)",
    "CVS": r"(?im)(\bCVS\b)",
    "Daimler AG": r"(?im)(\bDaimler AG\b)",
    "DANONE": r"(?im)(\bDANONE\b)",
    "DARDEN RESTAURANTS": r"(?im)(\bDARDEN RESTAURANTS\b)",
    "Deckers": r"(?im)(\bDeckers\b)",
    "Delaware North": r"(?im)(\bDelaware North\b)",
    "DELL": r"(?im)(\bDELL\b)",
    "Delta Airlines": r"(?im)(\bDelta Airlines\b)",
    "Demonstrate": r"(?im)(\bDemonstrate\b)",
    "DEPT. OF VETERANS AFFAIRS": r"(?im)(\bDEPT\. OF VETERANS AFFAIRS|Department of veteran\S* affairs|DEPT\ OF VETERANS AFFAIRS\b)",
    "Deutsch Telecom (TMO)": r"(?im)(\bDeutsch Telecom\b)",
    "DevaCurl": r"(?im)(\bDevaCurl\b)",
    "DIAGEO": r"(?im)(\bDIAGEO\b)",
    "DINE Brands/Applebee's": r"(?im)(\bDINE Brands|Applebee\'s\b)",
    "DOD": r"(?im)(\bDOD\b)",
    "DOD": r"(?im)(\b((DOD)\W+(?:\w+\W+){0,9}?(FORSMARSH))|((FORSMARSH)\W+(?:\w+\W+){0,9}?(DOD))\b)",
    "Domino's Pizza": r"(?im)(\bDomino\'s Pizza|Dominos\b)",
    "Doordash": r"(?im)(\bDoordash\b)",
    "DOT": r"(?im)(\bDOT\b)",
    "Dow Chemical Company": r"(?im)(\bDow Chemical Company|DOW\b)",
    "Dr Pepper Snapple": r"(?im)(\bDr Pepper|Snapple|Dr pepper snapple|dr\S* pepper snapple\b)",
    "Droga5": r"(?im)(\bDroga5\b)",
    "Duck Duck Go": r"(?im)(\bDuck Duck Go\b)",
    "E and J GALLO WINERY": r"(?im)(\bE \& J GALLO WINERY\b)",
    "e.l.f. Cosmetics": r"(?im)(\be\.l\.f\. Cosmetics\b)",
    "EDGEWELL": r"(?im)(\bEDGEWELL\b)",
    "Edward Jones": r"(?im)(\bEdward Jones\b)",
    "Ekaterra": r"(?im)(\bEkaterra\b)",
    "Elevance Health": r"(?im)(\bElevance Health\b)",
    "ELI LILLY": r"(?im)(\bELI LILLY\b)",
    "Energy Transfer Partners": r"(?im)(\bEnergy Transfer Partners\b)",
    "Enterprise Products": r"(?im)(\bEnterprise Products\b)",
    "ESTEE LAUDER COS": r"(?im)(\bESTEE LAUDER COS\b)",
    "Eventbrite": r"(?im)(\bEventbrite\b)",
    "EW Scripps": r"(?im)(\bEW Scripps\b)",
    "Exelon": r"(?im)(\bExelon\b)",
    "Expedia": r"(?im)(\bExpedia\b)",
    "ExxonMobil": r"(?im)(\bExxonMobil|Exxon\b)",
    "Farmer's Insurance": r"(?im)(\bFarmer\'s Insurance\b)",
    "Fastenal": r"(?im)(\bFastenal\b)",
    "FCA GROUP (FIAT/CHRYSLER GROUP)": r"(?im)(\bFCA GROUP|FIAT\/CHRYSLER GROUP\b)",
    "FEDERAL RESERVE": r"(?im)(\bFEDERAL RESERVE\b)",
    "FEDEX": r"(?im)(\bFEDEX\b)",
    "FERRERO": r"(?im)(\bFERRERO\b)",
    "First Horizon": r"(?im)(\bFirst Horizon\b)",
    "Fleetcor": r"(?im)(\bFleetcor\b)",
    "Flowers Foods": r"(?im)(\bFlowers Foods\b)",
    "Focus on the Family": r"(?im)(\bFocus on the Family\b)",
    "Ford Motor Company": r"(?im)(\bFord Motor Company|Ford\b)",
    "Foster Farms": r"(?im)(\bFoster Farms\b)",
    "Foundation CH": r"(?im)(\bFoundation CH\b)",
    "Fox Media": r"(?im)(\bFox Media|FOX\b)",
    "Frederick Wildman": r"(?im)(\bFrederick Wildman\b)",
    "Frontier Communications": r"(?im)(\bFrontier Communications\b)",
    "Gap": r"(?im)(\bGap\b)",
    "Gartner": r"(?im)(\bGartner\b)",
    "Geely Holding Group": r"(?im)(\bGeely Holding Group\b)",
    "General Dynamics": r"(?im)(\bGeneral Dynamics\b)",
    "GENERAL ELECTRIC + HAIER": r"(?im)(\bGENERAL ELECTRIC \+ HAIER|General electric|Haier|((General Electric)\W+(?:\w+\W+){0,9}?(Haier))|((Haier)\W+(?:\w+\W+){0,9}?(General Electric))\b)",
    "General Mills": r"(?im)(\bGeneral Mills\b)",
    "General Motors": r"(?im)(\bGeneral Motors\b)",
    "Givaudan": r"(?im)(\bGivaudan\b)",
    "Glassdoor": r"(?im)(\bGlassdoor\b)",
    "Goldman Sachs": r"(?im)(\bGoldman Sachs\b)",
    "GOOGLE": r"(?im)(\bGOOGLE\b)",
    "GOOGLE (Ad Sales)": r"(?im)(\bGOOGLE Ad Sales|((Google)\W+(?:\w+\W+){0,3}?(ad sales))|((ad sales)\W+(?:\w+\W+){0,9}?(google))\b)",
    "Gorton's Fish": r"(?im)(\bGorton\'s Fish\b)",
    "Goya": r"(?im)(\bGoya\b)",
    "GRUPO BIMBO": r"(?im)(\bGRUPO BIMBO\b)",
    "Gulf Oil": r"(?im)(\bGulf Oil\b)",
    "H and M": r"(?im)(\bH \& M\b)",
    "Haleon": r"(?im)(\bHaleon\b)",
    "Hamilton Beach": r"(?im)(\bHamilton Beach\b)",
    "Hanes Brands": r"(?im)(\bHanes Brands\b)",
    "Hard Rock": r"(?im)(\bHard Rock\b)",
    "Hartz": r"(?im)(\bHartz\b)",
    "HCA Healthcare": r"(?im)(\bHCA Healthcare\b)",
    "HEINEKEN HOLDING": r"(?im)(\bHEINEKEN HOLDING\b)",
    "Henkel": r"(?im)(\bHenkel\b)",
    "Hennessy": r"(?im)(\bHennessy\b)",
    "Hero Digital": r"(?im)(\bHero Digital\b)",
    "Hershey": r"(?im)(\bHershey\b)",
    "HEWLETT PACKARD": r"(?im)(\bHEWLETT PACKARD\b)",
    "HHS": r"(?im)(\bHHS\b)",
    "Hilton": r"(?im)(\bHilton\b)",
    "Hisense": r"(?im)(\bHisense\b)",
    "HOME DEPOT": r"(?im)(\bHOME DEPOT\b)",
    "Honda": r"(?im)(\bHonda\b)",
    "Honey Baked Ham": r"(?im)(\bHoney Baked Ham\b)",
    "Hormel": r"(?im)(\bHormel\b)",
    "Hostess Brands": r"(?im)(\bHostess Brands\b)",
    "HP Hood": r"(?im)(\bHP Hood\b)",
    "Hyatt": r"(?im)(\bHyatt\b)",
    "Hyundai/Kia": r"(?im)(\bHyundai\/Kia|hyundai|kia\b)",
    "IBM": r"(?im)(\bIBM\b)",
    "IKEA": r"(?im)(\bIKEA\b)",
    "ILLY CAFFE": r"(?im)(\bILLY CAFFE\b)",
    "Imperial Tobacco": r"(?im)(\bImperial Tobacco\b)",
    "Innventure": r"(?im)(\bInnventure\b)",
    "INSPIRE BRANDS INC": r"(?im)(\bINSPIRE BRANDS INC\S*\b)",
    "INSTACART": r"(?im)(\bINSTACART\b)",
    "Intel": r"(?im)(\bIntel\b)",
    "INTUIT": r"(?im)(\bINTUIT\b)",
    "J and J OTC": r"(?im)(\bJ\&J OTC\b)",
    "J.M. Smucker": r"(?im)(\bJ\.M\. Smucker\b)",
    "Jiffy": r"(?im)(\bJiffy\b)",
    "John Deere": r"(?im)(\bJohn Deere\b)",
    "JOHNSON and JOHNSON": r"(?im)(\bJOHNSON \& JOHNSON\b)",
    "JP MORGAN CHASE": r"(?im)(\bJP MORGAN CHASE\b)",
    "JUUL LABS": r"(?im)(\bJUUL LABS\b)",
    "KAISER PERMANENTE": r"(?im)(\bKAISER PERMANENTE\b)",
    "Kao Corporation": r"(?im)(\bKao Corporation\b)",
    "KELLOGGS": r"(?im)(\bKELLOGGS\b)",
    "Kimberly Clark": r"(?im)(\bKimberly\-Clark\b)",
    "King's Hawaiaan": r"(?im)(\bKing\'s Hawaiaan\b)",
    "Kohl's": r"(?im)(\bKohl\'s\b)",
    "KRAFT HEINZ COMPANY": r"(?im)(\bKRAFT HEINZ COMPANY\b)",
    "KROGER": r"(?im)(\bKROGER\b)",
    "Kum and Go": r"(?im)(\bKum \& Go\b)",
    "LA Clippers": r"(?im)(\bLA Clippers\b)",
    "La Madeleine FrenchBakery and Café": r"(?im)(\bLa Madeleine FrenchBakery & Café|La Madeleine French Bakery and Cafe|La Madeleine French Bakery \& Cafe\b)",
    "LACTALIS": r"(?im)(\bLACTALIS\b)",
    "Lamb Weston": r"(?im)(\bLamb Weston\b)",
    "Lerma Agency": r"(?im)(\bLerma Agency\b)",
    "LEVI STRAUSS": r"(?im)(\bLEVI STRAUSS\b)",
    "LG INTERNATIONAL": r"(?im)(\bLG INTERNATIONAL\b)",
    "Liberty Mutual": r"(?im)(\bLiberty Mutual\b)",
    "Liberty Mutual Group": r"(?im)(\bLiberty Mutual Group\b)",
    "Life Time Fitness": r"(?im)(\bLife Time Fitness\b)",
    "Lincoln Financial": r"(?im)(\bLincoln Financial\b)",
    "LIV Golf": r"(?im)(\bLIV Golf\b)",
    "Lockheed Martin": r"(?im)(\bLockheed Martin\b)",
    "L'Oreal": r"(?im)(\bL\'Oreal\b)",
    "LOWES COS": r"(?im)(\bLOWES COS|Lowes\b)",
    "Luxottica Group": r"(?im)(\bLuxottica Group\b)",
    "LVMH \(splits with Ivana by house\)": r"(?im)(\bLVMH\b)",
    "Lyft": r"(?im)(\bLyft\b)",
    "MANSCAPED": r"(?im)(\bMANSCAPED\b)",
    "Manulife Financial": r"(?im)(\bManulife Financial\b)",
    "Marathon": r"(?im)(\bMarathon\b)",
    "Marriott": r"(?im)(\bMarriott\b)",
    "MARS \(MASTERFOOD\)": r"(?im)(\bMARS|Masterfood\b)",
    "Mastercard": r"(?im)(\bMastercard\b)",
    "Match.com": r"(?im)(\bMatch\.com\b)",
    "Mattel": r"(?im)(\bMattel\b)",
    "MAYO CLINIC": r"(?im)(\bMAYO CLINIC\b)",
    "Mazda": r"(?im)(\bMazda\b)",
    "McCain Food": r"(?im)(\bMcCain Food\b)",
    "McCormick and Co": r"(?im)(\bMcCormick \& Co\S*\b)",
    "MCDONALD'S": r"(?im)(\bMCDONALD\'S\b)",
    "McIntosh Group": r"(?im)(\bMcIntosh Group\b)",
    "McKesson Corporation": r"(?im)(\bMcKesson Corporation\b)",
    "MEDTRONIC": r"(?im)(\bMEDTRONIC\b)",
    "MERCK": r"(?im)(\bMERCK|MSD\b)",
    "Meta \(Facebook\)": r"(?im)(\bMeta\b)",
    "METLIFE": r"(?im)(\bMETLIFE\b)",
    "MGM": r"(?im)(\bMGM\b)",
    "MICROSOFT": r"(?im)(\bMICROSOFT\b)",
    "Mikes Hard Lemonda": r"(?im)(\bMike\'s Hard Lemonade\b)",
    "Milos Tea": r"(?im)(\bMilo\'s Tea\b)",
    "Mitsubishi": r"(?im)(\bMitsubishi\b)",
    "MOEN INCORPORATED": r"(?im)(\bMOEN INCORPORATED\b)",
    "Moloco": r"(?im)(\bMoloco\b)",
    "Molson Coors": r"(?im)(\bMolson Coors\b)",
    "MONDELEZ": r"(?im)(\bMONDELEZ\b)",
    "Morton Salt": r"(?im)(\bMorton Salt\b)",
    "Mother LTD": r"(?im)(\bMother LTD\b)",
    "Motorola": r"(?im)(\bMotorola\b)",
    "My Bird Buddy": r"(?im)(\bMy Bird Buddy\b)",
    "My Fitness Pal": r"(?im)(\bMy Fitness Pal\b)",
    "NATIONAL AMUSEMENTS, INC.": r"(?im)(\bNATIONAL AMUSEMENTS\, INC\S*\b)",
    "Nationwide": r"(?im)(\bNationwide\b)",
    "Natures Sunshine": r"(?im)(\bNature\'s Sunshine\b)",
    "Navy Federal": r"(?im)(\bNavy Federal\b)",
    "NBA": r"(?im)(\bNBA|National Basketball Association\b)",
    "Nestle": r"(?im)(\bNestle\b)",
    "Nestle Waters": r"(?im)(\bNestle Waters\b)",
    "NETFLIX": r"(?im)(\bNETFLIX\b)",
    "New York Life": r"(?im)(\bNew York Life\b)",
    "Newell Rubbermaid": r"(?im)(\bNewell Rubbermaid\b)",
    "Newmans Own": r"(?im)(\bNewman\'s Own\b)",
    "NEXTera/FPL": r"(?im)(\bNEXTera\/FPL|Nextera|fpl\b)",
    "NFL": r"(?im)(\bNFL|National Football Association\b)",
    "NIKE": r"(?im)(\bNIKE\b)",
    "Nissan Motor": r"(?im)(\bNissan Motor\b)",
    "NJOY": r"(?im)(\bNJOY\b)",
    "Nokia": r"(?im)(\bNokia\b)",
    "NOOM, INC.": r"(?im)(\bNOOM\, INC\S*\b)",
    "Norwegian Cruise Line": r"(?im)(\bNorwegian Cruise Line\b)",
    "NOVARTIS INTERNATIONAL": r"(?im)(\bNOVARTIS INTERNATIONAL\b)",
    "Nucor": r"(?im)(\bNucor\b)",
    "Ocean Spray": r"(?im)(\bOcean Spray\b)",
    "Olympics": r"(?im)(\bOlympics\b)",
    "Opryland": r"(?im)(\bOpryland\b)",
    "Oracle Corporation": r"(?im)(\bOracle Corporation\b)",
    "Oral Essentials": r"(?im)(\bOral Essentials\b)",
    "Pacific Life": r"(?im)(\bPacific Life\b)",
    "Panasonic": r"(?im)(\bPanasonic\b)",
    "Panda": r"(?im)(\bPanda\b)",
    "Paypal": r"(?im)(\bPaypal\b)",
    "PEPSICO": r"(?im)(\bPEPSICO\b)",
    "PERNOD RICARD": r"(?im)(\bPERNOD RICARD\b)",
    "PetCo": r"(?im)(\bPetCo\b)",
    "PETSMART": r"(?im)(\bPETSMART\b)",
    "PFIZER": r"(?im)(\bPFIZER\b)",
    "PHILLIPS 66": r"(?im)(\bPHILLIPS 66\b)",
    "Pilgrims": r"(?im)(\bPilgrim\’s\b)",
    "PITNEY BOWES": r"(?im)(\bPITNEY BOWES\b)",
    "Plains All American Pipeline": r"(?im)(\bPlains All American Pipeline\b)",
    "Planet Fitness": r"(?im)(\bPlanet Fitness\b)",
    "Planned Parenthood": r"(?im)(\bPlanned Parenthood\b)",
    "PMI US": r"(?im)(\bPMI US|PMI\b)",
    "PNC FINANCIAL SERVICES": r"(?im)(\bPNC FINANCIAL SERVICES\b)",
    "Post Foods": r"(?im)(\bPost Foods\b)",
    "Post Holdings": r"(?im)(\bPost Holdings\b)",
    "PPD": r"(?im)(\bPPD\b)",
    "Prestige Brands": r"(?im)(\bPrestige Brands\b)",
    "PROCTER and GAMBLE": r"(?im)(\bPROCTER \& GAMBLE\b)",
    "Progressive": r"(?im)(\bProgressive\b)",
    "ProTrans": r"(?im)(\bProTrans\b)",
    "Prudential": r"(?im)(\bPrudential\b)",
    "Publix": r"(?im)(\bPublix\b)",
    "Purchasing Power": r"(?im)(\bPurchasing Power\b)",
    "Qualcomm": r"(?im)(\bQualcomm\b)",
    "Raytheon Technologies": r"(?im)(\bRaytheon Technologies\b)",
    "RBI": r"(?im)(\bRBI|Restaurant Brands Intl|Restaurant brands international\b)",
    "Reckitt": r"(?im)(\bReckitt\b)",
    "REDBULL": r"(?im)(\bREDBULL\b)",
    "Reddit": r"(?im)(\bReddit\b)",
    "RELX Technology": r"(?im)(\bRELX Technology\b)",
    "Remy Cointreau": r"(?im)(\bRemy Cointreau\b)",
    "RENAULT": r"(?im)(\bRENAULT\b)",
    "RingCentral": r"(?im)(\bRingCentral|ring central\b)",
    "Roku Inc": r"(?im)(\bRoku Inc\b)",
    "Royal Caribbean": r"(?im)(\bRoyal Caribbean\b)",
    "ROYAL DUTCH SHELL": r"(?im)(\bROYAL DUTCH SHELL\b)",
    "Royal Philips Electronics": r"(?im)(\bRoyal Philips Electronics\b)",
    "RSM": r"(?im)(\bRSM\b)",
    "Sabra": r"(?im)(\bSabra\b)",
    "SALESFORCE.COM": r"(?im)(\bSALESFORCE\.COM\b)",
    "Salt River Project": r"(?im)(\bSalt River Project\b)",
    "SAMSUNG": r"(?im)(\bSAMSUNG\b)",
    "San Francisco 49ers": r"(?im)(\bSan Francisco 49\'ers\b)",
    "SANOFI": r"(?im)(\bSANOFI\b)",
    "SANOFI": r"(?im)(\bSANOFI|((sanofi)\W+(?:\w+\W+){0,3}?(pharma))|((pharma)\W+(?:\w+\W+){0,9}?(sanofi))\b)",
    "SANTANDER GROUP": r"(?im)(\bSANTANDER GROUP\b)",
    "Saputo": r"(?im)(\bSaputo\b)",
    "SC Johnson": r"(?im)(\bSC Johnson\b)",
    "Scooter's Coffee": r"(?im)(\bScooter\'s Coffee\b)",
    "Seven and I Holdings": r"(?im)(\bSeven \& I Holdings\b)",
    "Smartfrog Group": r"(?im)(\bSmartfrog Group\b)",
    "Snapchat": r"(?im)(\bSnapchat\b)",
    "SOCIAL SECURITY ADMINISTRATION": r"(?im)(\bSOCIAL SECURITY ADMINISTRATION\b)",
    "SONIC": r"(?im)(\bSONIC DRIVE\-IN|Sonic\b)",
    "Sony": r"(?im)(\bSony\b)",
    "Spotify": r"(?im)(\bSpotify\b)",
    "Square Enix": r"(?im)(\bSquare Enix\b)",
    "Staples": r"(?im)(\bStaples\b)",
    "STARBUCKS": r"(?im)(\bSTARBUCKS\b)",
    "State Farm": r"(?im)(\bState Farm\b)",
    "Stellantis": r"(?im)(\bStellantis\b)",
    "StoneX Group": r"(?im)(\bStoneX Group\b)",
    "Strategic Education": r"(?im)(\bStrategic Education\b)",
    "SUBARU": r"(?im)(\bSUBARU\b)",
    "SUNTORY HOLDINGS LIMITED": r"(?im)(\bSUNTORY HOLDINGS LIMITED\b)",
    "Synchrony": r"(?im)(\bSynchrony\b)",
    "Sysco": r"(?im)(\bSysco\b)",
    "TAKEDA": r"(?im)(\bTAKEDA\b)",
    "Tapestry": r"(?im)(\bTapestry\b)",
    "Target": r"(?im)(\bTarget\b)",
    "TATA GROUP": r"(?im)(\bTATA GROUP\b)",
    "TD Bank": r"(?im)(\bTD Bank\b)",
    "Televisa Univision": r"(?im)(\bTelevisa Univision\b)",
    "Tesla": r"(?im)(\bTesla\b)",
    "Thales Group": r"(?im)(\bThales Group\b)",
    "The Community": r"(?im)(\bThe Community\b)",
    "The Melting Pot": r"(?im)(\bThe Melting Pot\b)",
    "Thermo Fisher Scientific": r"(?im)(\bThermo Fisher Scientific\b)",
    "Tinder": r"(?im)(\bTinder\b)",
    "TJX": r"(?im)(\bTJX\b)",
    "Toyota Industries": r"(?im)(\bToyota Industries\b)",
    "TRAMONTINA USA": r"(?im)(\bTRAMONTINA USA\b)",
    "TRANE": r"(?im)(\bTRANE\b)",
    "Treehouse": r"(?im)(\bTreehouse\b)",
    "Trive Capital": r"(?im)(\bTrive Capital\b)",
    "TWITTER, INC.": r"(?im)(\bTWITTER\, INC\.)",
    "TYSON FOODS": r"(?im)(\bTYSON FOODS\b)",
    "U.S. POSTAL": r"(?im)(\bU\.S\. POSTAL|Postal Service\b)",
    "UBER TECHNOLOGIES": r"(?im)(\bUBER TECHNOLOGIES\b)",
    "Ulta Beauty": r"(?im)(\bUlta Beauty\b)",
    "UNDER ARMOUR, INC.": r"(?im)(\bUNDER ARMOUR\, INC\S*\b)",
    "UNILEVER": r"(?im)(\bUNILEVER\b)",
    "UNITEDHEALTH GROUP": r"(?im)(\bUNITEDHEALTH GROUP\b)",
    "UPS": r"(?im)(\bUPS\b)",
    "US BANK": r"(?im)(\bUS BANK\b)",
    "US Cellular": r"(?im)(\bUS Cellular\b)",
    "US GOVERNMENT": r"(?im)(\bUS GOVERNMENT\b)",
    "Workday": r"(?im)(\bWorkday\b)",
    "USAA": r"(?im)(\bUSAA\b)",
    "USHBC": r"(?im)(\bUSHBC\b)",
    "Valvoline": r"(?im)(\bValvoline\b)",
    "Vanguard": r"(?im)(\bVanguard\b)",
    "VERIZON COMMUNICATIONS": r"(?im)(\bVERIZON COMMUNICATIONS\b)",
    "VF CORP": r"(?im)(\bVF CORP\b)",
    "Vimergy": r"(?im)(\bVimergy\b)",
    "VISA": r"(?im)(\bVISA\b)",
    "Visit Orlando": r"(?im)(\bVisit Orlando\b)",
    "Vitamix": r"(?im)(\bVitamix\b)",
    "Volkswagen": r"(?im)(\bVolkswagen\b)",
    "WALGREENS": r"(?im)(\bWALGREENS\b)",
    "WALMART": r"(?im)(\bWAL\-MART|walmart|wal mart\b)",
    "WALT DISNEY": r"(?im)(\bWALT DISNEY|Disney\b)",
    "WARNER BROS. DISCOVERY": r"(?im)(\bWARNER BROS\. DISCOVERY|Warner Bros\b)",
    "Wayfair": r"(?im)(\bWayfair\b)",
    "Welch's": r"(?im)(\bWelch\'s\b)",
    "WELLS FARGO": r"(?im)(\bWELLS FARGO\b)",
    "WhatIF? Consulting": r"(?im)(\bWhatIF\? Consulting\b)",
    "Whirlpool": r"(?im)(\bWhirlpool\b)",
    "Who Gives A Crap": r"(?im)(\bWho Gives A Crap\b)",
    "Willo": r"(?im)(\bWillo\b)",
    "Wonderful": r"(?im)(\bWonderful\b)",
    "Words from the Woods / RTIC": r"(?im)(\bWords from the Woods|RTIC\b)",
    "WORLD BANK": r"(?im)(\bWORLD BANK\b)",
    "WWE": r"(?im)(\bWWE\b)",
    "Xmedia": r"(?im)(\bXmedia\b)",
    "Yasso": r"(?im)(\bYasso\b)",
    "YUM BRANDS": r"(?im)(\bYUM BRANDS\b)",
    "Zoom": r"(?im)(\bZoom\b)"}



from gdeltdoc import GdeltDoc, Filters, near, repeat
import re 

f = Filters(
    #keyword = "('new chief marketing officer' OR 'hiring')",
    keyword = "hiring",
    start_date = "2023-04-01",
    end_date = "2023-05-10",
    country = ["UK", "US", "AU"],
    #theme = "TAX_FNCACT_BUSINESS_LEADERS",
    #near = near(10, "Disney", "company"),
)

gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)
from itertools import islice

def select_first_5_entries(dictionary):
    return dict(islice(dictionary.items(), 5))
company_regexes2 = select_first_5_entries(company_regexes)
import pandas as pd
from gdelt import GdeltDoc, Filters
from time import sleep

def process_articles(dictionary):
    gd = GdeltDoc()
    master_df = pd.DataFrame()
    
    for key, value in dictionary.items():
        f = Filters(
            keyword="{} hiring".format(key),
            start_date="2023-04-01",
            end_date="2023-05-10",
            country=["UK", "US", "AU"]
        )
        articles = gd.article_search(f)

        # Create a dataframe for the current result and add 'key' column
        result_df = pd.DataFrame(articles)
        result_df['Key'] = key

        # Append the result to the master dataframe
        master_df = master_df.append(result_df, ignore_index=True)
        
        sleep(1)
        
    return master_df

result_df = process_articles(company_regexes)
articles.info()

result_df2 = result_df.drop_duplicates(subset='title')
result_df2.to_excel('result_df.xlsx')

import pandas as pd
import os
os.chdir(r"Z:/Desktop/rad/scrapes/karachi")
result_df2 = pd.read_excel('result_df.xlsx')
from urllib.request import Request, urlopen
import requests
from boilerpy3 import extractors

extractor = extractors.ArticleExtractor()

# extracted content chunks from GDELT URLs go into this list
juicy_content_list = []

urls = result_df2['url'].to_list()
# urls = urls[0:10]

for url in urls:
    try:
        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()   
        html = str(html.decode('utf-8'))
        content = extractor.get_content(html)
    except Exception as e:
        print(f"Caught an exception: {e}")
        continue

    juicy_content_list.append(content) # juicy content is a clean list of str content chunks
    print(content)
    print('\n')
    

!pip install --upgrade tensorflow
!pip install --upgrade tensorflow-gpu
# STEP 1: USE SUMMARIZATION ALGO
# uses transformers lib
from tensorflow import keras
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn",truncation=True)
sum_content_list = [] # summarized content goes in here
# sum_content_list: a list of lists where each list contains a dict with "summary text:" as k and summary as v

for content in juicy_content_list:
    summary = summarizer(content) # 152--magic number--won't break QA model
    sum_content_list.append(summary)
#print(sum_content_list) 