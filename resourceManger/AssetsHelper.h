#ifndef _LIBEXTENSIONS_ASSERTSHELPER_H__
#define _LIBEXTENSIONS_ASSERTSHELPER_H__
#include "cocos2d.h"
#include "ExtensionMacros.h"


NS_CC_EXT_BEGIN
//һ����ԴԪ��
class AssetElement
{
public:
	enum AssetType
	{
		NORMAL_PIC=1,//������ͼƬ
		PLIST_FILe,//plist�ļ�
		PLIST_PIC,//��plist�е�ͼƬ
		UN_KNOW_TYPE//δ֪
	};
	AssetElement();
	~AssetElement();
	CC_SYNTHESIZE(AssetType,m_assetType,AssetType);
	CC_SYNTHESIZE_PASS_BY_REF(std::string,m_assetKeyName,KeyName);
	CC_SYNTHESIZE_PASS_BY_REF(std::string,m_assetPath,AssetPath);

};

//��Դ��
class AssetsHelper
{
public:
	AssetsHelper();
	~AssetsHelper();
	//��ȡʵ��
	static AssetsHelper*  getInstance();
	//������Դ�ļ���
	bool LoadAssetsDict(const char* dictpath);

	//��ȡ��Դ����
	AssetElement::AssetType getAssertType(std::string& assertname);

	//��ȡ��Դ��keyֵ
	static std::string getAssertKey(const std::string& assertname);


	//��ȡ��Դ��Ϣ(��m_assetdic��ȡ��
	AssetElement* getAssertInfo(const std::string& assertname);

	//��ȡplist��Դ��Ϣ(��m_plistDic��ȡ��
	AssetElement* getPlistAssertInfo(const std::string& plistName);


	//��ȡ����ֻ������ͨͼƬ
	Texture2D *getAssertTexture(const std::string& assertname);

	//��ȡplistͼƬ������
	SpriteFrame * getPlistPicSpriteFrame(AssetElement* element);

private:
	std::map<std::string,AssetElement*> m_assetdic;  //ͼƬ��Դ��
	std::map<std::string,AssetElement*> m_plistDic;//plist��Դ��
};
NS_CC_EXT_END;

#endif