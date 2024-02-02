from ..CANDLESTICK_ANALYZER.candlestick_analyzer import CANDLESTICK_ANALYZER
from ..CONFORMATION_INDICATOR.conformation_indicator import CONFORMATION_INDICATOR
from ..CONSTANTS.constants import *

#$$$$$$$$$$#

class TECHNICAL_ANALYSIS :
    def __init__(self) -> None :
        self.CANDLESTICK_ANALYZER_OBJ = CANDLESTICK_ANALYZER()
        self.CONFORMATION_INDICATOR_OBJ = CONFORMATION_INDICATOR()

    def analyze(self,
                data: dict[str: list[ float ] ]) -> dict :
        temp = {}
        for _ in CANDLESTICK_ANALYZER_INPUT :
            temp[_] = data[_]
        candlestick_analysis = self.CANDLESTICK_ANALYZER_OBJ.analyze_candlestick_patterns(temp)
        indicators = self.CONFORMATION_INDICATOR_OBJ.overall_indications(MARKET_ANALYSIS_INTERVALS,
                                                                         temp)
        result = {_: MARKET_ANALYSIS_REST for _ in MARKET_ANALYSIS_INTERVALS}
        if not candlestick_analysis : return result
        if candlestick_analysis["ANALYSIS"] == "BUY" :
            for _ in MARKET_ANALYSIS_INTERVALS :
                if not ((indicators["SCHOCASTIC_OSCILLATOR"][_] < MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_BUY_THREASHOLD and
                         indicators["RSI"][_]["STEP_2"] < MARKET_ANALYSIS_RSI_SELL_THREASHOLD) or
                        (indicators["RSI"][_]["STEP_2"] < MARKET_ANALYSIS_RSI_BUY_THREASHOLD and
                         indicators["SCHOCASTIC_OSCILLATOR"][_] < MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_SELL_THREASHOLD)) :
                    continue
                result[_] = MARKET_ANALYSIS_BUY
            return result

        if candlestick_analysis["ANALYSIS"] == "SELL" :
            for _ in MARKET_ANALYSIS_INTERVALS :
                if not ((indicators["SCHOCASTIC_OSCILLATOR"][_] > MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_SELL_THREASHOLD and
                         indicators["RSI"][_]["STEP_2"] > MARKET_ANALYSIS_RSI_BUY_THREASHOLD) or
                        (indicators["RSI"][_]["STEP_2"] > MARKET_ANALYSIS_RSI_SELL_THREASHOLD and
                         indicators["SCHOCASTIC_OSCILLATOR"][_] > MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_BUY_THREASHOLD)) :
                    continue
                result[_] = MARKET_ANALYSIS_SELL
            return result

        for _ in MARKET_ANALYSIS_INTERVALS :
            if ((indicators["SCHOCASTIC_OSCILLATOR"][_] < MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_BUY_THREASHOLD and
                 indicators["RSI"][_]["STEP_2"] < MARKET_ANALYSIS_RSI_SELL_THREASHOLD) or
                (indicators["RSI"][_]["STEP_2"] < MARKET_ANALYSIS_RSI_BUY_THREASHOLD and
                 indicators["SCHOCASTIC_OSCILLATOR"][_] < MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_SELL_THREASHOLD)) :
                result[_] = MARKET_ANALYSIS_BUY
            if ((indicators["SCHOCASTIC_OSCILLATOR"][_] > MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_SELL_THREASHOLD and
                 indicators["RSI"][_]["STEP_2"] > MARKET_ANALYSIS_RSI_BUY_THREASHOLD) or
                (indicators["RSI"][_]["STEP_2"] > MARKET_ANALYSIS_RSI_SELL_THREASHOLD and
                 indicators["SCHOCASTIC_OSCILLATOR"][_] > MARKET_ANALYSIS_SCHOCASTIC_OSCILLATOR_BUY_THREASHOLD)) :
                result[_] = MARKET_ANALYSIS_SELL
        return result
