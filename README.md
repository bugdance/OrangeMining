### Orange PMT
    1.需VS2010，基于python34单独装。  
    2.orange单独装，并配置环境变量为orange下的pip。  
    3.安装最新的包，如numpy,scipy。  
    4.orange安装addons。  
    5.界面的修改在canvas下，登录主体main和follow。    
    6.凡是界面内容的修改在canvas下的application,图片在icons。    
    7.控件的在widgets下，目前改了的有data下的owlogis, owtable, owsave, owdatasampler, 特别是owlogis，把数据库单独提出放置在owedit下便于隐藏。  
    8.基于数据库链接自己的修改还包括了backend下的base和postgres。Base基于修改了限制个数，postgres修改了不强制转换类型。  
    9.打包的情况必须基于orange原生修改的文件，否则运行不了，安装install shield,按照说明一步步打包即可。  