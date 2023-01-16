#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:04:07 2023

@author: jai
"""
Nifty50 = ['TATASTEEL','HINDALCO','ONGC','TATAMOTORS','ICICIBANK','RELIANCE','AXISBANK','INFY','JSWSTEEL','BPCL','M&M','BHARTIARTL','NTPC','SBILIFE','UPL','POWERGRID','HDFC','ULTRACEMCO','GRASIM','INDUSINDBK','HDFCLIFE','ADANIPORTS','ITC','LT','TCS','MARUTI','BAJAJFINSV','KOTAKBANK','EICHERMOT','WIPRO','HCLTECH','HDFCBANK','NESTLEIND','COALINDIA','BRITANNIA','CIPLA','DRREDDY','SBIN','HINDUNILVR','BAJFINANCE','ADANIENT','SUNPHARMA','APOLLOHOSP','TECHM','TATACONSUM','HEROMOTOCO','BAJAJ-AUTO','ASIANPAINT','TITAN','DIVISLAB']

Nifty_Next50 = ['LICI','MUTHOOTFIN','BANDHANBNK','VEDL','GODREJCP','IOC','MOTHERSON','TATAPOWER','ZOMATO','INDIGO','CHOLAFIN','DLF','ICICIGI','SHREECEM','GAIL','BIOCON','BANKBARODA','AMBUJACEM','HAL','ICICIPRULI','IRCTC','BEL','DABUR','PAYTM','HDFCAMC','NYKAA','GLAND','HAVELLS','SRF','TORNTPHARM','SIEMENS','DMART','SBICARD','ACC','INDUSTOWER','MPHASIS','PIIND','BOSCHLTD','BERGEPAINT','MARICO','NAUKRI','MCDOWELL-N','PIDILITIND','COLPAL','LTIM','ADANITRANS','PGHH','ADANIGREEN','BAJAJHLDNG','ATGL' ]

Nifty_Midcap50 = ['SAIL','PFC','IDFCFIRSTB','PERSISTENT','ASHOKLEY','RECLTD','TATACOMM','M&MFIN','LICHSGFIN','JINDALSTEL','IDEA','TORNTPOWER','COFORGE','PNB','LTTS','GODREJPROP','MFSL','ZEEL','GUJGASLTD','HINDPETRO','CANBK','SHRIRAMFIN','PETRONET','POLYCAB','BHARATFORG','CUMMINSIND','CONCOR','BATAINDIA','VOLTAS','ESCORTS','OFSS','ZYDUSLIFE','AUBANK','ASTRAL','OBEROIRLTY','ABB','ABBOTINDIA','ALKEM','LUPIN','BALKRISIND','INDHOTEL','MRF','UBL','FEDERALBNK','AUROPHARMA','TVSMOTOR','TRENT','JUBLFOOD','HONAUT','PAGEIND']

Nifty_Midcap150 = ['SAIL','YESBANK','PFC','GICRE','IDFCFIRSTB','BANKINDIA','PERSISTENT','NIACL','NATIONALUM','INDIANB','ASHOKLEY','ABCAPITAL','OIL','L&TFH','RECLTD','TATACOMM','STARHEALTH','GRINDWELL','M&MFIN','LINDEINDIA','GSPL','GMRINFRA','LICHSGFIN','CROMPTON','JINDALSTEL','JSWENERGY','IDEA','PRESTIGE','MANYAVAR','BHEL','MAXHEALTH','IEX','TORNTPOWER','COFORGE','SUMICHEM','APLAPOLLO','PNB','GODREJIND','LTTS','DALBHARAT','GODREJPROP','NAM-INDIA','POLICYBZR','IGL','UNIONBANK','RAMCOCEM','AIAENG','MFSL','EMAMILTD','ZEEL','NAVINFLUOR','HINDZINC','JKCEMENT','SOLARINDS','SKFINDIA','COROMANDEL','GUJGASLTD','HINDPETRO','CANBK','IRFC','SHRIRAMFIN','PETRONET','VBL','KPRMILL','NHPC','TATACHEM','CGPOWER','POLYCAB','TRIDENT','UNOMINDA','BLUEDART','PHOENIXLTD','TATAELXSI','FLUOROCHEM','BHARATFORG','LODHA','HAPPSTMNDS','SUNTV','INDIAMART','CUMMINSIND','DEEPAKNTR','CLEAN','CONCOR','BATAINDIA','TIINDIA','VOLTAS','VINATIORGA','ESCORTS','OFSS','ALKYLAMINE','SONACOMS','DELHIVERY','ZYDUSLIFE','AUBANK','ASTRAL','GLAXO','OBEROIRLTY','PATANJALI','ABB','ENDURANCE','SUNDARMFIN','ABBOTINDIA','ALKEM','AJANTPHARM','MSUMI','SANOFI','LUPIN','SCHAEFFLER','SUNDRMFAST','DEVYANI','BALKRISIND','RELAXO','DIXON','ABFRL','INDHOTEL','WHIRLPOOL','THERMAX','LAURUSLABS','KAJARIACER','MRF','APLLTD','KANSAINER','ISEC','UBL','ATUL','PFIZER','AFFLE','FEDERALBNK','AUROPHARMA','IPCALAB','TTML','SYNGENE','ZFCVINDIA','TVSMOTOR','BAYERCROP','TRENT','HATSUN','JUBLFOOD','FORTIS','NATCOPHARM','AAVAS','POONAWALLA','3MINDIA','HONAUT','PAGEIND','SUPREMEIND','AWL','LALPATHLAB','RAJESHEXPO','CRISIL']

Nifty_Smlcap50 = ['CHEMPLASTS','METROPOLIS','MAHABANK','REDINGTON','MANAPPURAM','ROUTE','HFCL','RADICO','LXCHEM','ZENSARTECH','JUBLINGREA','CAMS','BALRAMCHIN','FSL','RENUKA','CYIENT','LATENTVIEW','CAMPUS','AMARAJABAT','CANFINHOME','MEDPLUS','JBCHEPHARM','METROBRAND','ANGELONE','BSOFT','ALOKINDS','UTIAMC','BSE','CHAMBLFERT','BAJAJELEC','KPITTECH','CESC','BIRLACORPN','BDL','ANURAS','INTELLECT','AMBER','BALAMINES','INDIGOPNTS','TV18BRDCST','CDSL','PVR','GNFC','WELSPUNIND','GRAPHITE','APOLLOTYRE','HINDCOPPER','STLTECH','MRPL','IDFC']

Nifty_Smlcap250 = ['SWANENERGY','CSBBANK','RVNL','CHEMPLASTS','HIKAL','UCOBANK','MAZDOCK','METROPOLIS','MAHABANK','RAINBOW','WOCKPHARMA','PRAJIND','MCX','DBL','GMMPFAUDLR','REDINGTON','GRANULES','RBLBANK','MANAPPURAM','BORORENEW','FINCABLES','GARFIBRES','IOB','MGL','BLUESTARCO','GLENMARK','ROUTE','HFCL','MAPMYINDIA','RTNINDIA','SAPPHIRE','KRBL','KARURVYSYA','PGHL','SUPRAJIT','RADICO','LXCHEM','IDBI','GPPL','ZENSARTECH','CENTRALBK','MOTILALOFS','JUBLINGREA','COCHINSHIP','CAMS','PRINCEPIPE','BALRAMCHIN','MASTEK','LUXIND','GOCOLORS','ASTRAZEN','INFIBEAM','LAXMIMACH','KEI','SPARC','FSL','CARBORUNIV','RENUKA','ENGINERSIN','THYROCARE','CYIENT','NUVOCO','TATACOFFEE','SYMPHONY','LATENTVIEW','AVANTIFEED','GRINFRA','CAMPUS','KALPATPOWR','AMARAJABAT','GODFRYPHLP','SUDARSCHEM','TANLA','SOBHA','SHYAMMETL','TRIVENI','CANFINHOME','ASTERDM','IRB','CAPLIPOINT','APTUS','SHILPAMED','BEML','NH','MEDPLUS','SFL','TTKPRESTIG','AETHER','DELTACORP','CEATLTD','SHOPERSTOP','VAIBHAVGBL','ROSSARI','ECLERX','IBREALEST','BRIGADE','VARROC','KNRCON','SUVENPHAR','JBCHEPHARM','BHARATRAS','METROBRAND','EIHOTEL','SWSOLAR','TCNSBRANDS','EDELWEISS','CASTROLIND','HLEGLAS','POLYMED','ANGELONE','BSOFT','JAMNAAUTO','HGS','FINEORG','OLECTRA','SJVN','SUZLON','ALOKINDS','CREDITACC','MMTC','IIFLWAM','SUNTECK','CGCL','CHALET','AEGISCHEM','FINPIPE','NOCIL','ORIENTELEC','UFLEX','SHARDACROP','QUESS','JUSTDIAL','UTIAMC','CERA','NBCC','CUB','JKPAPER','BSE','TEAMLEASE','CHAMBLFERT','BAJAJELEC','KPITTECH','MAHLOG','CESC','BIRLACORPN','BDL','VTL','TATAINVEST','ANURAS','PNBHOUSING','POLYPLEX','CHOLAHLDNG','INTELLECT','CENTURYTEX','AMBER','GALAXYSURF','ABSLAMC','MHRIL','JUBLPHARMA','BALAMINES','RAYMOND','PCBL','BCG','MAHLIFE','INDIGOPNTS','BASF','GREENPANEL','GODREJAGRO','VGUARD','WELCORP','TV18BRDCST','INDOCO','JYOTHYLAB','GUJALKALI','WESTLIFE','CDSL','INOXLEISUR','JMFINANCIL','LEMONTREE','PVR','TCIEXP','PRSMJOHNSN','GNFC','CENTURYPLY','RAIN','WELSPUNIND','RATNAMANI','GRAPHITE','ZYDUSWELL','EQUITASBNK','JBMA','KALYANKJIL','MOIL','GAEL','EXIDEIND','BBTC','KEC','APOLLOTYRE','FDC','DCMSHRIRAM','IFBIND','POWERINDIA','INDIACEM','HINDCOPPER','VMART','NETWORK18','STLTECH','ASAHIINDIA','MRPL','TCI','NLCINDIA','AARTIDRUGS','EIDPARRY','RALLIS','VIPIND','IDFC','EASEMYTRIP','TEJASNET','PNCINFRA','HEG','SONATSOFTW','KIMS','HUDCO','ITI','VIJAYA','NAZARA','GSFC','RHIM','RITES','SIS','EPL','TIMKEN','HOMEFIRST','MTARTECH','NCC','JKLAKSHMI','RCF','IIFL','DHANI','ELGIEQUIP','RBA','CCL','GESHIP','DEEPAKFERT','TRITURBINE','PRIVISCL','IBULHSGFIN','JSL','MAHINDCIE','FACT']

Nifty_500 = ['3MINDIA','ABB','ACC','AIAENG','APLAPOLLO','AUBANK','AARTIDRUGS','AAVAS','ABBOTINDIA','ADANIENT','ADANIGREEN','ADANIPORTS','ATGL','ADANITRANS','AWL','ABCAPITAL','ABFRL','ABSLAMC','AEGISCHEM','AETHER','AFFLE','AJANTPHARM','APLLTD','ALKEM','ALKYLAMINE','ALOKINDS','AMARAJABAT','AMBER','AMBUJACEM','ANGELONE','ANURAS','APOLLOHOSP','APOLLOTYRE','APTUS','ASAHIINDIA','ASHOKLEY','ASIANPAINT','ASTERDM','ASTRAZEN','ASTRAL','ATUL','AUROPHARMA','AVANTIFEED','DMART','AXISBANK','BASF','BEML','BSE','BAJAJ-AUTO','BAJAJELEC','BAJFINANCE','BAJAJFINSV','BAJAJHLDNG','BALAMINES','BALKRISIND','BALRAMCHIN','BANDHANBNK','BANKBARODA','BANKINDIA','MAHABANK','BATAINDIA','BAYERCROP','BERGEPAINT','BDL','BEL','BHARATFORG','BHEL','BPCL','BHARATRAS','BHARTIARTL','BIOCON','BIRLACORPN','BSOFT','BLUEDART','BLUESTARCO','BBTC','BORORENEW','BOSCHLTD','BRIGADE','BCG','BRITANNIA','MAPMYINDIA','CCL','CESC','CGPOWER','CRISIL','CSBBANK','CAMPUS','CANFINHOME','CANBK','CAPLIPOINT','CGCL','CARBORUNIV','CASTROLIND','CEATLTD','CENTRALBK','CDSL','CENTURYPLY','CENTURYTEX','CERA','CHALET','CHAMBLFERT','CHEMPLASTS','CHOLAHLDNG','CHOLAFIN','CIPLA','CUB','CLEAN','COALINDIA','COCHINSHIP','COFORGE','COLPAL','CAMS','CONCOR','COROMANDEL','CREDITACC','CROMPTON','CUMMINSIND','CYIENT','DCMSHRIRAM','DLF','DABUR','DALBHARAT','DEEPAKFERT','DEEPAKNTR','DELHIVERY','DELTACORP','DEVYANI','DHANI','DBL','DIVISLAB','DIXON','LALPATHLAB','DRREDDY','EIDPARRY','EIHOTEL','EPL','EASEMYTRIP','EDELWEISS','EICHERMOT','ELGIEQUIP','EMAMILTD','ENDURANCE','ENGINERSIN','EQUITASBNK','ESCORTS','EXIDEIND','FDC','NYKAA','FEDERALBNK','FACT','FINEORG','FINCABLES','FINPIPE','FSL','FORTIS','GRINFRA','GAIL','GMMPFAUDLR','GMRINFRA','GALAXYSURF','GARFIBRES','GICRE','GLAND','GLAXO','GLENMARK','GOCOLORS','GODFRYPHLP','GODREJAGRO','GODREJCP','GODREJIND','GODREJPROP','GRANULES','GRAPHITE','GRASIM','GESHIP','GREENPANEL','GRINDWELL','GUJALKALI','GAEL','FLUOROCHEM','GUJGASLTD','GNFC','GPPL','GSFC','GSPL','HEG','HCLTECH','HDFCAMC','HDFCBANK','HDFCLIFE','HFCL','HLEGLAS','HAPPSTMNDS','HATSUN','HAVELLS','HEROMOTOCO','HIKAL','HINDALCO','HGS','HAL','HINDCOPPER','HINDPETRO','HINDUNILVR','HINDZINC','POWERINDIA','HOMEFIRST','HONAUT','HUDCO','HDFC','ICICIBANK','ICICIGI','ICICIPRULI','ISEC','IDBI','IDFCFIRSTB','IDFC','IFBIND','IIFL','IIFLWAM','IRB','ITC','ITI','INDIACEM','IBULHSGFIN','IBREALEST','INDIAMART','INDIANB','IEX','INDHOTEL','IOC','IOB','IRCTC','IRFC','INDIGOPNTS','INDOCO','IGL','INDUSTOWER','INDUSINDBK','INFIBEAM','NAUKRI','INFY','INOXLEISUR','INTELLECT','INDIGO','IPCALAB','JBCHEPHARM','JKCEMENT','JBMA','JKLAKSHMI','JKPAPER','JMFINANCIL','JSWENERGY','JSWSTEEL','JAMNAAUTO','JSL','JINDALSTEL','JUBLFOOD','JUBLINGREA','JUBLPHARMA','JUSTDIAL','JYOTHYLAB','KPRMILL','KEI','KNRCON','KPITTECH','KRBL','KAJARIACER','KALPATPOWR','KALYANKJIL','KANSAINER','KARURVYSYA','KEC','KOTAKBANK','KIMS','L&TFH','LTTS','LICHSGFIN','LTIM','LAXMIMACH','LT','LATENTVIEW','LAURUSLABS','LXCHEM','LEMONTREE','LICI','LINDEINDIA','LUPIN','LUXIND','MMTC','MOIL','MRF','MTARTECH','LODHA','MGL','M&MFIN','M&M','MAHINDCIE','MHRIL','MAHLIFE','MAHLOG','MANAPPURAM','MRPL','MARICO','MARUTI','MASTEK','MFSL','MAXHEALTH','MAZDOCK','MEDPLUS','METROBRAND','METROPOLIS','MSUMI','MOTILALOFS','MPHASIS','MCX','MUTHOOTFIN','NATCOPHARM','NBCC','NCC','NHPC','NLCINDIA','NOCIL','NTPC','NH','NATIONALUM','NAVINFLUOR','NAZARA','NESTLEIND','NETWORK18','NAM-INDIA','NUVOCO','OBEROIRLTY','ONGC','OIL','OLECTRA','PAYTM','OFSS','ORIENTELEC','POLICYBZR','PCBL','PIIND','PNBHOUSING','PNCINFRA','PVR','PAGEIND','PATANJALI','PERSISTENT','PETRONET','PFIZER','PHOENIXLTD','PIDILITIND','POLYMED','POLYCAB','POLYPLEX','POONAWALLA','PFC','POWERGRID','PRAJIND','PRESTIGE','PRINCEPIPE','PRSMJOHNSN','PRIVISCL','PGHL','PGHH','PNB','QUESS','RBLBANK','RECLTD','RHIM','RITES','RADICO','RVNL','RAIN','RAINBOW','RAJESHEXPO','RALLIS','RCF','RATNAMANI','RTNINDIA','RAYMOND','REDINGTON','RELAXO','RELIANCE','RBA','ROSSARI','ROUTE','SBICARD','SBILIFE','SIS','SJVN','SKFINDIA','SRF','MOTHERSON','SANOFI','SAPPHIRE','SCHAEFFLER','SHARDACROP','SFL','SHILPAMED','SHOPERSTOP','SHREECEM','RENUKA','SHRIRAMFIN','SHYAMMETL','SIEMENS','SOBHA','SOLARINDS','SONACOMS','SONATSOFTW','STARHEALTH','SBIN','SAIL','SWSOLAR','STLTECH','SUDARSCHEM','SUMICHEM','SPARC','SUNPHARMA','SUNTV','SUNDARMFIN','SUNDRMFAST','SUNTECK','SUPRAJIT','SUPREMEIND','SUVENPHAR','SUZLON','SWANENERGY','SYMPHONY','SYNGENE','TCIEXP','TCNSBRANDS','TTKPRESTIG','TV18BRDCST','TVSMOTOR','TANLA','TATACHEM','TATACOFFEE','TATACOMM','TCS','TATACONSUM','TATAELXSI','TATAINVEST','TATAMTRDVR','TATAMOTORS','TATAPOWER','TATASTEEL','TTML','TEAMLEASE','TECHM','TEJASNET','NIACL','RAMCOCEM','THERMAX','THYROCARE','TIMKEN','TITAN','TORNTPHARM','TORNTPOWER','TCI','TRENT','TRIDENT','TRIVENI','TRITURBINE','TIINDIA','UCOBANK','UFLEX','UNOMINDA','UPL','UTIAMC','ULTRACEMCO','UNIONBANK','UBL','MCDOWELL-N','VGUARD','VMART','VIPIND','VAIBHAVGBL','VTL','VARROC','VBL','MANYAVAR','VEDL','VIJAYA','VINATIORGA','IDEA','VOLTAS','WELCORP','WELSPUNIND','WESTLIFE','WHIRLPOOL','WIPRO','WOCKPHARMA','YESBANK','ZFCVINDIA','ZEEL','ZENSARTECH','ZOMATO','ZYDUSLIFE','ZYDUSWELL','ECLERX',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'3MINDIA','ABB','ACC','AIAENG','APLAPOLLO','AUBANK','AARTIDRUGS','AAVAS','ABBOTINDIA','ADANIENT','ADANIGREEN','ADANIPORTS','ATGL','ADANITRANS','AWL','ABCAPITAL','ABFRL','ABSLAMC','AEGISCHEM','AETHER','AFFLE','AJANTPHARM','APLLTD','ALKEM','ALKYLAMINE','ALOKINDS','AMARAJABAT','AMBER','AMBUJACEM','ANGELONE','ANURAS','APOLLOHOSP','APOLLOTYRE','APTUS','ASAHIINDIA','ASHOKLEY','ASIANPAINT','ASTERDM','ASTRAZEN','ASTRAL','ATUL','AUROPHARMA','AVANTIFEED','DMART','AXISBANK','BASF','BEML','BSE','BAJAJ-AUTO','BAJAJELEC','BAJFINANCE','BAJAJFINSV','BAJAJHLDNG','BALAMINES','BALKRISIND','BALRAMCHIN','BANDHANBNK','BANKBARODA','BANKINDIA','MAHABANK','BATAINDIA','BAYERCROP','BERGEPAINT','BDL','BEL','BHARATFORG','BHEL','BPCL','BHARATRAS','BHARTIARTL','BIOCON','BIRLACORPN','BSOFT','BLUEDART','BLUESTARCO','BBTC','BORORENEW','BOSCHLTD','BRIGADE','BCG','BRITANNIA','MAPMYINDIA','CCL','CESC','CGPOWER','CRISIL','CSBBANK','CAMPUS','CANFINHOME','CANBK','CAPLIPOINT','CGCL','CARBORUNIV','CASTROLIND','CEATLTD','CENTRALBK','CDSL','CENTURYPLY','CENTURYTEX','CERA','CHALET','CHAMBLFERT','CHEMPLASTS','CHOLAHLDNG','CHOLAFIN','CIPLA','CUB','CLEAN','COALINDIA','COCHINSHIP','COFORGE','COLPAL','CAMS','CONCOR','COROMANDEL','CREDITACC','CROMPTON','CUMMINSIND','CYIENT','DCMSHRIRAM','DLF','DABUR','DALBHARAT','DEEPAKFERT','DEEPAKNTR','DELHIVERY','DELTACORP','DEVYANI','DHANI','DBL','DIVISLAB','DIXON','LALPATHLAB','DRREDDY','EIDPARRY','EIHOTEL','EPL','EASEMYTRIP','EDELWEISS','EICHERMOT','ELGIEQUIP','EMAMILTD','ENDURANCE','ENGINERSIN','EQUITASBNK','ESCORTS','EXIDEIND','FDC','NYKAA','FEDERALBNK','FACT','FINEORG','FINCABLES','FINPIPE','FSL','FORTIS','GRINFRA','GAIL','GMMPFAUDLR','GMRINFRA','GALAXYSURF','GARFIBRES','GICRE','GLAND','GLAXO','GLENMARK','GOCOLORS','GODFRYPHLP','GODREJAGRO','GODREJCP','GODREJIND','GODREJPROP','GRANULES','GRAPHITE','GRASIM','GESHIP','GREENPANEL','GRINDWELL','GUJALKALI','GAEL','FLUOROCHEM','GUJGASLTD','GNFC','GPPL','GSFC','GSPL','HEG','HCLTECH','HDFCAMC','HDFCBANK','HDFCLIFE','HFCL','HLEGLAS','HAPPSTMNDS','HATSUN','HAVELLS','HEROMOTOCO','HIKAL','HINDALCO','HGS','HAL','HINDCOPPER','HINDPETRO','HINDUNILVR','HINDZINC','POWERINDIA','HOMEFIRST','HONAUT','HUDCO','HDFC','ICICIBANK','ICICIGI','ICICIPRULI','ISEC','IDBI','IDFCFIRSTB','IDFC','IFBIND','IIFL','IIFLWAM','IRB','ITC','ITI','INDIACEM','IBULHSGFIN','IBREALEST','INDIAMART','INDIANB','IEX','INDHOTEL','IOC','IOB','IRCTC','IRFC','INDIGOPNTS','INDOCO','IGL','INDUSTOWER','INDUSINDBK','INFIBEAM','NAUKRI','INFY','INOXLEISUR','INTELLECT','INDIGO','IPCALAB','JBCHEPHARM','JKCEMENT','JBMA','JKLAKSHMI','JKPAPER','JMFINANCIL','JSWENERGY','JSWSTEEL','JAMNAAUTO','JSL','JINDALSTEL','JUBLFOOD','JUBLINGREA','JUBLPHARMA','JUSTDIAL','JYOTHYLAB','KPRMILL','KEI','KNRCON','KPITTECH','KRBL','KAJARIACER','KALPATPOWR','KALYANKJIL','KANSAINER','KARURVYSYA','KEC','KOTAKBANK','KIMS','L&TFH','LTTS','LICHSGFIN','LTIM','LAXMIMACH','LT','LATENTVIEW','LAURUSLABS','LXCHEM','LEMONTREE','LICI','LINDEINDIA','LUPIN','LUXIND','MMTC','MOIL','MRF','MTARTECH','LODHA','MGL','M&MFIN','M&M','MAHINDCIE','MHRIL','MAHLIFE','MAHLOG','MANAPPURAM','MRPL','MARICO','MARUTI','MASTEK','MFSL','MAXHEALTH','MAZDOCK','MEDPLUS','METROBRAND','METROPOLIS','MSUMI','MOTILALOFS','MPHASIS','MCX','MUTHOOTFIN','NATCOPHARM','NBCC','NCC','NHPC','NLCINDIA','NOCIL','NTPC','NH','NATIONALUM','NAVINFLUOR','NAZARA','NESTLEIND','NETWORK18','NAM-INDIA','NUVOCO','OBEROIRLTY','ONGC','OIL','OLECTRA','PAYTM','OFSS','ORIENTELEC','POLICYBZR','PCBL','PIIND','PNBHOUSING','PNCINFRA','PVR','PAGEIND','PATANJALI','PERSISTENT','PETRONET','PFIZER','PHOENIXLTD','PIDILITIND','POLYMED','POLYCAB','POLYPLEX','POONAWALLA','PFC','POWERGRID','PRAJIND','PRESTIGE','PRINCEPIPE','PRSMJOHNSN','PRIVISCL','PGHL','PGHH','PNB','QUESS','RBLBANK','RECLTD','RHIM','RITES','RADICO','RVNL','RAIN','RAINBOW','RAJESHEXPO','RALLIS','RCF','RATNAMANI','RTNINDIA','RAYMOND','REDINGTON','RELAXO','RELIANCE','RBA','ROSSARI','ROUTE','SBICARD','SBILIFE','SIS','SJVN','SKFINDIA','SRF','MOTHERSON','SANOFI','SAPPHIRE','SCHAEFFLER','SHARDACROP','SFL','SHILPAMED','SHOPERSTOP','SHREECEM','RENUKA','SHRIRAMFIN','SHYAMMETL','SIEMENS','SOBHA','SOLARINDS','SONACOMS','SONATSOFTW','STARHEALTH','SBIN','SAIL','SWSOLAR','STLTECH','SUDARSCHEM','SUMICHEM','SPARC','SUNPHARMA','SUNTV','SUNDARMFIN','SUNDRMFAST','SUNTECK','SUPRAJIT','SUPREMEIND','SUVENPHAR','SUZLON','SWANENERGY','SYMPHONY','SYNGENE','TCIEXP','TCNSBRANDS','TTKPRESTIG','TV18BRDCST','TVSMOTOR','TANLA','TATACHEM','TATACOFFEE','TATACOMM','TCS','TATACONSUM','TATAELXSI','TATAINVEST','TATAMTRDVR','TATAMOTORS','TATAPOWER','TATASTEEL','TTML','TEAMLEASE','TECHM','TEJASNET','NIACL','RAMCOCEM','THERMAX','THYROCARE','TIMKEN','TITAN','TORNTPHARM','TORNTPOWER','TCI','TRENT','TRIDENT','TRIVENI','TRITURBINE','TIINDIA','UCOBANK','UFLEX','UNOMINDA','UPL','UTIAMC','ULTRACEMCO','UNIONBANK','UBL','MCDOWELL-N','VGUARD','VMART','VIPIND','VAIBHAVGBL','VTL','VARROC','VBL','MANYAVAR','VEDL','VIJAYA','VINATIORGA','IDEA','VOLTAS','WELCORP','WELSPUNIND','WESTLIFE','WHIRLPOOL','WIPRO','WOCKPHARMA','YESBANK','ZFCVINDIA','ZEEL','ZENSARTECH','ZOMATO','ZYDUSLIFE','ZYDUSWELL','ECLERX']
