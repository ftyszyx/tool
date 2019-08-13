#ifndef _LIBEXTENSIONS_ASSERTSHELPER_H__
#define _LIBEXTENSIONS_ASSERTSHELPER_H__
#include "cocos2d.h"
#include "ExtensionMacros.h"


NS_CC_EXT_BEGIN
//一个资源元素
class AssetElement
{
public:
	enum AssetType
	{
		NORMAL_PIC=1,//正常的图片
		PLIST_FILe,//plist文件
		PLIST_PIC,//在plist中的图片
		UN_KNOW_TYPE//未知
	};
	AssetElement();
	~AssetElement();
	CC_SYNTHESIZE(AssetType,m_assetType,AssetType);
	CC_SYNTHESIZE_PASS_BY_REF(std::string,m_assetKeyName,KeyName);
	CC_SYNTHESIZE_PASS_BY_REF(std::string,m_assetPath,AssetPath);

};

//资源表
class AssetsHelper
{
public:
	AssetsHelper();
	~AssetsHelper();
	//获取实例
	static AssetsHelper*  getInstance();
	//加载资源文件表
	bool LoadAssetsDict(const char* dictpath);

	//获取资源类型
	AssetElement::AssetType getAssertType(std::string& assertname);

	//获取资源的key值
	static std::string getAssertKey(const std::string& assertname);


	//获取资源信息(从m_assetdic获取）
	AssetElement* getAssertInfo(const std::string& assertname);

	//获取plist资源信息(从m_plistDic获取）
	AssetElement* getPlistAssertInfo(const std::string& plistName);


	//获取纹理只能是普通图片
	Texture2D *getAssertTexture(const std::string& assertname);

	//获取plist图片的纹理
	SpriteFrame * getPlistPicSpriteFrame(AssetElement* element);

private:
	std::map<std::string,AssetElement*> m_assetdic;  //图片资源表
	std::map<std::string,AssetElement*> m_plistDic;//plist资源表
};
NS_CC_EXT_END;

#endif