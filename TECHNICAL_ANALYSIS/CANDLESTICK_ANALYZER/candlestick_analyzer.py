from ..CONSTANTS.constants import *

#$$$$$$$$$$#

class CANDLESTICK_ANALYZER :
    def __init__(self) -> None :
        self.SCORE = 0

    def analyze_candlestick_patterns(self,
                                     data: CANDLESTICK_ANALYZER_INPUT_FORMAT) -> CANDLESTICK_ANALYZER_OUTPUT_FORMAT :
        discrete_data = self.convert_to_discrete_data(data)
        analysis_dictionary = {"PATTERNS": {},
                               "ANALYSIS": "REST",
                               "CURRENT_TREND": "ABSENT"}
        self.SCORE = 0
        if discrete_data is None :
            return analysis_dictionary
        if len(discrete_data) < CANDLESTICK_ANALYZER_OBSERVATIONS :
            return analysis_dictionary
 
        #print("#")
        self.chek_hammer(discrete_data,
                         analysis_dictionary)
        #print("#")
        self.chek_piercing(discrete_data,
                           analysis_dictionary)
        #print("#")
        self.chek_bullish_engulfing(discrete_data,
                                    analysis_dictionary)
        #print("#")
        self.chek_morning_star(discrete_data,
                               analysis_dictionary)
        #print("#")
        self.three_white_soliders(discrete_data,
                                  analysis_dictionary)
        #print("#")
        self.chek_white_marubozu(discrete_data,
                                 analysis_dictionary)
        #print("#")
        self.chek_three_inside_up(discrete_data,
                                  analysis_dictionary)
        #print("#")
        self.chek_bullish_harami(discrete_data,
                                 analysis_dictionary)
        #print("#")
        self.chek_tweezer_bottom(discrete_data,
                                 analysis_dictionary)
        #print("#")
        self.chek_inverted_hammer(discrete_data,
                                  analysis_dictionary)
        #print("#")
        self.chek_three_outside_up(discrete_data,
                                   analysis_dictionary)
        #print("#")
        self.chek_on_neck(discrete_data,
                          analysis_dictionary)
        #print("#")
        self.chek_hanging_man(discrete_data,
                              analysis_dictionary)
        #print("#")
        self.chek_dark_cloud_cover(discrete_data,
                                   analysis_dictionary)
        #print("#")
        self.chek_bearish_engulfing(discrete_data,
                                    analysis_dictionary)
        #print("#")
        self.chek_evening_star(discrete_data,
                               analysis_dictionary)
        #print("#")
        self.chek_three_black_crows(discrete_data,
                                    analysis_dictionary)
        #print("#")
        self.chek_black_marubozu(discrete_data,
                                 analysis_dictionary)
        #print("#")
        self.chek_three_inside_down(discrete_data,
                                    analysis_dictionary)
        #print("#")
        self.chek_bearish_harami(discrete_data,
                                 analysis_dictionary)
        #print("#")
        self.chek_shooting_star(discrete_data,
                                analysis_dictionary)
        #print("#")
        self.chek_tweezer_top(discrete_data,
                              analysis_dictionary)
        #print("#")
        self.chek_three_outside_down(discrete_data,
                                     analysis_dictionary)
        self.process_score_and_analysis(discrete_data,
                                        analysis_dictionary)
        return analysis_dictionary

    def convert_to_discrete_data(self,
                                 data: CANDLESTICK_ANALYZER_INPUT_FORMAT) -> CANDLESTICK_ANALYZER_INTERNAL_FORMAT :
        if type(data) is list :
            return self.list_to_discrete_data(data)
        if type(data) is dict :
            return self.dict_to_discrete_data(data)

    def list_to_discrete_data(self,
                              data: CANDLESTICK_ANALYZER_LIST_INPUT_FORMAT) -> CANDLESTICK_ANALYZER_INTERNAL_FORMAT :
        temp = []
        for _ in range(-CANDLESTICK_ANALYZER_OBSERVATIONS, 0) :
            temp += data[_]
        max_ = max(temp)

        temp = []
        for _ in range(-CANDLESTICK_ANALYZER_OBSERVATIONS, 0) :
            temp += data[_]
        min_ = min(temp)

        discrete_data = []
        for _ in range(-CANDLESTICK_ANALYZER_OBSERVATIONS, 0) :
            temp = []
            for __ in range(4) :
                temp.append( round(((data[_][__] - min_)/
                                    (max_ - min_ + CANDLESTICK_ANALYZER_AVOID_ZERO))*
                                   CANDLESTICK_ANALYZER_DISCRETE_PARTS, 0))
            discrete_data.append(temp)
        return discrete_data

    def dict_to_discrete_data(self,
                              data: CANDLESTICK_ANALYZER_DICT_INPUT_FORMAT) -> CANDLESTICK_ANALYZER_INTERNAL_FORMAT :
        temp = []
        for _ in CANDLESTICK_ANALYZER_INPUT :
            temp += data[_][-CANDLESTICK_ANALYZER_OBSERVATIONS:]
        max_ = max(temp)

        temp = []
        for _ in CANDLESTICK_ANALYZER_INPUT :
            temp += data[_][-CANDLESTICK_ANALYZER_OBSERVATIONS:]
        min_ = min(temp)

        discrete_data = []
        try :
            for _ in range(-CANDLESTICK_ANALYZER_OBSERVATIONS, 0) :
                temp = []
                for __ in CANDLESTICK_ANALYZER_INPUT :
                    temp.append(round( ((data[__][_]-min_)/(max_ - min_ + CANDLESTICK_ANALYZER_AVOID_ZERO))*CANDLESTICK_ANALYZER_DISCRETE_PARTS ))
                discrete_data.append(temp)
        except : print(data)
        return discrete_data

    """#$$$$$$$$$$#"""
    """
    BULLISH TRENDS
    """
    def chek_hammer(self,
                     data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                     analysis_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analysis_data["PATTERNS"]["HAMMER"] = 0
        if not (
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data))) :
            return
        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        body = abs(close - open)
        lower_shadow = min(open, close) - low
        upper_shadow = high - max(close, open)

        if not (upper_shadow <= (high-low)*(HAMMER_UPPER_SHADOW) and
                lower_shadow >= body*HAMMER_LOWER_SHADOW_FACTOR and
                body <= (high-low)*(HAMMER_BODY)) :
            return
        analysis_data["PATTERNS"]["HAMMER"] = 1
        self.SCORE += 1

    def chek_piercing(self,
                      data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                      analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["PIERCING"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bearish(-2, data) and
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data))) :
            return

        open_bear = data[-2][0]
        high_bear = data[-2][1]
        low_bear = data[-2][2]
        close_bear = data[-2][3]
        body_bear = abs(open_bear - close_bear)
        lower_shadow_bear = close_bear - low_bear
        upper_shadow_bear = high_bear - open_bear

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = abs(close_bull - open_bull)
        lower_shadow_bull = open_bull - low_bull
        upper_shadow_bull = high_bull - close_bull

        if not body_bear > (high_bear - low_bear)*PIERCING_MARBOZU_BODY :
            return

        if not (close_bull > ((open_bear+close_bear)/2) and
                open_bull < close_bear) :
            return
        analytics_data["PATTERNS"]["PIERCING"] = 1
        self.SCORE += 1

    def chek_bullish_engulfing(self,
                               data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                               analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["BULLISH_ENGULFING"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bearish(-2, data) and
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data))) :
            return

        open_bear = data[-2][0]
        high_bear = data[-2][1]
        low_bear = data[-2][2]
        close_bear = data[-2][3]
        body_bear = abs(open_bear - close_bear)
        lower_shadow_bear = close_bear - low_bear
        upper_shadow_bear = high_bear - open_bear

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = abs(close_bull - open_bull)
        lower_shadow_bull = open_bull - low_bull
        upper_shadow_bull = high_bull - close_bull

        if not (close_bull >= open_bear and
                open_bull <= close_bear) :
            return
        analytics_data["PATTERNS"]["BULLISH_ENGULFING"] = 1
        self.SCORE += 1

    def chek_morning_star(self,
                          data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                          analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["MORNING_STAR"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bearish(-3, data) and
                (self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data) or
                 self.is_bearish_trend(-5, data))) :
            return

        open_bear = data[-3][0]
        high_bear = data[-3][1]
        low_bear = data[-3][2]
        close_bear = data[-3][3]
        body_bear = abs(open_bear - close_bear)
        lower_shadow_bear = close_bear - low_bear
        upper_shadow_bear = high_bear - open_bear

        open_dogi = data[-2][0]
        high_dogi = data[-2][1]
        low_dogi = data[-2][2]
        close_dogi = data[-2][3]
        body_dogi = abs(open_dogi - close_dogi)
        lower_shadow_dogi = min(open_dogi, close_dogi) - low_dogi
        upper_shadow_dogi = high_dogi - max(open_dogi, close_dogi)

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = abs(close_bull - open_bull)
        lower_shadow_bull = open_bull - low_bull
        upper_shadow_bull = high_bull - close_bull

        if not (body_dogi <= (high_dogi - low_dogi)*DOGI_BODY and
                max(open_dogi, close_dogi) < max(close_bear, open_bull)) :
            return
        analytics_data["PATTERNS"]["MORNING_STAR"] = 1
        self.SCORE += 1

    def three_white_soliders(self,
                             data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                             analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["THREE_WHITE_SOLIDERS"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bullish(-2, data) and
                self.is_bullish(-3, data) and
                (self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data) or
                 self.is_bearish_trend(-5, data))) :
            return

        open_bull_1 = data[-3][0]
        high_bull_1 = data[-3][1]
        low_bull_1 = data[-3][2]
        close_bull_1 = data[-3][3]
        body_bull_1 = abs(close_bull_1 - open_bull_1)

        open_bull_2 = data[-2][0]
        high_bull_2 = data[-2][1]
        low_bull_2 = data[-2][2]
        close_bull_2 = data[-2][3]
        body_bull_2 = abs(close_bull_2 - open_bull_2)


        open_bull_3 = data[-1][0]
        high_bull_3 = data[-1][1]
        low_bull_3 = data[-1][2]
        close_bull_3 = data[-1][3]
        body_bull_3 = abs(close_bull_3 - open_bull_3)

        if not (body_bull_1 > (high_bull_1-low_bull_1)*THREE_WHITE_SOLIDERS_BODY and
                body_bull_2 > (high_bull_2-low_bull_2)*THREE_WHITE_SOLIDERS_BODY and
                body_bull_3 > (high_bull_3-low_bull_3)*THREE_WHITE_SOLIDERS_BODY) :
            return
        if not (((open_bull_1+close_bull_1)/2 < open_bull_2 or
                 (open_bull_2+close_bull_2)/2 < open_bull_3)) :
            return
        if not (close_bull_1 < close_bull_2 < close_bull_3) :
            return
        analytics_data["PATTERNS"]["THREE_WHITE_SOLIDERS"] = 1
        self.SCORE += 1

    def chek_white_marubozu(self,
                            data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                            analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["WHITE_MARUBOZU"] = 0

        if not(self.is_bullish(-1, data) and
               (self.is_bearish_trend(-2, data) or
                self.is_bearish_trend(-3, data))) :
            return

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = abs(close_bull - open_bull)

        if not body_bull >= (high_bull - low_bull)*MARUBOZU_BODY :
            return
        analytics_data["PATTERNS"]["WHITE_MARUBOZU"] = 1
        self.SCORE += 1

    def chek_three_inside_up(self,
                             data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                             analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["THREE_INSIDE_UP"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bullish(-2, data) and
                self.is_bearish(-3, data) and
                (self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data) or
                 self.is_bearish_trend(-5, data))) :
            return

        open_bear = data[-3][0]
        high_bear = data[-3][1]
        low_bear = data[-3][2]
        close_bear = data[-3][3]
        body_bear = abs(open_bear - close_bear)

        open_bull_1 = data[-2][0]
        high_bull_1 = data[-2][1]
        low_bull_1 = data[-2][2]
        close_bull_1 = data[-2][3]
        body_bull_1 = abs(close_bull_1 - open_bull_1)

        open_bull_2 = data[-1][0]
        high_bull_2 = data[-1][1]
        low_bull_2 = data[-1][2]
        close_bull_2 = data[-1][3]
        body_bull_2 = abs(close_bull_2 - open_bull_2)

        if not body_bear >= (high_bear - low_bear)*THREE_INSIDE_UP_BEAR_BODY :
            return
        if not (open_bear > close_bull_1 and
                close_bear < open_bull_1 and
                open_bear > open_bull_2 > close_bear and
                close_bull_2 > close_bull_1) :
            return
        analytics_data["PATTERNS"]["THREE_INSIDE_UP"] = 1
        self.SCORE += 1

    def chek_bullish_harami(self,
                            data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                            analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["BULLISH_HARAMI"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bearish(-2, data) and
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data))) :
            return

        open_bear = data[-2][0]
        high_bear = data[-2][1]
        low_bear = data[-2][2]
        close_bear = data[-2][3]
        body_bear = abs(open_bear - close_bear)

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = abs(close_bull - open_bull)

        #if not body_bear >= (high_bear - low_bear)*BULLISH_HARAMI_BEAR_BODY :
        #    return
        if not (open_bear > close_bull and
                open_bull > close_bear) :
            return
        analytics_data["PATTERNS"]["BULLISH_HARAMI"] = 1
        self.SCORE += 1

    def chek_tweezer_bottom(self,
                            data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                            analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["TWEEZER_BOTTOM"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bearish(-2, data) and
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data))) :
            return

        open_bear = data[-2][0]
        high_bear = data[-2][1]
        low_bear = data[-2][2]
        close_bear = data[-2][3]
        body_bear = abs(open_bear - close_bear)

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = abs(close_bull - open_bull)

        if not abs(low_bear - low_bull) < CANDLESTICK_ANALYZER_DISCRETE_PARTS*TWEEZER_BOTTOM_SIMILARITY_RATIO :
            return
        analytics_data["PATTERNS"]["TWEEZER_BOTTOM"] = 1
        self.SCORE += 1

    def chek_inverted_hammer(self,
                             data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                             analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["INVERTED_HAMMER"] = 0

        if not (
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data))) :
            return

        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        body = abs(close - open)
        lower_shadow = min(open, close) - low
        upper_shadow = high - max(close, open)

        if not (lower_shadow <= (high-low)*INVERTED_HAMMER_LOWER_SHADOW and
                upper_shadow >= body*INVERTED_HAMMER_UPPER_SHADOW_FACTOR and
                body <= (high-low)*INVERTED_HAMMER_BODY) :
            return
        analytics_data["PATTERNS"]["INVERTED_HAMMER"] = 1
        self.SCORE += 1

    def chek_three_outside_up(self,
                              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["THREE_OUTSIDE_UP"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bullish(-2, data) and
                self.is_bearish(-3, data) and
                (self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data) or
                 self.is_bearish_trend(-5, data))) :
            return

        open_bear = data[-3][0]
        high_bear = data[-3][1]
        low_bear = data[-3][2]
        close_bear = data[-3][3]
        body_bear = abs(open_bear - close_bear)
        lower_shadow_bear = low_bear - close_bear
        upper_shadow_bear = high_bear - open_bear

        open_bull_1 = data[-2][0]
        high_bull_1 = data[-2][1]
        low_bull_1 = data[-2][2]
        close_bull_1 = data[-2][3]
        body_bull_1 = abs(close_bull_1 - open_bull_1)
        lower_shadow_bull_1 = open_bull_1 - low_bull_1
        upper_shadow_bull_1 = high_bull_1 - close_bull_1

        open_bull_2 = data[-1][0]
        high_bull_2 = data[-1][1]
        low_bull_2 = data[-1][2]
        close_bull_2 = data[-1][3]
        body_bull_2 = abs(close_bull_2 - open_bull_2)
        lower_shadow_bull_2 = open_bull_2 - low_bull_2
        upper_shadow_bull_2 = high_bull_2 - close_bull_2

        if not (close_bull_1 > open_bear and
                open_bull_1 < close_bear and
                body_bull_1 >= (high_bull_1-low_bull_1)*THREE_OUTSIDE_UP_BULL_BODY) :
            return
        if not (close_bull_2 > close_bull_1) :
            return
        analytics_data["PATTERNS"]["THREE_OUTSIDE_UP"] = 1
        self.SCORE += 1

    def chek_on_neck(self,
                     data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                     analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["ON_NECK"] = 0

        if not (self.is_bullish(-1, data) and
                self.is_bearish(-2, data) and
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data) or
                 self.is_bearish_trend(-4, data))) :
            return

        open_bear = data[-2][0]
        high_bear = data[-2][1]
        low_bear = data[-2][2]
        close_bear = data[-2][3]
        body_bear = abs(open_bear - close_bear)
        lower_shadow_bear = close_bear - low_bear
        upper_shadow_bear = high_bear - open_bear

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = abs(close_bull - open_bull)
        lower_shadow_bull = open_bull - low_bull
        upper_shadow_bull = high_bull - close_bull

        if not (abs(close_bear - close_bull) < CANDLESTICK_ANALYZER_DISCRETE_PARTS*ON_NECK_SIMILARITY_RATIO) :
            return
        analytics_data["PATTERNS"]["ON_NECK"] = 1
        self.SCORE += 1


    """#$$$$$$$$$$#"""
    """
    BEARISH TRENDS
    """
    def chek_hanging_man(self,
                         data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                         analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["HANGING_MAN"] = 0

        if not (
                (self.is_bullish_trend(-2, data) or
                 self.is_bullish_trend(-3, data))) :
            return

        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        body = abs(open - close)
        lower_shadow = min(close, open) - low
        upper_shadow = high - max(open, close)

        if not (upper_shadow <= (high-low)*HANGING_MAN_UPPER_SHADOW and
                lower_shadow >= body*HANDING_MAN_LOWER_SHADOW_FACTOR and
                body <= (high-low)*HANGING_MAN_BODY) :
            return
        analytics_data["PATTERNS"]["HANGING_MAN"] = 1
        self.SCORE -= 1

    def chek_dark_cloud_cover(self,
                              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["DARK_CLOUD_COVER"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bullish(-2, data) and
                (self.is_bullish_trend(-2, data) or
                 self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data))) :
            return

        open_bull = data[-1][0]
        high_bull = data[-1][1]
        low_bull = data[-1][2]
        close_bull = data[-1][3]
        body_bull = close_bull - open_bull
        lower_shadow_bull = open_bull - low_bull
        upper_shadow_bull = high_bull - close_bull

        open_bear = data[-2][0]
        high_bear = data[-2][1]
        low_bear = data[-2][2]
        close_bear = data[-2][3]
        body_bear = open_bear - close_bear
        lower_shadow_bear = close_bull - low_bull
        upper_shadow_bear = high_bull - open_bull

        if not (body_bull > (high_bull - low_bull)*DARK_CLOUD_COVER_BODY) :
            return

        if not (open_bear < ((open_bull+close_bull)/2) and
                open_bull < close_bear < close_bull) :
            return
        analytics_data["PATTERNS"]["DARK_CLOUD_COVER"] = 1
        self.SCORE -= 1

    def chek_bearish_engulfing(self,
                               data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                               analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["BEARISH_ENGULFING"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bullish(-2, data) and
                (self.is_bullish_trend(-2, data) or
                 self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data))) :
            return

        open_bull = data[-2][0]
        high_bull = data[-2][1]
        low_bull = data[-2][2]
        close_bull = data[-2][3]
        body_bull = abs(close_bull - open_bull)
        lower_shadow_bull = open_bull - low_bull
        upper_shadow_bull = high_bull - close_bull

        open_bear = data[-1][0]
        high_bear = data[-1][1]
        low_bear = data[-1][2]
        close_bear = data[-1][3]
        body_bear = abs(open_bear - close_bear)
        lower_shadow_bear = close_bear - low_bear
        upper_shadow_bear = high_bear - open_bear

        if not (close_bull <= open_bear and
                open_bull >= close_bear) :
            return
        analytics_data["PATTERNS"]["BEARISH_ENGULFING"] = 1
        self.SCORE -= 1

    def chek_evening_star(self,
                          data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                          analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["EVENING_STAR"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bearish(-3, data) and
                (self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data) or
                 self.is_bullish_trend(-5, data))) :
            return

        open_bull = data[-3][0]
        high_bull = data[-3][1]
        low_bull = data[-3][2]
        close_bull = data[-3][3]
        body_bull = abs(open_bull - close_bull)
        lower_shadow_bull = close_bull - low_bull
        upper_shadow_bull = high_bull - open_bull

        open_dogi = data[-2][0]
        high_dogi = data[-2][1]
        low_dogi = data[-2][2]
        close_dogi = data[-2][3]
        body_dogi = abs(open_dogi - close_dogi)
        lower_shadow_dogi = min(open_dogi, close_dogi) - low_dogi
        upper_shadow_dogi = high_dogi - max(open_dogi, close_dogi)

        open_bear = data[-1][0]
        high_bear = data[-1][1]
        low_bear = data[-1][2]
        close_bear = data[-1][3]
        body_bear = abs(close_bear - open_bear)
        lower_shadow_bear = open_bear - low_bear
        upper_shadow_bear = high_bear - close_bear

        if not (body_dogi <= (high_dogi - low_dogi)*DOGI_BODY and
                min(open_dogi, close_dogi) > min(close_bull, open_bear)) :
            return
        analytics_data["PATTERNS"]["EVENING_STAR"] = 1
        self.SCORE -= 1

    def chek_three_black_crows(self,
                               data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                               analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["THREE_BLACK_CROWS"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bearish(-2, data) and
                self.is_bearish(-3, data) and
                (self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data) or
                 self.is_bullish_trend(-5, data))) :
            return

        open_bear_1 = data[-3][0]
        high_bear_1 = data[-3][1]
        low_bear_1 = data[-3][2]
        close_bear_1 = data[-3][3]
        body_bear_1 = abs(open_bear_1 - close_bear_1)

        open_bear_2 = data[-2][0]
        high_bear_2 = data[-2][1]
        low_bear_2 = data[-2][2]
        close_bear_2 = data[-2][3]
        body_bear_2 = abs(open_bear_2 - close_bear_2)


        open_bear_3 = data[-1][0]
        high_bear_3 = data[-1][1]
        low_bear_3 = data[-1][2]
        close_bear_3 = data[-1][3]
        body_bear_3 = abs(open_bear_3 - close_bear_3)

        if not (body_bear_1 > (high_bear_1-low_bear_1)*THREE_BLACK_CROWS_BODY and
                body_bear_1 > (high_bear_2-low_bear_2)*THREE_BLACK_CROWS_BODY and
                body_bear_1 > (high_bear_3-low_bear_3)*THREE_BLACK_CROWS_BODY) :
            return
        if not ((open_bear_1+close_bear_1)/2 > open_bear_2 or
                (open_bear_2+close_bear_2)/2 > open_bear_3) :
            return
        if not (close_bear_1 > close_bear_2 > close_bear_3) :
            return
        analytics_data["PATTERNS"]["THREE_BLACK_CROWS"] = 1
        self.SCORE -= 1

    def chek_black_marubozu(self,
                            data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                            analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["BLACK_MARUBOZU"] = 0

        if not (self.is_bearish(-1, data) and
                (self.is_bullish_trend(-2, data) and
                 self.is_bullish_trend(-3, data))) :
            return

        open_bear = data[-1][0]
        high_bear = data[-1][1]
        low_bear = data[-1][2]
        close_bear = data[-1][3]
        body_bear = abs(open_bear - close_bear)

        if not body_bear >= (high_bear - low_bear)*MARUBOZU_BODY :
            return
        analytics_data["PATTERNS"]["BLACK_MARUBOZU"] = 1
        self.SCORE -= 1

    def chek_three_inside_down(self,
                               data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                               analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["THREE_INSIDE_DOWN"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bearish(-2, data) and
                self.is_bullish(-3, data) and
                (self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data) or
                 self.is_bullish_trend(-5, data))) :
            return

        open_bull = data[-3][0]
        high_bull = data[-3][1]
        low_bull = data[-3][2]
        close_bull = data[-3][3]
        body_bull = abs(close_bull - open_bull)

        open_bear_1 = data[-2][0]
        high_bear_1 = data[-2][1]
        low_bear_1 = data[-2][2]
        close_bear_1 = data[-2][3]
        body_bear_1 = abs(open_bear_1 - close_bear_1)

        open_bear_2 = data[-1][0]
        high_bear_2 = data[-1][1]
        low_bear_2 = data[-1][2]
        close_bear_2 = data[-1][3]
        body_bear_2 = abs(open_bear_2 - close_bear_2)

        if not body_bull >= (high_bull - low_bull)*THREE_INSIDE_DOWN_BULL_BODY :
            return
        if not (close_bull > open_bear_1 and
                close_bear_1 > open_bull and
                close_bull > open_bear_2 > open_bull and
                close_bear_2 < close_bear_1) :
            return
        analytics_data["PATTERNS"]["THREE_INSIDE_DOWN"] = 1
        self.SCORE -= 1

    def chek_bearish_harami(self,
                            data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                            analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["BEARISH_HARAMI"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bullish(-2, data) and
                (self.is_bullish_trend(-2, data) or
                 self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data))) :
            return

        open_bull = data[-2][0]
        high_bull = data[-2][1]
        low_bull = data[-2][2]
        close_bull = data[-2][3]
        body_bull = abs(close_bull - open_bull)

        open_bear = data[-1][0]
        high_bear = data[-1][1]
        low_bear = data[-1][2]
        close_bear = data[-1][3]
        body_bear = abs(open_bear - close_bear)

        #if not body_bull >= (high_bull - low_bull)*BEARISH_HARAMI_BEAR_BODY :
        #    return
        if not (open_bear < close_bull and
                open_bull < close_bear) :
            return
        analytics_data["PATTERNS"]["BEARISH_HARAMI"] = 1
        self.SCORE -= 1

    def chek_shooting_star(self,
                           data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                           analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["SHOOTING_STAR"] = 0

        if not (
                (self.is_bullish_trend(-2, data) or
                 self.is_bullish_trend(-3, data))) :
            return

        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        body = abs(open - close)
        lower_shadow = min(close, open) - low
        upper_shadow = high - max(open, close)

        if not (lower_shadow <= (high-low)*SHOOTING_STAR_LOWER_SHADOW and
                upper_shadow >= body*SHOOTING_STAR_UPPER_SHADOW_FACTOR and
                body <= (high-low)*SHOOTING_STAR_BODY) :
            return
        analytics_data["PATTERNS"]["SHOOTING_STAR"] = 1
        self.SCORE -= 1

    def chek_tweezer_top(self,
                         data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                         analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["TWEEZER_TOP"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bullish(-2, data) and
                (self.is_bullish_trend(-2, data) or
                 self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data))) :
            return

        open_bull = data[-2][0]
        high_bull = data[-2][1]
        low_bull = data[-2][2]
        close_bull = data[-2][3]
        body_bull = abs(close_bull - open_bull)

        open_bear = data[-1][0]
        high_bear = data[-1][1]
        low_bear = data[-1][2]
        close_bear = data[-1][3]
        body_bear = abs(open_bear - close_bear)

        if not abs(high_bull - high_bear) < CANDLESTICK_ANALYZER_DISCRETE_PARTS*TWEEZER_TOP_SIMILARITY_RATIO :
            return
        analytics_data["PATTERNS"]["TWEEZER_TOP"] = 1
        self.SCORE -= 1

    def chek_three_outside_down(self,
                                data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                                analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["PATTERNS"]["THREE_OUTSIDE_DOWN"] = 0

        if not (self.is_bearish(-1, data) and
                self.is_bearish(-2, data) and
                self.is_bullish(-3, data) and
                (self.is_bullish_trend(-3, data) or
                 self.is_bullish_trend(-4, data) or
                 self.is_bullish_trend(-5, data))) :
            return

        open_bull = data[-3][0]
        high_bull = data[-3][1]
        low_bull = data[-3][2]
        close_bull = data[-3][3]
        body_bull = abs(close_bull - open_bull)
        lower_shadow_bull = open_bull - low_bull
        upper_shadow_bull = high_bull - close_bull

        open_bear_1 = data[-2][0]
        high_bear_1 = data[-2][1]
        low_bear_1 = data[-2][2]
        close_bear_1 = data[-2][3]
        body_bear_1 = abs(open_bear_1 - close_bear_1)
        lower_shadow_bear_1 = close_bear_1 - low_bear_1
        upper_shadow_bear_1 = high_bear_1 - open_bear_1

        open_bear_2 = data[-1][0]
        high_bear_2 = data[-1][1]
        low_bear_2 = data[-1][2]
        close_bear_2 = data[-1][3]
        body_bear_2 = abs(open_bear_2 - close_bear_2)
        lower_shadow_bear_2 = close_bear_2 - low_bear_2
        upper_shadow_bear_2 = high_bear_2 - open_bear_2

        if not (open_bear_1 > close_bull and
                close_bear_1 < open_bull and
                body_bear_1 > (high_bull - low_bull)*THREE_OUTSIDE_DOWN_BEAR_BODY) :
            return
        if not (close_bear_2 < close_bear_1) :
            return
        analytics_data["PATTERNS"]["THREE_OUTSIDE_DOWN"] = 1
        self.SCORE -= 1


    """#$$$$$$$$$$#"""
    """
    103 CANDLES
    """
    """
    def chek_bearish_belt_hold(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["BEARISH_BELT_HOLD"] = 0
        if not (self.is_bearish(-1, data) and
                (self.is_bullish_trend(-2, data) or
                 self.is_bullish_trend(-3, data))) :
            return

        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        upper_shadow = high - open
        lower_shadow = close - low

        if not ( upper_shadow < (high - low)*BEARISH_BELT_HOLD_UPPER_SHADOW_FACTOR) :
            return
        if not (lower_shadow < (high - low)*BEARISH_BELT_HOLD_UPPER_SHADOW_FACTOR) :
            return

        analytics_data["BEARISH_BELT_HOLD"] = 1
        self.SCORE += BEARISH_BELT_HOLD_SCORE

    def chek_bullish_belt_hold(self,
                               data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                               analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["BULLISH_BELT_HOLD"] = 0
        if not (self.is_bullish(-1, data) and
                (self.is_bearish_trend(-2, data) or
                 self.is_bearish_trend(-3, data))) :
            return

        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        upper_shadow = high - close
        lower_shadow = open - low

        if not (upper_shadow < (high - low)*BULLISH_BELT_HOLD_UPPER_SHADOW_FACTOR) :
            return

        if not (lower_shadow < (high - low)*BULLISH_BELT_HOLD_LOWER_SHADOW_FACTOR) :
            return

        analytics_data["BULLISH_BELT_HOLD"] = 1
        self.SCORE += BULLISH_BELT_HOLD_SCORE

    def chek_black_candle(self,
                          data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                          analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["BLACK_CANDLE"] = 0
        if not (self.is_bearish(-1, data)) : return

        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        body = open - close
        upper_shadow = high - open
        lower_shadow = close - low

        #if not avarage_body_size : return
        if not (body > max(lower_shadow, upper_shadow)) : return

        analytics_data["BLACK_CANDLE"] = 1
        self.SCORE += BLACK_CANDLE_SCORE

    def chek_short_black_candle(self,
                                data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                                analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data["SHORT_BLACK_CANDLE"] = 0
        if not (self.is_bearish(-1, data)) : return

        open = data[-1][0]
        high = data[-1][1]
        low = data[-1][2]
        close = data[-1][3]
        body = open - close
        upper_shadow = high - open
        lower_shadow = close - low

        #if not short_body_size : retrun
        if not (body > max(lower_shadow, upper_shadow)) : return

        analytics_data["SHORT_BLACK_CANDLE"] = 1
        self.SCORE += SHORT_BLACK_CANDLE_SCORE

    def chek_short_white_candle(self,
                                data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                                analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1

    def chek_(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1

    def chek_(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1

    def chek_(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1

    def chek_(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1

    def chek_(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1

    def chek_(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1

    def chek_(self,
              data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
              analytics_data: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        analytics_data[""] = 0

        analytics_data[""] = 1
    """

    """#$$$$$$$$$$#"""
    """
    PROCESS SCORE DATA AND ANALYSIS_DICTIONARY
    """
    def process_score_and_analysis(self,
                                   data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT,
                                   analysis_dict: CANDLESTICK_ANALYZER_OUTPUT_FORMAT) -> None :
        if self.SCORE > 0 : analysis_dict["ANALYSIS"] = CANDLESTICK_ANALYZER_BUY
        elif self.SCORE < 0 : analysis_dict["ANALYSIS"] = CANDLESTICK_ANALYZER_SELL
        else : analysis_dict["ANALYSIS"] = CANDLESTICK_ANALYZER_REST

        if (self.is_bullish_trend(-2, data) or
            self.is_bullish_trend(-3, data)) :
            analysis_dict["CURRENT_TREND"] = CANDLESTICK_ANALYZER_BULLISH_TREND
        elif (self.is_bearish_trend(-2, data) or
              self.is_bearish_trend(-3, data)) :
            analysis_dict["CURRENT_TREND"] = CANDLESTICK_ANALYZER_BEARISH_TREND
        else : pass


    """#$$$$$$$$$$#"""
    """
    UTILITY FUNCTIONS
    """
    def is_bullish(self,
                   index: int,
                   data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT) -> bool :
        return data[index][3] >= data[index][0]

    def is_bearish(self,
                   index: int,
                   data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT) -> bool :
        return data[index][3] <= data[index][0]

    def is_bearish_trend(self,
                         index: int,
                         data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT) -> bool : ####################################
        bearish_count = 0
        for _ in range(index - CANDLESTICK_ANALYZER_CHECK_TREND_SAMPLES + 1, index+1) :
            if data[_][0] > data[_][3] : bearish_count += 1
        if bearish_count > CANDLESTICK_ANALYZER_CHECK_TREND_SAMPLES/2 :
            return True
        return False

    def is_bullish_trend(self,
                         index: int,
                         data: CANDLESTICK_ANALYZER_INTERNAL_FORMAT) -> bool : ####################################
        bullish_count = 0
        for _ in range(index - CANDLESTICK_ANALYZER_CHECK_TREND_SAMPLES + 1, index+1) :
            if data[_][0] <= data[_][3] : bullish_count += 1
        if bullish_count > CANDLESTICK_ANALYZER_CHECK_TREND_SAMPLES/2 :
            return True
        return False
