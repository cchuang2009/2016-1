[![PyPI version]](https://badge.fury.io/py/japanize-matplotlib)
# tw_matplotlib
matplotlib 繁體中文化

## 使用方法
Import package after matplotlib.lib imported

```python
import matplotlib.pyplot as plt
import tw_matplotlib

plt.plot([1, 2, 3, 4])
plt.xlabel('繁體中文測試')
plt.show()