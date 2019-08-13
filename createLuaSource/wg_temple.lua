----------------------------------------------------
--name:(页面模块名)
--@author:zyx
--@copyright:
--@release:  2014-05-30
----------------------------------------------------
local widgetBase = require("scenes/base_wg")
--模块的变量名
local (###)Wg = widgetBase:New()

local eventDispacher = require('common/event_dispacher')

--注册网络事件消息处理函数
function (###)Wg:initMessageLister()
    --todo:增加要监听的消息
	--注册一个消息(消息id,处理函数)
    eventDispacher:AddListener(tostring(_MSGID.COMMON_NEWERGUIDE_NTF),self.onNewerGuid,self)
end

--页面关闭处理函数
function (###)Wg:OnClose()
    self:OnCloseBase()
    --去掉消息注册信息
    eventDispacher:Remove(tostring(_MSGID.COMMON_NEWERGUIDE_NTF),self.onNewerGuid,self)
    --todo:增加自己的消除函数
end

--初始化
function (###)Wg:OnInit()
	--页面要加入的层
	local layer =  MainScene.windowsLayer
  
     --增加屏蔽(可以设置颜色及透明度)
    local masktemp= require("common/mask_layer")
    self.mask=masktemp:Create({r=0, g=0, b=0, opacity=125},self.OnClose,self)
    layer:addChild(self.mask)

    self:OnEnterBase(layer,"(***3)")

    MakeCenter(self.widget)--页面居中

    self:initView()--初始化cocostudio的页面元素
    --初始化事件监听
    self:initMessageLister()
    self:initAnimation()
    --todo：自己的初始化

end


--按键响应函数在此处声明
(***2)



function (###)Wg:initView()
	--todo:增加要使用的页面元素在此处声明
(***1)

end

--初始化动画
function (###)Wg:initAnimation()
    -- --初始化动画
    -- ccs.ArmatureDataManager:getInstance():addArmatureFileInfo("effect_action/mainscenes.ExportJson")
    -- local armature = ccs.Armature:create("mainscenes")
    -- self.widget:addChild(armature)
    -- armature:setPosition(cc.p(383,377))
    -- armature:getAnimation():play("qizi_left")
end

return (###)Wg