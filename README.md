# ArtilleryCalculator
基于python屏幕像素计算的战争雷霆曲射火力计算器。  
双击可执行文件后回到游戏窗口，在弹出的程序窗口中先输入游戏小地图比例尺在电脑屏幕上的实际像素数（可以通过qq或微信截图等截图工具简易测得），再输入当前地图比例尺的实际距离（如比例尺为1:255，则填写255）。  
全部输入后程序自动截图随后在截图的小地图位置点击目标位置以及火炮当前位置即可，如火炮位置变更或目标位置更换，点击右上角重新截图即可，由于程序为窗口化执行，所以只要窗口位置不会覆盖右下角游戏小地图即可。  
注：因计算方式依赖手动标注，且受游戏内手动标记误差以及游戏内地形的高低落差影响，即便经练习手动标点已十分准确，测得距离仍有可能因地形落差导致较大误差。请尽量在平原类地图或对相对高度差不大的目标进行测距。  
dist文件夹中已有两种预设好的可执行文件，ArtilleryCalc_4k.exe为针对4k屏幕做出的窗口调整。  
如想自行修改并运行.py文件，所需的环境依赖也在requirements中，作者使用anaconda做的环境控制，如没有类似工具则对照requirements手动pip install应该也行。
