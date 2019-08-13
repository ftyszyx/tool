#include "AssetsHelper.h"
#include "cocostudio/DictionaryHelper.h"
using namespace cocostudio;
NS_CC_EXT_BEGIN;
AssetElement::AssetElement()
{
}

AssetElement::~AssetElement()
{
	
}

static AssetsHelper* sharedAssertsHelper=NULL;

AssetsHelper::AssetsHelper()
{
}

AssetsHelper::~AssetsHelper()
{
	for( auto it=m_assetdic.begin(); it!=m_assetdic.end(); ++it ) {
		CC_SAFE_DELETE(it->second);
	}
	m_assetdic.clear();
}

AssetsHelper* AssetsHelper::getInstance()
{
	if (!sharedAssertsHelper)
	{
		sharedAssertsHelper = new AssetsHelper();
	}
	return sharedAssertsHelper;
}

bool AssetsHelper::LoadAssetsDict(const char* dictpath)
{
	//加载文件
	std::string jsonpath;
	jsonpath=CCFileUtils::getInstance()->fullPathForFilename(dictpath);
	std::string contentStr = FileUtils::getInstance()->getStringFromFile(jsonpath);
	if(contentStr=="")
	{
		return false;
	}
	rapidjson::Document jsonDict;
	jsonDict.Parse<0>(contentStr.c_str());
	if (jsonDict.HasParseError())
	{
		CCLOG("GetParseError %s\n",jsonDict.GetParseError());
		return false;
	}
	int piccount = DICTOOL->getArrayCount_json(jsonDict, "pictrues");

	for (int i=0; i<piccount; i++)
	{
		const rapidjson::Value& assertJson = DICTOOL->getDictionaryFromArray_json(jsonDict, "pictrues", i);
		AssetElement* element=new AssetElement();
		std::string elementName=DICTOOL->getStringValue_json(assertJson,"key");
		std::string elementPath=DICTOOL->getStringValue_json(assertJson,"path");
		AssetElement::AssetType elementtype=static_cast<AssetElement::AssetType>(DICTOOL->getIntValue_json(assertJson,"type"));
		element->setKeyName(elementName);
		element->setAssetPath(elementPath);
		element->setAssetType(elementtype);
		if(elementtype==AssetElement::NORMAL_PIC||elementtype==AssetElement::PLIST_PIC)
		{
			m_assetdic.insert(std::make_pair(elementName,element));
		}
		else
		{
			m_plistDic.insert(std::make_pair(elementName,element));
		}
		
	}
	CCLOG("piccount %d\n",piccount);
	return true;
}

std::string AssetsHelper::getAssertKey(const std::string& assertname)
{
	//取得资key名
	if(assertname.length()==0){return std::string("");}
	int  pos = assertname.find_last_of('/');
	if(pos== std::string::npos)
	{
		pos=-1;
	}
	int  dotpos = assertname.find_last_of('.');
	if(dotpos==std::string::npos)
	{
		dotpos=assertname.length();
	}
	return assertname.substr(pos+1,dotpos-pos-1);
}


AssetElement::AssetType AssetsHelper::getAssertType(std::string& assertKeyName)
{
	auto it =m_assetdic.find(assertKeyName);
	if (it!=m_assetdic.end())
	{
		//有此资源
		return it->second->getAssetType();
	}
	return AssetElement::UN_KNOW_TYPE;
}


AssetElement* AssetsHelper::getAssertInfo(const std::string& assertname)
{
	//取得资key名
	std::string assertkeyname = getAssertKey(assertname);
	//查找资源
	auto it =m_assetdic.find(assertkeyname);
	if (it!=m_assetdic.end())
	{
		return it->second;
	}
	return NULL;
}


AssetElement* AssetsHelper::getPlistAssertInfo(const std::string& plistName)
{
	//取得资key名
	std::string assertkeyname =getAssertKey(plistName);
	//查找资源
	auto it =m_plistDic.find(assertkeyname);
	if (it!=m_plistDic.end())
	{
		return it->second;
	}
	return NULL;
}



Texture2D * AssetsHelper::getAssertTexture(const std::string& assertname)
{
	AssetElement* element=getAssertInfo(assertname);
	if (element!=NULL)
	{
		AssetElement::AssetType pictype=element->getAssetType();
		if(pictype==AssetElement::NORMAL_PIC)
		{
			//普通的图片直接加载
			std::string elementpath=element->getAssetPath();
			return Director::getInstance()->getTextureCache()->addImage(elementpath);
		}
	}
	return NULL;
}


SpriteFrame * AssetsHelper::getPlistPicSpriteFrame(AssetElement* element)
{
	if(element==NULL)
	{
		return NULL;
	}
	AssetElement::AssetType pictype=element->getAssetType();
	if(pictype==AssetElement::PLIST_PIC)
	{
		std::string elementpath=element->getAssetPath();
		//plist图片
		auto plistit=m_plistDic.find(elementpath);
		if(plistit==m_plistDic.end())
		{
			return NULL;
		}
		std::string plistpath=plistit->second->getAssetPath();
		SpriteFrameCache *cache = SpriteFrameCache::getInstance();
		cache->addSpriteFramesWithFile(plistpath);
		return cache->getSpriteFrameByName(element->getKeyName());
	}
	return NULL;
}




NS_CC_EXT_END;