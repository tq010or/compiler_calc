# A simple calculator 

This is a simple calculator when I try to recall my complier courses.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install calc.

```bash
pip install calc 
```

## Usage

```python
from calc import LexAnalysis, SyntaxAnalysis
# To highlight lexcial and syntax analysis
lex_analyser = LexAnalysis()
syntax_analyser = SyntaxAnalysis()

def calculate(expr, lex=lex_analyser, syn=syntax_analyser):
    expr_list = lex(expr)
    return syn(expr_list)

calculate('5+4*3^2') # 41
calculate('1/0') # ValueError
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)