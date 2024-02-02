"""#$$$$$$$$$$#"""
"""
MARKET_ANALYSIS
"""
MARKET_ANALYSIS_SHORT_INTERVAL = 7
MARKET_ANALYSIS_MID_INTERVAL = 10
MARKET_ANALYSIS_LONG_INTERVAL = 14
MARKET_ANALYSIS_INTERVALS = [MARKET_ANALYSIS_SHORT_INTERVAL,
                             MARKET_ANALYSIS_MID_INTERVAL,
                             MARKET_ANALYSIS_LONG_INTERVAL]
MARKET_ANALYSIS_RSI_BUY_THREASHOLD = 30
MARKET_ANALYSIS_RSI_SELL_THREASHOLD = 70
MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_BUY_THREASHOLD = 20
MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_SELL_THREASHOLD = 80
MARKET_ANALYSIS_BUY = "BUY"
MARKET_ANALYSIS_SELL = "SELL"
MARKET_ANALYSIS_REST = "REST"



"""#$$$$$$$$$$#"""
"""
CONFORMATION_ANALYZER
"""
CONFORMATION_INDICATOR_INPUT_DATA_FORMAT = dict[str: list[ float ]]
CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT = list[int]
CONFORMATION_INDICATOR_OUTPUT_FORMAT = dict[str: dict[int: list[ float|int ]]]
CONFORMATION_INDICATOR_INPUT = ["OPEN" ,"HIGH" ,"LOW" ,"CLOSE"]
CONFORMATION_INDICATOR_TREND_ANALYZER_INTERNAL_RETURN_DATA_FORMAT = dict[int: list[ float|int ]]
CONFORMATION_INDICATOR_SMA_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_EMA_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_SCHOCASTIC_OSCILLATOR_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_RSI_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_AVERAGE_TRUE_RANGE_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_BOILINGER_BANDS_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_ON_BALALNCE_VOLUME_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_CHAIKIN_OSCILLATOR_DATA_FORMAT = CONFORMATION_INDICATOR_OUTPUT_FORMAT
CONFORMATION_INDICATOR_AVOID_ZERO = 10**(-10)


"""#$$$$$$$$$$#"""
"""
CANDLESTICK_ANALYZER
"""
CANDLESTICK_ANALYZER_DISCRETE_PARTS = 100
CANDLESTICK_ANALYZER_CHECK_TREND_SAMPLES = 5
CANDLESTICK_ANALYZER_OBSERVATIONS = 20
CANDLESTICK_ANALYZER_INPUT = ["OPEN" ,"HIGH" ,"LOW" ,"CLOSE"]
CANDLESTICK_ANALYZER_AVOID_ZERO = 10**(-10)
CANDLESTICK_ANALYZER_LIST_INPUT_FORMAT = list[ list[ float ] ]
CANDLESTICK_ANALYZER_DICT_INPUT_FORMAT = dict[ str: list[ float ] ]
CANDLESTICK_ANALYZER_INPUT_FORMAT = CANDLESTICK_ANALYZER_LIST_INPUT_FORMAT | CANDLESTICK_ANALYZER_DICT_INPUT_FORMAT
CANDLESTICK_ANALYZER_INTERNAL_FORMAT = list[list[int]]
CANDLESTICK_ANALYZER_OUTPUT_FORMAT = dict[ str: dict[ str: int ] | str ]
CANDLESTICK_ANALYZER_BUY = "BUY"
CANDLESTICK_ANALYZER_SELL = "SELL"
CANDLESTICK_ANALYZER_REST = "REST"
CANDLESTICK_ANALYZER_BULLISH_TREND = "BULLISH"
CANDLESTICK_ANALYZER_BEARISH_TREND = "BEARISH"
CANDLESTICK_ANALYZER_DEFAULT_TREND = "ABSENT"



"""#$$$$$$$$$$#"""
"""
CANDLESTICK_METADATA
"""
HAMMER_BODY = 0.3
HAMMER_UPPER_SHADOW = 0.2
HAMMER_LOWER_SHADOW_FACTOR = 2

THREE_WHITE_SOLIDERS_BODY = 0.25

PIERCING_MARBOZU_BODY = 0.3

MARUBOZU_BODY = 0.7

DOGI_BODY = 0.15

THREE_INSIDE_UP_BEAR_BODY = 0.3

BULLISH_HARAMI_BEAR_BODY = 0.25

TWEEZER_BOTTOM_SIMILARITY_RATIO = 0.05

INVERTED_HAMMER_BODY = 0.2
INVERTED_HAMMER_LOWER_SHADOW = 0.2
INVERTED_HAMMER_UPPER_SHADOW_FACTOR = 2

THREE_OUTSIDE_UP_BULL_BODY = 0.25

ON_NECK_SIMILARITY_RATIO = 0.05

HANGING_MAN_BODY = 0.2
HANGING_MAN_UPPER_SHADOW = 0.2
HANDING_MAN_LOWER_SHADOW_FACTOR = 2

DARK_CLOUD_COVER_BODY = 0.25

THREE_BLACK_CROWS_BODY = 0.3

THREE_INSIDE_DOWN_BULL_BODY = 0.3

BEARISH_HARAMI_BEAR_BODY = 0.25

SHOOTING_STAR_BODY = 0.2
SHOOTING_STAR_LOWER_SHADOW = 0.2
SHOOTING_STAR_UPPER_SHADOW_FACTOR = 2

TWEEZER_TOP_SIMILARITY_RATIO = 0.05

THREE_OUTSIDE_DOWN_BEAR_BODY = 0.25



"""#$$$$$$$$$$#"""
"""
103 CANDLES
"""
BEARISH_BELT_HOLD_UPPER_SHADOW_FACTOR = 0.05
BEARISH_BELT_HOLD_UPPER_SHADOW_FACTOR = 0.2
BEARISH_BELT_HOLD_SCORE = -0.68

BULLISH_BELT_HOLD_UPPER_SHADOW_FACTOR = 0.2
BULLISH_BELT_HOLD_LOWER_SHADOW_FACTOR = 0.05
BULLISH_BELT_HOLD_SCORE = 0.71

BLACK_CANDLE_SCORE = 0.52

SHORT_BLACK_CANDLE_SCORE = 0.52