Shader "Custom/Diffuse Texture" {
	Properties {
		_MainColor ("Main Color", Color) = (0,0,1,0.5)//_Name("Display Name", type) = defaultValue[{options}]
		_Texture ("Texture", 2D) = "white" {}
	}
	SubShader {
		Tags { "RenderType"="Opaque" }//非透明物体时 Transparent透明物体
		LOD 200  //Quality Settings中可以设置最大lod,当设定值 比200小，这个shader会不可用
		
		CGPROGRAM //开始标记
		#pragma surface surf Lambert  //#pragma surface( 声明的是一个表面着色器) surfaceFunction(着色器代码的方法的名字) lightModel [optionalparams](使用的光照模型)

		sampler2D _MainTex;

		//定义input结构
		struct Input {
			float2 uv_MainTex; //uv值 其实就是两个代表贴图上点的二维坐标 
		};
		//SurfaceOutput定义 half和我们常见float与double类似，都表示浮点数，只不过精度不一样。也许你很熟悉单精度浮点数（float或者single）和双精

		//度浮点数（double），这里的half指的是半精度浮点数
		//struct SurfaceOutput {
		//    half3 Albedo;     //像素的颜色
		//    half3 Normal;     //像素的法向值
		//    half3 Emission;   //像素的发散颜色
		//    half Specular;    //像素的镜面高光
		//    half Gloss;       //像素的发光强度
		//    half Alpha;       //像素的透明度
		//};

		void surf (Input IN, inout SurfaceOutput o) {
			half4 c = tex2D (_MainTex, IN.uv_MainTex);//tex2d函数，这是CG程序中用来在一张贴图中对一个点进行采样的方法，返回一个float4
			o.Albedo = c.rgb;
			o.Alpha = c.a;
		}
		ENDCG //结束
	} 
	FallBack "Diffuse"
}
