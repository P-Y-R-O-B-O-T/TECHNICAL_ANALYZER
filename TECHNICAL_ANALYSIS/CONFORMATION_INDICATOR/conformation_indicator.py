from ..CONSTANTS.constants import *

#$$$$$$$$$$#

class CONFORMATION_INDICATOR :
    def __init__(self) -> None :
        pass

    def overall_indications(self,interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
                            data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_OUTPUT_FORMAT :
        result = {}
        result["SCHOCASTIC_OSCILLATOR"] = self.schocastic_oscillator(interval_list,
                                                                     data)
        result["RSI"] = self.rsi(interval_list,
                                 data)
        return result

    def sma(self,
            interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
            data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_SMA_DATA_FORMAT :
        pass

    def ema(self,
            interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
            data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_EMA_DATA_FORMAT :
        pass

    def schocastic_oscillator(self,
                              interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
                              data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_SCHOCASTIC_OSCILLATOR_DATA_FORMAT :
        result = {}
        for _ in interval_list :
            result[_] = ( (data["CLOSE"][-1]-
                           min(data["LOW"][-_:]))/(max(data["HIGH"][-_:])
                                                   -min(data["LOW"][-_:])+CONFORMATION_INDICATOR_AVOID_ZERO) )*100
        return result

    def rsi(self,
            interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
            data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_RSI_DATA_FORMAT :
        result = {}
        for _ in interval_list :
            profit_perc = 0
            loss_perc = 0
            for __ in range(-_, -1) :
                if data["CLOSE"][__] > data["CLOSE"][__-1] :
                    profit_perc += (data["CLOSE"][__]/data["CLOSE"][__-1]) - 1
                if data["CLOSE"][__] < data["CLOSE"][__-1] :
                    loss_perc += 1 - (data["CLOSE"][__]/data["CLOSE"][__-1])
            current_gain = (data["CLOSE"][-1]/data["CLOSE"][-2]) - 1
            current_loss = 1 - (data["CLOSE"][-1]/data["CLOSE"][-2])
            avg_profit_perc = profit_perc/_
            avg_loss_perc = loss_perc/_
            rsi_step_1 = 100 - ( 100/( 1 + ( avg_profit_perc/(avg_loss_perc+CONFORMATION_INDICATOR_AVOID_ZERO) ) ) )
            rsi_step_2 = 100 - ( 100/( 1 + ( (avg_profit_perc*(_ - 1)+
                                              current_gain)/(avg_loss_perc*(_ - 1)+
                                                             current_loss+
                                                             CONFORMATION_INDICATOR_AVOID_ZERO) ) ) )
            result[_] = {"STEP_1": rsi_step_1,
                         "STEP_2": rsi_step_2}
        return result

    def average_true_range(self,
                           interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
                           data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_AVERAGE_TRUE_RANGE_DATA_FORMAT :
        pass

    def boilinger_bands(self,
                        interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
                        data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_BOILINGER_BANDS_DATA_FORMAT :
        pass

    def on_balance_volume(self,
                          interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
                          data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_ON_BALALNCE_VOLUME_DATA_FORMAT :
        pass

    def chaikin_oscillator(self,
                           interval_list: CONFORMATION_INDICATOR_INTERVAL_LIST_FORMAT,
                           data: CONFORMATION_INDICATOR_INPUT_DATA_FORMAT) -> CONFORMATION_INDICATOR_CHAIKIN_OSCILLATOR_DATA_FORMAT :
        pass
