# add all the constants in this file
# path to the folder where we will save the files
PATH = "./xmp_files"
# initialise list of properties
PROPERTIES_NAMES = [
    "Temperature",
    "Tint",
    "Exposure",
    "Contrast",
    "Highlights",
    "Shadows",
    "Whites",
    "Blacks",
    "Texture",
    "Clarity",
    "Dehaze",
    "Vibrance",
    "Saturation",
]

XMP_TEXT_FILE = [
    '''<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21        ">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:tiff="http://ns.adobe.com/tiff/1.0/"
    xmlns:exif="http://ns.adobe.com/exif/1.0/"
    xmlns:aux="http://ns.adobe.com/exif/1.0/aux/"
    xmlns:exifEX="http://cipa.jp/exif/1.0/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:crd="http://ns.adobe.com/camera-raw-defaults/1.0/"
    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
   tiff:Make="Panasonic"
   tiff:Model="DMC-GX80"
   tiff:Orientation="1"
   exif:ExifVersion="0230"
   exif:ExposureTime="1/1"
   exif:ShutterSpeedValue="0/1"
   exif:FNumber="8/1"
   exif:ApertureValue="6/1"
   exif:ExposureProgram="1"
   exif:ExposureBiasValue="0/100"
   exif:MaxApertureValue="928/256"
   exif:MeteringMode="2"
   exif:LightSource="9"
   exif:FocalLength="130/10"
   exif:SensingMethod="2"
   exif:FileSource="3"
   exif:SceneType="1"
   exif:FocalLengthIn35mmFilm="26"
   exif:CustomRendered="0"
   exif:ExposureMode="1"
   exif:WhiteBalance="1"
   exif:SceneCaptureType="0"
   exif:GainControl="1"
   exif:Contrast="0"
   exif:Saturation="0"
   exif:Sharpness="0"
   exif:DigitalZoomRatio="0/10"
   exif:FocalPlaneXResolution="86953287/32768"
   exif:FocalPlaneYResolution="86953287/32768"
   exif:FocalPlaneResolutionUnit="3"
   exif:DateTimeOriginal="2022-09-07T18:13:22.548"
   aux:SerialNumber="XFR2203070007"
   aux:Lens="LUMIX G VARIO 12-32/F3.5-5.6"
   aux:LensSerialNumber="02BX2182633A"
   exifEX:LensModel="LUMIX G VARIO 12-32/F3.5-5.6"
   xmp:ModifyDate="2022-09-07T18:13:22.548"
   xmp:CreateDate="2022-09-07T18:13:22.548"
   xmp:MetadataDate="2022-09-10T20:26:38+01:00"
   photoshop:DateCreated="2022-09-07T18:13:22.548"
   photoshop:SidecarForExtension="RW2"
   photoshop:EmbeddedXMPDigest="00000000000000000000000000000000"
   xmpMM:DocumentID="BE5F6B8356F986E92C7C8D5B9E463AE9"
   xmpMM:OriginalDocumentID="BE5F6B8356F986E92C7C8D5B9E463AE9"
   xmpMM:InstanceID="xmp.iid:f4c68e02-239d-1448-8c14-d643a2163436"
   dc:format="image/x-panasonic-raw"
   crd:CameraProfile="Camera Standard"
   crd:LookName=""
   crs:Version="13.3"
   crs:ProcessVersion="11.0"
   crs:WhiteBalance="Custom"
   crs:Temperature="''',
    '''"
   crs:Tint="''',
    '''"
   crs:Exposure2012="''',
    '''"
   crs:Contrast2012="''',
    '''"
   crs:Highlights2012="''',
    '''"
   crs:Shadows2012="''',
    '''"
   crs:Whites2012="''',
    '''"
   crs:Blacks2012="''',
    '''"
   crs:Texture="''',
    '''"
   crs:Clarity2012="''',
    '''"
   crs:Dehaze="''',
    '''"
   crs:Vibrance="''',
    '''"
   crs:Saturation="''',
]

XMP_FILE_END = """"
   crs:ParametricShadows="0"
   crs:ParametricDarks="0"
   crs:ParametricLights="0"
   crs:ParametricHighlights="0"
   crs:ParametricShadowSplit="25"
   crs:ParametricMidtoneSplit="50"
   crs:ParametricHighlightSplit="75"
   crs:Sharpness="40"
   crs:SharpenRadius="+1.0"
   crs:SharpenDetail="25"
   crs:SharpenEdgeMasking="0"
   crs:LuminanceSmoothing="0"
   crs:ColorNoiseReduction="25"
   crs:ColorNoiseReductionDetail="50"
   crs:ColorNoiseReductionSmoothness="50"
   crs:HueAdjustmentRed="0"
   crs:HueAdjustmentOrange="0"
   crs:HueAdjustmentYellow="0"
   crs:HueAdjustmentGreen="0"
   crs:HueAdjustmentAqua="0"
   crs:HueAdjustmentBlue="0"
   crs:HueAdjustmentPurple="0"
   crs:HueAdjustmentMagenta="0"
   crs:SaturationAdjustmentRed="0"
   crs:SaturationAdjustmentOrange="0"
   crs:SaturationAdjustmentYellow="0"
   crs:SaturationAdjustmentGreen="0"
   crs:SaturationAdjustmentAqua="0"
   crs:SaturationAdjustmentBlue="0"
   crs:SaturationAdjustmentPurple="0"
   crs:SaturationAdjustmentMagenta="0"
   crs:LuminanceAdjustmentRed="0"
   crs:LuminanceAdjustmentOrange="0"
   crs:LuminanceAdjustmentYellow="0"
   crs:LuminanceAdjustmentGreen="0"
   crs:LuminanceAdjustmentAqua="0"
   crs:LuminanceAdjustmentBlue="0"
   crs:LuminanceAdjustmentPurple="0"
   crs:LuminanceAdjustmentMagenta="0"
   crs:SplitToningShadowHue="0"
   crs:SplitToningShadowSaturation="0"
   crs:SplitToningHighlightHue="0"
   crs:SplitToningHighlightSaturation="0"
   crs:SplitToningBalance="0"
   crs:ColorGradeMidtoneHue="0"
   crs:ColorGradeMidtoneSat="0"
   crs:ColorGradeShadowLum="0"
   crs:ColorGradeMidtoneLum="0"
   crs:ColorGradeHighlightLum="0"
   crs:ColorGradeBlending="50"
   crs:ColorGradeGlobalHue="0"
   crs:ColorGradeGlobalSat="0"
   crs:ColorGradeGlobalLum="0"
   crs:AutoLateralCA="0"
   crs:LensProfileEnable="0"
   crs:LensManualDistortionAmount="0"
   crs:VignetteAmount="0"
   crs:DefringePurpleAmount="0"
   crs:DefringePurpleHueLo="30"
   crs:DefringePurpleHueHi="70"
   crs:DefringeGreenAmount="0"
   crs:DefringeGreenHueLo="40"
   crs:DefringeGreenHueHi="60"
   crs:PerspectiveUpright="0"
   crs:PerspectiveVertical="0"
   crs:PerspectiveHorizontal="0"
   crs:PerspectiveRotate="0.0"
   crs:PerspectiveAspect="0"
   crs:PerspectiveScale="100"
   crs:PerspectiveX="0.00"
   crs:PerspectiveY="0.00"
   crs:GrainAmount="0"
   crs:PostCropVignetteAmount="0"
   crs:ShadowTint="0"
   crs:RedHue="0"
   crs:RedSaturation="0"
   crs:GreenHue="0"
   crs:GreenSaturation="0"
   crs:BlueHue="0"
   crs:BlueSaturation="0"
   crs:OverrideLookVignette="False"
   crs:ToneCurveName2012="Linear"
   crs:CameraProfile="Adobe Standard"
   crs:CameraProfileDigest="80EBDCBF84887BDB948934721C1FA354"
   crs:HasSettings="True"
   crs:HasCrop="False"
   crs:AlreadyApplied="False">
   <exif:ISOSpeedRatings>
    <rdf:Seq>
     <rdf:li>200</rdf:li>
    </rdf:Seq>
   </exif:ISOSpeedRatings>
   <exif:Flash
    exif:Fired="False"
    exif:Return="0"
    exif:Mode="2"
    exif:Function="False"
    exif:RedEyeMode="False"/>
   <xmpMM:History>
    <rdf:Seq>
     <rdf:li
      stEvt:action="saved"
      stEvt:instanceID="xmp.iid:f4c68e02-239d-1448-8c14-d643a2163436"
      stEvt:when="2022-09-10T20:26:38+01:00"
      stEvt:softwareAgent="Adobe Photoshop Camera Raw 13.3 (Windows)"
      stEvt:changed="/metadata"/>
    </rdf:Seq>
   </xmpMM:History>
   <crs:ToneCurvePV2012>
    <rdf:Seq>
     <rdf:li>0, 0</rdf:li>
     <rdf:li>255, 255</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012>
   <crs:ToneCurvePV2012Red>
    <rdf:Seq>
     <rdf:li>0, 0</rdf:li>
     <rdf:li>255, 255</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012Red>
   <crs:ToneCurvePV2012Green>
    <rdf:Seq>
     <rdf:li>0, 0</rdf:li>
     <rdf:li>255, 255</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012Green>
   <crs:ToneCurvePV2012Blue>
    <rdf:Seq>
     <rdf:li>0, 0</rdf:li>
     <rdf:li>255, 255</rdf:li>
    </rdf:Seq>
   </crs:ToneCurvePV2012Blue>
   <crs:Look>
    <rdf:Description
     crs:Name="Adobe Color"
     crs:Amount="1.000000"
     crs:UUID="B952C231111CD8E0ECCF14B86BAA7077"
     crs:SupportsAmount="false"
     crs:SupportsMonochrome="false"
     crs:SupportsOutputReferred="false"
     crs:Copyright="© 2018 Adobe Systems, Inc.">
    <crs:Group>
     <rdf:Alt>
      <rdf:li xml:lang="x-default">Profiles</rdf:li>
     </rdf:Alt>
    </crs:Group>
    <crs:Parameters>
     <rdf:Description
      crs:Version="13.3"
      crs:ProcessVersion="11.0"
      crs:ConvertToGrayscale="False"
      crs:CameraProfile="Adobe Standard"
      crs:LookTable="E1095149FDB39D7A057BAB208837E2E1">
     <crs:ToneCurvePV2012>
      <rdf:Seq>
       <rdf:li>0, 0</rdf:li>
       <rdf:li>22, 16</rdf:li>
       <rdf:li>40, 35</rdf:li>
       <rdf:li>127, 127</rdf:li>
       <rdf:li>224, 230</rdf:li>
       <rdf:li>240, 246</rdf:li>
       <rdf:li>255, 255</rdf:li>
      </rdf:Seq>
     </crs:ToneCurvePV2012>
     <crs:ToneCurvePV2012Red>
      <rdf:Seq>
       <rdf:li>0, 0</rdf:li>
       <rdf:li>255, 255</rdf:li>
      </rdf:Seq>
     </crs:ToneCurvePV2012Red>
     <crs:ToneCurvePV2012Green>
      <rdf:Seq>
       <rdf:li>0, 0</rdf:li>
       <rdf:li>255, 255</rdf:li>
      </rdf:Seq>
     </crs:ToneCurvePV2012Green>
     <crs:ToneCurvePV2012Blue>
      <rdf:Seq>
       <rdf:li>0, 0</rdf:li>
       <rdf:li>255, 255</rdf:li>
      </rdf:Seq>
     </crs:ToneCurvePV2012Blue>
     </rdf:Description>
    </crs:Parameters>
    </rdf:Description>
   </crs:Look>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>"""
