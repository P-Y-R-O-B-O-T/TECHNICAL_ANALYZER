# CANDLESTICK AND INDICATOR ANALYSIS FOR STOCKMARKET ANALYSIS FOR SHORT TERM

![](ZZZ/ZZZ.jpg)

* [PROJECT LINK GITHUB](https://github.com/P-Y-R-O-B-O-T/TECHNICAL_ANALYZER)

<!--- * [PROJECT LINK PYPI](https://pypi.org/project/TECHNICAL-ANALYZER-P-Y-R-O-B-O-T) --->

* A candlestick analyser for stocks and crypto currencies.

* Candle stick analysis made easy to understand.

* Get powerful insights using only 4 parameters.

* Just pass the data and get insights of all candlestick patterns, no need to check for any particular pattern, all are provided at a single function call.

* Also get free from checking for conformational indicators to buy or sell a unit or many, all the conformational indicators are also provided in the same call.

* Get all the info on your terminal

* Simple usage, no complex UI

# COMPATIBILITY

* Works on all os

* Python 3.10 and above

# INSTALLATION

> Install using cloning and pasting it in the python lib directory or local project directory.

<!--- * Goto [PYPI](https://pypi.org/project/TECHNICAL-ANALYZER-P-Y-R-O-B-O-T/) --->

# HOW TO USE

* Call import the package

* Create object

* Call function

* Pass ohlc data for 30 days in function call

```python
# import the package
from TECHNICAL_ANALYSIS.TECHNICAL_ANALYSIS.technical_analysis import *

#$$$$$$$$$$#

# LENGTH OF OPEN, HIGH, LOW, CLOSE MUST BE AT LEAST 21
# LENGTH OF OPEN, HIGH, LOW, CLOSE MUST BE SAME
DATA = {"OPEN": [26.799999237060547,
                 21.600000381469727,
                 21.850000381469727,
                 21.200000762939453,
                 23.149999618530273,
                 23.450000762939453,
                 23.899999618530273,
                 23.399999618530273,
                 22.25,
                 23.450000762939453,
                 22.5,
                 21.350000381469727,
                 22.0,
                 22.049999237060547,
                 21.950000762939453,
                 22.299999237060547,
                 22.450000762939453,
                 22.0,
                 22.0,
                 22.100000381469727,
                 22.25,
                 22.0,
                 21.399999618530273],

        "HIGH": [26.799999237060547,
                 22.700000762939453,
                 22.200000762939453,
                 22.049999237060547,
                 23.149999618530273,
                 24.200000762939453,
                 24.75,
                 23.399999618530273,
                 23.350000381469727,
                 23.450000762939453,
                 22.700000762939453,
                 22.0,
                 22.799999237060547,
                 22.5,
                 22.350000381469727,
                 22.299999237060547,
                 22.450000762939453,
                 22.350000381469727,
                 22.399999618530273,
                 22.399999618530273,
                 22.5,
                 22.299999237060547,
                 22.25],

        "LOW": [21.049999237060547,
                20.899999618530273,
                20.899999618530273,
                20.100000381469727,
                21.5,
                23.25,
                22.899999618530273,
                22.200000762939453,
                22.25,
                21.850000381469727,
                21.049999237060547,
                20.399999618530273,
                21.5,
                21.299999237060547,
                21.799999237060547,
                21.5,
                21.549999237060547,
                21.600000381469727,
                22.0,
                21.549999237060547,
                21.700000762939453,
                21.600000381469727,
                21.399999618530273],

        "CLOSE": [21.649999618530273,
                  21.549999237060547,
                  21.0,
                  22.049999237060547,
                  23.049999237060547,
                  23.899999618530273,
                  23.0,
                  22.75,
                  22.850000381469727,
                  22.049999237060547,
                  21.399999618530273,
                  21.899999618530273,
                  22.299999237060547,
                  21.899999618530273,
                  21.950000762939453,
                  22.0,
                  21.950000762939453,
                  22.0,
                  22.100000381469727,
                  22.25,
                  22.0,
                  21.75,
                  21.799999237060547]}

#$$$$$$$$$$#

# CREATE OBJ
TECHNICAL_ANALYSIS_OBJ = TECHNICAL_ANALYSIS()

# CALL FUNCTION
ANALYSIS_DATA = TECHNICAL_ANALYSIS_OBJ.analyze(DATA)

# PRINT DATA
print(ANALYSIS_DATA)
```
