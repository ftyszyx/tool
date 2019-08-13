----------------------------------------------------
--name:(页面模块名)
--@author:zyx
--@copyright:
--@release:  2014-05-30
----------------------------------------------------

--模块的变量名
local (###)Wg = {}


function (###)Wg:New()
    local this = {}
    setmetatable(this,self)
    self.__index=self
    this:OnInit()
    return this
end

--初始化
function (###)Wg:OnInit()
    -- 加载cocostudio的json文件
    self.widget=ccs.GUIReader:getInstance():widgetFromJsonFile("(***3).json",true)

    self.view=ccs.GUIReader:getInstance():getWidgetTable()--用来存储需要使用的cocostudio的页面元素
    self:initView()--初始化cocostudio的页面元素
end


--按键响应函数在此处声明
(***2)



function (###)Wg:initView()
	--todo:增加要使用的页面元素在此处声明
(***1)

end


return (###)Wg