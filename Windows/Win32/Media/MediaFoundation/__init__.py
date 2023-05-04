from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Devices.Properties
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D12
import Windows.Win32.Graphics.Direct3D9
import Windows.Win32.Graphics.Dxgi.Common
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Media.Audio
import Windows.Win32.Media.DxMediaObjects
import Windows.Win32.Media.MediaFoundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Variant
import Windows.Win32.System.WinRT
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AACMFTEncoder = Guid('{93af0c51-2275-45d2-a35b-f2ba21caed00}')
AEC_INPUT_STREAM = Int32
AEC_CAPTURE_STREAM: AEC_INPUT_STREAM = 0
AEC_REFERENCE_STREAM: AEC_INPUT_STREAM = 1
AEC_SYSTEM_MODE = Int32
SINGLE_CHANNEL_AEC: AEC_SYSTEM_MODE = 0
ADAPTIVE_ARRAY_ONLY: AEC_SYSTEM_MODE = 1
OPTIBEAM_ARRAY_ONLY: AEC_SYSTEM_MODE = 2
ADAPTIVE_ARRAY_AND_AEC: AEC_SYSTEM_MODE = 3
OPTIBEAM_ARRAY_AND_AEC: AEC_SYSTEM_MODE = 4
SINGLE_CHANNEL_NSAGC: AEC_SYSTEM_MODE = 5
MODE_NOT_SET: AEC_SYSTEM_MODE = 6
AEC_VAD_MODE = Int32
AEC_VAD_DISABLED: AEC_VAD_MODE = 0
AEC_VAD_NORMAL: AEC_VAD_MODE = 1
AEC_VAD_FOR_AGC: AEC_VAD_MODE = 2
AEC_VAD_FOR_SILENCE_SUPPRESSION: AEC_VAD_MODE = 3
ALawCodecWrapper = Guid('{36cb6e0c-78c1-42b2-9943-846262f31786}')
class AM_MEDIA_TYPE(EasyCastStructure):
    majortype: Guid
    subtype: Guid
    bFixedSizeSamples: Windows.Win32.Foundation.BOOL
    bTemporalCompression: Windows.Win32.Foundation.BOOL
    lSampleSize: UInt32
    formattype: Guid
    pUnk: Windows.Win32.System.Com.IUnknown_head
    cbFormat: UInt32
    pbFormat: POINTER(Byte)
class ASF_FLAT_PICTURE(EasyCastStructure):
    bPictureType: Byte
    dwDataLen: UInt32
    _pack_ = 1
class ASF_FLAT_SYNCHRONISED_LYRICS(EasyCastStructure):
    bTimeStampFormat: Byte
    bContentType: Byte
    dwLyricsLen: UInt32
    _pack_ = 1
class ASF_INDEX_DESCRIPTOR(EasyCastStructure):
    Identifier: Windows.Win32.Media.MediaFoundation.ASF_INDEX_IDENTIFIER
    cPerEntryBytes: UInt16
    szDescription: Char * 32
    dwInterval: UInt32
class ASF_INDEX_IDENTIFIER(EasyCastStructure):
    guidIndexType: Guid
    wStreamNumber: UInt16
class ASF_MUX_STATISTICS(EasyCastStructure):
    cFramesWritten: UInt32
    cFramesDropped: UInt32
ASF_SELECTION_STATUS = Int32
ASF_STATUS_NOTSELECTED: ASF_SELECTION_STATUS = 0
ASF_STATUS_CLEANPOINTSONLY: ASF_SELECTION_STATUS = 1
ASF_STATUS_ALLDATAUNITS: ASF_SELECTION_STATUS = 2
ASF_STATUSFLAGS = Int32
ASF_STATUSFLAGS_INCOMPLETE: ASF_STATUSFLAGS = 1
ASF_STATUSFLAGS_NONFATAL_ERROR: ASF_STATUSFLAGS = 2
class AecQualityMetrics_Struct(EasyCastStructure):
    i64Timestamp: Int64
    ConvergenceFlag: Byte
    MicClippedFlag: Byte
    MicSilenceFlag: Byte
    PstvFeadbackFlag: Byte
    SpkClippedFlag: Byte
    SpkMuteFlag: Byte
    GlitchFlag: Byte
    DoubleTalkFlag: Byte
    uGlitchCount: UInt32
    uMicClipCount: UInt32
    fDuration: Single
    fTSVariance: Single
    fTSDriftRate: Single
    fVoiceLevel: Single
    fNoiseLevel: Single
    fERLE: Single
    fAvgERLE: Single
    dwReserved: UInt32
MF_VERSION: UInt32 = 131184
MEDIASUBTYPE_None: Guid = Guid('{e436eb8e-524f-11ce-9f53-0020af0ba770}')
MEDIATYPE_Video: Guid = Guid('{73646976-0000-0010-8000-00aa00389b71}')
MEDIATYPE_Audio: Guid = Guid('{73647561-0000-0010-8000-00aa00389b71}')
MEDIATYPE_Text: Guid = Guid('{73747874-0000-0010-8000-00aa00389b71}')
MEDIATYPE_Midi: Guid = Guid('{7364696d-0000-0010-8000-00aa00389b71}')
MEDIATYPE_Stream: Guid = Guid('{e436eb83-524f-11ce-9f53-0020af0ba770}')
MEDIATYPE_Interleaved: Guid = Guid('{73766169-0000-0010-8000-00aa00389b71}')
MEDIATYPE_File: Guid = Guid('{656c6966-0000-0010-8000-00aa00389b71}')
MEDIATYPE_ScriptCommand: Guid = Guid('{73636d64-0000-0010-8000-00aa00389b71}')
MEDIATYPE_AUXLine21Data: Guid = Guid('{670aea80-3a82-11d0-b79b-00aa003767a7}')
MEDIATYPE_AUXTeletextPage: Guid = Guid('{11264acb-37de-4eba-8c35-7f04a1a68332}')
MEDIATYPE_CC_CONTAINER: Guid = Guid('{aeb312e9-3357-43ca-b701-97ec198e2b62}')
MEDIATYPE_DTVCCData: Guid = Guid('{fb77e152-53b2-499c-b46b-509fc33edfd7}')
MEDIATYPE_MSTVCaption: Guid = Guid('{b88b8a89-b049-4c80-adcf-5898985e22c1}')
MEDIATYPE_VBI: Guid = Guid('{f72a76e1-eb0a-11d0-ace4-0000c0cc16ba}')
MEDIASUBTYPE_DVB_SUBTITLES: Guid = Guid('{34ffcbc3-d5b3-4171-9002-d4c60301697f}')
MEDIASUBTYPE_ISDB_CAPTIONS: Guid = Guid('{059dd67d-2e55-4d41-8d1b-01f5e4f50607}')
MEDIASUBTYPE_ISDB_SUPERIMPOSE: Guid = Guid('{36dc6d28-f1a6-4216-9048-9cfcefeb5eba}')
MEDIATYPE_Timecode: Guid = Guid('{0482dee3-7817-11cf-8a03-00aa006ecb65}')
MEDIATYPE_LMRT: Guid = Guid('{74726c6d-0000-0010-8000-00aa00389b71}')
MEDIATYPE_URL_STREAM: Guid = Guid('{736c7275-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_CLPL: Guid = Guid('{4c504c43-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_YUYV: Guid = Guid('{56595559-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IYUV: Guid = Guid('{56555949-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_YVU9: Guid = Guid('{39555659-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Y411: Guid = Guid('{31313459-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Y41P: Guid = Guid('{50313459-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_YUY2: Guid = Guid('{32595559-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_YVYU: Guid = Guid('{55595659-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_UYVY: Guid = Guid('{59565955-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Y211: Guid = Guid('{31313259-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_CLJR: Guid = Guid('{524a4c43-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IF09: Guid = Guid('{39304649-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_CPLA: Guid = Guid('{414c5043-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MJPG: Guid = Guid('{47504a4d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_TVMJ: Guid = Guid('{4a4d5654-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WAKE: Guid = Guid('{454b4157-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_CFCC: Guid = Guid('{43434643-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IJPG: Guid = Guid('{47504a49-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Plum: Guid = Guid('{6d756c50-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_DVCS: Guid = Guid('{53435644-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_H264: Guid = Guid('{34363248-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_DVSD: Guid = Guid('{44535644-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MDVF: Guid = Guid('{4656444d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RGB1: Guid = Guid('{e436eb78-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_RGB4: Guid = Guid('{e436eb79-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_RGB8: Guid = Guid('{e436eb7a-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_RGB565: Guid = Guid('{e436eb7b-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_RGB555: Guid = Guid('{e436eb7c-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_RGB24: Guid = Guid('{e436eb7d-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_RGB32: Guid = Guid('{e436eb7e-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_ARGB1555: Guid = Guid('{297c55af-e209-4cb3-b757-c76d6b9c88a8}')
MEDIASUBTYPE_ARGB4444: Guid = Guid('{6e6415e6-5c24-425f-93cd-80102b3d1cca}')
MEDIASUBTYPE_ARGB32: Guid = Guid('{773c9ac0-3274-11d0-b724-00aa006c1a01}')
MEDIASUBTYPE_A2R10G10B10: Guid = Guid('{2f8bb76d-b644-4550-acf3-d30caa65d5c5}')
MEDIASUBTYPE_A2B10G10R10: Guid = Guid('{576f7893-bdf6-48c4-875f-ae7b81834567}')
MEDIASUBTYPE_AYUV: Guid = Guid('{56555941-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_AI44: Guid = Guid('{34344941-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IA44: Guid = Guid('{34344149-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RGB32_D3D_DX7_RT: Guid = Guid('{32335237-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RGB16_D3D_DX7_RT: Guid = Guid('{36315237-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_ARGB32_D3D_DX7_RT: Guid = Guid('{38384137-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_ARGB4444_D3D_DX7_RT: Guid = Guid('{34344137-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_ARGB1555_D3D_DX7_RT: Guid = Guid('{35314137-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RGB32_D3D_DX9_RT: Guid = Guid('{32335239-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RGB16_D3D_DX9_RT: Guid = Guid('{36315239-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_ARGB32_D3D_DX9_RT: Guid = Guid('{38384139-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_ARGB4444_D3D_DX9_RT: Guid = Guid('{34344139-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_ARGB1555_D3D_DX9_RT: Guid = Guid('{35314139-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_YV12: Guid = Guid('{32315659-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_NV12: Guid = Guid('{3231564e-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_NV11: Guid = Guid('{3131564e-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_P208: Guid = Guid('{38303250-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_P210: Guid = Guid('{30313250-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_P216: Guid = Guid('{36313250-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_P010: Guid = Guid('{30313050-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_P016: Guid = Guid('{36313050-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Y210: Guid = Guid('{30313259-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Y216: Guid = Guid('{36313259-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_P408: Guid = Guid('{38303450-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_NV24: Guid = Guid('{3432564e-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_420O: Guid = Guid('{4f303234-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IMC1: Guid = Guid('{31434d49-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IMC2: Guid = Guid('{32434d49-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IMC3: Guid = Guid('{33434d49-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IMC4: Guid = Guid('{34434d49-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_S340: Guid = Guid('{30343353-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_S342: Guid = Guid('{32343353-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Overlay: Guid = Guid('{e436eb7f-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_MPEG1Packet: Guid = Guid('{e436eb80-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_MPEG1Payload: Guid = Guid('{e436eb81-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_MPEG1AudioPayload: Guid = Guid('{00000050-0000-0010-8000-00aa00389b71}')
MEDIATYPE_MPEG1SystemStream: Guid = Guid('{e436eb82-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_MPEG1System: Guid = Guid('{e436eb84-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_MPEG1VideoCD: Guid = Guid('{e436eb85-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_MPEG1Video: Guid = Guid('{e436eb86-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_MPEG1Audio: Guid = Guid('{e436eb87-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_Avi: Guid = Guid('{e436eb88-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_Asf: Guid = Guid('{3db80f90-9412-11d1-aded-0000f8754b99}')
MEDIASUBTYPE_QTMovie: Guid = Guid('{e436eb89-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_QTRpza: Guid = Guid('{617a7072-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_QTSmc: Guid = Guid('{20636d73-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_QTRle: Guid = Guid('{20656c72-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_QTJpeg: Guid = Guid('{6765706a-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_PCMAudio_Obsolete: Guid = Guid('{e436eb8a-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_PCM: Guid = Guid('{00000001-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WAVE: Guid = Guid('{e436eb8b-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_AU: Guid = Guid('{e436eb8c-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_AIFF: Guid = Guid('{e436eb8d-524f-11ce-9f53-0020af0ba770}')
MEDIASUBTYPE_dvhd: Guid = Guid('{64687664-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_dvsl: Guid = Guid('{6c737664-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_dv25: Guid = Guid('{35327664-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_dv50: Guid = Guid('{30357664-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_dvh1: Guid = Guid('{31687664-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Line21_BytePair: Guid = Guid('{6e8d4a22-310c-11d0-b79a-00aa003767a7}')
MEDIASUBTYPE_Line21_GOPPacket: Guid = Guid('{6e8d4a23-310c-11d0-b79a-00aa003767a7}')
MEDIASUBTYPE_Line21_VBIRawData: Guid = Guid('{6e8d4a24-310c-11d0-b79a-00aa003767a7}')
MEDIASUBTYPE_708_608Data: Guid = Guid('{0af414bc-4ed2-445e-9839-8f095568ab3c}')
MEDIASUBTYPE_DtvCcData: Guid = Guid('{f52addaa-36f0-43f5-95ea-6d866484262a}')
MEDIASUBTYPE_CC_CONTAINER: Guid = Guid('{7ea626db-54da-437b-be9f-f73073adfa3c}')
MEDIASUBTYPE_TELETEXT: Guid = Guid('{f72a76e3-eb0a-11d0-ace4-0000c0cc16ba}')
MEDIASUBTYPE_VBI: Guid = Guid('{663da43c-03e8-4e9a-9cd5-bf11ed0def76}')
MEDIASUBTYPE_WSS: Guid = Guid('{2791d576-8e7a-466f-9e90-5d3f3083738b}')
MEDIASUBTYPE_XDS: Guid = Guid('{01ca73e3-dce6-4575-afe1-2bf1c902caf3}')
MEDIASUBTYPE_VPS: Guid = Guid('{a1b3f620-9792-4d8d-81a4-86af25772090}')
MEDIASUBTYPE_DRM_Audio: Guid = Guid('{00000009-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_IEEE_FLOAT: Guid = Guid('{00000003-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_DOLBY_AC3_SPDIF: Guid = Guid('{00000092-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RAW_SPORT: Guid = Guid('{00000240-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_SPDIF_TAG_241h: Guid = Guid('{00000241-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_DssVideo: Guid = Guid('{a0af4f81-e163-11d0-bad9-00609744111a}')
MEDIASUBTYPE_DssAudio: Guid = Guid('{a0af4f82-e163-11d0-bad9-00609744111a}')
MEDIASUBTYPE_VPVideo: Guid = Guid('{5a9b6a40-1a22-11d1-bad9-00609744111a}')
MEDIASUBTYPE_VPVBI: Guid = Guid('{5a9b6a41-1a22-11d1-bad9-00609744111a}')
CLSID_CaptureGraphBuilder: Guid = Guid('{bf87b6e0-8c27-11d0-b3f0-00aa003761c5}')
CLSID_CaptureGraphBuilder2: Guid = Guid('{bf87b6e1-8c27-11d0-b3f0-00aa003761c5}')
CLSID_ProtoFilterGraph: Guid = Guid('{e436ebb0-524f-11ce-9f53-0020af0ba770}')
CLSID_SystemClock: Guid = Guid('{e436ebb1-524f-11ce-9f53-0020af0ba770}')
CLSID_FilterMapper: Guid = Guid('{e436ebb2-524f-11ce-9f53-0020af0ba770}')
CLSID_FilterGraph: Guid = Guid('{e436ebb3-524f-11ce-9f53-0020af0ba770}')
CLSID_FilterGraphNoThread: Guid = Guid('{e436ebb8-524f-11ce-9f53-0020af0ba770}')
CLSID_FilterGraphPrivateThread: Guid = Guid('{a3ecbc41-581a-4476-b693-a63340462d8b}')
CLSID_MPEG1Doc: Guid = Guid('{e4bbd160-4269-11ce-838d-00aa0055595a}')
CLSID_FileSource: Guid = Guid('{701722e0-8ae3-11ce-a85c-00aa002feab5}')
CLSID_MPEG1PacketPlayer: Guid = Guid('{26c25940-4ca9-11ce-a828-00aa002feab5}')
CLSID_MPEG1Splitter: Guid = Guid('{336475d0-942a-11ce-a870-00aa002feab5}')
CLSID_CMpegVideoCodec: Guid = Guid('{feb50740-7bef-11ce-9bd9-0000e202599c}')
CLSID_CMpegAudioCodec: Guid = Guid('{4a2286e0-7bef-11ce-9bd9-0000e202599c}')
CLSID_TextRender: Guid = Guid('{e30629d3-27e5-11ce-875d-00608cb78066}')
CLSID_InfTee: Guid = Guid('{f8388a40-d5bb-11d0-be5a-0080c706568e}')
CLSID_AviSplitter: Guid = Guid('{1b544c20-fd0b-11ce-8c63-00aa0044b51e}')
CLSID_AviReader: Guid = Guid('{1b544c21-fd0b-11ce-8c63-00aa0044b51e}')
CLSID_VfwCapture: Guid = Guid('{1b544c22-fd0b-11ce-8c63-00aa0044b51e}')
CLSID_CaptureProperties: Guid = Guid('{1b544c22-fd0b-11ce-8c63-00aa0044b51f}')
CLSID_FGControl: Guid = Guid('{e436ebb4-524f-11ce-9f53-0020af0ba770}')
CLSID_MOVReader: Guid = Guid('{44584800-f8ee-11ce-b2d4-00dd01101b85}')
CLSID_QuickTimeParser: Guid = Guid('{d51bd5a0-7548-11cf-a520-0080c77ef58a}')
CLSID_QTDec: Guid = Guid('{fdfe9681-74a3-11d0-afa7-00aa00b67a42}')
CLSID_AVIDoc: Guid = Guid('{d3588ab0-0781-11ce-b03a-0020af0ba770}')
CLSID_VideoRenderer: Guid = Guid('{70e102b0-5556-11ce-97c0-00aa0055595a}')
CLSID_Colour: Guid = Guid('{1643e180-90f5-11ce-97d5-00aa0055595a}')
CLSID_Dither: Guid = Guid('{1da08500-9edc-11cf-bc10-00aa00ac74f6}')
CLSID_ModexRenderer: Guid = Guid('{07167665-5011-11cf-bf33-00aa0055595a}')
CLSID_AudioRender: Guid = Guid('{e30629d1-27e5-11ce-875d-00608cb78066}')
CLSID_AudioProperties: Guid = Guid('{05589faf-c356-11ce-bf01-00aa0055595a}')
CLSID_DSoundRender: Guid = Guid('{79376820-07d0-11cf-a24d-0020afd79767}')
CLSID_AudioRecord: Guid = Guid('{e30629d2-27e5-11ce-875d-00608cb78066}')
CLSID_AudioInputMixerProperties: Guid = Guid('{2ca8ca52-3c3f-11d2-b73d-00c04fb6bd3d}')
CLSID_AVIDec: Guid = Guid('{cf49d4e0-1115-11ce-b03a-0020af0ba770}')
CLSID_AVIDraw: Guid = Guid('{a888df60-1e90-11cf-ac98-00aa004c0fa9}')
CLSID_ACMWrapper: Guid = Guid('{6a08cf80-0e18-11cf-a24d-0020afd79767}')
CLSID_AsyncReader: Guid = Guid('{e436ebb5-524f-11ce-9f53-0020af0ba770}')
CLSID_URLReader: Guid = Guid('{e436ebb6-524f-11ce-9f53-0020af0ba770}')
CLSID_PersistMonikerPID: Guid = Guid('{e436ebb7-524f-11ce-9f53-0020af0ba770}')
CLSID_AVICo: Guid = Guid('{d76e2820-1563-11cf-ac98-00aa004c0fa9}')
CLSID_FileWriter: Guid = Guid('{8596e5f0-0da5-11d0-bd21-00a0c911ce86}')
CLSID_AviDest: Guid = Guid('{e2510970-f137-11ce-8b67-00aa00a3f1a6}')
CLSID_AviMuxProptyPage: Guid = Guid('{c647b5c0-157c-11d0-bd23-00a0c911ce86}')
CLSID_AviMuxProptyPage1: Guid = Guid('{0a9ae910-85c0-11d0-bd42-00a0c911ce86}')
CLSID_AVIMIDIRender: Guid = Guid('{07b65360-c445-11ce-afde-00aa006c14f4}')
CLSID_WMAsfReader: Guid = Guid('{187463a0-5bb7-11d3-acbe-0080c75e246e}')
CLSID_WMAsfWriter: Guid = Guid('{7c23220e-55bb-11d3-8b16-00c04fb6bd3d}')
CLSID_MPEG2Demultiplexer: Guid = Guid('{afb6c280-2c41-11d3-8a60-0000f81e0e4a}')
CLSID_MPEG2Demultiplexer_NoClock: Guid = Guid('{687d3367-3644-467a-adfe-6cd7a85c4a2c}')
CLSID_MMSPLITTER: Guid = Guid('{3ae86b20-7be8-11d1-abe6-00a0c905f375}')
CLSID_StreamBufferSink: Guid = Guid('{2db47ae5-cf39-43c2-b4d6-0cd8d90946f4}')
CLSID_SBE2Sink: Guid = Guid('{e2448508-95da-4205-9a27-7ec81e723b1a}')
CLSID_StreamBufferSource: Guid = Guid('{c9f5fe02-f851-4eb5-99ee-ad602af1e619}')
CLSID_StreamBufferConfig: Guid = Guid('{fa8a68b2-c864-4ba2-ad53-d3876a87494b}')
CLSID_StreamBufferPropertyHandler: Guid = Guid('{e37a73f8-fb01-43dc-914e-aaee76095ab9}')
CLSID_StreamBufferThumbnailHandler: Guid = Guid('{713790ee-5ee1-45ba-8070-a1337d2762fa}')
CLSID_Mpeg2VideoStreamAnalyzer: Guid = Guid('{6cfad761-735d-4aa5-8afc-af91a7d61eba}')
CLSID_StreamBufferRecordingAttributes: Guid = Guid('{ccaa63ac-1057-4778-ae92-1206ab9acee6}')
CLSID_StreamBufferComposeRecording: Guid = Guid('{d682c4ba-a90a-42fe-b9e1-03109849c423}')
CLSID_SBE2File: Guid = Guid('{93a094d7-51e8-485b-904a-8d6b97dc6b39}')
CLSID_DVVideoCodec: Guid = Guid('{b1b77c00-c3e4-11cf-af79-00aa00b67a42}')
CLSID_DVVideoEnc: Guid = Guid('{13aa3650-bb6f-11d0-afb9-00aa00b67a42}')
CLSID_DVSplitter: Guid = Guid('{4eb31670-9fc6-11cf-af6e-00aa00b67a42}')
CLSID_DVMux: Guid = Guid('{129d7e40-c10d-11d0-afb9-00aa00b67a42}')
CLSID_SeekingPassThru: Guid = Guid('{060af76c-68dd-11d0-8fc1-00c04fd9189d}')
CLSID_Line21Decoder: Guid = Guid('{6e8d4a20-310c-11d0-b79a-00aa003767a7}')
CLSID_Line21Decoder2: Guid = Guid('{e4206432-01a1-4bee-b3e1-3702c8edc574}')
CLSID_CCAFilter: Guid = Guid('{3d07a539-35ca-447c-9b05-8d85ce924f9e}')
CLSID_OverlayMixer: Guid = Guid('{cd8743a1-3736-11d0-9e69-00c04fd7c15b}')
CLSID_VBISurfaces: Guid = Guid('{814b9800-1c88-11d1-bad9-00609744111a}')
CLSID_WSTDecoder: Guid = Guid('{70bc06e0-5666-11d3-a184-00105aef9f33}')
CLSID_MjpegDec: Guid = Guid('{301056d0-6dff-11d2-9eeb-006008039e37}')
CLSID_MJPGEnc: Guid = Guid('{b80ab0a0-7416-11d2-9eeb-006008039e37}')
CLSID_SystemDeviceEnum: Guid = Guid('{62be5d10-60eb-11d0-bd3b-00a0c911ce86}')
CLSID_CDeviceMoniker: Guid = Guid('{4315d437-5b8c-11d0-bd3b-00a0c911ce86}')
CLSID_VideoInputDeviceCategory: Guid = Guid('{860bb310-5d01-11d0-bd3b-00a0c911ce86}')
CLSID_CVidCapClassManager: Guid = Guid('{860bb310-5d01-11d0-bd3b-00a0c911ce86}')
CLSID_LegacyAmFilterCategory: Guid = Guid('{083863f1-70de-11d0-bd40-00a0c911ce86}')
CLSID_CQzFilterClassManager: Guid = Guid('{083863f1-70de-11d0-bd40-00a0c911ce86}')
CLSID_VideoCompressorCategory: Guid = Guid('{33d9a760-90c8-11d0-bd43-00a0c911ce86}')
CLSID_CIcmCoClassManager: Guid = Guid('{33d9a760-90c8-11d0-bd43-00a0c911ce86}')
CLSID_AudioCompressorCategory: Guid = Guid('{33d9a761-90c8-11d0-bd43-00a0c911ce86}')
CLSID_CAcmCoClassManager: Guid = Guid('{33d9a761-90c8-11d0-bd43-00a0c911ce86}')
CLSID_AudioInputDeviceCategory: Guid = Guid('{33d9a762-90c8-11d0-bd43-00a0c911ce86}')
CLSID_CWaveinClassManager: Guid = Guid('{33d9a762-90c8-11d0-bd43-00a0c911ce86}')
CLSID_AudioRendererCategory: Guid = Guid('{e0f158e1-cb04-11d0-bd4e-00a0c911ce86}')
CLSID_CWaveOutClassManager: Guid = Guid('{e0f158e1-cb04-11d0-bd4e-00a0c911ce86}')
CLSID_MidiRendererCategory: Guid = Guid('{4efe2452-168a-11d1-bc76-00c04fb9453b}')
CLSID_CMidiOutClassManager: Guid = Guid('{4efe2452-168a-11d1-bc76-00c04fb9453b}')
CLSID_TransmitCategory: Guid = Guid('{cc7bfb41-f175-11d1-a392-00e0291f3959}')
CLSID_DeviceControlCategory: Guid = Guid('{cc7bfb46-f175-11d1-a392-00e0291f3959}')
CLSID_ActiveMovieCategories: Guid = Guid('{da4e3da0-d07d-11d0-bd50-00a0c911ce86}')
CLSID_DVDHWDecodersCategory: Guid = Guid('{2721ae20-7e70-11d0-a5d6-28db04c10000}')
CLSID_MediaEncoderCategory: Guid = Guid('{7d22e920-5ca9-4787-8c2b-a6779bd11781}')
CLSID_MediaMultiplexerCategory: Guid = Guid('{236c9559-adce-4736-bf72-bab34e392196}')
CLSID_FilterMapper2: Guid = Guid('{cda42200-bd88-11d0-bd4e-00a0c911ce86}')
CLSID_MemoryAllocator: Guid = Guid('{1e651cc0-b199-11d0-8212-00c04fc32c45}')
CLSID_MediaPropertyBag: Guid = Guid('{cdbd8d00-c193-11d0-bd4e-00a0c911ce86}')
CLSID_DvdGraphBuilder: Guid = Guid('{fcc152b7-f372-11d0-8e00-00c04fd7c08b}')
CLSID_DVDNavigator: Guid = Guid('{9b8c4620-2c1a-11d0-8493-00a02438ad48}')
CLSID_DVDState: Guid = Guid('{f963c5cf-a659-4a93-9638-caf3cd277d13}')
CLSID_SmartTee: Guid = Guid('{cc58e280-8aa1-11d1-b3f1-00aa003761c5}')
CLSID_DtvCcFilter: Guid = Guid('{fb056ba0-2502-45b9-8e86-2b40de84ad29}')
CLSID_CaptionsFilter: Guid = Guid('{2f7ee4b6-6ff5-4eb4-b24a-2bfc41117171}')
CLSID_SubtitlesFilter: Guid = Guid('{9f22cfea-ce07-41ab-8ba0-c7364af90af9}')
CLSID_DirectShowPluginControl: Guid = Guid('{8670c736-f614-427b-8ada-bbadc587194b}')
FORMAT_None: Guid = Guid('{0f6417d6-c318-11d0-a43f-00a0c9223196}')
FORMAT_VideoInfo: Guid = Guid('{05589f80-c356-11ce-bf01-00aa0055595a}')
FORMAT_VideoInfo2: Guid = Guid('{f72a76a0-eb0a-11d0-ace4-0000c0cc16ba}')
FORMAT_WaveFormatEx: Guid = Guid('{05589f81-c356-11ce-bf01-00aa0055595a}')
FORMAT_MPEGVideo: Guid = Guid('{05589f82-c356-11ce-bf01-00aa0055595a}')
FORMAT_MPEGStreams: Guid = Guid('{05589f83-c356-11ce-bf01-00aa0055595a}')
FORMAT_DvInfo: Guid = Guid('{05589f84-c356-11ce-bf01-00aa0055595a}')
FORMAT_525WSS: Guid = Guid('{c7ecf04d-4582-4869-9abb-bfb523b62edf}')
CLSID_DirectDrawProperties: Guid = Guid('{944d4c00-dd52-11ce-bf0e-00aa0055595a}')
CLSID_PerformanceProperties: Guid = Guid('{59ce6880-acf8-11cf-b56e-0080c7c4b68a}')
CLSID_QualityProperties: Guid = Guid('{418afb70-f8b8-11ce-aac6-0020af0b99a3}')
CLSID_VPObject: Guid = Guid('{ce292861-fc88-11d0-9e69-00c04fd7c15b}')
CLSID_VPVBIObject: Guid = Guid('{814b9801-1c88-11d1-bad9-00609744111a}')
CLSID_DVDecPropertiesPage: Guid = Guid('{101193c0-0bfe-11d0-af91-00aa00b67a42}')
CLSID_DVEncPropertiesPage: Guid = Guid('{4150f050-bb6f-11d0-afb9-00aa00b67a42}')
CLSID_DVMuxPropertyPage: Guid = Guid('{4db880e0-c10d-11d0-afb9-00aa00b67a42}')
CLSID_WstDecoderPropertyPage: Guid = Guid('{04e27f80-91e4-11d3-a184-00105aef9f33}')
FORMAT_AnalogVideo: Guid = Guid('{0482dde0-7817-11cf-8a03-00aa006ecb65}')
MEDIATYPE_AnalogVideo: Guid = Guid('{0482dde1-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_NTSC_M: Guid = Guid('{0482dde2-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_B: Guid = Guid('{0482dde5-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_D: Guid = Guid('{0482dde6-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_G: Guid = Guid('{0482dde7-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_H: Guid = Guid('{0482dde8-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_I: Guid = Guid('{0482dde9-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_M: Guid = Guid('{0482ddea-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_N: Guid = Guid('{0482ddeb-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_PAL_N_COMBO: Guid = Guid('{0482ddec-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_SECAM_B: Guid = Guid('{0482ddf0-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_SECAM_D: Guid = Guid('{0482ddf1-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_SECAM_G: Guid = Guid('{0482ddf2-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_SECAM_H: Guid = Guid('{0482ddf3-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_SECAM_K: Guid = Guid('{0482ddf4-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_SECAM_K1: Guid = Guid('{0482ddf5-7817-11cf-8a03-00aa006ecb65}')
MEDIASUBTYPE_AnalogVideo_SECAM_L: Guid = Guid('{0482ddf6-7817-11cf-8a03-00aa006ecb65}')
MEDIATYPE_AnalogAudio: Guid = Guid('{0482dee1-7817-11cf-8a03-00aa006ecb65}')
FORMAT_CAPTIONED_H264VIDEO: Guid = Guid('{a4efc024-873e-4da3-898b-474ddbd79fd0}')
FORMAT_CC_CONTAINER: Guid = Guid('{50997a4a-e508-4054-a2b2-10ff0ac1a69a}')
CAPTION_FORMAT_ATSC: Guid = Guid('{3ed9cb31-fd10-4ade-bccc-fb9105d2f3ef}')
CAPTION_FORMAT_DVB: Guid = Guid('{12230db4-ff2a-447e-bb88-6841c416d068}')
CAPTION_FORMAT_DIRECTV: Guid = Guid('{e9ca1ce7-915e-47be-9bb9-bf1d8a13a5ec}')
CAPTION_FORMAT_ECHOSTAR: Guid = Guid('{ebb1a262-1158-4b99-ae80-92ac776952c4}')
FORMAT_CAPTIONED_MPEG2VIDEO: Guid = Guid('{7ab2ada2-81b6-4f14-b3c8-d0c486393b67}')
TIME_FORMAT_NONE: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
TIME_FORMAT_FRAME: Guid = Guid('{7b785570-8c82-11cf-bc0c-00aa00ac74f6}')
TIME_FORMAT_BYTE: Guid = Guid('{7b785571-8c82-11cf-bc0c-00aa00ac74f6}')
TIME_FORMAT_SAMPLE: Guid = Guid('{7b785572-8c82-11cf-bc0c-00aa00ac74f6}')
TIME_FORMAT_FIELD: Guid = Guid('{7b785573-8c82-11cf-bc0c-00aa00ac74f6}')
TIME_FORMAT_MEDIA_TIME: Guid = Guid('{7b785574-8c82-11cf-bc0c-00aa00ac74f6}')
AMPROPSETID_Pin: Guid = Guid('{9b00f101-1567-11d1-b3f1-00aa003761c5}')
PIN_CATEGORY_CAPTURE: Guid = Guid('{fb6c4281-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_PREVIEW: Guid = Guid('{fb6c4282-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_ANALOGVIDEOIN: Guid = Guid('{fb6c4283-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_VBI: Guid = Guid('{fb6c4284-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_VIDEOPORT: Guid = Guid('{fb6c4285-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_NABTS: Guid = Guid('{fb6c4286-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_EDS: Guid = Guid('{fb6c4287-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_TELETEXT: Guid = Guid('{fb6c4288-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_CC: Guid = Guid('{fb6c4289-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_STILL: Guid = Guid('{fb6c428a-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_TIMECODE: Guid = Guid('{fb6c428b-0353-11d1-905f-0000c0cc16ba}')
PIN_CATEGORY_VIDEOPORT_VBI: Guid = Guid('{fb6c428c-0353-11d1-905f-0000c0cc16ba}')
LOOK_UPSTREAM_ONLY: Guid = Guid('{ac798be0-98e3-11d1-b3f1-00aa003761c5}')
LOOK_DOWNSTREAM_ONLY: Guid = Guid('{ac798be1-98e3-11d1-b3f1-00aa003761c5}')
CLSID_TVTunerFilterPropertyPage: Guid = Guid('{266eee41-6c63-11cf-8a03-00aa006ecb65}')
CLSID_CrossbarFilterPropertyPage: Guid = Guid('{71f96461-78f3-11d0-a18c-00a0c9118956}')
CLSID_TVAudioFilterPropertyPage: Guid = Guid('{71f96463-78f3-11d0-a18c-00a0c9118956}')
CLSID_VideoProcAmpPropertyPage: Guid = Guid('{71f96464-78f3-11d0-a18c-00a0c9118956}')
CLSID_CameraControlPropertyPage: Guid = Guid('{71f96465-78f3-11d0-a18c-00a0c9118956}')
CLSID_AnalogVideoDecoderPropertyPage: Guid = Guid('{71f96466-78f3-11d0-a18c-00a0c9118956}')
CLSID_VideoStreamConfigPropertyPage: Guid = Guid('{71f96467-78f3-11d0-a18c-00a0c9118956}')
CLSID_AudioRendererAdvancedProperties: Guid = Guid('{37e92a92-d9aa-11d2-bf84-8ef2b1555aed}')
CLSID_VideoMixingRenderer: Guid = Guid('{b87beb7b-8d29-423f-ae4d-6582c10175ac}')
CLSID_VideoRendererDefault: Guid = Guid('{6bc1cffa-8fc1-4261-ac22-cfb4cc38db50}')
CLSID_AllocPresenter: Guid = Guid('{99d54f63-1a69-41ae-aa4d-c976eb3f0713}')
CLSID_AllocPresenterDDXclMode: Guid = Guid('{4444ac9e-242e-471b-a3c7-45dcd46352bc}')
CLSID_VideoPortManager: Guid = Guid('{6f26a6cd-967b-47fd-874a-7aed2c9d25a2}')
CLSID_VideoMixingRenderer9: Guid = Guid('{51b4abf3-748f-4e3b-a276-c828330e926a}')
CLSID_EnhancedVideoRenderer: Guid = Guid('{fa10746c-9b63-4b6c-bc49-fc300ea5f256}')
CLSID_MFVideoMixer9: Guid = Guid('{e474e05a-ab65-4f6a-827c-218b1baaf31f}')
CLSID_MFVideoPresenter9: Guid = Guid('{98455561-5136-4d28-ab08-4cee40ea2781}')
CLSID_EVRTearlessWindowPresenter9: Guid = Guid('{a0a7a57b-59b2-4919-a694-add0a526c373}')
CLSID_EVRPlaybackPipelineOptimizer: Guid = Guid('{62079164-233b-41f8-a80f-f01705f514a8}')
EVRConfig_ForceBob: Guid = Guid('{e447df01-10ca-4d17-b17e-6a840f8a3a4c}')
EVRConfig_ForceThrottle: Guid = Guid('{e447df03-10ca-4d17-b17e-6a840f8a3a4c}')
EVRConfig_ForceHalfInterlace: Guid = Guid('{e447df05-10ca-4d17-b17e-6a840f8a3a4c}')
EVRConfig_ForceScaling: Guid = Guid('{e447df07-10ca-4d17-b17e-6a840f8a3a4c}')
EVRConfig_ForceBatching: Guid = Guid('{e447df09-10ca-4d17-b17e-6a840f8a3a4c}')
CLSID_NetworkProvider: Guid = Guid('{b2f3a67c-29da-4c78-8831-091ed509a475}')
CLSID_ATSCNetworkProvider: Guid = Guid('{0dad2fdd-5fd7-11d3-8f50-00c04f7971e2}')
CLSID_ATSCNetworkPropertyPage: Guid = Guid('{e3444d16-5ac4-4386-88df-13fd230e1dda}')
CLSID_DVBSNetworkProvider: Guid = Guid('{fa4b375a-45b4-4d45-8440-263957b11623}')
CLSID_DVBTNetworkProvider: Guid = Guid('{216c62df-6d7f-4e9a-8571-05f14edb766a}')
CLSID_DVBCNetworkProvider: Guid = Guid('{dc0c0fe7-0485-4266-b93f-68fbf80ed834}')
DSATTRIB_UDCRTag: Guid = Guid('{eb7836ca-14ff-4919-bce7-3af12319e50c}')
DSATTRIB_PicSampleSeq: Guid = Guid('{2f5bae02-7b8f-4f60-82d6-e4ea2f1f4c99}')
DSATTRIB_OptionalVideoAttributes: Guid = Guid('{5a5f08ca-55c2-4033-92ab-55db8f781226}')
DSATTRIB_CC_CONTAINER_INFO: Guid = Guid('{e7e050fb-dd5d-40dd-9915-35dcb81bdc8a}')
DSATTRIB_TRANSPORT_PROPERTIES: Guid = Guid('{b622f612-47ad-4671-ad6c-05a98e65de3a}')
DSATTRIB_PBDATAG_ATTRIBUTE: Guid = Guid('{e0b56679-12b9-43cc-b7df-578caa5a7b63}')
DSATTRIB_CAPTURE_STREAMTIME: Guid = Guid('{0c1a5614-30cd-4f40-bcbf-d03e52306207}')
DSATTRIB_DSHOW_STREAM_DESC: Guid = Guid('{5fb5673b-0a2a-4565-827b-6853fd75e611}')
DSATTRIB_SAMPLE_LIVE_STREAM_TIME: Guid = Guid('{892cd111-72f3-411d-8b91-a9e9123ac29a}')
UUID_UdriTagTables: Guid = Guid('{e1b98d74-9778-4878-b664-eb2020364d88}')
UUID_WMDRMTagTables: Guid = Guid('{5dcd1101-9263-45bb-a4d5-c415ab8c589c}')
CLSID_DShowTVEFilter: Guid = Guid('{05500280-faa5-4df9-8246-bfc23ac5cea8}')
CLSID_TVEFilterTuneProperties: Guid = Guid('{05500281-faa5-4df9-8246-bfc23ac5cea8}')
CLSID_TVEFilterCCProperties: Guid = Guid('{05500282-faa5-4df9-8246-bfc23ac5cea8}')
CLSID_TVEFilterStatsProperties: Guid = Guid('{05500283-faa5-4df9-8246-bfc23ac5cea8}')
CLSID_IVideoEncoderProxy: Guid = Guid('{b43c4eec-8c32-4791-9102-508ada5ee8e7}')
CLSID_ICodecAPIProxy: Guid = Guid('{7ff0997a-1999-4286-a73c-622b8814e7eb}')
CLSID_IVideoEncoderCodecAPIProxy: Guid = Guid('{b05dabd9-56e5-4fdc-afa4-8a47e91f1c9c}')
ENCAPIPARAM_BITRATE: Guid = Guid('{49cc4c43-ca83-4ad4-a9af-f3696af666df}')
ENCAPIPARAM_PEAK_BITRATE: Guid = Guid('{703f16a9-3d48-44a1-b077-018dff915d19}')
ENCAPIPARAM_BITRATE_MODE: Guid = Guid('{ee5fb25c-c713-40d1-9d58-c0d7241e250f}')
ENCAPIPARAM_SAP_MODE: Guid = Guid('{0c0171db-fefc-4af7-9991-a5657c191cd1}')
CODECAPI_CHANGELISTS: Guid = Guid('{62b12acf-f6b0-47d9-9456-96f22c4e0b9d}')
CODECAPI_VIDEO_ENCODER: Guid = Guid('{7112e8e1-3d03-47ef-8e60-03f1cf537301}')
CODECAPI_AUDIO_ENCODER: Guid = Guid('{b9d19a3e-f897-429c-bc46-8138b7272b2d}')
CODECAPI_SETALLDEFAULTS: Guid = Guid('{6c5e6a7c-acf8-4f55-a999-1a628109051b}')
CODECAPI_ALLSETTINGS: Guid = Guid('{6a577e92-83e1-4113-adc2-4fcec32f83a1}')
CODECAPI_SUPPORTSEVENTS: Guid = Guid('{0581af97-7693-4dbd-9dca-3f9ebd6585a1}')
CODECAPI_CURRENTCHANGELIST: Guid = Guid('{1cb14e83-7d72-4657-83fd-47a2c5b9d13d}')
CLSID_SBE2MediaTypeProfile: Guid = Guid('{1f26a602-2b5c-4b63-b8e8-9ea5c1a7dc2e}')
CLSID_SBE2FileScan: Guid = Guid('{3e458037-0ca6-41aa-a594-2aa6c02d709b}')
CODECAPI_AVDecMmcssClass: Guid = Guid('{e0ad4828-df66-4893-9f33-788aa4ec4082}')
AVENC_H263V_LEVELCOUNT: UInt32 = 8
AVENC_H264V_LEVELCOUNT: UInt32 = 16
AVENC_H264V_MAX_MBBITS: UInt32 = 3200
D3D12_VIDEO_DECODE_PROFILE_MPEG2: Guid = Guid('{ee27417f-5e28-4e65-beea-1d26b508adc9}')
D3D12_VIDEO_DECODE_PROFILE_MPEG1_AND_MPEG2: Guid = Guid('{86695f12-340e-4f04-9fd3-9253dd327460}')
D3D12_VIDEO_DECODE_PROFILE_H264: Guid = Guid('{1b81be68-a0c7-11d3-b984-00c04f2e73c5}')
D3D12_VIDEO_DECODE_PROFILE_H264_STEREO_PROGRESSIVE: Guid = Guid('{d79be8da-0cf1-4c81-b82a-69a4e236f43d}')
D3D12_VIDEO_DECODE_PROFILE_H264_STEREO: Guid = Guid('{f9aaccbb-c2b6-4cfc-8779-5707b1760552}')
D3D12_VIDEO_DECODE_PROFILE_H264_MULTIVIEW: Guid = Guid('{705b9d82-76cf-49d6-b7e6-ac8872db013c}')
D3D12_VIDEO_DECODE_PROFILE_VC1: Guid = Guid('{1b81bea3-a0c7-11d3-b984-00c04f2e73c5}')
D3D12_VIDEO_DECODE_PROFILE_VC1_D2010: Guid = Guid('{1b81bea4-a0c7-11d3-b984-00c04f2e73c5}')
D3D12_VIDEO_DECODE_PROFILE_MPEG4PT2_SIMPLE: Guid = Guid('{efd64d74-c9e8-41d7-a5e9-e9b0e39fa319}')
D3D12_VIDEO_DECODE_PROFILE_MPEG4PT2_ADVSIMPLE_NOGMC: Guid = Guid('{ed418a9f-010d-4eda-9ae3-9a65358d8d2e}')
D3D12_VIDEO_DECODE_PROFILE_HEVC_MAIN: Guid = Guid('{5b11d51b-2f4c-4452-bcc3-09f2a1160cc0}')
D3D12_VIDEO_DECODE_PROFILE_HEVC_MAIN10: Guid = Guid('{107af0e0-ef1a-4d19-aba8-67a163073d13}')
D3D12_VIDEO_DECODE_PROFILE_VP9: Guid = Guid('{463707f8-a1d0-4585-876d-83aa6d60b89e}')
D3D12_VIDEO_DECODE_PROFILE_VP9_10BIT_PROFILE2: Guid = Guid('{a4c749ef-6ecf-48aa-8448-50a7a1165ff7}')
D3D12_VIDEO_DECODE_PROFILE_VP8: Guid = Guid('{90b899ea-3a62-4705-88b3-8df04b2744e7}')
D3D12_VIDEO_DECODE_PROFILE_AV1_PROFILE0: Guid = Guid('{b8be4ccb-cf53-46ba-8d59-d6b8a6da5d2a}')
D3D12_VIDEO_DECODE_PROFILE_AV1_PROFILE1: Guid = Guid('{6936ff0f-45b1-4163-9cc1-646ef6946108}')
D3D12_VIDEO_DECODE_PROFILE_AV1_PROFILE2: Guid = Guid('{0c5f2aa1-e541-4089-bb7b-98110a19d7c8}')
D3D12_VIDEO_DECODE_PROFILE_AV1_12BIT_PROFILE2: Guid = Guid('{17127009-a00f-4ce1-994e-bf4081f6f3f0}')
D3D12_VIDEO_DECODE_PROFILE_AV1_12BIT_PROFILE2_420: Guid = Guid('{2d80bed6-9cac-4835-9e91-327bbc4f9ee8}')
DXVA2_ModeMPEG2_MoComp: Guid = Guid('{e6a9f44b-61b0-4563-9ea4-63d2a3c6fe66}')
DXVA2_ModeMPEG2_IDCT: Guid = Guid('{bf22ad00-03ea-4690-8077-473346209b7e}')
DXVA2_ModeMPEG2_VLD: Guid = Guid('{ee27417f-5e28-4e65-beea-1d26b508adc9}')
DXVA2_ModeMPEG1_VLD: Guid = Guid('{6f3ec719-3735-42cc-8063-65cc3cb36616}')
DXVA2_ModeMPEG2and1_VLD: Guid = Guid('{86695f12-340e-4f04-9fd3-9253dd327460}')
DXVA2_ModeH264_A: Guid = Guid('{1b81be64-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeH264_B: Guid = Guid('{1b81be65-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeH264_C: Guid = Guid('{1b81be66-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeH264_D: Guid = Guid('{1b81be67-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeH264_E: Guid = Guid('{1b81be68-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeH264_F: Guid = Guid('{1b81be69-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeH264_VLD_WithFMOASO_NoFGT: Guid = Guid('{d5f04ff9-3418-45d8-9561-32a76aae2ddd}')
DXVA2_ModeH264_VLD_Stereo_Progressive_NoFGT: Guid = Guid('{d79be8da-0cf1-4c81-b82a-69a4e236f43d}')
DXVA2_ModeH264_VLD_Stereo_NoFGT: Guid = Guid('{f9aaccbb-c2b6-4cfc-8779-5707b1760552}')
DXVA2_ModeH264_VLD_Multiview_NoFGT: Guid = Guid('{705b9d82-76cf-49d6-b7e6-ac8872db013c}')
DXVA2_ModeWMV8_A: Guid = Guid('{1b81be80-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeWMV8_B: Guid = Guid('{1b81be81-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeWMV9_A: Guid = Guid('{1b81be90-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeWMV9_B: Guid = Guid('{1b81be91-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeWMV9_C: Guid = Guid('{1b81be94-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeVC1_A: Guid = Guid('{1b81bea0-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeVC1_B: Guid = Guid('{1b81bea1-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeVC1_C: Guid = Guid('{1b81bea2-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeVC1_D: Guid = Guid('{1b81bea3-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_ModeVC1_D2010: Guid = Guid('{1b81bea4-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_NoEncrypt: Guid = Guid('{1b81bed0-a0c7-11d3-b984-00c04f2e73c5}')
DXVA2_VideoProcProgressiveDevice: Guid = Guid('{5a54a0c9-c7ec-4bd9-8ede-f3c75dc4393b}')
DXVA2_VideoProcBobDevice: Guid = Guid('{335aa36e-7884-43a4-9c91-7f87faf3e37e}')
DXVA2_VideoProcSoftwareDevice: Guid = Guid('{4553d47f-ee7e-4e3f-9475-dbf1376c4810}')
DXVA2_ModeMPEG4pt2_VLD_Simple: Guid = Guid('{efd64d74-c9e8-41d7-a5e9-e9b0e39fa319}')
DXVA2_ModeMPEG4pt2_VLD_AdvSimple_NoGMC: Guid = Guid('{ed418a9f-010d-4eda-9ae3-9a65358d8d2e}')
DXVA2_ModeMPEG4pt2_VLD_AdvSimple_GMC: Guid = Guid('{ab998b5b-4258-44a9-9feb-94e597a6baae}')
DXVA2_ModeHEVC_VLD_Main: Guid = Guid('{5b11d51b-2f4c-4452-bcc3-09f2a1160cc0}')
DXVA2_ModeHEVC_VLD_Main10: Guid = Guid('{107af0e0-ef1a-4d19-aba8-67a163073d13}')
DXVA2_ModeVP9_VLD_Profile0: Guid = Guid('{463707f8-a1d0-4585-876d-83aa6d60b89e}')
DXVA2_ModeVP9_VLD_10bit_Profile2: Guid = Guid('{a4c749ef-6ecf-48aa-8448-50a7a1165ff7}')
DXVA2_ModeVP8_VLD: Guid = Guid('{90b899ea-3a62-4705-88b3-8df04b2744e7}')
DXVA2_E_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2147217408
DXVA2_E_NEW_VIDEO_DEVICE: Windows.Win32.Foundation.HRESULT = -2147217407
DXVA2_E_VIDEO_DEVICE_LOCKED: Windows.Win32.Foundation.HRESULT = -2147217406
DXVA2_E_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2147217405
MAX_SUBSTREAMS: UInt32 = 15
DXVA2_DECODE_GET_DRIVER_HANDLE: UInt32 = 1829
DXVA2_DECODE_SPECIFY_ENCRYPTED_BLOCKS: UInt32 = 1828
DXVAp_ModeMPEG2_A: Guid = Guid('{1b81be0a-a0c7-11d3-b984-00c04f2e73c5}')
DXVAp_ModeMPEG2_C: Guid = Guid('{1b81be0c-a0c7-11d3-b984-00c04f2e73c5}')
DXVAp_NoEncrypt: Guid = Guid('{1b81bed0-a0c7-11d3-b984-00c04f2e73c5}')
DXVAp_DeinterlaceBobDevice: Guid = Guid('{335aa36e-7884-43a4-9c91-7f87faf3e37e}')
DXVAp_DeinterlaceContainerDevice: Guid = Guid('{0e85cb93-3046-4ff0-aecc-d58cb5f035fd}')
DXVAHD_STREAM_STATE_PRIVATE_IVTC: Guid = Guid('{9c601e3c-0f33-414c-a739-99540ee42da5}')
DXVAHDControlGuid: Guid = Guid('{a0386e75-f70c-464c-a9ce-33c44e091623}')
DXVAHDETWGUID_CREATEVIDEOPROCESSOR: Guid = Guid('{681e3d1e-5674-4fb3-a503-2f2055e91f60}')
DXVAHDETWGUID_VIDEOPROCESSBLTSTATE: Guid = Guid('{76c94b5a-193f-4692-9484-a4d999da81a8}')
DXVAHDETWGUID_VIDEOPROCESSSTREAMSTATE: Guid = Guid('{262c0b02-209d-47ed-94d8-82ae02b84aa7}')
DXVAHDETWGUID_VIDEOPROCESSBLTHD: Guid = Guid('{bef3d435-78c7-4de3-9707-cd1b083b160a}')
DXVAHDETWGUID_VIDEOPROCESSBLTHD_STREAM: Guid = Guid('{27ae473e-a5fc-4be5-b4e3-f24994d3c495}')
DXVAHDETWGUID_DESTROYVIDEOPROCESSOR: Guid = Guid('{f943f0a0-3f16-43e0-8093-105a986aa5f1}')
MR_VIDEO_RENDER_SERVICE: Guid = Guid('{1092a86c-ab1a-459a-a336-831fbc4d11ff}')
MR_VIDEO_MIXER_SERVICE: Guid = Guid('{073cd2fc-6cf4-40b7-8859-e89552c841f8}')
MR_VIDEO_ACCELERATION_SERVICE: Guid = Guid('{efef5175-5c7d-4ce2-bbbd-34ff8bca6554}')
MR_BUFFER_SERVICE: Guid = Guid('{a562248c-9ac6-4ffc-9fba-3af8f8ad1a4d}')
VIDEO_ZOOM_RECT: Guid = Guid('{7aaa1638-1b7f-4c93-bd89-5b9c9fb6fcf0}')
MFEVRDLL: UInt32 = 0
MF_SDK_VERSION: UInt32 = 2
MF_API_VERSION: UInt32 = 112
MFSTARTUP_NOSOCKET: UInt32 = 1
MFSTARTUP_LITE: UInt32 = 1
MFSTARTUP_FULL: UInt32 = 0
MF_E_DXGI_DEVICE_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2147217408
MF_E_DXGI_NEW_VIDEO_DEVICE: Windows.Win32.Foundation.HRESULT = -2147217407
MF_E_DXGI_VIDEO_DEVICE_LOCKED: Windows.Win32.Foundation.HRESULT = -2147217406
MF_1_BYTE_ALIGNMENT: UInt32 = 0
MF_2_BYTE_ALIGNMENT: UInt32 = 1
MF_4_BYTE_ALIGNMENT: UInt32 = 3
MF_8_BYTE_ALIGNMENT: UInt32 = 7
MF_16_BYTE_ALIGNMENT: UInt32 = 15
MF_32_BYTE_ALIGNMENT: UInt32 = 31
MF_64_BYTE_ALIGNMENT: UInt32 = 63
MF_128_BYTE_ALIGNMENT: UInt32 = 127
MF_256_BYTE_ALIGNMENT: UInt32 = 255
MF_512_BYTE_ALIGNMENT: UInt32 = 511
MF_1024_BYTE_ALIGNMENT: UInt32 = 1023
MF_2048_BYTE_ALIGNMENT: UInt32 = 2047
MF_4096_BYTE_ALIGNMENT: UInt32 = 4095
MF_8192_BYTE_ALIGNMENT: UInt32 = 8191
MF_EVENT_SESSIONCAPS: Guid = Guid('{7e5ebcd0-11b8-4abe-afad-10f6599a7f42}')
MF_EVENT_SESSIONCAPS_DELTA: Guid = Guid('{7e5ebcd1-11b8-4abe-afad-10f6599a7f42}')
MFSESSIONCAP_START: UInt32 = 1
MFSESSIONCAP_SEEK: UInt32 = 2
MFSESSIONCAP_PAUSE: UInt32 = 4
MFSESSIONCAP_RATE_FORWARD: UInt32 = 16
MFSESSIONCAP_RATE_REVERSE: UInt32 = 32
MFSESSIONCAP_DOES_NOT_USE_NETWORK: UInt32 = 64
MF_EVENT_TOPOLOGY_STATUS: Guid = Guid('{30c5018d-9a53-454b-ad9e-6d5f8fa7c43b}')
MF_EVENT_START_PRESENTATION_TIME: Guid = Guid('{5ad914d0-9b45-4a8d-a2c0-81d1e50bfb07}')
MF_EVENT_PRESENTATION_TIME_OFFSET: Guid = Guid('{5ad914d1-9b45-4a8d-a2c0-81d1e50bfb07}')
MF_EVENT_START_PRESENTATION_TIME_AT_OUTPUT: Guid = Guid('{5ad914d2-9b45-4a8d-a2c0-81d1e50bfb07}')
MF_EVENT_SOURCE_FAKE_START: Guid = Guid('{a8cc55a7-6b31-419f-845d-ffb351a2434b}')
MF_EVENT_SOURCE_PROJECTSTART: Guid = Guid('{a8cc55a8-6b31-419f-845d-ffb351a2434b}')
MF_EVENT_SOURCE_ACTUAL_START: Guid = Guid('{a8cc55a9-6b31-419f-845d-ffb351a2434b}')
MF_EVENT_SOURCE_TOPOLOGY_CANCELED: Guid = Guid('{db62f650-9a5e-4704-acf3-563bc6a73364}')
MF_EVENT_SOURCE_CHARACTERISTICS: Guid = Guid('{47db8490-8b22-4f52-afda-9ce1b2d3cfa8}')
MF_EVENT_SOURCE_CHARACTERISTICS_OLD: Guid = Guid('{47db8491-8b22-4f52-afda-9ce1b2d3cfa8}')
MF_EVENT_DO_THINNING: Guid = Guid('{321ea6fb-dad9-46e4-b31d-d2eae7090e30}')
MF_EVENT_SCRUBSAMPLE_TIME: Guid = Guid('{9ac712b3-dcb8-44d5-8d0c-37455a2782e3}')
MF_EVENT_OUTPUT_NODE: Guid = Guid('{830f1a8b-c060-46dd-a801-1c95dec9b107}')
MF_EVENT_MFT_INPUT_STREAM_ID: Guid = Guid('{f29c2cca-7ae6-42d2-b284-bf837cc874e2}')
MF_EVENT_MFT_CONTEXT: Guid = Guid('{b7cd31f1-899e-4b41-80c9-26a896d32977}')
MF_EVENT_STREAM_METADATA_KEYDATA: Guid = Guid('{cd59a4a1-4a3b-4bbd-8665-72a40fbea776}')
MF_EVENT_STREAM_METADATA_CONTENT_KEYIDS: Guid = Guid('{5063449d-cc29-4fc6-a75a-d247b35af85c}')
MF_EVENT_STREAM_METADATA_SYSTEMID: Guid = Guid('{1ea2ef64-ba16-4a36-8719-fe7560ba32ad}')
MFSampleExtension_MaxDecodeFrameSize: Guid = Guid('{d3cc654f-f9f3-4a13-889f-f04eb2b5b957}')
MFSampleExtension_AccumulatedNonRefPicPercent: Guid = Guid('{79ea74df-a740-445b-bc98-c9ed1f260eee}')
MFSampleExtension_Encryption_ProtectionScheme: Guid = Guid('{d054d096-28bb-45da-87ec-74f351871406}')
MFSampleExtension_Encryption_CryptByteBlock: Guid = Guid('{9d84289b-0c7f-4713-ab95-108ab42ad801}')
MFSampleExtension_Encryption_SkipByteBlock: Guid = Guid('{0d550548-8317-4ab1-845f-d06306e293e3}')
MFSampleExtension_Encryption_SubSample_Mapping: Guid = Guid('{8444f27a-69a1-48da-bd08-11cef36830d2}')
MFSampleExtension_Encryption_ClearSliceHeaderData: Guid = Guid('{5509a4f4-320d-4e6c-8d1a-94c66dd20cb0}')
MFSampleExtension_Encryption_HardwareProtection_KeyInfoID: Guid = Guid('{8cbfcceb-94a5-4de1-8231-a85e47cf81e7}')
MFSampleExtension_Encryption_HardwareProtection_KeyInfo: Guid = Guid('{b2372080-455b-4dd7-9989-1a955784b754}')
MFSampleExtension_Encryption_HardwareProtection_VideoDecryptorContext: Guid = Guid('{693470c8-e837-47a0-88cb-535b905e3582}')
MFSampleExtension_Encryption_Opaque_Data: Guid = Guid('{224d77e5-1391-4ffb-9f41-b432f68c611d}')
MFSampleExtension_NALULengthInfo: Guid = Guid('{19124e7c-ad4b-465f-bb18-20186287b6af}')
MFSampleExtension_Encryption_ResumeVideoOutput: Guid = Guid('{a435aba5-afde-4cf5-bc1c-f6acaf13949d}')
MFSampleExtension_Encryption_NALUTypes: Guid = Guid('{b0f067c7-714c-416c-8d59-5f4ddf8913b6}')
MFSampleExtension_Encryption_SPSPPSData: Guid = Guid('{aede0fa2-0e0c-453c-b7f3-de8693364d11}')
MFSampleExtension_Encryption_SEIData: Guid = Guid('{3cf0e972-4542-4687-9999-585f565fba7d}')
MFSampleExtension_Encryption_HardwareProtection: Guid = Guid('{9a2b2d2b-8270-43e3-8448-994f426e8886}')
MFSampleExtension_CleanPoint: Guid = Guid('{9cdf01d8-a0f0-43ba-b077-eaa06cbd728a}')
MFSampleExtension_Discontinuity: Guid = Guid('{9cdf01d9-a0f0-43ba-b077-eaa06cbd728a}')
MFSampleExtension_Token: Guid = Guid('{8294da66-f328-4805-b551-00deb4c57a61}')
MFSampleExtension_ClosedCaption_CEA708: Guid = Guid('{26f09068-e744-47dc-aa03-dbf20403bde6}')
MFSampleExtension_ClosedCaption_CEA708_MAX_SIZE: UInt32 = 256
MFSampleExtension_DecodeTimestamp: Guid = Guid('{73a954d4-09e2-4861-befc-94bd97c08e6e}')
MFSampleExtension_VideoEncodeQP: Guid = Guid('{b2efe478-f979-4c66-b95e-ee2b82c82f36}')
MFSampleExtension_VideoEncodePictureType: Guid = Guid('{973704e6-cd14-483c-8f20-c9fc0928bad5}')
MFSampleExtension_FrameCorruption: Guid = Guid('{b4dd4a8c-0beb-44c4-8b75-b02b913b04f0}')
MFSampleExtension_DirtyRects: Guid = Guid('{9ba70225-b342-4e97-9126-0b566ab7ea7e}')
MFSampleExtension_MoveRegions: Guid = Guid('{e2a6c693-3a8b-4b8d-95d0-f60281a12fb7}')
MFSampleExtension_HDCP_OptionalHeader: Guid = Guid('{9a2e7390-121f-455f-8376-c97428e0b540}')
MFSampleExtension_HDCP_FrameCounter: Guid = Guid('{9d389c60-f507-4aa6-a40a-71027a02f3de}')
MFSampleExtension_HDCP_StreamID: Guid = Guid('{177e5d74-c370-4a7a-95a2-36833c01d0af}')
MFSampleExtension_Timestamp: Guid = Guid('{1e436999-69be-4c7a-9369-70068c0260cb}')
MFSampleExtension_RepeatFrame: Guid = Guid('{88be738f-0711-4f42-b458-344aed42ec2f}')
MFT_ENCODER_ERROR: Guid = Guid('{c8d1eda4-98e4-41d5-9297-44f53852f90e}')
MFT_GFX_DRIVER_VERSION_ID_Attribute: Guid = Guid('{f34b9093-05e0-4b16-993d-3e2a2cde6ad3}')
MFSampleExtension_DescrambleData: Guid = Guid('{43483be6-4903-4314-b032-2951365936fc}')
MFSampleExtension_SampleKeyID: Guid = Guid('{9ed713c8-9b87-4b26-8297-a93b0c5a8acc}')
MFSampleExtension_GenKeyFunc: Guid = Guid('{441ca1ee-6b1f-4501-903a-de87df42f6ed}')
MFSampleExtension_GenKeyCtx: Guid = Guid('{188120cb-d7da-4b59-9b3e-9252fd37301c}')
MFSampleExtension_PacketCrossOffsets: Guid = Guid('{2789671d-389f-40bb-90d9-c282f77f9abd}')
MFSampleExtension_Encryption_SampleID: Guid = Guid('{6698b84e-0afa-4330-aeb2-1c0a98d7a44d}')
MFSampleExtension_Encryption_KeyID: Guid = Guid('{76376591-795f-4da1-86ed-9d46eca109a9}')
MFSampleExtension_Content_KeyID: Guid = Guid('{c6c7f5b0-acca-415b-87d9-10441469efc6}')
MFSampleExtension_Encryption_SubSampleMappingSplit: Guid = Guid('{fe0254b9-2aa5-4edc-99f7-17e89dbf9174}')
MFSampleExtension_Interlaced: Guid = Guid('{b1d5830a-deb8-40e3-90fa-389943716461}')
MFSampleExtension_BottomFieldFirst: Guid = Guid('{941ce0a3-6ae3-4dda-9a08-a64298340617}')
MFSampleExtension_RepeatFirstField: Guid = Guid('{304d257c-7493-4fbd-b149-9228de8d9a99}')
MFSampleExtension_SingleField: Guid = Guid('{9d85f816-658b-455a-bde0-9fa7e15ab8f9}')
MFSampleExtension_DerivedFromTopField: Guid = Guid('{6852465a-ae1c-4553-8e9b-c3420fcb1637}')
MFSampleExtension_MeanAbsoluteDifference: Guid = Guid('{1cdbde11-08b4-4311-a6dd-0f9f371907aa}')
MFSampleExtension_LongTermReferenceFrameInfo: Guid = Guid('{9154733f-e1bd-41bf-81d3-fcd918f71332}')
MFSampleExtension_ROIRectangle: Guid = Guid('{3414a438-4998-4d2c-be82-be3ca0b24d43}')
MFSampleExtension_LastSlice: Guid = Guid('{2b5d5457-5547-4f07-b8c8-b4a3a9a1daac}')
MACROBLOCK_FLAG_SKIP: UInt32 = 1
MACROBLOCK_FLAG_DIRTY: UInt32 = 2
MACROBLOCK_FLAG_MOTION: UInt32 = 4
MACROBLOCK_FLAG_VIDEO: UInt32 = 8
MACROBLOCK_FLAG_HAS_MOTION_VECTOR: UInt32 = 16
MACROBLOCK_FLAG_HAS_QP: UInt32 = 32
MFSampleExtension_FeatureMap: Guid = Guid('{a032d165-46fc-400a-b449-49de53e62a6e}')
MFSampleExtension_ChromaOnly: Guid = Guid('{1eb9179c-a01f-4845-8c04-0e65a26eb04f}')
MFSampleExtension_PhotoThumbnail: Guid = Guid('{74bbc85c-c8bb-42dc-b586-da17ffd35dcc}')
MFSampleExtension_PhotoThumbnailMediaType: Guid = Guid('{61ad5420-ebf8-4143-89af-6bf25f672def}')
MFSampleExtension_CaptureMetadata: Guid = Guid('{2ebe23a8-faf5-444a-a6a2-eb810880ab5d}')
MFSampleExtension_MDLCacheCookie: Guid = Guid('{5f002af9-d8f9-41a3-b6c3-a2ad43f647ad}')
MF_CAPTURE_METADATA_PHOTO_FRAME_FLASH: Guid = Guid('{0f9dd6c6-6003-45d8-bd59-f1f53e3d04e8}')
MF_CAPTURE_METADATA_FRAME_RAWSTREAM: Guid = Guid('{9252077b-2680-49b9-ae02-b19075973b70}')
MF_CAPTURE_METADATA_FOCUSSTATE: Guid = Guid('{a87ee154-997f-465d-b91f-29d53b982b88}')
MF_CAPTURE_METADATA_REQUESTED_FRAME_SETTING_ID: Guid = Guid('{bb3716d9-8a61-47a4-8197-459c7ff174d5}')
MF_CAPTURE_METADATA_EXPOSURE_TIME: Guid = Guid('{16b9ae99-cd84-4063-879d-a28c7633729e}')
MF_CAPTURE_METADATA_EXPOSURE_COMPENSATION: Guid = Guid('{d198aa75-4b62-4345-abf3-3c31fa12c299}')
MF_CAPTURE_METADATA_ISO_SPEED: Guid = Guid('{e528a68f-b2e3-44fe-8b65-07bf4b5a13ff}')
MF_CAPTURE_METADATA_LENS_POSITION: Guid = Guid('{b5fc8e86-11d1-4e70-819b-723a89fa4520}')
MF_CAPTURE_METADATA_SCENE_MODE: Guid = Guid('{9cc3b54d-5ed3-4bae-b388-7670aef59e13}')
MF_CAPTURE_METADATA_FLASH: Guid = Guid('{4a51520b-fb36-446c-9df2-68171b9a0389}')
MF_CAPTURE_METADATA_FLASH_POWER: Guid = Guid('{9c0e0d49-0205-491a-bc9d-2d6e1f4d5684}')
MF_CAPTURE_METADATA_WHITEBALANCE: Guid = Guid('{c736fd77-0fb9-4e2e-97a2-fcd490739ee9}')
MF_CAPTURE_METADATA_ZOOMFACTOR: Guid = Guid('{e50b0b81-e501-42c2-abf2-857ecb13fa5c}')
MF_CAPTURE_METADATA_FACEROIS: Guid = Guid('{864f25a6-349f-46b1-a30e-54cc22928a47}')
MF_CAPTURE_METADATA_FACEROITIMESTAMPS: Guid = Guid('{e94d50cc-3da0-44d4-bb34-83198a741868}')
MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS: Guid = Guid('{b927a1a8-18ef-46d3-b3af-69372f94d9b2}')
MF_CAPTURE_METADATA_ISO_GAINS: Guid = Guid('{05802ac9-0e1d-41c7-a8c8-7e7369f84e1e}')
MF_CAPTURE_METADATA_SENSORFRAMERATE: Guid = Guid('{db51357e-9d3d-4962-b06d-07ce650d9a0a}')
MF_CAPTURE_METADATA_WHITEBALANCE_GAINS: Guid = Guid('{e7570c8f-2dcb-4c7c-aace-22ece7cce647}')
MF_CAPTURE_METADATA_HISTOGRAM: Guid = Guid('{85358432-2ef6-4ba9-a3fb-06d82974b895}')
MF_CAPTURE_METADATA_EXIF: Guid = Guid('{2e9575b8-8c31-4a02-8575-42b197b71592}')
MF_CAPTURE_METADATA_FRAME_ILLUMINATION: Guid = Guid('{6d688ffc-63d3-46fe-bada-5b947db0d080}')
MF_CAPTURE_METADATA_UVC_PAYLOADHEADER: Guid = Guid('{f9f88a87-e1dd-441e-95cb-42e21a64f1d9}')
MFSampleExtension_Depth_MinReliableDepth: Guid = Guid('{5f8582b2-e36b-47c8-9b87-fee1ca72c5b0}')
MFSampleExtension_Depth_MaxReliableDepth: Guid = Guid('{e45545d1-1f0f-4a32-a8a7-6101a24ea8be}')
MF_CAPTURE_METADATA_FIRST_SCANLINE_START_TIME_QPC: Guid = Guid('{6a2c49f1-e052-46b6-b2d9-73c1558709af}')
MF_CAPTURE_METADATA_LAST_SCANLINE_END_TIME_QPC: Guid = Guid('{dccadecb-c4d4-400d-b418-10e88525e1f6}')
MF_CAPTURE_METADATA_SCANLINE_TIME_QPC_ACCURACY: Guid = Guid('{4cd79c51-f765-4b09-b1e1-27d1f7ebea09}')
MF_CAPTURE_METADATA_SCANLINE_DIRECTION: Guid = Guid('{6496a3ba-1907-49e6-b0c3-123795f380a9}')
MFCAPTURE_METADATA_SCAN_RIGHT_LEFT: UInt32 = 1
MFCAPTURE_METADATA_SCAN_BOTTOM_TOP: UInt32 = 2
MFCAPTURE_METADATA_SCANLINE_VERTICAL: UInt32 = 4
MF_CAPTURE_METADATA_DIGITALWINDOW: Guid = Guid('{276f72a2-59c8-4f69-97b4-068b8c0ec044}')
MF_CAPTURE_METADATA_FRAME_BACKGROUND_MASK: Guid = Guid('{03f14dd3-75dd-433a-a8e2-1e3f5f2a50a0}')
MF_METADATAFACIALEXPRESSION_SMILE: UInt32 = 1
MF_METADATATIMESTAMPS_DEVICE: UInt32 = 1
MF_METADATATIMESTAMPS_PRESENTATION: UInt32 = 2
MF_HISTOGRAM_CHANNEL_Y: UInt32 = 1
MF_HISTOGRAM_CHANNEL_R: UInt32 = 2
MF_HISTOGRAM_CHANNEL_G: UInt32 = 4
MF_HISTOGRAM_CHANNEL_B: UInt32 = 8
MF_HISTOGRAM_CHANNEL_Cb: UInt32 = 16
MF_HISTOGRAM_CHANNEL_Cr: UInt32 = 32
MFT_CATEGORY_VIDEO_DECODER: Guid = Guid('{d6c02d4b-6833-45b4-971a-05a4b04bab91}')
MFT_CATEGORY_VIDEO_ENCODER: Guid = Guid('{f79eac7d-e545-4387-bdee-d647d7bde42a}')
MFT_CATEGORY_VIDEO_EFFECT: Guid = Guid('{12e17c21-532c-4a6e-8a1c-40825a736397}')
MFT_CATEGORY_MULTIPLEXER: Guid = Guid('{059c561e-05ae-4b61-b69d-55b61ee54a7b}')
MFT_CATEGORY_DEMULTIPLEXER: Guid = Guid('{a8700a7a-939b-44c5-99d7-76226b23b3f1}')
MFT_CATEGORY_AUDIO_DECODER: Guid = Guid('{9ea73fb4-ef7a-4559-8d5d-719d8f0426c7}')
MFT_CATEGORY_AUDIO_ENCODER: Guid = Guid('{91c64bd0-f91e-4d8c-9276-db248279d975}')
MFT_CATEGORY_AUDIO_EFFECT: Guid = Guid('{11064c48-3648-4ed0-932e-05ce8ac811b7}')
MFT_CATEGORY_VIDEO_PROCESSOR: Guid = Guid('{302ea3fc-aa5f-47f9-9f7a-c2188bb16302}')
MFT_CATEGORY_OTHER: Guid = Guid('{90175d57-b7ea-4901-aeb3-933a8747756f}')
MFT_CATEGORY_ENCRYPTOR: Guid = Guid('{b0c687be-01cd-44b5-b8b2-7c1d7e058b1f}')
MFT_CATEGORY_VIDEO_RENDERER_EFFECT: Guid = Guid('{145cd8b4-92f4-4b23-8ae7-e0df06c2da95}')
MFT_ENUM_VIDEO_RENDERER_EXTENSION_PROFILE: Guid = Guid('{62c56928-9a4e-443b-b9dc-cac830c24100}')
MFT_ENUM_ADAPTER_LUID: Guid = Guid('{1d39518c-e220-4da8-a07f-ba172552d6b1}')
MFT_SUPPORT_DYNAMIC_FORMAT_CHANGE: Guid = Guid('{53476a11-3f13-49fb-ac42-ee2733c96741}')
LOCAL_D3DFMT_DEFINES: UInt32 = 1
MFVideoFormat_Base: Guid = Guid('{00000000-0000-0010-8000-00aa00389b71}')
MFVideoFormat_RGB32: Guid = Guid('{00000016-0000-0010-8000-00aa00389b71}')
MFVideoFormat_ARGB32: Guid = Guid('{00000015-0000-0010-8000-00aa00389b71}')
MFVideoFormat_RGB24: Guid = Guid('{00000014-0000-0010-8000-00aa00389b71}')
MFVideoFormat_RGB555: Guid = Guid('{00000018-0000-0010-8000-00aa00389b71}')
MFVideoFormat_RGB565: Guid = Guid('{00000017-0000-0010-8000-00aa00389b71}')
MFVideoFormat_RGB8: Guid = Guid('{00000029-0000-0010-8000-00aa00389b71}')
MFVideoFormat_L8: Guid = Guid('{00000032-0000-0010-8000-00aa00389b71}')
MFVideoFormat_L16: Guid = Guid('{00000051-0000-0010-8000-00aa00389b71}')
MFVideoFormat_D16: Guid = Guid('{00000050-0000-0010-8000-00aa00389b71}')
MFVideoFormat_AI44: Guid = Guid('{34344941-0000-0010-8000-00aa00389b71}')
MFVideoFormat_AYUV: Guid = Guid('{56555941-0000-0010-8000-00aa00389b71}')
MFVideoFormat_YUY2: Guid = Guid('{32595559-0000-0010-8000-00aa00389b71}')
MFVideoFormat_YVYU: Guid = Guid('{55595659-0000-0010-8000-00aa00389b71}')
MFVideoFormat_YVU9: Guid = Guid('{39555659-0000-0010-8000-00aa00389b71}')
MFVideoFormat_UYVY: Guid = Guid('{59565955-0000-0010-8000-00aa00389b71}')
MFVideoFormat_NV11: Guid = Guid('{3131564e-0000-0010-8000-00aa00389b71}')
MFVideoFormat_NV12: Guid = Guid('{3231564e-0000-0010-8000-00aa00389b71}')
MFVideoFormat_NV21: Guid = Guid('{3132564e-0000-0010-8000-00aa00389b71}')
MFVideoFormat_YV12: Guid = Guid('{32315659-0000-0010-8000-00aa00389b71}')
MFVideoFormat_I420: Guid = Guid('{30323449-0000-0010-8000-00aa00389b71}')
MFVideoFormat_IYUV: Guid = Guid('{56555949-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Y210: Guid = Guid('{30313259-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Y216: Guid = Guid('{36313259-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Y410: Guid = Guid('{30313459-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Y416: Guid = Guid('{36313459-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Y41P: Guid = Guid('{50313459-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Y41T: Guid = Guid('{54313459-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Y42T: Guid = Guid('{54323459-0000-0010-8000-00aa00389b71}')
MFVideoFormat_P210: Guid = Guid('{30313250-0000-0010-8000-00aa00389b71}')
MFVideoFormat_P216: Guid = Guid('{36313250-0000-0010-8000-00aa00389b71}')
MFVideoFormat_P010: Guid = Guid('{30313050-0000-0010-8000-00aa00389b71}')
MFVideoFormat_P016: Guid = Guid('{36313050-0000-0010-8000-00aa00389b71}')
MFVideoFormat_v210: Guid = Guid('{30313276-0000-0010-8000-00aa00389b71}')
MFVideoFormat_v216: Guid = Guid('{36313276-0000-0010-8000-00aa00389b71}')
MFVideoFormat_v410: Guid = Guid('{30313476-0000-0010-8000-00aa00389b71}')
MFVideoFormat_MP43: Guid = Guid('{3334504d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_MP4S: Guid = Guid('{5334504d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_M4S2: Guid = Guid('{3253344d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_MP4V: Guid = Guid('{5634504d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_WMV1: Guid = Guid('{31564d57-0000-0010-8000-00aa00389b71}')
MFVideoFormat_WMV2: Guid = Guid('{32564d57-0000-0010-8000-00aa00389b71}')
MFVideoFormat_WMV3: Guid = Guid('{33564d57-0000-0010-8000-00aa00389b71}')
MFVideoFormat_WVC1: Guid = Guid('{31435657-0000-0010-8000-00aa00389b71}')
MFVideoFormat_MSS1: Guid = Guid('{3153534d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_MSS2: Guid = Guid('{3253534d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_MPG1: Guid = Guid('{3147504d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_DVSL: Guid = Guid('{6c737664-0000-0010-8000-00aa00389b71}')
MFVideoFormat_DVSD: Guid = Guid('{64737664-0000-0010-8000-00aa00389b71}')
MFVideoFormat_DVHD: Guid = Guid('{64687664-0000-0010-8000-00aa00389b71}')
MFVideoFormat_DV25: Guid = Guid('{35327664-0000-0010-8000-00aa00389b71}')
MFVideoFormat_DV50: Guid = Guid('{30357664-0000-0010-8000-00aa00389b71}')
MFVideoFormat_DVH1: Guid = Guid('{31687664-0000-0010-8000-00aa00389b71}')
MFVideoFormat_H264: Guid = Guid('{34363248-0000-0010-8000-00aa00389b71}')
MFVideoFormat_H265: Guid = Guid('{35363248-0000-0010-8000-00aa00389b71}')
MFVideoFormat_MJPG: Guid = Guid('{47504a4d-0000-0010-8000-00aa00389b71}')
MFVideoFormat_420O: Guid = Guid('{4f303234-0000-0010-8000-00aa00389b71}')
MFVideoFormat_HEVC: Guid = Guid('{43564548-0000-0010-8000-00aa00389b71}')
MFVideoFormat_HEVC_ES: Guid = Guid('{53564548-0000-0010-8000-00aa00389b71}')
MFVideoFormat_VP80: Guid = Guid('{30385056-0000-0010-8000-00aa00389b71}')
MFVideoFormat_VP90: Guid = Guid('{30395056-0000-0010-8000-00aa00389b71}')
MFVideoFormat_ORAW: Guid = Guid('{5741524f-0000-0010-8000-00aa00389b71}')
MFVideoFormat_H263: Guid = Guid('{33363248-0000-0010-8000-00aa00389b71}')
MFVideoFormat_A2R10G10B10: Guid = Guid('{0000001f-0000-0010-8000-00aa00389b71}')
MFVideoFormat_A16B16G16R16F: Guid = Guid('{00000071-0000-0010-8000-00aa00389b71}')
MFVideoFormat_VP10: Guid = Guid('{30315056-0000-0010-8000-00aa00389b71}')
MFVideoFormat_AV1: Guid = Guid('{31305641-0000-0010-8000-00aa00389b71}')
MFVideoFormat_Theora: Guid = Guid('{6f656874-0000-0010-8000-00aa00389b71}')
MFVideoFormat_H264_ES: Guid = Guid('{3f40f4f0-5622-4ff8-b6d8-a17a584bee5e}')
MFVideoFormat_MPEG2: Guid = Guid('{e06d8026-db46-11cf-b4d1-00805f6cbbea}')
MFAudioFormat_Base: Guid = Guid('{00000000-0000-0010-8000-00aa00389b71}')
MFAudioFormat_PCM: Guid = Guid('{00000001-0000-0010-8000-00aa00389b71}')
MFAudioFormat_Float: Guid = Guid('{00000003-0000-0010-8000-00aa00389b71}')
MFAudioFormat_DTS: Guid = Guid('{00000008-0000-0010-8000-00aa00389b71}')
MFAudioFormat_Dolby_AC3_SPDIF: Guid = Guid('{00000092-0000-0010-8000-00aa00389b71}')
MFAudioFormat_DRM: Guid = Guid('{00000009-0000-0010-8000-00aa00389b71}')
MFAudioFormat_WMAudioV8: Guid = Guid('{00000161-0000-0010-8000-00aa00389b71}')
MFAudioFormat_WMAudioV9: Guid = Guid('{00000162-0000-0010-8000-00aa00389b71}')
MFAudioFormat_WMAudio_Lossless: Guid = Guid('{00000163-0000-0010-8000-00aa00389b71}')
MFAudioFormat_WMASPDIF: Guid = Guid('{00000164-0000-0010-8000-00aa00389b71}')
MFAudioFormat_MSP1: Guid = Guid('{0000000a-0000-0010-8000-00aa00389b71}')
MFAudioFormat_MP3: Guid = Guid('{00000055-0000-0010-8000-00aa00389b71}')
MFAudioFormat_MPEG: Guid = Guid('{00000050-0000-0010-8000-00aa00389b71}')
MFAudioFormat_AAC: Guid = Guid('{00001610-0000-0010-8000-00aa00389b71}')
MFAudioFormat_ADTS: Guid = Guid('{00001600-0000-0010-8000-00aa00389b71}')
MFAudioFormat_AMR_NB: Guid = Guid('{00007361-0000-0010-8000-00aa00389b71}')
MFAudioFormat_AMR_WB: Guid = Guid('{00007362-0000-0010-8000-00aa00389b71}')
MFAudioFormat_AMR_WP: Guid = Guid('{00007363-0000-0010-8000-00aa00389b71}')
MFAudioFormat_FLAC: Guid = Guid('{0000f1ac-0000-0010-8000-00aa00389b71}')
MFAudioFormat_ALAC: Guid = Guid('{00006c61-0000-0010-8000-00aa00389b71}')
MFAudioFormat_Opus: Guid = Guid('{0000704f-0000-0010-8000-00aa00389b71}')
MFAudioFormat_Dolby_AC4: Guid = Guid('{0000ac40-0000-0010-8000-00aa00389b71}')
MFAudioFormat_Dolby_AC3: Guid = Guid('{e06d802c-db46-11cf-b4d1-00805f6cbbea}')
MFAudioFormat_Dolby_DDPlus: Guid = Guid('{a7fb87af-2d02-42fb-a4d4-05cd93843bdd}')
MFAudioFormat_Dolby_AC4_V1: Guid = Guid('{36b7927c-3d87-4a2a-9196-a21ad9e935e6}')
MFAudioFormat_Dolby_AC4_V2: Guid = Guid('{7998b2a0-17dd-49b6-8dfa-9b278552a2ac}')
MFAudioFormat_Dolby_AC4_V1_ES: Guid = Guid('{9d8dccc6-d156-4fb8-979c-a85be7d21dfa}')
MFAudioFormat_Dolby_AC4_V2_ES: Guid = Guid('{7e58c9f9-b070-45f4-8ccd-a99a0417c1ac}')
MFAudioFormat_Vorbis: Guid = Guid('{8d2fd10b-5841-4a6b-8905-588fec1aded9}')
MFAudioFormat_DTS_RAW: Guid = Guid('{e06d8033-db46-11cf-b4d1-00805f6cbbea}')
MFAudioFormat_DTS_HD: Guid = Guid('{a2e58eb7-0fa9-48bb-a40c-fa0e156d0645}')
MFAudioFormat_DTS_XLL: Guid = Guid('{45b37c1b-8c70-4e59-a7be-a1e42c81c80d}')
MFAudioFormat_DTS_LBR: Guid = Guid('{c2fe6f0a-4e3c-4df1-9b60-50863091e4b9}')
MFAudioFormat_DTS_UHD: Guid = Guid('{87020117-ace3-42de-b73e-c656706263f8}')
MFAudioFormat_DTS_UHDY: Guid = Guid('{9b9cca00-91b9-4ccc-883a-8f787ac3cc86}')
MFAudioFormat_Float_SpatialObjects: Guid = Guid('{fa39cd94-bc64-4ab1-9b71-dcd09d5a7e7a}')
MFAudioFormat_LPCM: Guid = Guid('{e06d8032-db46-11cf-b4d1-00805f6cbbea}')
MFAudioFormat_PCM_HDCP: Guid = Guid('{a5e7ff01-8411-4acc-a865-5f4941288d80}')
MFAudioFormat_Dolby_AC3_HDCP: Guid = Guid('{97663a80-8ffb-4445-a6ba-792d908f497f}')
MFAudioFormat_AAC_HDCP: Guid = Guid('{419bce76-8b72-400f-adeb-84b57d63484d}')
MFAudioFormat_ADTS_HDCP: Guid = Guid('{da4963a3-14d8-4dcf-92b7-193eb84363db}')
MFAudioFormat_Base_HDCP: Guid = Guid('{3884b5bc-e277-43fd-983d-038aa8d9b605}')
MFVideoFormat_H264_HDCP: Guid = Guid('{5d0ce9dd-9817-49da-bdfd-f5f5b98f18a6}')
MFVideoFormat_HEVC_HDCP: Guid = Guid('{3cfe0fe6-05c4-47dc-9d70-4bdb2959720f}')
MFVideoFormat_Base_HDCP: Guid = Guid('{eac3b9d5-bd14-4237-8f1f-bab428e49312}')
MFMPEG4Format_Base: Guid = Guid('{00000000-767a-494d-b478-f29d25dc9037}')
MFSubtitleFormat_XML: Guid = Guid('{2006f94f-29ca-4195-b8db-00ded8ff0c97}')
MFSubtitleFormat_TTML: Guid = Guid('{73e73992-9a10-4356-9557-7194e91e3e54}')
MFSubtitleFormat_ATSC: Guid = Guid('{7fa7faa3-feae-4e16-aedf-36b9acfbb099}')
MFSubtitleFormat_WebVTT: Guid = Guid('{c886d215-f485-40bb-8db6-fadbc619a45d}')
MFSubtitleFormat_SRT: Guid = Guid('{5e467f2e-77ca-4ca5-8391-d142ed4b76c8}')
MFSubtitleFormat_SSA: Guid = Guid('{57176a1b-1a9e-4eea-abef-c61760198ac4}')
MFSubtitleFormat_CustomUserData: Guid = Guid('{1bb3d849-6614-4d80-8882-ed24aa82da92}')
MFSubtitleFormat_PGS: Guid = Guid('{71f40e4a-1278-4442-b30d-39dd1d7722bc}')
MFSubtitleFormat_VobSub: Guid = Guid('{6b8e40f4-8d2c-4ced-ad91-5960e45b4433}')
MF_MT_MAJOR_TYPE: Guid = Guid('{48eba18e-f8c9-4687-bf11-0a74c9f96a8f}')
MF_MT_SUBTYPE: Guid = Guid('{f7e34c9a-42e8-4714-b74b-cb29d72c35e5}')
MF_MT_ALL_SAMPLES_INDEPENDENT: Guid = Guid('{c9173739-5e56-461c-b713-46fb995cb95f}')
MF_MT_FIXED_SIZE_SAMPLES: Guid = Guid('{b8ebefaf-b718-4e04-b0a9-116775e3321b}')
MF_MT_COMPRESSED: Guid = Guid('{3afd0cee-18f2-4ba5-a110-8bea502e1f92}')
MF_MT_SAMPLE_SIZE: Guid = Guid('{dad3ab78-1990-408b-bce2-eba673dacc10}')
MF_MT_WRAPPED_TYPE: Guid = Guid('{4d3f7b23-d02f-4e6c-9bee-e4bf2c6c695d}')
MF_MT_VIDEO_3D: Guid = Guid('{cb5e88cf-7b5b-476b-85aa-1ca5ae187555}')
MF_MT_VIDEO_3D_FORMAT: Guid = Guid('{5315d8a0-87c5-4697-b793-6606c67c049b}')
MF_MT_VIDEO_3D_NUM_VIEWS: Guid = Guid('{bb077e8a-dcbf-42eb-af60-418df98aa495}')
MF_MT_VIDEO_3D_LEFT_IS_BASE: Guid = Guid('{6d4b7bff-5629-4404-948c-c634f4ce26d4}')
MF_MT_VIDEO_3D_FIRST_IS_LEFT: Guid = Guid('{ec298493-0ada-4ea1-a4fe-cbbd36ce9331}')
MFSampleExtension_3DVideo: Guid = Guid('{f86f97a4-dd54-4e2e-9a5e-55fc2d74a005}')
MFSampleExtension_3DVideo_SampleFormat: Guid = Guid('{08671772-e36f-4cff-97b3-d72e20987a48}')
MF_MT_VIDEO_ROTATION: Guid = Guid('{c380465d-2271-428c-9b83-ecea3b4a85c1}')
MF_DEVICESTREAM_MULTIPLEXED_MANAGER: Guid = Guid('{6ea542b0-281f-4231-a464-fe2f5022501c}')
MF_MEDIATYPE_MULTIPLEXED_MANAGER: Guid = Guid('{13c78fb5-f275-4ea0-bb5f-0249832b0d6e}')
MFSampleExtension_MULTIPLEXED_MANAGER: Guid = Guid('{8dcdee79-6b5a-4c45-8db9-20b395f02fcf}')
MF_MT_SECURE: Guid = Guid('{c5acc4fd-0304-4ecf-809f-47bc97ff63bd}')
MF_DEVICESTREAM_ATTRIBUTE_FRAMESOURCE_TYPES: Guid = Guid('{17145fd1-1b2b-423c-8001-2b6833ed3588}')
MF_MT_ALPHA_MODE: Guid = Guid('{5d959b0d-4cbf-4d04-919f-3f5f7f284211}')
MF_MT_DEPTH_MEASUREMENT: Guid = Guid('{fd5ac489-0917-4bb6-9d54-3122bf70144b}')
MF_MT_DEPTH_VALUE_UNIT: Guid = Guid('{21a800f5-3189-4797-beba-f13cd9a31a5e}')
MF_MT_VIDEO_NO_FRAME_ORDERING: Guid = Guid('{3f5b106f-6bc2-4ee3-b7ed-8902c18f5351}')
MF_MT_VIDEO_H264_NO_FMOASO: Guid = Guid('{ed461cd6-ec9f-416a-a8a3-26d7d31018d7}')
MFSampleExtension_ForwardedDecodeUnits: Guid = Guid('{424c754c-97c8-48d6-8777-fc41f7b60879}')
MFSampleExtension_TargetGlobalLuminance: Guid = Guid('{3f60ef36-31ef-4daf-8360-940397e41ef3}')
MFSampleExtension_ForwardedDecodeUnitType: Guid = Guid('{089e57c7-47d3-4a26-bf9c-4b64fafb5d1e}')
MF_MT_FORWARD_CUSTOM_NALU: Guid = Guid('{ed336efd-244f-428d-9153-28f399458890}')
MF_MT_FORWARD_CUSTOM_SEI: Guid = Guid('{e27362f1-b136-41d1-9594-3a7e4febf2d1}')
MF_MT_VIDEO_RENDERER_EXTENSION_PROFILE: Guid = Guid('{8437d4b9-d448-4fcd-9b6b-839bf96c7798}')
MF_DECODER_FWD_CUSTOM_SEI_DECODE_ORDER: Guid = Guid('{f13bbe3c-36d4-410a-b985-7a951a1e6294}')
MF_VIDEO_RENDERER_EFFECT_APP_SERVICE_NAME: Guid = Guid('{c6052a80-6d9c-40a3-9db8-f027a25c9ab9}')
MF_MT_AUDIO_NUM_CHANNELS: Guid = Guid('{37e48bf5-645e-4c5b-89de-ada9e29b696a}')
MF_MT_AUDIO_SAMPLES_PER_SECOND: Guid = Guid('{5faeeae7-0290-4c31-9e8a-c534f68d9dba}')
MF_MT_AUDIO_FLOAT_SAMPLES_PER_SECOND: Guid = Guid('{fb3b724a-cfb5-4319-aefe-6e42b2406132}')
MF_MT_AUDIO_AVG_BYTES_PER_SECOND: Guid = Guid('{1aab75c8-cfef-451c-ab95-ac034b8e1731}')
MF_MT_AUDIO_BLOCK_ALIGNMENT: Guid = Guid('{322de230-9eeb-43bd-ab7a-ff412251541d}')
MF_MT_AUDIO_BITS_PER_SAMPLE: Guid = Guid('{f2deb57f-40fa-4764-aa33-ed4f2d1ff669}')
MF_MT_AUDIO_VALID_BITS_PER_SAMPLE: Guid = Guid('{d9bf8d6a-9530-4b7c-9ddf-ff6fd58bbd06}')
MF_MT_AUDIO_SAMPLES_PER_BLOCK: Guid = Guid('{aab15aac-e13a-4995-9222-501ea15c6877}')
MF_MT_AUDIO_CHANNEL_MASK: Guid = Guid('{55fb5765-644a-4caf-8479-938983bb1588}')
MF_MT_AUDIO_FOLDDOWN_MATRIX: Guid = Guid('{9d62927c-36be-4cf2-b5c4-a3926e3e8711}')
MF_MT_AUDIO_WMADRC_PEAKREF: Guid = Guid('{9d62927d-36be-4cf2-b5c4-a3926e3e8711}')
MF_MT_AUDIO_WMADRC_PEAKTARGET: Guid = Guid('{9d62927e-36be-4cf2-b5c4-a3926e3e8711}')
MF_MT_AUDIO_WMADRC_AVGREF: Guid = Guid('{9d62927f-36be-4cf2-b5c4-a3926e3e8711}')
MF_MT_AUDIO_WMADRC_AVGTARGET: Guid = Guid('{9d629280-36be-4cf2-b5c4-a3926e3e8711}')
MF_MT_AUDIO_PREFER_WAVEFORMATEX: Guid = Guid('{a901aaba-e037-458a-bdf6-545be2074042}')
MF_MT_AAC_PAYLOAD_TYPE: Guid = Guid('{bfbabe79-7434-4d1c-94f0-72a3b9e17188}')
MF_MT_AAC_AUDIO_PROFILE_LEVEL_INDICATION: Guid = Guid('{7632f0e6-9538-4d61-acda-ea29c8c14456}')
MF_MT_AUDIO_FLAC_MAX_BLOCK_SIZE: Guid = Guid('{8b81adae-4b5a-4d40-8022-f38d09ca3c5c}')
MF_MT_SPATIAL_AUDIO_MAX_DYNAMIC_OBJECTS: Guid = Guid('{dcfba24a-2609-4240-a721-3faea76a4df9}')
MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_FORMAT_ID: Guid = Guid('{2ab71bc0-6223-4ba7-ad64-7b94b47ae792}')
MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_LENGTH: Guid = Guid('{094ba8be-d723-489f-92fa-766777b34726}')
MF_MT_SPATIAL_AUDIO_MAX_METADATA_ITEMS: Guid = Guid('{11aa80b4-e0da-47c6-8060-96c1259ae50d}')
MF_MT_SPATIAL_AUDIO_MIN_METADATA_ITEM_OFFSET_SPACING: Guid = Guid('{83e96ec9-1184-417e-8254-9f269158fc06}')
MF_MT_SPATIAL_AUDIO_DATA_PRESENT: Guid = Guid('{6842f6e7-d43e-4ebb-9c9c-c96f41784863}')
MF_MT_FRAME_SIZE: Guid = Guid('{1652c33d-d6b2-4012-b834-72030849a37d}')
MF_MT_FRAME_RATE: Guid = Guid('{c459a2e8-3d2c-4e44-b132-fee5156c7bb0}')
MF_MT_PIXEL_ASPECT_RATIO: Guid = Guid('{c6376a1e-8d0a-4027-be45-6d9a0ad39bb6}')
MF_MT_DRM_FLAGS: Guid = Guid('{8772f323-355a-4cc7-bb78-6d61a048ae82}')
MF_MT_TIMESTAMP_CAN_BE_DTS: Guid = Guid('{24974215-1b7b-41e4-8625-ac469f2dedaa}')
MF_MT_PAD_CONTROL_FLAGS: Guid = Guid('{4d0e73e5-80ea-4354-a9d0-1176ceb028ea}')
MF_MT_SOURCE_CONTENT_HINT: Guid = Guid('{68aca3cc-22d0-44e6-85f8-28167197fa38}')
MF_MT_VIDEO_CHROMA_SITING: Guid = Guid('{65df2370-c773-4c33-aa64-843e068efb0c}')
MF_MT_INTERLACE_MODE: Guid = Guid('{e2724bb8-e676-4806-b4b2-a8d6efb44ccd}')
MF_MT_TRANSFER_FUNCTION: Guid = Guid('{5fb0fce9-be5c-4935-a811-ec838f8eed93}')
MF_MT_VIDEO_PRIMARIES: Guid = Guid('{dbfbe4d7-0740-4ee0-8192-850ab0e21935}')
MF_MT_MAX_LUMINANCE_LEVEL: Guid = Guid('{50253128-c110-4de4-98ae-46a324fae6da}')
MF_MT_MAX_FRAME_AVERAGE_LUMINANCE_LEVEL: Guid = Guid('{58d4bf57-6f52-4733-a195-a9e29ecf9e27}')
MF_MT_MAX_MASTERING_LUMINANCE: Guid = Guid('{d6c6b997-272f-4ca1-8d00-8042111a0ff6}')
MF_MT_MIN_MASTERING_LUMINANCE: Guid = Guid('{839a4460-4e7e-4b4f-ae79-cc08905c7b27}')
MF_MT_DECODER_USE_MAX_RESOLUTION: Guid = Guid('{4c547c24-af9a-4f38-96ad-978773cf53e7}')
MF_MT_DECODER_MAX_DPB_COUNT: Guid = Guid('{67be144c-88b7-4ca9-9628-c808d5262217}')
MF_MT_CUSTOM_VIDEO_PRIMARIES: Guid = Guid('{47537213-8cfb-4722-aa34-fbc9e24d77b8}')
MF_MT_YUV_MATRIX: Guid = Guid('{3e23d450-2c75-4d25-a00e-b91670d12327}')
MF_MT_VIDEO_LIGHTING: Guid = Guid('{53a0529c-890b-4216-8bf9-599367ad6d20}')
MF_MT_VIDEO_NOMINAL_RANGE: Guid = Guid('{c21b8ee5-b956-4071-8daf-325edf5cab11}')
MF_MT_GEOMETRIC_APERTURE: Guid = Guid('{66758743-7e5f-400d-980a-aa8596c85696}')
MF_MT_MINIMUM_DISPLAY_APERTURE: Guid = Guid('{d7388766-18fe-48c6-a177-ee894867c8c4}')
MF_MT_PAN_SCAN_APERTURE: Guid = Guid('{79614dde-9187-48fb-b8c7-4d52689de649}')
MF_MT_PAN_SCAN_ENABLED: Guid = Guid('{4b7f6bc3-8b13-40b2-a993-abf630b8204e}')
MF_MT_AVG_BITRATE: Guid = Guid('{20332624-fb0d-4d9e-bd0d-cbf6786c102e}')
MF_MT_AVG_BIT_ERROR_RATE: Guid = Guid('{799cabd6-3508-4db4-a3c7-569cd533deb1}')
MF_MT_MAX_KEYFRAME_SPACING: Guid = Guid('{c16eb52b-73a1-476f-8d62-839d6a020652}')
MF_MT_USER_DATA: Guid = Guid('{b6bc765f-4c3b-40a4-bd51-2535b66fe09d}')
MF_MT_OUTPUT_BUFFER_NUM: Guid = Guid('{a505d3ac-f930-436e-8ede-93a509ce23b2}')
MF_MT_REALTIME_CONTENT: Guid = Guid('{bb12d222-2bdb-425e-91ec-2308e189a58f}')
MF_MT_DEFAULT_STRIDE: Guid = Guid('{644b4e48-1e02-4516-b0eb-c01ca9d49ac6}')
MF_MT_PALETTE: Guid = Guid('{6d283f42-9846-4410-afd9-654d503b1a54}')
MF_MT_AM_FORMAT_TYPE: Guid = Guid('{73d1072d-1870-4174-a063-29ff4ff6c11e}')
MF_MT_VIDEO_PROFILE: Guid = Guid('{ad76a80b-2d5c-4e0b-b375-64e520137036}')
MF_MT_VIDEO_LEVEL: Guid = Guid('{96f66574-11c5-4015-8666-bff516436da7}')
MF_MT_MPEG_START_TIME_CODE: Guid = Guid('{91f67885-4333-4280-97cd-bd5a6c03a06e}')
MF_MT_MPEG2_PROFILE: Guid = Guid('{ad76a80b-2d5c-4e0b-b375-64e520137036}')
MF_MT_MPEG2_LEVEL: Guid = Guid('{96f66574-11c5-4015-8666-bff516436da7}')
MF_MT_MPEG2_FLAGS: Guid = Guid('{31e3991d-f701-4b2f-b426-8ae3bda9e04b}')
MF_MT_MPEG_SEQUENCE_HEADER: Guid = Guid('{3c036de7-3ad0-4c9e-9216-ee6d6ac21cb3}')
MF_MT_MPEG2_STANDARD: Guid = Guid('{a20af9e8-928a-4b26-aaa9-f05c74cac47c}')
MF_MT_MPEG2_TIMECODE: Guid = Guid('{5229ba10-e29d-4f80-a59c-df4f180207d2}')
MF_MT_MPEG2_CONTENT_PACKET: Guid = Guid('{825d55e4-4f12-4197-9eb3-59b6e4710f06}')
MF_MT_MPEG2_ONE_FRAME_PER_PACKET: Guid = Guid('{91a49eb5-1d20-4b42-ace8-804269bf95ed}')
MF_MT_MPEG2_HDCP: Guid = Guid('{168f1b4a-3e91-450f-aea7-e4baeadae5ba}')
MF_MT_H264_MAX_CODEC_CONFIG_DELAY: Guid = Guid('{f5929986-4c45-4fbb-bb49-6cc534d05b9b}')
MF_MT_H264_SUPPORTED_SLICE_MODES: Guid = Guid('{c8be1937-4d64-4549-8343-a8086c0bfda5}')
MF_MT_H264_SUPPORTED_SYNC_FRAME_TYPES: Guid = Guid('{89a52c01-f282-48d2-b522-22e6ae633199}')
MF_MT_H264_RESOLUTION_SCALING: Guid = Guid('{e3854272-f715-4757-ba90-1b696c773457}')
MF_MT_H264_SIMULCAST_SUPPORT: Guid = Guid('{9ea2d63d-53f0-4a34-b94e-9de49a078cb3}')
MF_MT_H264_SUPPORTED_RATE_CONTROL_MODES: Guid = Guid('{6a8ac47e-519c-4f18-9bb3-7eeaaea5594d}')
MF_MT_H264_MAX_MB_PER_SEC: Guid = Guid('{45256d30-7215-4576-9336-b0f1bcd59bb2}')
MF_MT_H264_SUPPORTED_USAGES: Guid = Guid('{60b1a998-dc01-40ce-9736-aba845a2dbdc}')
MF_MT_H264_CAPABILITIES: Guid = Guid('{bb3bd508-490a-11e0-99e4-1316dfd72085}')
MF_MT_H264_SVC_CAPABILITIES: Guid = Guid('{f8993abe-d937-4a8f-bbca-6966fe9e1152}')
MF_MT_H264_USAGE: Guid = Guid('{359ce3a5-af00-49ca-a2f4-2ac94ca82b61}')
MF_MT_H264_RATE_CONTROL_MODES: Guid = Guid('{705177d8-45cb-11e0-ac7d-b91ce0d72085}')
MF_MT_H264_LAYOUT_PER_STREAM: Guid = Guid('{85e299b2-90e3-4fe8-b2f5-c067e0bfe57a}')
MF_MT_IN_BAND_PARAMETER_SET: Guid = Guid('{75da5090-910b-4a03-896c-7b898feea5af}')
MF_MT_MPEG4_TRACK_TYPE: Guid = Guid('{54f486dd-9327-4f6d-80ab-6f709ebb4cce}')
MF_MT_CONTAINER_RATE_SCALING: Guid = Guid('{83877f5e-0444-4e28-8479-6db0989b8c09}')
MF_MT_DV_AAUX_SRC_PACK_0: Guid = Guid('{84bd5d88-0fb8-4ac8-be4b-a8848bef98f3}')
MF_MT_DV_AAUX_CTRL_PACK_0: Guid = Guid('{f731004e-1dd1-4515-aabe-f0c06aa536ac}')
MF_MT_DV_AAUX_SRC_PACK_1: Guid = Guid('{720e6544-0225-4003-a651-0196563a958e}')
MF_MT_DV_AAUX_CTRL_PACK_1: Guid = Guid('{cd1f470d-1f04-4fe0-bfb9-d07ae0386ad8}')
MF_MT_DV_VAUX_SRC_PACK: Guid = Guid('{41402d9d-7b57-43c6-b129-2cb997f15009}')
MF_MT_DV_VAUX_CTRL_PACK: Guid = Guid('{2f84e1c4-0da1-4788-938e-0dfbfbb34b48}')
MF_MT_ARBITRARY_HEADER: Guid = Guid('{9e6bd6f5-0109-4f95-84ac-9309153a19fc}')
MF_MT_ARBITRARY_FORMAT: Guid = Guid('{5a75b249-0d7d-49a1-a1c3-e0d87f0cade5}')
MF_MT_IMAGE_LOSS_TOLERANT: Guid = Guid('{ed062cf4-e34e-4922-be99-934032133d7c}')
MF_MT_MPEG4_SAMPLE_DESCRIPTION: Guid = Guid('{261e9d83-9529-4b8f-a111-8b9c950a81a9}')
MF_MT_MPEG4_CURRENT_SAMPLE_ENTRY: Guid = Guid('{9aa7e155-b64a-4c1d-a500-455d600b6560}')
MF_SD_AMBISONICS_SAMPLE3D_DESCRIPTION: Guid = Guid('{f715cf3e-a964-4c3f-94ae-9d6ba7264641}')
MF_MT_ORIGINAL_4CC: Guid = Guid('{d7be3fe0-2bc7-492d-b843-61a1919b70c3}')
MF_MT_ORIGINAL_WAVE_FORMAT_TAG: Guid = Guid('{8cbbc843-9fd9-49c2-882f-a72586c408ad}')
MF_MT_FRAME_RATE_RANGE_MIN: Guid = Guid('{d2e7558c-dc1f-403f-9a72-d28bb1eb3b5e}')
MF_MT_FRAME_RATE_RANGE_MAX: Guid = Guid('{e3371d41-b4cf-4a05-bd4e-20b88bb2c4d6}')
MF_LOW_LATENCY: Guid = Guid('{9c27891a-ed7a-40e1-88e8-b22727a024ee}')
MF_VIDEO_MAX_MB_PER_SEC: Guid = Guid('{e3f2e203-d445-4b8c-9211-ae390d3ba017}')
MF_DISABLE_FRAME_CORRUPTION_INFO: Guid = Guid('{7086e16c-49c5-4201-882a-8538f38cf13a}')
MFStreamExtension_CameraExtrinsics: Guid = Guid('{686196d0-13e2-41d9-9638-ef032c272a52}')
MFSampleExtension_CameraExtrinsics: Guid = Guid('{6b761658-b7ec-4c3b-8225-8623cabec31d}')
MFStreamExtension_PinholeCameraIntrinsics: Guid = Guid('{dbac0455-0ec8-4aef-9c32-7a3ee3456f53}')
MFSampleExtension_PinholeCameraIntrinsics: Guid = Guid('{4ee3b6c5-6a15-4e72-9761-70c1db8b9fe3}')
MFMediaType_Default: Guid = Guid('{81a412e6-8103-4b06-857f-1862781024ac}')
MFMediaType_Audio: Guid = Guid('{73647561-0000-0010-8000-00aa00389b71}')
MFMediaType_Video: Guid = Guid('{73646976-0000-0010-8000-00aa00389b71}')
MFMediaType_Protected: Guid = Guid('{7b4b6fe6-9d04-4494-be14-7e0bd076c8e4}')
MFMediaType_SAMI: Guid = Guid('{e69669a0-3dcd-40cb-9e2e-3708387c0616}')
MFMediaType_Script: Guid = Guid('{72178c22-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFMediaType_Image: Guid = Guid('{72178c23-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFMediaType_HTML: Guid = Guid('{72178c24-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFMediaType_Binary: Guid = Guid('{72178c25-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFMediaType_FileTransfer: Guid = Guid('{72178c26-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFMediaType_Stream: Guid = Guid('{e436eb83-524f-11ce-9f53-0020af0ba770}')
MFMediaType_MultiplexedFrames: Guid = Guid('{6ea542b0-281f-4231-a464-fe2f5022501c}')
MFMediaType_Subtitle: Guid = Guid('{a6d13581-ed50-4e65-ae08-26065576aacc}')
MFMediaType_Perception: Guid = Guid('{597ff6f9-6ea2-4670-85b4-ea84073fe940}')
MFImageFormat_JPEG: Guid = Guid('{19e4a5aa-5662-4fc5-a0c0-1758028e1057}')
MFImageFormat_RGB32: Guid = Guid('{00000016-0000-0010-8000-00aa00389b71}')
MFStreamFormat_MPEG2Transport: Guid = Guid('{e06d8023-db46-11cf-b4d1-00805f6cbbea}')
MFStreamFormat_MPEG2Program: Guid = Guid('{263067d1-d330-45dc-b669-34d986e4e3e1}')
AM_MEDIA_TYPE_REPRESENTATION: Guid = Guid('{e2e42ad2-132c-491e-a268-3c7c2dca181f}')
FORMAT_MFVideoFormat: Guid = Guid('{aed4ab2d-7326-43cb-9464-c879cab9c43d}')
MFMediaType_Metadata: Guid = Guid('{2c8fa20c-82bb-4782-90a0-98a2a5bd8ef8}')
CLSID_MFSourceResolver: Guid = Guid('{90eab60f-e43a-4188-bcc4-e47fdf04868c}')
MF_DEVICESTREAM_ATTRIBUTE_FACEAUTH_CAPABILITY: Guid = Guid('{cb6fd12a-2248-4e41-ad46-e78bb90ab9fc}')
MF_DEVICESTREAM_ATTRIBUTE_SECURE_CAPABILITY: Guid = Guid('{940fd626-ea6e-4684-9840-36bd6ec9fbef}')
MEDIASINK_FIXED_STREAMS: UInt32 = 1
MEDIASINK_CANNOT_MATCH_CLOCK: UInt32 = 2
MEDIASINK_RATELESS: UInt32 = 4
MEDIASINK_CLOCK_REQUIRED: UInt32 = 8
MEDIASINK_CAN_PREROLL: UInt32 = 16
MEDIASINK_REQUIRE_REFERENCE_MEDIATYPE: UInt32 = 32
MFCLOCK_FREQUENCY_HNS: UInt32 = 10000000
MFCLOCK_TOLERANCE_UNKNOWN: UInt32 = 50000
MFCLOCK_JITTER_ISR: UInt32 = 1000
MFCLOCK_JITTER_DPC: UInt32 = 4000
MFCLOCK_JITTER_PASSIVE: UInt32 = 10000
PRESENTATION_CURRENT_POSITION: UInt64 = 9223372036854775807
MF_PD_ADAPTIVE_STREAMING: Guid = Guid('{ea0d5d97-29f9-488b-ae6b-7d6b4136112b}')
MF_AUDIO_RENDERER_ATTRIBUTE_FLAGS_CROSSPROCESS: UInt32 = 1
MF_AUDIO_RENDERER_ATTRIBUTE_FLAGS_NOPERSIST: UInt32 = 2
MF_AUDIO_RENDERER_ATTRIBUTE_FLAGS_DONT_ALLOW_FORMAT_CHANGES: UInt32 = 4
MFRR_INFO_VERSION: UInt32 = 0
MF_USER_MODE_COMPONENT_LOAD: UInt32 = 1
MF_KERNEL_MODE_COMPONENT_LOAD: UInt32 = 2
MF_GRL_LOAD_FAILED: UInt32 = 16
MF_INVALID_GRL_SIGNATURE: UInt32 = 32
MF_GRL_ABSENT: UInt32 = 4096
MF_COMPONENT_REVOKED: UInt32 = 8192
MF_COMPONENT_INVALID_EKU: UInt32 = 16384
MF_COMPONENT_CERT_REVOKED: UInt32 = 32768
MF_COMPONENT_INVALID_ROOT: UInt32 = 65536
MF_COMPONENT_HS_CERT_REVOKED: UInt32 = 131072
MF_COMPONENT_LS_CERT_REVOKED: UInt32 = 262144
MF_BOOT_DRIVER_VERIFICATION_FAILED: UInt32 = 1048576
MF_TEST_SIGNED_COMPONENT_LOADING: UInt32 = 16777216
MF_MINCRYPT_FAILURE: UInt32 = 268435456
SHA_HASH_LEN: UInt32 = 20
MFSEQUENCER_INVALID_ELEMENT_ID: UInt32 = 4294967295
MF_WRAPPED_BUFFER_SERVICE: Guid = Guid('{ab544072-c269-4ebc-a552-1c3b32bed5ca}')
CLSID_MPEG2ByteStreamPlugin: Guid = Guid('{40871c59-ab40-471f-8dc3-1f259d862479}')
MFCONTENTPROTECTIONDEVICE_FUNCTIONID_START: UInt32 = 67108864
MFCONTENTPROTECTIONDEVICE_REALTIMECLIENT_DATA_FUNCTIONID: UInt32 = 67108864
MF_UNKNOWN_DURATION: UInt32 = 0
MFStreamExtension_ExtendedCameraIntrinsics: Guid = Guid('{aa74b3df-9a2c-48d6-8393-5bd1c1a81e6e}')
MFSampleExtension_ExtendedCameraIntrinsics: Guid = Guid('{560bc4a5-4de0-4113-9cdc-832db9740f3d}')
MF_INVALID_PRESENTATION_TIME: UInt64 = 9223372036854775808
MF_MEDIATYPE_EQUAL_MAJOR_TYPES: UInt32 = 1
MF_MEDIATYPE_EQUAL_FORMAT_TYPES: UInt32 = 2
MF_MEDIATYPE_EQUAL_FORMAT_DATA: UInt32 = 4
MF_MEDIATYPE_EQUAL_FORMAT_USER_DATA: UInt32 = 8
MFASYNC_FAST_IO_PROCESSING_CALLBACK: UInt32 = 1
MFASYNC_SIGNAL_CALLBACK: UInt32 = 2
MFASYNC_BLOCKING_CALLBACK: UInt32 = 4
MFASYNC_REPLY_CALLBACK: UInt32 = 8
MFASYNC_LOCALIZE_REMOTE_CALLBACK: UInt32 = 16
MFASYNC_CALLBACK_QUEUE_UNDEFINED: UInt32 = 0
MFASYNC_CALLBACK_QUEUE_STANDARD: UInt32 = 1
MFASYNC_CALLBACK_QUEUE_RT: UInt32 = 2
MFASYNC_CALLBACK_QUEUE_IO: UInt32 = 3
MFASYNC_CALLBACK_QUEUE_TIMER: UInt32 = 4
MFASYNC_CALLBACK_QUEUE_MULTITHREADED: UInt32 = 5
MFASYNC_CALLBACK_QUEUE_LONG_FUNCTION: UInt32 = 7
MFASYNC_CALLBACK_QUEUE_PRIVATE_MASK: UInt32 = 4294901760
MFASYNC_CALLBACK_QUEUE_ALL: UInt32 = 4294967295
MFBYTESTREAM_IS_READABLE: UInt32 = 1
MFBYTESTREAM_IS_WRITABLE: UInt32 = 2
MFBYTESTREAM_IS_SEEKABLE: UInt32 = 4
MFBYTESTREAM_IS_REMOTE: UInt32 = 8
MFBYTESTREAM_IS_DIRECTORY: UInt32 = 128
MFBYTESTREAM_HAS_SLOW_SEEK: UInt32 = 256
MFBYTESTREAM_IS_PARTIALLY_DOWNLOADED: UInt32 = 512
MFBYTESTREAM_SHARE_WRITE: UInt32 = 1024
MFBYTESTREAM_DOES_NOT_USE_NETWORK: UInt32 = 2048
MFBYTESTREAM_SEEK_FLAG_CANCEL_PENDING_IO: UInt32 = 1
MF_MEDIA_SHARING_ENGINE_INITIAL_SEEK_TIME: Guid = Guid('{6f3497f5-d528-4a4f-8dd7-db36657ec4c9}')
MF_SHUTDOWN_RENDERER_ON_ENGINE_SHUTDOWN: Guid = Guid('{c112d94d-6b9c-48f8-b6f9-7950ff9ab71e}')
MF_PREFERRED_SOURCE_URI: Guid = Guid('{5fc85488-436a-4db8-90af-4db402ae5c57}')
MF_SHARING_ENGINE_SHAREDRENDERER: Guid = Guid('{efa446a0-73e7-404e-8ae2-fef60af5a32b}')
MF_SHARING_ENGINE_CALLBACK: Guid = Guid('{57dc1e95-d252-43fa-9bbc-180070eefe6d}')
MFT_STREAMS_UNLIMITED: UInt32 = 4294967295
MFT_OUTPUT_BOUND_UPPER_UNBOUNDED: UInt64 = 9223372036854775807
OPM_GET_CURRENT_HDCP_SRM_VERSION: Guid = Guid('{99c5ceff-5f1d-4879-81c1-c52443c9482b}')
OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION: Guid = Guid('{0db59d74-a992-492e-a0bd-c23fda564e00}')
OPM_GET_ACP_AND_CGMSA_SIGNALING: Guid = Guid('{6629a591-3b79-4cf3-924a-11e8e7811671}')
OPM_GET_CONNECTOR_TYPE: Guid = Guid('{81d0bfd5-6afe-48c2-99c0-95a08f97c5da}')
OPM_GET_SUPPORTED_PROTECTION_TYPES: Guid = Guid('{38f2a801-9a6c-48bb-9107-b6696e6f1797}')
OPM_GET_VIRTUAL_PROTECTION_LEVEL: Guid = Guid('{b2075857-3eda-4d5d-88db-748f8c1a0549}')
OPM_GET_ACTUAL_PROTECTION_LEVEL: Guid = Guid('{1957210a-7766-452a-b99a-d27aed54f03a}')
OPM_GET_ACTUAL_OUTPUT_FORMAT: Guid = Guid('{d7bf1ba3-ad13-4f8e-af98-0dcb3ca204cc}')
OPM_GET_ADAPTER_BUS_TYPE: Guid = Guid('{c6f4d673-6174-4184-8e35-f6db5200bcba}')
OPM_GET_OUTPUT_ID: Guid = Guid('{72cb6df3-244f-40ce-b09e-20506af6302f}')
OPM_GET_DVI_CHARACTERISTICS: Guid = Guid('{a470b3bb-5dd7-4172-839c-3d3776e0ebf5}')
OPM_GET_CODEC_INFO: Guid = Guid('{4f374491-8f5f-4445-9dba-95588f6b58b4}')
OPM_GET_OUTPUT_HARDWARE_PROTECTION_SUPPORT: Guid = Guid('{3b129589-2af8-4ef0-96a2-704a845a218e}')
OPM_SET_PROTECTION_LEVEL: Guid = Guid('{9bb9327c-4eb5-4727-9f00-b42b0919c0da}')
OPM_SET_ACP_AND_CGMSA_SIGNALING: Guid = Guid('{09a631a5-d684-4c60-8e4d-d3bb0f0be3ee}')
OPM_SET_HDCP_SRM: Guid = Guid('{8b5ef5d1-c30d-44ff-84a5-ea71dce78f13}')
OPM_SET_PROTECTION_LEVEL_ACCORDING_TO_CSS_DVD: Guid = Guid('{39ce333e-4cc0-44ae-bfcc-da50b5f82e72}')
WM_CODEC_ONEPASS_CBR: UInt32 = 1
WM_CODEC_ONEPASS_VBR: UInt32 = 2
WM_CODEC_TWOPASS_CBR: UInt32 = 4
WM_CODEC_TWOPASS_VBR_UNCONSTRAINED: UInt32 = 8
WM_CODEC_TWOPASS_VBR_PEAKCONSTRAINED: UInt32 = 16
SYSFXUI_DONOTSHOW_LOUDNESSEQUALIZATION: UInt32 = 1
SYSFXUI_DONOTSHOW_ROOMCORRECTION: UInt32 = 2
SYSFXUI_DONOTSHOW_BASSMANAGEMENT: UInt32 = 4
SYSFXUI_DONOTSHOW_BASSBOOST: UInt32 = 8
SYSFXUI_DONOTSHOW_HEADPHONEVIRTUALIZATION: UInt32 = 16
SYSFXUI_DONOTSHOW_VIRTUALSURROUND: UInt32 = 32
SYSFXUI_DONOTSHOW_SPEAKERFILLING: UInt32 = 64
SYSFXUI_DONOTSHOW_CHANNELPHANTOMING: UInt32 = 128
AEC_MAX_SYSTEM_MODES: UInt32 = 6
WMAAECMA_E_NO_ACTIVE_RENDER_STREAM: UInt32 = 2278293514
MEDIASUBTYPE_Y41T: Guid = Guid('{54313459-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_Y42T: Guid = Guid('{54323459-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_V216: Guid = Guid('{36313256-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_V410: Guid = Guid('{30313456-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_v210: Guid = Guid('{30313276-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_I420: Guid = Guid('{30323449-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WVC1: Guid = Guid('{31435657-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMVA: Guid = Guid('{41564d57-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMVB: Guid = Guid('{42564d57-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMVR: Guid = Guid('{52564d57-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMVP: Guid = Guid('{50564d57-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WVP2: Guid = Guid('{32505657-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMV3: Guid = Guid('{33564d57-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMV2: Guid = Guid('{32564d57-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMV1: Guid = Guid('{31564d57-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MPG4: Guid = Guid('{3447504d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MP42: Guid = Guid('{3234504d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MP43: Guid = Guid('{3334504d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MP4S: Guid = Guid('{5334504d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_M4S2: Guid = Guid('{3253344d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MSS1: Guid = Guid('{3153534d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MSS2: Guid = Guid('{3253534d-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MSAUDIO1: Guid = Guid('{00000160-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMAUDIO2: Guid = Guid('{00000161-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMAUDIO3: Guid = Guid('{00000162-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMAUDIO_LOSSLESS: Guid = Guid('{00000163-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMASPDIF: Guid = Guid('{00000164-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_WMAUDIO4: Guid = Guid('{00000168-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MPEG_ADTS_AAC: Guid = Guid('{00001600-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MPEG_RAW_AAC: Guid = Guid('{00001601-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MPEG_LOAS: Guid = Guid('{00001602-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_NOKIA_MPEG_ADTS_AAC: Guid = Guid('{00001608-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_NOKIA_MPEG_RAW_AAC: Guid = Guid('{00001609-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_VODAFONE_MPEG_ADTS_AAC: Guid = Guid('{0000160a-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_VODAFONE_MPEG_RAW_AAC: Guid = Guid('{0000160b-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_MPEG_HEAAC: Guid = Guid('{00001610-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RAW_AAC1: Guid = Guid('{000000ff-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_DVM: Guid = Guid('{00002000-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_DTS2: Guid = Guid('{00002001-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_DOLBY_DDPLUS: Guid = Guid('{a7fb87af-2d02-42fb-a4d4-05cd93843bdd}')
MEDIASUBTYPE_DOLBY_TRUEHD: Guid = Guid('{eb27cec4-163e-4ca3-8b74-8e25f91b517e}')
MEDIASUBTYPE_DTS_HD: Guid = Guid('{a2e58eb7-0fa9-48bb-a40c-fa0e156d0645}')
MEDIASUBTYPE_DTS_HD_HRA: Guid = Guid('{a61ac364-ad0e-4744-89ff-213ce0df8804}')
MEDIASUBTYPE_AVC1: Guid = Guid('{31435641-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_X264: Guid = Guid('{34363258-0000-0010-8000-00aa00389b71}')
MF_VIDEODSP_MODE: Guid = Guid('{16d720f0-768c-11de-8a39-0800200c9a66}')
MFSampleExtension_VideoDSPMode: Guid = Guid('{c12d55cb-d7d9-476d-81f3-69117f163ea0}')
CLSID_CTocEntry: Guid = Guid('{f22f5e05-585c-4def-8523-6555cfbc0cb3}')
CLSID_CTocEntryList: Guid = Guid('{3a8cccbc-0efd-43a3-b838-f38a552ba237}')
CLSID_CToc: Guid = Guid('{4fe24495-28ce-4920-a4c4-e556e1f0df2a}')
CLSID_CTocCollection: Guid = Guid('{5058292d-a244-4840-ab44-480975c4ffe4}')
CLSID_CTocParser: Guid = Guid('{499eaeea-2737-4849-8bb6-47f107eaf358}')
CLSID_CAsfTocParser: Guid = Guid('{9b77c0f2-8735-46c5-b90f-5f0b303ef6ab}')
CLSID_CAviTocParser: Guid = Guid('{3adce5cc-13c8-4573-b328-ed438eb694f9}')
CLSID_CFileIo: Guid = Guid('{11993195-1244-4840-ab44-480975c4ffe4}')
CLSID_CFileClient: Guid = Guid('{bfccd195-1244-4840-ab44-480975c4ffe4}')
CLSID_CClusterDetectorEx: Guid = Guid('{47354492-827e-4b8a-b318-c80eba1381f0}')
E_TOCPARSER_INVALIDASFFILE: Windows.Win32.Foundation.HRESULT = -1728053247
E_TOCPARSER_INVALIDRIFFFILE: Windows.Win32.Foundation.HRESULT = -1728053246
TOC_MAX_DESCRIPTION_SIZE: UInt32 = 65535
TOC_ENTRY_MAX_TITLE_SIZE: UInt32 = 65535
MFASFINDEXER_PER_ENTRY_BYTES_DYNAMIC: UInt32 = 65535
MFASFINDEXER_NO_FIXED_INTERVAL: UInt32 = 4294967295
MFASFINDEXER_READ_FOR_REVERSEPLAYBACK_OUTOFDATASEGMENT: UInt64 = 18446744073709551615
MFASFINDEXER_APPROX_SEEK_TIME_UNKNOWN: UInt64 = 18446744073709551615
MFASF_MAX_STREAM_NUMBER: UInt32 = 127
MFASF_INVALID_STREAM_NUMBER: UInt32 = 128
MFASF_PAYLOADEXTENSION_MAX_SIZE: UInt32 = 255
MFASF_PAYLOADEXTENSION_VARIABLE_SIZE: UInt32 = 65535
MFASF_DEFAULT_BUFFER_WINDOW_MS: UInt32 = 3000
FACILITY_MF: UInt32 = 13
FACILITY_MF_WIN32: UInt32 = 7
MF_E_PLATFORM_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -1072875856
MF_E_BUFFERTOOSMALL: Windows.Win32.Foundation.HRESULT = -1072875855
MF_E_INVALIDREQUEST: Windows.Win32.Foundation.HRESULT = -1072875854
MF_E_INVALIDSTREAMNUMBER: Windows.Win32.Foundation.HRESULT = -1072875853
MF_E_INVALIDMEDIATYPE: Windows.Win32.Foundation.HRESULT = -1072875852
MF_E_NOTACCEPTING: Windows.Win32.Foundation.HRESULT = -1072875851
MF_E_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -1072875850
MF_E_UNSUPPORTED_REPRESENTATION: Windows.Win32.Foundation.HRESULT = -1072875849
MF_E_NO_MORE_TYPES: Windows.Win32.Foundation.HRESULT = -1072875847
MF_E_UNSUPPORTED_SERVICE: Windows.Win32.Foundation.HRESULT = -1072875846
MF_E_UNEXPECTED: Windows.Win32.Foundation.HRESULT = -1072875845
MF_E_INVALIDNAME: Windows.Win32.Foundation.HRESULT = -1072875844
MF_E_INVALIDTYPE: Windows.Win32.Foundation.HRESULT = -1072875843
MF_E_INVALID_FILE_FORMAT: Windows.Win32.Foundation.HRESULT = -1072875842
MF_E_INVALIDINDEX: Windows.Win32.Foundation.HRESULT = -1072875841
MF_E_INVALID_TIMESTAMP: Windows.Win32.Foundation.HRESULT = -1072875840
MF_E_UNSUPPORTED_SCHEME: Windows.Win32.Foundation.HRESULT = -1072875837
MF_E_UNSUPPORTED_BYTESTREAM_TYPE: Windows.Win32.Foundation.HRESULT = -1072875836
MF_E_UNSUPPORTED_TIME_FORMAT: Windows.Win32.Foundation.HRESULT = -1072875835
MF_E_NO_SAMPLE_TIMESTAMP: Windows.Win32.Foundation.HRESULT = -1072875832
MF_E_NO_SAMPLE_DURATION: Windows.Win32.Foundation.HRESULT = -1072875831
MF_E_INVALID_STREAM_DATA: Windows.Win32.Foundation.HRESULT = -1072875829
MF_E_RT_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -1072875825
MF_E_UNSUPPORTED_RATE: Windows.Win32.Foundation.HRESULT = -1072875824
MF_E_THINNING_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072875823
MF_E_REVERSE_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072875822
MF_E_UNSUPPORTED_RATE_TRANSITION: Windows.Win32.Foundation.HRESULT = -1072875821
MF_E_RATE_CHANGE_PREEMPTED: Windows.Win32.Foundation.HRESULT = -1072875820
MF_E_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072875819
MF_E_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -1072875818
MF_E_NO_CLOCK: Windows.Win32.Foundation.HRESULT = -1072875817
MF_S_MULTIPLE_BEGIN: Windows.Win32.Foundation.HRESULT = 866008
MF_E_MULTIPLE_BEGIN: Windows.Win32.Foundation.HRESULT = -1072875815
MF_E_MULTIPLE_SUBSCRIBERS: Windows.Win32.Foundation.HRESULT = -1072875814
MF_E_TIMER_ORPHANED: Windows.Win32.Foundation.HRESULT = -1072875813
MF_E_STATE_TRANSITION_PENDING: Windows.Win32.Foundation.HRESULT = -1072875812
MF_E_UNSUPPORTED_STATE_TRANSITION: Windows.Win32.Foundation.HRESULT = -1072875811
MF_E_UNRECOVERABLE_ERROR_OCCURRED: Windows.Win32.Foundation.HRESULT = -1072875810
MF_E_SAMPLE_HAS_TOO_MANY_BUFFERS: Windows.Win32.Foundation.HRESULT = -1072875809
MF_E_SAMPLE_NOT_WRITABLE: Windows.Win32.Foundation.HRESULT = -1072875808
MF_E_INVALID_KEY: Windows.Win32.Foundation.HRESULT = -1072875806
MF_E_BAD_STARTUP_VERSION: Windows.Win32.Foundation.HRESULT = -1072875805
MF_E_UNSUPPORTED_CAPTION: Windows.Win32.Foundation.HRESULT = -1072875804
MF_E_INVALID_POSITION: Windows.Win32.Foundation.HRESULT = -1072875803
MF_E_ATTRIBUTENOTFOUND: Windows.Win32.Foundation.HRESULT = -1072875802
MF_E_PROPERTY_TYPE_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1072875801
MF_E_PROPERTY_TYPE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072875800
MF_E_PROPERTY_EMPTY: Windows.Win32.Foundation.HRESULT = -1072875799
MF_E_PROPERTY_NOT_EMPTY: Windows.Win32.Foundation.HRESULT = -1072875798
MF_E_PROPERTY_VECTOR_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1072875797
MF_E_PROPERTY_VECTOR_REQUIRED: Windows.Win32.Foundation.HRESULT = -1072875796
MF_E_OPERATION_CANCELLED: Windows.Win32.Foundation.HRESULT = -1072875795
MF_E_BYTESTREAM_NOT_SEEKABLE: Windows.Win32.Foundation.HRESULT = -1072875794
MF_E_DISABLED_IN_SAFEMODE: Windows.Win32.Foundation.HRESULT = -1072875793
MF_E_CANNOT_PARSE_BYTESTREAM: Windows.Win32.Foundation.HRESULT = -1072875792
MF_E_SOURCERESOLVER_MUTUALLY_EXCLUSIVE_FLAGS: Windows.Win32.Foundation.HRESULT = -1072875791
MF_E_MEDIAPROC_WRONGSTATE: Windows.Win32.Foundation.HRESULT = -1072875790
MF_E_RT_THROUGHPUT_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -1072875789
MF_E_RT_TOO_MANY_CLASSES: Windows.Win32.Foundation.HRESULT = -1072875788
MF_E_RT_WOULDBLOCK: Windows.Win32.Foundation.HRESULT = -1072875787
MF_E_NO_BITPUMP: Windows.Win32.Foundation.HRESULT = -1072875786
MF_E_RT_OUTOFMEMORY: Windows.Win32.Foundation.HRESULT = -1072875785
MF_E_RT_WORKQUEUE_CLASS_NOT_SPECIFIED: Windows.Win32.Foundation.HRESULT = -1072875784
MF_E_INSUFFICIENT_BUFFER: Windows.Win32.Foundation.HRESULT = -1072860816
MF_E_CANNOT_CREATE_SINK: Windows.Win32.Foundation.HRESULT = -1072875782
MF_E_BYTESTREAM_UNKNOWN_LENGTH: Windows.Win32.Foundation.HRESULT = -1072875781
MF_E_SESSION_PAUSEWHILESTOPPED: Windows.Win32.Foundation.HRESULT = -1072875780
MF_S_ACTIVATE_REPLACED: Windows.Win32.Foundation.HRESULT = 866045
MF_E_FORMAT_CHANGE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072875778
MF_E_INVALID_WORKQUEUE: Windows.Win32.Foundation.HRESULT = -1072875777
MF_E_DRM_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072875776
MF_E_UNAUTHORIZED: Windows.Win32.Foundation.HRESULT = -1072875775
MF_E_OUT_OF_RANGE: Windows.Win32.Foundation.HRESULT = -1072875774
MF_E_INVALID_CODEC_MERIT: Windows.Win32.Foundation.HRESULT = -1072875773
MF_E_HW_MFT_FAILED_START_STREAMING: Windows.Win32.Foundation.HRESULT = -1072875772
MF_E_OPERATION_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1072875771
MF_E_HARDWARE_DRM_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072875770
MF_E_DURATION_TOO_LONG: Windows.Win32.Foundation.HRESULT = -1072875769
MF_E_OPERATION_UNSUPPORTED_AT_D3D_FEATURE_LEVEL: Windows.Win32.Foundation.HRESULT = -1072875768
MF_E_UNSUPPORTED_MEDIATYPE_AT_D3D_FEATURE_LEVEL: Windows.Win32.Foundation.HRESULT = -1072875767
MF_S_ASF_PARSEINPROGRESS: Windows.Win32.Foundation.HRESULT = 1074608792
MF_E_ASF_PARSINGINCOMPLETE: Windows.Win32.Foundation.HRESULT = -1072874856
MF_E_ASF_MISSINGDATA: Windows.Win32.Foundation.HRESULT = -1072874855
MF_E_ASF_INVALIDDATA: Windows.Win32.Foundation.HRESULT = -1072874854
MF_E_ASF_OPAQUEPACKET: Windows.Win32.Foundation.HRESULT = -1072874853
MF_E_ASF_NOINDEX: Windows.Win32.Foundation.HRESULT = -1072874852
MF_E_ASF_OUTOFRANGE: Windows.Win32.Foundation.HRESULT = -1072874851
MF_E_ASF_INDEXNOTLOADED: Windows.Win32.Foundation.HRESULT = -1072874850
MF_E_ASF_TOO_MANY_PAYLOADS: Windows.Win32.Foundation.HRESULT = -1072874849
MF_E_ASF_UNSUPPORTED_STREAM_TYPE: Windows.Win32.Foundation.HRESULT = -1072874848
MF_E_ASF_DROPPED_PACKET: Windows.Win32.Foundation.HRESULT = -1072874847
MF_E_NO_EVENTS_AVAILABLE: Windows.Win32.Foundation.HRESULT = -1072873856
MF_E_INVALID_STATE_TRANSITION: Windows.Win32.Foundation.HRESULT = -1072873854
MF_E_END_OF_STREAM: Windows.Win32.Foundation.HRESULT = -1072873852
MF_E_SHUTDOWN: Windows.Win32.Foundation.HRESULT = -1072873851
MF_E_MP3_NOTFOUND: Windows.Win32.Foundation.HRESULT = -1072873850
MF_E_MP3_OUTOFDATA: Windows.Win32.Foundation.HRESULT = -1072873849
MF_E_MP3_NOTMP3: Windows.Win32.Foundation.HRESULT = -1072873848
MF_E_MP3_NOTSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072873847
MF_E_NO_DURATION: Windows.Win32.Foundation.HRESULT = -1072873846
MF_E_INVALID_FORMAT: Windows.Win32.Foundation.HRESULT = -1072873844
MF_E_PROPERTY_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072873843
MF_E_PROPERTY_READ_ONLY: Windows.Win32.Foundation.HRESULT = -1072873842
MF_E_PROPERTY_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1072873841
MF_E_MEDIA_SOURCE_NOT_STARTED: Windows.Win32.Foundation.HRESULT = -1072873839
MF_E_UNSUPPORTED_FORMAT: Windows.Win32.Foundation.HRESULT = -1072873832
MF_E_MP3_BAD_CRC: Windows.Win32.Foundation.HRESULT = -1072873831
MF_E_NOT_PROTECTED: Windows.Win32.Foundation.HRESULT = -1072873830
MF_E_MEDIA_SOURCE_WRONGSTATE: Windows.Win32.Foundation.HRESULT = -1072873829
MF_E_MEDIA_SOURCE_NO_STREAMS_SELECTED: Windows.Win32.Foundation.HRESULT = -1072873828
MF_E_CANNOT_FIND_KEYFRAME_SAMPLE: Windows.Win32.Foundation.HRESULT = -1072873827
MF_E_UNSUPPORTED_CHARACTERISTICS: Windows.Win32.Foundation.HRESULT = -1072873826
MF_E_NO_AUDIO_RECORDING_DEVICE: Windows.Win32.Foundation.HRESULT = -1072873825
MF_E_AUDIO_RECORDING_DEVICE_IN_USE: Windows.Win32.Foundation.HRESULT = -1072873824
MF_E_AUDIO_RECORDING_DEVICE_INVALIDATED: Windows.Win32.Foundation.HRESULT = -1072873823
MF_E_VIDEO_RECORDING_DEVICE_INVALIDATED: Windows.Win32.Foundation.HRESULT = -1072873822
MF_E_VIDEO_RECORDING_DEVICE_PREEMPTED: Windows.Win32.Foundation.HRESULT = -1072873821
MF_E_NETWORK_RESOURCE_FAILURE: Windows.Win32.Foundation.HRESULT = -1072872856
MF_E_NET_WRITE: Windows.Win32.Foundation.HRESULT = -1072872855
MF_E_NET_READ: Windows.Win32.Foundation.HRESULT = -1072872854
MF_E_NET_REQUIRE_NETWORK: Windows.Win32.Foundation.HRESULT = -1072872853
MF_E_NET_REQUIRE_ASYNC: Windows.Win32.Foundation.HRESULT = -1072872852
MF_E_NET_BWLEVEL_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072872851
MF_E_NET_STREAMGROUPS_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072872850
MF_E_NET_MANUALSS_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072872849
MF_E_NET_INVALID_PRESENTATION_DESCRIPTOR: Windows.Win32.Foundation.HRESULT = -1072872848
MF_E_NET_CACHESTREAM_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072872847
MF_I_MANUAL_PROXY: Windows.Win32.Foundation.HRESULT = 1074610802
MF_E_NET_REQUIRE_INPUT: Windows.Win32.Foundation.HRESULT = -1072872844
MF_E_NET_REDIRECT: Windows.Win32.Foundation.HRESULT = -1072872843
MF_E_NET_REDIRECT_TO_PROXY: Windows.Win32.Foundation.HRESULT = -1072872842
MF_E_NET_TOO_MANY_REDIRECTS: Windows.Win32.Foundation.HRESULT = -1072872841
MF_E_NET_TIMEOUT: Windows.Win32.Foundation.HRESULT = -1072872840
MF_E_NET_CLIENT_CLOSE: Windows.Win32.Foundation.HRESULT = -1072872839
MF_E_NET_BAD_CONTROL_DATA: Windows.Win32.Foundation.HRESULT = -1072872838
MF_E_NET_INCOMPATIBLE_SERVER: Windows.Win32.Foundation.HRESULT = -1072872837
MF_E_NET_UNSAFE_URL: Windows.Win32.Foundation.HRESULT = -1072872836
MF_E_NET_CACHE_NO_DATA: Windows.Win32.Foundation.HRESULT = -1072872835
MF_E_NET_EOL: Windows.Win32.Foundation.HRESULT = -1072872834
MF_E_NET_BAD_REQUEST: Windows.Win32.Foundation.HRESULT = -1072872833
MF_E_NET_INTERNAL_SERVER_ERROR: Windows.Win32.Foundation.HRESULT = -1072872832
MF_E_NET_SESSION_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072872831
MF_E_NET_NOCONNECTION: Windows.Win32.Foundation.HRESULT = -1072872830
MF_E_NET_CONNECTION_FAILURE: Windows.Win32.Foundation.HRESULT = -1072872829
MF_E_NET_INCOMPATIBLE_PUSHSERVER: Windows.Win32.Foundation.HRESULT = -1072872828
MF_E_NET_SERVER_ACCESSDENIED: Windows.Win32.Foundation.HRESULT = -1072872827
MF_E_NET_PROXY_ACCESSDENIED: Windows.Win32.Foundation.HRESULT = -1072872826
MF_E_NET_CANNOTCONNECT: Windows.Win32.Foundation.HRESULT = -1072872825
MF_E_NET_INVALID_PUSH_TEMPLATE: Windows.Win32.Foundation.HRESULT = -1072872824
MF_E_NET_INVALID_PUSH_PUBLISHING_POINT: Windows.Win32.Foundation.HRESULT = -1072872823
MF_E_NET_BUSY: Windows.Win32.Foundation.HRESULT = -1072872822
MF_E_NET_RESOURCE_GONE: Windows.Win32.Foundation.HRESULT = -1072872821
MF_E_NET_ERROR_FROM_PROXY: Windows.Win32.Foundation.HRESULT = -1072872820
MF_E_NET_PROXY_TIMEOUT: Windows.Win32.Foundation.HRESULT = -1072872819
MF_E_NET_SERVER_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -1072872818
MF_E_NET_TOO_MUCH_DATA: Windows.Win32.Foundation.HRESULT = -1072872817
MF_E_NET_SESSION_INVALID: Windows.Win32.Foundation.HRESULT = -1072872816
MF_E_OFFLINE_MODE: Windows.Win32.Foundation.HRESULT = -1072872815
MF_E_NET_UDP_BLOCKED: Windows.Win32.Foundation.HRESULT = -1072872814
MF_E_NET_UNSUPPORTED_CONFIGURATION: Windows.Win32.Foundation.HRESULT = -1072872813
MF_E_NET_PROTOCOL_DISABLED: Windows.Win32.Foundation.HRESULT = -1072872812
MF_E_NET_COMPANION_DRIVER_DISCONNECT: Windows.Win32.Foundation.HRESULT = -1072872811
MF_E_ALREADY_INITIALIZED: Windows.Win32.Foundation.HRESULT = -1072871856
MF_E_BANDWIDTH_OVERRUN: Windows.Win32.Foundation.HRESULT = -1072871855
MF_E_LATE_SAMPLE: Windows.Win32.Foundation.HRESULT = -1072871854
MF_E_FLUSH_NEEDED: Windows.Win32.Foundation.HRESULT = -1072871853
MF_E_INVALID_PROFILE: Windows.Win32.Foundation.HRESULT = -1072871852
MF_E_INDEX_NOT_COMMITTED: Windows.Win32.Foundation.HRESULT = -1072871851
MF_E_NO_INDEX: Windows.Win32.Foundation.HRESULT = -1072871850
MF_E_CANNOT_INDEX_IN_PLACE: Windows.Win32.Foundation.HRESULT = -1072871849
MF_E_MISSING_ASF_LEAKYBUCKET: Windows.Win32.Foundation.HRESULT = -1072871848
MF_E_INVALID_ASF_STREAMID: Windows.Win32.Foundation.HRESULT = -1072871847
MF_E_STREAMSINK_REMOVED: Windows.Win32.Foundation.HRESULT = -1072870856
MF_E_STREAMSINKS_OUT_OF_SYNC: Windows.Win32.Foundation.HRESULT = -1072870854
MF_E_STREAMSINKS_FIXED: Windows.Win32.Foundation.HRESULT = -1072870853
MF_E_STREAMSINK_EXISTS: Windows.Win32.Foundation.HRESULT = -1072870852
MF_E_SAMPLEALLOCATOR_CANCELED: Windows.Win32.Foundation.HRESULT = -1072870851
MF_E_SAMPLEALLOCATOR_EMPTY: Windows.Win32.Foundation.HRESULT = -1072870850
MF_E_SINK_ALREADYSTOPPED: Windows.Win32.Foundation.HRESULT = -1072870849
MF_E_ASF_FILESINK_BITRATE_UNKNOWN: Windows.Win32.Foundation.HRESULT = -1072870848
MF_E_SINK_NO_STREAMS: Windows.Win32.Foundation.HRESULT = -1072870847
MF_S_SINK_NOT_FINALIZED: Windows.Win32.Foundation.HRESULT = 870978
MF_E_METADATA_TOO_LONG: Windows.Win32.Foundation.HRESULT = -1072870845
MF_E_SINK_NO_SAMPLES_PROCESSED: Windows.Win32.Foundation.HRESULT = -1072870844
MF_E_SINK_HEADERS_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072870843
MF_E_VIDEO_REN_NO_PROCAMP_HW: Windows.Win32.Foundation.HRESULT = -1072869856
MF_E_VIDEO_REN_NO_DEINTERLACE_HW: Windows.Win32.Foundation.HRESULT = -1072869855
MF_E_VIDEO_REN_COPYPROT_FAILED: Windows.Win32.Foundation.HRESULT = -1072869854
MF_E_VIDEO_REN_SURFACE_NOT_SHARED: Windows.Win32.Foundation.HRESULT = -1072869853
MF_E_VIDEO_DEVICE_LOCKED: Windows.Win32.Foundation.HRESULT = -1072869852
MF_E_NEW_VIDEO_DEVICE: Windows.Win32.Foundation.HRESULT = -1072869851
MF_E_NO_VIDEO_SAMPLE_AVAILABLE: Windows.Win32.Foundation.HRESULT = -1072869850
MF_E_NO_AUDIO_PLAYBACK_DEVICE: Windows.Win32.Foundation.HRESULT = -1072869756
MF_E_AUDIO_PLAYBACK_DEVICE_IN_USE: Windows.Win32.Foundation.HRESULT = -1072869755
MF_E_AUDIO_PLAYBACK_DEVICE_INVALIDATED: Windows.Win32.Foundation.HRESULT = -1072869754
MF_E_AUDIO_SERVICE_NOT_RUNNING: Windows.Win32.Foundation.HRESULT = -1072869753
MF_E_AUDIO_BUFFER_SIZE_ERROR: Windows.Win32.Foundation.HRESULT = -1072869752
MF_E_AUDIO_CLIENT_WRAPPER_SPOOF_ERROR: Windows.Win32.Foundation.HRESULT = -1072869751
MF_E_TOPO_INVALID_OPTIONAL_NODE: Windows.Win32.Foundation.HRESULT = -1072868850
MF_E_TOPO_CANNOT_FIND_DECRYPTOR: Windows.Win32.Foundation.HRESULT = -1072868847
MF_E_TOPO_CODEC_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072868846
MF_E_TOPO_CANNOT_CONNECT: Windows.Win32.Foundation.HRESULT = -1072868845
MF_E_TOPO_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072868844
MF_E_TOPO_INVALID_TIME_ATTRIBUTES: Windows.Win32.Foundation.HRESULT = -1072868843
MF_E_TOPO_LOOPS_IN_TOPOLOGY: Windows.Win32.Foundation.HRESULT = -1072868842
MF_E_TOPO_MISSING_PRESENTATION_DESCRIPTOR: Windows.Win32.Foundation.HRESULT = -1072868841
MF_E_TOPO_MISSING_STREAM_DESCRIPTOR: Windows.Win32.Foundation.HRESULT = -1072868840
MF_E_TOPO_STREAM_DESCRIPTOR_NOT_SELECTED: Windows.Win32.Foundation.HRESULT = -1072868839
MF_E_TOPO_MISSING_SOURCE: Windows.Win32.Foundation.HRESULT = -1072868838
MF_E_TOPO_SINK_ACTIVATES_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072868837
MF_E_SEQUENCER_UNKNOWN_SEGMENT_ID: Windows.Win32.Foundation.HRESULT = -1072864852
MF_S_SEQUENCER_CONTEXT_CANCELED: Windows.Win32.Foundation.HRESULT = 876973
MF_E_NO_SOURCE_IN_CACHE: Windows.Win32.Foundation.HRESULT = -1072864850
MF_S_SEQUENCER_SEGMENT_AT_END_OF_STREAM: Windows.Win32.Foundation.HRESULT = 876975
MF_E_TRANSFORM_TYPE_NOT_SET: Windows.Win32.Foundation.HRESULT = -1072861856
MF_E_TRANSFORM_STREAM_CHANGE: Windows.Win32.Foundation.HRESULT = -1072861855
MF_E_TRANSFORM_INPUT_REMAINING: Windows.Win32.Foundation.HRESULT = -1072861854
MF_E_TRANSFORM_PROFILE_MISSING: Windows.Win32.Foundation.HRESULT = -1072861853
MF_E_TRANSFORM_PROFILE_INVALID_OR_CORRUPT: Windows.Win32.Foundation.HRESULT = -1072861852
MF_E_TRANSFORM_PROFILE_TRUNCATED: Windows.Win32.Foundation.HRESULT = -1072861851
MF_E_TRANSFORM_PROPERTY_PID_NOT_RECOGNIZED: Windows.Win32.Foundation.HRESULT = -1072861850
MF_E_TRANSFORM_PROPERTY_VARIANT_TYPE_WRONG: Windows.Win32.Foundation.HRESULT = -1072861849
MF_E_TRANSFORM_PROPERTY_NOT_WRITEABLE: Windows.Win32.Foundation.HRESULT = -1072861848
MF_E_TRANSFORM_PROPERTY_ARRAY_VALUE_WRONG_NUM_DIM: Windows.Win32.Foundation.HRESULT = -1072861847
MF_E_TRANSFORM_PROPERTY_VALUE_SIZE_WRONG: Windows.Win32.Foundation.HRESULT = -1072861846
MF_E_TRANSFORM_PROPERTY_VALUE_OUT_OF_RANGE: Windows.Win32.Foundation.HRESULT = -1072861845
MF_E_TRANSFORM_PROPERTY_VALUE_INCOMPATIBLE: Windows.Win32.Foundation.HRESULT = -1072861844
MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_OUTPUT_MEDIATYPE: Windows.Win32.Foundation.HRESULT = -1072861843
MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_INPUT_MEDIATYPE: Windows.Win32.Foundation.HRESULT = -1072861842
MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_MEDIATYPE_COMBINATION: Windows.Win32.Foundation.HRESULT = -1072861841
MF_E_TRANSFORM_CONFLICTS_WITH_OTHER_CURRENTLY_ENABLED_FEATURES: Windows.Win32.Foundation.HRESULT = -1072861840
MF_E_TRANSFORM_NEED_MORE_INPUT: Windows.Win32.Foundation.HRESULT = -1072861838
MF_E_TRANSFORM_NOT_POSSIBLE_FOR_CURRENT_SPKR_CONFIG: Windows.Win32.Foundation.HRESULT = -1072861837
MF_E_TRANSFORM_CANNOT_CHANGE_MEDIATYPE_WHILE_PROCESSING: Windows.Win32.Foundation.HRESULT = -1072861836
MF_S_TRANSFORM_DO_NOT_PROPAGATE_EVENT: Windows.Win32.Foundation.HRESULT = 879989
MF_E_UNSUPPORTED_D3D_TYPE: Windows.Win32.Foundation.HRESULT = -1072861834
MF_E_TRANSFORM_ASYNC_LOCKED: Windows.Win32.Foundation.HRESULT = -1072861833
MF_E_TRANSFORM_CANNOT_INITIALIZE_ACM_DRIVER: Windows.Win32.Foundation.HRESULT = -1072861832
MF_E_TRANSFORM_STREAM_INVALID_RESOLUTION: Windows.Win32.Foundation.HRESULT = -1072861831
MF_E_TRANSFORM_ASYNC_MFT_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072861830
MF_E_TRANSFORM_EXATTRIBUTE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072861828
MF_E_LICENSE_INCORRECT_RIGHTS: Windows.Win32.Foundation.HRESULT = -1072860856
MF_E_LICENSE_OUTOFDATE: Windows.Win32.Foundation.HRESULT = -1072860855
MF_E_LICENSE_REQUIRED: Windows.Win32.Foundation.HRESULT = -1072860854
MF_E_DRM_HARDWARE_INCONSISTENT: Windows.Win32.Foundation.HRESULT = -1072860853
MF_E_NO_CONTENT_PROTECTION_MANAGER: Windows.Win32.Foundation.HRESULT = -1072860852
MF_E_LICENSE_RESTORE_NO_RIGHTS: Windows.Win32.Foundation.HRESULT = -1072860851
MF_E_BACKUP_RESTRICTED_LICENSE: Windows.Win32.Foundation.HRESULT = -1072860850
MF_E_LICENSE_RESTORE_NEEDS_INDIVIDUALIZATION: Windows.Win32.Foundation.HRESULT = -1072860849
MF_S_PROTECTION_NOT_REQUIRED: Windows.Win32.Foundation.HRESULT = 880976
MF_E_COMPONENT_REVOKED: Windows.Win32.Foundation.HRESULT = -1072860847
MF_E_TRUST_DISABLED: Windows.Win32.Foundation.HRESULT = -1072860846
MF_E_WMDRMOTA_NO_ACTION: Windows.Win32.Foundation.HRESULT = -1072860845
MF_E_WMDRMOTA_ACTION_ALREADY_SET: Windows.Win32.Foundation.HRESULT = -1072860844
MF_E_WMDRMOTA_DRM_HEADER_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -1072860843
MF_E_WMDRMOTA_DRM_ENCRYPTION_SCHEME_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072860842
MF_E_WMDRMOTA_ACTION_MISMATCH: Windows.Win32.Foundation.HRESULT = -1072860841
MF_E_WMDRMOTA_INVALID_POLICY: Windows.Win32.Foundation.HRESULT = -1072860840
MF_E_POLICY_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -1072860839
MF_E_OPL_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072860838
MF_E_TOPOLOGY_VERIFICATION_FAILED: Windows.Win32.Foundation.HRESULT = -1072860837
MF_E_SIGNATURE_VERIFICATION_FAILED: Windows.Win32.Foundation.HRESULT = -1072860836
MF_E_DEBUGGING_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1072860835
MF_E_CODE_EXPIRED: Windows.Win32.Foundation.HRESULT = -1072860834
MF_E_GRL_VERSION_TOO_LOW: Windows.Win32.Foundation.HRESULT = -1072860833
MF_E_GRL_RENEWAL_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072860832
MF_E_GRL_EXTENSIBLE_ENTRY_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1072860831
MF_E_KERNEL_UNTRUSTED: Windows.Win32.Foundation.HRESULT = -1072860830
MF_E_PEAUTH_UNTRUSTED: Windows.Win32.Foundation.HRESULT = -1072860829
MF_E_NON_PE_PROCESS: Windows.Win32.Foundation.HRESULT = -1072860827
MF_E_REBOOT_REQUIRED: Windows.Win32.Foundation.HRESULT = -1072860825
MF_S_WAIT_FOR_POLICY_SET: Windows.Win32.Foundation.HRESULT = 881000
MF_S_VIDEO_DISABLED_WITH_UNKNOWN_SOFTWARE_OUTPUT: Windows.Win32.Foundation.HRESULT = 881001
MF_E_GRL_INVALID_FORMAT: Windows.Win32.Foundation.HRESULT = -1072860822
MF_E_GRL_UNRECOGNIZED_FORMAT: Windows.Win32.Foundation.HRESULT = -1072860821
MF_E_ALL_PROCESS_RESTART_REQUIRED: Windows.Win32.Foundation.HRESULT = -1072860820
MF_E_PROCESS_RESTART_REQUIRED: Windows.Win32.Foundation.HRESULT = -1072860819
MF_E_USERMODE_UNTRUSTED: Windows.Win32.Foundation.HRESULT = -1072860818
MF_E_PEAUTH_SESSION_NOT_STARTED: Windows.Win32.Foundation.HRESULT = -1072860817
MF_E_PEAUTH_PUBLICKEY_REVOKED: Windows.Win32.Foundation.HRESULT = -1072860815
MF_E_GRL_ABSENT: Windows.Win32.Foundation.HRESULT = -1072860814
MF_S_PE_TRUSTED: Windows.Win32.Foundation.HRESULT = 881011
MF_E_PE_UNTRUSTED: Windows.Win32.Foundation.HRESULT = -1072860812
MF_E_PEAUTH_NOT_STARTED: Windows.Win32.Foundation.HRESULT = -1072860811
MF_E_INCOMPATIBLE_SAMPLE_PROTECTION: Windows.Win32.Foundation.HRESULT = -1072860810
MF_E_PE_SESSIONS_MAXED: Windows.Win32.Foundation.HRESULT = -1072860809
MF_E_HIGH_SECURITY_LEVEL_CONTENT_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1072860808
MF_E_TEST_SIGNED_COMPONENTS_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1072860807
MF_E_ITA_UNSUPPORTED_ACTION: Windows.Win32.Foundation.HRESULT = -1072860806
MF_E_ITA_ERROR_PARSING_SAP_PARAMETERS: Windows.Win32.Foundation.HRESULT = -1072860805
MF_E_POLICY_MGR_ACTION_OUTOFBOUNDS: Windows.Win32.Foundation.HRESULT = -1072860804
MF_E_BAD_OPL_STRUCTURE_FORMAT: Windows.Win32.Foundation.HRESULT = -1072860803
MF_E_ITA_UNRECOGNIZED_ANALOG_VIDEO_PROTECTION_GUID: Windows.Win32.Foundation.HRESULT = -1072860802
MF_E_NO_PMP_HOST: Windows.Win32.Foundation.HRESULT = -1072860801
MF_E_ITA_OPL_DATA_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -1072860800
MF_E_ITA_UNRECOGNIZED_ANALOG_VIDEO_OUTPUT: Windows.Win32.Foundation.HRESULT = -1072860799
MF_E_ITA_UNRECOGNIZED_DIGITAL_VIDEO_OUTPUT: Windows.Win32.Foundation.HRESULT = -1072860798
MF_E_RESOLUTION_REQUIRES_PMP_CREATION_CALLBACK: Windows.Win32.Foundation.HRESULT = -1072860797
MF_E_INVALID_AKE_CHANNEL_PARAMETERS: Windows.Win32.Foundation.HRESULT = -1072860796
MF_E_CONTENT_PROTECTION_SYSTEM_NOT_ENABLED: Windows.Win32.Foundation.HRESULT = -1072860795
MF_E_UNSUPPORTED_CONTENT_PROTECTION_SYSTEM: Windows.Win32.Foundation.HRESULT = -1072860794
MF_E_DRM_MIGRATION_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072860793
MF_E_HDCP_AUTHENTICATION_FAILURE: Windows.Win32.Foundation.HRESULT = -1072860792
MF_E_HDCP_LINK_FAILURE: Windows.Win32.Foundation.HRESULT = -1072860791
MF_E_CLOCK_INVALID_CONTINUITY_KEY: Windows.Win32.Foundation.HRESULT = -1072849856
MF_E_CLOCK_NO_TIME_SOURCE: Windows.Win32.Foundation.HRESULT = -1072849855
MF_E_CLOCK_STATE_ALREADY_SET: Windows.Win32.Foundation.HRESULT = -1072849854
MF_E_CLOCK_NOT_SIMPLE: Windows.Win32.Foundation.HRESULT = -1072849853
MF_S_CLOCK_STOPPED: Windows.Win32.Foundation.HRESULT = 891972
MF_E_CLOCK_AUDIO_DEVICE_POSITION_UNEXPECTED: Windows.Win32.Foundation.HRESULT = 891973
MF_E_CLOCK_AUDIO_RENDER_POSITION_UNEXPECTED: Windows.Win32.Foundation.HRESULT = 891974
MF_E_CLOCK_AUDIO_RENDER_TIME_UNEXPECTED: Windows.Win32.Foundation.HRESULT = 891975
MF_E_NO_MORE_DROP_MODES: Windows.Win32.Foundation.HRESULT = -1072848856
MF_E_NO_MORE_QUALITY_LEVELS: Windows.Win32.Foundation.HRESULT = -1072848855
MF_E_DROPTIME_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072848854
MF_E_QUALITYKNOB_WAIT_LONGER: Windows.Win32.Foundation.HRESULT = -1072848853
MF_E_QM_INVALIDSTATE: Windows.Win32.Foundation.HRESULT = -1072848852
MF_E_TRANSCODE_NO_CONTAINERTYPE: Windows.Win32.Foundation.HRESULT = -1072847856
MF_E_TRANSCODE_PROFILE_NO_MATCHING_STREAMS: Windows.Win32.Foundation.HRESULT = -1072847855
MF_E_TRANSCODE_NO_MATCHING_ENCODER: Windows.Win32.Foundation.HRESULT = -1072847854
MF_E_TRANSCODE_INVALID_PROFILE: Windows.Win32.Foundation.HRESULT = -1072847853
MF_E_ALLOCATOR_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -1072846856
MF_E_ALLOCATOR_NOT_COMMITED: Windows.Win32.Foundation.HRESULT = -1072846855
MF_E_ALLOCATOR_ALREADY_COMMITED: Windows.Win32.Foundation.HRESULT = -1072846854
MF_E_STREAM_ERROR: Windows.Win32.Foundation.HRESULT = -1072846853
MF_E_INVALID_STREAM_STATE: Windows.Win32.Foundation.HRESULT = -1072846852
MF_E_HW_STREAM_NOT_CONNECTED: Windows.Win32.Foundation.HRESULT = -1072846851
MF_E_NO_CAPTURE_DEVICES_AVAILABLE: Windows.Win32.Foundation.HRESULT = -1072845856
MF_E_CAPTURE_SINK_OUTPUT_NOT_SET: Windows.Win32.Foundation.HRESULT = -1072845855
MF_E_CAPTURE_SINK_MIRROR_ERROR: Windows.Win32.Foundation.HRESULT = -1072845854
MF_E_CAPTURE_SINK_ROTATE_ERROR: Windows.Win32.Foundation.HRESULT = -1072845853
MF_E_CAPTURE_ENGINE_INVALID_OP: Windows.Win32.Foundation.HRESULT = -1072845852
MF_E_CAPTURE_ENGINE_ALL_EFFECTS_REMOVED: Windows.Win32.Foundation.HRESULT = -1072845851
MF_E_CAPTURE_SOURCE_NO_INDEPENDENT_PHOTO_STREAM_PRESENT: Windows.Win32.Foundation.HRESULT = -1072845850
MF_E_CAPTURE_SOURCE_NO_VIDEO_STREAM_PRESENT: Windows.Win32.Foundation.HRESULT = -1072845849
MF_E_CAPTURE_SOURCE_NO_AUDIO_STREAM_PRESENT: Windows.Win32.Foundation.HRESULT = -1072845848
MF_E_CAPTURE_SOURCE_DEVICE_EXTENDEDPROP_OP_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1072845847
MF_E_CAPTURE_PROPERTY_SET_DURING_PHOTO: Windows.Win32.Foundation.HRESULT = -1072845846
MF_E_CAPTURE_NO_SAMPLES_IN_QUEUE: Windows.Win32.Foundation.HRESULT = -1072845845
MF_E_HW_ACCELERATED_THUMBNAIL_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1072845844
MF_E_UNSUPPORTED_CAPTURE_DEVICE_PRESENT: Windows.Win32.Foundation.HRESULT = -1072845843
MF_E_TIMELINECONTROLLER_UNSUPPORTED_SOURCE_TYPE: Windows.Win32.Foundation.HRESULT = -1072844856
MF_E_TIMELINECONTROLLER_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1072844855
MF_E_TIMELINECONTROLLER_CANNOT_ATTACH: Windows.Win32.Foundation.HRESULT = -1072844854
MF_E_MEDIA_EXTENSION_APPSERVICE_CONNECTION_FAILED: Windows.Win32.Foundation.HRESULT = -1072843856
MF_E_MEDIA_EXTENSION_APPSERVICE_REQUEST_FAILED: Windows.Win32.Foundation.HRESULT = -1072843855
MF_E_MEDIA_EXTENSION_PACKAGE_INTEGRITY_CHECK_FAILED: Windows.Win32.Foundation.HRESULT = -1072843854
MF_E_MEDIA_EXTENSION_PACKAGE_LICENSE_INVALID: Windows.Win32.Foundation.HRESULT = -1072843853
MF_INDEX_SIZE_ERR: UInt32 = 2154823681
MF_NOT_FOUND_ERR: UInt32 = 2154823688
MF_NOT_SUPPORTED_ERR: UInt32 = 2154823689
MF_INVALID_STATE_ERR: UInt32 = 2154823691
MF_SYNTAX_ERR: UInt32 = 2154823692
MF_INVALID_ACCESS_ERR: UInt32 = 2154823695
MF_QUOTA_EXCEEDED_ERR: UInt32 = 2154823702
MF_PARSE_ERR: UInt32 = 2154823761
MF_TYPE_ERR: UInt32 = 2154840069
def DEVPKEY_DeviceInterface_IsVirtualCamera():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{6edc630d-c2e3-43b7-b2d1-20525a1af120}'), pid=3)
def DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{6edc630d-c2e3-43b7-b2d1-20525a1af120}'), pid=4)
def DEVPKEY_DeviceInterface_VirtualCameraAssociatedCameras():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{6edc630d-c2e3-43b7-b2d1-20525a1af120}'), pid=5)
g_wszSpeechFormatCaps: String = 'SpeechFormatCap'
g_wszWMCPCodecName: String = '_CODECNAME'
g_wszWMCPSupportedVBRModes: String = '_SUPPORTEDVBRMODES'
g_wszWMCPAudioVBRSupported: String = '_VBRENABLED'
g_wszWMCPAudioVBRQuality: String = '_VBRQUALITY'
g_wszWMCPMaxPasses: String = '_PASSESRECOMMENDED'
g_wszWMCPDefaultCrisp: String = '_DEFAULTCRISP'
COPP_ProtectionType_Unknown: Int32 = -2147483648
COPP_ProtectionType_None: Int32 = 0
COPP_ProtectionType_HDCP: Int32 = 1
COPP_ProtectionType_ACP: Int32 = 2
COPP_ProtectionType_CGMSA: Int32 = 4
COPP_ProtectionType_Mask: Int32 = -2147483641
COPP_ProtectionType_Reserved: Int32 = 2147483640
MF_BYTESTREAM_ORIGIN_NAME: Guid = Guid('{fc358288-3cb6-460c-a424-b6681260375a}')
MF_BYTESTREAM_CONTENT_TYPE: Guid = Guid('{fc358289-3cb6-460c-a424-b6681260375a}')
MF_BYTESTREAM_DURATION: Guid = Guid('{fc35828a-3cb6-460c-a424-b6681260375a}')
MF_BYTESTREAM_LAST_MODIFIED_TIME: Guid = Guid('{fc35828b-3cb6-460c-a424-b6681260375a}')
MF_BYTESTREAM_IFO_FILE_URI: Guid = Guid('{fc35828c-3cb6-460c-a424-b6681260375a}')
MF_BYTESTREAM_DLNA_PROFILE_ID: Guid = Guid('{fc35828d-3cb6-460c-a424-b6681260375a}')
MF_BYTESTREAM_EFFECTIVE_URL: Guid = Guid('{9afa0209-89d1-42af-8456-1de6b562d691}')
MF_BYTESTREAM_TRANSCODED: Guid = Guid('{b6c5c282-4dc9-4db9-ab48-cf3b6d8bc5e0}')
CLSID_MFByteStreamProxyClassFactory: Guid = Guid('{770e8e77-4916-441c-a9a7-b342d0eebc71}')
MEDeviceStreamCreated: Guid = Guid('{0252a1cf-3540-43b4-9164-d72eb405fa40}')
MF_SA_D3D_AWARE: Guid = Guid('{eaa35c29-775e-488e-9b61-b3283e49583b}')
MF_SA_REQUIRED_SAMPLE_COUNT: Guid = Guid('{18802c61-324b-4952-abd0-176ff5c696ff}')
MFT_END_STREAMING_AWARE: Guid = Guid('{70fbc845-b07e-4089-b064-399dc6110f29}')
MF_SA_AUDIO_ENDPOINT_AWARE: Guid = Guid('{c0381701-805c-42b2-ac8d-e2b4bf21f4f8}')
MFT_AUDIO_DECODER_AUDIO_ENDPOINT_ID: Guid = Guid('{c7ccdd6e-5398-4695-8be7-51b3e95111bd}')
MFT_AUDIO_DECODER_SPATIAL_METADATA_CLIENT: Guid = Guid('{05987df4-1270-4999-925f-8e939a7c0af7}')
MF_DMFT_FRAME_BUFFER_INFO: Guid = Guid('{396ce1c9-67a9-454c-8797-95a45799d804}')
MF_SA_REQUIRED_SAMPLE_COUNT_PROGRESSIVE: Guid = Guid('{b172d58e-fa77-4e48-8d2a-1df2d850eac2}')
MF_SA_MINIMUM_OUTPUT_SAMPLE_COUNT: Guid = Guid('{851745d5-c3d6-476d-9527-498ef2d10d18}')
MF_SA_MINIMUM_OUTPUT_SAMPLE_COUNT_PROGRESSIVE: Guid = Guid('{0f5523a5-1cb2-47c5-a550-2eeb84b4d14a}')
MFT_SUPPORT_3DVIDEO: Guid = Guid('{093f81b1-4f2e-4631-8168-7934032a01d3}')
MF_ENABLE_3DVIDEO_OUTPUT: Guid = Guid('{bdad7bca-0e5f-4b10-ab16-26de381b6293}')
MF_SA_D3D11_BINDFLAGS: Guid = Guid('{eacf97ad-065c-4408-bee3-fdcbfd128be2}')
MF_SA_D3D11_USAGE: Guid = Guid('{e85fe442-2ca3-486e-a9c7-109dda609880}')
MF_SA_D3D11_AWARE: Guid = Guid('{206b4fc8-fcf9-4c51-afe3-9764369e33a0}')
MF_SA_D3D11_SHARED: Guid = Guid('{7b8f32c3-6d96-4b89-9203-dd38b61414f3}')
MF_SA_D3D11_SHARED_WITHOUT_MUTEX: Guid = Guid('{39dbd44d-2e44-4931-a4c8-352d3dc42115}')
MF_SA_D3D11_ALLOW_DYNAMIC_YUV_TEXTURE: Guid = Guid('{ce06d49f-0613-4b9d-86a6-d8c4f9c10075}')
MF_SA_D3D11_HW_PROTECTED: Guid = Guid('{3a8ba9d9-92ca-4307-a391-6999dbf3b6ce}')
MF_SA_BUFFERS_PER_SAMPLE: Guid = Guid('{873c5171-1e3d-4e25-988d-b433ce041983}')
MF_SA_D3D11_ALLOCATE_DISPLAYABLE_RESOURCES: Guid = Guid('{eeface6d-2ea9-4adf-bbdf-7bbc482a1b6d}')
MFT_DECODER_EXPOSE_OUTPUT_TYPES_IN_NATIVE_ORDER: Guid = Guid('{ef80833f-f8fa-44d9-80d8-41ed6232670c}')
MFT_DECODER_QUALITY_MANAGEMENT_CUSTOM_CONTROL: Guid = Guid('{a24e30d7-de25-4558-bbfb-71070a2d332e}')
MFT_DECODER_QUALITY_MANAGEMENT_RECOVERY_WITHOUT_ARTIFACTS: Guid = Guid('{d8980deb-0a48-425f-8623-611db41d3810}')
MFT_REMUX_MARK_I_PICTURE_AS_CLEAN_POINT: Guid = Guid('{364e8f85-3f2e-436c-b2a2-4440a012a9e8}')
MFT_DECODER_FINAL_VIDEO_RESOLUTION_HINT: Guid = Guid('{dc2f8496-15c4-407a-b6f0-1b66ab5fbf53}')
MFT_ENCODER_SUPPORTS_CONFIG_EVENT: Guid = Guid('{86a355ae-3a77-4ec4-9f31-01149a4e92de}')
MFT_ENUM_HARDWARE_VENDOR_ID_Attribute: Guid = Guid('{3aecb0cc-035b-4bcc-8185-2b8d551ef3af}')
MF_TRANSFORM_ASYNC: Guid = Guid('{f81a699a-649a-497d-8c73-29f8fed6ad7a}')
MF_TRANSFORM_ASYNC_UNLOCK: Guid = Guid('{e5666d6b-3422-4eb6-a421-da7db1f8e207}')
MF_TRANSFORM_FLAGS_Attribute: Guid = Guid('{9359bb7e-6275-46c4-a025-1c01e45f1a86}')
MF_TRANSFORM_CATEGORY_Attribute: Guid = Guid('{ceabba49-506d-4757-a6ff-66c184987e4e}')
MFT_TRANSFORM_CLSID_Attribute: Guid = Guid('{6821c42b-65a4-4e82-99bc-9a88205ecd0c}')
MFT_INPUT_TYPES_Attributes: Guid = Guid('{4276c9b1-759d-4bf3-9cd0-0d723d138f96}')
MFT_OUTPUT_TYPES_Attributes: Guid = Guid('{8eae8cf3-a44f-4306-ba5c-bf5dda242818}')
MFT_ENUM_HARDWARE_URL_Attribute: Guid = Guid('{2fb866ac-b078-4942-ab6c-003d05cda674}')
MFT_FRIENDLY_NAME_Attribute: Guid = Guid('{314ffbae-5b41-4c95-9c19-4e7d586face3}')
MFT_CONNECTED_STREAM_ATTRIBUTE: Guid = Guid('{71eeb820-a59f-4de2-bcec-38db1dd611a4}')
MFT_CONNECTED_TO_HW_STREAM: Guid = Guid('{34e6e728-06d6-4491-a553-4795650db912}')
MFT_PREFERRED_OUTPUTTYPE_Attribute: Guid = Guid('{7e700499-396a-49ee-b1b4-f628021e8c9d}')
MFT_PROCESS_LOCAL_Attribute: Guid = Guid('{543186e4-4649-4e65-b588-4aa352aff379}')
MFT_PREFERRED_ENCODER_PROFILE: Guid = Guid('{53004909-1ef5-46d7-a18e-5a75f8b5905f}')
MFT_HW_TIMESTAMP_WITH_QPC_Attribute: Guid = Guid('{8d030fb8-cc43-4258-a22e-9210bef89be4}')
MFT_FIELDOFUSE_UNLOCK_Attribute: Guid = Guid('{8ec2e9fd-9148-410d-831e-702439461a8e}')
MFT_CODEC_MERIT_Attribute: Guid = Guid('{88a7cb15-7b07-4a34-9128-e64c6703c4d3}')
MFT_ENUM_TRANSCODE_ONLY_ATTRIBUTE: Guid = Guid('{111ea8cd-b62a-4bdb-89f6-67ffcdc2458b}')
MFT_AUDIO_DECODER_DEGRADATION_INFO_ATTRIBUTE: Guid = Guid('{6c3386ad-ec20-430d-b2a5-505c7178d9c4}')
MFT_POLICY_SET_AWARE: Guid = Guid('{5a633b19-cc39-4fa8-8ca5-59981b7a0018}')
MFT_USING_HARDWARE_DRM: Guid = Guid('{34faa77d-d79e-4957-b8ce-362b2684996c}')
MF_WVC1_PROG_SINGLE_SLICE_CONTENT: Guid = Guid('{67ec2559-0f2f-4420-a4dd-2f8ee7a5738b}')
MF_PROGRESSIVE_CODING_CONTENT: Guid = Guid('{8f020eea-1508-471f-9da6-507d7cfa40db}')
MF_NALU_LENGTH_SET: Guid = Guid('{a7911d53-12a4-4965-ae70-6eadd6ff0551}')
MF_NALU_LENGTH_INFORMATION: Guid = Guid('{19124e7c-ad4b-465f-bb18-20186287b6af}')
MF_USER_DATA_PAYLOAD: Guid = Guid('{d1d4985d-dc92-457a-b3a0-651a33a31047}')
MF_MPEG4SINK_SPSPPS_PASSTHROUGH: Guid = Guid('{5601a134-2005-4ad2-b37d-22a6c554deb2}')
MF_MPEG4SINK_MOOV_BEFORE_MDAT: Guid = Guid('{f672e3ac-e1e6-4f10-b5ec-5f3b30828816}')
MF_MPEG4SINK_MINIMUM_PROPERTIES_SIZE: Guid = Guid('{dca1ed52-450e-4a22-8c62-4ed452f7a187}')
MF_MPEG4SINK_MIN_FRAGMENT_DURATION: Guid = Guid('{a30b570c-8efd-45e8-94fe-27c84b5bdff6}')
MF_MPEG4SINK_MAX_CODED_SEQUENCES_PER_FRAGMENT: Guid = Guid('{fc1b3bd6-692d-4ce5-9299-738aa5463e9a}')
MF_SESSION_TOPOLOADER: Guid = Guid('{1e83d482-1f1c-4571-8405-88f4b2181f71}')
MF_SESSION_GLOBAL_TIME: Guid = Guid('{1e83d482-1f1c-4571-8405-88f4b2181f72}')
MF_SESSION_QUALITY_MANAGER: Guid = Guid('{1e83d482-1f1c-4571-8405-88f4b2181f73}')
MF_SESSION_CONTENT_PROTECTION_MANAGER: Guid = Guid('{1e83d482-1f1c-4571-8405-88f4b2181f74}')
MF_SESSION_SERVER_CONTEXT: Guid = Guid('{afe5b291-50fa-46e8-b9be-0c0c3ce4b3a5}')
MF_SESSION_REMOTE_SOURCE_MODE: Guid = Guid('{f4033ef4-9bb3-4378-941f-85a0856bc244}')
MF_SESSION_APPROX_EVENT_OCCURRENCE_TIME: Guid = Guid('{190e852f-6238-42d1-b5af-69ea338ef850}')
MF_PMP_SERVER_CONTEXT: Guid = Guid('{2f00c910-d2cf-4278-8b6a-d077fac3a25f}')
MF_TIME_FORMAT_ENTRY_RELATIVE: Guid = Guid('{4399f178-46d3-4504-afda-20d32e9ba360}')
MF_SOURCE_STREAM_SUPPORTS_HW_CONNECTION: Guid = Guid('{a38253aa-6314-42fd-a3ce-bb27b6859946}')
MF_STREAM_SINK_SUPPORTS_HW_CONNECTION: Guid = Guid('{9b465cbf-0597-4f9e-9f3c-b97eeef90359}')
MF_STREAM_SINK_SUPPORTS_ROTATION: Guid = Guid('{b3e96280-bd05-41a5-97ad-8a7fee24b912}')
MF_SINK_VIDEO_PTS: Guid = Guid('{2162bde7-421e-4b90-9b33-e58fbf1d58b6}')
MF_SINK_VIDEO_NATIVE_WIDTH: Guid = Guid('{e6d6a707-1505-4747-9b10-72d2d158cb3a}')
MF_SINK_VIDEO_NATIVE_HEIGHT: Guid = Guid('{f0ca6705-490c-43e8-941c-c0b3206b9a65}')
MF_SINK_VIDEO_DISPLAY_ASPECT_RATIO_NUMERATOR: Guid = Guid('{d0f33b22-b78a-4879-b455-f03ef3fa82cd}')
MF_SINK_VIDEO_DISPLAY_ASPECT_RATIO_DENOMINATOR: Guid = Guid('{6ea1eb97-1fe0-4f10-a6e4-1f4f661564e0}')
MF_BD_MVC_PLANE_OFFSET_METADATA: Guid = Guid('{62a654e4-b76c-4901-9823-2cb615d47318}')
MF_LUMA_KEY_ENABLE: Guid = Guid('{7369820f-76de-43ca-9284-47b8f37e0649}')
MF_LUMA_KEY_LOWER: Guid = Guid('{93d7b8d5-0b81-4715-aea0-8725871621e9}')
MF_LUMA_KEY_UPPER: Guid = Guid('{d09f39bb-4602-4c31-a706-a12171a5110a}')
MF_USER_EXTENDED_ATTRIBUTES: Guid = Guid('{c02abac6-feb2-4541-922f-920b43702722}')
MF_INDEPENDENT_STILL_IMAGE: Guid = Guid('{ea12af41-0710-42c9-a127-daa3e78483a5}')
MF_XVP_SAMPLE_LOCK_TIMEOUT: Guid = Guid('{aa4ddb29-5134-4363-ac72-83ec4bc10426}')
MF_TOPOLOGY_PROJECTSTART: Guid = Guid('{7ed3f802-86bb-4b3f-b7e4-7cb43afd4b80}')
MF_TOPOLOGY_PROJECTSTOP: Guid = Guid('{7ed3f803-86bb-4b3f-b7e4-7cb43afd4b80}')
MF_TOPOLOGY_NO_MARKIN_MARKOUT: Guid = Guid('{7ed3f804-86bb-4b3f-b7e4-7cb43afd4b80}')
MF_TOPOLOGY_DXVA_MODE: Guid = Guid('{1e8d34f6-f5ab-4e23-bb88-874aa3a1a74d}')
MF_TOPOLOGY_ENABLE_XVP_FOR_PLAYBACK: Guid = Guid('{1967731f-cd78-42fc-b026-0992a56e5693}')
MF_TOPOLOGY_STATIC_PLAYBACK_OPTIMIZATIONS: Guid = Guid('{b86cac42-41a6-4b79-897a-1ab0e52b4a1b}')
MF_TOPOLOGY_PLAYBACK_MAX_DIMS: Guid = Guid('{5715cf19-5768-44aa-ad6e-8721f1b0f9bb}')
MF_TOPOLOGY_HARDWARE_MODE: Guid = Guid('{d2d362fd-4e4f-4191-a579-c618b66706af}')
MF_TOPOLOGY_PLAYBACK_FRAMERATE: Guid = Guid('{c164737a-c2b1-4553-83bb-5a526072448f}')
MF_TOPOLOGY_DYNAMIC_CHANGE_NOT_ALLOWED: Guid = Guid('{d529950b-d484-4527-a9cd-b1909532b5b0}')
MF_TOPOLOGY_ENUMERATE_SOURCE_TYPES: Guid = Guid('{6248c36d-5d0b-4f40-a0bb-b0b305f77698}')
MF_TOPOLOGY_START_TIME_ON_PRESENTATION_SWITCH: Guid = Guid('{c8cc113f-7951-4548-aad6-9ed6202e62b3}')
MF_DISABLE_LOCALLY_REGISTERED_PLUGINS: Guid = Guid('{66b16da9-add4-47e0-a16b-5af1fb483634}')
MF_LOCAL_PLUGIN_CONTROL_POLICY: Guid = Guid('{d91b0085-c86d-4f81-8822-8c68e1d7fa04}')
MF_TOPONODE_FLUSH: Guid = Guid('{494bbce8-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_DRAIN: Guid = Guid('{494bbce9-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_D3DAWARE: Guid = Guid('{494bbced-b031-4e38-97c4-d5422dd618dc}')
MF_TOPOLOGY_RESOLUTION_STATUS: Guid = Guid('{494bbcde-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_ERRORCODE: Guid = Guid('{494bbcee-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_CONNECT_METHOD: Guid = Guid('{494bbcf1-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_LOCKED: Guid = Guid('{494bbcf7-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_WORKQUEUE_ID: Guid = Guid('{494bbcf8-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_WORKQUEUE_MMCSS_CLASS: Guid = Guid('{494bbcf9-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_DECRYPTOR: Guid = Guid('{494bbcfa-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_DISCARDABLE: Guid = Guid('{494bbcfb-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_ERROR_MAJORTYPE: Guid = Guid('{494bbcfd-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_ERROR_SUBTYPE: Guid = Guid('{494bbcfe-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_WORKQUEUE_MMCSS_TASKID: Guid = Guid('{494bbcff-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_WORKQUEUE_MMCSS_PRIORITY: Guid = Guid('{5001f840-2816-48f4-9364-ad1ef661a123}')
MF_TOPONODE_WORKQUEUE_ITEM_PRIORITY: Guid = Guid('{a1ff99be-5e97-4a53-b494-568c642c0ff3}')
MF_TOPONODE_MARKIN_HERE: Guid = Guid('{494bbd00-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_MARKOUT_HERE: Guid = Guid('{494bbd01-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_DECODER: Guid = Guid('{494bbd02-b031-4e38-97c4-d5422dd618dc}')
MF_TOPONODE_MEDIASTART: Guid = Guid('{835c58ea-e075-4bc7-bcba-4de000df9ae6}')
MF_TOPONODE_MEDIASTOP: Guid = Guid('{835c58eb-e075-4bc7-bcba-4de000df9ae6}')
MF_TOPONODE_SOURCE: Guid = Guid('{835c58ec-e075-4bc7-bcba-4de000df9ae6}')
MF_TOPONODE_PRESENTATION_DESCRIPTOR: Guid = Guid('{835c58ed-e075-4bc7-bcba-4de000df9ae6}')
MF_TOPONODE_STREAM_DESCRIPTOR: Guid = Guid('{835c58ee-e075-4bc7-bcba-4de000df9ae6}')
MF_TOPONODE_SEQUENCE_ELEMENTID: Guid = Guid('{835c58ef-e075-4bc7-bcba-4de000df9ae6}')
MF_TOPONODE_TRANSFORM_OBJECTID: Guid = Guid('{88dcc0c9-293e-4e8b-9aeb-0ad64cc016b0}')
MF_TOPONODE_STREAMID: Guid = Guid('{14932f9b-9087-4bb4-8412-5167145cbe04}')
MF_TOPONODE_NOSHUTDOWN_ON_REMOVE: Guid = Guid('{14932f9c-9087-4bb4-8412-5167145cbe04}')
MF_TOPONODE_RATELESS: Guid = Guid('{14932f9d-9087-4bb4-8412-5167145cbe04}')
MF_TOPONODE_DISABLE_PREROLL: Guid = Guid('{14932f9e-9087-4bb4-8412-5167145cbe04}')
MF_TOPONODE_PRIMARYOUTPUT: Guid = Guid('{6304ef99-16b2-4ebe-9d67-e4c539b3a259}')
MF_PD_PMPHOST_CONTEXT: Guid = Guid('{6c990d31-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_APP_CONTEXT: Guid = Guid('{6c990d32-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_DURATION: Guid = Guid('{6c990d33-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_TOTAL_FILE_SIZE: Guid = Guid('{6c990d34-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_AUDIO_ENCODING_BITRATE: Guid = Guid('{6c990d35-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_VIDEO_ENCODING_BITRATE: Guid = Guid('{6c990d36-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_MIME_TYPE: Guid = Guid('{6c990d37-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_LAST_MODIFIED_TIME: Guid = Guid('{6c990d38-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_PLAYBACK_ELEMENT_ID: Guid = Guid('{6c990d39-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_PREFERRED_LANGUAGE: Guid = Guid('{6c990d3a-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_PLAYBACK_BOUNDARY_TIME: Guid = Guid('{6c990d3b-bb8e-477a-8598-0d5d96fcd88a}')
MF_PD_AUDIO_ISVARIABLEBITRATE: Guid = Guid('{33026ee0-e387-4582-ae0a-34a2ad3baa18}')
MF_SD_LANGUAGE: Guid = Guid('{00af2180-bdc2-423c-abca-f503593bc121}')
MF_SD_PROTECTED: Guid = Guid('{00af2181-bdc2-423c-abca-f503593bc121}')
MF_SD_STREAM_NAME: Guid = Guid('{4f1b099d-d314-41e5-a781-7fefaa4c501f}')
MF_SD_MUTUALLY_EXCLUSIVE: Guid = Guid('{023ef79c-388d-487f-ac17-696cd6e3c6f5}')
MF_ACTIVATE_CUSTOM_VIDEO_MIXER_CLSID: Guid = Guid('{ba491360-be50-451e-95ab-6d4accc7dad8}')
MF_ACTIVATE_CUSTOM_VIDEO_MIXER_ACTIVATE: Guid = Guid('{ba491361-be50-451e-95ab-6d4accc7dad8}')
MF_ACTIVATE_CUSTOM_VIDEO_MIXER_FLAGS: Guid = Guid('{ba491362-be50-451e-95ab-6d4accc7dad8}')
MF_ACTIVATE_CUSTOM_VIDEO_PRESENTER_CLSID: Guid = Guid('{ba491364-be50-451e-95ab-6d4accc7dad8}')
MF_ACTIVATE_CUSTOM_VIDEO_PRESENTER_ACTIVATE: Guid = Guid('{ba491365-be50-451e-95ab-6d4accc7dad8}')
MF_ACTIVATE_CUSTOM_VIDEO_PRESENTER_FLAGS: Guid = Guid('{ba491366-be50-451e-95ab-6d4accc7dad8}')
MF_ACTIVATE_MFT_LOCKED: Guid = Guid('{c1f6093c-7f65-4fbd-9e39-5faec3c4fbd7}')
MF_ACTIVATE_VIDEO_WINDOW: Guid = Guid('{9a2dbbdd-f57e-4162-82b9-6831377682d3}')
MF_AUDIO_RENDERER_ATTRIBUTE_FLAGS: Guid = Guid('{ede4b5e0-f805-4d6c-99b3-db01bf95dfab}')
MF_AUDIO_RENDERER_ATTRIBUTE_SESSION_ID: Guid = Guid('{ede4b5e3-f805-4d6c-99b3-db01bf95dfab}')
MF_AUDIO_RENDERER_ATTRIBUTE_ENDPOINT_ID: Guid = Guid('{b10aaec3-ef71-4cc3-b873-05a9a08b9f8e}')
MF_AUDIO_RENDERER_ATTRIBUTE_ENDPOINT_ROLE: Guid = Guid('{6ba644ff-27c5-4d02-9887-c28619fdb91b}')
MF_AUDIO_RENDERER_ATTRIBUTE_STREAM_CATEGORY: Guid = Guid('{a9770471-92ec-4df4-94fe-81c36f0c3a7a}')
MFENABLETYPE_WMDRMV1_LicenseAcquisition: Guid = Guid('{4ff6eeaf-0b43-4797-9b85-abf31815e7b0}')
MFENABLETYPE_WMDRMV7_LicenseAcquisition: Guid = Guid('{003306df-4a06-4884-a097-ef6d22ec84a3}')
MFENABLETYPE_WMDRMV7_Individualization: Guid = Guid('{acd2c84a-b303-4f65-bc2c-2c848d01a989}')
MFENABLETYPE_MF_UpdateRevocationInformation: Guid = Guid('{e558b0b5-b3c4-44a0-924c-50d178932385}')
MFENABLETYPE_MF_UpdateUntrustedComponent: Guid = Guid('{9879f3d6-cee2-48e6-b573-9767ab172f16}')
MFENABLETYPE_MF_RebootRequired: Guid = Guid('{6d4d3d4b-0ece-4652-8b3a-f2d24260d887}')
MF_METADATA_PROVIDER_SERVICE: Guid = Guid('{db214084-58a4-4d2e-b84f-6f755b2f7a0d}')
MF_PROPERTY_HANDLER_SERVICE: Guid = Guid('{a3face02-32b8-41dd-90e7-5fef7c8991b5}')
MF_RATE_CONTROL_SERVICE: Guid = Guid('{866fa297-b802-4bf8-9dc9-5e3b6a9f53c9}')
MF_TIMECODE_SERVICE: Guid = Guid('{a0d502a7-0eb3-4885-b1b9-9feb0d083454}')
MR_POLICY_VOLUME_SERVICE: Guid = Guid('{1abaa2ac-9d3b-47c6-ab48-c59506de784d}')
MR_CAPTURE_POLICY_VOLUME_SERVICE: Guid = Guid('{24030acd-107a-4265-975c-414e33e65f2a}')
MR_STREAM_VOLUME_SERVICE: Guid = Guid('{f8b5fa2f-32ef-46f5-b172-1321212fb2c4}')
MR_AUDIO_POLICY_SERVICE: Guid = Guid('{911fd737-6775-4ab0-a614-297862fdac88}')
MF_SAMPLEGRABBERSINK_SAMPLE_TIME_OFFSET: Guid = Guid('{62e3d776-8100-4e03-a6e8-bd3857ac9c47}')
MF_SAMPLEGRABBERSINK_IGNORE_CLOCK: Guid = Guid('{0efda2c0-2b69-4e2e-ab8d-46dcbff7d25d}')
MF_QUALITY_SERVICES: Guid = Guid('{b7e2be11-2f96-4640-b52c-282365bdf16c}')
MF_WORKQUEUE_SERVICES: Guid = Guid('{8e37d489-41e0-413a-9068-287c886d8dda}')
MF_QUALITY_NOTIFY_PROCESSING_LATENCY: Guid = Guid('{f6b44af8-604d-46fe-a95d-45479b10c9bc}')
MF_QUALITY_NOTIFY_SAMPLE_LAG: Guid = Guid('{30d15206-ed2a-4760-be17-eb4a9f12295c}')
MF_TIME_FORMAT_SEGMENT_OFFSET: Guid = Guid('{c8b8be77-869c-431d-812e-169693f65a39}')
MF_SOURCE_PRESENTATION_PROVIDER_SERVICE: Guid = Guid('{e002aadc-f4af-4ee5-9847-053edf840426}')
MF_TOPONODE_ATTRIBUTE_EDITOR_SERVICE: Guid = Guid('{65656e1a-077f-4472-83ef-316f11d5087a}')
MFNETSOURCE_SSLCERTIFICATE_MANAGER: Guid = Guid('{55e6cb27-e69b-4267-940c-2d7ec5bb8a0f}')
MFNETSOURCE_RESOURCE_FILTER: Guid = Guid('{815d0ff6-265a-4477-9e46-7b80ad80b5fb}')
MFNET_SAVEJOB_SERVICE: Guid = Guid('{b85a587f-3d02-4e52-9565-55d3ec1e7ff7}')
MFNETSOURCE_STATISTICS_SERVICE: Guid = Guid('{3cb1f275-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_STATISTICS: Guid = Guid('{3cb1f274-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_BUFFERINGTIME: Guid = Guid('{3cb1f276-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ACCELERATEDSTREAMINGDURATION: Guid = Guid('{3cb1f277-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_MAXUDPACCELERATEDSTREAMINGDURATION: Guid = Guid('{4aab2879-bbe1-4994-9ff0-5495bd250129}')
MFNETSOURCE_MAXBUFFERTIMEMS: Guid = Guid('{408b24e6-4038-4401-b5b2-fe701a9ebf10}')
MFNETSOURCE_CONNECTIONBANDWIDTH: Guid = Guid('{3cb1f278-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_CACHEENABLED: Guid = Guid('{3cb1f279-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_AUTORECONNECTLIMIT: Guid = Guid('{3cb1f27a-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_RESENDSENABLED: Guid = Guid('{3cb1f27b-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_THINNINGENABLED: Guid = Guid('{3cb1f27c-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROTOCOL: Guid = Guid('{3cb1f27d-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_TRANSPORT: Guid = Guid('{3cb1f27e-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PREVIEWMODEENABLED: Guid = Guid('{3cb1f27f-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_CREDENTIAL_MANAGER: Guid = Guid('{3cb1f280-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PPBANDWIDTH: Guid = Guid('{3cb1f281-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_AUTORECONNECTPROGRESS: Guid = Guid('{3cb1f282-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROXYLOCATORFACTORY: Guid = Guid('{3cb1f283-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_BROWSERUSERAGENT: Guid = Guid('{3cb1f28b-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_BROWSERWEBPAGE: Guid = Guid('{3cb1f28c-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PLAYERVERSION: Guid = Guid('{3cb1f28d-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PLAYERID: Guid = Guid('{3cb1f28e-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_HOSTEXE: Guid = Guid('{3cb1f28f-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_HOSTVERSION: Guid = Guid('{3cb1f291-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PLAYERUSERAGENT: Guid = Guid('{3cb1f292-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_CLIENTGUID: Guid = Guid('{60a2c4a6-f197-4c14-a5bf-88830d2458af}')
MFNETSOURCE_LOGURL: Guid = Guid('{3cb1f293-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_UDP: Guid = Guid('{3cb1f294-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_TCP: Guid = Guid('{3cb1f295-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_MSB: Guid = Guid('{3cb1f296-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_RTSP: Guid = Guid('{3cb1f298-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_HTTP: Guid = Guid('{3cb1f299-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_STREAMING: Guid = Guid('{3cb1f29c-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_DOWNLOAD: Guid = Guid('{3cb1f29d-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_ENABLE_PRIVATEMODE: Guid = Guid('{824779d8-f18b-4405-8cf1-464fb5aa8f71}')
MFNETSOURCE_UDP_PORT_RANGE: Guid = Guid('{3cb1f29a-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROXYINFO: Guid = Guid('{3cb1f29b-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_DRMNET_LICENSE_REPRESENTATION: Guid = Guid('{47eae1bd-bdfe-42e2-82f3-54a48c17962d}')
MFNETSOURCE_PROXYSETTINGS: Guid = Guid('{3cb1f287-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROXYHOSTNAME: Guid = Guid('{3cb1f284-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROXYPORT: Guid = Guid('{3cb1f288-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROXYEXCEPTIONLIST: Guid = Guid('{3cb1f285-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROXYBYPASSFORLOCAL: Guid = Guid('{3cb1f286-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_PROXYRERUNAUTODETECTION: Guid = Guid('{3cb1f289-0505-4c5d-ae71-0a556344efa1}')
MFNETSOURCE_STREAM_LANGUAGE: Guid = Guid('{9ab44318-f7cd-4f2d-8d6d-fa35b492cecb}')
MFNETSOURCE_LOGPARAMS: Guid = Guid('{64936ae8-9418-453a-8cda-3e0a668b353b}')
MFNETSOURCE_PEERMANAGER: Guid = Guid('{48b29adb-febf-45ee-a9bf-efb81c492efc}')
MFNETSOURCE_FRIENDLYNAME: Guid = Guid('{5b2a7757-bc6b-447e-aa06-0dda1c646e2f}')
MF_BYTESTREAMHANDLER_ACCEPTS_SHARE_WRITE: Guid = Guid('{a6e1f733-3001-4915-8150-1558a2180ec8}')
MF_BYTESTREAM_SERVICE: Guid = Guid('{ab025e2b-16d9-4180-a127-ba6c70156161}')
MF_MEDIA_PROTECTION_MANAGER_PROPERTIES: Guid = Guid('{38bd81a9-acea-4c73-89b2-5532c0aeca79}')
MFCONNECTOR_SPDIF: Guid = Guid('{0b94a712-ad3e-4cee-83ce-ce32e3db6522}')
MFCONNECTOR_UNKNOWN: Guid = Guid('{ac3aef5c-ce43-11d9-92db-000bdb28ff98}')
MFCONNECTOR_PCI: Guid = Guid('{ac3aef5d-ce43-11d9-92db-000bdb28ff98}')
MFCONNECTOR_PCIX: Guid = Guid('{ac3aef5e-ce43-11d9-92db-000bdb28ff98}')
MFCONNECTOR_PCI_Express: Guid = Guid('{ac3aef5f-ce43-11d9-92db-000bdb28ff98}')
MFCONNECTOR_AGP: Guid = Guid('{ac3aef60-ce43-11d9-92db-000bdb28ff98}')
MFCONNECTOR_VGA: Guid = Guid('{57cd5968-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_SVIDEO: Guid = Guid('{57cd5969-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_COMPOSITE: Guid = Guid('{57cd596a-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_COMPONENT: Guid = Guid('{57cd596b-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_DVI: Guid = Guid('{57cd596c-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_HDMI: Guid = Guid('{57cd596d-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_LVDS: Guid = Guid('{57cd596e-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_D_JPN: Guid = Guid('{57cd5970-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_SDI: Guid = Guid('{57cd5971-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_DISPLAYPORT_EXTERNAL: Guid = Guid('{57cd5972-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_DISPLAYPORT_EMBEDDED: Guid = Guid('{57cd5973-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_UDI_EXTERNAL: Guid = Guid('{57cd5974-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_UDI_EMBEDDED: Guid = Guid('{57cd5975-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_MIRACAST: Guid = Guid('{57cd5977-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_TRANSPORT_AGNOSTIC_DIGITAL_MODE_A: Guid = Guid('{57cd5978-ce47-11d9-92db-000bdb28ff98}')
MFCONNECTOR_TRANSPORT_AGNOSTIC_DIGITAL_MODE_B: Guid = Guid('{57cd5979-ce47-11d9-92db-000bdb28ff98}')
MF_POLICY_ID: Guid = Guid('{b160c24d-c059-48f1-a901-9ee298a9a8c3}')
MFPROTECTION_DISABLE: Guid = Guid('{8cc6d81b-fec6-4d8f-964b-cfba0b0dad0d}')
MFPROTECTION_CONSTRICTVIDEO: Guid = Guid('{193370ce-c5e4-4c3a-8a66-6959b4da4442}')
MFPROTECTION_CONSTRICTVIDEO_NOOPM: Guid = Guid('{a580e8cd-c247-4957-b983-3c2eebd1ff59}')
MFPROTECTION_CONSTRICTAUDIO: Guid = Guid('{ffc99b44-df48-4e16-8e66-096892c1578a}')
MFPROTECTION_TRUSTEDAUDIODRIVERS: Guid = Guid('{65bdf3d2-0168-4816-a533-55d47b027101}')
MFPROTECTION_HDCP: Guid = Guid('{ae7cc03d-c828-4021-acb7-d578d27aaf13}')
MFPROTECTION_CGMSA: Guid = Guid('{e57e69e9-226b-4d31-b4e3-d3db008736dd}')
MFPROTECTION_ACP: Guid = Guid('{c3fd11c6-f8b7-4d20-b008-1db17d61f2da}')
MFPROTECTION_WMDRMOTA: Guid = Guid('{a267a6a1-362e-47d0-8805-4628598a23e4}')
MFPROTECTION_FFT: Guid = Guid('{462a56b2-2866-4bb6-980d-6d8d9edb1a8c}')
MFPROTECTION_PROTECTED_SURFACE: Guid = Guid('{4f5d9566-e742-4a25-8d1f-d287b5fa0ade}')
MFPROTECTION_DISABLE_SCREEN_SCRAPE: Guid = Guid('{a21179a4-b7cd-40d8-9614-8ef2371ba78d}')
MFPROTECTION_VIDEO_FRAMES: Guid = Guid('{36a59cbc-7401-4a8c-bc20-46a7c9e597f0}')
MFPROTECTION_HARDWARE: Guid = Guid('{4ee7f0c1-9ed7-424f-b6be-996b33528856}')
MFPROTECTION_HDCP_WITH_TYPE_ENFORCEMENT: Guid = Guid('{a4a585e8-ed60-442d-814d-db4d4220a06d}')
MFPROTECTIONATTRIBUTE_BEST_EFFORT: Guid = Guid('{c8e06331-75f0-4ec1-8e77-17578f773b46}')
MFPROTECTIONATTRIBUTE_FAIL_OVER: Guid = Guid('{8536abc5-38f1-4151-9cce-f55d941229ac}')
MFPROTECTION_GRAPHICS_TRANSFER_AES_ENCRYPTION: Guid = Guid('{c873de64-d8a5-49e6-88bb-fb963fd3d4ce}')
MFPROTECTIONATTRIBUTE_CONSTRICTVIDEO_IMAGESIZE: Guid = Guid('{008476fc-4b58-4d80-a790-e7297673161d}')
MFPROTECTIONATTRIBUTE_HDCP_SRM: Guid = Guid('{6f302107-3477-4468-8a08-eef9db10e20f}')
MF_SampleProtectionSalt: Guid = Guid('{5403deee-b9ee-438f-aa83-3804997e569d}')
MF_REMOTE_PROXY: Guid = Guid('{2f00c90e-d2cf-4278-8b6a-d077fac3a25f}')
CLSID_CreateMediaExtensionObject: Guid = Guid('{ef65a54d-0788-45b8-8b14-bc0f6a6b5137}')
MF_SAMI_SERVICE: Guid = Guid('{49a89ae7-b4d9-4ef2-aa5c-f65a3e05ae4e}')
MF_PD_SAMI_STYLELIST: Guid = Guid('{e0b73c7f-486d-484e-9872-4de5192a7bf8}')
MF_SD_SAMI_LANGUAGE: Guid = Guid('{36fcb98a-6cd0-44cb-acb9-a8f5600dd0bb}')
MF_TRANSCODE_CONTAINERTYPE: Guid = Guid('{150ff23f-4abc-478b-ac4f-e1916fba1cca}')
MFTranscodeContainerType_ASF: Guid = Guid('{430f6f6e-b6bf-4fc1-a0bd-9ee46eee2afb}')
MFTranscodeContainerType_MPEG4: Guid = Guid('{dc6cd05d-b9d0-40ef-bd35-fa622c1ab28a}')
MFTranscodeContainerType_MP3: Guid = Guid('{e438b912-83f1-4de6-9e3a-9ffbc6dd24d1}')
MFTranscodeContainerType_FLAC: Guid = Guid('{31344aa3-05a9-42b5-901b-8e9d4257f75e}')
MFTranscodeContainerType_3GP: Guid = Guid('{34c50167-4472-4f34-9ea0-c49fbacf037d}')
MFTranscodeContainerType_AC3: Guid = Guid('{6d8d91c3-8c91-4ed1-8742-8c347d5b44d0}')
MFTranscodeContainerType_ADTS: Guid = Guid('{132fd27d-0f02-43de-a301-38fbbbb3834e}')
MFTranscodeContainerType_MPEG2: Guid = Guid('{bfc2dbf9-7bb4-4f8f-afde-e112c44ba882}')
MFTranscodeContainerType_WAVE: Guid = Guid('{64c3453c-0f26-4741-be63-87bdf8bb935b}')
MFTranscodeContainerType_AVI: Guid = Guid('{7edfe8af-402f-4d76-a33c-619fd157d0f1}')
MFTranscodeContainerType_FMPEG4: Guid = Guid('{9ba876f1-419f-4b77-a1e0-35959d9d4004}')
MFTranscodeContainerType_AMR: Guid = Guid('{025d5ad3-621a-475b-964d-66b1c824f079}')
MF_TRANSCODE_SKIP_METADATA_TRANSFER: Guid = Guid('{4e4469ef-b571-4959-8f83-3dcfba33a393}')
MF_TRANSCODE_TOPOLOGYMODE: Guid = Guid('{3e3df610-394a-40b2-9dea-3bab650bebf2}')
MF_TRANSCODE_ADJUST_PROFILE: Guid = Guid('{9c37c21b-060f-487c-a690-80d7f50d1c72}')
MF_TRANSCODE_ENCODINGPROFILE: Guid = Guid('{6947787c-f508-4ea9-b1e9-a1fe3a49fbc9}')
MF_TRANSCODE_QUALITYVSSPEED: Guid = Guid('{98332df8-03cd-476b-89fa-3f9e442dec9f}')
MF_TRANSCODE_DONOT_INSERT_ENCODER: Guid = Guid('{f45aa7ce-ab24-4012-a11b-dc8220201410}')
MF_VIDEO_PROCESSOR_ALGORITHM: Guid = Guid('{4a0a1e1f-272c-4fb6-9eb1-db330cbc97ca}')
MF_XVP_DISABLE_FRC: Guid = Guid('{2c0afa19-7a97-4d5a-9ee8-16d4fc518d8c}')
MF_XVP_CALLER_ALLOCATES_OUTPUT: Guid = Guid('{04a2cabc-0cab-40b1-a1b9-75bc3658f000}')
MF_LOCAL_MFT_REGISTRATION_SERVICE: Guid = Guid('{ddf5cf9c-4506-45aa-abf0-6d5d94dd1b4a}')
MF_WRAPPED_SAMPLE_SERVICE: Guid = Guid('{31f52bf2-d03e-4048-80d0-9c1046d87c61}')
MF_WRAPPED_OBJECT: Guid = Guid('{2b182c4c-d6ac-49f4-8915-f71887db70cd}')
CLSID_HttpSchemePlugin: Guid = Guid('{44cb442b-9da9-49df-b3fd-023777b16e50}')
CLSID_UrlmonSchemePlugin: Guid = Guid('{9ec4b4f9-3029-45ad-947b-344de2a249e2}')
CLSID_NetSchemePlugin: Guid = Guid('{e9f4ebab-d97b-463e-a2b1-c54ee3f9414d}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE: Guid = Guid('{c60ac5fe-252a-478f-a0ef-bc8fa5f7cad3}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_HW_SOURCE: Guid = Guid('{de7046ba-54d6-4487-a2a4-ec7c0d1bd163}')
MF_DEVSOURCE_ATTRIBUTE_FRIENDLY_NAME: Guid = Guid('{60d0e559-52f8-4fa2-bbce-acdb34a8ec01}')
MF_DEVSOURCE_ATTRIBUTE_MEDIA_TYPE: Guid = Guid('{56a819ca-0c78-4de4-a0a7-3ddaba0f24d4}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_CATEGORY: Guid = Guid('{77f0ae69-c3bd-4509-941d-467e4d24899e}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_SYMBOLIC_LINK: Guid = Guid('{58f0aad8-22bf-4f8a-bb3d-d2c4978c6e2f}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_SYMBOLIC_LINK: Guid = Guid('{98d24b5e-5930-4614-b5a1-f600f9355a78}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_MAX_BUFFERS: Guid = Guid('{7dd9b730-4f2d-41d5-8f95-0cc9a912ba26}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_ENDPOINT_ID: Guid = Guid('{30da9258-feb9-47a7-a453-763a7a8e1c5f}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_ROLE: Guid = Guid('{bc9d118e-8c67-4a18-85d4-12d300400552}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_PROVIDER_DEVICE_ID: Guid = Guid('{36689d42-a06c-40ae-84cf-f5a034067cc4}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_XADDRESS: Guid = Guid('{bca0be52-c327-44c7-9b7d-7fa8d9b5bcda}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_STREAM_URL: Guid = Guid('{9d7b40d2-3617-4043-93e3-8d6da9bb3492}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_USERNAME: Guid = Guid('{05d01add-949f-46eb-bc8e-8b0d2b32d79d}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_PASSWORD: Guid = Guid('{a0fd7e16-42d9-49df-84c0-e82c5eab8874}')
CLSID_FrameServerNetworkCameraSource: Guid = Guid('{7a213aa7-866f-414a-8c1a-275c7283a395}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_GUID: Guid = Guid('{14dd9a1c-7cff-41be-b1b9-ba1ac6ecb571}')
MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_GUID: Guid = Guid('{8ac3587a-4ae7-42d8-99e0-0a6013eef90f}')
MF_DEVICESTREAM_IMAGE_STREAM: Guid = Guid('{a7ffb865-e7b2-43b0-9f6f-9af2a0e50fc0}')
MF_DEVICESTREAM_INDEPENDENT_IMAGE_STREAM: Guid = Guid('{03eeec7e-d605-4576-8b29-6580b490d7d3}')
MF_DEVICESTREAM_STREAM_ID: Guid = Guid('{11bd5120-d124-446b-88e6-17060257fff9}')
MF_DEVICESTREAM_STREAM_CATEGORY: Guid = Guid('{2939e7b8-a62e-4579-b674-d4073dfabbba}')
MF_DEVICESTREAM_FRAMESERVER_SHARED: Guid = Guid('{1cb378e9-b279-41d4-af97-34a243e68320}')
MF_DEVICESTREAM_TRANSFORM_STREAM_ID: Guid = Guid('{e63937b7-daaf-4d49-815f-d826f8ad31e7}')
MF_DEVICESTREAM_EXTENSION_PLUGIN_CLSID: Guid = Guid('{048e6558-60c4-4173-bd5b-6a3ca2896aee}')
MF_DEVICEMFT_EXTENSION_PLUGIN_CLSID: Guid = Guid('{0844dbae-34fa-48a0-a783-8e696fb1c9a8}')
MF_DEVICESTREAM_EXTENSION_PLUGIN_CONNECTION_POINT: Guid = Guid('{37f9375c-e664-4ea4-aae4-cb6d1daca1f4}')
MF_DEVICESTREAM_TAKEPHOTO_TRIGGER: Guid = Guid('{1d180e34-538c-4fbb-a75a-859af7d261a6}')
MF_DEVICESTREAM_MAX_FRAME_BUFFERS: Guid = Guid('{1684cebe-3175-4985-882c-0efd3e8ac11e}')
MF_DEVICEMFT_CONNECTED_FILTER_KSCONTROL: Guid = Guid('{6a2c4fa6-d179-41cd-9523-822371ea40e5}')
MF_DEVICEMFT_CONNECTED_PIN_KSCONTROL: Guid = Guid('{e63310f7-b244-4ef8-9a7d-24c74e32ebd0}')
MF_DEVICE_THERMAL_STATE_CHANGED: Guid = Guid('{70ccd0af-fc9f-4deb-a875-9fecd16c5bd4}')
MFSampleExtension_DeviceTimestamp: Guid = Guid('{8f3e35e7-2dcd-4887-8622-2a58baa652b0}')
MFSampleExtension_Spatial_CameraViewTransform: Guid = Guid('{4e251fa4-830f-4770-859a-4b8d99aa809b}')
MFSampleExtension_Spatial_CameraCoordinateSystem: Guid = Guid('{9d13c82f-2199-4e67-91cd-d1a4181f2534}')
MFSampleExtension_Spatial_CameraProjectionTransform: Guid = Guid('{47f9fcb5-2a02-4f26-a477-792fdf95886a}')
MF_MEDIASOURCE_SERVICE: Guid = Guid('{f09992f7-9fba-4c4a-a37f-8c47b4e1dfe7}')
MF_ACCESS_CONTROLLED_MEDIASOURCE_SERVICE: Guid = Guid('{014a5031-2f05-4c6a-9f9c-7d0dc4eda5f4}')
MF_CONTENT_DECRYPTOR_SERVICE: Guid = Guid('{68a72927-fc7b-44ee-85f4-7c51bd55a659}')
MF_CONTENT_PROTECTION_DEVICE_SERVICE: Guid = Guid('{ff58436f-76a0-41fe-b566-10cc53962edd}')
MF_SD_AUDIO_ENCODER_DELAY: Guid = Guid('{8e85422c-73de-403f-9a35-550ad6e8b951}')
MF_SD_AUDIO_ENCODER_PADDING: Guid = Guid('{529c7f2c-ac4b-4e3f-bfc3-0902194982cb}')
CLSID_MSH264DecoderMFT: Guid = Guid('{62ce7e72-4c71-4d20-b15d-452831a87d9d}')
CLSID_MSH264EncoderMFT: Guid = Guid('{6ca50344-051a-4ded-9779-a43305165e35}')
CLSID_MSDDPlusDecMFT: Guid = Guid('{177c0afe-900b-48d4-9e4c-57add250b3d4}')
CLSID_MP3DecMediaObject: Guid = Guid('{bbeea841-0a63-4f52-a7ab-a9b3a84ed38a}')
CLSID_MSAACDecMFT: Guid = Guid('{32d186a7-218f-4c75-8876-dd77273a8999}')
CLSID_MSH265DecoderMFT: Guid = Guid('{420a51a3-d605-430c-b4fc-45274fa6c562}')
CLSID_WMVDecoderMFT: Guid = Guid('{82d353df-90bd-4382-8bc2-3f6192b76e34}')
CLSID_WMADecMediaObject: Guid = Guid('{2eeb4adf-4578-4d10-bca7-bb955f56320a}')
CLSID_MSMPEGAudDecMFT: Guid = Guid('{70707b39-b2ca-4015-abea-f8447d22d88b}')
CLSID_MSMPEGDecoderMFT: Guid = Guid('{2d709e52-123f-49b5-9cbc-9af5cde28fb9}')
CLSID_AudioResamplerMediaObject: Guid = Guid('{f447b69e-1884-4a7e-8055-346f74d6edb3}')
CLSID_MSVPxDecoder: Guid = Guid('{e3aaf548-c9a4-4c6e-234d-5ada374b0000}')
CLSID_MSOpusDecoder: Guid = Guid('{63e17c10-2d43-4c42-8fe3-8d8b63e46a6a}')
CLSID_VideoProcessorMFT: Guid = Guid('{88753b26-5b24-49bd-b2e7-0c445c78c982}')
MFNETSOURCE_CROSS_ORIGIN_SUPPORT: Guid = Guid('{9842207c-b02c-4271-a2fc-72e49308e5c2}')
MFNETSOURCE_HTTP_DOWNLOAD_SESSION_PROVIDER: Guid = Guid('{7d55081e-307d-4d6d-a663-a93be97c4b5c}')
MF_SD_MEDIASOURCE_STATUS: Guid = Guid('{1913678b-fc0f-44da-8f43-1ba3b526f4ae}')
MF_SD_VIDEO_SPHERICAL: Guid = Guid('{a51da449-3fdc-478c-bcb5-30be76595f55}')
MF_SD_VIDEO_SPHERICAL_FORMAT: Guid = Guid('{4a8fc407-6ea1-46c8-b567-6971d4a139c3}')
MF_SD_VIDEO_SPHERICAL_INITIAL_VIEWDIRECTION: Guid = Guid('{11d25a49-bb62-467f-9db1-c17165716c49}')
MF_MEDIASOURCE_EXPOSE_ALL_STREAMS: Guid = Guid('{e7f250b8-8fd9-4a09-b6c1-6a315c7c720e}')
MF_ST_MEDIASOURCE_COLLECTION: Guid = Guid('{616de972-83ad-4950-8170-630d19cbe307}')
MF_DEVICESTREAM_FILTER_KSCONTROL: Guid = Guid('{46783cca-3df5-4923-a9ef-36b7223edde0}')
MF_DEVICESTREAM_PIN_KSCONTROL: Guid = Guid('{ef3ef9a7-87f2-48ca-be02-674878918e98}')
MF_DEVICESTREAM_SOURCE_ATTRIBUTES: Guid = Guid('{2f8cb617-361b-434f-85ea-99a03e1ce4e0}')
MF_DEVICESTREAM_FRAMESERVER_HIDDEN: Guid = Guid('{f402567b-4d91-4179-96d1-74c8480c2034}')
MF_STF_VERSION_INFO: Guid = Guid('{6770bd39-ef82-44ee-a49b-934beb24aef7}')
MF_STF_VERSION_DATE: Guid = Guid('{31a165d5-df67-4095-8e44-8868fc20dbfd}')
MF_DEVICESTREAM_REQUIRED_CAPABILITIES: Guid = Guid('{6d8b957e-7cf6-43f4-af56-9c0e1e4fcbe1}')
MF_DEVICESTREAM_REQUIRED_SDDL: Guid = Guid('{331ae85d-c0d3-49ba-83ba-82a12d63cdd6}')
MF_DEVICEMFT_SENSORPROFILE_COLLECTION: Guid = Guid('{36ebdc44-b12c-441b-89f4-08b2f41a9cfc}')
MF_DEVICESTREAM_SENSORSTREAM_ID: Guid = Guid('{e35b9fe4-0659-4cad-bb51-33160be7e413}')
KSPROPERTYSETID_ANYCAMERACONTROL: Guid = Guid('{94dd0c30-28c7-4efb-9d6b-812300fb0c7f}')
CLSID_CameraConfigurationManager: Guid = Guid('{6c92b540-5854-4a17-92b6-ac89c96e9683}')
MF_PD_ASF_FILEPROPERTIES_FILE_ID: Guid = Guid('{3de649b4-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_CREATION_TIME: Guid = Guid('{3de649b6-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_PACKETS: Guid = Guid('{3de649b7-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_PLAY_DURATION: Guid = Guid('{3de649b8-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_SEND_DURATION: Guid = Guid('{3de649b9-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_PREROLL: Guid = Guid('{3de649ba-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_FLAGS: Guid = Guid('{3de649bb-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_MIN_PACKET_SIZE: Guid = Guid('{3de649bc-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_MAX_PACKET_SIZE: Guid = Guid('{3de649bd-d76d-4e66-9ec9-78120fb4c7e3}')
MF_PD_ASF_FILEPROPERTIES_MAX_BITRATE: Guid = Guid('{3de649be-d76d-4e66-9ec9-78120fb4c7e3}')
CLSID_WMDRMSystemID: Guid = Guid('{8948bb22-11bd-4796-93e3-974d1b575678}')
MF_PD_ASF_CONTENTENCRYPTION_TYPE: Guid = Guid('{8520fe3d-277e-46ea-99e4-e30a86db12be}')
MF_PD_ASF_CONTENTENCRYPTION_KEYID: Guid = Guid('{8520fe3e-277e-46ea-99e4-e30a86db12be}')
MF_PD_ASF_CONTENTENCRYPTION_SECRET_DATA: Guid = Guid('{8520fe3f-277e-46ea-99e4-e30a86db12be}')
MF_PD_ASF_CONTENTENCRYPTION_LICENSE_URL: Guid = Guid('{8520fe40-277e-46ea-99e4-e30a86db12be}')
MF_PD_ASF_CONTENTENCRYPTIONEX_ENCRYPTION_DATA: Guid = Guid('{62508be5-ecdf-4924-a359-72bab3397b9d}')
MF_PD_ASF_LANGLIST: Guid = Guid('{f23de43c-9977-460d-a6ec-32937f160f7d}')
MF_PD_ASF_LANGLIST_LEGACYORDER: Guid = Guid('{f23de43d-9977-460d-a6ec-32937f160f7d}')
MF_PD_ASF_MARKER: Guid = Guid('{5134330e-83a6-475e-a9d5-4fb875fb2e31}')
MF_PD_ASF_SCRIPT: Guid = Guid('{e29cd0d7-d602-4923-a7fe-73fd97ecc650}')
MF_PD_ASF_CODECLIST: Guid = Guid('{e4bb3509-c18d-4df1-bb99-7a36b3cc4119}')
MF_PD_ASF_METADATA_IS_VBR: Guid = Guid('{5fc6947a-ef60-445d-b449-442ecc78b4c1}')
MF_PD_ASF_METADATA_V8_VBRPEAK: Guid = Guid('{5fc6947b-ef60-445d-b449-442ecc78b4c1}')
MF_PD_ASF_METADATA_V8_BUFFERAVERAGE: Guid = Guid('{5fc6947c-ef60-445d-b449-442ecc78b4c1}')
MF_PD_ASF_METADATA_LEAKY_BUCKET_PAIRS: Guid = Guid('{5fc6947d-ef60-445d-b449-442ecc78b4c1}')
MF_PD_ASF_DATA_START_OFFSET: Guid = Guid('{e7d5b3e7-1f29-45d3-8822-3e78fae272ed}')
MF_PD_ASF_DATA_LENGTH: Guid = Guid('{e7d5b3e8-1f29-45d3-8822-3e78fae272ed}')
MF_SD_ASF_EXTSTRMPROP_LANGUAGE_ID_INDEX: Guid = Guid('{48f8a522-305d-422d-8524-2502dda33680}')
MF_SD_ASF_EXTSTRMPROP_AVG_DATA_BITRATE: Guid = Guid('{48f8a523-305d-422d-8524-2502dda33680}')
MF_SD_ASF_EXTSTRMPROP_AVG_BUFFERSIZE: Guid = Guid('{48f8a524-305d-422d-8524-2502dda33680}')
MF_SD_ASF_EXTSTRMPROP_MAX_DATA_BITRATE: Guid = Guid('{48f8a525-305d-422d-8524-2502dda33680}')
MF_SD_ASF_EXTSTRMPROP_MAX_BUFFERSIZE: Guid = Guid('{48f8a526-305d-422d-8524-2502dda33680}')
MF_SD_ASF_STREAMBITRATES_BITRATE: Guid = Guid('{a8e182ed-afc8-43d0-b0d1-f65bad9da558}')
MF_SD_ASF_METADATA_DEVICE_CONFORMANCE_TEMPLATE: Guid = Guid('{245e929d-c44e-4f7e-bb3c-77d4dfd27f8a}')
MF_PD_ASF_INFO_HAS_AUDIO: Guid = Guid('{80e62295-2296-4a44-b31c-d103c6fed23c}')
MF_PD_ASF_INFO_HAS_VIDEO: Guid = Guid('{80e62296-2296-4a44-b31c-d103c6fed23c}')
MF_PD_ASF_INFO_HAS_NON_AUDIO_VIDEO: Guid = Guid('{80e62297-2296-4a44-b31c-d103c6fed23c}')
MF_ASFPROFILE_MINPACKETSIZE: Guid = Guid('{22587626-47de-4168-87f5-b5aa9b12a8f0}')
MF_ASFPROFILE_MAXPACKETSIZE: Guid = Guid('{22587627-47de-4168-87f5-b5aa9b12a8f0}')
MF_ASFSTREAMCONFIG_LEAKYBUCKET1: Guid = Guid('{c69b5901-ea1a-4c9b-b692-e2a0d29a8add}')
MF_ASFSTREAMCONFIG_LEAKYBUCKET2: Guid = Guid('{c69b5902-ea1a-4c9b-b692-e2a0d29a8add}')
MFASFSampleExtension_SampleDuration: Guid = Guid('{c6bd9450-867f-4907-83a3-c77921b733ad}')
MFASFSampleExtension_OutputCleanPoint: Guid = Guid('{f72a3c6f-6eb4-4ebc-b192-09ad9759e828}')
MFASFSampleExtension_SMPTE: Guid = Guid('{399595ec-8667-4e2d-8fdb-98814ce76c1e}')
MFASFSampleExtension_FileName: Guid = Guid('{e165ec0e-19ed-45d7-b4a7-25cbd1e28e9b}')
MFASFSampleExtension_ContentType: Guid = Guid('{d590dc20-07bc-436c-9cf7-f3bbfbf1a4dc}')
MFASFSampleExtension_PixelAspectRatio: Guid = Guid('{1b1ee554-f9ea-4bc8-821a-376b74e4c4b8}')
MFASFSampleExtension_Encryption_SampleID: Guid = Guid('{6698b84e-0afa-4330-aeb2-1c0a98d7a44d}')
MFASFSampleExtension_Encryption_KeyID: Guid = Guid('{76376591-795f-4da1-86ed-9d46eca109a9}')
MFASFMutexType_Language: Guid = Guid('{72178c2b-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFASFMutexType_Bitrate: Guid = Guid('{72178c2c-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFASFMutexType_Presentation: Guid = Guid('{72178c2d-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFASFMutexType_Unknown: Guid = Guid('{72178c2e-e45b-11d5-bc2a-00b0d0f3f4ab}')
MFASFSPLITTER_PACKET_BOUNDARY: Guid = Guid('{fe584a05-e8d6-42e3-b176-f1211705fb6f}')
MFASFINDEXER_TYPE_TIMECODE: Guid = Guid('{49815231-6bad-44fd-810a-3f60984ec7fd}')
MF_CAPTURE_ENGINE_INITIALIZED: Guid = Guid('{219992bc-cf92-4531-a1ae-96e1e886c8f1}')
MF_CAPTURE_ENGINE_PREVIEW_STARTED: Guid = Guid('{a416df21-f9d3-4a74-991b-b817298952c4}')
MF_CAPTURE_ENGINE_PREVIEW_STOPPED: Guid = Guid('{13d5143c-1edd-4e50-a2ef-350a47678060}')
MF_CAPTURE_ENGINE_RECORD_STARTED: Guid = Guid('{ac2b027b-ddf9-48a0-89be-38ab35ef45c0}')
MF_CAPTURE_ENGINE_RECORD_STOPPED: Guid = Guid('{55e5200a-f98f-4c0d-a9ec-9eb25ed3d773}')
MF_CAPTURE_ENGINE_PHOTO_TAKEN: Guid = Guid('{3c50c445-7304-48eb-865d-bba19ba3af5c}')
MF_CAPTURE_SOURCE_CURRENT_DEVICE_MEDIA_TYPE_SET: Guid = Guid('{e7e75e4c-039c-4410-815b-8741307b63aa}')
MF_CAPTURE_ENGINE_ERROR: Guid = Guid('{46b89fc6-33cc-4399-9dad-784de77d587c}')
MF_CAPTURE_ENGINE_EFFECT_ADDED: Guid = Guid('{aa8dc7b5-a048-4e13-8ebe-f23c46c830c1}')
MF_CAPTURE_ENGINE_EFFECT_REMOVED: Guid = Guid('{c6e8db07-fb09-4a48-89c6-bf92a04222c9}')
MF_CAPTURE_ENGINE_ALL_EFFECTS_REMOVED: Guid = Guid('{fded7521-8ed8-431a-a96b-f3e2565e981c}')
MF_CAPTURE_SINK_PREPARED: Guid = Guid('{7bfce257-12b1-4409-8c34-d445daab7578}')
MF_CAPTURE_ENGINE_OUTPUT_MEDIA_TYPE_SET: Guid = Guid('{caaad994-83ec-45e9-a30a-1f20aadb9831}')
MF_CAPTURE_ENGINE_CAMERA_STREAM_BLOCKED: Guid = Guid('{a4209417-8d39-46f3-b759-5912528f4207}')
MF_CAPTURE_ENGINE_CAMERA_STREAM_UNBLOCKED: Guid = Guid('{9be9eef0-cdaf-4717-8564-834aae66415c}')
MF_CAPTURE_ENGINE_D3D_MANAGER: Guid = Guid('{76e25e7b-d595-4283-962c-c594afd78ddf}')
MF_CAPTURE_ENGINE_RECORD_SINK_VIDEO_MAX_UNPROCESSED_SAMPLES: Guid = Guid('{b467f705-7913-4894-9d42-a215fea23da9}')
MF_CAPTURE_ENGINE_RECORD_SINK_AUDIO_MAX_UNPROCESSED_SAMPLES: Guid = Guid('{1cddb141-a7f4-4d58-9896-4d15a53c4efe}')
MF_CAPTURE_ENGINE_RECORD_SINK_VIDEO_MAX_PROCESSED_SAMPLES: Guid = Guid('{e7b4a49e-382c-4aef-a946-aed5490b7111}')
MF_CAPTURE_ENGINE_RECORD_SINK_AUDIO_MAX_PROCESSED_SAMPLES: Guid = Guid('{9896e12a-f707-4500-b6bd-db8eb810b50f}')
MF_CAPTURE_ENGINE_USE_AUDIO_DEVICE_ONLY: Guid = Guid('{1c8077da-8466-4dc4-8b8e-276b3f85923b}')
MF_CAPTURE_ENGINE_USE_VIDEO_DEVICE_ONLY: Guid = Guid('{7e025171-cf32-4f2e-8f19-410577b73a66}')
MF_CAPTURE_ENGINE_DISABLE_HARDWARE_TRANSFORMS: Guid = Guid('{b7c42a6b-3207-4495-b4e7-81f9c35d5991}')
MF_CAPTURE_ENGINE_DISABLE_DXVA: Guid = Guid('{f9818862-179d-433f-a32f-74cbcf74466d}')
MF_CAPTURE_ENGINE_MEDIASOURCE_CONFIG: Guid = Guid('{bc6989d2-0fc1-46e1-a74f-efd36bc788de}')
MF_CAPTURE_ENGINE_DECODER_MFT_FIELDOFUSE_UNLOCK_Attribute: Guid = Guid('{2b8ad2e8-7acb-4321-a606-325c4249f4fc}')
MF_CAPTURE_ENGINE_ENCODER_MFT_FIELDOFUSE_UNLOCK_Attribute: Guid = Guid('{54c63a00-78d5-422f-aa3e-5e99ac649269}')
MF_CAPTURE_ENGINE_ENABLE_CAMERA_STREAMSTATE_NOTIFICATION: Guid = Guid('{4c808e9d-aaed-4713-90fb-cb24064ab8da}')
MF_CAPTURE_ENGINE_MEDIA_CATEGORY: Guid = Guid('{8e3f5bd5-dbbf-42f0-8542-d07a3971762a}')
MF_CAPTURE_ENGINE_AUDIO_PROCESSING: Guid = Guid('{10f1be5e-7e11-410b-973d-f4b6109000fe}')
MF_CAPTURE_ENGINE_EVENT_GENERATOR_GUID: Guid = Guid('{abfa8ad5-fc6d-4911-87e0-961945f8f7ce}')
MF_CAPTURE_ENGINE_EVENT_STREAM_INDEX: Guid = Guid('{82697f44-b1cf-42eb-9753-f86d649c8865}')
MF_CAPTURE_ENGINE_SELECTEDCAMERAPROFILE: Guid = Guid('{03160b7e-1c6f-4db2-ad56-a7c430f82392}')
MF_CAPTURE_ENGINE_SELECTEDCAMERAPROFILE_INDEX: Guid = Guid('{3ce88613-2214-46c3-b417-82f8a313c9c3}')
CLSID_MFCaptureEngine: Guid = Guid('{efce38d3-8914-4674-a7df-ae1b3d654b8a}')
CLSID_MFCaptureEngineClassFactory: Guid = Guid('{efce38d3-8914-4674-a7df-ae1b3d654b8a}')
MFSampleExtension_DeviceReferenceSystemTime: Guid = Guid('{6523775a-ba2d-405f-b2c5-01ff88e2e8f6}')
MF_D3D12_SYNCHRONIZATION_OBJECT: Guid = Guid('{2a7c8d6a-85a6-494d-a046-06ea1a138f4b}')
MF_MT_D3D_RESOURCE_VERSION: Guid = Guid('{174f1e85-fe26-453d-b52e-5bdd4e55b944}')
MF_MT_D3D12_CPU_READBACK: Guid = Guid('{28ee9fe3-d481-46a6-b98a-7f69d5280e82}')
MF_MT_D3D12_TEXTURE_LAYOUT: Guid = Guid('{97c85caa-0beb-4ee1-9715-f22fad8c10f5}')
MF_MT_D3D12_RESOURCE_FLAG_ALLOW_RENDER_TARGET: Guid = Guid('{eeac2585-3430-498c-84a2-77b1bba570f6}')
MF_MT_D3D12_RESOURCE_FLAG_ALLOW_DEPTH_STENCIL: Guid = Guid('{b1138dc3-01d5-4c14-9bdc-cdc9336f55b9}')
MF_MT_D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS: Guid = Guid('{82c85647-5057-4960-9559-f45b8e271427}')
MF_MT_D3D12_RESOURCE_FLAG_DENY_SHADER_RESOURCE: Guid = Guid('{ba06bfac-ffe3-474a-ab55-161ee4417a2e}')
MF_MT_D3D12_RESOURCE_FLAG_ALLOW_CROSS_ADAPTER: Guid = Guid('{a6a1e439-2f96-4ab5-98dc-adf74973505d}')
MF_MT_D3D12_RESOURCE_FLAG_ALLOW_SIMULTANEOUS_ACCESS: Guid = Guid('{0a4940b2-cfd6-4738-9d02-98113734015a}')
MF_SA_D3D12_HEAP_FLAGS: Guid = Guid('{496b3266-d28f-4f8c-93a7-4a596b1a31a1}')
MF_SA_D3D12_HEAP_TYPE: Guid = Guid('{56f26a76-bbc1-4ce0-bb11-e22368d874ed}')
MF_SA_D3D12_CLEAR_VALUE: Guid = Guid('{86ba9a39-0526-495d-9ab5-54ec9fad6fc3}')
MF_MSE_CALLBACK: Guid = Guid('{9063a7c0-42c5-4ffd-a8a8-6fcf9ea3d00c}')
MF_MSE_ACTIVELIST_CALLBACK: Guid = Guid('{949bda0f-4549-46d5-ad7f-b846e1ab1652}')
MF_MSE_BUFFERLIST_CALLBACK: Guid = Guid('{42e669b0-d60e-4afb-a85b-d8e5fe6bdab5}')
MF_MSE_VP9_SUPPORT: Guid = Guid('{92d78429-d88b-4ff0-8322-803efa6e9626}')
MF_MSE_OPUS_SUPPORT: Guid = Guid('{4d224cc1-8cc4-48a3-a7a7-e4c16ce6388a}')
MF_MEDIA_ENGINE_NEEDKEY_CALLBACK: Guid = Guid('{7ea80843-b6e4-432c-8ea4-7848ffe4220e}')
MF_MEDIA_ENGINE_CALLBACK: Guid = Guid('{c60381b8-83a4-41f8-a3d0-de05076849a9}')
MF_MEDIA_ENGINE_DXGI_MANAGER: Guid = Guid('{065702da-1094-486d-8617-ee7cc4ee4648}')
MF_MEDIA_ENGINE_EXTENSION: Guid = Guid('{3109fd46-060d-4b62-8dcf-faff811318d2}')
MF_MEDIA_ENGINE_PLAYBACK_HWND: Guid = Guid('{d988879b-67c9-4d92-baa7-6eadd446039d}')
MF_MEDIA_ENGINE_OPM_HWND: Guid = Guid('{a0be8ee7-0572-4f2c-a801-2a151bd3e726}')
MF_MEDIA_ENGINE_PLAYBACK_VISUAL: Guid = Guid('{6debd26f-6ab9-4d7e-b0ee-c61a73ffad15}')
MF_MEDIA_ENGINE_COREWINDOW: Guid = Guid('{fccae4dc-0b7f-41c2-9f96-4659948acddc}')
MF_MEDIA_ENGINE_VIDEO_OUTPUT_FORMAT: Guid = Guid('{5066893c-8cf9-42bc-8b8a-472212e52726}')
MF_MEDIA_ENGINE_CONTENT_PROTECTION_FLAGS: Guid = Guid('{e0350223-5aaf-4d76-a7c3-06de70894db4}')
MF_MEDIA_ENGINE_CONTENT_PROTECTION_MANAGER: Guid = Guid('{fdd6dfaa-bd85-4af3-9e0f-a01d539d876a}')
MF_MEDIA_ENGINE_AUDIO_ENDPOINT_ROLE: Guid = Guid('{d2cb93d1-116a-44f2-9385-f7d0fda2fb46}')
MF_MEDIA_ENGINE_AUDIO_CATEGORY: Guid = Guid('{c8d4c51d-350e-41f2-ba46-faebbb0857f6}')
MF_MEDIA_ENGINE_STREAM_CONTAINS_ALPHA_CHANNEL: Guid = Guid('{5cbfaf44-d2b2-4cfb-80a7-d429c74c789d}')
MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE: Guid = Guid('{4e0212e2-e18f-41e1-95e5-c0e7e9235bc3}')
MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE9: Guid = Guid('{052c2d39-40c0-4188-ab86-f828273b7522}')
MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE10: Guid = Guid('{11a47afd-6589-4124-b312-6158ec517fc3}')
MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE11: Guid = Guid('{1cf1315f-ce3f-4035-9391-16142f775189}')
MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE_EDGE: Guid = Guid('{a6f3e465-3aca-442c-a3f0-ad6ddad839ae}')
MF_MEDIA_ENGINE_COMPATIBILITY_MODE: Guid = Guid('{3ef26ad4-dc54-45de-b9af-76c8c66bfa8e}')
MF_MEDIA_ENGINE_COMPATIBILITY_MODE_WWA_EDGE: Guid = Guid('{15b29098-9f01-4e4d-b65a-c06c6c89da2a}')
MF_MEDIA_ENGINE_COMPATIBILITY_MODE_WIN10: Guid = Guid('{5b25e089-6ca7-4139-a2cb-fcaab39552a3}')
MF_MEDIA_ENGINE_SOURCE_RESOLVER_CONFIG_STORE: Guid = Guid('{0ac0c497-b3c4-48c9-9cde-bb8ca2442ca3}')
MF_MEDIA_ENGINE_TRACK_ID: Guid = Guid('{65bea312-4043-4815-8eab-44dce2ef8f2a}')
MF_MEDIA_ENGINE_TELEMETRY_APPLICATION_ID: Guid = Guid('{1e7b273b-a7e4-402a-8f51-c48e88a2cabc}')
MF_MEDIA_ENGINE_SYNCHRONOUS_CLOSE: Guid = Guid('{c3c2e12f-7e0e-4e43-b91c-dc992ccdfa5e}')
MF_MEDIA_ENGINE_MEDIA_PLAYER_MODE: Guid = Guid('{3ddd8d45-5aa1-4112-82e5-36f6a2197e6e}')
CLSID_MFMediaEngineClassFactory: Guid = Guid('{b44392da-499b-446b-a4cb-005fead0e6d5}')
MF_MEDIA_ENGINE_TIMEDTEXT: Guid = Guid('{805ea411-92e0-4e59-9b6e-5c7d7915e64f}')
MF_MEDIA_ENGINE_CONTINUE_ON_CODEC_ERROR: Guid = Guid('{dbcdb7f9-48e4-4295-b70d-d518234eeb38}')
MF_MEDIA_ENGINE_EME_CALLBACK: Guid = Guid('{494553a7-a481-4cb7-bec5-380903513731}')
CLSID_MPEG2DLNASink: Guid = Guid('{fa5fe7c5-6a1d-4b11-b41f-f959d6c76500}')
MF_MP2DLNA_USE_MMCSS: Guid = Guid('{54f3e2ee-a2a2-497d-9834-973afde521eb}')
MF_MP2DLNA_VIDEO_BIT_RATE: Guid = Guid('{e88548de-73b4-42d7-9c75-adfa0a2a6e4c}')
MF_MP2DLNA_AUDIO_BIT_RATE: Guid = Guid('{2d1c070e-2b5f-4ab3-a7e6-8d943ba8d00a}')
MF_MP2DLNA_ENCODE_QUALITY: Guid = Guid('{b52379d7-1d46-4fb6-a317-a4a5f60959f8}')
MF_MP2DLNA_STATISTICS: Guid = Guid('{75e488a3-d5ad-4898-85e0-bcce24a722d7}')
CLSID_MFReadWriteClassFactory: Guid = Guid('{48e2ed0f-98c2-4a37-bed5-166312ddd83f}')
CLSID_MFSourceReader: Guid = Guid('{1777133c-0881-411b-a577-ad545f0714c4}')
MF_SOURCE_READER_ASYNC_CALLBACK: Guid = Guid('{1e3dbeac-bb43-4c35-b507-cd644464c965}')
MF_SOURCE_READER_D3D_MANAGER: Guid = Guid('{ec822da2-e1e9-4b29-a0d8-563c719f5269}')
MF_SOURCE_READER_DISABLE_DXVA: Guid = Guid('{aa456cfd-3943-4a1e-a77d-1838c0ea2e35}')
MF_SOURCE_READER_MEDIASOURCE_CONFIG: Guid = Guid('{9085abeb-0354-48f9-abb5-200df838c68e}')
MF_SOURCE_READER_MEDIASOURCE_CHARACTERISTICS: Guid = Guid('{6d23f5c8-c5d7-4a9b-9971-5d11f8bca880}')
MF_SOURCE_READER_ENABLE_VIDEO_PROCESSING: Guid = Guid('{fb394f3d-ccf1-42ee-bbb3-f9b845d5681d}')
MF_SOURCE_READER_ENABLE_ADVANCED_VIDEO_PROCESSING: Guid = Guid('{0f81da2c-b537-4672-a8b2-a681b17307a3}')
MF_SOURCE_READER_DISABLE_CAMERA_PLUGINS: Guid = Guid('{9d3365dd-058f-4cfb-9f97-b314cc99c8ad}')
MF_SOURCE_READER_DISCONNECT_MEDIASOURCE_ON_SHUTDOWN: Guid = Guid('{56b67165-219e-456d-a22e-2d3004c7fe56}')
MF_SOURCE_READER_ENABLE_TRANSCODE_ONLY_TRANSFORMS: Guid = Guid('{dfd4f008-b5fd-4e78-ae44-62a1e67bbe27}')
MF_SOURCE_READER_D3D11_BIND_FLAGS: Guid = Guid('{33f3197b-f73a-4e14-8d85-0e4c4368788d}')
CLSID_MFSinkWriter: Guid = Guid('{a3bbfb17-8273-4e52-9e0e-9739dc887990}')
MF_SINK_WRITER_ASYNC_CALLBACK: Guid = Guid('{48cb183e-7b0b-46f4-822e-5e1d2dda4354}')
MF_SINK_WRITER_DISABLE_THROTTLING: Guid = Guid('{08b845d8-2b74-4afe-9d53-be16d2d5ae4f}')
MF_SINK_WRITER_D3D_MANAGER: Guid = Guid('{ec822da2-e1e9-4b29-a0d8-563c719f5269}')
MF_SINK_WRITER_ENCODER_CONFIG: Guid = Guid('{ad91cd04-a7cc-4ac7-99b6-a57b9a4a7c70}')
MF_READWRITE_DISABLE_CONVERTERS: Guid = Guid('{98d5b065-1374-4847-8d5d-31520fee7156}')
MF_READWRITE_ENABLE_HARDWARE_TRANSFORMS: Guid = Guid('{a634a91c-822b-41b9-a494-4de4643612b0}')
MF_READWRITE_MMCSS_CLASS: Guid = Guid('{39384300-d0eb-40b1-87a0-3318871b5a53}')
MF_READWRITE_MMCSS_PRIORITY: Guid = Guid('{43ad19ce-f33f-4ba9-a580-e4cd12f2d144}')
MF_READWRITE_MMCSS_CLASS_AUDIO: Guid = Guid('{430847da-0890-4b0e-938c-054332c547e1}')
MF_READWRITE_MMCSS_PRIORITY_AUDIO: Guid = Guid('{273db885-2de2-4db2-a6a7-fdb66fb40b61}')
MF_READWRITE_D3D_OPTIONAL: Guid = Guid('{216479d9-3071-42ca-bb6c-4c22102e1d18}')
MF_MEDIASINK_AUTOFINALIZE_SUPPORTED: Guid = Guid('{48c131be-135a-41cb-8290-03652509c999}')
MF_MEDIASINK_ENABLE_AUTOFINALIZE: Guid = Guid('{34014265-cb7e-4cde-ac7c-effd3b3c2530}')
MF_READWRITE_ENABLE_AUTOFINALIZE: Guid = Guid('{dd7ca129-8cd1-4dc5-9dde-ce168675de61}')
MFP_POSITIONTYPE_100NS: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
MF_MEDIA_SHARING_ENGINE_DEVICE_NAME: Guid = Guid('{771e05d1-862f-4299-95ac-ae81fd14f3e7}')
MF_MEDIA_SHARING_ENGINE_DEVICE: Guid = Guid('{b461c58a-7a08-4b98-99a8-70fd5f3badfd}')
CLSID_MFMediaSharingEngineClassFactory: Guid = Guid('{f8e307fb-6d45-4ad3-9993-66cd5a529659}')
CLSID_MFImageSharingEngineClassFactory: Guid = Guid('{b22c3339-87f3-4059-a0c5-037aa9707eaf}')
CLSID_PlayToSourceClassFactory: Guid = Guid('{da17539a-3dc3-42c1-a749-a183b51f085e}')
GUID_PlayToService: Guid = Guid('{f6a8ff9d-9e14-41c9-bf0f-120a2b3ce120}')
GUID_NativeDeviceService: Guid = Guid('{ef71e53c-52f4-43c5-b86a-ad6cb216a61e}')
MF_CONTENTDECRYPTIONMODULE_SERVICE: Guid = Guid('{15320c45-ff80-484a-9dcb-0df894e69a01}')
MF_DEVSOURCE_ATTRIBUTE_ENABLE_MS_CAMERA_EFFECTS: Guid = Guid('{28a5531a-57dd-4fd5-aaa7-385abf57d785}')
MF_VIRTUALCAMERA_ASSOCIATED_CAMERA_SOURCES: Guid = Guid('{1bb79e7c-5d83-438c-94d8-e5f0df6d3279}')
MF_VIRTUALCAMERA_PROVIDE_ASSOCIATED_CAMERA_SOURCES: Guid = Guid('{f0273718-4a4d-4ac5-a15d-305eb5e90667}')
MF_VIRTUALCAMERA_CONFIGURATION_APP_PACKAGE_FAMILY_NAME: Guid = Guid('{658abe51-8044-462e-97ea-e676fd72055f}')
MF_FRAMESERVER_VCAMEVENT_EXTENDED_SOURCE_INITIALIZE: Guid = Guid('{e52c4dff-e46d-4d0b-bc75-ddd4c8723f96}')
MF_FRAMESERVER_VCAMEVENT_EXTENDED_SOURCE_START: Guid = Guid('{b1eeb989-b456-4f4a-ae40-079c28e24af8}')
MF_FRAMESERVER_VCAMEVENT_EXTENDED_SOURCE_STOP: Guid = Guid('{b7fe7a61-fe91-415e-8608-d37dedb1a58b}')
MF_FRAMESERVER_VCAMEVENT_EXTENDED_SOURCE_UNINITIALIZE: Guid = Guid('{a0ebaba7-a422-4e33-8401-b37d2800aa67}')
MF_FRAMESERVER_VCAMEVENT_EXTENDED_PIPELINE_SHUTDOWN: Guid = Guid('{45a81b31-43f8-4e5d-8ce2-22dce026996d}')
MF_FRAMESERVER_VCAMEVENT_EXTENDED_CUSTOM_EVENT: Guid = Guid('{6e59489c-47d3-4467-83ef-12d34e871665}')
@winfunctype('dxva2.dll')
def DXVAHD_CreateDevice(pD3DDevice: Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9Ex_head, pContentDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CONTENT_DESC_head), Usage: Windows.Win32.Media.MediaFoundation.DXVAHD_DEVICE_USAGE, pPlugin: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_Plugin, ppDevice: POINTER(Windows.Win32.Media.MediaFoundation.IDXVAHD_Device_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxva2.dll')
def DXVA2CreateDirect3DDeviceManager9(pResetToken: POINTER(UInt32), ppDeviceManager: POINTER(Windows.Win32.Media.MediaFoundation.IDirect3DDeviceManager9_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxva2.dll')
def DXVA2CreateVideoService(pDD: Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9_head, riid: POINTER(Guid), ppService: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxva2.dll')
def OPMGetVideoOutputsFromHMONITOR(hMonitor: Windows.Win32.Graphics.Gdi.HMONITOR, vos: Windows.Win32.Media.MediaFoundation.OPM_VIDEO_OUTPUT_SEMANTICS, pulNumVideoOutputs: POINTER(UInt32), pppOPMVideoOutputArray: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.IOPMVideoOutput_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxva2.dll')
def OPMGetVideoOutputForTarget(pAdapterLuid: POINTER(Windows.Win32.Foundation.LUID_head), VidPnTarget: UInt32, vos: Windows.Win32.Media.MediaFoundation.OPM_VIDEO_OUTPUT_SEMANTICS, ppOPMVideoOutput: POINTER(Windows.Win32.Media.MediaFoundation.IOPMVideoOutput_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxva2.dll')
def OPMGetVideoOutputsFromIDirect3DDevice9Object(pDirect3DDevice9: Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9_head, vos: Windows.Win32.Media.MediaFoundation.OPM_VIDEO_OUTPUT_SEMANTICS, pulNumVideoOutputs: POINTER(UInt32), pppOPMVideoOutputArray: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.IOPMVideoOutput_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFSerializeAttributesToStream(pAttr: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, dwOptions: UInt32, pStm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFDeserializeAttributesFromStream(pAttr: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, dwOptions: UInt32, pStm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateTransformActivate(ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateMediaSession(pConfiguration: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppMediaSession: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreatePMPMediaSession(dwCreationFlags: UInt32, pConfiguration: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppMediaSession: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSession_head), ppEnablerActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateSourceResolver(ppISourceResolver: POINTER(Windows.Win32.Media.MediaFoundation.IMFSourceResolver_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def CreatePropertyStore(ppStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetSupportedSchemes(pPropVarSchemeArray: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetSupportedMimeTypes(pPropVarMimeTypeArray: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateTopology(ppTopo: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopology_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateTopologyNode(NodeType: Windows.Win32.Media.MediaFoundation.MF_TOPOLOGY_TYPE, ppNode: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFGetTopoNodeCurrentType(pNode: Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head, dwStreamIndex: UInt32, fOutput: Windows.Win32.Foundation.BOOL, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFGetService(punkObject: Windows.Win32.System.Com.IUnknown_head, guidService: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetSystemTime() -> Int64: ...
@winfunctype('MF.dll')
def MFCreatePresentationClock(ppPresentationClock: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateSystemTimeSource(ppSystemTimeSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationTimeSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreatePresentationDescriptor(cStreamDescriptors: UInt32, apStreamDescriptors: POINTER(Windows.Win32.Media.MediaFoundation.IMFStreamDescriptor_head), ppPresentationDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFRequireProtectedEnvironment(pPresentationDescriptor: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFSerializePresentationDescriptor(pPD: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head, pcbData: POINTER(UInt32), ppbData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFDeserializePresentationDescriptor(cbData: UInt32, pbData: POINTER(Byte), ppPD: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateStreamDescriptor(dwStreamIdentifier: UInt32, cMediaTypes: UInt32, apMediaTypes: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head), ppDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.IMFStreamDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateSimpleTypeHandler(ppHandler: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTypeHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFShutdownObject(pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateAudioRenderer(pAudioAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateAudioRendererActivate(ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateVideoRendererActivate(hwndVideo: Windows.Win32.Foundation.HWND, ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateMPEG4MediaSink(pIByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pVideoMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppIMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreate3GPMediaSink(pIByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pVideoMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppIMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateMP3MediaSink(pTargetByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, ppMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateAC3MediaSink(pTargetByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateADTSMediaSink(pTargetByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateMuxSink(guidOutputSubType: Guid, pOutputAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pOutputByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, ppMuxSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateFMPEG4MediaSink(pIByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pVideoMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppIMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mfsrcsnk.dll')
def MFCreateAVIMediaSink(pIByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pVideoMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppIMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mfsrcsnk.dll')
def MFCreateWAVEMediaSink(pTargetByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateTopoLoader(ppObj: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopoLoader_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateSampleGrabberSinkActivate(pIMFMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pIMFSampleGrabberSinkCallback: Windows.Win32.Media.MediaFoundation.IMFSampleGrabberSinkCallback_head, ppIActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateStandardQualityManager(ppQualityManager: POINTER(Windows.Win32.Media.MediaFoundation.IMFQualityManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateSequencerSource(pReserved: Windows.Win32.System.Com.IUnknown_head, ppSequencerSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFSequencerSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateSequencerSegmentOffset(dwId: UInt32, hnsOffset: Int64, pvarSegmentOffset: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateAggregateSource(pSourceCollection: Windows.Win32.Media.MediaFoundation.IMFCollection_head, ppAggSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateCredentialCache(ppCache: POINTER(Windows.Win32.Media.MediaFoundation.IMFNetCredentialCache_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateProxyLocator(pszProtocol: Windows.Win32.Foundation.PWSTR, pProxyConfig: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppProxyLocator: POINTER(Windows.Win32.Media.MediaFoundation.IMFNetProxyLocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateNetSchemePlugin(riid: POINTER(Guid), ppvHandler: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreatePMPServer(dwCreationFlags: UInt32, ppPMPServer: POINTER(Windows.Win32.Media.MediaFoundation.IMFPMPServer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateRemoteDesktopPlugin(ppPlugin: POINTER(Windows.Win32.Media.MediaFoundation.IMFRemoteDesktopPlugin_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def CreateNamedPropertyStore(ppStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.INamedPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateSampleCopierMFT(ppCopierMFT: POINTER(Windows.Win32.Media.MediaFoundation.IMFTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateTranscodeProfile(ppTranscodeProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFTranscodeProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateTranscodeTopology(pSrc: Windows.Win32.Media.MediaFoundation.IMFMediaSource_head, pwszOutputFilePath: Windows.Win32.Foundation.PWSTR, pProfile: Windows.Win32.Media.MediaFoundation.IMFTranscodeProfile_head, ppTranscodeTopo: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopology_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateTranscodeTopologyFromByteStream(pSrc: Windows.Win32.Media.MediaFoundation.IMFMediaSource_head, pOutputStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pProfile: Windows.Win32.Media.MediaFoundation.IMFTranscodeProfile_head, ppTranscodeTopo: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopology_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFTranscodeGetAudioOutputAvailableTypes(guidSubType: POINTER(Guid), dwMFTFlags: UInt32, pCodecConfig: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppAvailableTypes: POINTER(Windows.Win32.Media.MediaFoundation.IMFCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateTranscodeSinkActivate(ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateTrackedSample(ppMFSample: POINTER(Windows.Win32.Media.MediaFoundation.IMFTrackedSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMFByteStreamOnStream(pStream: Windows.Win32.System.Com.IStream_head, ppByteStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateStreamOnMFByteStream(pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMFByteStreamOnStreamEx(punkStream: Windows.Win32.System.Com.IUnknown_head, ppByteStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateStreamOnMFByteStreamEx(pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMediaTypeFromProperties(punkStream: Windows.Win32.System.Com.IUnknown_head, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreatePropertiesFromMediaType(pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFEnumDeviceSources(pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pppSourceActivate: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)), pcSourceActivate: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateDeviceSource(pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateDeviceSourceActivate(pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateProtectedEnvironmentAccess(ppAccess: POINTER(Windows.Win32.Media.MediaFoundation.IMFProtectedEnvironmentAccess_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFLoadSignedLibrary(pszName: Windows.Win32.Foundation.PWSTR, ppLib: POINTER(Windows.Win32.Media.MediaFoundation.IMFSignedLibrary_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFGetSystemId(ppId: POINTER(Windows.Win32.Media.MediaFoundation.IMFSystemId_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFGetLocalId(verifier: POINTER(Byte), size: UInt32, id: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateContentProtectionDevice(ProtectionSystemId: POINTER(Guid), ContentProtectionDevice: POINTER(Windows.Win32.Media.MediaFoundation.IMFContentProtectionDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFIsContentProtectionDeviceSupported(ProtectionSystemId: POINTER(Guid), isSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateContentDecryptorContext(guidMediaProtectionSystemId: POINTER(Guid), pD3DManager: Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head, pContentProtectionDevice: Windows.Win32.Media.MediaFoundation.IMFContentProtectionDevice_head, ppContentDecryptorContext: POINTER(Windows.Win32.Media.MediaFoundation.IMFContentDecryptorContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateSensorGroup(SensorGroupSymbolicLink: Windows.Win32.Foundation.PWSTR, ppSensorGroup: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateSensorStream(StreamId: UInt32, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pMediaTypeCollection: Windows.Win32.Media.MediaFoundation.IMFCollection_head, ppStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateSensorProfile(ProfileType: POINTER(Guid), ProfileIndex: UInt32, Constraints: Windows.Win32.Foundation.PWSTR, ppProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateSensorProfileCollection(ppSensorProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorProfileCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateSensorActivityMonitor(pCallback: Windows.Win32.Media.MediaFoundation.IMFSensorActivitiesReportCallback_head, ppActivityMonitor: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorActivityMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFCORE.dll')
def MFCreateExtendedCameraIntrinsics(ppExtendedCameraIntrinsics: POINTER(Windows.Win32.Media.MediaFoundation.IMFExtendedCameraIntrinsics_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFCORE.dll')
def MFCreateExtendedCameraIntrinsicModel(distortionModelType: Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_DistortionModelType, ppExtendedCameraIntrinsicModel: POINTER(Windows.Win32.Media.MediaFoundation.IMFExtendedCameraIntrinsicModel_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateRelativePanelWatcher(videoDeviceId: Windows.Win32.Foundation.PWSTR, displayMonitorDeviceId: Windows.Win32.Foundation.PWSTR, ppRelativePanelWatcher: POINTER(Windows.Win32.Media.MediaFoundation.IMFRelativePanelWatcher_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateCameraOcclusionStateMonitor(symbolicLink: Windows.Win32.Foundation.PWSTR, callback: Windows.Win32.Media.MediaFoundation.IMFCameraOcclusionStateReportCallback_head, occlusionStateMonitor: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraOcclusionStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateCameraControlMonitor(symbolicLink: Windows.Win32.Foundation.PWSTR, callback: Windows.Win32.Media.MediaFoundation.IMFCameraControlNotify_head, ppCameraControlMonitor: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraControlMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFContentInfo(ppIContentInfo: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFIndexer(ppIIndexer: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFIndexer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFIndexerByteStream(pIContentByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, cbIndexStartOffset: UInt64, pIIndexByteStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFSplitter(ppISplitter: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFSplitter_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFProfile(ppIProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFProfileFromPresentationDescriptor(pIPD: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head, ppIProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreatePresentationDescriptorFromASFProfile(pIProfile: Windows.Win32.Media.MediaFoundation.IMFASFProfile_head, ppIPD: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFMultiplexer(ppIMultiplexer: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFMultiplexer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFStreamSelector(pIASFProfile: Windows.Win32.Media.MediaFoundation.IMFASFProfile_head, ppSelector: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamSelector_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFMediaSink(pIByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, ppIMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFMediaSinkActivate(pwszFileName: Windows.Win32.Foundation.PWSTR, pContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head, ppIActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateWMVEncoderActivate(pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pEncodingConfigurationProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateWMAEncoderActivate(pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pEncodingConfigurationProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFStreamingMediaSink(pIByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, ppIMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateASFStreamingMediaSinkActivate(pByteStreamActivate: Windows.Win32.Media.MediaFoundation.IMFActivate_head, pContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head, ppIActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateD3D12SynchronizationObject(pDevice: Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, riid: POINTER(Guid), ppvSyncObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFStartup(Version: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFShutdown() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFLockPlatform() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFUnlockPlatform() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFPutWorkItem(dwQueue: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFPutWorkItem2(dwQueue: UInt32, Priority: Int32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFPutWorkItemEx(dwQueue: UInt32, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFPutWorkItemEx2(dwQueue: UInt32, Priority: Int32, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFPutWaitingWorkItem(hEvent: Windows.Win32.Foundation.HANDLE, Priority: Int32, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pKey: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFAllocateSerialWorkQueue(dwWorkQueue: UInt32, pdwWorkQueue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFScheduleWorkItemEx(pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, Timeout: Int64, pKey: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFScheduleWorkItem(pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head, Timeout: Int64, pKey: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCancelWorkItem(Key: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetTimerPeriodicity(Periodicity: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFAddPeriodicCallback(Callback: Windows.Win32.Media.MediaFoundation.MFPERIODICCALLBACK, pContext: Windows.Win32.System.Com.IUnknown_head, pdwKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFRemovePeriodicCallback(dwKey: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFAllocateWorkQueueEx(WorkQueueType: Windows.Win32.Media.MediaFoundation.MFASYNC_WORKQUEUE_TYPE, pdwWorkQueue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFAllocateWorkQueue(pdwWorkQueue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFLockWorkQueue(dwWorkQueue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFUnlockWorkQueue(dwWorkQueue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFBeginRegisterWorkQueueWithMMCSS(dwWorkQueueId: UInt32, wszClass: Windows.Win32.Foundation.PWSTR, dwTaskId: UInt32, pDoneCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pDoneState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFBeginRegisterWorkQueueWithMMCSSEx(dwWorkQueueId: UInt32, wszClass: Windows.Win32.Foundation.PWSTR, dwTaskId: UInt32, lPriority: Int32, pDoneCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pDoneState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFEndRegisterWorkQueueWithMMCSS(pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pdwTaskId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFBeginUnregisterWorkQueueWithMMCSS(dwWorkQueueId: UInt32, pDoneCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pDoneState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFEndUnregisterWorkQueueWithMMCSS(pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetWorkQueueMMCSSClass(dwWorkQueueId: UInt32, pwszClass: Windows.Win32.Foundation.PWSTR, pcchClass: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetWorkQueueMMCSSTaskId(dwWorkQueueId: UInt32, pdwTaskId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFRegisterPlatformWithMMCSS(wszClass: Windows.Win32.Foundation.PWSTR, pdwTaskId: POINTER(UInt32), lPriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFUnregisterPlatformFromMMCSS() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFLockSharedWorkQueue(wszClass: Windows.Win32.Foundation.PWSTR, BasePriority: Int32, pdwTaskId: POINTER(UInt32), pID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetWorkQueueMMCSSPriority(dwWorkQueueId: UInt32, lPriority: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateAsyncResult(punkObject: Windows.Win32.System.Com.IUnknown_head, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head, ppAsyncResult: POINTER(Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInvokeCallback(pAsyncResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateFile(AccessMode: Windows.Win32.Media.MediaFoundation.MF_FILE_ACCESSMODE, OpenMode: Windows.Win32.Media.MediaFoundation.MF_FILE_OPENMODE, fFlags: Windows.Win32.Media.MediaFoundation.MF_FILE_FLAGS, pwszFileURL: Windows.Win32.Foundation.PWSTR, ppIByteStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateTempFile(AccessMode: Windows.Win32.Media.MediaFoundation.MF_FILE_ACCESSMODE, OpenMode: Windows.Win32.Media.MediaFoundation.MF_FILE_OPENMODE, fFlags: Windows.Win32.Media.MediaFoundation.MF_FILE_FLAGS, ppIByteStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFBeginCreateFile(AccessMode: Windows.Win32.Media.MediaFoundation.MF_FILE_ACCESSMODE, OpenMode: Windows.Win32.Media.MediaFoundation.MF_FILE_OPENMODE, fFlags: Windows.Win32.Media.MediaFoundation.MF_FILE_FLAGS, pwszFilePath: Windows.Win32.Foundation.PWSTR, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head, ppCancelCookie: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFEndCreateFile(pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, ppFile: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCancelCreateFile(pCancelCookie: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMemoryBuffer(cbMaxLength: UInt32, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMediaBufferWrapper(pBuffer: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head, cbOffset: UInt32, dwLength: UInt32, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateLegacyMediaBufferOnMFMediaBuffer(pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head, pMFMediaBuffer: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head, cbOffset: UInt32, ppMediaBuffer: POINTER(Windows.Win32.Media.DxMediaObjects.IMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFMapDX9FormatToDXGIFormat(dx9: UInt32) -> Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT: ...
@winfunctype('MFPlat.dll')
def MFMapDXGIFormatToDX9Format(dx11: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT) -> UInt32: ...
@winfunctype('MFPlat.dll')
def MFLockDXGIDeviceManager(pResetToken: POINTER(UInt32), ppManager: POINTER(Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFUnlockDXGIDeviceManager() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateDXSurfaceBuffer(riid: POINTER(Guid), punkSurface: Windows.Win32.System.Com.IUnknown_head, fBottomUpWhenLinear: Windows.Win32.Foundation.BOOL, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateWICBitmapBuffer(riid: POINTER(Guid), punkSurface: Windows.Win32.System.Com.IUnknown_head, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateDXGISurfaceBuffer(riid: POINTER(Guid), punkSurface: Windows.Win32.System.Com.IUnknown_head, uSubresourceIndex: UInt32, fBottomUpWhenLinear: Windows.Win32.Foundation.BOOL, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateVideoSampleAllocatorEx(riid: POINTER(Guid), ppSampleAllocator: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateDXGIDeviceManager(resetToken: POINTER(UInt32), ppDeviceManager: POINTER(Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateAlignedMemoryBuffer(cbMaxLength: UInt32, cbAligment: UInt32, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMediaEvent(met: UInt32, guidExtendedType: POINTER(Guid), hrStatus: Windows.Win32.Foundation.HRESULT, pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppEvent: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateEventQueue(ppMediaEventQueue: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaEventQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateSample(ppIMFSample: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateAttributes(ppMFAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head), cInitialSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitAttributesFromBlob(pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pBuf: POINTER(Byte), cbBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetAttributesAsBlobSize(pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pcbBufSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetAttributesAsBlob(pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pBuf: POINTER(Byte), cbBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTRegister(clsidMFT: Guid, guidCategory: Guid, pszName: Windows.Win32.Foundation.PWSTR, Flags: UInt32, cInputTypes: UInt32, pInputTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), cOutputTypes: UInt32, pOutputTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTUnregister(clsidMFT: Guid) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTRegisterLocal(pClassFactory: Windows.Win32.System.Com.IClassFactory_head, guidCategory: POINTER(Guid), pszName: Windows.Win32.Foundation.PWSTR, Flags: UInt32, cInputTypes: UInt32, pInputTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), cOutputTypes: UInt32, pOutputTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTUnregisterLocal(pClassFactory: Windows.Win32.System.Com.IClassFactory_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTRegisterLocalByCLSID(clisdMFT: POINTER(Guid), guidCategory: POINTER(Guid), pszName: Windows.Win32.Foundation.PWSTR, Flags: UInt32, cInputTypes: UInt32, pInputTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), cOutputTypes: UInt32, pOutputTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTUnregisterLocalByCLSID(clsidMFT: Guid) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTEnum(guidCategory: Guid, Flags: UInt32, pInputType: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), pOutputType: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppclsidMFT: POINTER(POINTER(Guid)), pcMFTs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTEnumEx(guidCategory: Guid, Flags: Windows.Win32.Media.MediaFoundation.MFT_ENUM_FLAG, pInputType: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), pOutputType: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), pppMFTActivate: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)), pnumMFTActivate: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTEnum2(guidCategory: Guid, Flags: Windows.Win32.Media.MediaFoundation.MFT_ENUM_FLAG, pInputType: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), pOutputType: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head), pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pppMFTActivate: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)), pnumMFTActivate: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFTGetInfo(clsidMFT: Guid, pszName: POINTER(Windows.Win32.Foundation.PWSTR), ppInputTypes: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head)), pcInputTypes: POINTER(UInt32), ppOutputTypes: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head)), pcOutputTypes: POINTER(UInt32), ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetPluginControl(ppPluginControl: POINTER(Windows.Win32.Media.MediaFoundation.IMFPluginControl_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetMFTMerit(pMFT: Windows.Win32.System.Com.IUnknown_head, cbVerifier: UInt32, verifier: POINTER(Byte), merit: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFRegisterLocalSchemeHandler(szScheme: Windows.Win32.Foundation.PWSTR, pActivate: Windows.Win32.Media.MediaFoundation.IMFActivate_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFRegisterLocalByteStreamHandler(szFileExtension: Windows.Win32.Foundation.PWSTR, szMimeType: Windows.Win32.Foundation.PWSTR, pActivate: Windows.Win32.Media.MediaFoundation.IMFActivate_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMFByteStreamWrapper(pStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, ppStreamWrapper: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMediaExtensionActivate(szActivatableClassId: Windows.Win32.Foundation.PWSTR, pConfiguration: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMuxStreamAttributes(pAttributesToMux: Windows.Win32.Media.MediaFoundation.IMFCollection_head, ppMuxAttribs: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMuxStreamMediaType(pMediaTypesToMux: Windows.Win32.Media.MediaFoundation.IMFCollection_head, ppMuxMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMuxStreamSample(pSamplesToMux: Windows.Win32.Media.MediaFoundation.IMFCollection_head, ppMuxSample: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFValidateMediaTypeSize(FormatType: Guid, pBlock: POINTER(Byte), cbSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMediaType(ppMFType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMFVideoFormatFromMFMediaType(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppMFVF: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head)), pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateWaveFormatExFromMFMediaType(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppWF: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)), pcbSize: POINTER(UInt32), Flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitMediaTypeFromVideoInfoHeader(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pVIH: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head), cbBufSize: UInt32, pSubtype: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitMediaTypeFromVideoInfoHeader2(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pVIH2: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER2_head), cbBufSize: UInt32, pSubtype: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitMediaTypeFromMPEG1VideoInfo(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pMP1VI: POINTER(Windows.Win32.Media.MediaFoundation.MPEG1VIDEOINFO_head), cbBufSize: UInt32, pSubtype: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitMediaTypeFromMPEG2VideoInfo(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pMP2VI: POINTER(Windows.Win32.Media.MediaFoundation.MPEG2VIDEOINFO_head), cbBufSize: UInt32, pSubtype: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCalculateBitmapImageSize(pBMIH: POINTER(Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER_head), cbBufSize: UInt32, pcbImageSize: POINTER(UInt32), pbKnown: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCalculateImageSize(guidSubtype: POINTER(Guid), unWidth: UInt32, unHeight: UInt32, pcbImageSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFFrameRateToAverageTimePerFrame(unNumerator: UInt32, unDenominator: UInt32, punAverageTimePerFrame: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFAverageTimePerFrameToFrameRate(unAverageTimePerFrame: UInt64, punNumerator: POINTER(UInt32), punDenominator: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitMediaTypeFromMFVideoFormat(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pMFVF: POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head), cbBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitMediaTypeFromWaveFormatEx(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pWaveFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), cbBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitMediaTypeFromAMMediaType(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pAMType: POINTER(Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitAMMediaTypeFromMFMediaType(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, guidFormatBlockType: Guid, pAMType: POINTER(Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateAMMediaTypeFromMFMediaType(pMFType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, guidFormatBlockType: Guid, ppAMType: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.AM_MEDIA_TYPE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCompareFullToPartialMediaType(pMFTypeFull: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pMFTypePartial: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MFPlat.dll')
def MFWrapMediaType(pOrig: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, MajorType: POINTER(Guid), SubType: POINTER(Guid), ppWrap: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFUnwrapMediaType(pWrap: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppOrig: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateVideoMediaType(pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head), ppIVideoMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFVideoMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateVideoMediaTypeFromSubtype(pAMSubtype: POINTER(Guid), ppIVideoMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFVideoMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('EVR.dll')
def MFIsFormatYUV(Format: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MFPlat.dll')
def MFCreateVideoMediaTypeFromBitMapInfoHeader(pbmihBitMapInfoHeader: POINTER(Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER_head), dwPixelAspectRatioX: UInt32, dwPixelAspectRatioY: UInt32, InterlaceMode: Windows.Win32.Media.MediaFoundation.MFVideoInterlaceMode, VideoFlags: UInt64, qwFramesPerSecondNumerator: UInt64, qwFramesPerSecondDenominator: UInt64, dwMaxBitRate: UInt32, ppIVideoMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFVideoMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetStrideForBitmapInfoHeader(format: UInt32, dwWidth: UInt32, pStride: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('EVR.dll')
def MFGetPlaneSize(format: UInt32, dwWidth: UInt32, dwHeight: UInt32, pdwPlaneSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateVideoMediaTypeFromBitMapInfoHeaderEx(pbmihBitMapInfoHeader: POINTER(Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER_head), cbBitMapInfoHeader: UInt32, dwPixelAspectRatioX: UInt32, dwPixelAspectRatioY: UInt32, InterlaceMode: Windows.Win32.Media.MediaFoundation.MFVideoInterlaceMode, VideoFlags: UInt64, dwFramesPerSecondNumerator: UInt32, dwFramesPerSecondDenominator: UInt32, dwMaxBitRate: UInt32, ppIVideoMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFVideoMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMediaTypeFromRepresentation(guidRepresentation: Guid, pvRepresentation: c_void_p, ppIMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateAudioMediaType(pAudioFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), ppIAudioMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFAudioMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFGetUncompressedVideoFormat(pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head)) -> UInt32: ...
@winfunctype('MFPlat.dll')
def MFInitVideoFormat(pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head), type: Windows.Win32.Media.MediaFoundation.MFStandardVideoFormat) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFInitVideoFormat_RGB(pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head), dwWidth: UInt32, dwHeight: UInt32, D3Dfmt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFConvertColorInfoToDXVA(pdwToDXVA: POINTER(UInt32), pFromFormat: POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFConvertColorInfoFromDXVA(pToFormat: POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head), dwFromDXVA: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCopyImage(pDest: POINTER(Byte), lDestStride: Int32, pSrc: POINTER(Byte), lSrcStride: Int32, dwWidthInBytes: UInt32, dwLines: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFConvertFromFP16Array(pDest: POINTER(Single), pSrc: POINTER(UInt16), dwCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFConvertToFP16Array(pDest: POINTER(UInt16), pSrc: POINTER(Single), dwCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreate2DMediaBuffer(dwWidth: UInt32, dwHeight: UInt32, dwFourCC: UInt32, fBottomUp: Windows.Win32.Foundation.BOOL, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateMediaBufferFromMediaType(pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, llDuration: Int64, dwMinLength: UInt32, dwMinAlignment: UInt32, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCreateCollection(ppIMFCollection: POINTER(Windows.Win32.Media.MediaFoundation.IMFCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFHeapAlloc(nSize: UIntPtr, dwFlags: UInt32, pszFile: Windows.Win32.Foundation.PSTR, line: Int32, eat: Windows.Win32.Media.MediaFoundation.EAllocationType) -> c_void_p: ...
@winfunctype('MFPlat.dll')
def MFHeapFree(pv: c_void_p) -> Void: ...
@winfunctype('MFPlat.dll')
def MFllMulDiv(a: Int64, b: Int64, c: Int64, d: Int64) -> Int64: ...
@winfunctype('MFPlat.dll')
def MFGetContentProtectionSystemCLSID(guidProtectionSystemID: POINTER(Guid), pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFCombineSamples(pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head, pSampleToAdd: Windows.Win32.Media.MediaFoundation.IMFSample_head, dwMaxMergedDurationInMS: UInt32, pMerged: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlat.dll')
def MFSplitSample(pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head, pOutputSamples: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head), dwOutputSampleMaxCount: UInt32, pdwOutputSampleCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFReadWrite.dll')
def MFCreateSourceReaderFromURL(pwszURL: Windows.Win32.Foundation.PWSTR, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppSourceReader: POINTER(Windows.Win32.Media.MediaFoundation.IMFSourceReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFReadWrite.dll')
def MFCreateSourceReaderFromByteStream(pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppSourceReader: POINTER(Windows.Win32.Media.MediaFoundation.IMFSourceReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFReadWrite.dll')
def MFCreateSourceReaderFromMediaSource(pMediaSource: Windows.Win32.Media.MediaFoundation.IMFMediaSource_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppSourceReader: POINTER(Windows.Win32.Media.MediaFoundation.IMFSourceReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFReadWrite.dll')
def MFCreateSinkWriterFromURL(pwszOutputURL: Windows.Win32.Foundation.PWSTR, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppSinkWriter: POINTER(Windows.Win32.Media.MediaFoundation.IMFSinkWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFReadWrite.dll')
def MFCreateSinkWriterFromMediaSink(pMediaSink: Windows.Win32.Media.MediaFoundation.IMFMediaSink_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppSinkWriter: POINTER(Windows.Win32.Media.MediaFoundation.IMFSinkWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('EVR.dll')
def MFCreateVideoPresenter(pOwner: Windows.Win32.System.Com.IUnknown_head, riidDevice: POINTER(Guid), riid: POINTER(Guid), ppVideoPresenter: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('EVR.dll')
def MFCreateVideoMixer(pOwner: Windows.Win32.System.Com.IUnknown_head, riidDevice: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('EVR.dll')
def MFCreateVideoMixerAndPresenter(pMixerOwner: Windows.Win32.System.Com.IUnknown_head, pPresenterOwner: Windows.Win32.System.Com.IUnknown_head, riidMixer: POINTER(Guid), ppvVideoMixer: POINTER(c_void_p), riidPresenter: POINTER(Guid), ppvVideoPresenter: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateVideoRenderer(riidRenderer: POINTER(Guid), ppVideoRenderer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('EVR.dll')
def MFCreateVideoSampleFromSurface(pUnkSurface: Windows.Win32.System.Com.IUnknown_head, ppSample: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('EVR.dll')
def MFCreateVideoSampleAllocator(riid: POINTER(Guid), ppSampleAllocator: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFPlay.dll')
def MFPCreateMediaPlayer(pwszURL: Windows.Win32.Foundation.PWSTR, fStartPlayback: Windows.Win32.Foundation.BOOL, creationOptions: Windows.Win32.Media.MediaFoundation.MFP_CREATION_OPTIONS, pCallback: Windows.Win32.Media.MediaFoundation.IMFPMediaPlayerCallback_head, hWnd: Windows.Win32.Foundation.HWND, ppMediaPlayer: POINTER(Windows.Win32.Media.MediaFoundation.IMFPMediaPlayer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MF.dll')
def MFCreateEncryptedMediaExtensionsStoreActivate(pmpHost: Windows.Win32.Media.MediaFoundation.IMFPMPHostApp_head, objectStream: Windows.Win32.System.Com.IStream_head, classId: Windows.Win32.Foundation.PWSTR, activate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFCreateVirtualCamera(type: Windows.Win32.Media.MediaFoundation.MFVirtualCameraType, lifetime: Windows.Win32.Media.MediaFoundation.MFVirtualCameraLifetime, access: Windows.Win32.Media.MediaFoundation.MFVirtualCameraAccess, friendlyName: Windows.Win32.Foundation.PWSTR, sourceId: Windows.Win32.Foundation.PWSTR, categories: POINTER(Guid), categoryCount: UInt32, virtualCamera: POINTER(Windows.Win32.Media.MediaFoundation.IMFVirtualCamera_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MFSENSORGROUP.dll')
def MFIsVirtualCameraTypeSupported(type: Windows.Win32.Media.MediaFoundation.MFVirtualCameraType, supported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OPMXbox.dll')
def OPMXboxEnableHDCP(HDCPType: Windows.Win32.Media.MediaFoundation.OPM_HDCP_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OPMXbox.dll')
def OPMXboxGetHDCPStatus(pHDCPStatus: POINTER(Windows.Win32.Media.MediaFoundation.OPM_HDCP_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OPMXbox.dll')
def OPMXboxGetHDCPStatusAndType(pHDCPStatus: POINTER(Windows.Win32.Media.MediaFoundation.OPM_HDCP_STATUS), pHDCPType: POINTER(Windows.Win32.Media.MediaFoundation.OPM_HDCP_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
CAC3DecMediaObject = Guid('{03d7c802-ecfa-47d9-b268-5fb3e310dee4}')
CClusterDetectorDmo = Guid('{36e820c4-165a-4521-863c-619e1160d4d4}')
CColorControlDmo = Guid('{798059f0-89ca-4160-b325-aeb48efe4f9a}')
CColorConvertDMO = Guid('{98230571-0087-4204-b020-3282538e57d3}')
CColorLegalizerDmo = Guid('{fdfaa753-e48e-4e33-9c74-98a27fc6726a}')
CDTVAudDecoderDS = Guid('{8e269032-fe03-4753-9b17-18253c21722e}')
CDTVVidDecoderDS = Guid('{64777dc8-4e24-4beb-9d19-60a35be1daaf}')
CDVDecoderMediaObject = Guid('{e54709c5-1e17-4c8d-94e7-478940433584}')
CDVEncoderMediaObject = Guid('{c82ae729-c327-4cce-914d-8171fefebefb}')
CDeColorConvMediaObject = Guid('{49034c05-f43c-400f-84c1-90a683195a3a}')
CFrameInterpDMO = Guid('{0a7cfe1b-6ab5-4334-9ed8-3f97cb37daa1}')
CFrameRateConvertDmo = Guid('{01f36ce2-0907-4d8b-979d-f151be91c883}')
CInterlaceMediaObject = Guid('{b5a89c80-4901-407b-9abc-90d9a644bb46}')
CMP3DecMediaObject = Guid('{bbeea841-0a63-4f52-a7ab-a9b3a84ed38a}')
CMPEG2AudDecoderDS = Guid('{e1f1a0b8-beee-490d-ba7c-066c40b5e2b9}')
CMPEG2AudioEncoderMFT = Guid('{46a4dd5c-73f8-4304-94df-308f760974f4}')
CMPEG2EncoderAudioDS = Guid('{acd453bc-c58a-44d1-bbf5-bfb325be2d78}')
CMPEG2EncoderDS = Guid('{5f5aff4a-2f7f-4279-88c2-cd88eb39d144}')
CMPEG2EncoderVideoDS = Guid('{42150cd9-ca9a-4ea5-9939-30ee037f6e74}')
CMPEG2VidDecoderDS = Guid('{212690fb-83e5-4526-8fd7-74478b7939cd}')
CMPEG2VideoEncoderMFT = Guid('{e6335f02-80b7-4dc4-adfa-dfe7210d20d5}')
CMPEGAACDecMediaObject = Guid('{8dde1772-edad-41c3-b4be-1f30fb4ee0d6}')
CMSAACDecMFT = Guid('{32d186a7-218f-4c75-8876-dd77273a8999}')
CMSAC3Enc = Guid('{c6b400e2-20a7-4e58-a2fe-24619682ce6c}')
CMSALACDecMFT = Guid('{c0cd7d12-31fc-4bbc-b363-7322ee3e1879}')
CMSALACEncMFT = Guid('{9ab6a28c-748e-4b6a-bfff-cc443b8e8fb4}')
CMSDDPlusDecMFT = Guid('{177c0afe-900b-48d4-9e4c-57add250b3d4}')
CMSDolbyDigitalEncMFT = Guid('{ac3315c9-f481-45d7-826c-0b406c1f64b8}')
CMSFLACDecMFT = Guid('{6b0b3e6b-a2c5-4514-8055-afe8a95242d9}')
CMSFLACEncMFT = Guid('{128509e9-c44e-45dc-95e9-c255b8f466a6}')
CMSH263EncoderMFT = Guid('{bc47fcfe-98a0-4f27-bb07-698af24f2b38}')
CMSH264DecoderMFT = Guid('{62ce7e72-4c71-4d20-b15d-452831a87d9d}')
CMSH264EncoderMFT = Guid('{6ca50344-051a-4ded-9779-a43305165e35}')
CMSH264RemuxMFT = Guid('{05a47ebb-8bf0-4cbf-ad2f-3b71d75866f5}')
CMSH265EncoderMFT = Guid('{f2f84074-8bca-40bd-9159-e880f673dd3b}')
CMSMPEGAudDecMFT = Guid('{70707b39-b2ca-4015-abea-f8447d22d88b}')
CMSMPEGDecoderMFT = Guid('{2d709e52-123f-49b5-9cbc-9af5cde28fb9}')
CMSOpusDecMFT = Guid('{63e17c10-2d43-4c42-8fe3-8d8b63e46a6a}')
CMSSCDecMediaObject = Guid('{7bafb3b1-d8f4-4279-9253-27da423108de}')
CMSSCEncMediaObject = Guid('{8cb9cc06-d139-4ae6-8bb4-41e612e141d5}')
CMSSCEncMediaObject2 = Guid('{f7ffe0a0-a4f5-44b5-949e-15ed2bc66f9d}')
CMSVPXEncoderMFT = Guid('{aeb6c755-2546-4881-82cc-e15ae5ebff3d}')
CMSVideoDSPMFT = Guid('{51571744-7fe4-4ff2-a498-2dc34ff74f1b}')
CMpeg2DecMediaObject = Guid('{863d66cd-cdce-4617-b47f-c8929cfc28a6}')
CMpeg43DecMediaObject = Guid('{cba9e78b-49a3-49ea-93d4-6bcba8c4de07}')
CMpeg4DecMediaObject = Guid('{f371728a-6052-4d47-827c-d039335dfe0a}')
CMpeg4EncMediaObject = Guid('{24f258d8-c651-4042-93e4-ca654abb682c}')
CMpeg4sDecMFT = Guid('{5686a0d9-fe39-409f-9dff-3fdbc849f9f5}')
CMpeg4sDecMediaObject = Guid('{2a11bae2-fe6e-4249-864b-9e9ed6e8dbc2}')
CMpeg4sEncMediaObject = Guid('{6ec5a7be-d81e-4f9e-ada3-cd1bf262b6d8}')
CNokiaAACCCDecMediaObject = Guid('{eabf7a6f-ccba-4d60-8620-b152cc977263}')
CNokiaAACDecMediaObject = Guid('{3cb2bde4-4e29-4c44-a73e-2d7c2c46d6ec}')
CODECAPI_AVAudioChannelConfig = Guid('{17f89cb3-c38d-4368-9ede-63b94d177f9f}')
CODECAPI_AVAudioChannelCount = Guid('{1d3583c4-1583-474e-b71a-5ee463c198e4}')
CODECAPI_AVAudioSampleRate = Guid('{971d2723-1acb-42e7-855c-520a4b70a5f2}')
CODECAPI_AVDDSurroundMode = Guid('{99f2f386-98d1-4452-a163-abc78a6eb770}')
CODECAPI_AVDSPLoudnessEqualization = Guid('{8afd1a15-1812-4cbf-9319-433a5b2a3b27}')
CODECAPI_AVDSPSpeakerFill = Guid('{5612bca1-56da-4582-8da1-ca8090f92768}')
CODECAPI_AVDecAACDownmixMode = Guid('{01274475-f6bb-4017-b084-81a763c942d4}')
CODECAPI_AVDecAudioDualMono = Guid('{4a52cda8-30f8-4216-be0f-ba0b2025921d}')
CODECAPI_AVDecAudioDualMonoReproMode = Guid('{a5106186-cc94-4bc9-8cd9-aa2f61f6807e}')
CODECAPI_AVDecCommonInputFormat = Guid('{e5005239-bd89-4be3-9c0f-5dde317988cc}')
CODECAPI_AVDecCommonMeanBitRate = Guid('{59488217-007a-4f7a-8e41-5c48b1eac5c6}')
CODECAPI_AVDecCommonMeanBitRateInterval = Guid('{0ee437c6-38a7-4c5c-944c-68ab42116b85}')
CODECAPI_AVDecCommonOutputFormat = Guid('{3c790028-c0ce-4256-b1a2-1b0fc8b1dcdc}')
CODECAPI_AVDecDDDynamicRangeScaleHigh = Guid('{50196c21-1f33-4af5-b296-11426d6c8789}')
CODECAPI_AVDecDDDynamicRangeScaleLow = Guid('{044e62e4-11a5-42d5-a3b2-3bb2c7c2d7cf}')
CODECAPI_AVDecDDMatrixDecodingMode = Guid('{ddc811a5-04ed-4bf3-a0ca-d00449f9355f}')
CODECAPI_AVDecDDOperationalMode = Guid('{d6d6c6d1-064e-4fdd-a40e-3ecbfcb7ebd0}')
CODECAPI_AVDecDDStereoDownMixMode = Guid('{6ce4122c-3ee9-4182-b4ae-c10fc088649d}')
CODECAPI_AVDecDisableVideoPostProcessing = Guid('{f8749193-667a-4f2c-a9e8-5d4af924f08f}')
CODECAPI_AVDecHEAACDynamicRangeControl = Guid('{287c8abe-69a4-4d39-8080-d3d9712178a0}')
CODECAPI_AVDecNumWorkerThreads = Guid('{9561c3e8-ea9e-4435-9b1e-a93e691894d8}')
CODECAPI_AVDecSoftwareDynamicFormatChange = Guid('{862e2f0a-507b-47ff-af47-01e2624298b7}')
CODECAPI_AVDecVideoAcceleration_H264 = Guid('{f7db8a2f-4f48-4ee8-ae31-8b6ebe558ae2}')
CODECAPI_AVDecVideoAcceleration_MPEG2 = Guid('{f7db8a2e-4f48-4ee8-ae31-8b6ebe558ae2}')
CODECAPI_AVDecVideoAcceleration_VC1 = Guid('{f7db8a30-4f48-4ee8-ae31-8b6ebe558ae2}')
CODECAPI_AVDecVideoCodecType = Guid('{434528e5-21f0-46b6-b62c-9b1b6b658cd1}')
CODECAPI_AVDecVideoDXVABusEncryption = Guid('{42153c8b-fd0b-4765-a462-ddd9e8bcc388}')
CODECAPI_AVDecVideoDXVAMode = Guid('{f758f09e-7337-4ae7-8387-73dc2d54e67d}')
CODECAPI_AVDecVideoDropPicWithMissingRef = Guid('{f8226383-14c2-4567-9734-5004e96ff887}')
CODECAPI_AVDecVideoFastDecodeMode = Guid('{6b529f7d-d3b1-49c6-a999-9ec6911bedbf}')
CODECAPI_AVDecVideoH264ErrorConcealment = Guid('{ececace8-3436-462c-9294-cd7bacd758a9}')
CODECAPI_AVDecVideoImageSize = Guid('{5ee5747c-6801-4cab-aaf1-6248fa841ba4}')
CODECAPI_AVDecVideoInputScanType = Guid('{38477e1f-0ea7-42cd-8cd1-130ced57c580}')
CODECAPI_AVDecVideoMPEG2ErrorConcealment = Guid('{9d2bfe18-728d-48d2-b358-bc7e436c6674}')
CODECAPI_AVDecVideoMaxCodedHeight = Guid('{7262a16a-d2dc-4e75-9ba8-65c0c6d32b13}')
CODECAPI_AVDecVideoMaxCodedWidth = Guid('{5ae557b8-77af-41f5-9fa6-4db2fe1d4bca}')
CODECAPI_AVDecVideoPixelAspectRatio = Guid('{b0cf8245-f32d-41df-b02c-87bd304d12ab}')
CODECAPI_AVDecVideoProcDeinterlaceCSC = Guid('{f7db8a31-4f48-4ee8-ae31-8b6ebe558ae2}')
CODECAPI_AVDecVideoSWPowerLevel = Guid('{fb5d2347-4dd8-4509-aed0-db5fa9aa93f4}')
CODECAPI_AVDecVideoSoftwareDeinterlaceMode = Guid('{0c08d1ce-9ced-4540-bae3-ceb380141109}')
CODECAPI_AVDecVideoThumbnailGenerationMode = Guid('{2efd8eee-1150-4328-9cf5-66dce933fcf4}')
CODECAPI_AVEnableInLoopDeblockFilter = Guid('{d2e8e399-0623-4bf3-92a8-4d1818529ded}')
CODECAPI_AVEncAACEnableVBR = Guid('{e836bb98-fca3-44b6-9a39-24786be41be1}')
CODECAPI_AVEncAdaptiveMode = Guid('{4419b185-da1f-4f53-bc76-097d0c1efb1e}')
CODECAPI_AVEncAudioDualMono = Guid('{3648126b-a3e8-4329-9b3a-5ce566a43bd3}')
CODECAPI_AVEncAudioInputContent = Guid('{3e226c2b-60b9-4a39-b00b-a7b40f70d566}')
CODECAPI_AVEncAudioIntervalToEncode = Guid('{866e4b4d-725a-467c-bb01-b496b23b25f9}')
CODECAPI_AVEncAudioIntervalToSkip = Guid('{88c15f94-c38c-4796-a9e8-96e967983f26}')
CODECAPI_AVEncAudioMapDestChannel0 = Guid('{bc5d0b60-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel1 = Guid('{bc5d0b61-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel10 = Guid('{bc5d0b6a-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel11 = Guid('{bc5d0b6b-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel12 = Guid('{bc5d0b6c-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel13 = Guid('{bc5d0b6d-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel14 = Guid('{bc5d0b6e-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel15 = Guid('{bc5d0b6f-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel2 = Guid('{bc5d0b62-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel3 = Guid('{bc5d0b63-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel4 = Guid('{bc5d0b64-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel5 = Guid('{bc5d0b65-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel6 = Guid('{bc5d0b66-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel7 = Guid('{bc5d0b67-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel8 = Guid('{bc5d0b68-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMapDestChannel9 = Guid('{bc5d0b69-df6a-4e16-9803-b82007a30c8d}')
CODECAPI_AVEncAudioMeanBitRate = Guid('{921295bb-4fca-4679-aab8-9e2a1d753384}')
CODECAPI_AVEncChromaEncodeMode = Guid('{8a47ab5a-4798-4c93-b5a5-554f9a3b9f50}')
CODECAPI_AVEncChromaUpdateTime = Guid('{4b4fd998-4274-40bb-8ee4-07553e7e2d3a}')
CODECAPI_AVEncCodecType = Guid('{08af4ac1-f3f2-4c74-9dcf-37f2ec79f826}')
CODECAPI_AVEncCommonAllowFrameDrops = Guid('{d8477dcb-9598-48e3-8d0c-752bf206093e}')
CODECAPI_AVEncCommonBufferInLevel = Guid('{d9c5c8db-fc74-4064-94e9-cd19f947ed45}')
CODECAPI_AVEncCommonBufferOutLevel = Guid('{ccae7f49-d0bc-4e3d-a57e-fb5740140069}')
CODECAPI_AVEncCommonBufferSize = Guid('{0db96574-b6a4-4c8b-8106-3773de0310cd}')
CODECAPI_AVEncCommonFormatConstraint = Guid('{57cbb9b8-116f-4951-b40c-c2a035ed8f17}')
CODECAPI_AVEncCommonLowLatency = Guid('{9d3ecd55-89e8-490a-970a-0c9548d5a56e}')
CODECAPI_AVEncCommonMaxBitRate = Guid('{9651eae4-39b9-4ebf-85ef-d7f444ec7465}')
CODECAPI_AVEncCommonMeanBitRate = Guid('{f7222374-2144-4815-b550-a37f8e12ee52}')
CODECAPI_AVEncCommonMeanBitRateInterval = Guid('{bfaa2f0c-cb82-4bc0-8474-f06a8a0d0258}')
CODECAPI_AVEncCommonMinBitRate = Guid('{101405b2-2083-4034-a806-efbeddd7c9ff}')
CODECAPI_AVEncCommonMultipassMode = Guid('{22533d4c-47e1-41b5-9352-a2b7780e7ac4}')
CODECAPI_AVEncCommonPassEnd = Guid('{0e3d01bc-c85c-467d-8b60-c41012ee3bf6}')
CODECAPI_AVEncCommonPassStart = Guid('{6a67739f-4eb5-4385-9928-f276a939ef95}')
CODECAPI_AVEncCommonQuality = Guid('{fcbf57a3-7ea5-4b0c-9644-69b40c39c391}')
CODECAPI_AVEncCommonQualityVsSpeed = Guid('{98332df8-03cd-476b-89fa-3f9e442dec9f}')
CODECAPI_AVEncCommonRateControlMode = Guid('{1c0608e9-370c-4710-8a58-cb6181c42423}')
CODECAPI_AVEncCommonRealTime = Guid('{143a0ff6-a131-43da-b81e-98fbb8ec378e}')
CODECAPI_AVEncCommonStreamEndHandling = Guid('{6aad30af-6ba8-4ccc-8fca-18d19beaeb1c}')
CODECAPI_AVEncCommonTranscodeEncodingProfile = Guid('{6947787c-f508-4ea9-b1e9-a1fe3a49fbc9}')
CODECAPI_AVEncDDAtoDConverterType = Guid('{719f9612-81a1-47e0-9a05-d94ad5fca948}')
CODECAPI_AVEncDDCentreDownMixLevel = Guid('{e285072c-c958-4a81-afd2-e5e0daf1b148}')
CODECAPI_AVEncDDChannelBWLowPassFilter = Guid('{e197821d-d2e7-43e2-ad2c-00582f518545}')
CODECAPI_AVEncDDCopyright = Guid('{8694f076-cd75-481d-a5c6-a904dcc828f0}')
CODECAPI_AVEncDDDCHighPassFilter = Guid('{9565239f-861c-4ac8-bfda-e00cb4db8548}')
CODECAPI_AVEncDDDialogNormalization = Guid('{d7055acf-f125-437d-a704-79c79f0404a8}')
CODECAPI_AVEncDDDigitalDeemphasis = Guid('{e024a2c2-947c-45ac-87d8-f1030c5c0082}')
CODECAPI_AVEncDDDynamicRangeCompressionControl = Guid('{cfc2ff6d-79b8-4b8d-a8aa-a0c9bd1c2940}')
CODECAPI_AVEncDDHeadphoneMode = Guid('{4052dbec-52f5-42f5-9b00-d134b1341b9d}')
CODECAPI_AVEncDDLFELowPassFilter = Guid('{d3b80f6f-9d15-45e5-91be-019c3fab1f01}')
CODECAPI_AVEncDDLoRoCenterMixLvl_x10 = Guid('{1cfba222-25b3-4bf4-9bfd-e7111267858c}')
CODECAPI_AVEncDDLoRoSurroundMixLvl_x10 = Guid('{e725cff6-eb56-40c7-8450-2b9367e91555}')
CODECAPI_AVEncDDLtRtCenterMixLvl_x10 = Guid('{dca128a2-491f-4600-b2da-76e3344b4197}')
CODECAPI_AVEncDDLtRtSurroundMixLvl_x10 = Guid('{212246c7-3d2c-4dfa-bc21-652a9098690d}')
CODECAPI_AVEncDDOriginalBitstream = Guid('{966ae800-5bd3-4ff9-95b9-d30566273856}')
CODECAPI_AVEncDDPreferredStereoDownMixMode = Guid('{7f4e6b31-9185-403d-b0a2-763743e6f063}')
CODECAPI_AVEncDDProductionInfoExists = Guid('{b0b7fe5f-b6ab-4f40-964d-8d91f17c19e8}')
CODECAPI_AVEncDDProductionMixLevel = Guid('{301d103a-cbf9-4776-8899-7c15b461ab26}')
CODECAPI_AVEncDDProductionRoomType = Guid('{dad7ad60-23d8-4ab7-a284-556986d8a6fe}')
CODECAPI_AVEncDDRFPreEmphasisFilter = Guid('{21af44c0-244e-4f3d-a2cc-3d3068b2e73f}')
CODECAPI_AVEncDDService = Guid('{d2e1bec7-5172-4d2a-a50e-2f3b82b1ddf8}')
CODECAPI_AVEncDDSurround3dBAttenuation = Guid('{4d43b99d-31e2-48b9-bf2e-5cbf1a572784}')
CODECAPI_AVEncDDSurround90DegreeePhaseShift = Guid('{25ecec9d-3553-42c0-bb56-d25792104f80}')
CODECAPI_AVEncDDSurroundDownMixLevel = Guid('{7b20d6e5-0bcf-4273-a487-506b047997e9}')
CODECAPI_AVEncDDSurroundExMode = Guid('{91607cee-dbdd-4eb6-bca2-aadfafa3dd68}')
CODECAPI_AVEncEnableVideoProcessing = Guid('{006f4bf6-0ea3-4d42-8702-b5d8be0f7a92}')
CODECAPI_AVEncH264CABACEnable = Guid('{ee6cad62-d305-4248-a50e-e1b255f7caf8}')
CODECAPI_AVEncH264PPSID = Guid('{bfe29ec2-056c-4d68-a38d-ae5944c8582e}')
CODECAPI_AVEncH264SPSID = Guid('{50f38f51-2b79-40e3-b39c-7e9fa0770501}')
CODECAPI_AVEncInputVideoSystem = Guid('{bede146d-b616-4dc7-92b2-f5d9fa9298f7}')
CODECAPI_AVEncLowPowerEncoder = Guid('{b668d582-8bad-4f6a-9141-375a95358b6d}')
CODECAPI_AVEncMP12MuxDVDNavPacks = Guid('{c7607ced-8cf1-4a99-83a1-ee5461be3574}')
CODECAPI_AVEncMP12MuxEarliestPTS = Guid('{157232b6-f809-474e-9464-a7f93014a817}')
CODECAPI_AVEncMP12MuxInitialSCR = Guid('{3433ad21-1b91-4a0b-b190-2b77063b63a4}')
CODECAPI_AVEncMP12MuxLargestPacketSize = Guid('{35ceb711-f461-4b92-a4ef-17b6841ed254}')
CODECAPI_AVEncMP12MuxMuxRate = Guid('{ee047c72-4bdb-4a9d-8e21-41926c823da7}')
CODECAPI_AVEncMP12MuxNumStreams = Guid('{f7164a41-dced-4659-a8f2-fb693f2a4cd0}')
CODECAPI_AVEncMP12MuxPackSize = Guid('{f916053a-1ce8-4faf-aa0b-ba31c80034b8}')
CODECAPI_AVEncMP12MuxPacketOverhead = Guid('{e40bd720-3955-4453-acf9-b79132a38fa0}')
CODECAPI_AVEncMP12MuxSysAudioLock = Guid('{0fbb5752-1d43-47bf-bd79-f2293d8ce337}')
CODECAPI_AVEncMP12MuxSysCSPS = Guid('{7952ff45-9c0d-4822-bc82-8ad772e02993}')
CODECAPI_AVEncMP12MuxSysFixed = Guid('{cefb987e-894f-452e-8f89-a4ef8cec063a}')
CODECAPI_AVEncMP12MuxSysRateBound = Guid('{05f0428a-ee30-489d-ae28-205c72446710}')
CODECAPI_AVEncMP12MuxSysSTDBufferBound = Guid('{35746903-b545-43e7-bb35-c5e0a7d5093c}')
CODECAPI_AVEncMP12MuxSysVideoLock = Guid('{b8296408-2430-4d37-a2a1-95b3e435a91d}')
CODECAPI_AVEncMP12MuxTargetPacketizer = Guid('{d862212a-2015-45dd-9a32-1b3aa88205a0}')
CODECAPI_AVEncMP12PktzCopyright = Guid('{c8f4b0c1-094c-43c7-8e68-a595405a6ef8}')
CODECAPI_AVEncMP12PktzInitialPTS = Guid('{2a4f2065-9a63-4d20-ae22-0a1bc896a315}')
CODECAPI_AVEncMP12PktzOriginal = Guid('{6b178416-31b9-4964-94cb-6bff866cdf83}')
CODECAPI_AVEncMP12PktzPacketSize = Guid('{ab71347a-1332-4dde-a0e5-ccf7da8a0f22}')
CODECAPI_AVEncMP12PktzSTDBuffer = Guid('{0b751bd0-819e-478c-9435-75208926b377}')
CODECAPI_AVEncMP12PktzStreamID = Guid('{c834d038-f5e8-4408-9b60-88f36493fedf}')
CODECAPI_AVEncMPACodingMode = Guid('{b16ade03-4b93-43d7-a550-90b4fe224537}')
CODECAPI_AVEncMPACopyright = Guid('{a6ae762a-d0a9-4454-b8ef-f2dbeefdd3bd}')
CODECAPI_AVEncMPAEmphasisType = Guid('{2d59fcda-bf4e-4ed6-b5df-5b03b36b0a1f}')
CODECAPI_AVEncMPAEnableRedundancyProtection = Guid('{5e54b09e-b2e7-4973-a89b-0b3650a3beda}')
CODECAPI_AVEncMPALayer = Guid('{9d377230-f91b-453d-9ce0-78445414c22d}')
CODECAPI_AVEncMPAOriginalBitstream = Guid('{3cfb7855-9cc9-47ff-b829-b36786c92346}')
CODECAPI_AVEncMPAPrivateUserBit = Guid('{afa505ce-c1e3-4e3d-851b-61b700e5e6cc}')
CODECAPI_AVEncMPVAddSeqEndCode = Guid('{a823178f-57df-4c7a-b8fd-e5ec8887708d}')
CODECAPI_AVEncMPVDefaultBPictureCount = Guid('{8d390aac-dc5c-4200-b57f-814d04babab2}')
CODECAPI_AVEncMPVFrameFieldMode = Guid('{acb5de96-7b93-4c2f-8825-b0295fa93bf4}')
CODECAPI_AVEncMPVGOPOpen = Guid('{b1d5d4a6-3300-49b1-ae61-a09937ab0e49}')
CODECAPI_AVEncMPVGOPSInSeq = Guid('{993410d4-2691-4192-9978-98dc2603669f}')
CODECAPI_AVEncMPVGOPSize = Guid('{95f31b26-95a4-41aa-9303-246a7fc6eef1}')
CODECAPI_AVEncMPVGOPSizeMax = Guid('{fe7de4c4-1936-4fe2-bdf7-1f18ca1d001f}')
CODECAPI_AVEncMPVGOPSizeMin = Guid('{7155cf20-d440-4852-ad0f-9c4abfe37a6a}')
CODECAPI_AVEncMPVGenerateHeaderPicDispExt = Guid('{c6412f84-c03f-4f40-a00c-4293df8395bb}')
CODECAPI_AVEncMPVGenerateHeaderPicExt = Guid('{1b8464ab-944f-45f0-b74e-3a58dad11f37}')
CODECAPI_AVEncMPVGenerateHeaderSeqDispExt = Guid('{6437aa6f-5a3c-4de9-8a16-53d9c4ad326f}')
CODECAPI_AVEncMPVGenerateHeaderSeqExt = Guid('{d5e78611-082d-4e6b-98af-0f51ab139222}')
CODECAPI_AVEncMPVGenerateHeaderSeqScaleExt = Guid('{0722d62f-dd59-4a86-9cd5-644f8e2653d8}')
CODECAPI_AVEncMPVIntraDCPrecision = Guid('{a0116151-cbc8-4af3-97dc-d00cceb82d79}')
CODECAPI_AVEncMPVIntraVLCTable = Guid('{a2b83ff5-1a99-405a-af95-c5997d558d3a}')
CODECAPI_AVEncMPVLevel = Guid('{6ee40c40-a60c-41ef-8f50-37c2249e2cb3}')
CODECAPI_AVEncMPVProfile = Guid('{dabb534a-1d99-4284-975a-d90e2239baa1}')
CODECAPI_AVEncMPVQScaleType = Guid('{2b79ebb7-f484-4af7-bb58-a2a188c5cbbe}')
CODECAPI_AVEncMPVQuantMatrixChromaIntra = Guid('{9eb9ecd4-018d-4ffd-8f2d-39e49f07b17a}')
CODECAPI_AVEncMPVQuantMatrixChromaNonIntra = Guid('{1415b6b1-362a-4338-ba9a-1ef58703c05b}')
CODECAPI_AVEncMPVQuantMatrixIntra = Guid('{9bea04f3-6621-442c-8ba1-3ac378979698}')
CODECAPI_AVEncMPVQuantMatrixNonIntra = Guid('{87f441d8-0997-4beb-a08e-8573d409cf75}')
CODECAPI_AVEncMPVScanPattern = Guid('{7f8a478e-7bbb-4ae2-b2fc-96d17fc4a2d6}')
CODECAPI_AVEncMPVSceneDetection = Guid('{552799f1-db4c-405b-8a3a-c93f2d0674dc}')
CODECAPI_AVEncMPVUseConcealmentMotionVectors = Guid('{ec770cf3-6908-4b4b-aa30-7fb986214fea}')
CODECAPI_AVEncMaxFrameRate = Guid('{b98e1b31-19fa-4d4f-9931-d6a5b8aab93c}')
CODECAPI_AVEncMuxOutputStreamType = Guid('{cedd9e8f-34d3-44db-a1d8-f81520254f3e}')
CODECAPI_AVEncNoInputCopy = Guid('{d2b46a2a-e8ee-4ec5-869e-449b6c62c81a}')
CODECAPI_AVEncNumWorkerThreads = Guid('{b0c8bf60-16f7-4951-a30b-1db1609293d6}')
CODECAPI_AVEncProgressiveUpdateTime = Guid('{649faf66-afc6-4828-8fdc-0771cd9ab17d}')
CODECAPI_AVEncSliceControlMode = Guid('{e9e782ef-5f18-44c9-a90b-e9c3c2c17b0b}')
CODECAPI_AVEncSliceControlSize = Guid('{92f51df3-07a5-4172-aefe-c69ca3b60e35}')
CODECAPI_AVEncSliceGenerationMode = Guid('{8a6bc67f-9497-4286-b46b-02db8d60edbc}')
CODECAPI_AVEncStatAudioAverageBPS = Guid('{ca6724db-7059-4351-8b43-f82198826a14}')
CODECAPI_AVEncStatAudioAveragePCMValue = Guid('{979272f8-d17f-4e32-bb73-4e731c68ba2d}')
CODECAPI_AVEncStatAudioPeakPCMValue = Guid('{dce7fd34-dc00-4c16-821b-35d9eb00fb1a}')
CODECAPI_AVEncStatAverageBPS = Guid('{ca6724db-7059-4351-8b43-f82198826a14}')
CODECAPI_AVEncStatCommonCompletedPasses = Guid('{3e5de533-9df7-438c-854f-9f7dd3683d34}')
CODECAPI_AVEncStatHardwareBandwidthUtilitization = Guid('{0124ba9b-dc41-4826-b45f-18ac01b3d5a8}')
CODECAPI_AVEncStatHardwareProcessorUtilitization = Guid('{995dc027-cb95-49e6-b91b-5967753cdcb8}')
CODECAPI_AVEncStatMPVSkippedEmptyFrames = Guid('{32195fd3-590d-4812-a7ed-6d639a1f9711}')
CODECAPI_AVEncStatVideoCodedFrames = Guid('{d47f8d61-6f5a-4a26-bb9f-cd9518462bcd}')
CODECAPI_AVEncStatVideoOutputFrameRate = Guid('{be747849-9ab4-4a63-98fe-f143f04f8ee9}')
CODECAPI_AVEncStatVideoTotalFrames = Guid('{fdaa9916-119a-4222-9ad6-3f7cab99cc8b}')
CODECAPI_AVEncStatWMVCBAvg = Guid('{6aa6229f-d602-4b9d-b68c-c1ad78884bef}')
CODECAPI_AVEncStatWMVCBMax = Guid('{e976bef8-00fe-44b4-b625-8f238bc03499}')
CODECAPI_AVEncStatWMVDecoderComplexityProfile = Guid('{89e69fc3-0f9b-436c-974a-df821227c90d}')
CODECAPI_AVEncTileColumns = Guid('{b4b31205-01e8-452c-b876-8c6506545925}')
CODECAPI_AVEncTileRows = Guid('{fbc650fc-41ab-4f9b-84b5-065be9cd99ee}')
CODECAPI_AVEncVideoCBRMotionTradeoff = Guid('{0d49451e-18d5-4367-a4ef-3240df1693c4}')
CODECAPI_AVEncVideoCTBSize = Guid('{d47db8b2-e73b-4cb9-8c3e-bd877d06d77b}')
CODECAPI_AVEncVideoCodedVideoAccessUnitSize = Guid('{b4b10c15-14a7-4ce8-b173-dc90a0b4fcdb}')
CODECAPI_AVEncVideoConsecutiveFramesForLayer = Guid('{0af35522-d984-45ae-bbb8-53933e0ab1b5}')
CODECAPI_AVEncVideoContentType = Guid('{66117aca-eb77-459d-930c-a48d9d0683fc}')
CODECAPI_AVEncVideoDefaultUpperFieldDominant = Guid('{810167c4-0bc1-47ca-8fc2-57055a1474a5}')
CODECAPI_AVEncVideoDirtyRectEnabled = Guid('{8acb8fdd-5e0c-4c66-8729-b8f629ab04fb}')
CODECAPI_AVEncVideoDisplayDimension = Guid('{de053668-f4ec-47a9-86d0-836770f0c1d5}')
CODECAPI_AVEncVideoEncodeDimension = Guid('{1074df28-7e0f-47a4-a453-cdd73870f5ce}')
CODECAPI_AVEncVideoEncodeFrameTypeQP = Guid('{aa70b610-e03f-450c-ad07-07314e639ce7}')
CODECAPI_AVEncVideoEncodeOffsetOrigin = Guid('{6bc098fe-a71a-4454-852e-4d2ddeb2cd24}')
CODECAPI_AVEncVideoEncodeQP = Guid('{2cb5696b-23fb-4ce1-a0f9-ef5b90fd55ca}')
CODECAPI_AVEncVideoFieldSwap = Guid('{fefd7569-4e0a-49f2-9f2b-360ea48c19a2}')
CODECAPI_AVEncVideoForceKeyFrame = Guid('{398c1b98-8353-475a-9ef2-8f265d260345}')
CODECAPI_AVEncVideoForceSourceScanType = Guid('{1ef2065f-058a-4765-a4fc-8a864c103012}')
CODECAPI_AVEncVideoGradualIntraRefresh = Guid('{8f347dee-cb0d-49ba-b462-db6927ee2101}')
CODECAPI_AVEncVideoHeaderDropFrame = Guid('{6ed9e124-7925-43fe-971b-e019f62222b4}')
CODECAPI_AVEncVideoHeaderFrames = Guid('{afd5f567-5c1b-4adc-bdaf-735610381436}')
CODECAPI_AVEncVideoHeaderHours = Guid('{2acc7702-e2da-4158-bf9b-88880129d740}')
CODECAPI_AVEncVideoHeaderMinutes = Guid('{dc1a99ce-0307-408b-880b-b8348ee8ca7f}')
CODECAPI_AVEncVideoHeaderSeconds = Guid('{4a2e1a05-a780-4f58-8120-9a449d69656b}')
CODECAPI_AVEncVideoInputChromaResolution = Guid('{bb0cec33-16f1-47b0-8a88-37815bee1739}')
CODECAPI_AVEncVideoInputChromaSubsampling = Guid('{a8e73a39-4435-4ec3-a6ea-98300f4b36f7}')
CODECAPI_AVEncVideoInputColorLighting = Guid('{46a99549-0015-4a45-9c30-1d5cfa258316}')
CODECAPI_AVEncVideoInputColorNominalRange = Guid('{16cf25c6-a2a6-48e9-ae80-21aec41d427e}')
CODECAPI_AVEncVideoInputColorPrimaries = Guid('{c24d783f-7ce6-4278-90ab-28a4f1e5f86c}')
CODECAPI_AVEncVideoInputColorTransferFunction = Guid('{8c056111-a9c3-4b08-a0a0-ce13f8a27c75}')
CODECAPI_AVEncVideoInputColorTransferMatrix = Guid('{52ed68b9-72d5-4089-958d-f5405d55081c}')
CODECAPI_AVEncVideoInstantTemporalUpSwitching = Guid('{a3308307-0d96-4ba4-b1f0-b91a5e49df10}')
CODECAPI_AVEncVideoIntraLayerPrediction = Guid('{d3af46b8-bf47-44bb-a283-69f0b0228ff9}')
CODECAPI_AVEncVideoInverseTelecineEnable = Guid('{2ea9098b-e76d-4ccd-a030-d3b889c1b64c}')
CODECAPI_AVEncVideoInverseTelecineThreshold = Guid('{40247d84-e895-497f-b44c-b74560acfe27}')
CODECAPI_AVEncVideoLTRBufferControl = Guid('{a4a0e93d-4cbc-444c-89f4-826d310e92a7}')
CODECAPI_AVEncVideoMarkLTRFrame = Guid('{e42f4748-a06d-4ef9-8cea-3d05fde3bd3b}')
CODECAPI_AVEncVideoMaxCTBSize = Guid('{822363ff-cec8-43e5-92fd-e097488485e9}')
CODECAPI_AVEncVideoMaxKeyframeDistance = Guid('{2987123a-ba93-4704-b489-ec1e5f25292c}')
CODECAPI_AVEncVideoMaxNumRefFrame = Guid('{964829ed-94f9-43b4-b74d-ef40944b69a0}')
CODECAPI_AVEncVideoMaxNumRefFrameForLayer = Guid('{3141c639-6329-40d1-b7e7-2f0e3ac18e02}')
CODECAPI_AVEncVideoMaxQP = Guid('{3daf6f66-a6a7-45e0-a8e5-f2743f46a3a2}')
CODECAPI_AVEncVideoMaxTemporalLayers = Guid('{9c668cfe-08e1-424a-934e-b764b064802a}')
CODECAPI_AVEncVideoMeanAbsoluteDifference = Guid('{e5c0c10f-81a4-422d-8c3f-b474a4581336}')
CODECAPI_AVEncVideoMinQP = Guid('{0ee22c6a-a37c-4568-b5f1-9d4c2b3ab886}')
CODECAPI_AVEncVideoNoOfFieldsToEncode = Guid('{61e4bbe2-4ee0-40e7-80ab-51ddeebe6291}')
CODECAPI_AVEncVideoNoOfFieldsToSkip = Guid('{a97e1240-1427-4c16-a7f7-3dcfd8ba4cc5}')
CODECAPI_AVEncVideoNumGOPsPerIDR = Guid('{83bc5bdb-5b89-4521-8f66-33151c373176}')
CODECAPI_AVEncVideoOutputChromaResolution = Guid('{6097b4c9-7c1d-4e64-bfcc-9e9765318ae7}')
CODECAPI_AVEncVideoOutputChromaSubsampling = Guid('{fa561c6c-7d17-44f0-83c9-32ed12e96343}')
CODECAPI_AVEncVideoOutputColorLighting = Guid('{0e5aaac6-ace6-4c5c-998e-1a8c9c6c0f89}')
CODECAPI_AVEncVideoOutputColorNominalRange = Guid('{972835ed-87b5-4e95-9500-c73958566e54}')
CODECAPI_AVEncVideoOutputColorPrimaries = Guid('{be95907c-9d04-4921-8985-a6d6d87d1a6c}')
CODECAPI_AVEncVideoOutputColorTransferFunction = Guid('{4a7f884a-ea11-460d-bf57-b88bc75900de}')
CODECAPI_AVEncVideoOutputColorTransferMatrix = Guid('{a9b90444-af40-4310-8fbe-ed6d933f892b}')
CODECAPI_AVEncVideoOutputFrameRate = Guid('{ea85e7c3-9567-4d99-87c4-02c1c278ca7c}')
CODECAPI_AVEncVideoOutputFrameRateConversion = Guid('{8c068bf4-369a-4ba3-82fd-b2518fb3396e}')
CODECAPI_AVEncVideoOutputScanType = Guid('{460b5576-842e-49ab-a62d-b36f7312c9db}')
CODECAPI_AVEncVideoPixelAspectRatio = Guid('{3cdc718f-b3e9-4eb6-a57f-cf1f1b321b87}')
CODECAPI_AVEncVideoROIEnabled = Guid('{d74f7f18-44dd-4b85-aba3-05d9f42a8280}')
CODECAPI_AVEncVideoRateControlParams = Guid('{87d43767-7645-44ec-b438-d3322fbca29f}')
CODECAPI_AVEncVideoSelectLayer = Guid('{eb1084f5-6aaa-4914-bb2f-6147227f12e7}')
CODECAPI_AVEncVideoSourceFilmContent = Guid('{1791c64b-ccfc-4827-a0ed-2557793b2b1c}')
CODECAPI_AVEncVideoSourceIsBW = Guid('{42ffc49b-1812-4fdc-8d24-7054c521e6eb}')
CODECAPI_AVEncVideoSupportedControls = Guid('{d3f40fdd-77b9-473d-8196-061259e69cff}')
CODECAPI_AVEncVideoTemporalLayerCount = Guid('{19caebff-b74d-4cfd-8c27-c2f9d97d5f52}')
CODECAPI_AVEncVideoUsage = Guid('{1f636849-5dc1-49f1-b1d8-ce3cf62ea385}')
CODECAPI_AVEncVideoUseLTRFrame = Guid('{00752db8-55f7-4f80-895b-27639195f2ad}')
CODECAPI_AVEncWMVDecoderComplexity = Guid('{f32c0dab-f3cb-4217-b79f-8762768b5f67}')
CODECAPI_AVEncWMVInterlacedEncoding = Guid('{e3d00f8a-c6f5-4e14-a588-0ec87a726f9b}')
CODECAPI_AVEncWMVKeyFrameBufferLevelMarker = Guid('{51ff1115-33ac-426c-a1b1-09321bdf96b4}')
CODECAPI_AVEncWMVKeyFrameDistance = Guid('{5569055e-e268-4771-b83e-9555ea28aed3}')
CODECAPI_AVEncWMVProduceDummyFrames = Guid('{d669d001-183c-42e3-a3ca-2f4586d2396c}')
CODECAPI_AVLowLatencyMode = Guid('{9c27891a-ed7a-40e1-88e8-b22727a024ee}')
CODECAPI_AVPriorityControl = Guid('{54ba3dc8-bdde-4329-b187-2018bc5c2ba1}')
CODECAPI_AVRealtimeControl = Guid('{6f440632-c4ad-4bf7-9e52-456942b454b0}')
CODECAPI_AVScenarioInfo = Guid('{b28a6e64-3ff9-446a-8a4b-0d7a53413236}')
CODECAPI_GUID_AVDecAudioInputAAC = Guid('{97df7828-b94a-47e2-a4bc-51194db22a4d}')
CODECAPI_GUID_AVDecAudioInputDTS = Guid('{600bc0ca-6a1f-4e91-b241-1bbeb1cb19e0}')
CODECAPI_GUID_AVDecAudioInputDolby = Guid('{8e4228a0-f000-4e0b-8f54-ab8d24ad61a2}')
CODECAPI_GUID_AVDecAudioInputDolbyDigitalPlus = Guid('{0803e185-8f5d-47f5-9908-19a5bbc9fe34}')
CODECAPI_GUID_AVDecAudioInputHEAAC = Guid('{16efb4aa-330e-4f5c-98a8-cf6ac55cbe60}')
CODECAPI_GUID_AVDecAudioInputMPEG = Guid('{91106f36-02c5-4f75-9719-3b7abf75e1f6}')
CODECAPI_GUID_AVDecAudioInputPCM = Guid('{f2421da5-bbb4-4cd5-a996-933c6b5d1347}')
CODECAPI_GUID_AVDecAudioInputWMA = Guid('{c95e8dcf-4058-4204-8c42-cb24d91e4b9b}')
CODECAPI_GUID_AVDecAudioInputWMAPro = Guid('{0128b7c7-da72-4fe3-bef8-5c52e3557704}')
CODECAPI_GUID_AVDecAudioOutputFormat_PCM = Guid('{696e1d31-548f-4036-825f-7026c60011bd}')
CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Headphones = Guid('{696e1d34-548f-4036-825f-7026c60011bd}')
CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_Auto = Guid('{696e1d35-548f-4036-825f-7026c60011bd}')
CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_MatrixEncoded = Guid('{696e1d30-548f-4036-825f-7026c60011bd}')
CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_Bitstream = Guid('{696e1d33-548f-4036-825f-7026c60011bd}')
CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_PCM = Guid('{696e1d32-548f-4036-825f-7026c60011bd}')
CODECAPI_GUID_AVEncCommonFormatATSC = Guid('{8d7b897c-a019-4670-aa76-2edcac7ac296}')
CODECAPI_GUID_AVEncCommonFormatDVB = Guid('{71830d8f-6c33-430d-844b-c2705baae6db}')
CODECAPI_GUID_AVEncCommonFormatDVD_DashVR = Guid('{e55199d6-044c-4dae-a488-531ed306235b}')
CODECAPI_GUID_AVEncCommonFormatDVD_PlusVR = Guid('{e74c6f2e-ec37-478d-9af4-a5e135b6271c}')
CODECAPI_GUID_AVEncCommonFormatDVD_V = Guid('{cc9598c4-e7fe-451d-b1ca-761bc840b7f3}')
CODECAPI_GUID_AVEncCommonFormatHighMAT = Guid('{1eabe760-fb2b-4928-90d1-78db88eee889}')
CODECAPI_GUID_AVEncCommonFormatHighMPV = Guid('{a2d25db8-b8f9-42c2-8bc7-0b93cf604788}')
CODECAPI_GUID_AVEncCommonFormatMP3 = Guid('{349733cd-eb08-4dc2-8197-e49835ef828b}')
CODECAPI_GUID_AVEncCommonFormatSVCD = Guid('{51d85818-8220-448c-8066-d69bed16c9ad}')
CODECAPI_GUID_AVEncCommonFormatUnSpecified = Guid('{af46a35a-6024-4525-a48a-094b97f5b3c2}')
CODECAPI_GUID_AVEncCommonFormatVCD = Guid('{95035bf7-9d90-40ff-ad5c-5cf8cf71ca1d}')
CODECAPI_GUID_AVEncDTS = Guid('{45fbcaa2-5e6e-4ab0-8893-5903bee93acf}')
CODECAPI_GUID_AVEncDTSHD = Guid('{2052e630-469d-4bfb-80ca-1d656e7e918f}')
CODECAPI_GUID_AVEncDV = Guid('{09b769c7-3329-44fb-8954-fa30937d3d5a}')
CODECAPI_GUID_AVEncDolbyDigitalConsumer = Guid('{c1a7bf6c-0059-4bfa-94ef-ef747a768d52}')
CODECAPI_GUID_AVEncDolbyDigitalPlus = Guid('{698d1b80-f7dd-415c-971c-42492a2056c6}')
CODECAPI_GUID_AVEncDolbyDigitalPro = Guid('{f5be76cc-0ff8-40eb-9cb1-bba94004d44f}')
CODECAPI_GUID_AVEncH264Video = Guid('{95044eab-31b3-47de-8e75-38a42bb03e28}')
CODECAPI_GUID_AVEncMLP = Guid('{05f73e29-f0d1-431e-a41c-a47432ec5a66}')
CODECAPI_GUID_AVEncMPEG1Audio = Guid('{d4dd1362-cd4a-4cd6-8138-b94db4542b04}')
CODECAPI_GUID_AVEncMPEG1Video = Guid('{c8dafefe-da1e-4774-b27d-11830c16b1fe}')
CODECAPI_GUID_AVEncMPEG2Audio = Guid('{ee4cbb1f-9c3f-4770-92b5-fcb7c2a8d381}')
CODECAPI_GUID_AVEncMPEG2Video = Guid('{046dc19a-6677-4aaa-a31d-c1ab716f4560}')
CODECAPI_GUID_AVEncPCM = Guid('{844be7f4-26cf-4779-b386-cc05d187990c}')
CODECAPI_GUID_AVEncSDDS = Guid('{1dc1b82f-11c8-4c71-b7b6-ee3eb9bc2b94}')
CODECAPI_GUID_AVEncWMALossless = Guid('{55ca7265-23d8-4761-9031-b74fbe12f4c1}')
CODECAPI_GUID_AVEncWMAPro = Guid('{1955f90c-33f7-4a68-ab81-53f5657125c4}')
CODECAPI_GUID_AVEncWMAVoice = Guid('{13ed18cb-50e8-4276-a288-a6aa228382d9}')
CODECAPI_GUID_AVEncWMV = Guid('{4e0fef9b-1d43-41bd-b8bd-4d7bf7457a2a}')
CODECAPI_GUID_AVEndMPEG4Video = Guid('{dd37b12a-9503-4f8b-b8d0-324a00c0a1cf}')
CODECAPI_GetOPMContext = Guid('{2f036c05-4c14-4689-8839-294c6d73e053}')
CODECAPI_SetHDCPManagerContext = Guid('{6d2d1fc8-3dc9-47eb-a1a2-471c80cd60d0}')
CODECAPI_VideoEncoderDisplayContentType = Guid('{79b90b27-f4b1-42dc-9dd7-cdaf8135c400}')
CPK_DS_AC3Decoder = Guid('{6c9c69d6-0ffc-4481-afdb-cdf1c79c6f3e}')
CPK_DS_MPEG2Decoder = Guid('{9910c5cd-95c9-4e06-865a-efa1c8016bf4}')
CResamplerMediaObject = Guid('{f447b69e-1884-4a7e-8055-346f74d6edb3}')
CResizerDMO = Guid('{1ea1ea14-48f4-4054-ad1a-e8aee10ac805}')
CResizerMediaObject = Guid('{d3ec8b8b-7728-4fd8-9fe0-7b67d19f73a3}')
CShotDetectorDmo = Guid('{56aefacd-110c-4397-9292-b0a0c61b6750}')
CSmpteTransformsDmo = Guid('{bde6388b-da25-485d-ba7f-fabc28b20318}')
CThumbnailGeneratorDmo = Guid('{559c6bad-1ea8-4963-a087-8a6810f9218b}')
CTocGeneratorDmo = Guid('{4dda1941-77a0-4fb1-a518-e2185041d70c}')
CVodafoneAACCCDecMediaObject = Guid('{7e76bf7f-c993-4e26-8fab-470a70c0d59c}')
CVodafoneAACDecMediaObject = Guid('{7f36f942-dcf3-4d82-9289-5b1820278f7c}')
CWMADecMediaObject = Guid('{2eeb4adf-4578-4d10-bca7-bb955f56320a}')
CWMAEncMediaObject = Guid('{70f598e9-f4ab-495a-99e2-a7c4d3d89abf}')
CWMATransMediaObject = Guid('{edcad9cb-3127-40df-b527-0152ccb3f6f5}')
CWMAudioAEC = Guid('{745057c7-f353-4f2d-a7ee-58434477730e}')
CWMAudioCAPXGFXAPO = Guid('{13ab3ebd-137e-4903-9d89-60be8277fd17}')
CWMAudioCAPXLFXAPO = Guid('{c9453e73-8c5c-4463-9984-af8bab2f5447}')
CWMAudioGFXAPO = Guid('{637c490d-eee3-4c0a-973f-371958802da2}')
CWMAudioLFXAPO = Guid('{62dc1a93-ae24-464c-a43e-452f824c4250}')
CWMAudioSpdTxDMO = Guid('{5210f8e4-b0bb-47c3-a8d9-7b2282cc79ed}')
CWMSPDecMediaObject = Guid('{874131cb-4ecc-443b-8948-746b89595d20}')
CWMSPEncMediaObject = Guid('{67841b03-c689-4188-ad3f-4c9ebeec710b}')
CWMSPEncMediaObject2 = Guid('{1f1f4e1a-2252-4063-84bb-eee75f8856d5}')
CWMTDecMediaObject = Guid('{f9dbc64e-2dd0-45dd-9b52-66642ef94431}')
CWMTEncMediaObject = Guid('{60b67652-e46b-4e44-8609-f74bffdc083c}')
CWMV9EncMediaObject = Guid('{d23b90d0-144f-46bd-841d-59e4eb19dc59}')
CWMVDecMediaObject = Guid('{82d353df-90bd-4382-8bc2-3f6192b76e34}')
CWMVEncMediaObject2 = Guid('{96b57cdd-8966-410c-bb1f-c97eea765c04}')
CWMVXEncMediaObject = Guid('{7e320092-596a-41b2-bbeb-175d10504eb6}')
CWVC1DecMediaObject = Guid('{c9bfbccf-e60e-4588-a3df-5a03b1fd9585}')
CWVC1EncMediaObject = Guid('{44653d0d-8cca-41e7-baca-884337b747ac}')
CZuneAACCCDecMediaObject = Guid('{a74e98f2-52d6-4b4e-885b-e0a6ca4f187a}')
CZuneM4S2DecMediaObject = Guid('{c56fc25c-0fc6-404a-9503-b10bf51a8ab9}')
class CodecAPIEventData(EasyCastStructure):
    guid: Guid
    dataLength: UInt32
    reserved: UInt32 * 3
D3D12_BITSTREAM_ENCRYPTION_TYPE = Int32
D3D12_BITSTREAM_ENCRYPTION_TYPE_NONE: D3D12_BITSTREAM_ENCRYPTION_TYPE = 0
class D3D12_FEATURE_DATA_VIDEO_ARCHITECTURE(EasyCastStructure):
    IOCoherent: Windows.Win32.Foundation.BOOL
class D3D12_FEATURE_DATA_VIDEO_DECODER_HEAP_SIZE(EasyCastStructure):
    VideoDecoderHeapDesc: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_HEAP_DESC
    MemoryPoolL0Size: UInt64
    MemoryPoolL1Size: UInt64
class D3D12_FEATURE_DATA_VIDEO_DECODER_HEAP_SIZE1(EasyCastStructure):
    VideoDecoderHeapDesc: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_HEAP_DESC
    Protected: Windows.Win32.Foundation.BOOL
    MemoryPoolL0Size: UInt64
    MemoryPoolL1Size: UInt64
class D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    Configuration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION
    DecodeSample: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SAMPLE
    OutputFormat: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FORMAT
    FrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    BitRate: UInt32
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS
    ScaleSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SCALE_SUPPORT
class D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS(EasyCastStructure):
    NodeIndex: UInt32
    Configuration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION
    FormatCount: UInt32
    pOutputFormats: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT)
class D3D12_FEATURE_DATA_VIDEO_DECODE_FORMAT_COUNT(EasyCastStructure):
    NodeIndex: UInt32
    Configuration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION
    FormatCount: UInt32
class D3D12_FEATURE_DATA_VIDEO_DECODE_HISTOGRAM(EasyCastStructure):
    NodeIndex: UInt32
    DecodeProfile: Guid
    Width: UInt32
    Height: UInt32
    DecodeFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    Components: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS
    BinCount: UInt32
    CounterBitDepth: UInt32
class D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES(EasyCastStructure):
    NodeIndex: UInt32
    ProfileCount: UInt32
    pProfiles: POINTER(Guid)
class D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILE_COUNT(EasyCastStructure):
    NodeIndex: UInt32
    ProfileCount: UInt32
class D3D12_FEATURE_DATA_VIDEO_DECODE_PROTECTED_RESOURCES(EasyCastStructure):
    NodeIndex: UInt32
    Configuration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAGS
class D3D12_FEATURE_DATA_VIDEO_DECODE_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    Configuration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION
    Width: UInt32
    Height: UInt32
    DecodeFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    FrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    BitRate: UInt32
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_SUPPORT_FLAGS
    ConfigurationFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS
    DecodeTier: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_TIER
class D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    IsSupported: Windows.Win32.Foundation.BOOL
class D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    Profile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    IsSupported: Windows.Win32.Foundation.BOOL
    CodecSupportLimits: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT
class D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    Profile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    IsSupported: Windows.Win32.Foundation.BOOL
    PictureSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT
class D3D12_FEATURE_DATA_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    Profile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    Level: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_SETTING
    SubregionMode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE
    IsSupported: Windows.Win32.Foundation.BOOL
class D3D12_FEATURE_DATA_VIDEO_ENCODER_HEAP_SIZE(EasyCastStructure):
    HeapDesc: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_HEAP_DESC
    IsSupported: Windows.Win32.Foundation.BOOL
    MemoryPoolL0Size: UInt64
    MemoryPoolL1Size: UInt64
class D3D12_FEATURE_DATA_VIDEO_ENCODER_INPUT_FORMAT(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    Profile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    Format: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    IsSupported: Windows.Win32.Foundation.BOOL
class D3D12_FEATURE_DATA_VIDEO_ENCODER_INTRA_REFRESH_MODE(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    Profile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    Level: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_SETTING
    IntraRefreshMode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE
    IsSupported: Windows.Win32.Foundation.BOOL
class D3D12_FEATURE_DATA_VIDEO_ENCODER_OUTPUT_RESOLUTION(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    ResolutionRatiosCount: UInt32
    IsSupported: Windows.Win32.Foundation.BOOL
    MinResolutionSupported: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC
    MaxResolutionSupported: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC
    ResolutionWidthMultipleRequirement: UInt32
    ResolutionHeightMultipleRequirement: UInt32
    pResolutionRatios: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_RATIO_DESC_head)
class D3D12_FEATURE_DATA_VIDEO_ENCODER_OUTPUT_RESOLUTION_RATIOS_COUNT(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    ResolutionRatiosCount: UInt32
class D3D12_FEATURE_DATA_VIDEO_ENCODER_PROFILE_LEVEL(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    Profile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    IsSupported: Windows.Win32.Foundation.BOOL
    MinSupportedLevel: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_SETTING
    MaxSupportedLevel: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_SETTING
class D3D12_FEATURE_DATA_VIDEO_ENCODER_RATE_CONTROL_MODE(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    RateControlMode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE
    IsSupported: Windows.Win32.Foundation.BOOL
class D3D12_FEATURE_DATA_VIDEO_ENCODER_RESOLUTION_SUPPORT_LIMITS(EasyCastStructure):
    MaxSubregionsNumber: UInt32
    MaxIntraRefreshFrameDuration: UInt32
    SubregionBlockPixelsSize: UInt32
    QPMapRegionPixelsSize: UInt32
class D3D12_FEATURE_DATA_VIDEO_ENCODER_RESOURCE_REQUIREMENTS(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    Profile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    InputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    PictureTargetResolution: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC
    IsSupported: Windows.Win32.Foundation.BOOL
    CompressedBitstreamBufferAccessAlignment: UInt32
    EncoderMetadataBufferAccessAlignment: UInt32
    MaxEncoderOutputMetadataBufferSize: UInt32
class D3D12_FEATURE_DATA_VIDEO_ENCODER_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    Codec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    InputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    CodecConfiguration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION
    CodecGopSequence: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE
    RateControl: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL
    IntraRefresh: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE
    SubregionFrameEncoding: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE
    ResolutionsListCount: UInt32
    pResolutionList: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC_head)
    MaxReferenceFramesInDPB: UInt32
    ValidationFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_VALIDATION_FLAGS
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_SUPPORT_FLAGS
    SuggestedProfile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    SuggestedLevel: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_SETTING
    pResolutionDependentSupport: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_FEATURE_DATA_VIDEO_ENCODER_RESOLUTION_SUPPORT_LIMITS_head)
class D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMANDS(EasyCastStructure):
    NodeIndex: UInt32
    CommandCount: UInt32
    pCommandInfos: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_INFO_head)
class D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_COUNT(EasyCastStructure):
    NodeIndex: UInt32
    CommandCount: UInt32
class D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_PARAMETERS(EasyCastStructure):
    CommandId: Guid
    Stage: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE
    ParameterCount: UInt32
    pParameterInfos: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_INFO_head)
class D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_PARAMETER_COUNT(EasyCastStructure):
    CommandId: Guid
    Stage: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE
    ParameterCount: UInt32
    ParameterPacking: UInt32
class D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_SIZE(EasyCastStructure):
    NodeIndex: UInt32
    CommandId: Guid
    pCreationParameters: c_void_p
    CreationParametersSizeInBytes: UIntPtr
    MemoryPoolL0Size: UInt64
    MemoryPoolL1Size: UInt64
class D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    CommandId: Guid
    pInputData: c_void_p
    InputDataSizeInBytes: UIntPtr
    pOutputData: c_void_p
    OutputDataSizeInBytes: UIntPtr
class D3D12_FEATURE_DATA_VIDEO_FEATURE_AREA_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    VideoDecodeSupport: Windows.Win32.Foundation.BOOL
    VideoProcessSupport: Windows.Win32.Foundation.BOOL
    VideoEncodeSupport: Windows.Win32.Foundation.BOOL
class D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR(EasyCastStructure):
    NodeIndex: UInt32
    InputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    BlockSizeFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAGS
    PrecisionFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_FLAGS
    SizeRange: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SIZE_RANGE
class D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR_PROTECTED_RESOURCES(EasyCastStructure):
    NodeIndex: UInt32
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAGS
class D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR_SIZE(EasyCastStructure):
    NodeIndex: UInt32
    InputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    BlockSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE
    Precision: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION
    SizeRange: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SIZE_RANGE
    Protected: Windows.Win32.Foundation.BOOL
    MotionVectorHeapMemoryPoolL0Size: UInt64
    MotionVectorHeapMemoryPoolL1Size: UInt64
    MotionEstimatorMemoryPoolL0Size: UInt64
    MotionEstimatorMemoryPoolL1Size: UInt64
class D3D12_FEATURE_DATA_VIDEO_PROCESSOR_SIZE(EasyCastStructure):
    NodeMask: UInt32
    pOutputStreamDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC_head)
    NumInputStreamDescs: UInt32
    pInputStreamDescs: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC_head)
    MemoryPoolL0Size: UInt64
    MemoryPoolL1Size: UInt64
class D3D12_FEATURE_DATA_VIDEO_PROCESSOR_SIZE1(EasyCastStructure):
    NodeMask: UInt32
    pOutputStreamDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC_head)
    NumInputStreamDescs: UInt32
    pInputStreamDescs: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC_head)
    Protected: Windows.Win32.Foundation.BOOL
    MemoryPoolL0Size: UInt64
    MemoryPoolL1Size: UInt64
class D3D12_FEATURE_DATA_VIDEO_PROCESS_MAX_INPUT_STREAMS(EasyCastStructure):
    NodeIndex: UInt32
    MaxInputStreams: UInt32
class D3D12_FEATURE_DATA_VIDEO_PROCESS_PROTECTED_RESOURCES(EasyCastStructure):
    NodeIndex: UInt32
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAGS
class D3D12_FEATURE_DATA_VIDEO_PROCESS_REFERENCE_INFO(EasyCastStructure):
    NodeIndex: UInt32
    DeinterlaceMode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS
    Filters: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_FILTER_FLAGS
    FeatureSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_FEATURE_FLAGS
    InputFrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    OutputFrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    EnableAutoProcessing: Windows.Win32.Foundation.BOOL
    PastFrames: UInt32
    FutureFrames: UInt32
class D3D12_FEATURE_DATA_VIDEO_PROCESS_SUPPORT(EasyCastStructure):
    NodeIndex: UInt32
    InputSample: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SAMPLE
    InputFieldType: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FIELD_TYPE
    InputStereoFormat: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FRAME_STEREO_FORMAT
    InputFrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    OutputFormat: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FORMAT
    OutputStereoFormat: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FRAME_STEREO_FORMAT
    OutputFrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_SUPPORT_FLAGS
    ScaleSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SCALE_SUPPORT
    FeatureSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_FEATURE_FLAGS
    DeinterlaceSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS
    AutoProcessingSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS
    FilterSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_FILTER_FLAGS
    FilterRangeSupport: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_FILTER_RANGE * 32
D3D12_FEATURE_VIDEO = Int32
D3D12_FEATURE_VIDEO_DECODE_SUPPORT: D3D12_FEATURE_VIDEO = 0
D3D12_FEATURE_VIDEO_DECODE_PROFILES: D3D12_FEATURE_VIDEO = 1
D3D12_FEATURE_VIDEO_DECODE_FORMATS: D3D12_FEATURE_VIDEO = 2
D3D12_FEATURE_VIDEO_DECODE_CONVERSION_SUPPORT: D3D12_FEATURE_VIDEO = 3
D3D12_FEATURE_VIDEO_PROCESS_SUPPORT: D3D12_FEATURE_VIDEO = 5
D3D12_FEATURE_VIDEO_PROCESS_MAX_INPUT_STREAMS: D3D12_FEATURE_VIDEO = 6
D3D12_FEATURE_VIDEO_PROCESS_REFERENCE_INFO: D3D12_FEATURE_VIDEO = 7
D3D12_FEATURE_VIDEO_DECODER_HEAP_SIZE: D3D12_FEATURE_VIDEO = 8
D3D12_FEATURE_VIDEO_PROCESSOR_SIZE: D3D12_FEATURE_VIDEO = 9
D3D12_FEATURE_VIDEO_DECODE_PROFILE_COUNT: D3D12_FEATURE_VIDEO = 10
D3D12_FEATURE_VIDEO_DECODE_FORMAT_COUNT: D3D12_FEATURE_VIDEO = 11
D3D12_FEATURE_VIDEO_ARCHITECTURE: D3D12_FEATURE_VIDEO = 17
D3D12_FEATURE_VIDEO_DECODE_HISTOGRAM: D3D12_FEATURE_VIDEO = 18
D3D12_FEATURE_VIDEO_FEATURE_AREA_SUPPORT: D3D12_FEATURE_VIDEO = 19
D3D12_FEATURE_VIDEO_MOTION_ESTIMATOR: D3D12_FEATURE_VIDEO = 20
D3D12_FEATURE_VIDEO_MOTION_ESTIMATOR_SIZE: D3D12_FEATURE_VIDEO = 21
D3D12_FEATURE_VIDEO_EXTENSION_COMMAND_COUNT: D3D12_FEATURE_VIDEO = 22
D3D12_FEATURE_VIDEO_EXTENSION_COMMANDS: D3D12_FEATURE_VIDEO = 23
D3D12_FEATURE_VIDEO_EXTENSION_COMMAND_PARAMETER_COUNT: D3D12_FEATURE_VIDEO = 24
D3D12_FEATURE_VIDEO_EXTENSION_COMMAND_PARAMETERS: D3D12_FEATURE_VIDEO = 25
D3D12_FEATURE_VIDEO_EXTENSION_COMMAND_SUPPORT: D3D12_FEATURE_VIDEO = 26
D3D12_FEATURE_VIDEO_EXTENSION_COMMAND_SIZE: D3D12_FEATURE_VIDEO = 27
D3D12_FEATURE_VIDEO_DECODE_PROTECTED_RESOURCES: D3D12_FEATURE_VIDEO = 28
D3D12_FEATURE_VIDEO_PROCESS_PROTECTED_RESOURCES: D3D12_FEATURE_VIDEO = 29
D3D12_FEATURE_VIDEO_MOTION_ESTIMATOR_PROTECTED_RESOURCES: D3D12_FEATURE_VIDEO = 30
D3D12_FEATURE_VIDEO_DECODER_HEAP_SIZE1: D3D12_FEATURE_VIDEO = 31
D3D12_FEATURE_VIDEO_PROCESSOR_SIZE1: D3D12_FEATURE_VIDEO = 32
D3D12_FEATURE_VIDEO_ENCODER_CODEC: D3D12_FEATURE_VIDEO = 33
D3D12_FEATURE_VIDEO_ENCODER_PROFILE_LEVEL: D3D12_FEATURE_VIDEO = 34
D3D12_FEATURE_VIDEO_ENCODER_OUTPUT_RESOLUTION_RATIOS_COUNT: D3D12_FEATURE_VIDEO = 35
D3D12_FEATURE_VIDEO_ENCODER_OUTPUT_RESOLUTION: D3D12_FEATURE_VIDEO = 36
D3D12_FEATURE_VIDEO_ENCODER_INPUT_FORMAT: D3D12_FEATURE_VIDEO = 37
D3D12_FEATURE_VIDEO_ENCODER_RATE_CONTROL_MODE: D3D12_FEATURE_VIDEO = 38
D3D12_FEATURE_VIDEO_ENCODER_INTRA_REFRESH_MODE: D3D12_FEATURE_VIDEO = 39
D3D12_FEATURE_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE: D3D12_FEATURE_VIDEO = 40
D3D12_FEATURE_VIDEO_ENCODER_HEAP_SIZE: D3D12_FEATURE_VIDEO = 41
D3D12_FEATURE_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT: D3D12_FEATURE_VIDEO = 42
D3D12_FEATURE_VIDEO_ENCODER_SUPPORT: D3D12_FEATURE_VIDEO = 43
D3D12_FEATURE_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT: D3D12_FEATURE_VIDEO = 44
D3D12_FEATURE_VIDEO_ENCODER_RESOURCE_REQUIREMENTS: D3D12_FEATURE_VIDEO = 45
class D3D12_QUERY_DATA_VIDEO_DECODE_STATISTICS(EasyCastStructure):
    Status: UInt64
    NumMacroblocksAffected: UInt64
    FrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    BitRate: UInt32
class D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_INPUT(EasyCastStructure):
    pMotionVectorHeap: Windows.Win32.Media.MediaFoundation.ID3D12VideoMotionVectorHeap_head
    PixelWidth: UInt32
    PixelHeight: UInt32
class D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_OUTPUT(EasyCastStructure):
    pMotionVectorTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    MotionVectorCoordinate: Windows.Win32.Media.MediaFoundation.D3D12_RESOURCE_COORDINATE
class D3D12_RESOURCE_COORDINATE(EasyCastStructure):
    X: UInt64
    Y: UInt32
    Z: UInt32
    SubresourceIndex: UInt32
class D3D12_VIDEO_DECODER_DESC(EasyCastStructure):
    NodeMask: UInt32
    Configuration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION
class D3D12_VIDEO_DECODER_HEAP_DESC(EasyCastStructure):
    NodeMask: UInt32
    Configuration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONFIGURATION
    DecodeWidth: UInt32
    DecodeHeight: UInt32
    Format: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    FrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    BitRate: UInt32
    MaxDecodePictureBufferCount: UInt32
D3D12_VIDEO_DECODE_ARGUMENT_TYPE = Int32
D3D12_VIDEO_DECODE_ARGUMENT_TYPE_PICTURE_PARAMETERS: D3D12_VIDEO_DECODE_ARGUMENT_TYPE = 0
D3D12_VIDEO_DECODE_ARGUMENT_TYPE_INVERSE_QUANTIZATION_MATRIX: D3D12_VIDEO_DECODE_ARGUMENT_TYPE = 1
D3D12_VIDEO_DECODE_ARGUMENT_TYPE_SLICE_CONTROL: D3D12_VIDEO_DECODE_ARGUMENT_TYPE = 2
D3D12_VIDEO_DECODE_ARGUMENT_TYPE_MAX_VALID: D3D12_VIDEO_DECODE_ARGUMENT_TYPE = 3
class D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM(EasyCastStructure):
    pBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    Offset: UInt64
    Size: UInt64
class D3D12_VIDEO_DECODE_CONFIGURATION(EasyCastStructure):
    DecodeProfile: Guid
    BitstreamEncryption: Windows.Win32.Media.MediaFoundation.D3D12_BITSTREAM_ENCRYPTION_TYPE
    InterlaceType: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE
D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS = Int32
D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_NONE: D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS = 0
D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_HEIGHT_ALIGNMENT_MULTIPLE_32_REQUIRED: D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS = 1
D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_POST_PROCESSING_SUPPORTED: D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS = 2
D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_REFERENCE_ONLY_ALLOCATIONS_REQUIRED: D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS = 4
D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_ALLOW_RESOLUTION_CHANGE_ON_NON_KEY_FRAME: D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS = 8
class D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    pReferenceTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    ReferenceSubresource: UInt32
    OutputColorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
    DecodeColorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
class D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS1(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    pReferenceTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    ReferenceSubresource: UInt32
    OutputColorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
    DecodeColorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
    OutputWidth: UInt32
    OutputHeight: UInt32
D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS = Int32
D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAG_NONE: D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS = 0
D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAG_SUPPORTED: D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS = 1
class D3D12_VIDEO_DECODE_FRAME_ARGUMENT(EasyCastStructure):
    Type: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_ARGUMENT_TYPE
    Size: UInt32
    pData: c_void_p
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = Int32
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_Y: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = 0
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_U: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = 1
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_V: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = 2
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_R: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = 0
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_G: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = 1
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_B: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = 2
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_A: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT = 3
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = Int32
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_NONE: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 0
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_Y: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 1
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_U: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 2
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_V: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 4
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_R: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 1
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_G: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 2
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_B: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 4
D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_A: D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS = 8
class D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS(EasyCastStructure):
    NumFrameArguments: UInt32
    FrameArguments: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_FRAME_ARGUMENT * 10
    ReferenceFrames: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_REFERENCE_FRAMES
    CompressedBitstream: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM
    pHeap: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecoderHeap_head
class D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM(EasyCastStructure):
    Offset: UInt64
    pBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
class D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS(EasyCastStructure):
    pOutputTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    OutputSubresource: UInt32
    ConversionArguments: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS
class D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1(EasyCastStructure):
    pOutputTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    OutputSubresource: UInt32
    ConversionArguments: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS1
    Histograms: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM * 4
class D3D12_VIDEO_DECODE_REFERENCE_FRAMES(EasyCastStructure):
    NumTexture2Ds: UInt32
    ppTexture2Ds: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)
    pSubresources: POINTER(UInt32)
    ppHeaps: POINTER(Windows.Win32.Media.MediaFoundation.ID3D12VideoDecoderHeap_head)
D3D12_VIDEO_DECODE_STATUS = Int32
D3D12_VIDEO_DECODE_STATUS_OK: D3D12_VIDEO_DECODE_STATUS = 0
D3D12_VIDEO_DECODE_STATUS_CONTINUE: D3D12_VIDEO_DECODE_STATUS = 1
D3D12_VIDEO_DECODE_STATUS_CONTINUE_SKIP_DISPLAY: D3D12_VIDEO_DECODE_STATUS = 2
D3D12_VIDEO_DECODE_STATUS_RESTART: D3D12_VIDEO_DECODE_STATUS = 3
D3D12_VIDEO_DECODE_STATUS_RATE_EXCEEDED: D3D12_VIDEO_DECODE_STATUS = 4
D3D12_VIDEO_DECODE_SUPPORT_FLAGS = Int32
D3D12_VIDEO_DECODE_SUPPORT_FLAG_NONE: D3D12_VIDEO_DECODE_SUPPORT_FLAGS = 0
D3D12_VIDEO_DECODE_SUPPORT_FLAG_SUPPORTED: D3D12_VIDEO_DECODE_SUPPORT_FLAGS = 1
D3D12_VIDEO_DECODE_TIER = Int32
D3D12_VIDEO_DECODE_TIER_NOT_SUPPORTED: D3D12_VIDEO_DECODE_TIER = 0
D3D12_VIDEO_DECODE_TIER_1: D3D12_VIDEO_DECODE_TIER = 1
D3D12_VIDEO_DECODE_TIER_2: D3D12_VIDEO_DECODE_TIER = 2
D3D12_VIDEO_DECODE_TIER_3: D3D12_VIDEO_DECODE_TIER = 3
D3D12_VIDEO_ENCODER_CODEC = Int32
D3D12_VIDEO_ENCODER_CODEC_H264: D3D12_VIDEO_ENCODER_CODEC = 0
D3D12_VIDEO_ENCODER_CODEC_HEVC: D3D12_VIDEO_ENCODER_CODEC = 1
class D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pH264Config: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_head)
        pHEVCConfig: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_head)
class D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264(EasyCastStructure):
    ConfigurationFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS
    DirectModeConfig: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES
    DisableDeblockingFilterConfig: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES_DISABLED: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES_TEMPORAL: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES_SPATIAL: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAG_NONE: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAG_USE_CONSTRAINED_INTRAPREDICTION: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAG_USE_ADAPTIVE_8x8_TRANSFORM: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAG_ENABLE_CABAC_ENCODING: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS = 4
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAG_ALLOW_REQUEST_INTRA_CONSTRAINED_SLICES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS = 8
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_0_ALL_LUMA_CHROMA_SLICE_BLOCK_EDGES_ALWAYS_FILTERED: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_1_DISABLE_ALL_SLICE_BLOCK_EDGES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_2_DISABLE_SLICE_BOUNDARIES_BLOCKS: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_3_USE_TWO_STAGE_DEBLOCKING: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = 3
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_4_DISABLE_CHROMA_BLOCK_EDGES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = 4
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_5_DISABLE_CHROMA_BLOCK_EDGES_AND_LUMA_BOUNDARIES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = 5
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_6_DISABLE_CHROMA_BLOCK_EDGES_AND_USE_LUMA_TWO_STAGE_DEBLOCKING: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES = 6
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_NONE: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_0_ALL_LUMA_CHROMA_SLICE_BLOCK_EDGES_ALWAYS_FILTERED: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_1_DISABLE_ALL_SLICE_BLOCK_EDGES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_2_DISABLE_SLICE_BOUNDARIES_BLOCKS: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 4
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_3_USE_TWO_STAGE_DEBLOCKING: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 8
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_4_DISABLE_CHROMA_BLOCK_EDGES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 16
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_5_DISABLE_CHROMA_BLOCK_EDGES_AND_LUMA_BOUNDARIES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAG_6_DISABLE_CHROMA_BLOCK_EDGES_AND_USE_LUMA_TWO_STAGE_DEBLOCKING: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS = 64
class D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC(EasyCastStructure):
    ConfigurationFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS
    MinLumaCodingUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE
    MaxLumaCodingUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE
    MinLumaTransformUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE
    MaxLumaTransformUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE
    max_transform_hierarchy_depth_inter: Byte
    max_transform_hierarchy_depth_intra: Byte
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE_8x8: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE_16x16: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE_32x32: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE_64x64: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE = 3
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_NONE: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_DISABLE_LOOP_FILTER_ACROSS_SLICES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_ALLOW_REQUEST_INTRA_CONSTRAINED_SLICES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_ENABLE_SAO_FILTER: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 4
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_ENABLE_LONG_TERM_REFERENCES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 8
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_USE_ASYMETRIC_MOTION_PARTITION: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 16
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_ENABLE_TRANSFORM_SKIPPING: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAG_USE_CONSTRAINED_INTRAPREDICTION: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS = 64
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE_4x4: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE_8x8: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE_16x16: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE_32x32: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE = 3
class D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pH264Support: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_head)
        pHEVCSupport: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_head)
class D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264(EasyCastStructure):
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS
    DisableDeblockingFilterSupportedModes: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_NONE: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_CABAC_ENCODING_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_INTRA_SLICE_CONSTRAINED_ENCODING_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_BFRAME_LTR_COMBINED_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 4
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_ADAPTIVE_8x8_TRANSFORM_ENCODING_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 8
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_DIRECT_SPATIAL_ENCODING_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 16
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_DIRECT_TEMPORAL_ENCODING_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAG_CONSTRAINED_INTRAPREDICTION_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS = 64
class D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC(EasyCastStructure):
    SupportFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS
    MinLumaCodingUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE
    MaxLumaCodingUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE
    MinLumaTransformUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE
    MaxLumaTransformUnitSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE
    max_transform_hierarchy_depth_inter: Byte
    max_transform_hierarchy_depth_intra: Byte
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = Int32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_NONE: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 0
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_BFRAME_LTR_COMBINED_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 1
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_INTRA_SLICE_CONSTRAINED_ENCODING_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 2
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_CONSTRAINED_INTRAPREDICTION_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 4
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_SAO_FILTER_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 8
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_ASYMETRIC_MOTION_PARTITION_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 16
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_ASYMETRIC_MOTION_PARTITION_REQUIRED: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 32
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_TRANSFORM_SKIP_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 64
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_DISABLING_LOOP_FILTER_ACROSS_SLICES_SUPPORT: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 128
D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAG_P_FRAMES_IMPLEMENTED_AS_LOW_DELAY_B_FRAMES: D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS = 256
class D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pH264Support: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_H264_head)
        pHEVCSupport: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_HEVC_head)
class D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_H264(EasyCastStructure):
    MaxL0ReferencesForP: UInt32
    MaxL0ReferencesForB: UInt32
    MaxL1ReferencesForB: UInt32
    MaxLongTermReferences: UInt32
    MaxDPBCapacity: UInt32
class D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_HEVC(EasyCastStructure):
    MaxL0ReferencesForP: UInt32
    MaxL0ReferencesForB: UInt32
    MaxL1ReferencesForB: UInt32
    MaxLongTermReferences: UInt32
    MaxDPBCapacity: UInt32
class D3D12_VIDEO_ENCODER_COMPRESSED_BITSTREAM(EasyCastStructure):
    pBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    FrameStartOffset: UInt64
class D3D12_VIDEO_ENCODER_DESC(EasyCastStructure):
    NodeMask: UInt32
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_FLAGS
    EncodeCodec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    EncodeProfile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    InputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    CodecConfiguration: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION
    MaxMotionEstimationPrecision: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE
class D3D12_VIDEO_ENCODER_ENCODEFRAME_INPUT_ARGUMENTS(EasyCastStructure):
    SequenceControlDesc: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_DESC
    PictureControlDesc: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_DESC
    pInputFrame: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    InputFrameSubresource: UInt32
    CurrentFrameBitstreamMetadataSize: UInt32
class D3D12_VIDEO_ENCODER_ENCODEFRAME_OUTPUT_ARGUMENTS(EasyCastStructure):
    Bitstream: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_COMPRESSED_BITSTREAM
    ReconstructedPicture: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RECONSTRUCTED_PICTURE
    EncoderOutputMetadata: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_ENCODE_OPERATION_METADATA_BUFFER
D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS = Int32
D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAG_NO_ERROR: D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS = 0
D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAG_CODEC_PICTURE_CONTROL_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS = 1
D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAG_SUBREGION_LAYOUT_CONFIGURATION_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS = 2
D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAG_INVALID_REFERENCE_PICTURES: D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS = 4
D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAG_RECONFIGURATION_REQUEST_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS = 8
D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAG_INVALID_METADATA_BUFFER_SOURCE: D3D12_VIDEO_ENCODER_ENCODE_ERROR_FLAGS = 16
class D3D12_VIDEO_ENCODER_ENCODE_OPERATION_METADATA_BUFFER(EasyCastStructure):
    pBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    Offset: UInt64
D3D12_VIDEO_ENCODER_FLAGS = Int32
D3D12_VIDEO_ENCODER_FLAG_NONE: D3D12_VIDEO_ENCODER_FLAGS = 0
D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE = Int32
D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_FULL_FRAME: D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE = 0
D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_BYTES_PER_SUBREGION: D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE = 1
D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_SQUARE_UNITS_PER_SUBREGION_ROW_UNALIGNED: D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE = 2
D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_UNIFORM_PARTITIONING_ROWS_PER_SUBREGION: D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE = 3
D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_UNIFORM_PARTITIONING_SUBREGIONS_PER_FRAME: D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE = 4
class D3D12_VIDEO_ENCODER_FRAME_SUBREGION_METADATA(EasyCastStructure):
    bSize: UInt64
    bStartOffset: UInt64
    bHeaderSize: UInt64
D3D12_VIDEO_ENCODER_FRAME_TYPE_H264 = Int32
D3D12_VIDEO_ENCODER_FRAME_TYPE_H264_I_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_H264 = 0
D3D12_VIDEO_ENCODER_FRAME_TYPE_H264_P_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_H264 = 1
D3D12_VIDEO_ENCODER_FRAME_TYPE_H264_B_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_H264 = 2
D3D12_VIDEO_ENCODER_FRAME_TYPE_H264_IDR_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_H264 = 3
D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC = Int32
D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC_I_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC = 0
D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC_P_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC = 1
D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC_B_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC = 2
D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC_IDR_FRAME: D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC = 3
class D3D12_VIDEO_ENCODER_HEAP_DESC(EasyCastStructure):
    NodeMask: UInt32
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_HEAP_FLAGS
    EncodeCodec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    EncodeProfile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    EncodeLevel: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_SETTING
    ResolutionsListCount: UInt32
    pResolutionList: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC_head)
D3D12_VIDEO_ENCODER_HEAP_FLAGS = Int32
D3D12_VIDEO_ENCODER_HEAP_FLAG_NONE: D3D12_VIDEO_ENCODER_HEAP_FLAGS = 0
class D3D12_VIDEO_ENCODER_INTRA_REFRESH(EasyCastStructure):
    Mode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE
    IntraRefreshDuration: UInt32
D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE = Int32
D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE_NONE: D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE = 0
D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE_ROW_BASED: D3D12_VIDEO_ENCODER_INTRA_REFRESH_MODE = 1
D3D12_VIDEO_ENCODER_LEVELS_H264 = Int32
D3D12_VIDEO_ENCODER_LEVELS_H264_1: D3D12_VIDEO_ENCODER_LEVELS_H264 = 0
D3D12_VIDEO_ENCODER_LEVELS_H264_1b: D3D12_VIDEO_ENCODER_LEVELS_H264 = 1
D3D12_VIDEO_ENCODER_LEVELS_H264_11: D3D12_VIDEO_ENCODER_LEVELS_H264 = 2
D3D12_VIDEO_ENCODER_LEVELS_H264_12: D3D12_VIDEO_ENCODER_LEVELS_H264 = 3
D3D12_VIDEO_ENCODER_LEVELS_H264_13: D3D12_VIDEO_ENCODER_LEVELS_H264 = 4
D3D12_VIDEO_ENCODER_LEVELS_H264_2: D3D12_VIDEO_ENCODER_LEVELS_H264 = 5
D3D12_VIDEO_ENCODER_LEVELS_H264_21: D3D12_VIDEO_ENCODER_LEVELS_H264 = 6
D3D12_VIDEO_ENCODER_LEVELS_H264_22: D3D12_VIDEO_ENCODER_LEVELS_H264 = 7
D3D12_VIDEO_ENCODER_LEVELS_H264_3: D3D12_VIDEO_ENCODER_LEVELS_H264 = 8
D3D12_VIDEO_ENCODER_LEVELS_H264_31: D3D12_VIDEO_ENCODER_LEVELS_H264 = 9
D3D12_VIDEO_ENCODER_LEVELS_H264_32: D3D12_VIDEO_ENCODER_LEVELS_H264 = 10
D3D12_VIDEO_ENCODER_LEVELS_H264_4: D3D12_VIDEO_ENCODER_LEVELS_H264 = 11
D3D12_VIDEO_ENCODER_LEVELS_H264_41: D3D12_VIDEO_ENCODER_LEVELS_H264 = 12
D3D12_VIDEO_ENCODER_LEVELS_H264_42: D3D12_VIDEO_ENCODER_LEVELS_H264 = 13
D3D12_VIDEO_ENCODER_LEVELS_H264_5: D3D12_VIDEO_ENCODER_LEVELS_H264 = 14
D3D12_VIDEO_ENCODER_LEVELS_H264_51: D3D12_VIDEO_ENCODER_LEVELS_H264 = 15
D3D12_VIDEO_ENCODER_LEVELS_H264_52: D3D12_VIDEO_ENCODER_LEVELS_H264 = 16
D3D12_VIDEO_ENCODER_LEVELS_H264_6: D3D12_VIDEO_ENCODER_LEVELS_H264 = 17
D3D12_VIDEO_ENCODER_LEVELS_H264_61: D3D12_VIDEO_ENCODER_LEVELS_H264 = 18
D3D12_VIDEO_ENCODER_LEVELS_H264_62: D3D12_VIDEO_ENCODER_LEVELS_H264 = 19
D3D12_VIDEO_ENCODER_LEVELS_HEVC = Int32
D3D12_VIDEO_ENCODER_LEVELS_HEVC_1: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 0
D3D12_VIDEO_ENCODER_LEVELS_HEVC_2: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 1
D3D12_VIDEO_ENCODER_LEVELS_HEVC_21: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 2
D3D12_VIDEO_ENCODER_LEVELS_HEVC_3: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 3
D3D12_VIDEO_ENCODER_LEVELS_HEVC_31: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 4
D3D12_VIDEO_ENCODER_LEVELS_HEVC_4: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 5
D3D12_VIDEO_ENCODER_LEVELS_HEVC_41: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 6
D3D12_VIDEO_ENCODER_LEVELS_HEVC_5: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 7
D3D12_VIDEO_ENCODER_LEVELS_HEVC_51: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 8
D3D12_VIDEO_ENCODER_LEVELS_HEVC_52: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 9
D3D12_VIDEO_ENCODER_LEVELS_HEVC_6: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 10
D3D12_VIDEO_ENCODER_LEVELS_HEVC_61: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 11
D3D12_VIDEO_ENCODER_LEVELS_HEVC_62: D3D12_VIDEO_ENCODER_LEVELS_HEVC = 12
class D3D12_VIDEO_ENCODER_LEVEL_SETTING(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pH264LevelSetting: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVELS_H264)
        pHEVCLevelSetting: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_TIER_CONSTRAINTS_HEVC_head)
class D3D12_VIDEO_ENCODER_LEVEL_TIER_CONSTRAINTS_HEVC(EasyCastStructure):
    Level: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVELS_HEVC
    Tier: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_TIER_HEVC
D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE = Int32
D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE_MAXIMUM: D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE = 0
D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE_FULL_PIXEL: D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE = 1
D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE_HALF_PIXEL: D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE = 2
D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE_QUARTER_PIXEL: D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE = 3
class D3D12_VIDEO_ENCODER_OUTPUT_METADATA(EasyCastStructure):
    EncodeErrorFlags: UInt64
    EncodeStats: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_OUTPUT_METADATA_STATISTICS
    EncodedBitstreamWrittenBytesCount: UInt64
    WrittenSubregionsCount: UInt64
class D3D12_VIDEO_ENCODER_OUTPUT_METADATA_STATISTICS(EasyCastStructure):
    AverageQP: UInt64
    IntraCodingUnitsCount: UInt64
    InterCodingUnitsCount: UInt64
    SkipCodingUnitsCount: UInt64
    AverageMotionEstimationXDirection: UInt64
    AverageMotionEstimationYDirection: UInt64
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pH264PicData: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_head)
        pHEVCPicData: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_head)
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264(EasyCastStructure):
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAGS
    FrameType: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_FRAME_TYPE_H264
    pic_parameter_set_id: UInt32
    idr_pic_id: UInt32
    PictureOrderCountNumber: UInt32
    FrameDecodingOrderNumber: UInt32
    TemporalLayerIndex: UInt32
    List0ReferenceFramesCount: UInt32
    pList0ReferenceFrames: POINTER(UInt32)
    List1ReferenceFramesCount: UInt32
    pList1ReferenceFrames: POINTER(UInt32)
    ReferenceFramesReconPictureDescriptorsCount: UInt32
    pReferenceFramesReconPictureDescriptors: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_H264_head)
    adaptive_ref_pic_marking_mode_flag: Byte
    RefPicMarkingOperationsCommandsCount: UInt32
    pRefPicMarkingOperationsCommands: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_MARKING_OPERATION_head)
    List0RefPicModificationsCount: UInt32
    pList0RefPicModifications: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_LIST_MODIFICATION_OPERATION_head)
    List1RefPicModificationsCount: UInt32
    pList1RefPicModifications: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_LIST_MODIFICATION_OPERATION_head)
    QPMapValuesCount: UInt32
    pRateControlQPMap: POINTER(SByte)
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAGS = Int32
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAG_NONE: D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAGS = 0
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAG_REQUEST_INTRA_CONSTRAINED_SLICES: D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAGS = 1
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_LIST_MODIFICATION_OPERATION(EasyCastStructure):
    modification_of_pic_nums_idc: Byte
    abs_diff_pic_num_minus1: UInt32
    long_term_pic_num: UInt32
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_MARKING_OPERATION(EasyCastStructure):
    memory_management_control_operation: Byte
    difference_of_pic_nums_minus1: UInt32
    long_term_pic_num: UInt32
    long_term_frame_idx: UInt32
    max_long_term_frame_idx_plus1: UInt32
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC(EasyCastStructure):
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAGS
    FrameType: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_FRAME_TYPE_HEVC
    slice_pic_parameter_set_id: UInt32
    PictureOrderCountNumber: UInt32
    TemporalLayerIndex: UInt32
    List0ReferenceFramesCount: UInt32
    pList0ReferenceFrames: POINTER(UInt32)
    List1ReferenceFramesCount: UInt32
    pList1ReferenceFrames: POINTER(UInt32)
    ReferenceFramesReconPictureDescriptorsCount: UInt32
    pReferenceFramesReconPictureDescriptors: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_HEVC_head)
    List0RefPicModificationsCount: UInt32
    pList0RefPicModifications: POINTER(UInt32)
    List1RefPicModificationsCount: UInt32
    pList1RefPicModifications: POINTER(UInt32)
    QPMapValuesCount: UInt32
    pRateControlQPMap: POINTER(SByte)
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAGS = Int32
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAG_NONE: D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAGS = 0
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAG_REQUEST_INTRA_CONSTRAINED_SLICES: D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAGS = 1
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_DESC(EasyCastStructure):
    IntraRefreshFrameIndex: UInt32
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_FLAGS
    PictureControlCodecData: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA
    ReferenceFrames: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODE_REFERENCE_FRAMES
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_FLAGS = Int32
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_FLAG_NONE: D3D12_VIDEO_ENCODER_PICTURE_CONTROL_FLAGS = 0
D3D12_VIDEO_ENCODER_PICTURE_CONTROL_FLAG_USED_AS_REFERENCE_PICTURE: D3D12_VIDEO_ENCODER_PICTURE_CONTROL_FLAGS = 1
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pSlicesPartition_H264: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_SLICES_head)
        pSlicesPartition_HEVC: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_SLICES_head)
class D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_SLICES(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        MaxBytesPerSlice: UInt32
        NumberOfCodingUnitsPerSlice: UInt32
        NumberOfRowsPerSlice: UInt32
        NumberOfSlicesPerFrame: UInt32
class D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC(EasyCastStructure):
    Width: UInt32
    Height: UInt32
class D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_RATIO_DESC(EasyCastStructure):
    WidthRatio: UInt32
    HeightRatio: UInt32
class D3D12_VIDEO_ENCODER_PROFILE_DESC(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pH264Profile: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_H264)
        pHEVCProfile: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_HEVC)
D3D12_VIDEO_ENCODER_PROFILE_H264 = Int32
D3D12_VIDEO_ENCODER_PROFILE_H264_MAIN: D3D12_VIDEO_ENCODER_PROFILE_H264 = 0
D3D12_VIDEO_ENCODER_PROFILE_H264_HIGH: D3D12_VIDEO_ENCODER_PROFILE_H264 = 1
D3D12_VIDEO_ENCODER_PROFILE_H264_HIGH_10: D3D12_VIDEO_ENCODER_PROFILE_H264 = 2
D3D12_VIDEO_ENCODER_PROFILE_HEVC = Int32
D3D12_VIDEO_ENCODER_PROFILE_HEVC_MAIN: D3D12_VIDEO_ENCODER_PROFILE_HEVC = 0
D3D12_VIDEO_ENCODER_PROFILE_HEVC_MAIN10: D3D12_VIDEO_ENCODER_PROFILE_HEVC = 1
class D3D12_VIDEO_ENCODER_RATE_CONTROL(EasyCastStructure):
    Mode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS
    ConfigParams: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_CONFIGURATION_PARAMS
    TargetFrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
class D3D12_VIDEO_ENCODER_RATE_CONTROL_CBR(EasyCastStructure):
    InitialQP: UInt32
    MinQP: UInt32
    MaxQP: UInt32
    MaxFrameBitSize: UInt64
    TargetBitRate: UInt64
    VBVCapacity: UInt64
    InitialVBVFullness: UInt64
class D3D12_VIDEO_ENCODER_RATE_CONTROL_CONFIGURATION_PARAMS(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pConfiguration_CQP: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_CQP_head)
        pConfiguration_CBR: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_CBR_head)
        pConfiguration_VBR: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_VBR_head)
        pConfiguration_QVBR: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL_QVBR_head)
class D3D12_VIDEO_ENCODER_RATE_CONTROL_CQP(EasyCastStructure):
    ConstantQP_FullIntracodedFrame: UInt32
    ConstantQP_InterPredictedFrame_PrevRefOnly: UInt32
    ConstantQP_InterPredictedFrame_BiDirectionalRef: UInt32
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = Int32
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAG_NONE: D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = 0
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAG_ENABLE_DELTA_QP: D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = 1
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAG_ENABLE_FRAME_ANALYSIS: D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = 2
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAG_ENABLE_QP_RANGE: D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = 4
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAG_ENABLE_INITIAL_QP: D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = 8
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAG_ENABLE_MAX_FRAME_SIZE: D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = 16
D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAG_ENABLE_VBV_SIZES: D3D12_VIDEO_ENCODER_RATE_CONTROL_FLAGS = 32
D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE = Int32
D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE_ABSOLUTE_QP_MAP: D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE = 0
D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE_CQP: D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE = 1
D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE_CBR: D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE = 2
D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE_VBR: D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE = 3
D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE_QVBR: D3D12_VIDEO_ENCODER_RATE_CONTROL_MODE = 4
class D3D12_VIDEO_ENCODER_RATE_CONTROL_QVBR(EasyCastStructure):
    InitialQP: UInt32
    MinQP: UInt32
    MaxQP: UInt32
    MaxFrameBitSize: UInt64
    TargetAvgBitRate: UInt64
    PeakBitRate: UInt64
    ConstantQualityTarget: UInt32
class D3D12_VIDEO_ENCODER_RATE_CONTROL_VBR(EasyCastStructure):
    InitialQP: UInt32
    MinQP: UInt32
    MaxQP: UInt32
    MaxFrameBitSize: UInt64
    TargetAvgBitRate: UInt64
    PeakBitRate: UInt64
    VBVCapacity: UInt64
    InitialVBVFullness: UInt64
class D3D12_VIDEO_ENCODER_RECONSTRUCTED_PICTURE(EasyCastStructure):
    pReconstructedPicture: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    ReconstructedPictureSubresource: UInt32
class D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_H264(EasyCastStructure):
    ReconstructedPictureResourceIndex: UInt32
    IsLongTermReference: Windows.Win32.Foundation.BOOL
    LongTermPictureIdx: UInt32
    PictureOrderCountNumber: UInt32
    FrameDecodingOrderNumber: UInt32
    TemporalLayerIndex: UInt32
class D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_HEVC(EasyCastStructure):
    ReconstructedPictureResourceIndex: UInt32
    IsRefUsedByCurrentPic: Windows.Win32.Foundation.BOOL
    IsLongTermReference: Windows.Win32.Foundation.BOOL
    PictureOrderCountNumber: UInt32
    TemporalLayerIndex: UInt32
class D3D12_VIDEO_ENCODER_RESOLVE_METADATA_INPUT_ARGUMENTS(EasyCastStructure):
    EncoderCodec: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC
    EncoderProfile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC
    EncoderInputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    EncodedPictureEffectiveResolution: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC
    HWLayoutMetadata: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_ENCODE_OPERATION_METADATA_BUFFER
class D3D12_VIDEO_ENCODER_RESOLVE_METADATA_OUTPUT_ARGUMENTS(EasyCastStructure):
    ResolvedLayoutMetadata: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_ENCODE_OPERATION_METADATA_BUFFER
class D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_DESC(EasyCastStructure):
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS
    IntraRefreshConfig: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_INTRA_REFRESH
    RateControl: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RATE_CONTROL
    PictureTargetResolution: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC
    SelectedLayoutMode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE
    FrameSubregionsLayoutData: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA
    CodecGopSequence: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE
D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS = Int32
D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAG_NONE: D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS = 0
D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAG_RESOLUTION_CHANGE: D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS = 1
D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAG_RATE_CONTROL_CHANGE: D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS = 2
D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAG_SUBREGION_LAYOUT_CHANGE: D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS = 4
D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAG_REQUEST_INTRA_REFRESH: D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS = 8
D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAG_GOP_SEQUENCE_CHANGE: D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS = 16
class D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE(EasyCastStructure):
    DataSize: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pH264GroupOfPictures: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_H264_head)
        pHEVCGroupOfPictures: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_HEVC_head)
class D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_H264(EasyCastStructure):
    GOPLength: UInt32
    PPicturePeriod: UInt32
    pic_order_cnt_type: Byte
    log2_max_frame_num_minus4: Byte
    log2_max_pic_order_cnt_lsb_minus4: Byte
class D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_HEVC(EasyCastStructure):
    GOPLength: UInt32
    PPicturePeriod: UInt32
    log2_max_pic_order_cnt_lsb_minus4: Byte
D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = Int32
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_NONE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 0
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_GENERAL_SUPPORT_OK: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 1
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RATE_CONTROL_RECONFIGURATION_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 2
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RESOLUTION_RECONFIGURATION_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 4
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RATE_CONTROL_VBV_SIZE_CONFIG_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 8
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RATE_CONTROL_FRAME_ANALYSIS_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 16
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RECONSTRUCTED_FRAMES_REQUIRE_TEXTURE_ARRAYS: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 32
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RATE_CONTROL_DELTA_QP_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 64
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_SUBREGION_LAYOUT_RECONFIGURATION_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 128
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RATE_CONTROL_ADJUSTABLE_QP_RANGE_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 256
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RATE_CONTROL_INITIAL_QP_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 512
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RATE_CONTROL_MAX_FRAME_SIZE_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 1024
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_SEQUENCE_GOP_RECONFIGURATION_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 2048
D3D12_VIDEO_ENCODER_SUPPORT_FLAG_MOTION_ESTIMATION_PRECISION_MODE_LIMIT_AVAILABLE: D3D12_VIDEO_ENCODER_SUPPORT_FLAGS = 4096
D3D12_VIDEO_ENCODER_TIER_HEVC = Int32
D3D12_VIDEO_ENCODER_TIER_HEVC_MAIN: D3D12_VIDEO_ENCODER_TIER_HEVC = 0
D3D12_VIDEO_ENCODER_TIER_HEVC_HIGH: D3D12_VIDEO_ENCODER_TIER_HEVC = 1
D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = Int32
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_NONE: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 0
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_CODEC_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 1
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_INPUT_FORMAT_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 8
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_CODEC_CONFIGURATION_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 16
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_RATE_CONTROL_MODE_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 32
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_RATE_CONTROL_CONFIGURATION_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 64
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_INTRA_REFRESH_MODE_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 128
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_SUBREGION_LAYOUT_MODE_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 256
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_RESOLUTION_NOT_SUPPORTED_IN_LIST: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 512
D3D12_VIDEO_ENCODER_VALIDATION_FLAG_GOP_STRUCTURE_NOT_SUPPORTED: D3D12_VIDEO_ENCODER_VALIDATION_FLAGS = 2048
class D3D12_VIDEO_ENCODE_REFERENCE_FRAMES(EasyCastStructure):
    NumTexture2Ds: UInt32
    ppTexture2Ds: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)
    pSubresources: POINTER(UInt32)
class D3D12_VIDEO_EXTENSION_COMMAND_DESC(EasyCastStructure):
    NodeMask: UInt32
    CommandId: Guid
class D3D12_VIDEO_EXTENSION_COMMAND_INFO(EasyCastStructure):
    CommandId: Guid
    Name: Windows.Win32.Foundation.PWSTR
    CommandListSupportFlags: Windows.Win32.Graphics.Direct3D12.D3D12_COMMAND_LIST_SUPPORT_FLAGS
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAGS = Int32
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAG_NONE: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAGS = 0
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAG_READ: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAGS = 1
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAG_WRITE: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAGS = 2
class D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_INFO(EasyCastStructure):
    Name: Windows.Win32.Foundation.PWSTR
    Type: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_FLAGS
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = Int32
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE_CREATION: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = 0
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE_INITIALIZATION: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = 1
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE_EXECUTION: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = 2
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE_CAPS_INPUT: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = 3
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE_CAPS_OUTPUT: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = 4
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE_DEVICE_EXECUTE_INPUT: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = 5
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE_DEVICE_EXECUTE_OUTPUT: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_STAGE = 6
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = Int32
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_UINT8: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 0
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_UINT16: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 1
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_UINT32: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 2
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_UINT64: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 3
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_SINT8: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 4
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_SINT16: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 5
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_SINT32: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 6
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_SINT64: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 7
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_FLOAT: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 8
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_DOUBLE: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 9
D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE_RESOURCE: D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_TYPE = 10
D3D12_VIDEO_FIELD_TYPE = Int32
D3D12_VIDEO_FIELD_TYPE_NONE: D3D12_VIDEO_FIELD_TYPE = 0
D3D12_VIDEO_FIELD_TYPE_INTERLACED_TOP_FIELD_FIRST: D3D12_VIDEO_FIELD_TYPE = 1
D3D12_VIDEO_FIELD_TYPE_INTERLACED_BOTTOM_FIELD_FIRST: D3D12_VIDEO_FIELD_TYPE = 2
class D3D12_VIDEO_FORMAT(EasyCastStructure):
    Format: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    ColorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE = Int32
D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE_NONE: D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE = 0
D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE_FIELD_BASED: D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE = 1
D3D12_VIDEO_FRAME_STEREO_FORMAT = Int32
D3D12_VIDEO_FRAME_STEREO_FORMAT_NONE: D3D12_VIDEO_FRAME_STEREO_FORMAT = 0
D3D12_VIDEO_FRAME_STEREO_FORMAT_MONO: D3D12_VIDEO_FRAME_STEREO_FORMAT = 1
D3D12_VIDEO_FRAME_STEREO_FORMAT_HORIZONTAL: D3D12_VIDEO_FRAME_STEREO_FORMAT = 2
D3D12_VIDEO_FRAME_STEREO_FORMAT_VERTICAL: D3D12_VIDEO_FRAME_STEREO_FORMAT = 3
D3D12_VIDEO_FRAME_STEREO_FORMAT_SEPARATE: D3D12_VIDEO_FRAME_STEREO_FORMAT = 4
class D3D12_VIDEO_MOTION_ESTIMATOR_DESC(EasyCastStructure):
    NodeMask: UInt32
    InputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    BlockSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE
    Precision: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION
    SizeRange: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SIZE_RANGE
class D3D12_VIDEO_MOTION_ESTIMATOR_INPUT(EasyCastStructure):
    pInputTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    InputSubresourceIndex: UInt32
    pReferenceTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    ReferenceSubresourceIndex: UInt32
    pHintMotionVectorHeap: Windows.Win32.Media.MediaFoundation.ID3D12VideoMotionVectorHeap_head
class D3D12_VIDEO_MOTION_ESTIMATOR_OUTPUT(EasyCastStructure):
    pMotionVectorHeap: Windows.Win32.Media.MediaFoundation.ID3D12VideoMotionVectorHeap_head
D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE = Int32
D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_8X8: D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE = 0
D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_16X16: D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE = 1
D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAGS = Int32
D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAG_NONE: D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAGS = 0
D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAG_8X8: D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAGS = 1
D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAG_16X16: D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE_FLAGS = 2
D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION = Int32
D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_QUARTER_PEL: D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION = 0
D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_FLAGS = Int32
D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_FLAG_NONE: D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_FLAGS = 0
D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_FLAG_QUARTER_PEL: D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION_FLAGS = 1
class D3D12_VIDEO_MOTION_VECTOR_HEAP_DESC(EasyCastStructure):
    NodeMask: UInt32
    InputFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    BlockSize: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_SEARCH_BLOCK_SIZE
    Precision: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_VECTOR_PRECISION
    SizeRange: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SIZE_RANGE
class D3D12_VIDEO_PROCESS_ALPHA_BLENDING(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    Alpha: Single
D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE = Int32
D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_OPAQUE: D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE = 0
D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_BACKGROUND: D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE = 1
D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_DESTINATION: D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE = 2
D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_SOURCE_STREAM: D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE = 3
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = UInt32
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_NONE: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 0
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_DENOISE: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 1
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_DERINGING: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 2
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_EDGE_ENHANCEMENT: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 4
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_COLOR_CORRECTION: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 8
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_FLESH_TONE_MAPPING: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 16
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_IMAGE_STABILIZATION: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 32
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_SUPER_RESOLUTION: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 64
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_ANAMORPHIC_SCALING: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 128
D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_CUSTOM: D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS = 2147483648
D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS = UInt32
D3D12_VIDEO_PROCESS_DEINTERLACE_FLAG_NONE: D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS = 0
D3D12_VIDEO_PROCESS_DEINTERLACE_FLAG_BOB: D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS = 1
D3D12_VIDEO_PROCESS_DEINTERLACE_FLAG_CUSTOM: D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS = 2147483648
D3D12_VIDEO_PROCESS_FEATURE_FLAGS = Int32
D3D12_VIDEO_PROCESS_FEATURE_FLAG_NONE: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 0
D3D12_VIDEO_PROCESS_FEATURE_FLAG_ALPHA_FILL: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 1
D3D12_VIDEO_PROCESS_FEATURE_FLAG_LUMA_KEY: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 2
D3D12_VIDEO_PROCESS_FEATURE_FLAG_STEREO: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 4
D3D12_VIDEO_PROCESS_FEATURE_FLAG_ROTATION: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 8
D3D12_VIDEO_PROCESS_FEATURE_FLAG_FLIP: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 16
D3D12_VIDEO_PROCESS_FEATURE_FLAG_ALPHA_BLENDING: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 32
D3D12_VIDEO_PROCESS_FEATURE_FLAG_PIXEL_ASPECT_RATIO: D3D12_VIDEO_PROCESS_FEATURE_FLAGS = 64
D3D12_VIDEO_PROCESS_FILTER = Int32
D3D12_VIDEO_PROCESS_FILTER_BRIGHTNESS: D3D12_VIDEO_PROCESS_FILTER = 0
D3D12_VIDEO_PROCESS_FILTER_CONTRAST: D3D12_VIDEO_PROCESS_FILTER = 1
D3D12_VIDEO_PROCESS_FILTER_HUE: D3D12_VIDEO_PROCESS_FILTER = 2
D3D12_VIDEO_PROCESS_FILTER_SATURATION: D3D12_VIDEO_PROCESS_FILTER = 3
D3D12_VIDEO_PROCESS_FILTER_NOISE_REDUCTION: D3D12_VIDEO_PROCESS_FILTER = 4
D3D12_VIDEO_PROCESS_FILTER_EDGE_ENHANCEMENT: D3D12_VIDEO_PROCESS_FILTER = 5
D3D12_VIDEO_PROCESS_FILTER_ANAMORPHIC_SCALING: D3D12_VIDEO_PROCESS_FILTER = 6
D3D12_VIDEO_PROCESS_FILTER_STEREO_ADJUSTMENT: D3D12_VIDEO_PROCESS_FILTER = 7
D3D12_VIDEO_PROCESS_FILTER_FLAGS = Int32
D3D12_VIDEO_PROCESS_FILTER_FLAG_NONE: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 0
D3D12_VIDEO_PROCESS_FILTER_FLAG_BRIGHTNESS: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 1
D3D12_VIDEO_PROCESS_FILTER_FLAG_CONTRAST: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 2
D3D12_VIDEO_PROCESS_FILTER_FLAG_HUE: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 4
D3D12_VIDEO_PROCESS_FILTER_FLAG_SATURATION: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 8
D3D12_VIDEO_PROCESS_FILTER_FLAG_NOISE_REDUCTION: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 16
D3D12_VIDEO_PROCESS_FILTER_FLAG_EDGE_ENHANCEMENT: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 32
D3D12_VIDEO_PROCESS_FILTER_FLAG_ANAMORPHIC_SCALING: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 64
D3D12_VIDEO_PROCESS_FILTER_FLAG_STEREO_ADJUSTMENT: D3D12_VIDEO_PROCESS_FILTER_FLAGS = 128
class D3D12_VIDEO_PROCESS_FILTER_RANGE(EasyCastStructure):
    Minimum: Int32
    Maximum: Int32
    Default: Int32
    Multiplier: Single
class D3D12_VIDEO_PROCESS_INPUT_STREAM(EasyCastStructure):
    pTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    Subresource: UInt32
    ReferenceSet: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_REFERENCE_SET
class D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS(EasyCastStructure):
    InputStream: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM * 2
    Transform: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_TRANSFORM
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS
    RateInfo: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE
    FilterLevels: Int32 * 32
    AlphaBlending: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_ALPHA_BLENDING
class D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS1(EasyCastStructure):
    InputStream: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM * 2
    Transform: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_TRANSFORM
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS
    RateInfo: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE
    FilterLevels: Int32 * 32
    AlphaBlending: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_ALPHA_BLENDING
    FieldType: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FIELD_TYPE
class D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC(EasyCastStructure):
    Format: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    ColorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
    SourceAspectRatio: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    DestinationAspectRatio: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    FrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    SourceSizeRange: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SIZE_RANGE
    DestinationSizeRange: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SIZE_RANGE
    EnableOrientation: Windows.Win32.Foundation.BOOL
    FilterFlags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_FILTER_FLAGS
    StereoFormat: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FRAME_STEREO_FORMAT
    FieldType: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FIELD_TYPE
    DeinterlaceMode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS
    EnableAlphaBlending: Windows.Win32.Foundation.BOOL
    LumaKey: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_LUMA_KEY
    NumPastFrames: UInt32
    NumFutureFrames: UInt32
    EnableAutoProcessing: Windows.Win32.Foundation.BOOL
D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS = Int32
D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAG_NONE: D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS = 0
D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAG_FRAME_DISCONTINUITY: D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS = 1
D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAG_FRAME_REPEAT: D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS = 2
class D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE(EasyCastStructure):
    OutputIndex: UInt32
    InputFrameOrField: UInt32
class D3D12_VIDEO_PROCESS_LUMA_KEY(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    Lower: Single
    Upper: Single
D3D12_VIDEO_PROCESS_ORIENTATION = Int32
D3D12_VIDEO_PROCESS_ORIENTATION_DEFAULT: D3D12_VIDEO_PROCESS_ORIENTATION = 0
D3D12_VIDEO_PROCESS_ORIENTATION_FLIP_HORIZONTAL: D3D12_VIDEO_PROCESS_ORIENTATION = 1
D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_90: D3D12_VIDEO_PROCESS_ORIENTATION = 2
D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_90_FLIP_HORIZONTAL: D3D12_VIDEO_PROCESS_ORIENTATION = 3
D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_180: D3D12_VIDEO_PROCESS_ORIENTATION = 4
D3D12_VIDEO_PROCESS_ORIENTATION_FLIP_VERTICAL: D3D12_VIDEO_PROCESS_ORIENTATION = 5
D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_270: D3D12_VIDEO_PROCESS_ORIENTATION = 6
D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_270_FLIP_HORIZONTAL: D3D12_VIDEO_PROCESS_ORIENTATION = 7
class D3D12_VIDEO_PROCESS_OUTPUT_STREAM(EasyCastStructure):
    pTexture2D: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
    Subresource: UInt32
class D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS(EasyCastStructure):
    OutputStream: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM * 2
    TargetRectangle: Windows.Win32.Foundation.RECT
class D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC(EasyCastStructure):
    Format: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    ColorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
    AlphaFillMode: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE
    AlphaFillModeSourceStreamIndex: UInt32
    BackgroundColor: Single * 4
    FrameRate: Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    EnableStereo: Windows.Win32.Foundation.BOOL
class D3D12_VIDEO_PROCESS_REFERENCE_SET(EasyCastStructure):
    NumPastFrames: UInt32
    ppPastFrames: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)
    pPastSubresources: POINTER(UInt32)
    NumFutureFrames: UInt32
    ppFutureFrames: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)
    pFutureSubresources: POINTER(UInt32)
D3D12_VIDEO_PROCESS_SUPPORT_FLAGS = Int32
D3D12_VIDEO_PROCESS_SUPPORT_FLAG_NONE: D3D12_VIDEO_PROCESS_SUPPORT_FLAGS = 0
D3D12_VIDEO_PROCESS_SUPPORT_FLAG_SUPPORTED: D3D12_VIDEO_PROCESS_SUPPORT_FLAGS = 1
class D3D12_VIDEO_PROCESS_TRANSFORM(EasyCastStructure):
    SourceRectangle: Windows.Win32.Foundation.RECT
    DestinationRectangle: Windows.Win32.Foundation.RECT
    Orientation: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_ORIENTATION
D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAGS = Int32
D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAG_NONE: D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAGS = 0
D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAG_SUPPORTED: D3D12_VIDEO_PROTECTED_RESOURCE_SUPPORT_FLAGS = 1
class D3D12_VIDEO_SAMPLE(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    Format: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_FORMAT
class D3D12_VIDEO_SCALE_SUPPORT(EasyCastStructure):
    OutputSizeRange: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SIZE_RANGE
    Flags: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_SCALE_SUPPORT_FLAGS
D3D12_VIDEO_SCALE_SUPPORT_FLAGS = Int32
D3D12_VIDEO_SCALE_SUPPORT_FLAG_NONE: D3D12_VIDEO_SCALE_SUPPORT_FLAGS = 0
D3D12_VIDEO_SCALE_SUPPORT_FLAG_POW2_ONLY: D3D12_VIDEO_SCALE_SUPPORT_FLAGS = 1
D3D12_VIDEO_SCALE_SUPPORT_FLAG_EVEN_DIMENSIONS_ONLY: D3D12_VIDEO_SCALE_SUPPORT_FLAGS = 2
class D3D12_VIDEO_SIZE_RANGE(EasyCastStructure):
    MaxWidth: UInt32
    MaxHeight: UInt32
    MinWidth: UInt32
    MinHeight: UInt32
if ARCH in 'X64,ARM64':
    class D3DCONTENTPROTECTIONCAPS(EasyCastStructure):
        Caps: UInt32
        KeyExchangeType: Guid
        BufferAlignmentStart: UInt32
        BlockAlignmentSize: UInt32
        ProtectedMemorySize: UInt64
if ARCH in 'X86':
    class D3DCONTENTPROTECTIONCAPS(EasyCastStructure):
        Caps: UInt32
        KeyExchangeType: Guid
        BufferAlignmentStart: UInt32
        BlockAlignmentSize: UInt32
        ProtectedMemorySize: UInt64
        _pack_ = 4
class D3DOVERLAYCAPS(EasyCastStructure):
    Caps: UInt32
    MaxOverlayDisplayWidth: UInt32
    MaxOverlayDisplayHeight: UInt32
class DEVICE_INFO(EasyCastStructure):
    pFriendlyDeviceName: Windows.Win32.Foundation.BSTR
    pUniqueDeviceName: Windows.Win32.Foundation.BSTR
    pManufacturerName: Windows.Win32.Foundation.BSTR
    pModelName: Windows.Win32.Foundation.BSTR
    pIconURL: Windows.Win32.Foundation.BSTR
class DIRTYRECT_INFO(EasyCastStructure):
    FrameNumber: UInt32
    NumDirtyRects: UInt32
    DirtyRects: Windows.Win32.Foundation.RECT * 1
class DXVA2_AES_CTR_IV(EasyCastStructure):
    IV: UInt64
    Count: UInt64
class DXVA2_AYUVSample16(EasyCastStructure):
    Cr: UInt16
    Cb: UInt16
    Y: UInt16
    Alpha: UInt16
class DXVA2_AYUVSample8(EasyCastStructure):
    Cr: Byte
    Cb: Byte
    Y: Byte
    Alpha: Byte
DXVA2_BufferfType = Int32
DXVA2_PictureParametersBufferType: DXVA2_BufferfType = 0
DXVA2_MacroBlockControlBufferType: DXVA2_BufferfType = 1
DXVA2_ResidualDifferenceBufferType: DXVA2_BufferfType = 2
DXVA2_DeblockingControlBufferType: DXVA2_BufferfType = 3
DXVA2_InverseQuantizationMatrixBufferType: DXVA2_BufferfType = 4
DXVA2_SliceControlBufferType: DXVA2_BufferfType = 5
DXVA2_BitStreamDateBufferType: DXVA2_BufferfType = 6
DXVA2_MotionVectorBuffer: DXVA2_BufferfType = 7
DXVA2_FilmGrainBuffer: DXVA2_BufferfType = 8
class DXVA2_ConfigPictureDecode(EasyCastStructure):
    guidConfigBitstreamEncryption: Guid
    guidConfigMBcontrolEncryption: Guid
    guidConfigResidDiffEncryption: Guid
    ConfigBitstreamRaw: UInt32
    ConfigMBcontrolRasterOrder: UInt32
    ConfigResidDiffHost: UInt32
    ConfigSpatialResid8: UInt32
    ConfigResid8Subtraction: UInt32
    ConfigSpatialHost8or9Clipping: UInt32
    ConfigSpatialResidInterleaved: UInt32
    ConfigIntraResidUnsigned: UInt32
    ConfigResidDiffAccelerator: UInt32
    ConfigHostInverseScan: UInt32
    ConfigSpecificIDCT: UInt32
    Config4GroupedCoefs: UInt32
    ConfigMinRenderTargetBuffCount: UInt16
    ConfigDecoderSpecific: UInt16
class DXVA2_DecodeBufferDesc(EasyCastStructure):
    CompressedBufferType: Windows.Win32.Media.MediaFoundation.DXVA2_BufferfType
    BufferIndex: UInt32
    DataOffset: UInt32
    DataSize: UInt32
    FirstMBaddress: UInt32
    NumMBsInBuffer: UInt32
    Width: UInt32
    Height: UInt32
    Stride: UInt32
    ReservedBits: UInt32
    pvPVPState: c_void_p
class DXVA2_DecodeExecuteParams(EasyCastStructure):
    NumCompBuffers: UInt32
    pCompressedBuffers: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_DecodeBufferDesc_head)
    pExtensionData: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_DecodeExtensionData_head)
class DXVA2_DecodeExtensionData(EasyCastStructure):
    Function: UInt32
    pPrivateInputData: c_void_p
    PrivateInputDataSize: UInt32
    pPrivateOutputData: c_void_p
    PrivateOutputDataSize: UInt32
DXVA2_DeinterlaceTech = Int32
DXVA2_DeinterlaceTech_Unknown: DXVA2_DeinterlaceTech = 0
DXVA2_DeinterlaceTech_BOBLineReplicate: DXVA2_DeinterlaceTech = 1
DXVA2_DeinterlaceTech_BOBVerticalStretch: DXVA2_DeinterlaceTech = 2
DXVA2_DeinterlaceTech_BOBVerticalStretch4Tap: DXVA2_DeinterlaceTech = 4
DXVA2_DeinterlaceTech_MedianFiltering: DXVA2_DeinterlaceTech = 8
DXVA2_DeinterlaceTech_EdgeFiltering: DXVA2_DeinterlaceTech = 16
DXVA2_DeinterlaceTech_FieldAdaptive: DXVA2_DeinterlaceTech = 32
DXVA2_DeinterlaceTech_PixelAdaptive: DXVA2_DeinterlaceTech = 64
DXVA2_DeinterlaceTech_MotionVectorSteered: DXVA2_DeinterlaceTech = 128
DXVA2_DeinterlaceTech_InverseTelecine: DXVA2_DeinterlaceTech = 256
DXVA2_DeinterlaceTech_Mask: DXVA2_DeinterlaceTech = 511
DXVA2_DestData = Int32
DXVA2_DestData_RFF: DXVA2_DestData = 1
DXVA2_DestData_TFF: DXVA2_DestData = 2
DXVA2_DestData_RFF_TFF_Present: DXVA2_DestData = 4
DXVA2_DestData_Mask: DXVA2_DestData = 65535
DXVA2_DetailFilterTech = Int32
DXVA2_DetailFilterTech_Unsupported: DXVA2_DetailFilterTech = 0
DXVA2_DetailFilterTech_Unknown: DXVA2_DetailFilterTech = 1
DXVA2_DetailFilterTech_Edge: DXVA2_DetailFilterTech = 2
DXVA2_DetailFilterTech_Sharpening: DXVA2_DetailFilterTech = 4
DXVA2_DetailFilterTech_Mask: DXVA2_DetailFilterTech = 7
class DXVA2_ExtendedFormat(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        value: UInt32
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
DXVA2_FilterType = Int32
DXVA2_NoiseFilterLumaLevel: DXVA2_FilterType = 1
DXVA2_NoiseFilterLumaThreshold: DXVA2_FilterType = 2
DXVA2_NoiseFilterLumaRadius: DXVA2_FilterType = 3
DXVA2_NoiseFilterChromaLevel: DXVA2_FilterType = 4
DXVA2_NoiseFilterChromaThreshold: DXVA2_FilterType = 5
DXVA2_NoiseFilterChromaRadius: DXVA2_FilterType = 6
DXVA2_DetailFilterLumaLevel: DXVA2_FilterType = 7
DXVA2_DetailFilterLumaThreshold: DXVA2_FilterType = 8
DXVA2_DetailFilterLumaRadius: DXVA2_FilterType = 9
DXVA2_DetailFilterChromaLevel: DXVA2_FilterType = 10
DXVA2_DetailFilterChromaThreshold: DXVA2_FilterType = 11
DXVA2_DetailFilterChromaRadius: DXVA2_FilterType = 12
class DXVA2_FilterValues(EasyCastStructure):
    Level: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    Threshold: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    Radius: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
class DXVA2_Fixed32(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        ll: Int32
        class _Anonymous_e__Struct(EasyCastStructure):
            Fraction: UInt16
            Value: Int16
class DXVA2_Frequency(EasyCastStructure):
    Numerator: UInt32
    Denominator: UInt32
DXVA2_NoiseFilterTech = Int32
DXVA2_NoiseFilterTech_Unsupported: DXVA2_NoiseFilterTech = 0
DXVA2_NoiseFilterTech_Unknown: DXVA2_NoiseFilterTech = 1
DXVA2_NoiseFilterTech_Median: DXVA2_NoiseFilterTech = 2
DXVA2_NoiseFilterTech_Temporal: DXVA2_NoiseFilterTech = 4
DXVA2_NoiseFilterTech_BlockNoise: DXVA2_NoiseFilterTech = 8
DXVA2_NoiseFilterTech_MosquitoNoise: DXVA2_NoiseFilterTech = 16
DXVA2_NoiseFilterTech_Mask: DXVA2_NoiseFilterTech = 31
DXVA2_NominalRange = Int32
DXVA2_NominalRangeMask: DXVA2_NominalRange = 7
DXVA2_NominalRange_Unknown: DXVA2_NominalRange = 0
DXVA2_NominalRange_Normal: DXVA2_NominalRange = 1
DXVA2_NominalRange_Wide: DXVA2_NominalRange = 2
DXVA2_NominalRange_0_255: DXVA2_NominalRange = 1
DXVA2_NominalRange_16_235: DXVA2_NominalRange = 2
DXVA2_NominalRange_48_208: DXVA2_NominalRange = 3
DXVA2_ProcAmp = Int32
DXVA2_ProcAmp_None: DXVA2_ProcAmp = 0
DXVA2_ProcAmp_Brightness: DXVA2_ProcAmp = 1
DXVA2_ProcAmp_Contrast: DXVA2_ProcAmp = 2
DXVA2_ProcAmp_Hue: DXVA2_ProcAmp = 4
DXVA2_ProcAmp_Saturation: DXVA2_ProcAmp = 8
DXVA2_ProcAmp_Mask: DXVA2_ProcAmp = 15
class DXVA2_ProcAmpValues(EasyCastStructure):
    Brightness: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    Contrast: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    Hue: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    Saturation: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
DXVA2_SampleData = Int32
DXVA2_SampleData_RFF: DXVA2_SampleData = 1
DXVA2_SampleData_TFF: DXVA2_SampleData = 2
DXVA2_SampleData_RFF_TFF_Present: DXVA2_SampleData = 4
DXVA2_SampleData_Mask: DXVA2_SampleData = 65535
DXVA2_SampleFormat = Int32
DXVA2_SampleFormatMask: DXVA2_SampleFormat = 255
DXVA2_SampleUnknown: DXVA2_SampleFormat = 0
DXVA2_SampleProgressiveFrame: DXVA2_SampleFormat = 2
DXVA2_SampleFieldInterleavedEvenFirst: DXVA2_SampleFormat = 3
DXVA2_SampleFieldInterleavedOddFirst: DXVA2_SampleFormat = 4
DXVA2_SampleFieldSingleEven: DXVA2_SampleFormat = 5
DXVA2_SampleFieldSingleOdd: DXVA2_SampleFormat = 6
DXVA2_SampleSubStream: DXVA2_SampleFormat = 7
DXVA2_SurfaceType = Int32
DXVA2_SurfaceType_DecoderRenderTarget: DXVA2_SurfaceType = 0
DXVA2_SurfaceType_ProcessorRenderTarget: DXVA2_SurfaceType = 1
DXVA2_SurfaceType_D3DRenderTargetTexture: DXVA2_SurfaceType = 2
DXVA2_VPDev = Int32
DXVA2_VPDev_HardwareDevice: DXVA2_VPDev = 1
DXVA2_VPDev_EmulatedDXVA1: DXVA2_VPDev = 2
DXVA2_VPDev_SoftwareDevice: DXVA2_VPDev = 4
DXVA2_VPDev_Mask: DXVA2_VPDev = 7
class DXVA2_ValueRange(EasyCastStructure):
    MinValue: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    MaxValue: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    DefaultValue: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    StepSize: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
DXVA2_VideoChromaSubSampling = Int32
DXVA2_VideoChromaSubsamplingMask: DXVA2_VideoChromaSubSampling = 15
DXVA2_VideoChromaSubsampling_Unknown: DXVA2_VideoChromaSubSampling = 0
DXVA2_VideoChromaSubsampling_ProgressiveChroma: DXVA2_VideoChromaSubSampling = 8
DXVA2_VideoChromaSubsampling_Horizontally_Cosited: DXVA2_VideoChromaSubSampling = 4
DXVA2_VideoChromaSubsampling_Vertically_Cosited: DXVA2_VideoChromaSubSampling = 2
DXVA2_VideoChromaSubsampling_Vertically_AlignedChromaPlanes: DXVA2_VideoChromaSubSampling = 1
DXVA2_VideoChromaSubsampling_MPEG2: DXVA2_VideoChromaSubSampling = 5
DXVA2_VideoChromaSubsampling_MPEG1: DXVA2_VideoChromaSubSampling = 1
DXVA2_VideoChromaSubsampling_DV_PAL: DXVA2_VideoChromaSubSampling = 6
DXVA2_VideoChromaSubsampling_Cosited: DXVA2_VideoChromaSubSampling = 7
class DXVA2_VideoDesc(EasyCastStructure):
    SampleWidth: UInt32
    SampleHeight: UInt32
    SampleFormat: Windows.Win32.Media.MediaFoundation.DXVA2_ExtendedFormat
    Format: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    InputSampleFreq: Windows.Win32.Media.MediaFoundation.DXVA2_Frequency
    OutputFrameFreq: Windows.Win32.Media.MediaFoundation.DXVA2_Frequency
    UABProtectionLevel: UInt32
    Reserved: UInt32
DXVA2_VideoLighting = Int32
DXVA2_VideoLightingMask: DXVA2_VideoLighting = 15
DXVA2_VideoLighting_Unknown: DXVA2_VideoLighting = 0
DXVA2_VideoLighting_bright: DXVA2_VideoLighting = 1
DXVA2_VideoLighting_office: DXVA2_VideoLighting = 2
DXVA2_VideoLighting_dim: DXVA2_VideoLighting = 3
DXVA2_VideoLighting_dark: DXVA2_VideoLighting = 4
DXVA2_VideoPrimaries = Int32
DXVA2_VideoPrimariesMask: DXVA2_VideoPrimaries = 31
DXVA2_VideoPrimaries_Unknown: DXVA2_VideoPrimaries = 0
DXVA2_VideoPrimaries_reserved: DXVA2_VideoPrimaries = 1
DXVA2_VideoPrimaries_BT709: DXVA2_VideoPrimaries = 2
DXVA2_VideoPrimaries_BT470_2_SysM: DXVA2_VideoPrimaries = 3
DXVA2_VideoPrimaries_BT470_2_SysBG: DXVA2_VideoPrimaries = 4
DXVA2_VideoPrimaries_SMPTE170M: DXVA2_VideoPrimaries = 5
DXVA2_VideoPrimaries_SMPTE240M: DXVA2_VideoPrimaries = 6
DXVA2_VideoPrimaries_EBU3213: DXVA2_VideoPrimaries = 7
DXVA2_VideoPrimaries_SMPTE_C: DXVA2_VideoPrimaries = 8
DXVA2_VideoProcess = Int32
DXVA2_VideoProcess_None: DXVA2_VideoProcess = 0
DXVA2_VideoProcess_YUV2RGB: DXVA2_VideoProcess = 1
DXVA2_VideoProcess_StretchX: DXVA2_VideoProcess = 2
DXVA2_VideoProcess_StretchY: DXVA2_VideoProcess = 4
DXVA2_VideoProcess_AlphaBlend: DXVA2_VideoProcess = 8
DXVA2_VideoProcess_SubRects: DXVA2_VideoProcess = 16
DXVA2_VideoProcess_SubStreams: DXVA2_VideoProcess = 32
DXVA2_VideoProcess_SubStreamsExtended: DXVA2_VideoProcess = 64
DXVA2_VideoProcess_YUV2RGBExtended: DXVA2_VideoProcess = 128
DXVA2_VideoProcess_AlphaBlendExtended: DXVA2_VideoProcess = 256
DXVA2_VideoProcess_Constriction: DXVA2_VideoProcess = 512
DXVA2_VideoProcess_NoiseFilter: DXVA2_VideoProcess = 1024
DXVA2_VideoProcess_DetailFilter: DXVA2_VideoProcess = 2048
DXVA2_VideoProcess_PlanarAlpha: DXVA2_VideoProcess = 4096
DXVA2_VideoProcess_LinearScaling: DXVA2_VideoProcess = 8192
DXVA2_VideoProcess_GammaCompensated: DXVA2_VideoProcess = 16384
DXVA2_VideoProcess_MaintainsOriginalFieldData: DXVA2_VideoProcess = 32768
DXVA2_VideoProcess_Mask: DXVA2_VideoProcess = 65535
class DXVA2_VideoProcessBltParams(EasyCastStructure):
    TargetFrame: Int64
    TargetRect: Windows.Win32.Foundation.RECT
    ConstrictionSize: Windows.Win32.Foundation.SIZE
    StreamingFlags: UInt32
    BackgroundColor: Windows.Win32.Media.MediaFoundation.DXVA2_AYUVSample16
    DestFormat: Windows.Win32.Media.MediaFoundation.DXVA2_ExtendedFormat
    ProcAmpValues: Windows.Win32.Media.MediaFoundation.DXVA2_ProcAmpValues
    Alpha: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    NoiseFilterLuma: Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    NoiseFilterChroma: Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    DetailFilterLuma: Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    DetailFilterChroma: Windows.Win32.Media.MediaFoundation.DXVA2_FilterValues
    DestData: UInt32
class DXVA2_VideoProcessorCaps(EasyCastStructure):
    DeviceCaps: UInt32
    InputPool: Windows.Win32.Graphics.Direct3D9.D3DPOOL
    NumForwardRefSamples: UInt32
    NumBackwardRefSamples: UInt32
    Reserved: UInt32
    DeinterlaceTechnology: UInt32
    ProcAmpControlCaps: UInt32
    VideoProcessorOperations: UInt32
    NoiseFilterTechnology: UInt32
    DetailFilterTechnology: UInt32
DXVA2_VideoRenderTargetType = Int32
DXVA2_VideoDecoderRenderTarget: DXVA2_VideoRenderTargetType = 0
DXVA2_VideoProcessorRenderTarget: DXVA2_VideoRenderTargetType = 1
DXVA2_VideoSoftwareRenderTarget: DXVA2_VideoRenderTargetType = 2
class DXVA2_VideoSample(EasyCastStructure):
    Start: Int64
    End: Int64
    SampleFormat: Windows.Win32.Media.MediaFoundation.DXVA2_ExtendedFormat
    SrcSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head
    SrcRect: Windows.Win32.Foundation.RECT
    DstRect: Windows.Win32.Foundation.RECT
    Pal: Windows.Win32.Media.MediaFoundation.DXVA2_AYUVSample8 * 16
    PlanarAlpha: Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32
    SampleData: UInt32
DXVA2_VideoTransferFunction = Int32
DXVA2_VideoTransFuncMask: DXVA2_VideoTransferFunction = 31
DXVA2_VideoTransFunc_Unknown: DXVA2_VideoTransferFunction = 0
DXVA2_VideoTransFunc_10: DXVA2_VideoTransferFunction = 1
DXVA2_VideoTransFunc_18: DXVA2_VideoTransferFunction = 2
DXVA2_VideoTransFunc_20: DXVA2_VideoTransferFunction = 3
DXVA2_VideoTransFunc_22: DXVA2_VideoTransferFunction = 4
DXVA2_VideoTransFunc_709: DXVA2_VideoTransferFunction = 5
DXVA2_VideoTransFunc_240M: DXVA2_VideoTransferFunction = 6
DXVA2_VideoTransFunc_sRGB: DXVA2_VideoTransferFunction = 7
DXVA2_VideoTransFunc_28: DXVA2_VideoTransferFunction = 8
DXVA2_VideoTransferMatrix = Int32
DXVA2_VideoTransferMatrixMask: DXVA2_VideoTransferMatrix = 7
DXVA2_VideoTransferMatrix_Unknown: DXVA2_VideoTransferMatrix = 0
DXVA2_VideoTransferMatrix_BT709: DXVA2_VideoTransferMatrix = 1
DXVA2_VideoTransferMatrix_BT601: DXVA2_VideoTransferMatrix = 2
DXVA2_VideoTransferMatrix_SMPTE240M: DXVA2_VideoTransferMatrix = 3
class DXVABufferInfo(EasyCastStructure):
    pCompSurface: c_void_p
    DataOffset: UInt32
    DataSize: UInt32
class DXVACompBufferInfo(EasyCastStructure):
    NumCompBuffers: UInt32
    WidthToCreate: UInt32
    HeightToCreate: UInt32
    BytesToAllocate: UInt32
    Usage: UInt32
    Pool: Windows.Win32.Graphics.Direct3D9.D3DPOOL
    Format: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
class DXVAHDETW_CREATEVIDEOPROCESSOR(EasyCastStructure):
    pObject: UInt64
    pD3D9Ex: UInt64
    VPGuid: Guid
class DXVAHDETW_DESTROYVIDEOPROCESSOR(EasyCastStructure):
    pObject: UInt64
class DXVAHDETW_VIDEOPROCESSBLTHD(EasyCastStructure):
    pObject: UInt64
    pOutputSurface: UInt64
    TargetRect: Windows.Win32.Foundation.RECT
    OutputFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    ColorSpace: UInt32
    OutputFrame: UInt32
    StreamCount: UInt32
    Enter: Windows.Win32.Foundation.BOOL
class DXVAHDETW_VIDEOPROCESSBLTHD_STREAM(EasyCastStructure):
    pObject: UInt64
    pInputSurface: UInt64
    SourceRect: Windows.Win32.Foundation.RECT
    DestinationRect: Windows.Win32.Foundation.RECT
    InputFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    FrameFormat: Windows.Win32.Media.MediaFoundation.DXVAHD_FRAME_FORMAT
    ColorSpace: UInt32
    StreamNumber: UInt32
    OutputIndex: UInt32
    InputFrameOrField: UInt32
    PastFrames: UInt32
    FutureFrames: UInt32
class DXVAHDETW_VIDEOPROCESSBLTSTATE(EasyCastStructure):
    pObject: UInt64
    State: Windows.Win32.Media.MediaFoundation.DXVAHD_BLT_STATE
    DataSize: UInt32
    SetState: Windows.Win32.Foundation.BOOL
class DXVAHDETW_VIDEOPROCESSSTREAMSTATE(EasyCastStructure):
    pObject: UInt64
    StreamNumber: UInt32
    State: Windows.Win32.Media.MediaFoundation.DXVAHD_STREAM_STATE
    DataSize: UInt32
    SetState: Windows.Win32.Foundation.BOOL
class DXVAHDSW_CALLBACKS(EasyCastStructure):
    CreateDevice: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_CreateDevice
    ProposeVideoPrivateFormat: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_ProposeVideoPrivateFormat
    GetVideoProcessorDeviceCaps: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessorDeviceCaps
    GetVideoProcessorOutputFormats: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessorOutputFormats
    GetVideoProcessorInputFormats: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessorInputFormats
    GetVideoProcessorCaps: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessorCaps
    GetVideoProcessorCustomRates: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessorCustomRates
    GetVideoProcessorFilterRange: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessorFilterRange
    DestroyDevice: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_DestroyDevice
    CreateVideoProcessor: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_CreateVideoProcessor
    SetVideoProcessBltState: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_SetVideoProcessBltState
    GetVideoProcessBltStatePrivate: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessBltStatePrivate
    SetVideoProcessStreamState: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_SetVideoProcessStreamState
    GetVideoProcessStreamStatePrivate: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_GetVideoProcessStreamStatePrivate
    VideoProcessBltHD: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_VideoProcessBltHD
    DestroyVideoProcessor: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_DestroyVideoProcessor
DXVAHD_ALPHA_FILL_MODE = Int32
DXVAHD_ALPHA_FILL_MODE_OPAQUE: DXVAHD_ALPHA_FILL_MODE = 0
DXVAHD_ALPHA_FILL_MODE_BACKGROUND: DXVAHD_ALPHA_FILL_MODE = 1
DXVAHD_ALPHA_FILL_MODE_DESTINATION: DXVAHD_ALPHA_FILL_MODE = 2
DXVAHD_ALPHA_FILL_MODE_SOURCE_STREAM: DXVAHD_ALPHA_FILL_MODE = 3
DXVAHD_BLT_STATE = Int32
DXVAHD_BLT_STATE_TARGET_RECT: DXVAHD_BLT_STATE = 0
DXVAHD_BLT_STATE_BACKGROUND_COLOR: DXVAHD_BLT_STATE = 1
DXVAHD_BLT_STATE_OUTPUT_COLOR_SPACE: DXVAHD_BLT_STATE = 2
DXVAHD_BLT_STATE_ALPHA_FILL: DXVAHD_BLT_STATE = 3
DXVAHD_BLT_STATE_CONSTRICTION: DXVAHD_BLT_STATE = 4
DXVAHD_BLT_STATE_PRIVATE: DXVAHD_BLT_STATE = 1000
class DXVAHD_BLT_STATE_ALPHA_FILL_DATA(EasyCastStructure):
    Mode: Windows.Win32.Media.MediaFoundation.DXVAHD_ALPHA_FILL_MODE
    StreamNumber: UInt32
class DXVAHD_BLT_STATE_BACKGROUND_COLOR_DATA(EasyCastStructure):
    YCbCr: Windows.Win32.Foundation.BOOL
    BackgroundColor: Windows.Win32.Media.MediaFoundation.DXVAHD_COLOR
class DXVAHD_BLT_STATE_CONSTRICTION_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    Size: Windows.Win32.Foundation.SIZE
class DXVAHD_BLT_STATE_OUTPUT_COLOR_SPACE_DATA(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        Value: UInt32
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
class DXVAHD_BLT_STATE_PRIVATE_DATA(EasyCastStructure):
    Guid: Guid
    DataSize: UInt32
    pData: c_void_p
class DXVAHD_BLT_STATE_TARGET_RECT_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    TargetRect: Windows.Win32.Foundation.RECT
class DXVAHD_COLOR(EasyCastUnion):
    RGB: Windows.Win32.Media.MediaFoundation.DXVAHD_COLOR_RGBA
    YCbCr: Windows.Win32.Media.MediaFoundation.DXVAHD_COLOR_YCbCrA
class DXVAHD_COLOR_RGBA(EasyCastStructure):
    R: Single
    G: Single
    B: Single
    A: Single
class DXVAHD_COLOR_YCbCrA(EasyCastStructure):
    Y: Single
    Cb: Single
    Cr: Single
    A: Single
class DXVAHD_CONTENT_DESC(EasyCastStructure):
    InputFrameFormat: Windows.Win32.Media.MediaFoundation.DXVAHD_FRAME_FORMAT
    InputFrameRate: Windows.Win32.Media.MediaFoundation.DXVAHD_RATIONAL
    InputWidth: UInt32
    InputHeight: UInt32
    OutputFrameRate: Windows.Win32.Media.MediaFoundation.DXVAHD_RATIONAL
    OutputWidth: UInt32
    OutputHeight: UInt32
class DXVAHD_CUSTOM_RATE_DATA(EasyCastStructure):
    CustomRate: Windows.Win32.Media.MediaFoundation.DXVAHD_RATIONAL
    OutputFrames: UInt32
    InputInterlaced: Windows.Win32.Foundation.BOOL
    InputFramesOrFields: UInt32
DXVAHD_DEVICE_CAPS = Int32
DXVAHD_DEVICE_CAPS_LINEAR_SPACE: DXVAHD_DEVICE_CAPS = 1
DXVAHD_DEVICE_CAPS_xvYCC: DXVAHD_DEVICE_CAPS = 2
DXVAHD_DEVICE_CAPS_RGB_RANGE_CONVERSION: DXVAHD_DEVICE_CAPS = 4
DXVAHD_DEVICE_CAPS_YCbCr_MATRIX_CONVERSION: DXVAHD_DEVICE_CAPS = 8
DXVAHD_DEVICE_TYPE = Int32
DXVAHD_DEVICE_TYPE_HARDWARE: DXVAHD_DEVICE_TYPE = 0
DXVAHD_DEVICE_TYPE_SOFTWARE: DXVAHD_DEVICE_TYPE = 1
DXVAHD_DEVICE_TYPE_REFERENCE: DXVAHD_DEVICE_TYPE = 2
DXVAHD_DEVICE_TYPE_OTHER: DXVAHD_DEVICE_TYPE = 3
DXVAHD_DEVICE_USAGE = Int32
DXVAHD_DEVICE_USAGE_PLAYBACK_NORMAL: DXVAHD_DEVICE_USAGE = 0
DXVAHD_DEVICE_USAGE_OPTIMAL_SPEED: DXVAHD_DEVICE_USAGE = 1
DXVAHD_DEVICE_USAGE_OPTIMAL_QUALITY: DXVAHD_DEVICE_USAGE = 2
DXVAHD_FEATURE_CAPS = Int32
DXVAHD_FEATURE_CAPS_ALPHA_FILL: DXVAHD_FEATURE_CAPS = 1
DXVAHD_FEATURE_CAPS_CONSTRICTION: DXVAHD_FEATURE_CAPS = 2
DXVAHD_FEATURE_CAPS_LUMA_KEY: DXVAHD_FEATURE_CAPS = 4
DXVAHD_FEATURE_CAPS_ALPHA_PALETTE: DXVAHD_FEATURE_CAPS = 8
DXVAHD_FILTER = Int32
DXVAHD_FILTER_BRIGHTNESS: DXVAHD_FILTER = 0
DXVAHD_FILTER_CONTRAST: DXVAHD_FILTER = 1
DXVAHD_FILTER_HUE: DXVAHD_FILTER = 2
DXVAHD_FILTER_SATURATION: DXVAHD_FILTER = 3
DXVAHD_FILTER_NOISE_REDUCTION: DXVAHD_FILTER = 4
DXVAHD_FILTER_EDGE_ENHANCEMENT: DXVAHD_FILTER = 5
DXVAHD_FILTER_ANAMORPHIC_SCALING: DXVAHD_FILTER = 6
DXVAHD_FILTER_CAPS = Int32
DXVAHD_FILTER_CAPS_BRIGHTNESS: DXVAHD_FILTER_CAPS = 1
DXVAHD_FILTER_CAPS_CONTRAST: DXVAHD_FILTER_CAPS = 2
DXVAHD_FILTER_CAPS_HUE: DXVAHD_FILTER_CAPS = 4
DXVAHD_FILTER_CAPS_SATURATION: DXVAHD_FILTER_CAPS = 8
DXVAHD_FILTER_CAPS_NOISE_REDUCTION: DXVAHD_FILTER_CAPS = 16
DXVAHD_FILTER_CAPS_EDGE_ENHANCEMENT: DXVAHD_FILTER_CAPS = 32
DXVAHD_FILTER_CAPS_ANAMORPHIC_SCALING: DXVAHD_FILTER_CAPS = 64
class DXVAHD_FILTER_RANGE_DATA(EasyCastStructure):
    Minimum: Int32
    Maximum: Int32
    Default: Int32
    Multiplier: Single
DXVAHD_FRAME_FORMAT = Int32
DXVAHD_FRAME_FORMAT_PROGRESSIVE: DXVAHD_FRAME_FORMAT = 0
DXVAHD_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST: DXVAHD_FRAME_FORMAT = 1
DXVAHD_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST: DXVAHD_FRAME_FORMAT = 2
DXVAHD_INPUT_FORMAT_CAPS = Int32
DXVAHD_INPUT_FORMAT_CAPS_RGB_INTERLACED: DXVAHD_INPUT_FORMAT_CAPS = 1
DXVAHD_INPUT_FORMAT_CAPS_RGB_PROCAMP: DXVAHD_INPUT_FORMAT_CAPS = 2
DXVAHD_INPUT_FORMAT_CAPS_RGB_LUMA_KEY: DXVAHD_INPUT_FORMAT_CAPS = 4
DXVAHD_INPUT_FORMAT_CAPS_PALETTE_INTERLACED: DXVAHD_INPUT_FORMAT_CAPS = 8
DXVAHD_ITELECINE_CAPS = Int32
DXVAHD_ITELECINE_CAPS_32: DXVAHD_ITELECINE_CAPS = 1
DXVAHD_ITELECINE_CAPS_22: DXVAHD_ITELECINE_CAPS = 2
DXVAHD_ITELECINE_CAPS_2224: DXVAHD_ITELECINE_CAPS = 4
DXVAHD_ITELECINE_CAPS_2332: DXVAHD_ITELECINE_CAPS = 8
DXVAHD_ITELECINE_CAPS_32322: DXVAHD_ITELECINE_CAPS = 16
DXVAHD_ITELECINE_CAPS_55: DXVAHD_ITELECINE_CAPS = 32
DXVAHD_ITELECINE_CAPS_64: DXVAHD_ITELECINE_CAPS = 64
DXVAHD_ITELECINE_CAPS_87: DXVAHD_ITELECINE_CAPS = 128
DXVAHD_ITELECINE_CAPS_222222222223: DXVAHD_ITELECINE_CAPS = 256
DXVAHD_ITELECINE_CAPS_OTHER: DXVAHD_ITELECINE_CAPS = -2147483648
DXVAHD_OUTPUT_RATE = Int32
DXVAHD_OUTPUT_RATE_NORMAL: DXVAHD_OUTPUT_RATE = 0
DXVAHD_OUTPUT_RATE_HALF: DXVAHD_OUTPUT_RATE = 1
DXVAHD_OUTPUT_RATE_CUSTOM: DXVAHD_OUTPUT_RATE = 2
DXVAHD_PROCESSOR_CAPS = Int32
DXVAHD_PROCESSOR_CAPS_DEINTERLACE_BLEND: DXVAHD_PROCESSOR_CAPS = 1
DXVAHD_PROCESSOR_CAPS_DEINTERLACE_BOB: DXVAHD_PROCESSOR_CAPS = 2
DXVAHD_PROCESSOR_CAPS_DEINTERLACE_ADAPTIVE: DXVAHD_PROCESSOR_CAPS = 4
DXVAHD_PROCESSOR_CAPS_DEINTERLACE_MOTION_COMPENSATION: DXVAHD_PROCESSOR_CAPS = 8
DXVAHD_PROCESSOR_CAPS_INVERSE_TELECINE: DXVAHD_PROCESSOR_CAPS = 16
DXVAHD_PROCESSOR_CAPS_FRAME_RATE_CONVERSION: DXVAHD_PROCESSOR_CAPS = 32
class DXVAHD_RATIONAL(EasyCastStructure):
    Numerator: UInt32
    Denominator: UInt32
class DXVAHD_STREAM_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    OutputIndex: UInt32
    InputFrameOrField: UInt32
    PastFrames: UInt32
    FutureFrames: UInt32
    ppPastSurfaces: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head)
    pInputSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head
    ppFutureSurfaces: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head)
DXVAHD_STREAM_STATE = Int32
DXVAHD_STREAM_STATE_D3DFORMAT: DXVAHD_STREAM_STATE = 0
DXVAHD_STREAM_STATE_FRAME_FORMAT: DXVAHD_STREAM_STATE = 1
DXVAHD_STREAM_STATE_INPUT_COLOR_SPACE: DXVAHD_STREAM_STATE = 2
DXVAHD_STREAM_STATE_OUTPUT_RATE: DXVAHD_STREAM_STATE = 3
DXVAHD_STREAM_STATE_SOURCE_RECT: DXVAHD_STREAM_STATE = 4
DXVAHD_STREAM_STATE_DESTINATION_RECT: DXVAHD_STREAM_STATE = 5
DXVAHD_STREAM_STATE_ALPHA: DXVAHD_STREAM_STATE = 6
DXVAHD_STREAM_STATE_PALETTE: DXVAHD_STREAM_STATE = 7
DXVAHD_STREAM_STATE_LUMA_KEY: DXVAHD_STREAM_STATE = 8
DXVAHD_STREAM_STATE_ASPECT_RATIO: DXVAHD_STREAM_STATE = 9
DXVAHD_STREAM_STATE_FILTER_BRIGHTNESS: DXVAHD_STREAM_STATE = 100
DXVAHD_STREAM_STATE_FILTER_CONTRAST: DXVAHD_STREAM_STATE = 101
DXVAHD_STREAM_STATE_FILTER_HUE: DXVAHD_STREAM_STATE = 102
DXVAHD_STREAM_STATE_FILTER_SATURATION: DXVAHD_STREAM_STATE = 103
DXVAHD_STREAM_STATE_FILTER_NOISE_REDUCTION: DXVAHD_STREAM_STATE = 104
DXVAHD_STREAM_STATE_FILTER_EDGE_ENHANCEMENT: DXVAHD_STREAM_STATE = 105
DXVAHD_STREAM_STATE_FILTER_ANAMORPHIC_SCALING: DXVAHD_STREAM_STATE = 106
DXVAHD_STREAM_STATE_PRIVATE: DXVAHD_STREAM_STATE = 1000
class DXVAHD_STREAM_STATE_ALPHA_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    Alpha: Single
class DXVAHD_STREAM_STATE_ASPECT_RATIO_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    SourceAspectRatio: Windows.Win32.Media.MediaFoundation.DXVAHD_RATIONAL
    DestinationAspectRatio: Windows.Win32.Media.MediaFoundation.DXVAHD_RATIONAL
class DXVAHD_STREAM_STATE_D3DFORMAT_DATA(EasyCastStructure):
    Format: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
class DXVAHD_STREAM_STATE_DESTINATION_RECT_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    DestinationRect: Windows.Win32.Foundation.RECT
class DXVAHD_STREAM_STATE_FILTER_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    Level: Int32
class DXVAHD_STREAM_STATE_FRAME_FORMAT_DATA(EasyCastStructure):
    FrameFormat: Windows.Win32.Media.MediaFoundation.DXVAHD_FRAME_FORMAT
class DXVAHD_STREAM_STATE_INPUT_COLOR_SPACE_DATA(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        Value: UInt32
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
class DXVAHD_STREAM_STATE_LUMA_KEY_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    Lower: Single
    Upper: Single
class DXVAHD_STREAM_STATE_OUTPUT_RATE_DATA(EasyCastStructure):
    RepeatFrame: Windows.Win32.Foundation.BOOL
    OutputRate: Windows.Win32.Media.MediaFoundation.DXVAHD_OUTPUT_RATE
    CustomRate: Windows.Win32.Media.MediaFoundation.DXVAHD_RATIONAL
class DXVAHD_STREAM_STATE_PALETTE_DATA(EasyCastStructure):
    Count: UInt32
    pEntries: POINTER(UInt32)
class DXVAHD_STREAM_STATE_PRIVATE_DATA(EasyCastStructure):
    Guid: Guid
    DataSize: UInt32
    pData: c_void_p
class DXVAHD_STREAM_STATE_PRIVATE_IVTC_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    ITelecineFlags: UInt32
    Frames: UInt32
    InputField: UInt32
class DXVAHD_STREAM_STATE_SOURCE_RECT_DATA(EasyCastStructure):
    Enable: Windows.Win32.Foundation.BOOL
    SourceRect: Windows.Win32.Foundation.RECT
DXVAHD_SURFACE_TYPE = Int32
DXVAHD_SURFACE_TYPE_VIDEO_INPUT: DXVAHD_SURFACE_TYPE = 0
DXVAHD_SURFACE_TYPE_VIDEO_INPUT_PRIVATE: DXVAHD_SURFACE_TYPE = 1
DXVAHD_SURFACE_TYPE_VIDEO_OUTPUT: DXVAHD_SURFACE_TYPE = 2
class DXVAHD_VPCAPS(EasyCastStructure):
    VPGuid: Guid
    PastFrames: UInt32
    FutureFrames: UInt32
    ProcessorCaps: UInt32
    ITelecineCaps: UInt32
    CustomRateCount: UInt32
class DXVAHD_VPDEVCAPS(EasyCastStructure):
    DeviceType: Windows.Win32.Media.MediaFoundation.DXVAHD_DEVICE_TYPE
    DeviceCaps: UInt32
    FeatureCaps: UInt32
    FilterCaps: UInt32
    InputFormatCaps: UInt32
    InputPool: Windows.Win32.Graphics.Direct3D9.D3DPOOL
    OutputFormatCount: UInt32
    InputFormatCount: UInt32
    VideoProcessorCount: UInt32
    MaxInputStreams: UInt32
    MaxStreamStates: UInt32
class DXVAUncompDataInfo(EasyCastStructure):
    UncompWidth: UInt32
    UncompHeight: UInt32
    UncompFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
class DXVA_AYUVsample2(EasyCastStructure):
    bCrValue: Byte
    bCbValue: Byte
    bY_Value: Byte
    bSampleAlpha8: Byte
class DXVA_BufferDescription(EasyCastStructure):
    dwTypeIndex: UInt32
    dwBufferIndex: UInt32
    dwDataOffset: UInt32
    dwDataSize: UInt32
    dwFirstMBaddress: UInt32
    dwNumMBsInBuffer: UInt32
    dwWidth: UInt32
    dwHeight: UInt32
    dwStride: UInt32
    dwReservedBits: UInt32
    _pack_ = 1
class DXVA_COPPCommand(EasyCastStructure):
    macKDI: Guid
    guidCommandID: Guid
    dwSequence: UInt32
    cbSizeData: UInt32
    CommandData: Byte * 4056
class DXVA_COPPSignature(EasyCastStructure):
    Signature: Byte * 256
class DXVA_COPPStatusInput(EasyCastStructure):
    rApp: Guid
    guidStatusRequestID: Guid
    dwSequence: UInt32
    cbSizeData: UInt32
    StatusData: Byte * 4056
class DXVA_COPPStatusOutput(EasyCastStructure):
    macKDI: Guid
    cbSizeData: UInt32
    COPPStatus: Byte * 4076
class DXVA_ConfigPictureDecode(EasyCastStructure):
    dwFunction: UInt32
    dwReservedBits: UInt32 * 3
    guidConfigBitstreamEncryption: Guid
    guidConfigMBcontrolEncryption: Guid
    guidConfigResidDiffEncryption: Guid
    bConfigBitstreamRaw: Byte
    bConfigMBcontrolRasterOrder: Byte
    bConfigResidDiffHost: Byte
    bConfigSpatialResid8: Byte
    bConfigResid8Subtraction: Byte
    bConfigSpatialHost8or9Clipping: Byte
    bConfigSpatialResidInterleaved: Byte
    bConfigIntraResidUnsigned: Byte
    bConfigResidDiffAccelerator: Byte
    bConfigHostInverseScan: Byte
    bConfigSpecificIDCT: Byte
    bConfig4GroupedCoefs: Byte
    _pack_ = 1
class DXVA_DeinterlaceBlt(EasyCastStructure):
    Size: UInt32
    Reserved: UInt32
    rtTarget: Int64
    DstRect: Windows.Win32.Foundation.RECT
    SrcRect: Windows.Win32.Foundation.RECT
    NumSourceSurfaces: UInt32
    Alpha: Single
    Source: Windows.Win32.Media.MediaFoundation.DXVA_VideoSample * 32
class DXVA_DeinterlaceBltEx(EasyCastStructure):
    Size: UInt32
    BackgroundColor: Windows.Win32.Media.MediaFoundation.DXVA_AYUVsample2
    rcTarget: Windows.Win32.Foundation.RECT
    rtTarget: Int64
    NumSourceSurfaces: UInt32
    Alpha: Single
    Source: Windows.Win32.Media.MediaFoundation.DXVA_VideoSample2 * 32
    DestinationFormat: UInt32
    DestinationFlags: UInt32
if ARCH in 'X64,ARM64':
    class DXVA_DeinterlaceBltEx32(EasyCastStructure):
        Size: UInt32
        BackgroundColor: Windows.Win32.Media.MediaFoundation.DXVA_AYUVsample2
        rcTarget: Windows.Win32.Foundation.RECT
        rtTarget: Int64
        NumSourceSurfaces: UInt32
        Alpha: Single
        Source: Windows.Win32.Media.MediaFoundation.DXVA_VideoSample32 * 32
        DestinationFormat: UInt32
        DestinationFlags: UInt32
class DXVA_DeinterlaceCaps(EasyCastStructure):
    Size: UInt32
    NumPreviousOutputFrames: UInt32
    InputPool: UInt32
    NumForwardRefSamples: UInt32
    NumBackwardRefSamples: UInt32
    d3dOutputFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    VideoProcessingCaps: Windows.Win32.Media.MediaFoundation.DXVA_VideoProcessCaps
    DeinterlaceTechnology: Windows.Win32.Media.MediaFoundation.DXVA_DeinterlaceTech
class DXVA_DeinterlaceQueryAvailableModes(EasyCastStructure):
    Size: UInt32
    NumGuids: UInt32
    Guids: Guid * 32
class DXVA_DeinterlaceQueryModeCaps(EasyCastStructure):
    Size: UInt32
    Guid: Guid
    VideoDesc: Windows.Win32.Media.MediaFoundation.DXVA_VideoDesc
DXVA_DeinterlaceTech = Int32
DXVA_DeinterlaceTech_Unknown: DXVA_DeinterlaceTech = 0
DXVA_DeinterlaceTech_BOBLineReplicate: DXVA_DeinterlaceTech = 1
DXVA_DeinterlaceTech_BOBVerticalStretch: DXVA_DeinterlaceTech = 2
DXVA_DeinterlaceTech_BOBVerticalStretch4Tap: DXVA_DeinterlaceTech = 256
DXVA_DeinterlaceTech_MedianFiltering: DXVA_DeinterlaceTech = 4
DXVA_DeinterlaceTech_EdgeFiltering: DXVA_DeinterlaceTech = 16
DXVA_DeinterlaceTech_FieldAdaptive: DXVA_DeinterlaceTech = 32
DXVA_DeinterlaceTech_PixelAdaptive: DXVA_DeinterlaceTech = 64
DXVA_DeinterlaceTech_MotionVectorSteered: DXVA_DeinterlaceTech = 128
DXVA_DestinationFlags = Int32
DXVA_DestinationFlagMask: DXVA_DestinationFlags = 15
DXVA_DestinationFlag_Background_Changed: DXVA_DestinationFlags = 1
DXVA_DestinationFlag_TargetRect_Changed: DXVA_DestinationFlags = 2
DXVA_DestinationFlag_ColorData_Changed: DXVA_DestinationFlags = 4
DXVA_DestinationFlag_Alpha_Changed: DXVA_DestinationFlags = 8
class DXVA_ExtendedFormat(EasyCastStructure):
    _bitfield: UInt32
class DXVA_Frequency(EasyCastStructure):
    Numerator: UInt32
    Denominator: UInt32
DXVA_NominalRange = Int32
DXVA_NominalRangeShift: DXVA_NominalRange = 12
DXVA_NominalRangeMask: DXVA_NominalRange = 28672
DXVA_NominalRange_Unknown: DXVA_NominalRange = 0
DXVA_NominalRange_Normal: DXVA_NominalRange = 1
DXVA_NominalRange_Wide: DXVA_NominalRange = 2
DXVA_NominalRange_0_255: DXVA_NominalRange = 1
DXVA_NominalRange_16_235: DXVA_NominalRange = 2
DXVA_NominalRange_48_208: DXVA_NominalRange = 3
class DXVA_PictureParameters(EasyCastStructure):
    wDecodedPictureIndex: UInt16
    wDeblockedPictureIndex: UInt16
    wForwardRefPictureIndex: UInt16
    wBackwardRefPictureIndex: UInt16
    wPicWidthInMBminus1: UInt16
    wPicHeightInMBminus1: UInt16
    bMacroblockWidthMinus1: Byte
    bMacroblockHeightMinus1: Byte
    bBlockWidthMinus1: Byte
    bBlockHeightMinus1: Byte
    bBPPminus1: Byte
    bPicStructure: Byte
    bSecondField: Byte
    bPicIntra: Byte
    bPicBackwardPrediction: Byte
    bBidirectionalAveragingMode: Byte
    bMVprecisionAndChromaRelation: Byte
    bChromaFormat: Byte
    bPicScanFixed: Byte
    bPicScanMethod: Byte
    bPicReadbackRequests: Byte
    bRcontrol: Byte
    bPicSpatialResid8: Byte
    bPicOverflowBlocks: Byte
    bPicExtrapolation: Byte
    bPicDeblocked: Byte
    bPicDeblockConfined: Byte
    bPic4MVallowed: Byte
    bPicOBMC: Byte
    bPicBinPB: Byte
    bMV_RPS: Byte
    bReservedBits: Byte
    wBitstreamFcodes: UInt16
    wBitstreamPCEelements: UInt16
    bBitstreamConcealmentNeed: Byte
    bBitstreamConcealmentMethod: Byte
    _pack_ = 1
class DXVA_ProcAmpControlBlt(EasyCastStructure):
    Size: UInt32
    DstRect: Windows.Win32.Foundation.RECT
    SrcRect: Windows.Win32.Foundation.RECT
    Alpha: Single
    Brightness: Single
    Contrast: Single
    Hue: Single
    Saturation: Single
class DXVA_ProcAmpControlCaps(EasyCastStructure):
    Size: UInt32
    InputPool: UInt32
    d3dOutputFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    ProcAmpControlProps: UInt32
    VideoProcessingCaps: UInt32
DXVA_ProcAmpControlProp = Int32
DXVA_ProcAmp_None: DXVA_ProcAmpControlProp = 0
DXVA_ProcAmp_Brightness: DXVA_ProcAmpControlProp = 1
DXVA_ProcAmp_Contrast: DXVA_ProcAmpControlProp = 2
DXVA_ProcAmp_Hue: DXVA_ProcAmpControlProp = 4
DXVA_ProcAmp_Saturation: DXVA_ProcAmpControlProp = 8
class DXVA_ProcAmpControlQueryRange(EasyCastStructure):
    Size: UInt32
    ProcAmpControlProp: Windows.Win32.Media.MediaFoundation.DXVA_ProcAmpControlProp
    VideoDesc: Windows.Win32.Media.MediaFoundation.DXVA_VideoDesc
DXVA_SampleFlags = Int32
DXVA_SampleFlagsMask: DXVA_SampleFlags = 15
DXVA_SampleFlag_Palette_Changed: DXVA_SampleFlags = 1
DXVA_SampleFlag_SrcRect_Changed: DXVA_SampleFlags = 2
DXVA_SampleFlag_DstRect_Changed: DXVA_SampleFlags = 4
DXVA_SampleFlag_ColorData_Changed: DXVA_SampleFlags = 8
DXVA_SampleFormat = Int32
DXVA_SampleFormatMask: DXVA_SampleFormat = 255
DXVA_SampleUnknown: DXVA_SampleFormat = 0
DXVA_SamplePreviousFrame: DXVA_SampleFormat = 1
DXVA_SampleProgressiveFrame: DXVA_SampleFormat = 2
DXVA_SampleFieldInterleavedEvenFirst: DXVA_SampleFormat = 3
DXVA_SampleFieldInterleavedOddFirst: DXVA_SampleFormat = 4
DXVA_SampleFieldSingleEven: DXVA_SampleFormat = 5
DXVA_SampleFieldSingleOdd: DXVA_SampleFormat = 6
DXVA_SampleSubStream: DXVA_SampleFormat = 7
DXVA_VideoChromaSubsampling = Int32
DXVA_VideoChromaSubsamplingShift: DXVA_VideoChromaSubsampling = 8
DXVA_VideoChromaSubsamplingMask: DXVA_VideoChromaSubsampling = 3840
DXVA_VideoChromaSubsampling_Unknown: DXVA_VideoChromaSubsampling = 0
DXVA_VideoChromaSubsampling_ProgressiveChroma: DXVA_VideoChromaSubsampling = 8
DXVA_VideoChromaSubsampling_Horizontally_Cosited: DXVA_VideoChromaSubsampling = 4
DXVA_VideoChromaSubsampling_Vertically_Cosited: DXVA_VideoChromaSubsampling = 2
DXVA_VideoChromaSubsampling_Vertically_AlignedChromaPlanes: DXVA_VideoChromaSubsampling = 1
DXVA_VideoChromaSubsampling_MPEG2: DXVA_VideoChromaSubsampling = 5
DXVA_VideoChromaSubsampling_MPEG1: DXVA_VideoChromaSubsampling = 1
DXVA_VideoChromaSubsampling_DV_PAL: DXVA_VideoChromaSubsampling = 6
DXVA_VideoChromaSubsampling_Cosited: DXVA_VideoChromaSubsampling = 7
class DXVA_VideoDesc(EasyCastStructure):
    Size: UInt32
    SampleWidth: UInt32
    SampleHeight: UInt32
    SampleFormat: UInt32
    d3dFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    InputSampleFreq: Windows.Win32.Media.MediaFoundation.DXVA_Frequency
    OutputFrameFreq: Windows.Win32.Media.MediaFoundation.DXVA_Frequency
DXVA_VideoLighting = Int32
DXVA_VideoLightingShift: DXVA_VideoLighting = 18
DXVA_VideoLightingMask: DXVA_VideoLighting = 3932160
DXVA_VideoLighting_Unknown: DXVA_VideoLighting = 0
DXVA_VideoLighting_bright: DXVA_VideoLighting = 1
DXVA_VideoLighting_office: DXVA_VideoLighting = 2
DXVA_VideoLighting_dim: DXVA_VideoLighting = 3
DXVA_VideoLighting_dark: DXVA_VideoLighting = 4
DXVA_VideoPrimaries = Int32
DXVA_VideoPrimariesShift: DXVA_VideoPrimaries = 22
DXVA_VideoPrimariesMask: DXVA_VideoPrimaries = 130023424
DXVA_VideoPrimaries_Unknown: DXVA_VideoPrimaries = 0
DXVA_VideoPrimaries_reserved: DXVA_VideoPrimaries = 1
DXVA_VideoPrimaries_BT709: DXVA_VideoPrimaries = 2
DXVA_VideoPrimaries_BT470_2_SysM: DXVA_VideoPrimaries = 3
DXVA_VideoPrimaries_BT470_2_SysBG: DXVA_VideoPrimaries = 4
DXVA_VideoPrimaries_SMPTE170M: DXVA_VideoPrimaries = 5
DXVA_VideoPrimaries_SMPTE240M: DXVA_VideoPrimaries = 6
DXVA_VideoPrimaries_EBU3213: DXVA_VideoPrimaries = 7
DXVA_VideoPrimaries_SMPTE_C: DXVA_VideoPrimaries = 8
DXVA_VideoProcessCaps = Int32
DXVA_VideoProcess_None: DXVA_VideoProcessCaps = 0
DXVA_VideoProcess_YUV2RGB: DXVA_VideoProcessCaps = 1
DXVA_VideoProcess_StretchX: DXVA_VideoProcessCaps = 2
DXVA_VideoProcess_StretchY: DXVA_VideoProcessCaps = 4
DXVA_VideoProcess_AlphaBlend: DXVA_VideoProcessCaps = 8
DXVA_VideoProcess_SubRects: DXVA_VideoProcessCaps = 16
DXVA_VideoProcess_SubStreams: DXVA_VideoProcessCaps = 32
DXVA_VideoProcess_SubStreamsExtended: DXVA_VideoProcessCaps = 64
DXVA_VideoProcess_YUV2RGBExtended: DXVA_VideoProcessCaps = 128
DXVA_VideoProcess_AlphaBlendExtended: DXVA_VideoProcessCaps = 256
class DXVA_VideoPropertyRange(EasyCastStructure):
    MinValue: Single
    MaxValue: Single
    DefaultValue: Single
    StepSize: Single
class DXVA_VideoSample(EasyCastStructure):
    rtStart: Int64
    rtEnd: Int64
    SampleFormat: Windows.Win32.Media.MediaFoundation.DXVA_SampleFormat
    lpDDSSrcSurface: c_void_p
if ARCH in 'X64,ARM64':
    class DXVA_VideoSample2(EasyCastStructure):
        Size: UInt32
        Reserved: UInt32
        rtStart: Int64
        rtEnd: Int64
        SampleFormat: UInt32
        SampleFlags: UInt32
        lpDDSSrcSurface: c_void_p
        rcSrc: Windows.Win32.Foundation.RECT
        rcDst: Windows.Win32.Foundation.RECT
        Palette: Windows.Win32.Media.MediaFoundation.DXVA_AYUVsample2 * 16
if ARCH in 'X86':
    class DXVA_VideoSample2(EasyCastStructure):
        rtStart: Int64
        rtEnd: Int64
        SampleFormat: UInt32
        SampleFlags: UInt32
        lpDDSSrcSurface: c_void_p
        rcSrc: Windows.Win32.Foundation.RECT
        rcDst: Windows.Win32.Foundation.RECT
        Palette: Windows.Win32.Media.MediaFoundation.DXVA_AYUVsample2 * 16
if ARCH in 'X64,ARM64':
    class DXVA_VideoSample32(EasyCastStructure):
        rtStart: Int64
        rtEnd: Int64
        SampleFormat: UInt32
        SampleFlags: UInt32
        lpDDSSrcSurface: UInt32
        rcSrc: Windows.Win32.Foundation.RECT
        rcDst: Windows.Win32.Foundation.RECT
        Palette: Windows.Win32.Media.MediaFoundation.DXVA_AYUVsample2 * 16
DXVA_VideoTransferFunction = Int32
DXVA_VideoTransFuncShift: DXVA_VideoTransferFunction = 27
DXVA_VideoTransFuncMask: DXVA_VideoTransferFunction = -134217728
DXVA_VideoTransFunc_Unknown: DXVA_VideoTransferFunction = 0
DXVA_VideoTransFunc_10: DXVA_VideoTransferFunction = 1
DXVA_VideoTransFunc_18: DXVA_VideoTransferFunction = 2
DXVA_VideoTransFunc_20: DXVA_VideoTransferFunction = 3
DXVA_VideoTransFunc_22: DXVA_VideoTransferFunction = 4
DXVA_VideoTransFunc_22_709: DXVA_VideoTransferFunction = 5
DXVA_VideoTransFunc_22_240M: DXVA_VideoTransferFunction = 6
DXVA_VideoTransFunc_22_8bit_sRGB: DXVA_VideoTransferFunction = 7
DXVA_VideoTransFunc_28: DXVA_VideoTransferFunction = 8
DXVA_VideoTransferMatrix = Int32
DXVA_VideoTransferMatrixShift: DXVA_VideoTransferMatrix = 15
DXVA_VideoTransferMatrixMask: DXVA_VideoTransferMatrix = 229376
DXVA_VideoTransferMatrix_Unknown: DXVA_VideoTransferMatrix = 0
DXVA_VideoTransferMatrix_BT709: DXVA_VideoTransferMatrix = 1
DXVA_VideoTransferMatrix_BT601: DXVA_VideoTransferMatrix = 2
DXVA_VideoTransferMatrix_SMPTE240M: DXVA_VideoTransferMatrix = 3
DeviceStreamState = Int32
DeviceStreamState_Stop: DeviceStreamState = 0
DeviceStreamState_Pause: DeviceStreamState = 1
DeviceStreamState_Run: DeviceStreamState = 2
DeviceStreamState_Disabled: DeviceStreamState = 3
class DigitalWindowSetting(EasyCastStructure):
    OriginX: Double
    OriginY: Double
    WindowSize: Double
EAllocationType = Int32
EAllocationType_eAllocationTypeDynamic: EAllocationType = 0
EAllocationType_eAllocationTypeRT: EAllocationType = 1
EAllocationType_eAllocationTypePageable: EAllocationType = 2
EAllocationType_eAllocationTypeIgnore: EAllocationType = 3
EVRFilterConfigPrefs = Int32
EVRFilterConfigPrefs_EnableQoS: EVRFilterConfigPrefs = 1
EVRFilterConfigPrefs_Mask: EVRFilterConfigPrefs = 1
FILE_ACCESSMODE = Int32
ACCESSMODE_READ: FILE_ACCESSMODE = 1
ACCESSMODE_WRITE: FILE_ACCESSMODE = 2
ACCESSMODE_READWRITE: FILE_ACCESSMODE = 3
ACCESSMODE_WRITE_EXCLUSIVE: FILE_ACCESSMODE = 4
FILE_OPENMODE = Int32
OPENMODE_FAIL_IF_NOT_EXIST: FILE_OPENMODE = 0
OPENMODE_FAIL_IF_EXIST: FILE_OPENMODE = 1
OPENMODE_RESET_IF_EXIST: FILE_OPENMODE = 2
OPENMODE_APPEND_IF_EXIST: FILE_OPENMODE = 3
OPENMODE_DELETE_IF_EXIST: FILE_OPENMODE = 4
class IAdvancedMediaCapture(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0751585-d216-4344-b5bf-463b68f977bb}')
    @commethod(3)
    def GetAdvancedMediaCaptureSettings(self, value: POINTER(Windows.Win32.Media.MediaFoundation.IAdvancedMediaCaptureSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAdvancedMediaCaptureInitializationSettings(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3de21209-8ba6-4f2a-a577-2819b56ff14d}')
    @commethod(3)
    def SetDirectxDeviceManager(self, value: Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAdvancedMediaCaptureSettings(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24e0485f-a33e-4aa1-b564-6019b1d14f65}')
    @commethod(3)
    def GetDirectxDeviceManager(self, value: POINTER(Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSourceProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ebbaf249-afc2-4582-91c6-b60df2e84954}')
    @commethod(3)
    def ProvideInput(self, dwSampleCount: UInt32, pdwChannelCount: POINTER(UInt32), pInterleavedAudioData: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IClusterDetector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3f07f7b7-c680-41d9-9423-915107ec9ff9}')
    @commethod(3)
    def Initialize(self, wBaseEntryLevel: UInt16, wClusterEntryLevel: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Detect(self, dwMaxNumClusters: UInt32, fMinClusterDuration: Single, fMaxClusterDuration: Single, pSrcToc: Windows.Win32.Media.MediaFoundation.IToc_head, ppDstToc: POINTER(Windows.Win32.Media.MediaFoundation.IToc_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICodecAPI(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{901db4c7-31ce-41a2-85dc-8fa0bf41b8da}')
    @commethod(3)
    def IsSupported(self, Api: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsModifiable(self, Api: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParameterRange(self, Api: POINTER(Guid), ValueMin: POINTER(Windows.Win32.System.Variant.VARIANT_head), ValueMax: POINTER(Windows.Win32.System.Variant.VARIANT_head), SteppingDelta: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetParameterValues(self, Api: POINTER(Guid), Values: POINTER(POINTER(Windows.Win32.System.Variant.VARIANT_head)), ValuesCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultValue(self, Api: POINTER(Guid), Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetValue(self, Api: POINTER(Guid), Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValue(self, Api: POINTER(Guid), Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterForEvent(self, Api: POINTER(Guid), userData: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterForEvent(self, Api: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetAllDefaults(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetValueWithNotify(self, Api: POINTER(Guid), Value: POINTER(Windows.Win32.System.Variant.VARIANT_head), ChangedParam: POINTER(POINTER(Guid)), ChangedParamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetAllDefaultsWithNotify(self, ChangedParam: POINTER(POINTER(Guid)), ChangedParamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetAllSettings(self, __MIDL__ICodecAPI0000: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetAllSettings(self, __MIDL__ICodecAPI0001: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetAllSettingsWithNotify(self, __MIDL__ICodecAPI0002: Windows.Win32.System.Com.IStream_head, ChangedParam: POINTER(POINTER(Guid)), ChangedParamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoDecodeCommandList(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12CommandList
    _iid_ = Guid('{3b60536e-ad29-4e64-a269-f853837e5e53}')
    @commethod(9)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self, pAllocator: Windows.Win32.Graphics.Direct3D12.ID3D12CommandAllocator_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearState(self) -> Void: ...
    @commethod(12)
    def ResourceBarrier(self, NumBarriers: UInt32, pBarriers: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_BARRIER_head)) -> Void: ...
    @commethod(13)
    def DiscardResource(self, pResource: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pRegion: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_DISCARD_REGION_head)) -> Void: ...
    @commethod(14)
    def BeginQuery(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, Index: UInt32) -> Void: ...
    @commethod(15)
    def EndQuery(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, Index: UInt32) -> Void: ...
    @commethod(16)
    def ResolveQueryData(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, StartIndex: UInt32, NumQueries: UInt32, pDestinationBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, AlignedDestinationBufferOffset: UInt64) -> Void: ...
    @commethod(17)
    def SetPredication(self, pBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, AlignedBufferOffset: UInt64, Operation: Windows.Win32.Graphics.Direct3D12.D3D12_PREDICATION_OP) -> Void: ...
    @commethod(18)
    def SetMarker(self, Metadata: UInt32, pData: c_void_p, Size: UInt32) -> Void: ...
    @commethod(19)
    def BeginEvent(self, Metadata: UInt32, pData: c_void_p, Size: UInt32) -> Void: ...
    @commethod(20)
    def EndEvent(self) -> Void: ...
    @commethod(21)
    def DecodeFrame(self, pDecoder: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecoder_head, pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS_head), pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_head)) -> Void: ...
    @commethod(22)
    def WriteBufferImmediate(self, Count: UInt32, pParams: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_WRITEBUFFERIMMEDIATE_PARAMETER_head), pModes: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_WRITEBUFFERIMMEDIATE_MODE)) -> Void: ...
class ID3D12VideoDecodeCommandList1(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecodeCommandList
    _iid_ = Guid('{d52f011b-b56e-453c-a05a-a7f311c8f472}')
    @commethod(23)
    def DecodeFrame1(self, pDecoder: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecoder_head, pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1_head), pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_head)) -> Void: ...
class ID3D12VideoDecodeCommandList2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecodeCommandList1
    _iid_ = Guid('{6e120880-c114-4153-8036-d247051e1729}')
    @commethod(24)
    def SetProtectedResourceSession(self, pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head) -> Void: ...
    @commethod(25)
    def InitializeExtensionCommand(self, pExtensionCommand: Windows.Win32.Media.MediaFoundation.ID3D12VideoExtensionCommand_head, pInitializationParameters: c_void_p, InitializationParametersSizeInBytes: UIntPtr) -> Void: ...
    @commethod(26)
    def ExecuteExtensionCommand(self, pExtensionCommand: Windows.Win32.Media.MediaFoundation.ID3D12VideoExtensionCommand_head, pExecutionParameters: c_void_p, ExecutionParametersSizeInBytes: UIntPtr) -> Void: ...
class ID3D12VideoDecodeCommandList3(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecodeCommandList2
    _iid_ = Guid('{2aee8c37-9562-42da-8abf-61efeb2e4513}')
    @commethod(27)
    def Barrier(self, NumBarrierGroups: UInt32, pBarrierGroups: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_BARRIER_GROUP_head)) -> Void: ...
class ID3D12VideoDecoder(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{c59b6bdc-7720-4074-a136-17a156037470}')
    @commethod(8)
    def GetDesc(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_DESC: ...
class ID3D12VideoDecoder1(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecoder
    _iid_ = Guid('{79a2e5fb-ccd2-469a-9fde-195d10951f7e}')
    @commethod(9)
    def GetProtectedResourceSession(self, riid: POINTER(Guid), ppProtectedSession: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoDecoderHeap(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{0946b7c9-ebf6-4047-bb73-8683e27dbb1f}')
    @commethod(8)
    def GetDesc(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_HEAP_DESC: ...
class ID3D12VideoDecoderHeap1(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDecoderHeap
    _iid_ = Guid('{da1d98c5-539f-41b2-bf6b-1198a03b6d26}')
    @commethod(9)
    def GetProtectedResourceSession(self, riid: POINTER(Guid), ppProtectedSession: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoDevice(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f052807-0b46-4acc-8a89-364f793718a4}')
    @commethod(3)
    def CheckFeatureSupport(self, FeatureVideo: Windows.Win32.Media.MediaFoundation.D3D12_FEATURE_VIDEO, pFeatureSupportData: c_void_p, FeatureSupportDataSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateVideoDecoder(self, pDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_DESC_head), riid: POINTER(Guid), ppVideoDecoder: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateVideoDecoderHeap(self, pVideoDecoderHeapDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_HEAP_DESC_head), riid: POINTER(Guid), ppVideoDecoderHeap: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateVideoProcessor(self, NodeMask: UInt32, pOutputStreamDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC_head), NumInputStreamDescs: UInt32, pInputStreamDescs: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC_head), riid: POINTER(Guid), ppVideoProcessor: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoDevice1(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDevice
    _iid_ = Guid('{981611ad-a144-4c83-9890-f30e26d658ab}')
    @commethod(7)
    def CreateVideoMotionEstimator(self, pDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_DESC_head), pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, riid: POINTER(Guid), ppVideoMotionEstimator: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateVideoMotionVectorHeap(self, pDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_VECTOR_HEAP_DESC_head), pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, riid: POINTER(Guid), ppVideoMotionVectorHeap: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoDevice2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDevice1
    _iid_ = Guid('{f019ac49-f838-4a95-9b17-579437c8f513}')
    @commethod(9)
    def CreateVideoDecoder1(self, pDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_DESC_head), pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, riid: POINTER(Guid), ppVideoDecoder: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateVideoDecoderHeap1(self, pVideoDecoderHeapDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_DECODER_HEAP_DESC_head), pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, riid: POINTER(Guid), ppVideoDecoderHeap: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateVideoProcessor1(self, NodeMask: UInt32, pOutputStreamDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC_head), NumInputStreamDescs: UInt32, pInputStreamDescs: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC_head), pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, riid: POINTER(Guid), ppVideoProcessor: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateVideoExtensionCommand(self, pDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_DESC_head), pCreationParameters: c_void_p, CreationParametersDataSizeInBytes: UIntPtr, pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head, riid: POINTER(Guid), ppVideoExtensionCommand: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ExecuteExtensionCommand(self, pExtensionCommand: Windows.Win32.Media.MediaFoundation.ID3D12VideoExtensionCommand_head, pExecutionParameters: c_void_p, ExecutionParametersSizeInBytes: UIntPtr, pOutputData: c_void_p, OutputDataSizeInBytes: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoDevice3(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoDevice2
    _iid_ = Guid('{4243adb4-3a32-4666-973c-0ccc5625dc44}')
    @commethod(14)
    def CreateVideoEncoder(self, pDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_DESC_head), riid: POINTER(Guid), ppVideoEncoder: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateVideoEncoderHeap(self, pDesc: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_HEAP_DESC_head), riid: POINTER(Guid), ppVideoEncoderHeap: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoEncodeCommandList(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12CommandList
    _iid_ = Guid('{8455293a-0cbd-4831-9b39-fbdbab724723}')
    @commethod(9)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self, pAllocator: Windows.Win32.Graphics.Direct3D12.ID3D12CommandAllocator_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearState(self) -> Void: ...
    @commethod(12)
    def ResourceBarrier(self, NumBarriers: UInt32, pBarriers: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_BARRIER_head)) -> Void: ...
    @commethod(13)
    def DiscardResource(self, pResource: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pRegion: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_DISCARD_REGION_head)) -> Void: ...
    @commethod(14)
    def BeginQuery(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, Index: UInt32) -> Void: ...
    @commethod(15)
    def EndQuery(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, Index: UInt32) -> Void: ...
    @commethod(16)
    def ResolveQueryData(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, StartIndex: UInt32, NumQueries: UInt32, pDestinationBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, AlignedDestinationBufferOffset: UInt64) -> Void: ...
    @commethod(17)
    def SetPredication(self, pBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, AlignedBufferOffset: UInt64, Operation: Windows.Win32.Graphics.Direct3D12.D3D12_PREDICATION_OP) -> Void: ...
    @commethod(18)
    def SetMarker(self, Metadata: UInt32, pData: c_void_p, Size: UInt32) -> Void: ...
    @commethod(19)
    def BeginEvent(self, Metadata: UInt32, pData: c_void_p, Size: UInt32) -> Void: ...
    @commethod(20)
    def EndEvent(self) -> Void: ...
    @commethod(21)
    def EstimateMotion(self, pMotionEstimator: Windows.Win32.Media.MediaFoundation.ID3D12VideoMotionEstimator_head, pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_OUTPUT_head), pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_INPUT_head)) -> Void: ...
    @commethod(22)
    def ResolveMotionVectorHeap(self, pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_OUTPUT_head), pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_INPUT_head)) -> Void: ...
    @commethod(23)
    def WriteBufferImmediate(self, Count: UInt32, pParams: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_WRITEBUFFERIMMEDIATE_PARAMETER_head), pModes: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_WRITEBUFFERIMMEDIATE_MODE)) -> Void: ...
    @commethod(24)
    def SetProtectedResourceSession(self, pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head) -> Void: ...
class ID3D12VideoEncodeCommandList1(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoEncodeCommandList
    _iid_ = Guid('{94971eca-2bdb-4769-88cf-3675ea757ebc}')
    @commethod(25)
    def InitializeExtensionCommand(self, pExtensionCommand: Windows.Win32.Media.MediaFoundation.ID3D12VideoExtensionCommand_head, pInitializationParameters: c_void_p, InitializationParametersSizeInBytes: UIntPtr) -> Void: ...
    @commethod(26)
    def ExecuteExtensionCommand(self, pExtensionCommand: Windows.Win32.Media.MediaFoundation.ID3D12VideoExtensionCommand_head, pExecutionParameters: c_void_p, ExecutionParametersSizeInBytes: UIntPtr) -> Void: ...
class ID3D12VideoEncodeCommandList2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoEncodeCommandList1
    _iid_ = Guid('{895491e2-e701-46a9-9a1f-8d3480ed867a}')
    @commethod(27)
    def EncodeFrame(self, pEncoder: Windows.Win32.Media.MediaFoundation.ID3D12VideoEncoder_head, pHeap: Windows.Win32.Media.MediaFoundation.ID3D12VideoEncoderHeap_head, pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_ENCODEFRAME_INPUT_ARGUMENTS_head), pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_ENCODEFRAME_OUTPUT_ARGUMENTS_head)) -> Void: ...
    @commethod(28)
    def ResolveEncoderOutputMetadata(self, pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RESOLVE_METADATA_INPUT_ARGUMENTS_head), pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_RESOLVE_METADATA_OUTPUT_ARGUMENTS_head)) -> Void: ...
class ID3D12VideoEncodeCommandList3(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoEncodeCommandList2
    _iid_ = Guid('{7f027b22-1515-4e85-aa0d-026486580576}')
    @commethod(29)
    def Barrier(self, NumBarrierGroups: UInt32, pBarrierGroups: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_BARRIER_GROUP_head)) -> Void: ...
class ID3D12VideoEncoder(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{2e0d212d-8df9-44a6-a770-bb289b182737}')
    @commethod(8)
    def GetNodeMask(self) -> UInt32: ...
    @commethod(9)
    def GetEncoderFlags(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_FLAGS: ...
    @commethod(10)
    def GetCodec(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC: ...
    @commethod(11)
    def GetCodecProfile(self, dstProfile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCodecConfiguration(self, dstCodecConfig: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInputFormat(self) -> Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT: ...
    @commethod(14)
    def GetMaxMotionEstimationPrecision(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE: ...
class ID3D12VideoEncoderHeap(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{22b35d96-876a-44c0-b25e-fb8c9c7f1c4a}')
    @commethod(8)
    def GetNodeMask(self) -> UInt32: ...
    @commethod(9)
    def GetEncoderHeapFlags(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_HEAP_FLAGS: ...
    @commethod(10)
    def GetCodec(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_CODEC: ...
    @commethod(11)
    def GetCodecProfile(self, dstProfile: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PROFILE_DESC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCodecLevel(self, dstLevel: Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_LEVEL_SETTING) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetResolutionListCount(self) -> UInt32: ...
    @commethod(14)
    def GetResolutionList(self, ResolutionsListCount: UInt32, pResolutionList: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoExtensionCommand(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{554e41e8-ae8e-4a8c-b7d2-5b4f274a30e4}')
    @commethod(8)
    def GetDesc(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_EXTENSION_COMMAND_DESC: ...
    @commethod(9)
    def GetProtectedResourceSession(self, riid: POINTER(Guid), ppProtectedSession: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoMotionEstimator(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{33fdae0e-098b-428f-87bb-34b695de08f8}')
    @commethod(8)
    def GetDesc(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_ESTIMATOR_DESC: ...
    @commethod(9)
    def GetProtectedResourceSession(self, riid: POINTER(Guid), ppProtectedSession: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoMotionVectorHeap(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{5be17987-743a-4061-834b-23d22daea505}')
    @commethod(8)
    def GetDesc(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_MOTION_VECTOR_HEAP_DESC: ...
    @commethod(9)
    def GetProtectedResourceSession(self, riid: POINTER(Guid), ppProtectedSession: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ID3D12VideoProcessCommandList(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12CommandList
    _iid_ = Guid('{aeb2543a-167f-4682-acc8-d159ed4a6209}')
    @commethod(9)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reset(self, pAllocator: Windows.Win32.Graphics.Direct3D12.ID3D12CommandAllocator_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ClearState(self) -> Void: ...
    @commethod(12)
    def ResourceBarrier(self, NumBarriers: UInt32, pBarriers: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_RESOURCE_BARRIER_head)) -> Void: ...
    @commethod(13)
    def DiscardResource(self, pResource: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, pRegion: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_DISCARD_REGION_head)) -> Void: ...
    @commethod(14)
    def BeginQuery(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, Index: UInt32) -> Void: ...
    @commethod(15)
    def EndQuery(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, Index: UInt32) -> Void: ...
    @commethod(16)
    def ResolveQueryData(self, pQueryHeap: Windows.Win32.Graphics.Direct3D12.ID3D12QueryHeap_head, Type: Windows.Win32.Graphics.Direct3D12.D3D12_QUERY_TYPE, StartIndex: UInt32, NumQueries: UInt32, pDestinationBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, AlignedDestinationBufferOffset: UInt64) -> Void: ...
    @commethod(17)
    def SetPredication(self, pBuffer: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, AlignedBufferOffset: UInt64, Operation: Windows.Win32.Graphics.Direct3D12.D3D12_PREDICATION_OP) -> Void: ...
    @commethod(18)
    def SetMarker(self, Metadata: UInt32, pData: c_void_p, Size: UInt32) -> Void: ...
    @commethod(19)
    def BeginEvent(self, Metadata: UInt32, pData: c_void_p, Size: UInt32) -> Void: ...
    @commethod(20)
    def EndEvent(self) -> Void: ...
    @commethod(21)
    def ProcessFrames(self, pVideoProcessor: Windows.Win32.Media.MediaFoundation.ID3D12VideoProcessor_head, pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS_head), NumInputStreams: UInt32, pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_head)) -> Void: ...
    @commethod(22)
    def WriteBufferImmediate(self, Count: UInt32, pParams: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_WRITEBUFFERIMMEDIATE_PARAMETER_head), pModes: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_WRITEBUFFERIMMEDIATE_MODE)) -> Void: ...
class ID3D12VideoProcessCommandList1(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoProcessCommandList
    _iid_ = Guid('{542c5c4d-7596-434f-8c93-4efa6766f267}')
    @commethod(23)
    def ProcessFrames1(self, pVideoProcessor: Windows.Win32.Media.MediaFoundation.ID3D12VideoProcessor_head, pOutputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS_head), NumInputStreams: UInt32, pInputArguments: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS1_head)) -> Void: ...
class ID3D12VideoProcessCommandList2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoProcessCommandList1
    _iid_ = Guid('{db525ae4-6ad6-473c-baa7-59b2e37082e4}')
    @commethod(24)
    def SetProtectedResourceSession(self, pProtectedResourceSession: Windows.Win32.Graphics.Direct3D12.ID3D12ProtectedResourceSession_head) -> Void: ...
    @commethod(25)
    def InitializeExtensionCommand(self, pExtensionCommand: Windows.Win32.Media.MediaFoundation.ID3D12VideoExtensionCommand_head, pInitializationParameters: c_void_p, InitializationParametersSizeInBytes: UIntPtr) -> Void: ...
    @commethod(26)
    def ExecuteExtensionCommand(self, pExtensionCommand: Windows.Win32.Media.MediaFoundation.ID3D12VideoExtensionCommand_head, pExecutionParameters: c_void_p, ExecutionParametersSizeInBytes: UIntPtr) -> Void: ...
class ID3D12VideoProcessCommandList3(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoProcessCommandList2
    _iid_ = Guid('{1a0a4ca4-9f08-40ce-9558-b411fd2666ff}')
    @commethod(27)
    def Barrier(self, NumBarrierGroups: UInt32, pBarrierGroups: POINTER(Windows.Win32.Graphics.Direct3D12.D3D12_BARRIER_GROUP_head)) -> Void: ...
class ID3D12VideoProcessor(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D12.ID3D12Pageable
    _iid_ = Guid('{304fdb32-bede-410a-8545-943ac6a46138}')
    @commethod(8)
    def GetNodeMask(self) -> UInt32: ...
    @commethod(9)
    def GetNumInputStreamDescs(self) -> UInt32: ...
    @commethod(10)
    def GetInputStreamDescs(self, NumInputStreamDescs: UInt32, pInputStreamDescs: POINTER(Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputStreamDesc(self) -> Windows.Win32.Media.MediaFoundation.D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC: ...
class ID3D12VideoProcessor1(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.ID3D12VideoProcessor
    _iid_ = Guid('{f3cfe615-553f-425c-86d8-ee8c1b1fb01c}')
    @commethod(12)
    def GetProtectedResourceSession(self, riid: POINTER(Guid), ppProtectedSession: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDXVAHD_Device(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95f12dfd-d77e-49be-815f-57d579634d6d}')
    @commethod(3)
    def CreateVideoSurface(self, Width: UInt32, Height: UInt32, Format: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, Pool: Windows.Win32.Graphics.Direct3D9.D3DPOOL, Usage: UInt32, Type: Windows.Win32.Media.MediaFoundation.DXVAHD_SURFACE_TYPE, NumSurfaces: UInt32, ppSurfaces: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head), pSharedHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVideoProcessorDeviceCaps(self, pCaps: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_VPDEVCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVideoProcessorOutputFormats(self, Count: UInt32, pFormats: POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVideoProcessorInputFormats(self, Count: UInt32, pFormats: POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetVideoProcessorCaps(self, Count: UInt32, pCaps: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_VPCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVideoProcessorCustomRates(self, pVPGuid: POINTER(Guid), Count: UInt32, pRates: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CUSTOM_RATE_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetVideoProcessorFilterRange(self, Filter: Windows.Win32.Media.MediaFoundation.DXVAHD_FILTER, pRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_FILTER_RANGE_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateVideoProcessor(self, pVPGuid: POINTER(Guid), ppVideoProcessor: POINTER(Windows.Win32.Media.MediaFoundation.IDXVAHD_VideoProcessor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDXVAHD_VideoProcessor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95f4edf4-6e03-4cd7-be1b-3075d665aa52}')
    @commethod(3)
    def SetVideoProcessBltState(self, State: Windows.Win32.Media.MediaFoundation.DXVAHD_BLT_STATE, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVideoProcessBltState(self, State: Windows.Win32.Media.MediaFoundation.DXVAHD_BLT_STATE, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetVideoProcessStreamState(self, StreamNumber: UInt32, State: Windows.Win32.Media.MediaFoundation.DXVAHD_STREAM_STATE, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVideoProcessStreamState(self, StreamNumber: UInt32, State: Windows.Win32.Media.MediaFoundation.DXVAHD_STREAM_STATE, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def VideoProcessBltHD(self, pOutputSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, OutputFrame: UInt32, StreamCount: UInt32, pStreams: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_STREAM_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirect3D9ExOverlayExtension(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{187aeb13-aaf5-4c59-876d-e059088c0df8}')
    @commethod(3)
    def CheckDeviceOverlayType(self, Adapter: UInt32, DevType: Windows.Win32.Graphics.Direct3D9.D3DDEVTYPE, OverlayWidth: UInt32, OverlayHeight: UInt32, OverlayFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, pDisplayMode: POINTER(Windows.Win32.Graphics.Direct3D9.D3DDISPLAYMODEEX_head), DisplayRotation: Windows.Win32.Graphics.Direct3D9.D3DDISPLAYROTATION, pOverlayCaps: POINTER(Windows.Win32.Media.MediaFoundation.D3DOVERLAYCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirect3DAuthenticatedChannel9(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ff24beee-da21-4beb-98b5-d2f899f98af9}')
    @commethod(3)
    def GetCertificateSize(self, pCertificateSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCertificate(self, CertifacteSize: UInt32, ppCertificate: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NegotiateKeyExchange(self, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Query(self, InputSize: UInt32, pInput: c_void_p, OutputSize: UInt32, pOutput: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Configure(self, InputSize: UInt32, pInput: c_void_p, pOutput: POINTER(Windows.Win32.Graphics.Direct3D9.D3DAUTHENTICATEDCHANNEL_CONFIGURE_OUTPUT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirect3DCryptoSession9(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa0ab799-7a9c-48ca-8c5b-237e71a54434}')
    @commethod(3)
    def GetCertificateSize(self, pCertificateSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCertificate(self, CertifacteSize: UInt32, ppCertificate: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NegotiateKeyExchange(self, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EncryptionBlt(self, pSrcSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, pDstSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, DstSurfaceSize: UInt32, pIV: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DecryptionBlt(self, pSrcSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, pDstSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, SrcSurfaceSize: UInt32, pEncryptedBlockInfo: POINTER(Windows.Win32.Graphics.Direct3D9.D3DENCRYPTED_BLOCK_INFO_head), pContentKey: c_void_p, pIV: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSurfacePitch(self, pSrcSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, pSurfacePitch: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StartSessionKeyRefresh(self, pRandomNumber: c_void_p, RandomNumberSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FinishSessionKeyRefresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEncryptionBltKey(self, pReadbackKey: c_void_p, KeySize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDirect3DDevice9Video(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26dc4561-a1ee-4ae7-96da-118a36c0ec95}')
    @commethod(3)
    def GetContentProtectionCaps(self, pCryptoType: POINTER(Guid), pDecodeProfile: POINTER(Guid), pCaps: POINTER(Windows.Win32.Media.MediaFoundation.D3DCONTENTPROTECTIONCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateAuthenticatedChannel(self, ChannelType: Windows.Win32.Graphics.Direct3D9.D3DAUTHENTICATEDCHANNELTYPE, ppAuthenticatedChannel: POINTER(Windows.Win32.Media.MediaFoundation.IDirect3DAuthenticatedChannel9_head), pChannelHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateCryptoSession(self, pCryptoType: POINTER(Guid), pDecodeProfile: POINTER(Guid), ppCryptoSession: POINTER(Windows.Win32.Media.MediaFoundation.IDirect3DCryptoSession9_head), pCryptoHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirect3DDeviceManager9(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0cade0f-06d5-4cf4-a1c7-f3cdd725aa75}')
    @commethod(3)
    def ResetDevice(self, pDevice: Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9_head, resetToken: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenDeviceHandle(self, phDevice: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CloseDeviceHandle(self, hDevice: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TestDevice(self, hDevice: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockDevice(self, hDevice: Windows.Win32.Foundation.HANDLE, ppDevice: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9_head), fBlock: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnlockDevice(self, hDevice: Windows.Win32.Foundation.HANDLE, fSaveState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetVideoService(self, hDevice: Windows.Win32.Foundation.HANDLE, riid: POINTER(Guid), ppService: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectXVideoAccelerationService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc51a550-d5e7-11d9-af55-00054e43ff02}')
    @commethod(3)
    def CreateSurface(self, Width: UInt32, Height: UInt32, BackBuffers: UInt32, Format: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, Pool: Windows.Win32.Graphics.Direct3D9.D3DPOOL, Usage: UInt32, DxvaType: Windows.Win32.Media.MediaFoundation.DXVA2_VideoRenderTargetType, ppSurface: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head), pSharedHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectXVideoDecoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f2b0810a-fd00-43c9-918c-df94e2d8ef7d}')
    @commethod(3)
    def GetVideoDecoderService(self, ppService: POINTER(Windows.Win32.Media.MediaFoundation.IDirectXVideoDecoderService_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCreationParameters(self, pDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), pConfig: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ConfigPictureDecode_head), pDecoderRenderTargets: POINTER(POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head)), pNumSurfaces: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBuffer(self, BufferType: Windows.Win32.Media.MediaFoundation.DXVA2_BufferfType, ppBuffer: POINTER(c_void_p), pBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReleaseBuffer(self, BufferType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginFrame(self, pRenderTarget: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, pvPVPData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EndFrame(self, pHandleComplete: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Execute(self, pExecuteParams: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_DecodeExecuteParams_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectXVideoDecoderService(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IDirectXVideoAccelerationService
    _iid_ = Guid('{fc51a551-d5e7-11d9-af55-00054e43ff02}')
    @commethod(4)
    def GetDecoderDeviceGuids(self, pCount: POINTER(UInt32), pGuids: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDecoderRenderTargets(self, Guid: POINTER(Guid), pCount: POINTER(UInt32), pFormats: POINTER(POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDecoderConfigurations(self, Guid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), pReserved: c_void_p, pCount: POINTER(UInt32), ppConfigs: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ConfigPictureDecode_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateVideoDecoder(self, Guid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), pConfig: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ConfigPictureDecode_head), ppDecoderRenderTargets: POINTER(Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head), NumRenderTargets: UInt32, ppDecode: POINTER(Windows.Win32.Media.MediaFoundation.IDirectXVideoDecoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectXVideoMemoryConfiguration(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7f916dd-db3b-49c1-84d7-e45ef99ec726}')
    @commethod(3)
    def GetAvailableSurfaceTypeByIndex(self, dwTypeIndex: UInt32, pdwType: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_SurfaceType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSurfaceType(self, dwType: Windows.Win32.Media.MediaFoundation.DXVA2_SurfaceType) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectXVideoProcessor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8c3a39f0-916e-4690-804f-4c8001355d25}')
    @commethod(3)
    def GetVideoProcessorService(self, ppService: POINTER(Windows.Win32.Media.MediaFoundation.IDirectXVideoProcessorService_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCreationParameters(self, pDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), pRenderTargetFormat: POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT), pMaxNumSubStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVideoProcessorCaps(self, pCaps: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoProcessorCaps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProcAmpRange(self, ProcAmpCap: UInt32, pRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFilterPropertyRange(self, FilterSetting: UInt32, pRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def VideoProcessBlt(self, pRenderTarget: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, pBltParams: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoProcessBltParams_head), pSamples: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoSample_head), NumSamples: UInt32, pHandleComplete: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IDirectXVideoProcessorService(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IDirectXVideoAccelerationService
    _iid_ = Guid('{fc51a552-d5e7-11d9-af55-00054e43ff02}')
    @commethod(4)
    def RegisterVideoProcessorSoftwareDevice(self, pCallbacks: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVideoProcessorDeviceGuids(self, pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), pCount: POINTER(UInt32), pGuids: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVideoProcessorRenderTargets(self, VideoProcDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), pCount: POINTER(UInt32), pFormats: POINTER(POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetVideoProcessorSubStreamFormats(self, VideoProcDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, pCount: POINTER(UInt32), pFormats: POINTER(POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVideoProcessorCaps(self, VideoProcDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, pCaps: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoProcessorCaps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProcAmpRange(self, VideoProcDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, ProcAmpCap: UInt32, pRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilterPropertyRange(self, VideoProcDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, FilterSetting: UInt32, pRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateVideoProcessor(self, VideoProcDeviceGuid: POINTER(Guid), pVideoDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoDesc_head), RenderTargetFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT, MaxNumSubStreams: UInt32, ppVidProcess: POINTER(Windows.Win32.Media.MediaFoundation.IDirectXVideoProcessor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEVRFilterConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83e91e85-82c1-4ea7-801d-85dc50b75086}')
    @commethod(3)
    def SetNumberOfStreams(self, dwMaxStreams: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberOfStreams(self, pdwMaxStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEVRFilterConfigEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IEVRFilterConfig
    _iid_ = Guid('{aea36028-796d-454f-beee-b48071e24304}')
    @commethod(5)
    def SetConfigPrefs(self, dwConfigFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetConfigPrefs(self, pdwConfigFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEVRTrustedVideoPlugin(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{83a4ce40-7710-494b-a893-a472049af630}')
    @commethod(3)
    def IsInTrustedVideoMode(self, pYes: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CanConstrict(self, pYes: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetConstriction(self, dwKPix: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisableImageExport(self, bDisable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IEVRVideoStreamControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0cfe38b-93e7-4772-8957-0400c49a4485}')
    @commethod(3)
    def SetStreamActiveState(self, fActive: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamActiveState(self, lpfActive: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IFileClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bfccd196-1244-4840-ab44-480975c4ffe4}')
    @commethod(3)
    def GetObjectDiskSize(self, pqwSize: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, pFio: Windows.Win32.Media.MediaFoundation.IFileIo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Read(self, pFio: Windows.Win32.Media.MediaFoundation.IFileIo_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFileIo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11993196-1244-4840-ab44-480975c4ffe4}')
    @commethod(3)
    def Initialize(self, eAccessMode: Windows.Win32.Media.MediaFoundation.FILE_ACCESSMODE, eOpenMode: Windows.Win32.Media.MediaFoundation.FILE_OPENMODE, pwszFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pqwLength: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLength(self, qwLength: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentPosition(self, pqwPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCurrentPosition(self, qwPosition: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsEndOfStream(self, pbEndOfStream: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Read(self, pbt: POINTER(Byte), ul: UInt32, pulRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Write(self, pbt: POINTER(Byte), ul: UInt32, pulWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Seek(self, eSeekOrigin: Windows.Win32.Media.MediaFoundation.SEEK_ORIGIN, qwSeekOffset: UInt64, dwSeekFlags: UInt32, pqwCurrentPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMF2DBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7dc9d5f9-9ed9-44ec-9bbf-0600bb589fbb}')
    @commethod(3)
    def Lock2D(self, ppbScanline0: POINTER(POINTER(Byte)), plPitch: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unlock2D(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetScanline0AndPitch(self, pbScanline0: POINTER(POINTER(Byte)), plPitch: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsContiguousFormat(self, pfIsContiguous: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetContiguousLength(self, pcbLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ContiguousCopyTo(self, pbDestBuffer: POINTER(Byte), cbDestBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ContiguousCopyFrom(self, pbSrcBuffer: POINTER(Byte), cbSrcBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMF2DBuffer2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMF2DBuffer
    _iid_ = Guid('{33ae5ea6-4316-436f-8ddd-d73d22f829ec}')
    @commethod(10)
    def Lock2DSize(self, lockFlags: Windows.Win32.Media.MediaFoundation.MF2DBuffer_LockFlags, ppbScanline0: POINTER(POINTER(Byte)), plPitch: POINTER(Int32), ppbBufferStart: POINTER(POINTER(Byte)), pcbBufferLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Copy2DTo(self, pDestBuffer: Windows.Win32.Media.MediaFoundation.IMF2DBuffer2_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFContentInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b1dca5cd-d5da-4451-8e9e-db5c59914ead}')
    @commethod(3)
    def GetHeaderSize(self, pIStartOfContent: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head, cbHeaderSize: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ParseHeader(self, pIHeaderBuffer: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head, cbOffsetWithinHeader: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GenerateHeader(self, pIHeader: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head, pcbHeader: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProfile(self, ppIProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetProfile(self, pIProfile: Windows.Win32.Media.MediaFoundation.IMFASFProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GeneratePresentationDescriptor(self, ppIPresentationDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEncodingConfigurationPropertyStore(self, wStreamNumber: UInt16, ppIStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFIndexer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53590f48-dc3b-4297-813f-787761ad7b3e}')
    @commethod(3)
    def SetFlags(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Initialize(self, pIContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIndexPosition(self, pIContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head, pcbIndexOffset: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetIndexByteStreams(self, ppIByteStreams: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head), cByteStreams: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIndexByteStreamCount(self, pcByteStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetIndexStatus(self, pIndexIdentifier: POINTER(Windows.Win32.Media.MediaFoundation.ASF_INDEX_IDENTIFIER_head), pfIsIndexed: POINTER(Windows.Win32.Foundation.BOOL), pbIndexDescriptor: POINTER(Byte), pcbIndexDescriptor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetIndexStatus(self, pbIndexDescriptor: POINTER(Byte), cbIndexDescriptor: UInt32, fGenerateIndex: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSeekPositionForValue(self, pvarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pIndexIdentifier: POINTER(Windows.Win32.Media.MediaFoundation.ASF_INDEX_IDENTIFIER_head), pcbOffsetWithinData: POINTER(UInt64), phnsApproxTime: POINTER(Int64), pdwPayloadNumberOfStreamWithinPacket: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GenerateIndexEntries(self, pIASFPacketSample: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CommitIndex(self, pIContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetIndexWriteSpace(self, pcbIndexWriteSpace: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCompletedIndex(self, pIIndexBuffer: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head, cbOffsetWithinIndex: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFMultiplexer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{57bdd80a-9b38-4838-b737-c58f670d7d4f}')
    @commethod(3)
    def Initialize(self, pIContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFlags(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ProcessSample(self, wStreamNumber: UInt16, pISample: Windows.Win32.Media.MediaFoundation.IMFSample_head, hnsTimestampAdjust: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNextPacket(self, pdwStatusFlags: POINTER(UInt32), ppIPacket: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def End(self, pIContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStatistics(self, wStreamNumber: UInt16, pMuxStats: POINTER(Windows.Win32.Media.MediaFoundation.ASF_MUX_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSyncTolerance(self, msSyncTolerance: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFMutualExclusion(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{12558291-e399-11d5-bc2a-00b0d0f3f4ab}')
    @commethod(3)
    def GetType(self, pguidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetType(self, guidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecordCount(self, pdwRecordCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamsForRecord(self, dwRecordNumber: UInt32, pwStreamNumArray: POINTER(UInt16), pcStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddStreamForRecord(self, dwRecordNumber: UInt32, wStreamNumber: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveStreamFromRecord(self, dwRecordNumber: UInt32, wStreamNumber: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveRecord(self, dwRecordNumber: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddRecord(self, pdwRecordNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, ppIMutex: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFMutualExclusion_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFProfile(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{d267bf6a-028b-4e0d-903d-43f0ef82d0d4}')
    @commethod(33)
    def GetStreamCount(self, pcStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetStream(self, dwStreamIndex: UInt32, pwStreamNumber: POINTER(UInt16), ppIStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetStreamByNumber(self, wStreamNumber: UInt16, ppIStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetStream(self, pIStream: Windows.Win32.Media.MediaFoundation.IMFASFStreamConfig_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def RemoveStream(self, wStreamNumber: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CreateStream(self, pIMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppIStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetMutualExclusionCount(self, pcMutexs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetMutualExclusion(self, dwMutexIndex: UInt32, ppIMutex: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFMutualExclusion_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def AddMutualExclusion(self, pIMutex: Windows.Win32.Media.MediaFoundation.IMFASFMutualExclusion_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def RemoveMutualExclusion(self, dwMutexIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def CreateMutualExclusion(self, ppIMutex: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFMutualExclusion_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetStreamPrioritization(self, ppIStreamPrioritization: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamPrioritization_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def AddStreamPrioritization(self, pIStreamPrioritization: Windows.Win32.Media.MediaFoundation.IMFASFStreamPrioritization_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def RemoveStreamPrioritization(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def CreateStreamPrioritization(self, ppIStreamPrioritization: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamPrioritization_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def Clone(self, ppIProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFSplitter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{12558295-e399-11d5-bc2a-00b0d0f3f4ab}')
    @commethod(3)
    def Initialize(self, pIContentInfo: Windows.Win32.Media.MediaFoundation.IMFASFContentInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFlags(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SelectStreams(self, pwStreamNumbers: POINTER(UInt16), wNumStreams: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSelectedStreams(self, pwStreamNumbers: POINTER(UInt16), pwNumStreams: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ParseData(self, pIBuffer: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head, cbBufferOffset: UInt32, cbLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextSample(self, pdwStatusFlags: POINTER(Windows.Win32.Media.MediaFoundation.ASF_STATUSFLAGS), pwStreamNumber: POINTER(UInt16), ppISample: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLastSendTime(self, pdwLastSendTime: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFStreamConfig(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{9e8ae8d2-dbbd-4200-9aca-06e6df484913}')
    @commethod(33)
    def GetStreamType(self, pguidStreamType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetStreamNumber(self) -> UInt16: ...
    @commethod(35)
    def SetStreamNumber(self, wStreamNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetMediaType(self, ppIMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetMediaType(self, pIMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetPayloadExtensionCount(self, pcPayloadExtensions: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetPayloadExtension(self, wPayloadExtensionNumber: UInt16, pguidExtensionSystemID: POINTER(Guid), pcbExtensionDataSize: POINTER(UInt16), pbExtensionSystemInfo: POINTER(Byte), pcbExtensionSystemInfo: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def AddPayloadExtension(self, guidExtensionSystemID: Guid, cbExtensionDataSize: UInt16, pbExtensionSystemInfo: POINTER(Byte), cbExtensionSystemInfo: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def RemoveAllPayloadExtensions(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Clone(self, ppIStreamConfig: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamConfig_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFStreamPrioritization(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{699bdc27-bbaf-49ff-8e38-9c39c9b5e088}')
    @commethod(3)
    def GetStreamCount(self, pdwStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStream(self, dwStreamIndex: UInt32, pwStreamNumber: POINTER(UInt16), pwStreamFlags: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddStream(self, wStreamNumber: UInt16, wStreamFlags: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveStream(self, dwStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Clone(self, ppIStreamPrioritization: POINTER(Windows.Win32.Media.MediaFoundation.IMFASFStreamPrioritization_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFASFStreamSelector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d01bad4a-4fa0-4a60-9349-c27e62da9d41}')
    @commethod(3)
    def GetStreamCount(self, pcStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputCount(self, pcOutputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputStreamCount(self, dwOutputNum: UInt32, pcStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputStreamNumbers(self, dwOutputNum: UInt32, rgwStreamNumbers: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputFromStream(self, wStreamNum: UInt16, pdwOutput: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputOverride(self, dwOutputNum: UInt32, pSelection: POINTER(Windows.Win32.Media.MediaFoundation.ASF_SELECTION_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputOverride(self, dwOutputNum: UInt32, Selection: Windows.Win32.Media.MediaFoundation.ASF_SELECTION_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOutputMutexCount(self, dwOutputNum: UInt32, pcMutexes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputMutex(self, dwOutputNum: UInt32, dwMutexNum: UInt32, ppMutex: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOutputMutexSelection(self, dwOutputNum: UInt32, dwMutexNum: UInt32, wSelectedRecord: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetBandwidthStepCount(self, pcStepCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetBandwidthStep(self, dwStepNum: UInt32, pdwBitrate: POINTER(UInt32), rgwStreamNumbers: POINTER(UInt16), rgSelections: POINTER(Windows.Win32.Media.MediaFoundation.ASF_SELECTION_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def BitrateToStepNumber(self, dwBitrate: UInt32, pdwStepNum: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStreamSelectorFlags(self, dwStreamSelectorFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFActivate(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{7fee9e9a-4a89-47a6-899c-b6a53a70fb67}')
    @commethod(33)
    def ActivateObject(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def ShutdownObject(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def DetachObject(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFAsyncCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a27003cf-2354-4f2a-8d6a-ab7cff15437e}')
    @commethod(3)
    def GetParameters(self, pdwFlags: POINTER(UInt32), pdwQueue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Invoke(self, pAsyncResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFAsyncCallbackLogging(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback
    _iid_ = Guid('{c7a4dca1-f5f0-47b6-b92b-bf0106d25791}')
    @commethod(5)
    def GetObjectPointer(self) -> c_void_p: ...
    @commethod(6)
    def GetObjectTag(self) -> UInt32: ...
class IMFAsyncResult(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ac6b7889-0740-4d51-8619-905994a55cc6}')
    @commethod(3)
    def GetState(self, ppunkState: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStatus(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStatus(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(self, ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStateNoAddRef(self) -> Windows.Win32.System.Com.IUnknown_head: ...
class IMFAttributes(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2cd2d921-c447-44a7-a13c-4adabfc247e3}')
    @commethod(3)
    def GetItem(self, guidKey: POINTER(Guid), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemType(self, guidKey: POINTER(Guid), pType: POINTER(Windows.Win32.Media.MediaFoundation.MF_ATTRIBUTE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CompareItem(self, guidKey: POINTER(Guid), Value: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pbResult: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Compare(self, pTheirs: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, MatchType: Windows.Win32.Media.MediaFoundation.MF_ATTRIBUTES_MATCH_TYPE, pbResult: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetUINT32(self, guidKey: POINTER(Guid), punValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetUINT64(self, guidKey: POINTER(Guid), punValue: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDouble(self, guidKey: POINTER(Guid), pfValue: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGUID(self, guidKey: POINTER(Guid), pguidValue: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStringLength(self, guidKey: POINTER(Guid), pcchLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetString(self, guidKey: POINTER(Guid), pwszValue: Windows.Win32.Foundation.PWSTR, cchBufSize: UInt32, pcchLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetAllocatedString(self, guidKey: POINTER(Guid), ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR), pcchLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetBlobSize(self, guidKey: POINTER(Guid), pcbBlobSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetBlob(self, guidKey: POINTER(Guid), pBuf: POINTER(Byte), cbBufSize: UInt32, pcbBlobSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAllocatedBlob(self, guidKey: POINTER(Guid), ppBuf: POINTER(POINTER(Byte)), pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetUnknown(self, guidKey: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetItem(self, guidKey: POINTER(Guid), Value: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DeleteItem(self, guidKey: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DeleteAllItems(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetUINT32(self, guidKey: POINTER(Guid), unValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetUINT64(self, guidKey: POINTER(Guid), unValue: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetDouble(self, guidKey: POINTER(Guid), fValue: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetGUID(self, guidKey: POINTER(Guid), guidValue: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetString(self, guidKey: POINTER(Guid), wszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetBlob(self, guidKey: POINTER(Guid), pBuf: POINTER(Byte), cbBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetUnknown(self, guidKey: POINTER(Guid), pUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def LockStore(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def UnlockStore(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetCount(self, pcItems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetItemByIndex(self, unIndex: UInt32, pguidKey: POINTER(Guid), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CopyAllItems(self, pDest: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFAudioMediaType(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaType
    _iid_ = Guid('{26a0adc3-ce26-4672-9304-69552edd3faf}')
    @commethod(38)
    def GetAudioFormat(self) -> POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head): ...
class IMFAudioPolicy(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0638c2b-6465-4395-9ae7-a321a9fd2856}')
    @commethod(3)
    def SetGroupingParam(self, rguidClass: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGroupingParam(self, pguidClass: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDisplayName(self, pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDisplayName(self, pszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetIconPath(self, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIconPath(self, pszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFAudioStreamVolume(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{76b1bbdb-4ec8-4f36-b106-70a9316df593}')
    @commethod(3)
    def GetChannelCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetChannelVolume(self, dwIndex: UInt32, fLevel: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelVolume(self, dwIndex: UInt32, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFBufferListNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24cd47f7-81d8-4785-adb2-af697a963cd2}')
    @commethod(3)
    def OnAddSourceBuffer(self) -> Void: ...
    @commethod(4)
    def OnRemoveSourceBuffer(self) -> Void: ...
class IMFByteStream(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ad4c1b00-4bf7-422f-9175-756693d9130d}')
    @commethod(3)
    def GetCapabilities(self, pdwCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLength(self, pqwLength: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLength(self, qwLength: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentPosition(self, pqwPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCurrentPosition(self, qwPosition: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsEndOfStream(self, pfEndOfStream: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Read(self, pb: POINTER(Byte), cb: UInt32, pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BeginRead(self, pb: POINTER(Byte), cb: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EndRead(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Write(self, pb: POINTER(Byte), cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def BeginWrite(self, pb: POINTER(Byte), cb: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EndWrite(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Seek(self, SeekOrigin: Windows.Win32.Media.MediaFoundation.MFBYTESTREAM_SEEK_ORIGIN, llSeekOffset: Int64, dwSeekFlags: UInt32, pqwCurrentPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFByteStreamBuffering(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d66d782-1d4f-4db7-8c63-cb8c77f1ef5e}')
    @commethod(3)
    def SetBufferingParams(self, pParams: POINTER(Windows.Win32.Media.MediaFoundation.MFBYTESTREAM_BUFFERING_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnableBuffering(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopBuffering(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFByteStreamCacheControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f5042ea4-7a96-4a75-aa7b-2be1ef7f88d5}')
    @commethod(3)
    def StopBackgroundTransfer(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFByteStreamCacheControl2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFByteStreamCacheControl
    _iid_ = Guid('{71ce469c-f34b-49ea-a56b-2d2a10e51149}')
    @commethod(4)
    def GetByteRanges(self, pcRanges: POINTER(UInt32), ppRanges: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.MF_BYTE_STREAM_CACHE_RANGE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCacheLimit(self, qwBytes: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsBackgroundTransferActive(self, pfActive: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFByteStreamHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb420aa4-765b-4a1f-91fe-d6a8a143924c}')
    @commethod(3)
    def BeginCreateObject(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pwszURL: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pProps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppIUnknownCancelCookie: POINTER(Windows.Win32.System.Com.IUnknown_head), pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndCreateObject(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pObjectType: POINTER(Windows.Win32.Media.MediaFoundation.MF_OBJECT_TYPE), ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelObjectCreation(self, pIUnknownCancelCookie: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxNumberOfBytesRequiredForResolution(self, pqwBytes: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFByteStreamProxyClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6b43f84-5c0a-42e8-a44d-b1857a76992f}')
    @commethod(3)
    def CreateByteStreamProxy(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFByteStreamTimeSeek(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64976bfa-fb61-4041-9069-8c9a5f659beb}')
    @commethod(3)
    def IsTimeSeekSupported(self, pfTimeSeekIsSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TimeSeek(self, qwTimePosition: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTimeSeekResult(self, pqwStartTime: POINTER(UInt64), pqwStopTime: POINTER(UInt64), pqwDuration: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCameraConfigurationManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a624f617-4704-4206-8a6d-ebda4a093985}')
    @commethod(3)
    def LoadDefaults(self, cameraAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, configurations: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraControlDefaultsCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveDefaults(self, configurations: Windows.Win32.Media.MediaFoundation.IMFCameraControlDefaultsCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Shutdown(self) -> Void: ...
class IMFCameraControlDefaults(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75510662-b034-48f4-88a7-8de61daa4af9}')
    @commethod(3)
    def GetType(self) -> Windows.Win32.Media.MediaFoundation.MF_CAMERA_CONTROL_CONFIGURATION_TYPE: ...
    @commethod(4)
    def GetRangeInfo(self, rangeInfo: POINTER(Windows.Win32.Media.MediaFoundation.MF_CAMERA_CONTROL_RANGE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LockControlData(self, control: POINTER(c_void_p), controlSize: POINTER(UInt32), data: POINTER(c_void_p), dataSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnlockControlData(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCameraControlDefaultsCollection(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{92d43d0f-54a8-4bae-96da-356d259a5c26}')
    @commethod(33)
    def GetControlCount(self) -> UInt32: ...
    @commethod(34)
    def GetControl(self, index: UInt32, configuration: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraControlDefaults_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetOrAddExtendedControl(self, configType: Windows.Win32.Media.MediaFoundation.MF_CAMERA_CONTROL_CONFIGURATION_TYPE, constrolId: UInt32, streamId: UInt32, dataSize: UInt32, defaults: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraControlDefaults_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetOrAddControl(self, configType: Windows.Win32.Media.MediaFoundation.MF_CAMERA_CONTROL_CONFIGURATION_TYPE, controlSet: POINTER(Guid), constrolId: UInt32, controlSize: UInt32, dataSize: UInt32, defaults: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraControlDefaults_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def RemoveControl(self, controlSet: POINTER(Guid), constrolId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def RemoveAllControls(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCameraControlMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4d46f2c9-28ba-4970-8c7b-1f0c9d80af69}')
    @commethod(3)
    def Start(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddControlSubscription(self, controlSet: Guid, id: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveControlSubscription(self, controlSet: Guid, id: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Shutdown(self) -> Void: ...
class IMFCameraControlNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e8f2540d-558a-4449-8b64-4863467a9fe8}')
    @commethod(3)
    def OnChange(self, controlSet: POINTER(Guid), id: UInt32) -> Void: ...
    @commethod(4)
    def OnError(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Void: ...
class IMFCameraOcclusionStateMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cc692f46-c697-47e2-a72d-7b064617749b}')
    @commethod(3)
    def Start(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSupportedStates(self) -> UInt32: ...
class IMFCameraOcclusionStateReport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1640b2cf-74da-4462-a43b-b76d3bdc1434}')
    @commethod(3)
    def GetOcclusionState(self, occlusionState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCameraOcclusionStateReportCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e5841c7-3889-4019-9035-783fb19b5948}')
    @commethod(3)
    def OnOcclusionStateReport(self, occlusionStateReport: Windows.Win32.Media.MediaFoundation.IMFCameraOcclusionStateReport_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCameraSyncObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6338b23a-3042-49d2-a3ea-ec0fed815407}')
    @commethod(3)
    def WaitOnSignal(self, timeOutInMs: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown(self) -> Void: ...
class IMFCaptureEngine(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6bba433-176b-48b2-b375-53aa03473207}')
    @commethod(3)
    def Initialize(self, pEventCallback: Windows.Win32.Media.MediaFoundation.IMFCaptureEngineOnEventCallback_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pAudioSource: Windows.Win32.System.Com.IUnknown_head, pVideoSource: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartPreview(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopPreview(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StartRecord(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def StopRecord(self, bFinalize: Windows.Win32.Foundation.BOOL, bFlushUnprocessedSamples: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def TakePhoto(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSink(self, mfCaptureEngineSinkType: Windows.Win32.Media.MediaFoundation.MF_CAPTURE_ENGINE_SINK_TYPE, ppSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFCaptureSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSource(self, ppSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFCaptureSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureEngineClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8f02d140-56fc-4302-a705-3a97c78be779}')
    @commethod(3)
    def CreateInstance(self, clsid: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureEngineOnEventCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aeda51c0-9025-4983-9012-de597b88b089}')
    @commethod(3)
    def OnEvent(self, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureEngineOnSampleCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52150b82-ab39-4467-980f-e48bf0822ecd}')
    @commethod(3)
    def OnSample(self, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureEngineOnSampleCallback2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFCaptureEngineOnSampleCallback
    _iid_ = Guid('{e37ceed7-340f-4514-9f4d-9c2ae026100b}')
    @commethod(4)
    def OnSynchronizedEvent(self, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCapturePhotoConfirmation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{19f68549-ca8a-4706-a4ef-481dbc95e12c}')
    @commethod(3)
    def SetPhotoConfirmationCallback(self, pNotificationCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPixelFormat(self, subtype: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPixelFormat(self, subtype: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCapturePhotoSink(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFCaptureSink
    _iid_ = Guid('{d2d43cc8-48bb-4aa7-95db-10c06977e777}')
    @commethod(8)
    def SetOutputFileName(self, fileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSampleCallback(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFCaptureEngineOnSampleCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetOutputByteStream(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCapturePreviewSink(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFCaptureSink
    _iid_ = Guid('{77346cfd-5b49-4d73-ace0-5b52a859f2e0}')
    @commethod(8)
    def SetRenderHandle(self, handle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetRenderSurface(self, pSurface: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UpdateVideo(self, pSrc: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head), pDst: POINTER(Windows.Win32.Foundation.RECT_head), pBorderClr: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSampleCallback(self, dwStreamSinkIndex: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFCaptureEngineOnSampleCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMirrorState(self, pfMirrorState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetMirrorState(self, fMirrorState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRotation(self, dwStreamIndex: UInt32, pdwRotationValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetRotation(self, dwStreamIndex: UInt32, dwRotationValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetCustomSink(self, pMediaSink: Windows.Win32.Media.MediaFoundation.IMFMediaSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureRecordSink(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFCaptureSink
    _iid_ = Guid('{3323b55a-f92a-4fe2-8edc-e9bfc0634d77}')
    @commethod(8)
    def SetOutputByteStream(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, guidContainerType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputFileName(self, fileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSampleCallback(self, dwStreamSinkIndex: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFCaptureEngineOnSampleCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetCustomSink(self, pMediaSink: Windows.Win32.Media.MediaFoundation.IMFMediaSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRotation(self, dwStreamIndex: UInt32, pdwRotationValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetRotation(self, dwStreamIndex: UInt32, dwRotationValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{72d6135b-35e9-412c-b926-fd5265f2a885}')
    @commethod(3)
    def GetOutputMediaType(self, dwSinkStreamIndex: UInt32, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetService(self, dwSinkStreamIndex: UInt32, rguidService: POINTER(Guid), riid: POINTER(Guid), ppUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddStream(self, dwSourceStreamIndex: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pdwSinkStreamIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Prepare(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAllStreams(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureSink2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFCaptureSink
    _iid_ = Guid('{f9e4219e-6197-4b5e-b888-bee310ab2c59}')
    @commethod(8)
    def SetOutputMediaType(self, dwStreamIndex: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pEncodingAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCaptureSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{439a42a8-0d2c-4505-be83-f79b2a05d5c4}')
    @commethod(3)
    def GetCaptureDeviceSource(self, mfCaptureEngineDeviceType: Windows.Win32.Media.MediaFoundation.MF_CAPTURE_ENGINE_DEVICE_TYPE, ppMediaSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCaptureDeviceActivate(self, mfCaptureEngineDeviceType: Windows.Win32.Media.MediaFoundation.MF_CAPTURE_ENGINE_DEVICE_TYPE, ppActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetService(self, rguidService: POINTER(Guid), riid: POINTER(Guid), ppUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddEffect(self, dwSourceStreamIndex: UInt32, pUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveEffect(self, dwSourceStreamIndex: UInt32, pUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAllEffects(self, dwSourceStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAvailableDeviceMediaType(self, dwSourceStreamIndex: UInt32, dwMediaTypeIndex: UInt32, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCurrentDeviceMediaType(self, dwSourceStreamIndex: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCurrentDeviceMediaType(self, dwSourceStreamIndex: UInt32, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDeviceStreamCount(self, pdwStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDeviceStreamCategory(self, dwSourceStreamIndex: UInt32, pStreamCategory: POINTER(Windows.Win32.Media.MediaFoundation.MF_CAPTURE_ENGINE_STREAM_CATEGORY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetMirrorState(self, dwStreamIndex: UInt32, pfMirrorState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetMirrorState(self, dwStreamIndex: UInt32, fMirrorState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetStreamIndexFromFriendlyName(self, uifriendlyName: UInt32, pdwActualStreamIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCdmSuspendNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7a5645d2-43bd-47fd-87b7-dcd24cc7d692}')
    @commethod(3)
    def Begin(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def End(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFClock(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2eb1e945-18b8-4139-9b1a-d5d584818530}')
    @commethod(3)
    def GetClockCharacteristics(self, pdwCharacteristics: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCorrelatedTime(self, dwReserved: UInt32, pllClockTime: POINTER(Int64), phnsSystemTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContinuityKey(self, pdwContinuityKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetState(self, dwReserved: UInt32, peClockState: POINTER(Windows.Win32.Media.MediaFoundation.MFCLOCK_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProperties(self, pClockProperties: POINTER(Windows.Win32.Media.MediaFoundation.MFCLOCK_PROPERTIES_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFClockConsumer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ef2a662-47c0-4666-b13d-cbb717f2fa2c}')
    @commethod(3)
    def SetPresentationClock(self, pPresentationClock: Windows.Win32.Media.MediaFoundation.IMFPresentationClock_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPresentationClock(self, ppPresentationClock: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFClockStateSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f6696e82-74f7-4f3d-a178-8a5e09c3659f}')
    @commethod(3)
    def OnClockStart(self, hnsSystemTime: Int64, llClockStartOffset: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnClockStop(self, hnsSystemTime: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnClockPause(self, hnsSystemTime: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnClockRestart(self, hnsSystemTime: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnClockSetRate(self, hnsSystemTime: Int64, flRate: Single) -> Windows.Win32.Foundation.HRESULT: ...
class IMFCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5bc8a76b-869a-46a3-9b03-fa218a66aebe}')
    @commethod(3)
    def GetElementCount(self, pcElements: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetElement(self, dwElementIndex: UInt32, ppUnkElement: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddElement(self, pUnkElement: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveElement(self, dwElementIndex: UInt32, ppUnkElement: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InsertElementAt(self, dwIndex: UInt32, pUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAllElements(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentDecryptionModule(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87be986c-10be-4943-bf48-4b54ce1983a2}')
    @commethod(3)
    def SetContentEnabler(self, contentEnabler: Windows.Win32.Media.MediaFoundation.IMFContentEnabler_head, result: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSuspendNotify(self, notify: POINTER(Windows.Win32.Media.MediaFoundation.IMFCdmSuspendNotify_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPMPHostApp(self, pmpHostApp: Windows.Win32.Media.MediaFoundation.IMFPMPHostApp_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSession(self, sessionType: Windows.Win32.Media.MediaFoundation.MF_MEDIAKEYSESSION_TYPE, callbacks: Windows.Win32.Media.MediaFoundation.IMFContentDecryptionModuleSessionCallbacks_head, session: POINTER(Windows.Win32.Media.MediaFoundation.IMFContentDecryptionModuleSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetServerCertificate(self, certificate: POINTER(Byte), certificateSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateTrustedInput(self, contentInitData: POINTER(Byte), contentInitDataSize: UInt32, trustedInput: POINTER(Windows.Win32.Media.MediaFoundation.IMFTrustedInput_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProtectionSystemIds(self, systemIds: POINTER(POINTER(Guid)), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentDecryptionModuleAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a853d1f4-e2a0-4303-9edc-f1a68ee43136}')
    @commethod(3)
    def CreateContentDecryptionModule(self, contentDecryptionModuleProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, contentDecryptionModule: POINTER(Windows.Win32.Media.MediaFoundation.IMFContentDecryptionModule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConfiguration(self, configuration: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeySystem(self, keySystem: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentDecryptionModuleFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d5abf16-4cbb-4e08-b977-9ba59049943e}')
    @commethod(3)
    def IsTypeSupported(self, keySystem: Windows.Win32.Foundation.PWSTR, contentType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def CreateContentDecryptionModuleAccess(self, keySystem: Windows.Win32.Foundation.PWSTR, configurations: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head), numConfigurations: UInt32, contentDecryptionModuleAccess: POINTER(Windows.Win32.Media.MediaFoundation.IMFContentDecryptionModuleAccess_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentDecryptionModuleSession(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e233efd-1dd2-49e8-b577-d63eee4c0d33}')
    @commethod(3)
    def GetSessionId(self, sessionId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetExpiration(self, expiration: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeyStatuses(self, keyStatuses: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.MFMediaKeyStatus_head)), numKeyStatuses: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Load(self, sessionId: Windows.Win32.Foundation.PWSTR, loaded: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GenerateRequest(self, initDataType: Windows.Win32.Foundation.PWSTR, initData: POINTER(Byte), initDataSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Update(self, response: POINTER(Byte), responseSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentDecryptionModuleSessionCallbacks(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3f96ee40-ad81-4096-8470-59a4b770f89a}')
    @commethod(3)
    def KeyMessage(self, messageType: Windows.Win32.Media.MediaFoundation.MF_MEDIAKEYSESSION_MESSAGETYPE, message: POINTER(Byte), messageSize: UInt32, destinationURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def KeyStatusChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentDecryptorContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ec4b1bd-43fb-4763-85d2-64fcb5c5f4cb}')
    @commethod(3)
    def InitializeHardwareKey(self, InputPrivateDataByteCount: UInt32, InputPrivateData: c_void_p, OutputPrivateData: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentEnabler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d3c4ef59-49ce-4381-9071-d5bcd044c770}')
    @commethod(3)
    def GetEnableType(self, pType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEnableURL(self, ppwszURL: POINTER(Windows.Win32.Foundation.PWSTR), pcchURL: POINTER(UInt32), pTrustStatus: POINTER(Windows.Win32.Media.MediaFoundation.MF_URL_TRUST_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnableData(self, ppbData: POINTER(POINTER(Byte)), pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsAutomaticSupported(self, pfAutomatic: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AutomaticEnable(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MonitorEnable(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentProtectionDevice(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e6257174-a060-4c9a-a088-3b1b471cad28}')
    @commethod(3)
    def InvokeFunction(self, FunctionId: UInt32, InputBufferByteCount: UInt32, InputBuffer: POINTER(Byte), OutputBufferByteCount: POINTER(UInt32), OutputBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrivateDataByteCount(self, PrivateInputByteCount: POINTER(UInt32), PrivateOutputByteCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFContentProtectionManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{acf92459-6a61-42bd-b57c-b43e51203cb0}')
    @commethod(3)
    def BeginEnableContent(self, pEnablerActivate: Windows.Win32.Media.MediaFoundation.IMFActivate_head, pTopo: Windows.Win32.Media.MediaFoundation.IMFTopology_head, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndEnableContent(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFD3D12SynchronizationObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{802302b0-82de-45e1-b421-f19ee5bdaf23}')
    @commethod(3)
    def SignalEventOnFinalResourceRelease(self, hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFD3D12SynchronizationObjectCommands(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09d0f835-92ff-4e53-8efa-40faa551f233}')
    @commethod(3)
    def EnqueueResourceReady(self, pProducerCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnqueueResourceReadyWait(self, pConsumerCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SignalEventOnResourceReady(self, hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnqueueResourceRelease(self, pConsumerCommandQueue: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFDLNASinkInit(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c012799-1b61-4c10-bda9-04445be5f561}')
    @commethod(3)
    def Initialize(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, fPal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMFDRMNetHelper(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d1ff0ea-679a-4190-8d46-7fa69e8c7e15}')
    @commethod(3)
    def ProcessLicenseRequest(self, pLicenseRequest: POINTER(Byte), cbLicenseRequest: UInt32, ppLicenseResponse: POINTER(POINTER(Byte)), pcbLicenseResponse: POINTER(UInt32), pbstrKID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChainedLicenseResponse(self, ppLicenseResponse: POINTER(POINTER(Byte)), pcbLicenseResponse: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFDXGIBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7174cfa-1c9e-48b1-8866-626226bfc258}')
    @commethod(3)
    def GetResource(self, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSubresourceIndex(self, puSubresource: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUnknown(self, guid: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetUnknown(self, guid: POINTER(Guid), pUnkData: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFDXGIDeviceManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eb533d5d-2db6-40f8-97a9-494692014f07}')
    @commethod(3)
    def CloseDeviceHandle(self, hDevice: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVideoService(self, hDevice: Windows.Win32.Foundation.HANDLE, riid: POINTER(Guid), ppService: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LockDevice(self, hDevice: Windows.Win32.Foundation.HANDLE, riid: POINTER(Guid), ppUnkDevice: POINTER(c_void_p), fBlock: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenDeviceHandle(self, phDevice: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResetDevice(self, pUnkDevice: Windows.Win32.System.Com.IUnknown_head, resetToken: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def TestDevice(self, hDevice: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnlockDevice(self, hDevice: Windows.Win32.Foundation.HANDLE, fSaveState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMFDXGIDeviceManagerSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20bc074b-7a8d-4609-8c3b-64a0a3b5d7ce}')
    @commethod(3)
    def GetManager(self, ppManager: POINTER(Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFDesiredSample(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56c294d0-753e-4260-8d61-a3d8820b1d54}')
    @commethod(3)
    def GetDesiredSampleTimeAndDuration(self, phnsSampleTime: POINTER(Int64), phnsSampleDuration: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDesiredSampleTimeAndDuration(self, hnsSampleTime: Int64, hnsSampleDuration: Int64) -> Void: ...
    @commethod(5)
    def Clear(self) -> Void: ...
class IMFDeviceTransform(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d818fbd8-fc46-42f2-87ac-1ea2d1f9bf32}')
    @commethod(3)
    def InitializeTransform(self, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInputAvailableType(self, dwInputStreamID: UInt32, dwTypeIndex: UInt32, pMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputCurrentType(self, dwInputStreamID: UInt32, pMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputStreamAttributes(self, dwInputStreamID: UInt32, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputAvailableType(self, dwOutputStreamID: UInt32, dwTypeIndex: UInt32, pMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputCurrentType(self, dwOutputStreamID: UInt32, pMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOutputStreamAttributes(self, dwOutputStreamID: UInt32, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStreamCount(self, pcInputStreams: POINTER(UInt32), pcOutputStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStreamIDs(self, dwInputIDArraySize: UInt32, pdwInputStreamIds: POINTER(UInt32), dwOutputIDArraySize: UInt32, pdwOutputStreamIds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ProcessEvent(self, dwInputStreamID: UInt32, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ProcessInput(self, dwInputStreamID: UInt32, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ProcessMessage(self, eMessage: Windows.Win32.Media.MediaFoundation.MFT_MESSAGE_TYPE, ulParam: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ProcessOutput(self, dwFlags: UInt32, cOutputBufferCount: UInt32, pOutputSample: POINTER(Windows.Win32.Media.MediaFoundation.MFT_OUTPUT_DATA_BUFFER_head), pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetInputStreamState(self, dwStreamID: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, value: Windows.Win32.Media.MediaFoundation.DeviceStreamState, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetInputStreamState(self, dwStreamID: UInt32, value: POINTER(Windows.Win32.Media.MediaFoundation.DeviceStreamState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetOutputStreamState(self, dwStreamID: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, value: Windows.Win32.Media.MediaFoundation.DeviceStreamState, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetOutputStreamState(self, dwStreamID: UInt32, value: POINTER(Windows.Win32.Media.MediaFoundation.DeviceStreamState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetInputStreamPreferredState(self, dwStreamID: UInt32, value: POINTER(Windows.Win32.Media.MediaFoundation.DeviceStreamState), ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def FlushInputStream(self, dwStreamIndex: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FlushOutputStream(self, dwStreamIndex: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFDeviceTransformCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d5cb646-29ec-41fb-8179-8c4c6d750811}')
    @commethod(3)
    def OnBufferSent(self, pCallbackAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pinId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFExtendedCameraControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{38e33520-fca1-4845-a27a-68b7c6ab3789}')
    @commethod(3)
    def GetCapabilities(self) -> UInt64: ...
    @commethod(4)
    def SetFlags(self, ulFlags: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(self) -> UInt64: ...
    @commethod(6)
    def LockPayload(self, ppPayload: POINTER(POINTER(Byte)), pulPayload: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnlockPayload(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitSettings(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFExtendedCameraController(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b91ebfee-ca03-4af4-8a82-a31752f4a0fc}')
    @commethod(3)
    def GetExtendedCameraControl(self, dwStreamIndex: UInt32, ulPropertyId: UInt32, ppControl: POINTER(Windows.Win32.Media.MediaFoundation.IMFExtendedCameraControl_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFExtendedCameraIntrinsicModel(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5c595e64-4630-4231-855a-12842f733245}')
    @commethod(3)
    def GetModel(self, pIntrinsicModel: POINTER(Windows.Win32.Media.MediaFoundation.MFExtendedCameraIntrinsic_IntrinsicModel_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetModel(self, pIntrinsicModel: POINTER(Windows.Win32.Media.MediaFoundation.MFExtendedCameraIntrinsic_IntrinsicModel_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDistortionModelType(self, pDistortionModelType: POINTER(Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_DistortionModelType)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFExtendedCameraIntrinsics(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{687f6dac-6987-4750-a16a-734d1e7a10fe}')
    @commethod(3)
    def InitializeFromBuffer(self, pbBuffer: POINTER(Byte), dwBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBufferSize(self, pdwBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SerializeToBuffer(self, pbBuffer: POINTER(Byte), pdwBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIntrinsicModelCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIntrinsicModelByIndex(self, dwIndex: UInt32, ppIntrinsicModel: POINTER(Windows.Win32.Media.MediaFoundation.IMFExtendedCameraIntrinsicModel_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddIntrinsicModel(self, pIntrinsicModel: Windows.Win32.Media.MediaFoundation.IMFExtendedCameraIntrinsicModel_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFExtendedCameraIntrinsicsDistortionModel6KT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{74c2653b-5f55-4eb1-9f0f-18b8f68b7d3d}')
    @commethod(3)
    def GetDistortionModel(self, pDistortionModel: POINTER(Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_DistortionModel6KT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDistortionModel(self, pDistortionModel: POINTER(Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_DistortionModel6KT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFExtendedCameraIntrinsicsDistortionModelArcTan(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{812d5f95-b572-45dc-bafc-ae24199ddda8}')
    @commethod(3)
    def GetDistortionModel(self, pDistortionModel: POINTER(Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_DistortionModelArcTan_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDistortionModel(self, pDistortionModel: POINTER(Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_DistortionModelArcTan_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFExtendedDRMTypeSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{332ec562-3758-468d-a784-e38f23552128}')
    @commethod(3)
    def IsTypeSupportedEx(self, type: Windows.Win32.Foundation.BSTR, keySystem: Windows.Win32.Foundation.BSTR, pAnswer: POINTER(Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_CANPLAY)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFFieldOfUseMFTUnlock(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{508e71d3-ec66-4fc3-8775-b4b9ed6ba847}')
    @commethod(3)
    def Unlock(self, pUnkMFT: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFFinalizableMediaSink(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaSink
    _iid_ = Guid('{eaecb74a-9a50-42ce-9541-6a7f57aa4ad7}')
    @commethod(12)
    def BeginFinalize(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EndFinalize(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFGetService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa993888-4383-415a-a930-dd472a8cf6f7}')
    @commethod(3)
    def GetService(self, guidService: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFHDCPStatus(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de400f54-5bf1-40cf-8964-0bea136b1e3d}')
    @commethod(3)
    def Query(self, pStatus: POINTER(Windows.Win32.Media.MediaFoundation.MF_HDCP_STATUS), pfStatus: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Set(self, status: Windows.Win32.Media.MediaFoundation.MF_HDCP_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
class IMFHttpDownloadRequest(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f779fddf-26e7-4270-8a8b-b983d1859de0}')
    @commethod(3)
    def AddHeader(self, szHeader: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginSendRequest(self, pbPayload: POINTER(Byte), cbPayload: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndSendRequest(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BeginReceiveResponse(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EndReceiveResponse(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginReadPayload(self, pb: POINTER(Byte), cb: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndReadPayload(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pqwOffset: POINTER(UInt64), pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def QueryHeader(self, szHeaderName: Windows.Win32.Foundation.PWSTR, dwIndex: UInt32, ppszHeaderValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetURL(self, ppszURL: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def HasNullSourceOrigin(self, pfNullSourceOrigin: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTimeSeekResult(self, pqwStartTime: POINTER(UInt64), pqwStopTime: POINTER(UInt64), pqwDuration: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetHttpStatus(self, pdwHttpStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetAtEndOfPayload(self, pfAtEndOfPayload: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTotalLength(self, pqwTotalLength: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRangeEndOffset(self, pqwRangeEnd: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFHttpDownloadSession(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71fa9a2c-53ce-4662-a132-1a7e8cbf62db}')
    @commethod(3)
    def SetServer(self, szServerName: Windows.Win32.Foundation.PWSTR, nPort: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRequest(self, szObjectName: Windows.Win32.Foundation.PWSTR, fBypassProxyCache: Windows.Win32.Foundation.BOOL, fSecure: Windows.Win32.Foundation.BOOL, szVerb: Windows.Win32.Foundation.PWSTR, szReferrer: Windows.Win32.Foundation.PWSTR, ppRequest: POINTER(Windows.Win32.Media.MediaFoundation.IMFHttpDownloadRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFHttpDownloadSessionProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1b4cf4b9-3a16-4115-839d-03cc5c99df01}')
    @commethod(3)
    def CreateHttpDownloadSession(self, wszScheme: Windows.Win32.Foundation.PWSTR, ppDownloadSession: POINTER(Windows.Win32.Media.MediaFoundation.IMFHttpDownloadSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFImageSharingEngine(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cfa0ae8e-7e1c-44d2-ae68-fc4c148a6354}')
    @commethod(3)
    def SetSource(self, pStream: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDevice(self, pDevice: POINTER(Windows.Win32.Media.MediaFoundation.DEVICE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFImageSharingEngineClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1fc55727-a7fb-4fc8-83ae-8af024990af1}')
    @commethod(3)
    def CreateInstanceFromUDN(self, pUniqueDeviceName: Windows.Win32.Foundation.BSTR, ppEngine: POINTER(Windows.Win32.Media.MediaFoundation.IMFImageSharingEngine_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFInputTrustAuthority(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d19f8e98-b126-4446-890c-5dcb7ad71453}')
    @commethod(3)
    def GetDecrypter(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RequestAccess(self, Action: Windows.Win32.Media.MediaFoundation.MFPOLICYMANAGER_ACTION, ppContentEnablerActivate: POINTER(Windows.Win32.Media.MediaFoundation.IMFActivate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPolicy(self, Action: Windows.Win32.Media.MediaFoundation.MFPOLICYMANAGER_ACTION, ppPolicy: POINTER(Windows.Win32.Media.MediaFoundation.IMFOutputPolicy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BindAccess(self, pParam: POINTER(Windows.Win32.Media.MediaFoundation.MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateAccess(self, pParam: POINTER(Windows.Win32.Media.MediaFoundation.MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFLocalMFTRegistration(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{149c4d73-b4be-4f8d-8b87-079e926b6add}')
    @commethod(3)
    def RegisterMFTs(self, pMFTs: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTRATION_INFO_head), cMFTs: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{045fa593-8799-42b8-bc8d-8968c6453507}')
    @commethod(3)
    def Lock(self, ppbBuffer: POINTER(POINTER(Byte)), pcbMaxLength: POINTER(UInt32), pcbCurrentLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unlock(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentLength(self, pcbCurrentLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetCurrentLength(self, cbCurrentLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxLength(self, pcbMaxLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngine(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{98a1b0bb-03eb-4935-ae7c-93c1fa0e1c93}')
    @commethod(3)
    def GetError(self, ppError: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaError_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetErrorCode(self, error: Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_ERR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSourceElements(self, pSrcElements: Windows.Win32.Media.MediaFoundation.IMFMediaEngineSrcElements_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSource(self, pUrl: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentSource(self, ppUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNetworkState(self) -> UInt16: ...
    @commethod(9)
    def GetPreload(self) -> Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_PRELOAD: ...
    @commethod(10)
    def SetPreload(self, Preload: Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_PRELOAD) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBuffered(self, ppBuffered: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTimeRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Load(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CanPlayType(self, type: Windows.Win32.Foundation.BSTR, pAnswer: POINTER(Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_CANPLAY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetReadyState(self) -> UInt16: ...
    @commethod(15)
    def IsSeeking(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(16)
    def GetCurrentTime(self) -> Double: ...
    @commethod(17)
    def SetCurrentTime(self, seekTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStartTime(self) -> Double: ...
    @commethod(19)
    def GetDuration(self) -> Double: ...
    @commethod(20)
    def IsPaused(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(21)
    def GetDefaultPlaybackRate(self) -> Double: ...
    @commethod(22)
    def SetDefaultPlaybackRate(self, Rate: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetPlaybackRate(self) -> Double: ...
    @commethod(24)
    def SetPlaybackRate(self, Rate: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPlayed(self, ppPlayed: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTimeRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetSeekable(self, ppSeekable: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTimeRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def IsEnded(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(28)
    def GetAutoPlay(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(29)
    def SetAutoPlay(self, AutoPlay: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetLoop(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(31)
    def SetLoop(self, Loop: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Play(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetMuted(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(35)
    def SetMuted(self, Muted: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetVolume(self) -> Double: ...
    @commethod(37)
    def SetVolume(self, Volume: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def HasVideo(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(39)
    def HasAudio(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(40)
    def GetNativeVideoSize(self, cx: POINTER(UInt32), cy: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetVideoAspectRatio(self, cx: POINTER(UInt32), cy: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def TransferVideoFrame(self, pDstSurf: Windows.Win32.System.Com.IUnknown_head, pSrc: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head), pDst: POINTER(Windows.Win32.Foundation.RECT_head), pBorderClr: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def OnVideoStreamTick(self, pPts: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineAudioEndpointId(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7a3bac98-0e76-49fb-8c20-8a86fd98eaf2}')
    @commethod(3)
    def SetAudioEndpointId(self, pszEndpointId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAudioEndpointId(self, ppszEndpointId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4d645ace-26aa-4688-9be1-df3516990b93}')
    @commethod(3)
    def CreateInstance(self, dwFlags: UInt32, pAttr: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppPlayer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaEngine_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTimeRange(self, ppTimeRange: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTimeRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateError(self, ppError: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaError_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineClassFactory2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09083cef-867f-4bf6-8776-dee3a7b42fca}')
    @commethod(3)
    def CreateMediaKeys2(self, keySystem: Windows.Win32.Foundation.BSTR, defaultCdmStorePath: Windows.Win32.Foundation.BSTR, inprivateCdmStorePath: Windows.Win32.Foundation.BSTR, ppKeys: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaKeys_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineClassFactory3(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3787614f-65f7-4003-b673-ead8293a0e60}')
    @commethod(3)
    def CreateMediaKeySystemAccess(self, keySystem: Windows.Win32.Foundation.BSTR, ppSupportedConfigurationsArray: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head), uSize: UInt32, ppKeyAccess: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaKeySystemAccess_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineClassFactory4(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fbe256c1-43cf-4a9b-8cb8-ce8632a34186}')
    @commethod(3)
    def CreateContentDecryptionModuleFactory(self, keySystem: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineClassFactoryEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEngineClassFactory
    _iid_ = Guid('{c56156c6-ea5b-48a5-9df8-fbe035d0929e}')
    @commethod(6)
    def CreateMediaSourceExtension(self, dwFlags: UInt32, pAttr: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppMSE: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSourceExtension_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateMediaKeys(self, keySystem: Windows.Win32.Foundation.BSTR, cdmStorePath: Windows.Win32.Foundation.BSTR, ppKeys: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaKeys_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsTypeSupported(self, type: Windows.Win32.Foundation.BSTR, keySystem: Windows.Win32.Foundation.BSTR, isSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineEME(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50dc93e4-ba4f-4275-ae66-83e836e57469}')
    @commethod(3)
    def get_Keys(self, keys: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaKeys_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMediaKeys(self, keys: Windows.Win32.Media.MediaFoundation.IMFMediaKeys_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineEMENotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9e184d15-cdb7-4f86-b49e-566689f4a601}')
    @commethod(3)
    def Encrypted(self, pbInitData: POINTER(Byte), cb: UInt32, bstrInitDataType: Windows.Win32.Foundation.BSTR) -> Void: ...
    @commethod(4)
    def WaitingForKey(self) -> Void: ...
class IMFMediaEngineEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEngine
    _iid_ = Guid('{83015ead-b1e6-40d0-a98a-37145ffe1ad1}')
    @commethod(45)
    def SetSourceFromByteStream(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pURL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetStatistics(self, StatisticID: Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_STATISTIC, pStatistic: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def UpdateVideoStream(self, pSrc: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head), pDst: POINTER(Windows.Win32.Foundation.RECT_head), pBorderClr: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetBalance(self) -> Double: ...
    @commethod(49)
    def SetBalance(self, balance: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def IsPlaybackRateSupported(self, rate: Double) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(51)
    def FrameStep(self, Forward: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetResourceCharacteristics(self, pCharacteristics: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def GetPresentationAttribute(self, guidMFAttribute: POINTER(Guid), pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetNumberOfStreams(self, pdwStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def GetStreamAttribute(self, dwStreamIndex: UInt32, guidMFAttribute: POINTER(Guid), pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetStreamSelection(self, dwStreamIndex: UInt32, pEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SetStreamSelection(self, dwStreamIndex: UInt32, Enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def ApplyStreamSelections(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def IsProtected(self, pProtected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def InsertVideoEffect(self, pEffect: Windows.Win32.System.Com.IUnknown_head, fOptional: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def InsertAudioEffect(self, pEffect: Windows.Win32.System.Com.IUnknown_head, fOptional: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def RemoveAllEffects(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def SetTimelineMarkerTimer(self, timeToFire: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetTimelineMarkerTimer(self, pTimeToFire: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def CancelTimelineMarkerTimer(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def IsStereo3D(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(67)
    def GetStereo3DFramePackingMode(self, packMode: POINTER(Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_S3D_PACKING_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def SetStereo3DFramePackingMode(self, packMode: Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_S3D_PACKING_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetStereo3DRenderMode(self, outputType: POINTER(Windows.Win32.Media.MediaFoundation.MF3DVideoOutputType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def SetStereo3DRenderMode(self, outputType: Windows.Win32.Media.MediaFoundation.MF3DVideoOutputType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def EnableWindowlessSwapchainMode(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def GetVideoSwapchainHandle(self, phSwapchain: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def EnableHorizontalMirrorMode(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def GetAudioStreamCategory(self, pCategory: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def SetAudioStreamCategory(self, category: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def GetAudioEndpointRole(self, pRole: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def SetAudioEndpointRole(self, role: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def GetRealTimeMode(self, pfEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def SetRealTimeMode(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def SetCurrentTimeEx(self, seekTime: Double, seekMode: Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_SEEK_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def EnableTimeUpdateTimer(self, fEnableTimer: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineExtension(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f69d622-20b5-41e9-afdf-89ced1dda04e}')
    @commethod(3)
    def CanPlayType(self, AudioOnly: Windows.Win32.Foundation.BOOL, MimeType: Windows.Win32.Foundation.BSTR, pAnswer: POINTER(Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_CANPLAY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginCreateObject(self, bstrURL: Windows.Win32.Foundation.BSTR, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, type: Windows.Win32.Media.MediaFoundation.MF_OBJECT_TYPE, ppIUnknownCancelCookie: POINTER(Windows.Win32.System.Com.IUnknown_head), pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelObjectCreation(self, pIUnknownCancelCookie: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndCreateObject(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineNeedKeyNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{46a30204-a696-4b18-8804-246b8f031bb1}')
    @commethod(3)
    def NeedKey(self, initData: POINTER(Byte), cb: UInt32) -> Void: ...
class IMFMediaEngineNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fee7c112-e776-42b5-9bbf-0048524e2bd5}')
    @commethod(3)
    def EventNotify(self, event: UInt32, param1: UIntPtr, param2: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineOPMInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{765763e6-6c01-4b01-bb0f-b829f60ed28c}')
    @commethod(3)
    def GetOPMInfo(self, pStatus: POINTER(Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_OPM_STATUS), pConstricted: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineProtectedContent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f8021e8-9c8c-487e-bb5c-79aa4779938c}')
    @commethod(3)
    def ShareResources(self, pUnkDeviceContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRequiredProtections(self, pFrameProtectionFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOPMWindow(self, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TransferVideoFrame(self, pDstSurf: Windows.Win32.System.Com.IUnknown_head, pSrc: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head), pDst: POINTER(Windows.Win32.Foundation.RECT_head), pBorderClr: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head), pFrameProtectionFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetContentProtectionManager(self, pCPM: Windows.Win32.Media.MediaFoundation.IMFContentProtectionManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetApplicationCertificate(self, pbBlob: POINTER(Byte), cbBlob: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineSrcElements(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7a5e5354-b114-4c72-b991-3131d75032ea}')
    @commethod(3)
    def GetLength(self) -> UInt32: ...
    @commethod(4)
    def GetURL(self, index: UInt32, pURL: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(self, index: UInt32, pType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMedia(self, index: UInt32, pMedia: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddElement(self, pURL: Windows.Win32.Foundation.BSTR, pType: Windows.Win32.Foundation.BSTR, pMedia: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAllElements(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineSrcElementsEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEngineSrcElements
    _iid_ = Guid('{654a6bb3-e1a3-424a-9908-53a43a0dfda0}')
    @commethod(9)
    def AddElementEx(self, pURL: Windows.Win32.Foundation.BSTR, pType: Windows.Win32.Foundation.BSTR, pMedia: Windows.Win32.Foundation.BSTR, keySystem: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetKeySystem(self, index: UInt32, pType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineSupportsSourceTransfer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a724b056-1b2e-4642-a6f3-db9420c52908}')
    @commethod(3)
    def ShouldTransferSource(self, pfShouldTransfer: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DetachMediaSource(self, ppByteStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFByteStream_head), ppMediaSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSource_head), ppMSE: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSourceExtension_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AttachMediaSource(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pMediaSource: Windows.Win32.Media.MediaFoundation.IMFMediaSource_head, pMSE: Windows.Win32.Media.MediaFoundation.IMFMediaSourceExtension_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineTransferSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24230452-fe54-40cc-94f3-fcc394c340d6}')
    @commethod(3)
    def TransferSourceToMediaEngine(self, destination: Windows.Win32.Media.MediaFoundation.IMFMediaEngine_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEngineWebSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba2743a1-07e0-48ef-84b6-9a2ed023ca6c}')
    @commethod(3)
    def ShouldDelayTheLoadEvent(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def ConnectWebAudio(self, dwSampleRate: UInt32, ppSourceProvider: POINTER(Windows.Win32.Media.MediaFoundation.IAudioSourceProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DisconnectWebAudio(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaError(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc0e10d2-ab2a-4501-a951-06bb1075184c}')
    @commethod(3)
    def GetErrorCode(self) -> UInt16: ...
    @commethod(4)
    def GetExtendedErrorCode(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetErrorCode(self, error: Windows.Win32.Media.MediaFoundation.MF_MEDIA_ENGINE_ERR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetExtendedErrorCode(self, error: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEvent(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{df598932-f10c-4e39-bba2-c308f101daa3}')
    @commethod(33)
    def GetType(self, pmet: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetExtendedType(self, pguidExtendedType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetStatus(self, phrStatus: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetValue(self, pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEventGenerator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2cd0bd52-bcd5-4b89-b62c-eadc0c031e7d}')
    @commethod(3)
    def GetEvent(self, dwFlags: Windows.Win32.Media.MediaFoundation.MEDIA_EVENT_GENERATOR_GET_EVENT_FLAGS, ppEvent: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginGetEvent(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetEvent(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, ppEvent: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueueEvent(self, met: UInt32, guidExtendedType: POINTER(Guid), hrStatus: Windows.Win32.Foundation.HRESULT, pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaEventQueue(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36f846fc-2256-48b6-b58e-e2b638316581}')
    @commethod(3)
    def GetEvent(self, dwFlags: UInt32, ppEvent: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginGetEvent(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetEvent(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, ppEvent: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueueEvent(self, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueueEventParamVar(self, met: UInt32, guidExtendedType: POINTER(Guid), hrStatus: Windows.Win32.Foundation.HRESULT, pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueueEventParamUnk(self, met: UInt32, guidExtendedType: POINTER(Guid), hrStatus: Windows.Win32.Foundation.HRESULT, pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaKeySession(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24fa67d5-d1d0-4dc5-995c-c0efdc191fb5}')
    @commethod(3)
    def GetError(self, code: POINTER(UInt16), systemCode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_KeySystem(self, keySystem: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_SessionId(self, sessionId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Update(self, key: POINTER(Byte), cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaKeySession2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaKeySession
    _iid_ = Guid('{e9707e05-6d55-4636-b185-3de21210bd75}')
    @commethod(8)
    def get_KeyStatuses(self, pKeyStatusesArray: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.MFMediaKeyStatus_head)), puSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Load(self, bstrSessionId: Windows.Win32.Foundation.BSTR, pfLoaded: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GenerateRequest(self, initDataType: Windows.Win32.Foundation.BSTR, pbInitData: POINTER(Byte), cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Expiration(self, dblExpiration: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaKeySessionNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a0083f9-8947-4c1d-9ce0-cdee22b23135}')
    @commethod(3)
    def KeyMessage(self, destinationURL: Windows.Win32.Foundation.BSTR, message: POINTER(Byte), cb: UInt32) -> Void: ...
    @commethod(4)
    def KeyAdded(self) -> Void: ...
    @commethod(5)
    def KeyError(self, code: UInt16, systemCode: UInt32) -> Void: ...
class IMFMediaKeySessionNotify2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaKeySessionNotify
    _iid_ = Guid('{c3a9e92a-da88-46b0-a110-6cf953026cb9}')
    @commethod(6)
    def KeyMessage2(self, eMessageType: Windows.Win32.Media.MediaFoundation.MF_MEDIAKEYSESSION_MESSAGETYPE, destinationURL: Windows.Win32.Foundation.BSTR, pbMessage: POINTER(Byte), cbMessage: UInt32) -> Void: ...
    @commethod(7)
    def KeyStatusChange(self) -> Void: ...
class IMFMediaKeySystemAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aec63fda-7a97-4944-b35c-6c6df8085cc3}')
    @commethod(3)
    def CreateMediaKeys(self, pCdmCustomConfig: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppKeys: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaKeys2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_SupportedConfiguration(self, ppSupportedConfiguration: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_KeySystem(self, pKeySystem: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaKeys(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5cb31c05-61ff-418f-afda-caaf41421a38}')
    @commethod(3)
    def CreateSession(self, mimeType: Windows.Win32.Foundation.BSTR, initData: POINTER(Byte), cb: UInt32, customData: POINTER(Byte), cbCustomData: UInt32, notify: Windows.Win32.Media.MediaFoundation.IMFMediaKeySessionNotify_head, ppSession: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaKeySession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_KeySystem(self, keySystem: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSuspendNotify(self, notify: POINTER(Windows.Win32.Media.MediaFoundation.IMFCdmSuspendNotify_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaKeys2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaKeys
    _iid_ = Guid('{45892507-ad66-4de2-83a2-acbb13cd8d43}')
    @commethod(7)
    def CreateSession2(self, eSessionType: Windows.Win32.Media.MediaFoundation.MF_MEDIAKEYSESSION_TYPE, pMFMediaKeySessionNotify2: Windows.Win32.Media.MediaFoundation.IMFMediaKeySessionNotify2_head, ppSession: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaKeySession2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetServerCertificate(self, pbServerCertificate: POINTER(Byte), cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDOMException(self, systemCode: Windows.Win32.Foundation.HRESULT, code: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSession(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEventGenerator
    _iid_ = Guid('{90377834-21d0-4dee-8214-ba2e3e6c1127}')
    @commethod(7)
    def SetTopology(self, dwSetTopologyFlags: UInt32, pTopology: Windows.Win32.Media.MediaFoundation.IMFTopology_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ClearTopologies(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Start(self, pguidTimeFormat: POINTER(Guid), pvarStartPosition: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetClock(self, ppClock: POINTER(Windows.Win32.Media.MediaFoundation.IMFClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSessionCapabilities(self, pdwCaps: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetFullTopology(self, dwGetFullTopologyFlags: UInt32, TopoId: UInt64, ppFullTopology: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopology_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSharingEngine(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEngine
    _iid_ = Guid('{8d3ce1bf-2367-40e0-9eee-40d377cc1b46}')
    @commethod(45)
    def GetDevice(self, pDevice: POINTER(Windows.Win32.Media.MediaFoundation.DEVICE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSharingEngineClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{524d2bc4-b2b1-4fe5-8fac-fa4e4512b4e0}')
    @commethod(3)
    def CreateInstance(self, dwFlags: UInt32, pAttr: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppEngine: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSharingEngine_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ef2a660-47c0-4666-b13d-cbb717f2fa2c}')
    @commethod(3)
    def GetCharacteristics(self, pdwCharacteristics: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddStreamSink(self, dwStreamSinkIdentifier: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppStreamSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFStreamSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveStreamSink(self, dwStreamSinkIdentifier: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamSinkCount(self, pcStreamSinkCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStreamSinkByIndex(self, dwIndex: UInt32, ppStreamSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFStreamSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamSinkById(self, dwStreamSinkIdentifier: UInt32, ppStreamSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFStreamSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPresentationClock(self, pPresentationClock: Windows.Win32.Media.MediaFoundation.IMFPresentationClock_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPresentationClock(self, ppPresentationClock: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSinkPreroll(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5dfd4b2a-7674-4110-a4e6-8a68fd5f3688}')
    @commethod(3)
    def NotifyPreroll(self, hnsUpcomingStartTime: Int64) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSource(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEventGenerator
    _iid_ = Guid('{279a808d-aec7-40c8-9c6b-a6b492c78a66}')
    @commethod(7)
    def GetCharacteristics(self, pdwCharacteristics: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreatePresentationDescriptor(self, ppPresentationDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Start(self, pPresentationDescriptor: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head, pguidTimeFormat: POINTER(Guid), pvarStartPosition: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSource2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaSourceEx
    _iid_ = Guid('{fbb03414-d13b-4786-8319-5ac51fc0a136}')
    @commethod(16)
    def SetMediaType(self, dwStreamID: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSourceEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaSource
    _iid_ = Guid('{3c9b2eb9-86d5-4514-a394-f56664f9f0d8}')
    @commethod(13)
    def GetSourceAttributes(self, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStreamAttributes(self, dwStreamIdentifier: UInt32, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetD3DManager(self, pManager: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSourceExtension(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e467b94e-a713-4562-a802-816a42e9008a}')
    @commethod(3)
    def GetSourceBuffers(self) -> Windows.Win32.Media.MediaFoundation.IMFSourceBufferList_head: ...
    @commethod(4)
    def GetActiveSourceBuffers(self) -> Windows.Win32.Media.MediaFoundation.IMFSourceBufferList_head: ...
    @commethod(5)
    def GetReadyState(self) -> Windows.Win32.Media.MediaFoundation.MF_MSE_READY: ...
    @commethod(6)
    def GetDuration(self) -> Double: ...
    @commethod(7)
    def SetDuration(self, duration: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddSourceBuffer(self, type: Windows.Win32.Foundation.BSTR, pNotify: Windows.Win32.Media.MediaFoundation.IMFSourceBufferNotify_head, ppSourceBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFSourceBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveSourceBuffer(self, pSourceBuffer: Windows.Win32.Media.MediaFoundation.IMFSourceBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetEndOfStream(self, error: Windows.Win32.Media.MediaFoundation.MF_MSE_ERROR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsTypeSupported(self, type: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(12)
    def GetSourceBuffer(self, dwStreamIndex: UInt32) -> Windows.Win32.Media.MediaFoundation.IMFSourceBuffer_head: ...
class IMFMediaSourceExtensionLiveSeekableRange(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d1abfd6-450a-4d92-9efc-d6b6cbc1f4da}')
    @commethod(3)
    def SetLiveSeekableRange(self, start: Double, end: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ClearLiveSeekableRange(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSourceExtensionNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7901327-05dd-4469-a7b7-0e01979e361d}')
    @commethod(3)
    def OnSourceOpen(self) -> Void: ...
    @commethod(4)
    def OnSourceEnded(self) -> Void: ...
    @commethod(5)
    def OnSourceClose(self) -> Void: ...
class IMFMediaSourcePresentationProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e1d600a-c9f3-442d-8c51-a42d2d49452f}')
    @commethod(3)
    def ForceEndOfPresentation(self, pPresentationDescriptor: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaSourceTopologyProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e1d6009-c9f3-442d-8c51-a42d2d49452f}')
    @commethod(3)
    def GetMediaSourceTopology(self, pPresentationDescriptor: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head, ppTopology: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopology_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaStream(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEventGenerator
    _iid_ = Guid('{d182108f-4ec6-443f-aa42-a71106ec825f}')
    @commethod(7)
    def GetMediaSource(self, ppMediaSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamDescriptor(self, ppStreamDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.IMFStreamDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RequestSample(self, pToken: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaStream2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaStream
    _iid_ = Guid('{c5bc37d6-75c7-46a1-a132-81b5f723c20f}')
    @commethod(10)
    def SetStreamState(self, value: Windows.Win32.Media.MediaFoundation.MF_STREAM_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStreamState(self, value: POINTER(Windows.Win32.Media.MediaFoundation.MF_STREAM_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaStreamSourceSampleRequest(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{380b9af9-a85b-4e78-a2af-ea5ce645c6b4}')
    @commethod(3)
    def SetSample(self, value: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaTimeRange(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db71a2fc-078a-414e-9df9-8c2531b0aa6c}')
    @commethod(3)
    def GetLength(self) -> UInt32: ...
    @commethod(4)
    def GetStart(self, index: UInt32, pStart: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEnd(self, index: UInt32, pEnd: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ContainsTime(self, time: Double) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(7)
    def AddRange(self, startTime: Double, endTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaType(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{44ae0fa8-ea31-4109-8d2e-4cae4997c555}')
    @commethod(33)
    def GetMajorType(self, pguidMajorType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def IsCompressedFormat(self, pfCompressed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def IsEqual(self, pIMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetRepresentation(self, guidRepresentation: Guid, ppvRepresentation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def FreeRepresentation(self, guidRepresentation: Guid, pvRepresentation: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMediaTypeHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e93dcf6c-4b07-4e1e-8123-aa16ed6eadf5}')
    @commethod(3)
    def IsMediaTypeSupported(self, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMediaTypeCount(self, pdwTypeCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMediaTypeByIndex(self, dwIndex: UInt32, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetCurrentMediaType(self, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentMediaType(self, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMajorType(self, pguidMajorType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMetadata(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f88cfb8c-ef16-4991-b450-cb8c69e51704}')
    @commethod(3)
    def SetLanguage(self, pwszRFC1766: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLanguage(self, ppwszRFC1766: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAllLanguages(self, ppvLanguages: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProperty(self, pwszName: Windows.Win32.Foundation.PWSTR, ppvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProperty(self, pwszName: Windows.Win32.Foundation.PWSTR, ppvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeleteProperty(self, pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAllPropertyNames(self, ppvNames: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMetadataProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56181d2d-e221-4adb-b1c8-3cee6a53f76f}')
    @commethod(3)
    def GetMFMetadata(self, pPresentationDescriptor: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head, dwStreamIdentifier: UInt32, dwFlags: UInt32, ppMFMetadata: POINTER(Windows.Win32.Media.MediaFoundation.IMFMetadata_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMuxStreamAttributesManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ce8bd576-e440-43b3-be34-1e53f565f7e8}')
    @commethod(3)
    def GetStreamCount(self, pdwMuxStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttributes(self, dwMuxStreamIndex: UInt32, ppStreamAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMuxStreamMediaTypeManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{505a2c72-42f7-4690-aeab-8f513d0ffdb8}')
    @commethod(3)
    def GetStreamCount(self, pdwMuxStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMediaType(self, dwMuxStreamIndex: UInt32, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamConfigurationCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddStreamConfiguration(self, ullStreamMask: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveStreamConfiguration(self, ullStreamMask: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamConfiguration(self, ulIndex: UInt32, pullStreamMask: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFMuxStreamSampleManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{74abbc19-b1cc-4e41-bb8b-9d9b86a8f6ca}')
    @commethod(3)
    def GetStreamCount(self, pdwMuxStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSample(self, dwMuxStreamIndex: UInt32, ppSample: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamConfiguration(self) -> UInt64: ...
class IMFNetCredential(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b87ef6a-7ed8-434f-ba0e-184fac1628d1}')
    @commethod(3)
    def SetUser(self, pbData: POINTER(Byte), cbData: UInt32, fDataIsEncrypted: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPassword(self, pbData: POINTER(Byte), cbData: UInt32, fDataIsEncrypted: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUser(self, pbData: POINTER(Byte), pcbData: POINTER(UInt32), fEncryptData: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPassword(self, pbData: POINTER(Byte), pcbData: POINTER(UInt32), fEncryptData: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoggedOnUser(self, pfLoggedOnUser: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFNetCredentialCache(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b87ef6c-7ed8-434f-ba0e-184fac1628d1}')
    @commethod(3)
    def GetCredential(self, pszUrl: Windows.Win32.Foundation.PWSTR, pszRealm: Windows.Win32.Foundation.PWSTR, dwAuthenticationFlags: UInt32, ppCred: POINTER(Windows.Win32.Media.MediaFoundation.IMFNetCredential_head), pdwRequirementsFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetGood(self, pCred: Windows.Win32.Media.MediaFoundation.IMFNetCredential_head, fGood: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUserOptions(self, pCred: Windows.Win32.Media.MediaFoundation.IMFNetCredential_head, dwOptionsFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFNetCredentialManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b87ef6b-7ed8-434f-ba0e-184fac1628d1}')
    @commethod(3)
    def BeginGetCredentials(self, pParam: POINTER(Windows.Win32.Media.MediaFoundation.MFNetCredentialManagerGetParam_head), pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndGetCredentials(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, ppCred: POINTER(Windows.Win32.Media.MediaFoundation.IMFNetCredential_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetGood(self, pCred: Windows.Win32.Media.MediaFoundation.IMFNetCredential_head, fGood: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMFNetCrossOriginSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc2b7d44-a72d-49d5-8376-1480dee58b22}')
    @commethod(3)
    def GetCrossOriginPolicy(self, pPolicy: POINTER(Windows.Win32.Media.MediaFoundation.MF_CROSS_ORIGIN_POLICY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceOrigin(self, wszSourceOrigin: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsSameOrigin(self, wszURL: Windows.Win32.Foundation.PWSTR, pfIsSameOrigin: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFNetProxyLocator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e9cd0383-a268-4bb4-82de-658d53574d41}')
    @commethod(3)
    def FindFirstProxy(self, pszHost: Windows.Win32.Foundation.PWSTR, pszUrl: Windows.Win32.Foundation.PWSTR, fReserved: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindNextProxy(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterProxyResult(self, hrOp: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentProxy(self, pszStr: Windows.Win32.Foundation.PWSTR, pcchStr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Clone(self, ppProxyLocator: POINTER(Windows.Win32.Media.MediaFoundation.IMFNetProxyLocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFNetProxyLocatorFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e9cd0384-a268-4bb4-82de-658d53574d41}')
    @commethod(3)
    def CreateProxyLocator(self, pszProtocol: Windows.Win32.Foundation.PWSTR, ppProxyLocator: POINTER(Windows.Win32.Media.MediaFoundation.IMFNetProxyLocator_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFNetResourceFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{091878a3-bf11-4a5c-bc9f-33995b06ef2d}')
    @commethod(3)
    def OnRedirect(self, pszUrl: Windows.Win32.Foundation.PWSTR, pvbCancel: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSendingRequest(self, pszUrl: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IMFNetSchemeHandlerConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7be19e73-c9bf-468a-ac5a-a5e8653bec87}')
    @commethod(3)
    def GetNumberOfSupportedProtocols(self, pcProtocols: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSupportedProtocolType(self, nProtocolIndex: UInt32, pnProtocolType: POINTER(Windows.Win32.Media.MediaFoundation.MFNETSOURCE_PROTOCOL_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ResetProtocolRolloverSettings(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFObjectReferenceStream(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09ef5be3-c8a7-469e-8b70-73bf25bb193f}')
    @commethod(3)
    def SaveReference(self, riid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadReference(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFOutputPolicy(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{7f00f10a-daed-41af-ab26-5fdfa4dfba3c}')
    @commethod(33)
    def GenerateRequiredSchemas(self, dwAttributes: UInt32, guidOutputSubType: Guid, rgGuidProtectionSchemasSupported: POINTER(Guid), cProtectionSchemasSupported: UInt32, ppRequiredProtectionSchemas: POINTER(Windows.Win32.Media.MediaFoundation.IMFCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetOriginatorID(self, pguidOriginatorID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetMinimumGRLVersion(self, pdwMinimumGRLVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFOutputSchema(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{7be0fc5b-abd9-44fb-a5c8-f50136e71599}')
    @commethod(33)
    def GetSchemaType(self, pguidSchemaType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetConfigurationData(self, pdwVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetOriginatorID(self, pguidOriginatorID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFOutputTrustAuthority(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d19f8e94-b126-4446-890c-5dcb7ad71453}')
    @commethod(3)
    def GetAction(self, pAction: POINTER(Windows.Win32.Media.MediaFoundation.MFPOLICYMANAGER_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPolicy(self, ppPolicy: POINTER(Windows.Win32.Media.MediaFoundation.IMFOutputPolicy_head), nPolicy: UInt32, ppbTicket: POINTER(POINTER(Byte)), pcbTicket: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMPClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6c4e655d-ead8-4421-b6b9-54dcdbbdf820}')
    @commethod(3)
    def SetPMPHost(self, pPMPHost: Windows.Win32.Media.MediaFoundation.IMFPMPHost_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMPClientApp(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c004f646-be2c-48f3-93a2-a0983eba1108}')
    @commethod(3)
    def SetPMPHost(self, pPMPHost: Windows.Win32.Media.MediaFoundation.IMFPMPHostApp_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMPHost(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f70ca1a9-fdc7-4782-b994-adffb1c98606}')
    @commethod(3)
    def LockProcess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnlockProcess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateObjectByCLSID(self, clsid: POINTER(Guid), pStream: Windows.Win32.System.Com.IStream_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMPHostApp(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{84d2054a-3aa1-4728-a3b0-440a418cf49c}')
    @commethod(3)
    def LockProcess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnlockProcess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ActivateClassById(self, id: Windows.Win32.Foundation.PWSTR, pStream: Windows.Win32.System.Com.IStream_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMPServer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{994e23af-1cc2-493c-b9fa-46f1cb040fa4}')
    @commethod(3)
    def LockProcess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnlockProcess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateObjectByCLSID(self, clsid: POINTER(Guid), riid: POINTER(Guid), ppObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMediaItem(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90eb3e6b-ecbf-45cc-b1da-c6fe3ea70d57}')
    @commethod(3)
    def GetMediaPlayer(self, ppMediaPlayer: POINTER(Windows.Win32.Media.MediaFoundation.IMFPMediaPlayer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetURL(self, ppwszURL: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObject(self, ppIUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUserData(self, pdwUserData: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetUserData(self, dwUserData: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStartStopPosition(self, pguidStartPositionType: POINTER(Guid), pvStartValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pguidStopPositionType: POINTER(Guid), pvStopValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetStartStopPosition(self, pguidStartPositionType: POINTER(Guid), pvStartValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pguidStopPositionType: POINTER(Guid), pvStopValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def HasVideo(self, pfHasVideo: POINTER(Windows.Win32.Foundation.BOOL), pfSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def HasAudio(self, pfHasAudio: POINTER(Windows.Win32.Foundation.BOOL), pfSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsProtected(self, pfProtected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDuration(self, guidPositionType: POINTER(Guid), pvDurationValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNumberOfStreams(self, pdwStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetStreamSelection(self, dwStreamIndex: UInt32, pfEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStreamSelection(self, dwStreamIndex: UInt32, fEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStreamAttribute(self, dwStreamIndex: UInt32, guidMFAttribute: POINTER(Guid), pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetPresentationAttribute(self, guidMFAttribute: POINTER(Guid), pvValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCharacteristics(self, pCharacteristics: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetStreamSink(self, dwStreamIndex: UInt32, pMediaSink: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetMetadata(self, ppMetadataStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMediaPlayer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a714590a-58af-430a-85bf-44f5ec838d85}')
    @commethod(3)
    def Play(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FrameStep(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPosition(self, guidPositionType: POINTER(Guid), pvPositionValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPosition(self, guidPositionType: POINTER(Guid), pvPositionValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDuration(self, guidPositionType: POINTER(Guid), pvDurationValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRate(self, flRate: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRate(self, pflRate: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSupportedRates(self, fForwardDirection: Windows.Win32.Foundation.BOOL, pflSlowestRate: POINTER(Single), pflFastestRate: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetState(self, peState: POINTER(Windows.Win32.Media.MediaFoundation.MFP_MEDIAPLAYER_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateMediaItemFromURL(self, pwszURL: Windows.Win32.Foundation.PWSTR, fSync: Windows.Win32.Foundation.BOOL, dwUserData: UIntPtr, ppMediaItem: POINTER(Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateMediaItemFromObject(self, pIUnknownObj: Windows.Win32.System.Com.IUnknown_head, fSync: Windows.Win32.Foundation.BOOL, dwUserData: UIntPtr, ppMediaItem: POINTER(Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetMediaItem(self, pIMFPMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ClearMediaItem(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetMediaItem(self, ppIMFPMediaItem: POINTER(Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetVolume(self, pflVolume: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetVolume(self, flVolume: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetBalance(self, pflBalance: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetBalance(self, flBalance: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetMute(self, pfMute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetMute(self, fMute: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetNativeVideoSize(self, pszVideo: POINTER(Windows.Win32.Foundation.SIZE_head), pszARVideo: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetIdealVideoSize(self, pszMin: POINTER(Windows.Win32.Foundation.SIZE_head), pszMax: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetVideoSourceRect(self, pnrcSource: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetVideoSourceRect(self, pnrcSource: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetAspectRatioMode(self, dwAspectRatioMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetAspectRatioMode(self, pdwAspectRatioMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetVideoWindow(self, phwndVideo: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def UpdateVideo(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetBorderColor(self, Clr: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetBorderColor(self, pClr: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def InsertEffect(self, pEffect: Windows.Win32.System.Com.IUnknown_head, fOptional: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def RemoveEffect(self, pEffect: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def RemoveAllEffects(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPMediaPlayerCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{766c8ffb-5fdb-4fea-a28d-b912996f51bd}')
    @commethod(3)
    def OnMediaPlayerEvent(self, pEventHeader: POINTER(Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER_head)) -> Void: ...
class IMFPluginControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5c6c44bf-1db6-435b-9249-e8cd10fdec96}')
    @commethod(3)
    def GetPreferredClsid(self, pluginType: UInt32, selector: Windows.Win32.Foundation.PWSTR, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPreferredClsidByIndex(self, pluginType: UInt32, index: UInt32, selector: POINTER(Windows.Win32.Foundation.PWSTR), clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPreferredClsid(self, pluginType: UInt32, selector: Windows.Win32.Foundation.PWSTR, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsDisabled(self, pluginType: UInt32, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDisabledByIndex(self, pluginType: UInt32, index: UInt32, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDisabled(self, pluginType: UInt32, clsid: POINTER(Guid), disabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPluginControl2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFPluginControl
    _iid_ = Guid('{c6982083-3ddc-45cb-af5e-0f7a8ce4de77}')
    @commethod(9)
    def SetPolicy(self, policy: Windows.Win32.Media.MediaFoundation.MF_PLUGIN_CONTROL_POLICY) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPresentationClock(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFClock
    _iid_ = Guid('{868ce85c-8ea9-4f55-ab82-b009a910a805}')
    @commethod(8)
    def SetTimeSource(self, pTimeSource: Windows.Win32.Media.MediaFoundation.IMFPresentationTimeSource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTimeSource(self, ppTimeSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationTimeSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetTime(self, phnsClockTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddClockStateSink(self, pStateSink: Windows.Win32.Media.MediaFoundation.IMFClockStateSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveClockStateSink(self, pStateSink: Windows.Win32.Media.MediaFoundation.IMFClockStateSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Start(self, llClockStartOffset: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPresentationDescriptor(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{03cb2711-24d7-4db6-a17f-f3a7a479a536}')
    @commethod(33)
    def GetStreamDescriptorCount(self, pdwDescriptorCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetStreamDescriptorByIndex(self, dwIndex: UInt32, pfSelected: POINTER(Windows.Win32.Foundation.BOOL), ppDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.IMFStreamDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SelectStream(self, dwDescriptorIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def DeselectStream(self, dwDescriptorIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Clone(self, ppPresentationDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFPresentationTimeSource(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFClock
    _iid_ = Guid('{7ff12cce-f76f-41c2-863b-1666c8e5e139}')
    @commethod(8)
    def GetUnderlyingClock(self, ppClock: POINTER(Windows.Win32.Media.MediaFoundation.IMFClock_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFProtectedEnvironmentAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ef5dc845-f0d9-4ec9-b00c-cb5183d38434}')
    @commethod(3)
    def Call(self, inputLength: UInt32, input: POINTER(Byte), outputLength: UInt32, output: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReadGRL(self, outputLength: POINTER(UInt32), output: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IMFQualityAdvise(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ec15e2e9-e36b-4f7c-8758-77d452ef4ce7}')
    @commethod(3)
    def SetDropMode(self, eDropMode: Windows.Win32.Media.MediaFoundation.MF_QUALITY_DROP_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetQualityLevel(self, eQualityLevel: Windows.Win32.Media.MediaFoundation.MF_QUALITY_LEVEL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDropMode(self, peDropMode: POINTER(Windows.Win32.Media.MediaFoundation.MF_QUALITY_DROP_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetQualityLevel(self, peQualityLevel: POINTER(Windows.Win32.Media.MediaFoundation.MF_QUALITY_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DropTime(self, hnsAmountToDrop: Int64) -> Windows.Win32.Foundation.HRESULT: ...
class IMFQualityAdvise2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFQualityAdvise
    _iid_ = Guid('{f3706f0d-8ea2-4886-8000-7155e9ec2eae}')
    @commethod(8)
    def NotifyQualityEvent(self, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFQualityAdviseLimits(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfcd8e4d-30b5-4567-acaa-8eb5b7853dc9}')
    @commethod(3)
    def GetMaximumDropMode(self, peDropMode: POINTER(Windows.Win32.Media.MediaFoundation.MF_QUALITY_DROP_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMinimumQualityLevel(self, peQualityLevel: POINTER(Windows.Win32.Media.MediaFoundation.MF_QUALITY_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFQualityManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d009d86-5b9f-4115-b1fc-9f80d52ab8ab}')
    @commethod(3)
    def NotifyTopology(self, pTopology: Windows.Win32.Media.MediaFoundation.IMFTopology_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyPresentationClock(self, pClock: Windows.Win32.Media.MediaFoundation.IMFPresentationClock_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyProcessInput(self, pNode: Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head, lInputIndex: Int32, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifyProcessOutput(self, pNode: Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head, lOutputIndex: Int32, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyQualityEvent(self, pObject: Windows.Win32.System.Com.IUnknown_head, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRateControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{88ddcd21-03c3-4275-91ed-55ee3929328f}')
    @commethod(3)
    def SetRate(self, fThin: Windows.Win32.Foundation.BOOL, flRate: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRate(self, pfThin: POINTER(Windows.Win32.Foundation.BOOL), pflRate: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRateSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0a9ccdbc-d797-4563-9667-94ec5d79292d}')
    @commethod(3)
    def GetSlowestRate(self, eDirection: Windows.Win32.Media.MediaFoundation.MFRATE_DIRECTION, fThin: Windows.Win32.Foundation.BOOL, pflRate: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFastestRate(self, eDirection: Windows.Win32.Media.MediaFoundation.MFRATE_DIRECTION, fThin: Windows.Win32.Foundation.BOOL, pflRate: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsRateSupported(self, fThin: Windows.Win32.Foundation.BOOL, flRate: Single, pflNearestSupportedRate: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFReadWriteClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7fe2e12-661c-40da-92f9-4f002ab67627}')
    @commethod(3)
    def CreateInstanceFromURL(self, clsid: POINTER(Guid), pwszURL: Windows.Win32.Foundation.PWSTR, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInstanceFromObject(self, clsid: POINTER(Guid), punkObject: Windows.Win32.System.Com.IUnknown_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRealTimeClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2347d60b-3fb5-480c-8803-8df3adcd3ef0}')
    @commethod(3)
    def RegisterThreads(self, dwTaskIndex: UInt32, wszClass: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterThreads(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetWorkQueue(self, dwWorkQueueId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRealTimeClientEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03910848-ab16-4611-b100-17b88ae2f248}')
    @commethod(3)
    def RegisterThreadsEx(self, pdwTaskIndex: POINTER(UInt32), wszClassName: Windows.Win32.Foundation.PWSTR, lBasePriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterThreads(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetWorkQueueEx(self, dwMultithreadedWorkQueueId: UInt32, lWorkItemBasePriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRelativePanelReport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f25362ea-2c0e-447f-81e2-755914cdc0c3}')
    @commethod(3)
    def GetRelativePanel(self, panel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRelativePanelWatcher(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFShutdown
    _iid_ = Guid('{421af7f6-573e-4ad0-8fda-2e57cedb18c6}')
    @commethod(5)
    def BeginGetReport(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndGetReport(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, ppRelativePanelReport: POINTER(Windows.Win32.Media.MediaFoundation.IMFRelativePanelReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetReport(self, ppRelativePanelReport: POINTER(Windows.Win32.Media.MediaFoundation.IMFRelativePanelReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRemoteAsyncCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a27003d0-2354-4f2a-8d6a-ab7cff15437e}')
    @commethod(3)
    def Invoke(self, hr: Windows.Win32.Foundation.HRESULT, pRemoteResult: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRemoteDesktopPlugin(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cde6309-cae0-4940-907e-c1ec9c3d1d4a}')
    @commethod(3)
    def UpdateTopology(self, pTopology: Windows.Win32.Media.MediaFoundation.IMFTopology_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFRemoteProxy(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{994e23ad-1cc2-493c-b9fa-46f1cb040fa4}')
    @commethod(3)
    def GetRemoteObject(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRemoteHost(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSAMIStyle(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7e025dd-5303-4a62-89d6-e747e1efac73}')
    @commethod(3)
    def GetStyleCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStyles(self, pPropVarStyleArray: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSelectedStyle(self, pwszStyle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSelectedStyle(self, ppwszStyle: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSSLCertificateManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61f7d887-1230-4a8b-aeba-8ad434d1a64d}')
    @commethod(3)
    def GetClientCertificate(self, pszURL: Windows.Win32.Foundation.PWSTR, ppbData: POINTER(POINTER(Byte)), pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginGetClientCertificate(self, pszURL: Windows.Win32.Foundation.PWSTR, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetClientCertificate(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, ppbData: POINTER(POINTER(Byte)), pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCertificatePolicy(self, pszURL: Windows.Win32.Foundation.PWSTR, pfOverrideAutomaticCheck: POINTER(Windows.Win32.Foundation.BOOL), pfClientCertificateAvailable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnServerCertificate(self, pszURL: Windows.Win32.Foundation.PWSTR, pbData: POINTER(Byte), cbData: UInt32, pfIsGood: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSample(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{c40a00f2-b93a-4d80-ae8c-5a1c634f58e4}')
    @commethod(33)
    def GetSampleFlags(self, pdwSampleFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetSampleFlags(self, dwSampleFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetSampleTime(self, phnsSampleTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetSampleTime(self, hnsSampleTime: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetSampleDuration(self, phnsSampleDuration: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetSampleDuration(self, hnsSampleDuration: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetBufferCount(self, pdwBufferCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetBufferByIndex(self, dwIndex: UInt32, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def ConvertToContiguousBuffer(self, ppBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def AddBuffer(self, pBuffer: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def RemoveBufferByIndex(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def RemoveAllBuffers(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetTotalLength(self, pcbTotalLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CopyToBuffer(self, pBuffer: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSampleAllocatorControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{da62b958-3a38-4a97-bd27-149c640c0771}')
    @commethod(3)
    def SetDefaultAllocator(self, dwOutputStreamID: UInt32, pAllocator: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAllocatorUsage(self, dwOutputStreamID: UInt32, pdwInputStreamID: POINTER(UInt32), peUsage: POINTER(Windows.Win32.Media.MediaFoundation.MFSampleAllocatorUsage)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSampleGrabberSinkCallback(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFClockStateSink
    _iid_ = Guid('{8c7b80bf-ee42-4b59-b1df-55668e1bdca8}')
    @commethod(8)
    def OnSetPresentationClock(self, pPresentationClock: Windows.Win32.Media.MediaFoundation.IMFPresentationClock_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnProcessSample(self, guidMajorMediaType: POINTER(Guid), dwSampleFlags: UInt32, llSampleTime: Int64, llSampleDuration: Int64, pSampleBuffer: POINTER(Byte), dwSampleSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnShutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSampleGrabberSinkCallback2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFSampleGrabberSinkCallback
    _iid_ = Guid('{ca86aa50-c46e-429e-ab27-16d6ac6844cb}')
    @commethod(11)
    def OnProcessSampleEx(self, guidMajorMediaType: POINTER(Guid), dwSampleFlags: UInt32, llSampleTime: Int64, llSampleDuration: Int64, pSampleBuffer: POINTER(Byte), dwSampleSize: UInt32, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSampleOutputStream(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8feed468-6f7e-440d-869a-49bdd283ad0d}')
    @commethod(3)
    def BeginWriteSample(self, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndWriteSample(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSampleProtection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8e36395f-c7b9-43c4-a54d-512b4af63c95}')
    @commethod(3)
    def GetInputProtectionVersion(self, pdwVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputProtectionVersion(self, pdwVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProtectionCertificate(self, dwVersion: UInt32, ppCert: POINTER(POINTER(Byte)), pcbCert: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitOutputProtection(self, dwVersion: UInt32, dwOutputId: UInt32, pbCert: POINTER(Byte), cbCert: UInt32, ppbSeed: POINTER(POINTER(Byte)), pcbSeed: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InitInputProtection(self, dwVersion: UInt32, dwInputId: UInt32, pbSeed: POINTER(Byte), cbSeed: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSaveJob(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e9931663-80bf-4c6e-98af-5dcf58747d1f}')
    @commethod(3)
    def BeginSave(self, pStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndSave(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelSave(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProgress(self, pdwPercentComplete: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSchemeHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d4c7b74-52a0-4bb7-b0db-55f29f47a668}')
    @commethod(3)
    def BeginCreateObject(self, pwszURL: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pProps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppIUnknownCancelCookie: POINTER(Windows.Win32.System.Com.IUnknown_head), pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndCreateObject(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pObjectType: POINTER(Windows.Win32.Media.MediaFoundation.MF_OBJECT_TYPE), ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelObjectCreation(self, pIUnknownCancelCookie: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSecureBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c1209904-e584-4752-a2d6-7f21693f8b21}')
    @commethod(3)
    def GetIdentifier(self, pGuidIdentifier: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSecureChannel(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0ae555d-3b12-4d97-b060-0990bc5aeb67}')
    @commethod(3)
    def GetCertificate(self, ppCert: POINTER(POINTER(Byte)), pcbCert: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetupSession(self, pbEncryptedSessionKey: POINTER(Byte), cbSessionKey: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSeekInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26afea53-d9ed-42b5-ab80-e64f9ee34779}')
    @commethod(3)
    def GetNearestKeyFrames(self, pguidTimeFormat: POINTER(Guid), pvarStartPosition: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarPreviousKeyFrame: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarNextKeyFrame: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorActivitiesReport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{683f7a5e-4a19-43cd-b1a9-dbf4ab3f7777}')
    @commethod(3)
    def GetCount(self, pcCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetActivityReport(self, Index: UInt32, sensorActivityReport: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorActivityReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetActivityReportByDeviceName(self, SymbolicName: Windows.Win32.Foundation.PWSTR, sensorActivityReport: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorActivityReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorActivitiesReportCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de5072ee-dbe3-46dc-8a87-b6f631194751}')
    @commethod(3)
    def OnActivitiesReport(self, sensorActivitiesReport: Windows.Win32.Media.MediaFoundation.IMFSensorActivitiesReport_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorActivityMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0cef145-b3f4-4340-a2e5-7a5080ca05cb}')
    @commethod(3)
    def Start(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorActivityReport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3e8c4be1-a8c2-4528-90de-2851bde5fead}')
    @commethod(3)
    def GetFriendlyName(self, FriendlyName: Windows.Win32.Foundation.PWSTR, cchFriendlyName: UInt32, pcchWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSymbolicLink(self, SymbolicLink: Windows.Win32.Foundation.PWSTR, cchSymbolicLink: UInt32, pcchWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProcessCount(self, pcCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetProcessActivity(self, Index: UInt32, ppProcessActivity: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorProcessActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorDevice(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb9f48f2-2a18-4e28-9730-786f30f04dc4}')
    @commethod(3)
    def GetDeviceId(self, pDeviceId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceType(self, pType: POINTER(Windows.Win32.Media.MediaFoundation.MFSensorDeviceType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFlags(self, pFlags: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSymbolicLink(self, SymbolicLink: Windows.Win32.Foundation.PWSTR, cchSymbolicLink: Int32, pcchWritten: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceAttributes(self, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStreamAttributesCount(self, eType: Windows.Win32.Media.MediaFoundation.MFSensorStreamType, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStreamAttributes(self, eType: Windows.Win32.Media.MediaFoundation.MFSensorStreamType, dwIndex: UInt32, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSensorDeviceMode(self, eMode: Windows.Win32.Media.MediaFoundation.MFSensorDeviceMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSensorDeviceMode(self, peMode: POINTER(Windows.Win32.Media.MediaFoundation.MFSensorDeviceMode)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorGroup(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4110243a-9757-461f-89f1-f22345bcab4e}')
    @commethod(3)
    def GetSymbolicLink(self, SymbolicLink: Windows.Win32.Foundation.PWSTR, cchSymbolicLink: Int32, pcchWritten: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(self, pFlags: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSensorGroupAttributes(self, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSensorDeviceCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSensorDevice(self, dwIndex: UInt32, ppDevice: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDefaultSensorDeviceIndex(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDefaultSensorDeviceIndex(self, pdwIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateMediaSource(self, ppSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorProcessActivity(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{39dc7f4a-b141-4719-813c-a7f46162a2b8}')
    @commethod(3)
    def GetProcessId(self, pPID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamingState(self, pfStreaming: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamingMode(self, pMode: POINTER(Windows.Win32.Media.MediaFoundation.MFSensorDeviceMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReportTime(self, pft: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorProfile(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22f765d1-8dab-4107-846d-56baf72215e7}')
    @commethod(3)
    def GetProfileId(self, pId: POINTER(Windows.Win32.Media.MediaFoundation.SENSORPROFILEID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddProfileFilter(self, StreamId: UInt32, wzFilterSetString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsMediaTypeSupported(self, StreamId: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pfSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddBlockedControl(self, wzBlockedControl: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorProfileCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c95ea55b-0187-48be-9353-8d2507662351}')
    @commethod(3)
    def GetProfileCount(self) -> UInt32: ...
    @commethod(4)
    def GetProfile(self, Index: UInt32, ppProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddProfile(self, pProfile: Windows.Win32.Media.MediaFoundation.IMFSensorProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindProfile(self, ProfileId: POINTER(Windows.Win32.Media.MediaFoundation.SENSORPROFILEID_head), ppProfile: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveProfileByIndex(self, Index: UInt32) -> Void: ...
    @commethod(8)
    def RemoveProfile(self, ProfileId: POINTER(Windows.Win32.Media.MediaFoundation.SENSORPROFILEID_head)) -> Void: ...
class IMFSensorStream(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{e9a42171-c56e-498a-8b39-eda5a070b7fc}')
    @commethod(33)
    def GetMediaTypeCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetMediaType(self, dwIndex: UInt32, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def CloneSensorStream(self, ppStream: POINTER(Windows.Win32.Media.MediaFoundation.IMFSensorStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSensorTransformFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eed9c2ee-66b4-4f18-a697-ac7d3960215c}')
    @commethod(3)
    def GetFactoryAttributes(self, ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeFactory(self, dwMaxTransformCount: UInt32, pSensorDevices: Windows.Win32.Media.MediaFoundation.IMFCollection_head, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTransformCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransformInformation(self, TransformIndex: UInt32, pguidTransformId: POINTER(Guid), ppAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head), ppStreamInformation: POINTER(Windows.Win32.Media.MediaFoundation.IMFCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateTransform(self, guidSensorTransformID: POINTER(Guid), pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppDeviceMFT: POINTER(Windows.Win32.Media.MediaFoundation.IMFDeviceTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSequencerSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{197cd219-19cb-4de1-a64c-acf2edcbe59e}')
    @commethod(3)
    def AppendTopology(self, pTopology: Windows.Win32.Media.MediaFoundation.IMFTopology_head, dwFlags: UInt32, pdwId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteTopology(self, dwId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPresentationContext(self, pPD: Windows.Win32.Media.MediaFoundation.IMFPresentationDescriptor_head, pId: POINTER(UInt32), ppTopology: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopology_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UpdateTopology(self, dwId: UInt32, pTopology: Windows.Win32.Media.MediaFoundation.IMFTopology_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateTopologyFlags(self, dwId: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSharingEngineClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2ba61f92-8305-413b-9733-faf15f259384}')
    @commethod(3)
    def CreateInstance(self, dwFlags: UInt32, pAttr: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, ppEngine: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFShutdown(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{97ec2ea4-0e42-4937-97ac-9d6d328824e1}')
    @commethod(3)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetShutdownStatus(self, pStatus: POINTER(Windows.Win32.Media.MediaFoundation.MFSHUTDOWN_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSignedLibrary(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4a724bca-ff6a-4c07-8e0d-7a358421cf06}')
    @commethod(3)
    def GetProcedureAddress(self, name: Windows.Win32.Foundation.PSTR, address: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSimpleAudioVolume(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{089edf13-cf71-4338-8d13-9e569dbdc319}')
    @commethod(3)
    def SetMasterVolume(self, fLevel: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMasterVolume(self, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMute(self, bMute: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMute(self, pbMute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSinkWriter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3137f1cd-fe5e-4805-a5d8-fb477448cb3d}')
    @commethod(3)
    def AddStream(self, pTargetMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pdwStreamIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetInputMediaType(self, dwStreamIndex: UInt32, pInputMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pEncodingParameters: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginWriting(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteSample(self, dwStreamIndex: UInt32, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SendStreamTick(self, dwStreamIndex: UInt32, llTimestamp: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PlaceMarker(self, dwStreamIndex: UInt32, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NotifyEndOfSegment(self, dwStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Flush(self, dwStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Finalize(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetServiceForStream(self, dwStreamIndex: UInt32, guidService: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetStatistics(self, dwStreamIndex: UInt32, pStats: POINTER(Windows.Win32.Media.MediaFoundation.MF_SINK_WRITER_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSinkWriterCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{666f76de-33d2-41b9-a458-29ed0a972c58}')
    @commethod(3)
    def OnFinalize(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMarker(self, dwStreamIndex: UInt32, pvContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSinkWriterCallback2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFSinkWriterCallback
    _iid_ = Guid('{2456bd58-c067-4513-84fe-8d0c88ffdc61}')
    @commethod(5)
    def OnTransformChange(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnStreamError(self, dwStreamIndex: UInt32, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSinkWriterEncoderConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17c3779e-3cde-4ede-8c60-3899f5f53ad6}')
    @commethod(3)
    def SetTargetMediaType(self, dwStreamIndex: UInt32, pTargetMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pEncodingParameters: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PlaceEncodingParameters(self, dwStreamIndex: UInt32, pEncodingParameters: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSinkWriterEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFSinkWriter
    _iid_ = Guid('{588d72ab-5bc1-496a-8714-b70617141b25}')
    @commethod(14)
    def GetTransformForStream(self, dwStreamIndex: UInt32, dwTransformIndex: UInt32, pGuidCategory: POINTER(Guid), ppTransform: POINTER(Windows.Win32.Media.MediaFoundation.IMFTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2cd3a4b-af25-4d3d-9110-da0e6f8ee877}')
    @commethod(3)
    def GetUpdating(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def GetBuffered(self, ppBuffered: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTimeRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTimeStampOffset(self) -> Double: ...
    @commethod(6)
    def SetTimeStampOffset(self, offset: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAppendWindowStart(self) -> Double: ...
    @commethod(8)
    def SetAppendWindowStart(self, time: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAppendWindowEnd(self) -> Double: ...
    @commethod(10)
    def SetAppendWindowEnd(self, time: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Append(self, pData: POINTER(Byte), len: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AppendByteStream(self, pStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pMaxLen: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Abort(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Remove(self, start: Double, end: Double) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceBufferAppendMode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{19666fb4-babe-4c55-bc03-0a074da37e2a}')
    @commethod(3)
    def GetAppendMode(self) -> Windows.Win32.Media.MediaFoundation.MF_MSE_APPEND_MODE: ...
    @commethod(4)
    def SetAppendMode(self, mode: Windows.Win32.Media.MediaFoundation.MF_MSE_APPEND_MODE) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceBufferList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{249981f8-8325-41f3-b80c-3b9e3aad0cbe}')
    @commethod(3)
    def GetLength(self) -> UInt32: ...
    @commethod(4)
    def GetSourceBuffer(self, index: UInt32) -> Windows.Win32.Media.MediaFoundation.IMFSourceBuffer_head: ...
class IMFSourceBufferNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87e47623-2ceb-45d6-9b88-d8520c4dcbbc}')
    @commethod(3)
    def OnUpdateStart(self) -> Void: ...
    @commethod(4)
    def OnAbort(self) -> Void: ...
    @commethod(5)
    def OnError(self, hr: Windows.Win32.Foundation.HRESULT) -> Void: ...
    @commethod(6)
    def OnUpdate(self) -> Void: ...
    @commethod(7)
    def OnUpdateEnd(self) -> Void: ...
class IMFSourceOpenMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{059054b3-027c-494c-a27d-9113291cf87f}')
    @commethod(3)
    def OnSourceEvent(self, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70ae66f2-c809-4e4f-8915-bdcb406b7993}')
    @commethod(3)
    def GetStreamSelection(self, dwStreamIndex: UInt32, pfSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetStreamSelection(self, dwStreamIndex: UInt32, fSelected: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNativeMediaType(self, dwStreamIndex: UInt32, dwMediaTypeIndex: UInt32, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentMediaType(self, dwStreamIndex: UInt32, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCurrentMediaType(self, dwStreamIndex: UInt32, pdwReserved: POINTER(UInt32), pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetCurrentPosition(self, guidTimeFormat: POINTER(Guid), varPosition: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ReadSample(self, dwStreamIndex: UInt32, dwControlFlags: UInt32, pdwActualStreamIndex: POINTER(UInt32), pdwStreamFlags: POINTER(UInt32), pllTimestamp: POINTER(Int64), ppSample: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Flush(self, dwStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetServiceForStream(self, dwStreamIndex: UInt32, guidService: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPresentationAttribute(self, dwStreamIndex: UInt32, guidAttribute: POINTER(Guid), pvarAttribute: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceReaderCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{deec8d99-fa1d-4d82-84c2-2c8969944867}')
    @commethod(3)
    def OnReadSample(self, hrStatus: Windows.Win32.Foundation.HRESULT, dwStreamIndex: UInt32, dwStreamFlags: UInt32, llTimestamp: Int64, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFlush(self, dwStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(self, dwStreamIndex: UInt32, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceReaderCallback2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFSourceReaderCallback
    _iid_ = Guid('{cf839fe6-8c2a-4dd2-b6ea-c22d6961af05}')
    @commethod(6)
    def OnTransformChange(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnStreamError(self, dwStreamIndex: UInt32, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceReaderEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFSourceReader
    _iid_ = Guid('{7b981cf0-560e-4116-9875-b099895f23d7}')
    @commethod(13)
    def SetNativeMediaType(self, dwStreamIndex: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, pdwStreamFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddTransformForStream(self, dwStreamIndex: UInt32, pTransformOrActivate: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveAllTransformsForStream(self, dwStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTransformForStream(self, dwStreamIndex: UInt32, dwTransformIndex: UInt32, pGuidCategory: POINTER(Guid), ppTransform: POINTER(Windows.Win32.Media.MediaFoundation.IMFTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSourceResolver(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fbe5a32d-a497-4b61-bb85-97b1a848a6e3}')
    @commethod(3)
    def CreateObjectFromURL(self, pwszURL: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pProps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, pObjectType: POINTER(Windows.Win32.Media.MediaFoundation.MF_OBJECT_TYPE), ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateObjectFromByteStream(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pwszURL: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pProps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, pObjectType: POINTER(Windows.Win32.Media.MediaFoundation.MF_OBJECT_TYPE), ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginCreateObjectFromURL(self, pwszURL: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pProps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppIUnknownCancelCookie: POINTER(Windows.Win32.System.Com.IUnknown_head), pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndCreateObjectFromURL(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pObjectType: POINTER(Windows.Win32.Media.MediaFoundation.MF_OBJECT_TYPE), ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginCreateObjectFromByteStream(self, pByteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, pwszURL: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pProps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, ppIUnknownCancelCookie: POINTER(Windows.Win32.System.Com.IUnknown_head), pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EndCreateObjectFromByteStream(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pObjectType: POINTER(Windows.Win32.Media.MediaFoundation.MF_OBJECT_TYPE), ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CancelObjectCreation(self, pIUnknownCancelCookie: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSpatialAudioObjectBuffer(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaBuffer
    _iid_ = Guid('{d396ec8c-605e-4249-978d-72ad1c312872}')
    @commethod(8)
    def SetID(self, u32ID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetID(self, pu32ID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetType(self, type: Windows.Win32.Media.Audio.AudioObjectType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetType(self, pType: POINTER(Windows.Win32.Media.Audio.AudioObjectType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMetadataItems(self, ppMetadataItems: POINTER(Windows.Win32.Media.Audio.ISpatialAudioMetadataItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSpatialAudioSample(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFSample
    _iid_ = Guid('{abf28a9b-3393-4290-ba79-5ffc46d986b2}')
    @commethod(47)
    def GetObjectCount(self, pdwObjectCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def AddSpatialAudioObject(self, pAudioObjBuffer: Windows.Win32.Media.MediaFoundation.IMFSpatialAudioObjectBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetSpatialAudioObjectByIndex(self, dwIndex: UInt32, ppAudioObjBuffer: POINTER(Windows.Win32.Media.MediaFoundation.IMFSpatialAudioObjectBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFStreamDescriptor(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{56c03d9c-9dbb-45f5-ab4b-d80f47c05938}')
    @commethod(33)
    def GetStreamIdentifier(self, pdwStreamIdentifier: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetMediaTypeHandler(self, ppMediaTypeHandler: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTypeHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFStreamSink(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaEventGenerator
    _iid_ = Guid('{0a97b3cf-8e7c-4a3d-8f8c-0c843dc247fb}')
    @commethod(7)
    def GetMediaSink(self, ppMediaSink: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIdentifier(self, pdwIdentifier: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMediaTypeHandler(self, ppHandler: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaTypeHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ProcessSample(self, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def PlaceMarker(self, eMarkerType: Windows.Win32.Media.MediaFoundation.MFSTREAMSINK_MARKER_TYPE, pvarMarkerValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarContextValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFStreamingSinkConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9db7aa41-3cc5-40d4-8509-555804ad34cc}')
    @commethod(3)
    def StartStreaming(self, fSeekOffsetIsByteOffset: Windows.Win32.Foundation.BOOL, qwSeekOffset: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IMFSystemId(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fff4af3a-1fc1-4ef9-a29b-d26c49e2f31a}')
    @commethod(3)
    def GetData(self, size: POINTER(UInt32), data: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Setup(self, stage: UInt32, cbIn: UInt32, pbIn: POINTER(Byte), pcbOut: POINTER(UInt32), ppbOut: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimecodeTranslate(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ab9d8661-f7e8-4ef4-9861-89f334f94e74}')
    @commethod(3)
    def BeginConvertTimecodeToHNS(self, pPropVarTimecode: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndConvertTimecodeToHNS(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, phnsTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginConvertHNSToTimecode(self, hnsTime: Int64, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndConvertHNSToTimecode(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pPropVarTimecode: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedText(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f2a94c9-a3df-430d-9d0f-acd85ddc29af}')
    @commethod(3)
    def RegisterNotifications(self, notify: Windows.Win32.Media.MediaFoundation.IMFTimedTextNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SelectTrack(self, trackId: UInt32, selected: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddDataSource(self, byteStream: Windows.Win32.Media.MediaFoundation.IMFByteStream_head, label: Windows.Win32.Foundation.PWSTR, language: Windows.Win32.Foundation.PWSTR, kind: Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_TRACK_KIND, isDefault: Windows.Win32.Foundation.BOOL, trackId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddDataSourceFromUrl(self, url: Windows.Win32.Foundation.PWSTR, label: Windows.Win32.Foundation.PWSTR, language: Windows.Win32.Foundation.PWSTR, kind: Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_TRACK_KIND, isDefault: Windows.Win32.Foundation.BOOL, trackId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddTrack(self, label: Windows.Win32.Foundation.PWSTR, language: Windows.Win32.Foundation.PWSTR, kind: Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_TRACK_KIND, track: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextTrack_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveTrack(self, track: Windows.Win32.Media.MediaFoundation.IMFTimedTextTrack_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCueTimeOffset(self, offset: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCueTimeOffset(self, offset: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTracks(self, tracks: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextTrackList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetActiveTracks(self, activeTracks: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextTrackList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTextTracks(self, textTracks: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextTrackList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetMetadataTracks(self, metadataTracks: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextTrackList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetInBandEnabled(self, enabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def IsInBandEnabled(self) -> Windows.Win32.Foundation.BOOL: ...
class IMFTimedTextBinary(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ae3a412-0545-43c4-bf6f-6b97a5c6c432}')
    @commethod(3)
    def GetData(self, data: POINTER(POINTER(Byte)), length: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextBouten(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c5f3e8a-90c0-464e-8136-898d2975f847}')
    @commethod(3)
    def GetBoutenType(self, value: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_BOUTEN_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBoutenColor(self, value: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBoutenPosition(self, value: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_BOUTEN_POSITION)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextCue(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1e560447-9a2b-43e1-a94c-b0aaabfbfbc9}')
    @commethod(3)
    def GetId(self) -> UInt32: ...
    @commethod(4)
    def GetOriginalId(self, originalId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCueKind(self) -> Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_TRACK_KIND: ...
    @commethod(6)
    def GetStartTime(self) -> Double: ...
    @commethod(7)
    def GetDuration(self) -> Double: ...
    @commethod(8)
    def GetTrackId(self) -> UInt32: ...
    @commethod(9)
    def GetData(self, data: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextBinary_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRegion(self, region: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextRegion_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStyle(self, style: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextStyle_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLineCount(self) -> UInt32: ...
    @commethod(13)
    def GetLine(self, index: UInt32, line: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextFormattedText_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextCueList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ad128745-211b-40a0-9981-fe65f166d0fd}')
    @commethod(3)
    def GetLength(self) -> UInt32: ...
    @commethod(4)
    def GetCueByIndex(self, index: UInt32, cue: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextCue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCueById(self, id: UInt32, cue: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextCue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCueByOriginalId(self, originalId: Windows.Win32.Foundation.PWSTR, cue: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextCue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddTextCue(self, start: Double, duration: Double, text: Windows.Win32.Foundation.PWSTR, cue: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextCue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddDataCue(self, start: Double, duration: Double, data: POINTER(Byte), dataSize: UInt32, cue: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextCue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveCue(self, cue: Windows.Win32.Media.MediaFoundation.IMFTimedTextCue_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextFormattedText(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e13af3c1-4d47-4354-b1f5-e83ae0ecae60}')
    @commethod(3)
    def GetText(self, text: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSubformattingCount(self) -> UInt32: ...
    @commethod(5)
    def GetSubformatting(self, index: UInt32, firstChar: POINTER(UInt32), charLength: POINTER(UInt32), style: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextStyle_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df6b87b6-ce12-45db-aba7-432fe054e57d}')
    @commethod(3)
    def TrackAdded(self, trackId: UInt32) -> Void: ...
    @commethod(4)
    def TrackRemoved(self, trackId: UInt32) -> Void: ...
    @commethod(5)
    def TrackSelected(self, trackId: UInt32, selected: Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(6)
    def TrackReadyStateChanged(self, trackId: UInt32) -> Void: ...
    @commethod(7)
    def Error(self, errorCode: Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_ERROR_CODE, extendedErrorCode: Windows.Win32.Foundation.HRESULT, sourceTrackId: UInt32) -> Void: ...
    @commethod(8)
    def Cue(self, cueEvent: Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_CUE_EVENT, currentTime: Double, cue: Windows.Win32.Media.MediaFoundation.IMFTimedTextCue_head) -> Void: ...
    @commethod(9)
    def Reset(self) -> Void: ...
class IMFTimedTextRegion(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8d22afc-bc47-4bdf-9b04-787e49ce3f58}')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPosition(self, pX: POINTER(Double), pY: POINTER(Double), unitType: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_UNIT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetExtent(self, pWidth: POINTER(Double), pHeight: POINTER(Double), unitType: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_UNIT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBackgroundColor(self, bgColor: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetWritingMode(self, writingMode: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_WRITING_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayAlignment(self, displayAlign: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_DISPLAY_ALIGNMENT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLineHeight(self, pLineHeight: POINTER(Double), unitType: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_UNIT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipOverflow(self, clipOverflow: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPadding(self, before: POINTER(Double), start: POINTER(Double), after: POINTER(Double), end: POINTER(Double), unitType: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_UNIT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetWrap(self, wrap: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetZIndex(self, zIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetScrollMode(self, scrollMode: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_SCROLL_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextRuby(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{76c6a6f5-4955-4de5-b27b-14b734cc14b4}')
    @commethod(3)
    def GetRubyText(self, rubyText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRubyPosition(self, value: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_RUBY_POSITION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRubyAlign(self, value: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_RUBY_ALIGN)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRubyReserve(self, value: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_RUBY_RESERVE)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextStyle(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09b2455d-b834-4f01-a347-9052e21c450e}')
    @commethod(3)
    def GetName(self, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsExternal(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(5)
    def GetFontFamily(self, fontFamily: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFontSize(self, fontSize: POINTER(Double), unitType: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_UNIT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetColor(self, color: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBackgroundColor(self, bgColor: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetShowBackgroundAlways(self, showBackgroundAlways: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFontStyle(self, fontStyle: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_FONT_STYLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBold(self, bold: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRightToLeft(self, rightToLeft: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTextAlignment(self, textAlign: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_ALIGNMENT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTextDecoration(self, textDecoration: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTextOutline(self, color: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head), thickness: POINTER(Double), blurRadius: POINTER(Double), unitType: POINTER(Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_UNIT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextStyle2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db639199-c809-4c89-bfca-d0bbb9729d6e}')
    @commethod(3)
    def GetRuby(self, ruby: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextRuby_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBouten(self, bouten: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextBouten_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsTextCombined(self, value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFontAngleInDegrees(self, value: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextTrack(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8822c32d-654e-4233-bf21-d7f2e67d30d4}')
    @commethod(3)
    def GetId(self) -> UInt32: ...
    @commethod(4)
    def GetLabel(self, label: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLabel(self, label: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLanguage(self, language: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTrackKind(self) -> Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_TRACK_KIND: ...
    @commethod(8)
    def IsInBand(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(9)
    def GetInBandMetadataTrackDispatchType(self, dispatchType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsActive(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(11)
    def GetErrorCode(self) -> Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_ERROR_CODE: ...
    @commethod(12)
    def GetExtendedErrorCode(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDataFormat(self, format: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetReadyState(self) -> Windows.Win32.Media.MediaFoundation.MF_TIMED_TEXT_TRACK_READY_STATE: ...
    @commethod(15)
    def GetCueList(self, cues: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextCueList_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimedTextTrackList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23ff334c-442c-445f-bccc-edc438aa11e2}')
    @commethod(3)
    def GetLength(self) -> UInt32: ...
    @commethod(4)
    def GetTrack(self, index: UInt32, track: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextTrack_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTrackById(self, trackId: UInt32, track: POINTER(Windows.Win32.Media.MediaFoundation.IMFTimedTextTrack_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTimer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e56e4cbd-8f70-49d8-a0f8-edb3d6ab9bf2}')
    @commethod(3)
    def SetTimer(self, dwFlags: UInt32, llClockTime: Int64, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, punkState: Windows.Win32.System.Com.IUnknown_head, ppunkKey: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelTimer(self, punkKey: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTopoLoader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de9a6157-f660-4643-b56a-df9f7998c7cd}')
    @commethod(3)
    def Load(self, pInputTopo: Windows.Win32.Media.MediaFoundation.IMFTopology_head, ppOutputTopo: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopology_head), pCurrentTopo: Windows.Win32.Media.MediaFoundation.IMFTopology_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTopology(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{83cf873a-f6da-4bc8-823f-bacfd55dc433}')
    @commethod(33)
    def GetTopologyID(self, pID: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def AddNode(self, pNode: Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def RemoveNode(self, pNode: Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetNodeCount(self, pwNodes: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetNode(self, wIndex: UInt16, ppNode: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def CloneFrom(self, pTopology: Windows.Win32.Media.MediaFoundation.IMFTopology_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetNodeByID(self, qwTopoNodeID: UInt64, ppNode: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetSourceNodeCollection(self, ppCollection: POINTER(Windows.Win32.Media.MediaFoundation.IMFCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetOutputNodeCollection(self, ppCollection: POINTER(Windows.Win32.Media.MediaFoundation.IMFCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTopologyNode(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{83cf873a-f6da-4bc8-823f-bacfd55dc430}')
    @commethod(33)
    def SetObject(self, pObject: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetObject(self, ppObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetNodeType(self, pType: POINTER(Windows.Win32.Media.MediaFoundation.MF_TOPOLOGY_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetTopoNodeID(self, pID: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetTopoNodeID(self, ullTopoID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetInputCount(self, pcInputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetOutputCount(self, pcOutputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def ConnectOutput(self, dwOutputIndex: UInt32, pDownstreamNode: Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head, dwInputIndexOnDownstreamNode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DisconnectOutput(self, dwOutputIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetInput(self, dwInputIndex: UInt32, ppUpstreamNode: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head), pdwOutputIndexOnUpstreamNode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetOutput(self, dwOutputIndex: UInt32, ppDownstreamNode: POINTER(Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head), pdwInputIndexOnDownstreamNode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def SetOutputPrefType(self, dwOutputIndex: UInt32, pType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetOutputPrefType(self, dwOutputIndex: UInt32, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def SetInputPrefType(self, dwInputIndex: UInt32, pType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetInputPrefType(self, dwInputIndex: UInt32, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def CloneFrom(self, pNode: Windows.Win32.Media.MediaFoundation.IMFTopologyNode_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTopologyNodeAttributeEditor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{676aa6dd-238a-410d-bb99-65668d01605a}')
    @commethod(3)
    def UpdateNodeAttributes(self, TopoId: UInt64, cUpdates: UInt32, pUpdates: POINTER(Windows.Win32.Media.MediaFoundation.MFTOPONODE_ATTRIBUTE_UPDATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTopologyServiceLookup(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa993889-4383-415a-a930-dd472a8cf6f7}')
    @commethod(3)
    def LookupService(self, Type: Windows.Win32.Media.MediaFoundation.MF_SERVICE_LOOKUP_TYPE, dwIndex: UInt32, guidService: POINTER(Guid), riid: POINTER(Guid), ppvObjects: POINTER(c_void_p), pnObjects: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTopologyServiceLookupClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa99388a-4383-415a-a930-dd472a8cf6f7}')
    @commethod(3)
    def InitServicePointers(self, pLookup: Windows.Win32.Media.MediaFoundation.IMFTopologyServiceLookup_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseServicePointers(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTrackedSample(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{245bf8e9-0755-40f7-88a5-ae0f18d55e17}')
    @commethod(3)
    def SetAllocator(self, pSampleAllocator: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pUnkState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTranscodeProfile(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4adfdba3-7ab0-4953-a62b-461e7ff3da1e}')
    @commethod(3)
    def SetAudioAttributes(self, pAttrs: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAudioAttributes(self, ppAttrs: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetVideoAttributes(self, pAttrs: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVideoAttributes(self, ppAttrs: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetContainerAttributes(self, pAttrs: Windows.Win32.Media.MediaFoundation.IMFAttributes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetContainerAttributes(self, ppAttrs: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTranscodeSinkInfoProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8cffcd2e-5a03-4a3a-aff7-edcd107c620e}')
    @commethod(3)
    def SetOutputFile(self, pwszFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetOutputByteStream(self, pByteStreamActivate: Windows.Win32.Media.MediaFoundation.IMFActivate_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProfile(self, pProfile: Windows.Win32.Media.MediaFoundation.IMFTranscodeProfile_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSinkInfo(self, pSinkInfo: POINTER(Windows.Win32.Media.MediaFoundation.MF_TRANSCODE_SINK_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTransform(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf94c121-5b05-4e6f-8000-ba598961414d}')
    @commethod(3)
    def GetStreamLimits(self, pdwInputMinimum: POINTER(UInt32), pdwInputMaximum: POINTER(UInt32), pdwOutputMinimum: POINTER(UInt32), pdwOutputMaximum: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamCount(self, pcInputStreams: POINTER(UInt32), pcOutputStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamIDs(self, dwInputIDArraySize: UInt32, pdwInputIDs: POINTER(UInt32), dwOutputIDArraySize: UInt32, pdwOutputIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputStreamInfo(self, dwInputStreamID: UInt32, pStreamInfo: POINTER(Windows.Win32.Media.MediaFoundation.MFT_INPUT_STREAM_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputStreamInfo(self, dwOutputStreamID: UInt32, pStreamInfo: POINTER(Windows.Win32.Media.MediaFoundation.MFT_OUTPUT_STREAM_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAttributes(self, pAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInputStreamAttributes(self, dwInputStreamID: UInt32, pAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOutputStreamAttributes(self, dwOutputStreamID: UInt32, pAttributes: POINTER(Windows.Win32.Media.MediaFoundation.IMFAttributes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteInputStream(self, dwStreamID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddInputStreams(self, cStreams: UInt32, adwStreamIDs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInputAvailableType(self, dwInputStreamID: UInt32, dwTypeIndex: UInt32, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetOutputAvailableType(self, dwOutputStreamID: UInt32, dwTypeIndex: UInt32, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetInputType(self, dwInputStreamID: UInt32, pType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetOutputType(self, dwOutputStreamID: UInt32, pType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetInputCurrentType(self, dwInputStreamID: UInt32, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetOutputCurrentType(self, dwOutputStreamID: UInt32, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetInputStatus(self, dwInputStreamID: UInt32, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetOutputStatus(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetOutputBounds(self, hnsLowerBound: Int64, hnsUpperBound: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ProcessEvent(self, dwInputStreamID: UInt32, pEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ProcessMessage(self, eMessage: Windows.Win32.Media.MediaFoundation.MFT_MESSAGE_TYPE, ulParam: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ProcessInput(self, dwInputStreamID: UInt32, pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ProcessOutput(self, dwFlags: UInt32, cOutputBufferCount: UInt32, pOutputSamples: POINTER(Windows.Win32.Media.MediaFoundation.MFT_OUTPUT_DATA_BUFFER_head), pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTrustedInput(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{542612c4-a1b8-4632-b521-de11ea64a0b0}')
    @commethod(3)
    def GetInputTrustAuthority(self, dwStreamID: UInt32, riid: POINTER(Guid), ppunkObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFTrustedOutput(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d19f8e95-b126-4446-890c-5dcb7ad71453}')
    @commethod(3)
    def GetOutputTrustAuthorityCount(self, pcOutputTrustAuthorities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputTrustAuthorityByIndex(self, dwIndex: UInt32, ppauthority: POINTER(Windows.Win32.Media.MediaFoundation.IMFOutputTrustAuthority_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsFinal(self, pfIsFinal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoCaptureSampleAllocator(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFVideoSampleAllocator
    _iid_ = Guid('{725b77c7-ca9f-4fe5-9d72-9946bf9b3c70}')
    @commethod(7)
    def InitializeCaptureSampleAllocator(self, cbSampleSize: UInt32, cbCaptureMetadataSize: UInt32, cbAlignment: UInt32, cMinimumSamples: UInt32, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoDeviceID(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a38d9567-5a9c-4f3c-b293-8eb415b279ba}')
    @commethod(3)
    def GetDeviceID(self, pDeviceID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoDisplayControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a490b1e4-ab84-4d31-a1b2-181e03b1077a}')
    @commethod(3)
    def GetNativeVideoSize(self, pszVideo: POINTER(Windows.Win32.Foundation.SIZE_head), pszARVideo: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIdealVideoSize(self, pszMin: POINTER(Windows.Win32.Foundation.SIZE_head), pszMax: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetVideoPosition(self, pnrcSource: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head), prcDest: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVideoPosition(self, pnrcSource: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head), prcDest: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAspectRatioMode(self, dwAspectRatioMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAspectRatioMode(self, pdwAspectRatioMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetVideoWindow(self, hwndVideo: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetVideoWindow(self, phwndVideo: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RepaintVideo(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCurrentImage(self, pBih: POINTER(Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER_head), pDib: POINTER(POINTER(Byte)), pcbDib: POINTER(UInt32), pTimeStamp: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetBorderColor(self, Clr: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetBorderColor(self, pClr: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetRenderingPrefs(self, dwRenderFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRenderingPrefs(self, pdwRenderFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetFullscreen(self, fFullscreen: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFullscreen(self, pfFullscreen: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoMediaType(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFMediaType
    _iid_ = Guid('{b99f381f-a8f9-47a2-a5af-ca3a225a3890}')
    @commethod(38)
    def GetVideoFormat(self) -> POINTER(Windows.Win32.Media.MediaFoundation.MFVIDEOFORMAT_head): ...
    @commethod(39)
    def GetVideoRepresentation(self, guidRepresentation: Guid, ppvRepresentation: POINTER(c_void_p), lStride: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoMixerBitmap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{814c7b20-0fdb-4eec-af8f-f957c8f69edc}')
    @commethod(3)
    def SetAlphaBitmap(self, pBmpParms: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoAlphaBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ClearAlphaBitmap(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateAlphaBitmapParameters(self, pBmpParms: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoAlphaBitmapParams_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAlphaBitmapParameters(self, pBmpParms: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoAlphaBitmapParams_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoMixerControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5c6c53f-c202-4aa5-9695-175ba8c508a5}')
    @commethod(3)
    def SetStreamZOrder(self, dwStreamID: UInt32, dwZ: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStreamZOrder(self, dwStreamID: UInt32, pdwZ: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStreamOutputRect(self, dwStreamID: UInt32, pnrcOutput: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStreamOutputRect(self, dwStreamID: UInt32, pnrcOutput: POINTER(Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoMixerControl2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFVideoMixerControl
    _iid_ = Guid('{8459616d-966e-4930-b658-54fa7e5a16d3}')
    @commethod(7)
    def SetMixingPrefs(self, dwMixFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMixingPrefs(self, pdwMixFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoPositionMapper(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f6a9f17-e70b-4e24-8ae4-0b2c3ba7a4ae}')
    @commethod(3)
    def MapOutputCoordinateToInputStream(self, xOut: Single, yOut: Single, dwOutputStreamIndex: UInt32, dwInputStreamIndex: UInt32, pxIn: POINTER(Single), pyIn: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoPresenter(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFClockStateSink
    _iid_ = Guid('{29aff080-182a-4a5d-af3b-448f3a6346cb}')
    @commethod(8)
    def ProcessMessage(self, eMessage: Windows.Win32.Media.MediaFoundation.MFVP_MESSAGE_TYPE, ulParam: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentMediaType(self, ppMediaType: POINTER(Windows.Win32.Media.MediaFoundation.IMFVideoMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoProcessor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ab0000c-fece-4d1f-a2ac-a9573530656e}')
    @commethod(3)
    def GetAvailableVideoProcessorModes(self, lpdwNumProcessingModes: POINTER(UInt32), ppVideoProcessingModes: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVideoProcessorCaps(self, lpVideoProcessorMode: POINTER(Guid), lpVideoProcessorCaps: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_VideoProcessorCaps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVideoProcessorMode(self, lpMode: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetVideoProcessorMode(self, lpMode: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProcAmpRange(self, dwProperty: UInt32, pPropRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProcAmpValues(self, dwFlags: UInt32, Values: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ProcAmpValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetProcAmpValues(self, dwFlags: UInt32, pValues: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ProcAmpValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilteringRange(self, dwProperty: UInt32, pPropRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_ValueRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFilteringValue(self, dwProperty: UInt32, pValue: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetFilteringValue(self, dwProperty: UInt32, pValue: POINTER(Windows.Win32.Media.MediaFoundation.DXVA2_Fixed32_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetBackgroundColor(self, lpClrBkg: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetBackgroundColor(self, ClrBkg: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoProcessorControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3f675d5-6119-4f7f-a100-1d8b280f0efb}')
    @commethod(3)
    def SetBorderColor(self, pBorderColor: POINTER(Windows.Win32.Media.MediaFoundation.MFARGB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSourceRectangle(self, pSrcRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDestinationRectangle(self, pDstRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMirror(self, eMirror: Windows.Win32.Media.MediaFoundation.MF_VIDEO_PROCESSOR_MIRROR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetRotation(self, eRotation: Windows.Win32.Media.MediaFoundation.MF_VIDEO_PROCESSOR_ROTATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetConstrictionSize(self, pConstrictionSize: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoProcessorControl2(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFVideoProcessorControl
    _iid_ = Guid('{bde633d3-e1dc-4a7f-a693-bbae399c4a20}')
    @commethod(9)
    def SetRotationOverride(self, uiRotation: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnableHardwareEffects(self, fEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSupportedHardwareEffects(self, puiSupport: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoProcessorControl3(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFVideoProcessorControl2
    _iid_ = Guid('{2424b3f2-eb23-40f1-91aa-74bddeea0883}')
    @commethod(12)
    def GetNaturalOutputType(self, ppType: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaType_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableSphericalVideoProcessing(self, fEnable: Windows.Win32.Foundation.BOOL, eFormat: Windows.Win32.Media.MediaFoundation.MFVideoSphericalFormat, eProjectionMode: Windows.Win32.Media.MediaFoundation.MFVideoSphericalProjectionMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSphericalVideoProperties(self, X: Single, Y: Single, Z: Single, W: Single, fieldOfView: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetOutputDevice(self, pOutputDevice: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoRenderer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfdfd197-a9ca-43d8-b341-6af3503792cd}')
    @commethod(3)
    def InitializeRenderer(self, pVideoMixer: Windows.Win32.Media.MediaFoundation.IMFTransform_head, pVideoPresenter: Windows.Win32.Media.MediaFoundation.IMFVideoPresenter_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoRendererEffectControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{604d33d7-cf23-41d5-8224-5bbbb1a87475}')
    @commethod(3)
    def OnAppServiceConnectionEstablished(self, pAppServiceConnection: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoSampleAllocator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86cbc910-e533-4751-8e3b-f19b5b806a03}')
    @commethod(3)
    def SetDirectXManager(self, pManager: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UninitializeSampleAllocator(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeSampleAllocator(self, cRequestedFrames: UInt32, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateSample(self, ppSample: POINTER(Windows.Win32.Media.MediaFoundation.IMFSample_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoSampleAllocatorCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{992388b4-3372-4f67-8b6f-c84c071f4751}')
    @commethod(3)
    def SetCallback(self, pNotify: Windows.Win32.Media.MediaFoundation.IMFVideoSampleAllocatorNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFreeSampleCount(self, plSamples: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoSampleAllocatorEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFVideoSampleAllocator
    _iid_ = Guid('{545b3a48-3283-4f62-866f-a62d8f598f9f}')
    @commethod(7)
    def InitializeSampleAllocatorEx(self, cInitialSamples: UInt32, cMaximumSamples: UInt32, pAttributes: Windows.Win32.Media.MediaFoundation.IMFAttributes_head, pMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoSampleAllocatorNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a792cdbe-c374-4e89-8335-278e7b9956a4}')
    @commethod(3)
    def NotifyRelease(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVideoSampleAllocatorNotifyEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFVideoSampleAllocatorNotify
    _iid_ = Guid('{3978aa1a-6d5b-4b7f-a340-90899189ae34}')
    @commethod(4)
    def NotifyPrune(self, __MIDL__IMFVideoSampleAllocatorNotifyEx0000: Windows.Win32.Media.MediaFoundation.IMFSample_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMFVirtualCamera(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAttributes
    _iid_ = Guid('{1c08a864-ef6c-4c75-af59-5f2d68da9563}')
    @commethod(33)
    def AddDeviceSourceInfo(self, DeviceSourceInfo: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def AddProperty(self, pKey: POINTER(Windows.Win32.Devices.Properties.DEVPROPKEY_head), Type: Windows.Win32.Devices.Properties.DEVPROPTYPE, pbData: POINTER(Byte), cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def AddRegistryEntry(self, EntryName: Windows.Win32.Foundation.PWSTR, SubkeyPath: Windows.Win32.Foundation.PWSTR, dwRegType: UInt32, pbData: POINTER(Byte), cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Start(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def Remove(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetMediaSource(self, ppMediaSource: POINTER(Windows.Win32.Media.MediaFoundation.IMFMediaSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SendCameraProperty(self, propertySet: POINTER(Guid), propertyId: UInt32, propertyFlags: UInt32, propertyPayload: c_void_p, propertyPayloadLength: UInt32, data: c_void_p, dataLength: UInt32, dataWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def CreateSyncEvent(self, kseventSet: POINTER(Guid), kseventId: UInt32, kseventFlags: UInt32, eventHandle: Windows.Win32.Foundation.HANDLE, cameraSyncObject: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraSyncObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def CreateSyncSemaphore(self, kseventSet: POINTER(Guid), kseventId: UInt32, kseventFlags: UInt32, semaphoreHandle: Windows.Win32.Foundation.HANDLE, semaphoreAdjustment: Int32, cameraSyncObject: POINTER(Windows.Win32.Media.MediaFoundation.IMFCameraSyncObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def Shutdown(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMFWorkQueueServices(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{35fe1bb8-a3a9-40fe-bbec-eb569c9ccca3}')
    @commethod(3)
    def BeginRegisterTopologyWorkQueuesWithMMCSS(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndRegisterTopologyWorkQueuesWithMMCSS(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginUnregisterTopologyWorkQueuesWithMMCSS(self, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndUnregisterTopologyWorkQueuesWithMMCSS(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTopologyWorkQueueMMCSSClass(self, dwTopologyWorkQueueId: UInt32, pwszClass: Windows.Win32.Foundation.PWSTR, pcchClass: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTopologyWorkQueueMMCSSTaskId(self, dwTopologyWorkQueueId: UInt32, pdwTaskId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BeginRegisterPlatformWorkQueueWithMMCSS(self, dwPlatformWorkQueue: UInt32, wszClass: Windows.Win32.Foundation.PWSTR, dwTaskId: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndRegisterPlatformWorkQueueWithMMCSS(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head, pdwTaskId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def BeginUnregisterPlatformWorkQueueWithMMCSS(self, dwPlatformWorkQueue: UInt32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndUnregisterPlatformWorkQueueWithMMCSS(self, pResult: Windows.Win32.Media.MediaFoundation.IMFAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPlaftormWorkQueueMMCSSClass(self, dwPlatformWorkQueueId: UInt32, pwszClass: Windows.Win32.Foundation.PWSTR, pcchClass: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetPlatformWorkQueueMMCSSTaskId(self, dwPlatformWorkQueueId: UInt32, pdwTaskId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMFWorkQueueServicesEx(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFWorkQueueServices
    _iid_ = Guid('{96bf961b-40fe-42f1-ba9d-320238b49700}')
    @commethod(15)
    def GetTopologyWorkQueueMMCSSPriority(self, dwTopologyWorkQueueId: UInt32, plPriority: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def BeginRegisterPlatformWorkQueueWithMMCSSEx(self, dwPlatformWorkQueue: UInt32, wszClass: Windows.Win32.Foundation.PWSTR, dwTaskId: UInt32, lPriority: Int32, pCallback: Windows.Win32.Media.MediaFoundation.IMFAsyncCallback_head, pState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetPlatformWorkQueueMMCSSPriority(self, dwPlatformWorkQueueId: UInt32, plPriority: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOPMVideoOutput(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0a15159d-41c7-4456-93e1-284cd61d4e8d}')
    @commethod(3)
    def StartInitialization(self, prnRandomNumber: POINTER(Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER_head), ppbCertificate: POINTER(POINTER(Byte)), pulCertificateLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FinishInitialization(self, pParameters: POINTER(Windows.Win32.Media.MediaFoundation.OPM_ENCRYPTED_INITIALIZATION_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInformation(self, pParameters: POINTER(Windows.Win32.Media.MediaFoundation.OPM_GET_INFO_PARAMETERS_head), pRequestedInformation: POINTER(Windows.Win32.Media.MediaFoundation.OPM_REQUESTED_INFORMATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def COPPCompatibleGetInformation(self, pParameters: POINTER(Windows.Win32.Media.MediaFoundation.OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS_head), pRequestedInformation: POINTER(Windows.Win32.Media.MediaFoundation.OPM_REQUESTED_INFORMATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Configure(self, pParameters: POINTER(Windows.Win32.Media.MediaFoundation.OPM_CONFIGURE_PARAMETERS_head), ulAdditionalParametersSize: UInt32, pbAdditionalParameters: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IPlayToControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{607574eb-f4b6-45c1-b08c-cb715122901d}')
    @commethod(3)
    def Connect(self, pFactory: Windows.Win32.Media.MediaFoundation.IMFSharingEngineClassFactory_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPlayToControlWithCapabilities(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IPlayToControl
    _iid_ = Guid('{aa9dd80f-c50a-4220-91c1-332287f82a34}')
    @commethod(5)
    def GetCapabilities(self, pCapabilities: POINTER(Windows.Win32.Media.MediaFoundation.PLAYTO_SOURCE_CREATEFLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
class IPlayToSourceClassFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{842b32a3-9b9b-4d1c-b3f3-49193248a554}')
    @commethod(3)
    def CreateInstance(self, dwFlags: UInt32, pControl: Windows.Win32.Media.MediaFoundation.IPlayToControl_head, ppSource: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IToc(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6f05441-a919-423b-91a0-89d5b4a8ab77}')
    @commethod(3)
    def SetDescriptor(self, pDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.TOC_DESCRIPTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescriptor(self, pDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.TOC_DESCRIPTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDescription(self, pwszDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(self, pwDescriptionSize: POINTER(UInt16), pwszDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetContext(self, dwContextSize: UInt32, pbtContext: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetContext(self, pdwContextSize: POINTER(UInt32), pbtContext: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEntryListCount(self, pwCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEntryListByIndex(self, wEntryListIndex: UInt16, ppEntryList: POINTER(Windows.Win32.Media.MediaFoundation.ITocEntryList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddEntryList(self, pEntryList: Windows.Win32.Media.MediaFoundation.ITocEntryList_head, pwEntryListIndex: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddEntryListByIndex(self, wEntryListIndex: UInt16, pEntryList: Windows.Win32.Media.MediaFoundation.ITocEntryList_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RemoveEntryListByIndex(self, wEntryListIndex: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class ITocCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23fee831-ae96-42df-b170-25a04847a3ca}')
    @commethod(3)
    def GetEntryCount(self, pdwEntryCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEntryByIndex(self, dwEntryIndex: UInt32, ppToc: POINTER(Windows.Win32.Media.MediaFoundation.IToc_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddEntry(self, pToc: Windows.Win32.Media.MediaFoundation.IToc_head, pdwEntryIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddEntryByIndex(self, dwEntryIndex: UInt32, pToc: Windows.Win32.Media.MediaFoundation.IToc_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveEntryByIndex(self, dwEntryIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITocEntry(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f22f5e06-585c-4def-8523-6555cfbc0cb3}')
    @commethod(3)
    def SetTitle(self, pwszTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTitle(self, pwTitleSize: POINTER(UInt16), pwszTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDescriptor(self, pDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.TOC_ENTRY_DESCRIPTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescriptor(self, pDescriptor: POINTER(Windows.Win32.Media.MediaFoundation.TOC_ENTRY_DESCRIPTOR_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSubEntries(self, dwNumSubEntries: UInt32, pwSubEntryIndices: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSubEntries(self, pdwNumSubEntries: POINTER(UInt32), pwSubEntryIndices: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetDescriptionData(self, dwDescriptionDataSize: UInt32, pbtDescriptionData: POINTER(Byte), pguidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDescriptionData(self, pdwDescriptionDataSize: POINTER(UInt32), pbtDescriptionData: POINTER(Byte), pGuidType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class ITocEntryList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a8cccbd-0efd-43a3-b838-f38a552ba237}')
    @commethod(3)
    def GetEntryCount(self, pdwEntryCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEntryByIndex(self, dwEntryIndex: UInt32, ppEntry: POINTER(Windows.Win32.Media.MediaFoundation.ITocEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddEntry(self, pEntry: Windows.Win32.Media.MediaFoundation.ITocEntry_head, pdwEntryIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddEntryByIndex(self, dwEntryIndex: UInt32, pEntry: Windows.Win32.Media.MediaFoundation.ITocEntry_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveEntryByIndex(self, dwEntryIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITocParser(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ecfb9a55-9298-4f49-887f-0b36206599d2}')
    @commethod(3)
    def Init(self, pwszFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTocCount(self, enumTocPosType: Windows.Win32.Media.MediaFoundation.TOC_POS_TYPE, pdwTocCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTocByIndex(self, enumTocPosType: Windows.Win32.Media.MediaFoundation.TOC_POS_TYPE, dwTocIndex: UInt32, ppToc: POINTER(Windows.Win32.Media.MediaFoundation.IToc_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTocByType(self, enumTocPosType: Windows.Win32.Media.MediaFoundation.TOC_POS_TYPE, guidTocType: Guid, ppTocs: POINTER(Windows.Win32.Media.MediaFoundation.ITocCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddToc(self, enumTocPosType: Windows.Win32.Media.MediaFoundation.TOC_POS_TYPE, pToc: Windows.Win32.Media.MediaFoundation.IToc_head, pdwTocIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveTocByIndex(self, enumTocPosType: Windows.Win32.Media.MediaFoundation.TOC_POS_TYPE, dwTocIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveTocByType(self, enumTocPosType: Windows.Win32.Media.MediaFoundation.TOC_POS_TYPE, guidTocType: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
class IValidateBinding(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04a578b2-e778-422a-a805-b3ee54d90bd9}')
    @commethod(3)
    def GetIdentifier(self, guidLicensorID: Guid, pbEphemeron: POINTER(Byte), cbEphemeron: UInt32, ppbBlobValidationID: POINTER(POINTER(Byte)), pcbBlobSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecLeakyBucket(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a81ba647-6227-43b7-b231-c7b15135dd7d}')
    @commethod(3)
    def SetBufferSizeBits(self, ulBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBufferSizeBits(self, pulBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetBufferFullnessBits(self, ulBufferFullness: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBufferFullnessBits(self, pulBufferFullness: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecOutputTimestamp(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b72adf95-7adc-4a72-bc05-577d8ea6bf68}')
    @commethod(3)
    def GetNextOutputTime(self, prtTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecPrivateData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73f0be8e-57f7-4f01-aa66-9f57340cfe0e}')
    @commethod(3)
    def SetPartialOutputType(self, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrivateData(self, pbData: POINTER(Byte), pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2573e11a-f01a-4fdd-a98d-63b8e0ba9589}')
    @commethod(3)
    def GetFormatProp(self, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.MediaFoundation.WMT_PROP_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCodecProp(self, dwFormat: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.MediaFoundation.WMT_PROP_DATATYPE), pValue: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMCodecStrings(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7b2504b-e58a-47fb-958b-cac7165a057d}')
    @commethod(3)
    def GetName(self, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), cchLength: UInt32, szName: Windows.Win32.Foundation.PWSTR, pcchLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), cchLength: UInt32, szDescription: Windows.Win32.Foundation.PWSTR, pcchLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMColorConvProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e6a49e22-c099-421d-aad3-c061fb4ae85b}')
    @commethod(3)
    def SetMode(self, lMode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFullCroppingParam(self, lSrcCropLeft: Int32, lSrcCropTop: Int32, lDstCropLeft: Int32, lDstCropTop: Int32, lCropWidth: Int32, lCropHeight: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMColorLegalizerProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{776c93b3-b72d-4508-b6d0-208785f553e7}')
    @commethod(3)
    def SetColorLegalizerQuality(self, lquality: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMFrameInterpProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4c06bb9b-626c-4614-8329-cc6a21b93fa0}')
    @commethod(3)
    def SetFrameRateIn(self, lFrameRate: Int32, lScale: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFrameRateOut(self, lFrameRate: Int32, lScale: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFrameInterpEnabled(self, bFIEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetComplexityLevel(self, iComplexity: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMInterlaceProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7b12e5d1-bd22-48ea-bc06-98e893221c89}')
    @commethod(3)
    def SetProcessType(self, iProcessType: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetInitInverseTeleCinePattern(self, iInitPattern: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLastFrame(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMResamplerProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7e9984f-f09f-4da4-903f-6e2e0efe56b5}')
    @commethod(3)
    def SetHalfFilterLength(self, lhalfFilterLen: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetUserChannelMtx(self, userChannelMtx: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMResizerProps(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{57665d4c-0414-4faa-905b-10e546f81c33}')
    @commethod(3)
    def SetResizerQuality(self, lquality: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetInterlaceMode(self, lmode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetClipRegion(self, lClipOriXSrc: Int32, lClipOriYSrc: Int32, lClipWidthSrc: Int32, lClipHeightSrc: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFullCropRegion(self, lClipOriXSrc: Int32, lClipOriYSrc: Int32, lClipWidthSrc: Int32, lClipHeightSrc: Int32, lClipOriXDst: Int32, lClipOriYDst: Int32, lClipWidthDst: Int32, lClipHeightDst: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFullCropRegion(self, lClipOriXSrc: POINTER(Int32), lClipOriYSrc: POINTER(Int32), lClipWidthSrc: POINTER(Int32), lClipHeightSrc: POINTER(Int32), lClipOriXDst: POINTER(Int32), lClipOriYDst: POINTER(Int32), lClipWidthDst: POINTER(Int32), lClipHeightDst: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMSampleExtensionSupport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9bca9884-0604-4c2a-87da-793ff4d586c3}')
    @commethod(3)
    def SetUseSampleExtensions(self, fUseExtensions: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWMValidate(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cee3def2-3808-414d-be66-fafd472210bc}')
    @commethod(3)
    def SetIdentifier(self, guidValidationID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
class IWMVideoDecoderHurryup(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{352bb3bd-2d4d-4323-9e71-dcdcfbd53ca6}')
    @commethod(3)
    def SetHurryup(self, lHurryup: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHurryup(self, plHurryup: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMVideoDecoderReconBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45bda2ac-88e2-4923-98ba-3949080711a3}')
    @commethod(3)
    def GetReconstructedVideoFrameSize(self, pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReconstructedVideoFrame(self, pBuf: Windows.Win32.Media.DxMediaObjects.IMediaBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetReconstructedVideoFrame(self, pBuf: Windows.Win32.Media.DxMediaObjects.IMediaBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWMVideoForceKeyFrame(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f8496be-5b9a-41b9-a9e8-f21cd80596c2}')
    @commethod(3)
    def SetKeyFrame(self) -> Windows.Win32.Foundation.HRESULT: ...
KSMETHOD_OPMVIDEOOUTPUT = Int32
KSMETHOD_OPMVIDEOOUTPUT_STARTINITIALIZATION: KSMETHOD_OPMVIDEOOUTPUT = 0
KSMETHOD_OPMVIDEOOUTPUT_FINISHINITIALIZATION: KSMETHOD_OPMVIDEOOUTPUT = 1
KSMETHOD_OPMVIDEOOUTPUT_GETINFORMATION: KSMETHOD_OPMVIDEOOUTPUT = 2
KSPROPSETID_OPMVideoOutput = Guid('{06f414bb-f43a-4fe2-a566-774b4c81f0db}')
class MACROBLOCK_DATA(EasyCastStructure):
    flags: UInt32
    motionVectorX: Int16
    motionVectorY: Int16
    QPDelta: Int32
MEDIA_EVENT_GENERATOR_GET_EVENT_FLAGS = UInt32
MF_EVENT_FLAG_NONE: MEDIA_EVENT_GENERATOR_GET_EVENT_FLAGS = 0
MF_EVENT_FLAG_NO_WAIT: MEDIA_EVENT_GENERATOR_GET_EVENT_FLAGS = 1
MF2DBuffer_LockFlags = Int32
MF2DBuffer_LockFlags_LockTypeMask: MF2DBuffer_LockFlags = 3
MF2DBuffer_LockFlags_Read: MF2DBuffer_LockFlags = 1
MF2DBuffer_LockFlags_Write: MF2DBuffer_LockFlags = 2
MF2DBuffer_LockFlags_ReadWrite: MF2DBuffer_LockFlags = 3
MF2DBuffer_LockFlags_ForceDWORD: MF2DBuffer_LockFlags = 2147483647
MF3DVideoOutputType = Int32
MF3DVideoOutputType_BaseView: MF3DVideoOutputType = 0
MF3DVideoOutputType_Stereo: MF3DVideoOutputType = 1
MFAMRNBByteStreamHandler = Guid('{efe6208a-0a2c-49fa-8a01-3768b559b6da}')
MFAMRNBSinkClassFactory = Guid('{b0271158-70d2-4c5b-9f94-76f549d90fdf}')
class MFARGB(EasyCastStructure):
    rgbBlue: Byte
    rgbGreen: Byte
    rgbRed: Byte
    rgbAlpha: Byte
MFASF_INDEXER_FLAGS = Int32
MFASF_INDEXER_WRITE_NEW_INDEX: MFASF_INDEXER_FLAGS = 1
MFASF_INDEXER_READ_FOR_REVERSEPLAYBACK: MFASF_INDEXER_FLAGS = 2
MFASF_INDEXER_WRITE_FOR_LIVEREAD: MFASF_INDEXER_FLAGS = 4
MFASF_MULTIPLEXERFLAGS = Int32
MFASF_MULTIPLEXER_AUTOADJUST_BITRATE: MFASF_MULTIPLEXERFLAGS = 1
MFASF_SPLITTERFLAGS = Int32
MFASF_SPLITTER_REVERSE: MFASF_SPLITTERFLAGS = 1
MFASF_SPLITTER_WMDRM: MFASF_SPLITTERFLAGS = 2
MFASF_STREAMSELECTOR_FLAGS = Int32
MFASF_STREAMSELECTOR_DISABLE_THINNING: MFASF_STREAMSELECTOR_FLAGS = 1
MFASF_STREAMSELECTOR_USE_AVERAGE_BITRATE: MFASF_STREAMSELECTOR_FLAGS = 2
class MFASYNCRESULT(ComPtr):
    extends: Windows.Win32.Media.MediaFoundation.IMFAsyncResult
MFASYNC_WORKQUEUE_TYPE = Int32
MF_STANDARD_WORKQUEUE: MFASYNC_WORKQUEUE_TYPE = 0
MF_WINDOW_WORKQUEUE: MFASYNC_WORKQUEUE_TYPE = 1
MF_MULTITHREADED_WORKQUEUE: MFASYNC_WORKQUEUE_TYPE = 2
class MFAYUVSample(EasyCastStructure):
    bCrValue: Byte
    bCbValue: Byte
    bYValue: Byte
    bSampleAlpha8: Byte
MFAudioConstriction = Int32
MFAudioConstriction_MFaudioConstrictionOff: MFAudioConstriction = 0
MFAudioConstriction_MFaudioConstriction48_16: MFAudioConstriction = 1
MFAudioConstriction_MFaudioConstriction44_16: MFAudioConstriction = 2
MFAudioConstriction_MFaudioConstriction14_14: MFAudioConstriction = 3
MFAudioConstriction_MFaudioConstrictionMute: MFAudioConstriction = 4
class MFAudioDecoderDegradationInfo(EasyCastStructure):
    eDegradationReason: Windows.Win32.Media.MediaFoundation.MFT_AUDIO_DECODER_DEGRADATION_REASON
    eType: Windows.Win32.Media.MediaFoundation.MFT_AUDIO_DECODER_DEGRADATION_TYPE
class MFBYTESTREAM_BUFFERING_PARAMS(EasyCastStructure):
    cbTotalFileSize: UInt64
    cbPlayableDataSize: UInt64
    prgBuckets: POINTER(Windows.Win32.Media.MediaFoundation.MF_LEAKY_BUCKET_PAIR_head)
    cBuckets: UInt32
    qwNetBufferingTime: UInt64
    qwExtraBufferingTimeDuringSeek: UInt64
    qwPlayDuration: UInt64
    dRate: Single
MFBYTESTREAM_SEEK_ORIGIN = Int32
MFBYTESTREAM_SEEK_ORIGIN_msoBegin: MFBYTESTREAM_SEEK_ORIGIN = 0
MFBYTESTREAM_SEEK_ORIGIN_msoCurrent: MFBYTESTREAM_SEEK_ORIGIN = 1
MFCLOCK_CHARACTERISTICS_FLAGS = Int32
MFCLOCK_CHARACTERISTICS_FLAG_FREQUENCY_10MHZ: MFCLOCK_CHARACTERISTICS_FLAGS = 2
MFCLOCK_CHARACTERISTICS_FLAG_ALWAYS_RUNNING: MFCLOCK_CHARACTERISTICS_FLAGS = 4
MFCLOCK_CHARACTERISTICS_FLAG_IS_SYSTEM_CLOCK: MFCLOCK_CHARACTERISTICS_FLAGS = 8
class MFCLOCK_PROPERTIES(EasyCastStructure):
    qwCorrelationRate: UInt64
    guidClockId: Guid
    dwClockFlags: UInt32
    qwClockFrequency: UInt64
    dwClockTolerance: UInt32
    dwClockJitter: UInt32
MFCLOCK_RELATIONAL_FLAGS = Int32
MFCLOCK_RELATIONAL_FLAG_JITTER_NEVER_AHEAD: MFCLOCK_RELATIONAL_FLAGS = 1
MFCLOCK_STATE = Int32
MFCLOCK_STATE_INVALID: MFCLOCK_STATE = 0
MFCLOCK_STATE_RUNNING: MFCLOCK_STATE = 1
MFCLOCK_STATE_STOPPED: MFCLOCK_STATE = 2
MFCLOCK_STATE_PAUSED: MFCLOCK_STATE = 3
class MFCONTENTPROTECTIONDEVICE_INPUT_DATA(EasyCastStructure):
    HWProtectionFunctionID: UInt32
    PrivateDataByteCount: UInt32
    HWProtectionDataByteCount: UInt32
    Reserved: UInt32
    InputData: Byte * 4
class MFCONTENTPROTECTIONDEVICE_OUTPUT_DATA(EasyCastStructure):
    PrivateDataByteCount: UInt32
    MaxHWProtectionDataByteCount: UInt32
    HWProtectionDataByteCount: UInt32
    Status: Windows.Win32.Foundation.HRESULT
    TransportTimeInHundredsOfNanoseconds: Int64
    ExecutionTimeInHundredsOfNanoseconds: Int64
    OutputData: Byte * 4
class MFCONTENTPROTECTIONDEVICE_REALTIMECLIENT_DATA(EasyCastStructure):
    TaskIndex: UInt32
    ClassName: Char * 260
    BasePriority: Int32
class MFCameraExtrinsic_CalibratedTransform(EasyCastStructure):
    CalibrationId: Guid
    Position: Windows.Win32.Media.MediaFoundation.MF_FLOAT3
    Orientation: Windows.Win32.Media.MediaFoundation.MF_QUATERNION
class MFCameraExtrinsics(EasyCastStructure):
    TransformCount: UInt32
    CalibratedTransforms: Windows.Win32.Media.MediaFoundation.MFCameraExtrinsic_CalibratedTransform * 1
class MFCameraIntrinsic_CameraModel(EasyCastStructure):
    FocalLength_x: Single
    FocalLength_y: Single
    PrincipalPoint_x: Single
    PrincipalPoint_y: Single
class MFCameraIntrinsic_DistortionModel(EasyCastStructure):
    Radial_k1: Single
    Radial_k2: Single
    Radial_k3: Single
    Tangential_p1: Single
    Tangential_p2: Single
class MFCameraIntrinsic_DistortionModel6KT(EasyCastStructure):
    Radial_k1: Single
    Radial_k2: Single
    Radial_k3: Single
    Radial_k4: Single
    Radial_k5: Single
    Radial_k6: Single
    Tangential_p1: Single
    Tangential_p2: Single
class MFCameraIntrinsic_DistortionModelArcTan(EasyCastStructure):
    Radial_k0: Single
    DistortionCenter_x: Single
    DistortionCenter_y: Single
    Tangential_x: Single
    Tangential_y: Single
MFCameraIntrinsic_DistortionModelType = Int32
MFCameraIntrinsic_DistortionModelType_6KT: MFCameraIntrinsic_DistortionModelType = 0
MFCameraIntrinsic_DistortionModelType_ArcTan: MFCameraIntrinsic_DistortionModelType = 1
class MFCameraIntrinsic_PinholeCameraModel(EasyCastStructure):
    FocalLength: Windows.Win32.Media.MediaFoundation.MF_FLOAT2
    PrincipalPoint: Windows.Win32.Media.MediaFoundation.MF_FLOAT2
MFCameraOcclusionState = Int32
MFCameraOcclusionState_Open: MFCameraOcclusionState = 0
MFCameraOcclusionState_OccludedByLid: MFCameraOcclusionState = 1
MFCameraOcclusionState_OccludedByCameraHardware: MFCameraOcclusionState = 2
MFDepthMeasurement = Int32
MFDepthMeasurement_DistanceToFocalPlane: MFDepthMeasurement = 0
MFDepthMeasurement_DistanceToOpticalCenter: MFDepthMeasurement = 1
class MFExtendedCameraIntrinsic_IntrinsicModel(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    SplitFrameId: UInt32
    CameraModel: Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_CameraModel
MFFLACBytestreamHandler = Guid('{0e41cfb8-0506-40f4-a516-77cc23642d91}')
MFFLACSinkClassFactory = Guid('{7d39c56f-6075-47c9-9bae-8cf9e531b5f5}')
class MFFOLDDOWN_MATRIX(EasyCastStructure):
    cbSize: UInt32
    cSrcChannels: UInt32
    cDstChannels: UInt32
    dwChannelMask: UInt32
    Coeff: Int32 * 64
MFFrameSourceTypes = Int32
MFFrameSourceTypes_Color: MFFrameSourceTypes = 1
MFFrameSourceTypes_Infrared: MFFrameSourceTypes = 2
MFFrameSourceTypes_Depth: MFFrameSourceTypes = 4
MFFrameSourceTypes_Image: MFFrameSourceTypes = 8
MFFrameSourceTypes_Custom: MFFrameSourceTypes = 128
class MFINPUTTRUSTAUTHORITY_ACCESS_ACTION(EasyCastStructure):
    Action: Windows.Win32.Media.MediaFoundation.MFPOLICYMANAGER_ACTION
    pbTicket: POINTER(Byte)
    cbTicket: UInt32
class MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS(EasyCastStructure):
    dwSize: UInt32
    dwVer: UInt32
    cbSignatureOffset: UInt32
    cbSignatureSize: UInt32
    cbExtensionOffset: UInt32
    cbExtensionSize: UInt32
    cActions: UInt32
    rgOutputActions: Windows.Win32.Media.MediaFoundation.MFINPUTTRUSTAUTHORITY_ACCESS_ACTION * 1
MFMEDIASOURCE_CHARACTERISTICS = Int32
MFMEDIASOURCE_IS_LIVE: MFMEDIASOURCE_CHARACTERISTICS = 1
MFMEDIASOURCE_CAN_SEEK: MFMEDIASOURCE_CHARACTERISTICS = 2
MFMEDIASOURCE_CAN_PAUSE: MFMEDIASOURCE_CHARACTERISTICS = 4
MFMEDIASOURCE_HAS_SLOW_SEEK: MFMEDIASOURCE_CHARACTERISTICS = 8
MFMEDIASOURCE_HAS_MULTIPLE_PRESENTATIONS: MFMEDIASOURCE_CHARACTERISTICS = 16
MFMEDIASOURCE_CAN_SKIPFORWARD: MFMEDIASOURCE_CHARACTERISTICS = 32
MFMEDIASOURCE_CAN_SKIPBACKWARD: MFMEDIASOURCE_CHARACTERISTICS = 64
MFMEDIASOURCE_DOES_NOT_USE_NETWORK: MFMEDIASOURCE_CHARACTERISTICS = 128
class MFMPEG2DLNASINKSTATS(EasyCastStructure):
    cBytesWritten: UInt64
    fPAL: Windows.Win32.Foundation.BOOL
    fccVideo: UInt32
    dwVideoWidth: UInt32
    dwVideoHeight: UInt32
    cVideoFramesReceived: UInt64
    cVideoFramesEncoded: UInt64
    cVideoFramesSkipped: UInt64
    cBlackVideoFramesEncoded: UInt64
    cVideoFramesDuplicated: UInt64
    cAudioSamplesPerSec: UInt32
    cAudioChannels: UInt32
    cAudioBytesReceived: UInt64
    cAudioFramesEncoded: UInt64
class MFMediaKeyStatus(EasyCastStructure):
    pbKeyId: POINTER(Byte)
    cbKeyId: UInt32
    eMediaKeyStatus: Windows.Win32.Media.MediaFoundation.MF_MEDIAKEY_STATUS
MFNETSOURCE_CACHE_STATE = Int32
MFNETSOURCE_CACHE_UNAVAILABLE: MFNETSOURCE_CACHE_STATE = 0
MFNETSOURCE_CACHE_ACTIVE_WRITING: MFNETSOURCE_CACHE_STATE = 1
MFNETSOURCE_CACHE_ACTIVE_COMPLETE: MFNETSOURCE_CACHE_STATE = 2
MFNETSOURCE_PROTOCOL_TYPE = Int32
MFNETSOURCE_UNDEFINED: MFNETSOURCE_PROTOCOL_TYPE = 0
MFNETSOURCE_HTTP: MFNETSOURCE_PROTOCOL_TYPE = 1
MFNETSOURCE_RTSP: MFNETSOURCE_PROTOCOL_TYPE = 2
MFNETSOURCE_FILE: MFNETSOURCE_PROTOCOL_TYPE = 3
MFNETSOURCE_MULTICAST: MFNETSOURCE_PROTOCOL_TYPE = 4
MFNETSOURCE_STATISTICS_IDS = Int32
MFNETSOURCE_RECVPACKETS_ID: MFNETSOURCE_STATISTICS_IDS = 0
MFNETSOURCE_LOSTPACKETS_ID: MFNETSOURCE_STATISTICS_IDS = 1
MFNETSOURCE_RESENDSREQUESTED_ID: MFNETSOURCE_STATISTICS_IDS = 2
MFNETSOURCE_RESENDSRECEIVED_ID: MFNETSOURCE_STATISTICS_IDS = 3
MFNETSOURCE_RECOVEREDBYECCPACKETS_ID: MFNETSOURCE_STATISTICS_IDS = 4
MFNETSOURCE_RECOVEREDBYRTXPACKETS_ID: MFNETSOURCE_STATISTICS_IDS = 5
MFNETSOURCE_OUTPACKETS_ID: MFNETSOURCE_STATISTICS_IDS = 6
MFNETSOURCE_RECVRATE_ID: MFNETSOURCE_STATISTICS_IDS = 7
MFNETSOURCE_AVGBANDWIDTHBPS_ID: MFNETSOURCE_STATISTICS_IDS = 8
MFNETSOURCE_BYTESRECEIVED_ID: MFNETSOURCE_STATISTICS_IDS = 9
MFNETSOURCE_PROTOCOL_ID: MFNETSOURCE_STATISTICS_IDS = 10
MFNETSOURCE_TRANSPORT_ID: MFNETSOURCE_STATISTICS_IDS = 11
MFNETSOURCE_CACHE_STATE_ID: MFNETSOURCE_STATISTICS_IDS = 12
MFNETSOURCE_LINKBANDWIDTH_ID: MFNETSOURCE_STATISTICS_IDS = 13
MFNETSOURCE_CONTENTBITRATE_ID: MFNETSOURCE_STATISTICS_IDS = 14
MFNETSOURCE_SPEEDFACTOR_ID: MFNETSOURCE_STATISTICS_IDS = 15
MFNETSOURCE_BUFFERSIZE_ID: MFNETSOURCE_STATISTICS_IDS = 16
MFNETSOURCE_BUFFERPROGRESS_ID: MFNETSOURCE_STATISTICS_IDS = 17
MFNETSOURCE_LASTBWSWITCHTS_ID: MFNETSOURCE_STATISTICS_IDS = 18
MFNETSOURCE_SEEKRANGESTART_ID: MFNETSOURCE_STATISTICS_IDS = 19
MFNETSOURCE_SEEKRANGEEND_ID: MFNETSOURCE_STATISTICS_IDS = 20
MFNETSOURCE_BUFFERINGCOUNT_ID: MFNETSOURCE_STATISTICS_IDS = 21
MFNETSOURCE_INCORRECTLYSIGNEDPACKETS_ID: MFNETSOURCE_STATISTICS_IDS = 22
MFNETSOURCE_SIGNEDSESSION_ID: MFNETSOURCE_STATISTICS_IDS = 23
MFNETSOURCE_MAXBITRATE_ID: MFNETSOURCE_STATISTICS_IDS = 24
MFNETSOURCE_RECEPTION_QUALITY_ID: MFNETSOURCE_STATISTICS_IDS = 25
MFNETSOURCE_RECOVEREDPACKETS_ID: MFNETSOURCE_STATISTICS_IDS = 26
MFNETSOURCE_VBR_ID: MFNETSOURCE_STATISTICS_IDS = 27
MFNETSOURCE_DOWNLOADPROGRESS_ID: MFNETSOURCE_STATISTICS_IDS = 28
MFNETSOURCE_UNPREDEFINEDPROTOCOLNAME_ID: MFNETSOURCE_STATISTICS_IDS = 29
MFNETSOURCE_TRANSPORT_TYPE = Int32
MFNETSOURCE_UDP: MFNETSOURCE_TRANSPORT_TYPE = 0
MFNETSOURCE_TCP: MFNETSOURCE_TRANSPORT_TYPE = 1
MFNET_PROXYSETTINGS = Int32
MFNET_PROXYSETTING_NONE: MFNET_PROXYSETTINGS = 0
MFNET_PROXYSETTING_MANUAL: MFNET_PROXYSETTINGS = 1
MFNET_PROXYSETTING_AUTO: MFNET_PROXYSETTINGS = 2
MFNET_PROXYSETTING_BROWSER: MFNET_PROXYSETTINGS = 3
MFNetAuthenticationFlags = Int32
MFNET_AUTHENTICATION_PROXY: MFNetAuthenticationFlags = 1
MFNET_AUTHENTICATION_CLEAR_TEXT: MFNetAuthenticationFlags = 2
MFNET_AUTHENTICATION_LOGGED_ON_USER: MFNetAuthenticationFlags = 4
class MFNetCredentialManagerGetParam(EasyCastStructure):
    hrOp: Windows.Win32.Foundation.HRESULT
    fAllowLoggedOnUser: Windows.Win32.Foundation.BOOL
    fClearTextPackage: Windows.Win32.Foundation.BOOL
    pszUrl: Windows.Win32.Foundation.PWSTR
    pszSite: Windows.Win32.Foundation.PWSTR
    pszRealm: Windows.Win32.Foundation.PWSTR
    pszPackage: Windows.Win32.Foundation.PWSTR
    nRetries: Int32
MFNetCredentialOptions = Int32
MFNET_CREDENTIAL_SAVE: MFNetCredentialOptions = 1
MFNET_CREDENTIAL_DONT_CACHE: MFNetCredentialOptions = 2
MFNET_CREDENTIAL_ALLOW_CLEAR_TEXT: MFNetCredentialOptions = 4
MFNetCredentialRequirements = Int32
REQUIRE_PROMPT: MFNetCredentialRequirements = 1
REQUIRE_SAVE_SELECTED: MFNetCredentialRequirements = 2
MFNominalRange = Int32
MFNominalRange_Unknown: MFNominalRange = 0
MFNominalRange_Normal: MFNominalRange = 1
MFNominalRange_Wide: MFNominalRange = 2
MFNominalRange_0_255: MFNominalRange = 1
MFNominalRange_16_235: MFNominalRange = 2
MFNominalRange_48_208: MFNominalRange = 3
MFNominalRange_64_127: MFNominalRange = 4
MFNominalRange_Last: MFNominalRange = 5
MFNominalRange_ForceDWORD: MFNominalRange = 2147483647
class MFOffset(EasyCastStructure):
    fract: UInt16
    value: Int16
@winfunctype_pointer
def MFPERIODICCALLBACK(pContext: Windows.Win32.System.Com.IUnknown_head) -> Void: ...
MFPMPSESSION_CREATION_FLAGS = Int32
MFPMPSESSION_UNPROTECTED_PROCESS: MFPMPSESSION_CREATION_FLAGS = 1
MFPMPSESSION_IN_PROCESS: MFPMPSESSION_CREATION_FLAGS = 2
MFPOLICYMANAGER_ACTION = Int32
PEACTION_NO: MFPOLICYMANAGER_ACTION = 0
PEACTION_PLAY: MFPOLICYMANAGER_ACTION = 1
PEACTION_COPY: MFPOLICYMANAGER_ACTION = 2
PEACTION_EXPORT: MFPOLICYMANAGER_ACTION = 3
PEACTION_EXTRACT: MFPOLICYMANAGER_ACTION = 4
PEACTION_RESERVED1: MFPOLICYMANAGER_ACTION = 5
PEACTION_RESERVED2: MFPOLICYMANAGER_ACTION = 6
PEACTION_RESERVED3: MFPOLICYMANAGER_ACTION = 7
PEACTION_LAST: MFPOLICYMANAGER_ACTION = 7
class MFP_ACQUIRE_USER_CREDENTIAL_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    dwUserData: UIntPtr
    fProceedWithAuthentication: Windows.Win32.Foundation.BOOL
    hrAuthenticationStatus: Windows.Win32.Foundation.HRESULT
    pwszURL: Windows.Win32.Foundation.PWSTR
    pwszSite: Windows.Win32.Foundation.PWSTR
    pwszRealm: Windows.Win32.Foundation.PWSTR
    pwszPackage: Windows.Win32.Foundation.PWSTR
    nRetries: Int32
    flags: UInt32
    pCredential: Windows.Win32.Media.MediaFoundation.IMFNetCredential_head
MFP_CREATION_OPTIONS = Int32
MFP_OPTION_NONE: MFP_CREATION_OPTIONS = 0
MFP_OPTION_FREE_THREADED_CALLBACK: MFP_CREATION_OPTIONS = 1
MFP_OPTION_NO_MMCSS: MFP_CREATION_OPTIONS = 2
MFP_OPTION_NO_REMOTE_DESKTOP_OPTIMIZATION: MFP_CREATION_OPTIONS = 4
class MFP_ERROR_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
class MFP_EVENT_HEADER(EasyCastStructure):
    eEventType: Windows.Win32.Media.MediaFoundation.MFP_EVENT_TYPE
    hrEvent: Windows.Win32.Foundation.HRESULT
    pMediaPlayer: Windows.Win32.Media.MediaFoundation.IMFPMediaPlayer_head
    eState: Windows.Win32.Media.MediaFoundation.MFP_MEDIAPLAYER_STATE
    pPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head
MFP_EVENT_TYPE = Int32
MFP_EVENT_TYPE_PLAY: MFP_EVENT_TYPE = 0
MFP_EVENT_TYPE_PAUSE: MFP_EVENT_TYPE = 1
MFP_EVENT_TYPE_STOP: MFP_EVENT_TYPE = 2
MFP_EVENT_TYPE_POSITION_SET: MFP_EVENT_TYPE = 3
MFP_EVENT_TYPE_RATE_SET: MFP_EVENT_TYPE = 4
MFP_EVENT_TYPE_MEDIAITEM_CREATED: MFP_EVENT_TYPE = 5
MFP_EVENT_TYPE_MEDIAITEM_SET: MFP_EVENT_TYPE = 6
MFP_EVENT_TYPE_FRAME_STEP: MFP_EVENT_TYPE = 7
MFP_EVENT_TYPE_MEDIAITEM_CLEARED: MFP_EVENT_TYPE = 8
MFP_EVENT_TYPE_MF: MFP_EVENT_TYPE = 9
MFP_EVENT_TYPE_ERROR: MFP_EVENT_TYPE = 10
MFP_EVENT_TYPE_PLAYBACK_ENDED: MFP_EVENT_TYPE = 11
MFP_EVENT_TYPE_ACQUIRE_USER_CREDENTIAL: MFP_EVENT_TYPE = 12
class MFP_FRAME_STEP_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFP_MEDIAITEM_CLEARED_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFP_MEDIAITEM_CREATED_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
    dwUserData: UIntPtr
class MFP_MEDIAITEM_SET_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
MFP_MEDIAPLAYER_STATE = Int32
MFP_MEDIAPLAYER_STATE_EMPTY: MFP_MEDIAPLAYER_STATE = 0
MFP_MEDIAPLAYER_STATE_STOPPED: MFP_MEDIAPLAYER_STATE = 1
MFP_MEDIAPLAYER_STATE_PLAYING: MFP_MEDIAPLAYER_STATE = 2
MFP_MEDIAPLAYER_STATE_PAUSED: MFP_MEDIAPLAYER_STATE = 3
MFP_MEDIAPLAYER_STATE_SHUTDOWN: MFP_MEDIAPLAYER_STATE = 4
class MFP_MF_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    MFEventType: UInt32
    pMFMediaEvent: Windows.Win32.Media.MediaFoundation.IMFMediaEvent_head
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFP_PAUSE_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFP_PLAYBACK_ENDED_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFP_PLAY_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFP_POSITION_SET_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFP_RATE_SET_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
    flRate: Single
class MFP_STOP_EVENT(EasyCastStructure):
    header: Windows.Win32.Media.MediaFoundation.MFP_EVENT_HEADER
    pMediaItem: Windows.Win32.Media.MediaFoundation.IMFPMediaItem_head
class MFPaletteEntry(EasyCastUnion):
    ARGB: Windows.Win32.Media.MediaFoundation.MFARGB
    AYCbCr: Windows.Win32.Media.MediaFoundation.MFAYUVSample
class MFPinholeCameraIntrinsic_IntrinsicModel(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    CameraModel: Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_PinholeCameraModel
    DistortionModel: Windows.Win32.Media.MediaFoundation.MFCameraIntrinsic_DistortionModel
class MFPinholeCameraIntrinsics(EasyCastStructure):
    IntrinsicModelCount: UInt32
    IntrinsicModels: Windows.Win32.Media.MediaFoundation.MFPinholeCameraIntrinsic_IntrinsicModel * 1
MFRATE_DIRECTION = Int32
MFRATE_FORWARD: MFRATE_DIRECTION = 0
MFRATE_REVERSE: MFRATE_DIRECTION = 1
class MFRR_COMPONENTS(EasyCastStructure):
    dwRRInfoVersion: UInt32
    dwRRComponents: UInt32
    pRRComponents: POINTER(Windows.Win32.Media.MediaFoundation.MFRR_COMPONENT_HASH_INFO_head)
class MFRR_COMPONENT_HASH_INFO(EasyCastStructure):
    ulReason: UInt32
    rgHeaderHash: Char * 43
    rgPublicKeyHash: Char * 43
    wszName: Char * 260
class MFRatio(EasyCastStructure):
    Numerator: UInt32
    Denominator: UInt32
MFSESSION_GETFULLTOPOLOGY_FLAGS = Int32
MFSESSION_GETFULLTOPOLOGY_CURRENT: MFSESSION_GETFULLTOPOLOGY_FLAGS = 1
MFSESSION_SETTOPOLOGY_FLAGS = Int32
MFSESSION_SETTOPOLOGY_IMMEDIATE: MFSESSION_SETTOPOLOGY_FLAGS = 1
MFSESSION_SETTOPOLOGY_NORESOLUTION: MFSESSION_SETTOPOLOGY_FLAGS = 2
MFSESSION_SETTOPOLOGY_CLEAR_CURRENT: MFSESSION_SETTOPOLOGY_FLAGS = 4
MFSHUTDOWN_STATUS = Int32
MFSHUTDOWN_INITIATED: MFSHUTDOWN_STATUS = 0
MFSHUTDOWN_COMPLETED: MFSHUTDOWN_STATUS = 1
MFSINK_WMDRMACTION = Int32
MFSINK_WMDRMACTION_UNDEFINED: MFSINK_WMDRMACTION = 0
MFSINK_WMDRMACTION_ENCODE: MFSINK_WMDRMACTION = 1
MFSINK_WMDRMACTION_TRANSCODE: MFSINK_WMDRMACTION = 2
MFSINK_WMDRMACTION_TRANSCRYPT: MFSINK_WMDRMACTION = 3
MFSINK_WMDRMACTION_LAST: MFSINK_WMDRMACTION = 3
MFSTREAMSINK_MARKER_TYPE = Int32
MFSTREAMSINK_MARKER_DEFAULT: MFSTREAMSINK_MARKER_TYPE = 0
MFSTREAMSINK_MARKER_ENDOFSEGMENT: MFSTREAMSINK_MARKER_TYPE = 1
MFSTREAMSINK_MARKER_TICK: MFSTREAMSINK_MARKER_TYPE = 2
MFSTREAMSINK_MARKER_EVENT: MFSTREAMSINK_MARKER_TYPE = 3
MFSampleAllocatorUsage = Int32
MFSampleAllocatorUsage_UsesProvidedAllocator: MFSampleAllocatorUsage = 0
MFSampleAllocatorUsage_UsesCustomAllocator: MFSampleAllocatorUsage = 1
MFSampleAllocatorUsage_DoesNotAllocate: MFSampleAllocatorUsage = 2
MFSampleEncryptionProtectionScheme = Int32
MF_SAMPLE_ENCRYPTION_PROTECTION_SCHEME_NONE: MFSampleEncryptionProtectionScheme = 0
MF_SAMPLE_ENCRYPTION_PROTECTION_SCHEME_AES_CTR: MFSampleEncryptionProtectionScheme = 1
MF_SAMPLE_ENCRYPTION_PROTECTION_SCHEME_AES_CBC: MFSampleEncryptionProtectionScheme = 2
MFSensorDeviceMode = Int32
MFSensorDeviceMode_Controller: MFSensorDeviceMode = 0
MFSensorDeviceMode_Shared: MFSensorDeviceMode = 1
MFSensorDeviceType = Int32
MFSensorDeviceType_Unknown: MFSensorDeviceType = 0
MFSensorDeviceType_Device: MFSensorDeviceType = 1
MFSensorDeviceType_MediaSource: MFSensorDeviceType = 2
MFSensorDeviceType_FrameProvider: MFSensorDeviceType = 3
MFSensorDeviceType_SensorTransform: MFSensorDeviceType = 4
MFSensorStreamType = Int32
MFSensorStreamType_Unknown: MFSensorStreamType = 0
MFSensorStreamType_Input: MFSensorStreamType = 1
MFSensorStreamType_Output: MFSensorStreamType = 2
MFSequencerTopologyFlags = Int32
SequencerTopologyFlags_Last: MFSequencerTopologyFlags = 1
MFStandardVideoFormat = Int32
MFStdVideoFormat_reserved: MFStandardVideoFormat = 0
MFStdVideoFormat_NTSC: MFStandardVideoFormat = 1
MFStdVideoFormat_PAL: MFStandardVideoFormat = 2
MFStdVideoFormat_DVD_NTSC: MFStandardVideoFormat = 3
MFStdVideoFormat_DVD_PAL: MFStandardVideoFormat = 4
MFStdVideoFormat_DV_PAL: MFStandardVideoFormat = 5
MFStdVideoFormat_DV_NTSC: MFStandardVideoFormat = 6
MFStdVideoFormat_ATSC_SD480i: MFStandardVideoFormat = 7
MFStdVideoFormat_ATSC_HD1080i: MFStandardVideoFormat = 8
MFStdVideoFormat_ATSC_HD720p: MFStandardVideoFormat = 9
MFTIMER_FLAGS = Int32
MFTIMER_RELATIVE: MFTIMER_FLAGS = 1
MFTOPOLOGY_DXVA_MODE = Int32
MFTOPOLOGY_DXVA_DEFAULT: MFTOPOLOGY_DXVA_MODE = 0
MFTOPOLOGY_DXVA_NONE: MFTOPOLOGY_DXVA_MODE = 1
MFTOPOLOGY_DXVA_FULL: MFTOPOLOGY_DXVA_MODE = 2
MFTOPOLOGY_HARDWARE_MODE = Int32
MFTOPOLOGY_HWMODE_SOFTWARE_ONLY: MFTOPOLOGY_HARDWARE_MODE = 0
MFTOPOLOGY_HWMODE_USE_HARDWARE: MFTOPOLOGY_HARDWARE_MODE = 1
MFTOPOLOGY_HWMODE_USE_ONLY_HARDWARE: MFTOPOLOGY_HARDWARE_MODE = 2
class MFTOPONODE_ATTRIBUTE_UPDATE(EasyCastStructure):
    NodeId: UInt64
    guidAttributeKey: Guid
    attrType: Windows.Win32.Media.MediaFoundation.MF_ATTRIBUTE_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        u32: UInt32
        u64: UInt64
        d: Double
MFT_AUDIO_DECODER_DEGRADATION_REASON = Int32
MFT_AUDIO_DECODER_DEGRADATION_REASON_NONE: MFT_AUDIO_DECODER_DEGRADATION_REASON = 0
MFT_AUDIO_DECODER_DEGRADATION_REASON_LICENSING_REQUIREMENT: MFT_AUDIO_DECODER_DEGRADATION_REASON = 1
MFT_AUDIO_DECODER_DEGRADATION_TYPE = Int32
MFT_AUDIO_DECODER_DEGRADATION_TYPE_NONE: MFT_AUDIO_DECODER_DEGRADATION_TYPE = 0
MFT_AUDIO_DECODER_DEGRADATION_TYPE_DOWNMIX2CHANNEL: MFT_AUDIO_DECODER_DEGRADATION_TYPE = 1
MFT_AUDIO_DECODER_DEGRADATION_TYPE_DOWNMIX6CHANNEL: MFT_AUDIO_DECODER_DEGRADATION_TYPE = 2
MFT_AUDIO_DECODER_DEGRADATION_TYPE_DOWNMIX8CHANNEL: MFT_AUDIO_DECODER_DEGRADATION_TYPE = 3
MFT_DRAIN_TYPE = Int32
MFT_DRAIN_PRODUCE_TAILS: MFT_DRAIN_TYPE = 0
MFT_DRAIN_NO_TAILS: MFT_DRAIN_TYPE = 1
MFT_ENUM_FLAG = Int32
MFT_ENUM_FLAG_SYNCMFT: MFT_ENUM_FLAG = 1
MFT_ENUM_FLAG_ASYNCMFT: MFT_ENUM_FLAG = 2
MFT_ENUM_FLAG_HARDWARE: MFT_ENUM_FLAG = 4
MFT_ENUM_FLAG_FIELDOFUSE: MFT_ENUM_FLAG = 8
MFT_ENUM_FLAG_LOCALMFT: MFT_ENUM_FLAG = 16
MFT_ENUM_FLAG_TRANSCODE_ONLY: MFT_ENUM_FLAG = 32
MFT_ENUM_FLAG_SORTANDFILTER: MFT_ENUM_FLAG = 64
MFT_ENUM_FLAG_SORTANDFILTER_APPROVED_ONLY: MFT_ENUM_FLAG = 192
MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY: MFT_ENUM_FLAG = 320
MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY_EDGEMODE: MFT_ENUM_FLAG = 576
MFT_ENUM_FLAG_UNTRUSTED_STOREMFT: MFT_ENUM_FLAG = 1024
MFT_ENUM_FLAG_ALL: MFT_ENUM_FLAG = 63
class MFT_INPUT_STREAM_INFO(EasyCastStructure):
    hnsMaxLatency: Int64
    dwFlags: UInt32
    cbSize: UInt32
    cbMaxLookahead: UInt32
    cbAlignment: UInt32
MFT_MESSAGE_TYPE = Int32
MFT_MESSAGE_COMMAND_FLUSH: MFT_MESSAGE_TYPE = 0
MFT_MESSAGE_COMMAND_DRAIN: MFT_MESSAGE_TYPE = 1
MFT_MESSAGE_SET_D3D_MANAGER: MFT_MESSAGE_TYPE = 2
MFT_MESSAGE_DROP_SAMPLES: MFT_MESSAGE_TYPE = 3
MFT_MESSAGE_COMMAND_TICK: MFT_MESSAGE_TYPE = 4
MFT_MESSAGE_NOTIFY_BEGIN_STREAMING: MFT_MESSAGE_TYPE = 268435456
MFT_MESSAGE_NOTIFY_END_STREAMING: MFT_MESSAGE_TYPE = 268435457
MFT_MESSAGE_NOTIFY_END_OF_STREAM: MFT_MESSAGE_TYPE = 268435458
MFT_MESSAGE_NOTIFY_START_OF_STREAM: MFT_MESSAGE_TYPE = 268435459
MFT_MESSAGE_NOTIFY_RELEASE_RESOURCES: MFT_MESSAGE_TYPE = 268435460
MFT_MESSAGE_NOTIFY_REACQUIRE_RESOURCES: MFT_MESSAGE_TYPE = 268435461
MFT_MESSAGE_NOTIFY_EVENT: MFT_MESSAGE_TYPE = 268435462
MFT_MESSAGE_COMMAND_SET_OUTPUT_STREAM_STATE: MFT_MESSAGE_TYPE = 268435463
MFT_MESSAGE_COMMAND_FLUSH_OUTPUT_STREAM: MFT_MESSAGE_TYPE = 268435464
MFT_MESSAGE_COMMAND_MARKER: MFT_MESSAGE_TYPE = 536870912
class MFT_OUTPUT_DATA_BUFFER(EasyCastStructure):
    dwStreamID: UInt32
    pSample: Windows.Win32.Media.MediaFoundation.IMFSample_head
    dwStatus: UInt32
    pEvents: Windows.Win32.Media.MediaFoundation.IMFCollection_head
class MFT_OUTPUT_STREAM_INFO(EasyCastStructure):
    dwFlags: UInt32
    cbSize: UInt32
    cbAlignment: UInt32
class MFT_REGISTER_TYPE_INFO(EasyCastStructure):
    guidMajorType: Guid
    guidSubtype: Guid
class MFT_REGISTRATION_INFO(EasyCastStructure):
    clsid: Guid
    guidCategory: Guid
    uiFlags: UInt32
    pszName: Windows.Win32.Foundation.PWSTR
    cInTypes: UInt32
    pInTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head)
    cOutTypes: UInt32
    pOutTypes: POINTER(Windows.Win32.Media.MediaFoundation.MFT_REGISTER_TYPE_INFO_head)
class MFT_STREAM_STATE_PARAM(EasyCastStructure):
    StreamId: UInt32
    State: Windows.Win32.Media.MediaFoundation.MF_STREAM_STATE
class MFVIDEOFORMAT(EasyCastStructure):
    dwSize: UInt32
    videoInfo: Windows.Win32.Media.MediaFoundation.MFVideoInfo
    guidFormat: Guid
    compressedInfo: Windows.Win32.Media.MediaFoundation.MFVideoCompressedInfo
    surfaceInfo: Windows.Win32.Media.MediaFoundation.MFVideoSurfaceInfo
MFVP_MESSAGE_TYPE = Int32
MFVP_MESSAGE_FLUSH: MFVP_MESSAGE_TYPE = 0
MFVP_MESSAGE_INVALIDATEMEDIATYPE: MFVP_MESSAGE_TYPE = 1
MFVP_MESSAGE_PROCESSINPUTNOTIFY: MFVP_MESSAGE_TYPE = 2
MFVP_MESSAGE_BEGINSTREAMING: MFVP_MESSAGE_TYPE = 3
MFVP_MESSAGE_ENDSTREAMING: MFVP_MESSAGE_TYPE = 4
MFVP_MESSAGE_ENDOFSTREAM: MFVP_MESSAGE_TYPE = 5
MFVP_MESSAGE_STEP: MFVP_MESSAGE_TYPE = 6
MFVP_MESSAGE_CANCELSTEP: MFVP_MESSAGE_TYPE = 7
MFVideo3DFormat = Int32
MFVideo3DSampleFormat_BaseView: MFVideo3DFormat = 0
MFVideo3DSampleFormat_MultiView: MFVideo3DFormat = 1
MFVideo3DSampleFormat_Packed_LeftRight: MFVideo3DFormat = 2
MFVideo3DSampleFormat_Packed_TopBottom: MFVideo3DFormat = 3
MFVideo3DSampleFormat = Int32
MFSampleExtension_3DVideo_MultiView: MFVideo3DSampleFormat = 1
MFSampleExtension_3DVideo_Packed: MFVideo3DSampleFormat = 0
class MFVideoAlphaBitmap(EasyCastStructure):
    GetBitmapFromDC: Windows.Win32.Foundation.BOOL
    bitmap: _bitmap_e__Union
    params: Windows.Win32.Media.MediaFoundation.MFVideoAlphaBitmapParams
    class _bitmap_e__Union(EasyCastUnion):
        hdc: Windows.Win32.Graphics.Gdi.HDC
        pDDS: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head
MFVideoAlphaBitmapFlags = Int32
MFVideoAlphaBitmap_EntireDDS: MFVideoAlphaBitmapFlags = 1
MFVideoAlphaBitmap_SrcColorKey: MFVideoAlphaBitmapFlags = 2
MFVideoAlphaBitmap_SrcRect: MFVideoAlphaBitmapFlags = 4
MFVideoAlphaBitmap_DestRect: MFVideoAlphaBitmapFlags = 8
MFVideoAlphaBitmap_FilterMode: MFVideoAlphaBitmapFlags = 16
MFVideoAlphaBitmap_Alpha: MFVideoAlphaBitmapFlags = 32
MFVideoAlphaBitmap_BitMask: MFVideoAlphaBitmapFlags = 63
class MFVideoAlphaBitmapParams(EasyCastStructure):
    dwFlags: UInt32
    clrSrcKey: Windows.Win32.Foundation.COLORREF
    rcSrc: Windows.Win32.Foundation.RECT
    nrcDest: Windows.Win32.Media.MediaFoundation.MFVideoNormalizedRect
    fAlpha: Single
    dwFilterMode: UInt32
class MFVideoArea(EasyCastStructure):
    OffsetX: Windows.Win32.Media.MediaFoundation.MFOffset
    OffsetY: Windows.Win32.Media.MediaFoundation.MFOffset
    Area: Windows.Win32.Foundation.SIZE
MFVideoAspectRatioMode = Int32
MFVideoARMode_None: MFVideoAspectRatioMode = 0
MFVideoARMode_PreservePicture: MFVideoAspectRatioMode = 1
MFVideoARMode_PreservePixel: MFVideoAspectRatioMode = 2
MFVideoARMode_NonLinearStretch: MFVideoAspectRatioMode = 4
MFVideoARMode_Mask: MFVideoAspectRatioMode = 7
MFVideoChromaSubsampling = Int32
MFVideoChromaSubsampling_Unknown: MFVideoChromaSubsampling = 0
MFVideoChromaSubsampling_ProgressiveChroma: MFVideoChromaSubsampling = 8
MFVideoChromaSubsampling_Horizontally_Cosited: MFVideoChromaSubsampling = 4
MFVideoChromaSubsampling_Vertically_Cosited: MFVideoChromaSubsampling = 2
MFVideoChromaSubsampling_Vertically_AlignedChromaPlanes: MFVideoChromaSubsampling = 1
MFVideoChromaSubsampling_MPEG2: MFVideoChromaSubsampling = 5
MFVideoChromaSubsampling_MPEG1: MFVideoChromaSubsampling = 1
MFVideoChromaSubsampling_DV_PAL: MFVideoChromaSubsampling = 6
MFVideoChromaSubsampling_Cosited: MFVideoChromaSubsampling = 7
MFVideoChromaSubsampling_Last: MFVideoChromaSubsampling = 8
MFVideoChromaSubsampling_ForceDWORD: MFVideoChromaSubsampling = 2147483647
class MFVideoCompressedInfo(EasyCastStructure):
    AvgBitrate: Int64
    AvgBitErrorRate: Int64
    MaxKeyFrameSpacing: UInt32
MFVideoDRMFlags = Int32
MFVideoDRMFlag_None: MFVideoDRMFlags = 0
MFVideoDRMFlag_AnalogProtected: MFVideoDRMFlags = 1
MFVideoDRMFlag_DigitallyProtected: MFVideoDRMFlags = 2
MFVideoDSPMode = Int32
MFVideoDSPMode_Passthrough: MFVideoDSPMode = 1
MFVideoDSPMode_Stabilization: MFVideoDSPMode = 4
MFVideoFlags = Int32
MFVideoFlag_PAD_TO_Mask: MFVideoFlags = 3
MFVideoFlag_PAD_TO_None: MFVideoFlags = 0
MFVideoFlag_PAD_TO_4x3: MFVideoFlags = 1
MFVideoFlag_PAD_TO_16x9: MFVideoFlags = 2
MFVideoFlag_SrcContentHintMask: MFVideoFlags = 28
MFVideoFlag_SrcContentHintNone: MFVideoFlags = 0
MFVideoFlag_SrcContentHint16x9: MFVideoFlags = 4
MFVideoFlag_SrcContentHint235_1: MFVideoFlags = 8
MFVideoFlag_AnalogProtected: MFVideoFlags = 32
MFVideoFlag_DigitallyProtected: MFVideoFlags = 64
MFVideoFlag_ProgressiveContent: MFVideoFlags = 128
MFVideoFlag_FieldRepeatCountMask: MFVideoFlags = 1792
MFVideoFlag_FieldRepeatCountShift: MFVideoFlags = 8
MFVideoFlag_ProgressiveSeqReset: MFVideoFlags = 2048
MFVideoFlag_PanScanEnabled: MFVideoFlags = 131072
MFVideoFlag_LowerFieldFirst: MFVideoFlags = 262144
MFVideoFlag_BottomUpLinearRep: MFVideoFlags = 524288
MFVideoFlags_DXVASurface: MFVideoFlags = 1048576
MFVideoFlags_RenderTargetSurface: MFVideoFlags = 4194304
MFVideoFlags_ForceQWORD: MFVideoFlags = 2147483647
class MFVideoInfo(EasyCastStructure):
    dwWidth: UInt32
    dwHeight: UInt32
    PixelAspectRatio: Windows.Win32.Media.MediaFoundation.MFRatio
    SourceChromaSubsampling: Windows.Win32.Media.MediaFoundation.MFVideoChromaSubsampling
    InterlaceMode: Windows.Win32.Media.MediaFoundation.MFVideoInterlaceMode
    TransferFunction: Windows.Win32.Media.MediaFoundation.MFVideoTransferFunction
    ColorPrimaries: Windows.Win32.Media.MediaFoundation.MFVideoPrimaries
    TransferMatrix: Windows.Win32.Media.MediaFoundation.MFVideoTransferMatrix
    SourceLighting: Windows.Win32.Media.MediaFoundation.MFVideoLighting
    FramesPerSecond: Windows.Win32.Media.MediaFoundation.MFRatio
    NominalRange: Windows.Win32.Media.MediaFoundation.MFNominalRange
    GeometricAperture: Windows.Win32.Media.MediaFoundation.MFVideoArea
    MinimumDisplayAperture: Windows.Win32.Media.MediaFoundation.MFVideoArea
    PanScanAperture: Windows.Win32.Media.MediaFoundation.MFVideoArea
    VideoFlags: UInt64
MFVideoInterlaceMode = Int32
MFVideoInterlace_Unknown: MFVideoInterlaceMode = 0
MFVideoInterlace_Progressive: MFVideoInterlaceMode = 2
MFVideoInterlace_FieldInterleavedUpperFirst: MFVideoInterlaceMode = 3
MFVideoInterlace_FieldInterleavedLowerFirst: MFVideoInterlaceMode = 4
MFVideoInterlace_FieldSingleUpper: MFVideoInterlaceMode = 5
MFVideoInterlace_FieldSingleLower: MFVideoInterlaceMode = 6
MFVideoInterlace_MixedInterlaceOrProgressive: MFVideoInterlaceMode = 7
MFVideoInterlace_Last: MFVideoInterlaceMode = 8
MFVideoInterlace_ForceDWORD: MFVideoInterlaceMode = 2147483647
MFVideoLighting = Int32
MFVideoLighting_Unknown: MFVideoLighting = 0
MFVideoLighting_bright: MFVideoLighting = 1
MFVideoLighting_office: MFVideoLighting = 2
MFVideoLighting_dim: MFVideoLighting = 3
MFVideoLighting_dark: MFVideoLighting = 4
MFVideoLighting_Last: MFVideoLighting = 5
MFVideoLighting_ForceDWORD: MFVideoLighting = 2147483647
MFVideoMixPrefs = Int32
MFVideoMixPrefs_ForceHalfInterlace: MFVideoMixPrefs = 1
MFVideoMixPrefs_AllowDropToHalfInterlace: MFVideoMixPrefs = 2
MFVideoMixPrefs_AllowDropToBob: MFVideoMixPrefs = 4
MFVideoMixPrefs_ForceBob: MFVideoMixPrefs = 8
MFVideoMixPrefs_EnableRotation: MFVideoMixPrefs = 16
MFVideoMixPrefs_Mask: MFVideoMixPrefs = 31
class MFVideoNormalizedRect(EasyCastStructure):
    left: Single
    top: Single
    right: Single
    bottom: Single
MFVideoPadFlags = Int32
MFVideoPadFlag_PAD_TO_None: MFVideoPadFlags = 0
MFVideoPadFlag_PAD_TO_4x3: MFVideoPadFlags = 1
MFVideoPadFlag_PAD_TO_16x9: MFVideoPadFlags = 2
MFVideoPrimaries = Int32
MFVideoPrimaries_Unknown: MFVideoPrimaries = 0
MFVideoPrimaries_reserved: MFVideoPrimaries = 1
MFVideoPrimaries_BT709: MFVideoPrimaries = 2
MFVideoPrimaries_BT470_2_SysM: MFVideoPrimaries = 3
MFVideoPrimaries_BT470_2_SysBG: MFVideoPrimaries = 4
MFVideoPrimaries_SMPTE170M: MFVideoPrimaries = 5
MFVideoPrimaries_SMPTE240M: MFVideoPrimaries = 6
MFVideoPrimaries_EBU3213: MFVideoPrimaries = 7
MFVideoPrimaries_SMPTE_C: MFVideoPrimaries = 8
MFVideoPrimaries_BT2020: MFVideoPrimaries = 9
MFVideoPrimaries_XYZ: MFVideoPrimaries = 10
MFVideoPrimaries_DCI_P3: MFVideoPrimaries = 11
MFVideoPrimaries_ACES: MFVideoPrimaries = 12
MFVideoPrimaries_Last: MFVideoPrimaries = 13
MFVideoPrimaries_ForceDWORD: MFVideoPrimaries = 2147483647
MFVideoRenderPrefs = Int32
MFVideoRenderPrefs_DoNotRenderBorder: MFVideoRenderPrefs = 1
MFVideoRenderPrefs_DoNotClipToDevice: MFVideoRenderPrefs = 2
MFVideoRenderPrefs_AllowOutputThrottling: MFVideoRenderPrefs = 4
MFVideoRenderPrefs_ForceOutputThrottling: MFVideoRenderPrefs = 8
MFVideoRenderPrefs_ForceBatching: MFVideoRenderPrefs = 16
MFVideoRenderPrefs_AllowBatching: MFVideoRenderPrefs = 32
MFVideoRenderPrefs_ForceScaling: MFVideoRenderPrefs = 64
MFVideoRenderPrefs_AllowScaling: MFVideoRenderPrefs = 128
MFVideoRenderPrefs_DoNotRepaintOnStop: MFVideoRenderPrefs = 256
MFVideoRenderPrefs_Mask: MFVideoRenderPrefs = 511
MFVideoRotationFormat = Int32
MFVideoRotationFormat_0: MFVideoRotationFormat = 0
MFVideoRotationFormat_90: MFVideoRotationFormat = 90
MFVideoRotationFormat_180: MFVideoRotationFormat = 180
MFVideoRotationFormat_270: MFVideoRotationFormat = 270
MFVideoSphericalFormat = Int32
MFVideoSphericalFormat_Unsupported: MFVideoSphericalFormat = 0
MFVideoSphericalFormat_Equirectangular: MFVideoSphericalFormat = 1
MFVideoSphericalFormat_CubeMap: MFVideoSphericalFormat = 2
MFVideoSphericalFormat_3DMesh: MFVideoSphericalFormat = 3
MFVideoSphericalProjectionMode = Int32
MFVideoSphericalProjectionMode_Spherical: MFVideoSphericalProjectionMode = 0
MFVideoSphericalProjectionMode_Flat: MFVideoSphericalProjectionMode = 1
MFVideoSrcContentHintFlags = Int32
MFVideoSrcContentHintFlag_None: MFVideoSrcContentHintFlags = 0
MFVideoSrcContentHintFlag_16x9: MFVideoSrcContentHintFlags = 1
MFVideoSrcContentHintFlag_235_1: MFVideoSrcContentHintFlags = 2
class MFVideoSurfaceInfo(EasyCastStructure):
    Format: UInt32
    PaletteEntries: UInt32
    Palette: Windows.Win32.Media.MediaFoundation.MFPaletteEntry * 1
MFVideoTransferFunction = Int32
MFVideoTransFunc_Unknown: MFVideoTransferFunction = 0
MFVideoTransFunc_10: MFVideoTransferFunction = 1
MFVideoTransFunc_18: MFVideoTransferFunction = 2
MFVideoTransFunc_20: MFVideoTransferFunction = 3
MFVideoTransFunc_22: MFVideoTransferFunction = 4
MFVideoTransFunc_709: MFVideoTransferFunction = 5
MFVideoTransFunc_240M: MFVideoTransferFunction = 6
MFVideoTransFunc_sRGB: MFVideoTransferFunction = 7
MFVideoTransFunc_28: MFVideoTransferFunction = 8
MFVideoTransFunc_Log_100: MFVideoTransferFunction = 9
MFVideoTransFunc_Log_316: MFVideoTransferFunction = 10
MFVideoTransFunc_709_sym: MFVideoTransferFunction = 11
MFVideoTransFunc_2020_const: MFVideoTransferFunction = 12
MFVideoTransFunc_2020: MFVideoTransferFunction = 13
MFVideoTransFunc_26: MFVideoTransferFunction = 14
MFVideoTransFunc_2084: MFVideoTransferFunction = 15
MFVideoTransFunc_HLG: MFVideoTransferFunction = 16
MFVideoTransFunc_10_rel: MFVideoTransferFunction = 17
MFVideoTransFunc_Last: MFVideoTransferFunction = 18
MFVideoTransFunc_ForceDWORD: MFVideoTransferFunction = 2147483647
MFVideoTransferMatrix = Int32
MFVideoTransferMatrix_Unknown: MFVideoTransferMatrix = 0
MFVideoTransferMatrix_BT709: MFVideoTransferMatrix = 1
MFVideoTransferMatrix_BT601: MFVideoTransferMatrix = 2
MFVideoTransferMatrix_SMPTE240M: MFVideoTransferMatrix = 3
MFVideoTransferMatrix_BT2020_10: MFVideoTransferMatrix = 4
MFVideoTransferMatrix_BT2020_12: MFVideoTransferMatrix = 5
MFVideoTransferMatrix_Last: MFVideoTransferMatrix = 6
MFVideoTransferMatrix_ForceDWORD: MFVideoTransferMatrix = 2147483647
MFVirtualCameraAccess = Int32
MFVirtualCameraAccess_CurrentUser: MFVirtualCameraAccess = 0
MFVirtualCameraAccess_AllUsers: MFVirtualCameraAccess = 1
MFVirtualCameraLifetime = Int32
MFVirtualCameraLifetime_Session: MFVirtualCameraLifetime = 0
MFVirtualCameraLifetime_System: MFVirtualCameraLifetime = 1
MFVirtualCameraType = Int32
MFVirtualCameraType_SoftwareCameraSource: MFVirtualCameraType = 0
MFWaveFormatExConvertFlags = Int32
MFWaveFormatExConvertFlag_Normal: MFWaveFormatExConvertFlags = 0
MFWaveFormatExConvertFlag_ForceExtensible: MFWaveFormatExConvertFlags = 1
MF_ACTIVATE_CUSTOM_MIXER = Int32
MF_ACTIVATE_CUSTOM_MIXER_ALLOWFAIL: MF_ACTIVATE_CUSTOM_MIXER = 1
MF_ACTIVATE_CUSTOM_PRESENTER = Int32
MF_ACTIVATE_CUSTOM_PRESENTER_ALLOWFAIL: MF_ACTIVATE_CUSTOM_PRESENTER = 1
MF_ATTRIBUTES_MATCH_TYPE = Int32
MF_ATTRIBUTES_MATCH_OUR_ITEMS: MF_ATTRIBUTES_MATCH_TYPE = 0
MF_ATTRIBUTES_MATCH_THEIR_ITEMS: MF_ATTRIBUTES_MATCH_TYPE = 1
MF_ATTRIBUTES_MATCH_ALL_ITEMS: MF_ATTRIBUTES_MATCH_TYPE = 2
MF_ATTRIBUTES_MATCH_INTERSECTION: MF_ATTRIBUTES_MATCH_TYPE = 3
MF_ATTRIBUTES_MATCH_SMALLER: MF_ATTRIBUTES_MATCH_TYPE = 4
MF_ATTRIBUTE_SERIALIZE_OPTIONS = Int32
MF_ATTRIBUTE_SERIALIZE_UNKNOWN_BYREF: MF_ATTRIBUTE_SERIALIZE_OPTIONS = 1
MF_ATTRIBUTE_TYPE = Int32
MF_ATTRIBUTE_UINT32: MF_ATTRIBUTE_TYPE = 19
MF_ATTRIBUTE_UINT64: MF_ATTRIBUTE_TYPE = 21
MF_ATTRIBUTE_DOUBLE: MF_ATTRIBUTE_TYPE = 5
MF_ATTRIBUTE_GUID: MF_ATTRIBUTE_TYPE = 72
MF_ATTRIBUTE_STRING: MF_ATTRIBUTE_TYPE = 31
MF_ATTRIBUTE_BLOB: MF_ATTRIBUTE_TYPE = 4113
MF_ATTRIBUTE_IUNKNOWN: MF_ATTRIBUTE_TYPE = 13
MF_AUVRHP_ROOMMODEL = Int32
VRHP_SMALLROOM: MF_AUVRHP_ROOMMODEL = 0
VRHP_MEDIUMROOM: MF_AUVRHP_ROOMMODEL = 1
VRHP_BIGROOM: MF_AUVRHP_ROOMMODEL = 2
VRHP_CUSTUMIZEDROOM: MF_AUVRHP_ROOMMODEL = 3
class MF_BYTE_STREAM_CACHE_RANGE(EasyCastStructure):
    qwStartOffset: UInt64
    qwEndOffset: UInt64
MF_CAMERA_CONTROL_CONFIGURATION_TYPE = Int32
MF_CAMERA_CONTROL_CONFIGURATION_TYPE_PRESTART: MF_CAMERA_CONTROL_CONFIGURATION_TYPE = 0
MF_CAMERA_CONTROL_CONFIGURATION_TYPE_POSTSTART: MF_CAMERA_CONTROL_CONFIGURATION_TYPE = 1
class MF_CAMERA_CONTROL_RANGE_INFO(EasyCastStructure):
    minValue: Int32
    maxValue: Int32
    stepValue: Int32
    defaultValue: Int32
MF_CAPTURE_ENGINE_AUDIO_PROCESSING_MODE = Int32
MF_CAPTURE_ENGINE_AUDIO_PROCESSING_DEFAULT: MF_CAPTURE_ENGINE_AUDIO_PROCESSING_MODE = 0
MF_CAPTURE_ENGINE_AUDIO_PROCESSING_RAW: MF_CAPTURE_ENGINE_AUDIO_PROCESSING_MODE = 1
MF_CAPTURE_ENGINE_DEVICE_TYPE = Int32
MF_CAPTURE_ENGINE_DEVICE_TYPE_AUDIO: MF_CAPTURE_ENGINE_DEVICE_TYPE = 0
MF_CAPTURE_ENGINE_DEVICE_TYPE_VIDEO: MF_CAPTURE_ENGINE_DEVICE_TYPE = 1
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = Int32
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_OTHER: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 0
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_COMMUNICATIONS: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 1
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_MEDIA: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 2
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_GAMECHAT: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 3
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_SPEECH: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 4
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_FARFIELDSPEECH: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 5
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_UNIFORMSPEECH: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 6
MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_VOICETYPING: MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE = 7
MF_CAPTURE_ENGINE_SINK_TYPE = Int32
MF_CAPTURE_ENGINE_SINK_TYPE_RECORD: MF_CAPTURE_ENGINE_SINK_TYPE = 0
MF_CAPTURE_ENGINE_SINK_TYPE_PREVIEW: MF_CAPTURE_ENGINE_SINK_TYPE = 1
MF_CAPTURE_ENGINE_SINK_TYPE_PHOTO: MF_CAPTURE_ENGINE_SINK_TYPE = 2
MF_CAPTURE_ENGINE_SOURCE = UInt32
MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_PREVIEW: MF_CAPTURE_ENGINE_SOURCE = 4294967290
MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_RECORD: MF_CAPTURE_ENGINE_SOURCE = 4294967289
MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_PHOTO: MF_CAPTURE_ENGINE_SOURCE = 4294967288
MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_AUDIO: MF_CAPTURE_ENGINE_SOURCE = 4294967287
MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_METADATA: MF_CAPTURE_ENGINE_SOURCE = 4294967286
MF_CAPTURE_ENGINE_MEDIASOURCE: MF_CAPTURE_ENGINE_SOURCE = 4294967295
MF_CAPTURE_ENGINE_STREAM_CATEGORY = Int32
MF_CAPTURE_ENGINE_STREAM_CATEGORY_VIDEO_PREVIEW: MF_CAPTURE_ENGINE_STREAM_CATEGORY = 0
MF_CAPTURE_ENGINE_STREAM_CATEGORY_VIDEO_CAPTURE: MF_CAPTURE_ENGINE_STREAM_CATEGORY = 1
MF_CAPTURE_ENGINE_STREAM_CATEGORY_PHOTO_INDEPENDENT: MF_CAPTURE_ENGINE_STREAM_CATEGORY = 2
MF_CAPTURE_ENGINE_STREAM_CATEGORY_PHOTO_DEPENDENT: MF_CAPTURE_ENGINE_STREAM_CATEGORY = 3
MF_CAPTURE_ENGINE_STREAM_CATEGORY_AUDIO: MF_CAPTURE_ENGINE_STREAM_CATEGORY = 4
MF_CAPTURE_ENGINE_STREAM_CATEGORY_UNSUPPORTED: MF_CAPTURE_ENGINE_STREAM_CATEGORY = 5
MF_CAPTURE_ENGINE_STREAM_CATEGORY_METADATA: MF_CAPTURE_ENGINE_STREAM_CATEGORY = 6
MF_CONNECT_METHOD = Int32
MF_CONNECT_DIRECT: MF_CONNECT_METHOD = 0
MF_CONNECT_ALLOW_CONVERTER: MF_CONNECT_METHOD = 1
MF_CONNECT_ALLOW_DECODER: MF_CONNECT_METHOD = 3
MF_CONNECT_RESOLVE_INDEPENDENT_OUTPUTTYPES: MF_CONNECT_METHOD = 4
MF_CONNECT_AS_OPTIONAL: MF_CONNECT_METHOD = 65536
MF_CONNECT_AS_OPTIONAL_BRANCH: MF_CONNECT_METHOD = 131072
MF_CROSS_ORIGIN_POLICY = Int32
MF_CROSS_ORIGIN_POLICY_NONE: MF_CROSS_ORIGIN_POLICY = 0
MF_CROSS_ORIGIN_POLICY_ANONYMOUS: MF_CROSS_ORIGIN_POLICY = 1
MF_CROSS_ORIGIN_POLICY_USE_CREDENTIALS: MF_CROSS_ORIGIN_POLICY = 2
MF_CUSTOM_DECODE_UNIT_TYPE = Int32
MF_DECODE_UNIT_NAL: MF_CUSTOM_DECODE_UNIT_TYPE = 0
MF_DECODE_UNIT_SEI: MF_CUSTOM_DECODE_UNIT_TYPE = 1
MF_EVENT_TYPE = Int32
MF_EVENT_TYPE_MEUnknown: MF_EVENT_TYPE = 0
MF_EVENT_TYPE_MEError: MF_EVENT_TYPE = 1
MF_EVENT_TYPE_MEExtendedType: MF_EVENT_TYPE = 2
MF_EVENT_TYPE_MENonFatalError: MF_EVENT_TYPE = 3
MF_EVENT_TYPE_MEGenericV1Anchor: MF_EVENT_TYPE = 3
MF_EVENT_TYPE_MESessionUnknown: MF_EVENT_TYPE = 100
MF_EVENT_TYPE_MESessionTopologySet: MF_EVENT_TYPE = 101
MF_EVENT_TYPE_MESessionTopologiesCleared: MF_EVENT_TYPE = 102
MF_EVENT_TYPE_MESessionStarted: MF_EVENT_TYPE = 103
MF_EVENT_TYPE_MESessionPaused: MF_EVENT_TYPE = 104
MF_EVENT_TYPE_MESessionStopped: MF_EVENT_TYPE = 105
MF_EVENT_TYPE_MESessionClosed: MF_EVENT_TYPE = 106
MF_EVENT_TYPE_MESessionEnded: MF_EVENT_TYPE = 107
MF_EVENT_TYPE_MESessionRateChanged: MF_EVENT_TYPE = 108
MF_EVENT_TYPE_MESessionScrubSampleComplete: MF_EVENT_TYPE = 109
MF_EVENT_TYPE_MESessionCapabilitiesChanged: MF_EVENT_TYPE = 110
MF_EVENT_TYPE_MESessionTopologyStatus: MF_EVENT_TYPE = 111
MF_EVENT_TYPE_MESessionNotifyPresentationTime: MF_EVENT_TYPE = 112
MF_EVENT_TYPE_MENewPresentation: MF_EVENT_TYPE = 113
MF_EVENT_TYPE_MELicenseAcquisitionStart: MF_EVENT_TYPE = 114
MF_EVENT_TYPE_MELicenseAcquisitionCompleted: MF_EVENT_TYPE = 115
MF_EVENT_TYPE_MEIndividualizationStart: MF_EVENT_TYPE = 116
MF_EVENT_TYPE_MEIndividualizationCompleted: MF_EVENT_TYPE = 117
MF_EVENT_TYPE_MEEnablerProgress: MF_EVENT_TYPE = 118
MF_EVENT_TYPE_MEEnablerCompleted: MF_EVENT_TYPE = 119
MF_EVENT_TYPE_MEPolicyError: MF_EVENT_TYPE = 120
MF_EVENT_TYPE_MEPolicyReport: MF_EVENT_TYPE = 121
MF_EVENT_TYPE_MEBufferingStarted: MF_EVENT_TYPE = 122
MF_EVENT_TYPE_MEBufferingStopped: MF_EVENT_TYPE = 123
MF_EVENT_TYPE_MEConnectStart: MF_EVENT_TYPE = 124
MF_EVENT_TYPE_MEConnectEnd: MF_EVENT_TYPE = 125
MF_EVENT_TYPE_MEReconnectStart: MF_EVENT_TYPE = 126
MF_EVENT_TYPE_MEReconnectEnd: MF_EVENT_TYPE = 127
MF_EVENT_TYPE_MERendererEvent: MF_EVENT_TYPE = 128
MF_EVENT_TYPE_MESessionStreamSinkFormatChanged: MF_EVENT_TYPE = 129
MF_EVENT_TYPE_MESessionV1Anchor: MF_EVENT_TYPE = 129
MF_EVENT_TYPE_MESourceUnknown: MF_EVENT_TYPE = 200
MF_EVENT_TYPE_MESourceStarted: MF_EVENT_TYPE = 201
MF_EVENT_TYPE_MEStreamStarted: MF_EVENT_TYPE = 202
MF_EVENT_TYPE_MESourceSeeked: MF_EVENT_TYPE = 203
MF_EVENT_TYPE_MEStreamSeeked: MF_EVENT_TYPE = 204
MF_EVENT_TYPE_MENewStream: MF_EVENT_TYPE = 205
MF_EVENT_TYPE_MEUpdatedStream: MF_EVENT_TYPE = 206
MF_EVENT_TYPE_MESourceStopped: MF_EVENT_TYPE = 207
MF_EVENT_TYPE_MEStreamStopped: MF_EVENT_TYPE = 208
MF_EVENT_TYPE_MESourcePaused: MF_EVENT_TYPE = 209
MF_EVENT_TYPE_MEStreamPaused: MF_EVENT_TYPE = 210
MF_EVENT_TYPE_MEEndOfPresentation: MF_EVENT_TYPE = 211
MF_EVENT_TYPE_MEEndOfStream: MF_EVENT_TYPE = 212
MF_EVENT_TYPE_MEMediaSample: MF_EVENT_TYPE = 213
MF_EVENT_TYPE_MEStreamTick: MF_EVENT_TYPE = 214
MF_EVENT_TYPE_MEStreamThinMode: MF_EVENT_TYPE = 215
MF_EVENT_TYPE_MEStreamFormatChanged: MF_EVENT_TYPE = 216
MF_EVENT_TYPE_MESourceRateChanged: MF_EVENT_TYPE = 217
MF_EVENT_TYPE_MEEndOfPresentationSegment: MF_EVENT_TYPE = 218
MF_EVENT_TYPE_MESourceCharacteristicsChanged: MF_EVENT_TYPE = 219
MF_EVENT_TYPE_MESourceRateChangeRequested: MF_EVENT_TYPE = 220
MF_EVENT_TYPE_MESourceMetadataChanged: MF_EVENT_TYPE = 221
MF_EVENT_TYPE_MESequencerSourceTopologyUpdated: MF_EVENT_TYPE = 222
MF_EVENT_TYPE_MESourceV1Anchor: MF_EVENT_TYPE = 222
MF_EVENT_TYPE_MESinkUnknown: MF_EVENT_TYPE = 300
MF_EVENT_TYPE_MEStreamSinkStarted: MF_EVENT_TYPE = 301
MF_EVENT_TYPE_MEStreamSinkStopped: MF_EVENT_TYPE = 302
MF_EVENT_TYPE_MEStreamSinkPaused: MF_EVENT_TYPE = 303
MF_EVENT_TYPE_MEStreamSinkRateChanged: MF_EVENT_TYPE = 304
MF_EVENT_TYPE_MEStreamSinkRequestSample: MF_EVENT_TYPE = 305
MF_EVENT_TYPE_MEStreamSinkMarker: MF_EVENT_TYPE = 306
MF_EVENT_TYPE_MEStreamSinkPrerolled: MF_EVENT_TYPE = 307
MF_EVENT_TYPE_MEStreamSinkScrubSampleComplete: MF_EVENT_TYPE = 308
MF_EVENT_TYPE_MEStreamSinkFormatChanged: MF_EVENT_TYPE = 309
MF_EVENT_TYPE_MEStreamSinkDeviceChanged: MF_EVENT_TYPE = 310
MF_EVENT_TYPE_MEQualityNotify: MF_EVENT_TYPE = 311
MF_EVENT_TYPE_MESinkInvalidated: MF_EVENT_TYPE = 312
MF_EVENT_TYPE_MEAudioSessionNameChanged: MF_EVENT_TYPE = 313
MF_EVENT_TYPE_MEAudioSessionVolumeChanged: MF_EVENT_TYPE = 314
MF_EVENT_TYPE_MEAudioSessionDeviceRemoved: MF_EVENT_TYPE = 315
MF_EVENT_TYPE_MEAudioSessionServerShutdown: MF_EVENT_TYPE = 316
MF_EVENT_TYPE_MEAudioSessionGroupingParamChanged: MF_EVENT_TYPE = 317
MF_EVENT_TYPE_MEAudioSessionIconChanged: MF_EVENT_TYPE = 318
MF_EVENT_TYPE_MEAudioSessionFormatChanged: MF_EVENT_TYPE = 319
MF_EVENT_TYPE_MEAudioSessionDisconnected: MF_EVENT_TYPE = 320
MF_EVENT_TYPE_MEAudioSessionExclusiveModeOverride: MF_EVENT_TYPE = 321
MF_EVENT_TYPE_MESinkV1Anchor: MF_EVENT_TYPE = 321
MF_EVENT_TYPE_MECaptureAudioSessionVolumeChanged: MF_EVENT_TYPE = 322
MF_EVENT_TYPE_MECaptureAudioSessionDeviceRemoved: MF_EVENT_TYPE = 323
MF_EVENT_TYPE_MECaptureAudioSessionFormatChanged: MF_EVENT_TYPE = 324
MF_EVENT_TYPE_MECaptureAudioSessionDisconnected: MF_EVENT_TYPE = 325
MF_EVENT_TYPE_MECaptureAudioSessionExclusiveModeOverride: MF_EVENT_TYPE = 326
MF_EVENT_TYPE_MECaptureAudioSessionServerShutdown: MF_EVENT_TYPE = 327
MF_EVENT_TYPE_MESinkV2Anchor: MF_EVENT_TYPE = 327
MF_EVENT_TYPE_METrustUnknown: MF_EVENT_TYPE = 400
MF_EVENT_TYPE_MEPolicyChanged: MF_EVENT_TYPE = 401
MF_EVENT_TYPE_MEContentProtectionMessage: MF_EVENT_TYPE = 402
MF_EVENT_TYPE_MEPolicySet: MF_EVENT_TYPE = 403
MF_EVENT_TYPE_METrustV1Anchor: MF_EVENT_TYPE = 403
MF_EVENT_TYPE_MEWMDRMLicenseBackupCompleted: MF_EVENT_TYPE = 500
MF_EVENT_TYPE_MEWMDRMLicenseBackupProgress: MF_EVENT_TYPE = 501
MF_EVENT_TYPE_MEWMDRMLicenseRestoreCompleted: MF_EVENT_TYPE = 502
MF_EVENT_TYPE_MEWMDRMLicenseRestoreProgress: MF_EVENT_TYPE = 503
MF_EVENT_TYPE_MEWMDRMLicenseAcquisitionCompleted: MF_EVENT_TYPE = 506
MF_EVENT_TYPE_MEWMDRMIndividualizationCompleted: MF_EVENT_TYPE = 508
MF_EVENT_TYPE_MEWMDRMIndividualizationProgress: MF_EVENT_TYPE = 513
MF_EVENT_TYPE_MEWMDRMProximityCompleted: MF_EVENT_TYPE = 514
MF_EVENT_TYPE_MEWMDRMLicenseStoreCleaned: MF_EVENT_TYPE = 515
MF_EVENT_TYPE_MEWMDRMRevocationDownloadCompleted: MF_EVENT_TYPE = 516
MF_EVENT_TYPE_MEWMDRMV1Anchor: MF_EVENT_TYPE = 516
MF_EVENT_TYPE_METransformUnknown: MF_EVENT_TYPE = 600
MF_EVENT_TYPE_METransformNeedInput: MF_EVENT_TYPE = 601
MF_EVENT_TYPE_METransformHaveOutput: MF_EVENT_TYPE = 602
MF_EVENT_TYPE_METransformDrainComplete: MF_EVENT_TYPE = 603
MF_EVENT_TYPE_METransformMarker: MF_EVENT_TYPE = 604
MF_EVENT_TYPE_METransformInputStreamStateChanged: MF_EVENT_TYPE = 605
MF_EVENT_TYPE_MEByteStreamCharacteristicsChanged: MF_EVENT_TYPE = 700
MF_EVENT_TYPE_MEVideoCaptureDeviceRemoved: MF_EVENT_TYPE = 800
MF_EVENT_TYPE_MEVideoCaptureDevicePreempted: MF_EVENT_TYPE = 801
MF_EVENT_TYPE_MEStreamSinkFormatInvalidated: MF_EVENT_TYPE = 802
MF_EVENT_TYPE_MEEncodingParameters: MF_EVENT_TYPE = 803
MF_EVENT_TYPE_MEContentProtectionMetadata: MF_EVENT_TYPE = 900
MF_EVENT_TYPE_MEDeviceThermalStateChanged: MF_EVENT_TYPE = 950
MF_EVENT_TYPE_MEReservedMax: MF_EVENT_TYPE = 10000
MF_FILE_ACCESSMODE = Int32
MF_ACCESSMODE_READ: MF_FILE_ACCESSMODE = 1
MF_ACCESSMODE_WRITE: MF_FILE_ACCESSMODE = 2
MF_ACCESSMODE_READWRITE: MF_FILE_ACCESSMODE = 3
MF_FILE_FLAGS = Int32
MF_FILEFLAGS_NONE: MF_FILE_FLAGS = 0
MF_FILEFLAGS_NOBUFFERING: MF_FILE_FLAGS = 1
MF_FILEFLAGS_ALLOW_WRITE_SHARING: MF_FILE_FLAGS = 2
MF_FILE_OPENMODE = Int32
MF_OPENMODE_FAIL_IF_NOT_EXIST: MF_FILE_OPENMODE = 0
MF_OPENMODE_FAIL_IF_EXIST: MF_FILE_OPENMODE = 1
MF_OPENMODE_RESET_IF_EXIST: MF_FILE_OPENMODE = 2
MF_OPENMODE_APPEND_IF_EXIST: MF_FILE_OPENMODE = 3
MF_OPENMODE_DELETE_IF_EXIST: MF_FILE_OPENMODE = 4
class MF_FLOAT2(EasyCastStructure):
    x: Single
    y: Single
class MF_FLOAT3(EasyCastStructure):
    x: Single
    y: Single
    z: Single
MF_HDCP_STATUS = Int32
MF_HDCP_STATUS_ON: MF_HDCP_STATUS = 0
MF_HDCP_STATUS_OFF: MF_HDCP_STATUS = 1
MF_HDCP_STATUS_ON_WITH_TYPE_ENFORCEMENT: MF_HDCP_STATUS = 2
class MF_LEAKY_BUCKET_PAIR(EasyCastStructure):
    dwBitrate: UInt32
    msBufferWindow: UInt32
MF_MEDIAKEYSESSION_MESSAGETYPE = Int32
MF_MEDIAKEYSESSION_MESSAGETYPE_LICENSE_REQUEST: MF_MEDIAKEYSESSION_MESSAGETYPE = 0
MF_MEDIAKEYSESSION_MESSAGETYPE_LICENSE_RENEWAL: MF_MEDIAKEYSESSION_MESSAGETYPE = 1
MF_MEDIAKEYSESSION_MESSAGETYPE_LICENSE_RELEASE: MF_MEDIAKEYSESSION_MESSAGETYPE = 2
MF_MEDIAKEYSESSION_MESSAGETYPE_INDIVIDUALIZATION_REQUEST: MF_MEDIAKEYSESSION_MESSAGETYPE = 3
MF_MEDIAKEYSESSION_TYPE = Int32
MF_MEDIAKEYSESSION_TYPE_TEMPORARY: MF_MEDIAKEYSESSION_TYPE = 0
MF_MEDIAKEYSESSION_TYPE_PERSISTENT_LICENSE: MF_MEDIAKEYSESSION_TYPE = 1
MF_MEDIAKEYSESSION_TYPE_PERSISTENT_RELEASE_MESSAGE: MF_MEDIAKEYSESSION_TYPE = 2
MF_MEDIAKEYSESSION_TYPE_PERSISTENT_USAGE_RECORD: MF_MEDIAKEYSESSION_TYPE = 3
MF_MEDIAKEYS_REQUIREMENT = Int32
MF_MEDIAKEYS_REQUIREMENT_REQUIRED: MF_MEDIAKEYS_REQUIREMENT = 1
MF_MEDIAKEYS_REQUIREMENT_OPTIONAL: MF_MEDIAKEYS_REQUIREMENT = 2
MF_MEDIAKEYS_REQUIREMENT_NOT_ALLOWED: MF_MEDIAKEYS_REQUIREMENT = 3
MF_MEDIAKEY_STATUS = Int32
MF_MEDIAKEY_STATUS_USABLE: MF_MEDIAKEY_STATUS = 0
MF_MEDIAKEY_STATUS_EXPIRED: MF_MEDIAKEY_STATUS = 1
MF_MEDIAKEY_STATUS_OUTPUT_DOWNSCALED: MF_MEDIAKEY_STATUS = 2
MF_MEDIAKEY_STATUS_OUTPUT_NOT_ALLOWED: MF_MEDIAKEY_STATUS = 3
MF_MEDIAKEY_STATUS_STATUS_PENDING: MF_MEDIAKEY_STATUS = 4
MF_MEDIAKEY_STATUS_INTERNAL_ERROR: MF_MEDIAKEY_STATUS = 5
MF_MEDIAKEY_STATUS_RELEASED: MF_MEDIAKEY_STATUS = 6
MF_MEDIAKEY_STATUS_OUTPUT_RESTRICTED: MF_MEDIAKEY_STATUS = 7
MF_MEDIA_ENGINE_CANPLAY = Int32
MF_MEDIA_ENGINE_CANPLAY_NOT_SUPPORTED: MF_MEDIA_ENGINE_CANPLAY = 0
MF_MEDIA_ENGINE_CANPLAY_MAYBE: MF_MEDIA_ENGINE_CANPLAY = 1
MF_MEDIA_ENGINE_CANPLAY_PROBABLY: MF_MEDIA_ENGINE_CANPLAY = 2
MF_MEDIA_ENGINE_CREATEFLAGS = Int32
MF_MEDIA_ENGINE_AUDIOONLY: MF_MEDIA_ENGINE_CREATEFLAGS = 1
MF_MEDIA_ENGINE_WAITFORSTABLE_STATE: MF_MEDIA_ENGINE_CREATEFLAGS = 2
MF_MEDIA_ENGINE_FORCEMUTE: MF_MEDIA_ENGINE_CREATEFLAGS = 4
MF_MEDIA_ENGINE_REAL_TIME_MODE: MF_MEDIA_ENGINE_CREATEFLAGS = 8
MF_MEDIA_ENGINE_DISABLE_LOCAL_PLUGINS: MF_MEDIA_ENGINE_CREATEFLAGS = 16
MF_MEDIA_ENGINE_CREATEFLAGS_MASK: MF_MEDIA_ENGINE_CREATEFLAGS = 31
MF_MEDIA_ENGINE_ERR = Int32
MF_MEDIA_ENGINE_ERR_NOERROR: MF_MEDIA_ENGINE_ERR = 0
MF_MEDIA_ENGINE_ERR_ABORTED: MF_MEDIA_ENGINE_ERR = 1
MF_MEDIA_ENGINE_ERR_NETWORK: MF_MEDIA_ENGINE_ERR = 2
MF_MEDIA_ENGINE_ERR_DECODE: MF_MEDIA_ENGINE_ERR = 3
MF_MEDIA_ENGINE_ERR_SRC_NOT_SUPPORTED: MF_MEDIA_ENGINE_ERR = 4
MF_MEDIA_ENGINE_ERR_ENCRYPTED: MF_MEDIA_ENGINE_ERR = 5
MF_MEDIA_ENGINE_EVENT = Int32
MF_MEDIA_ENGINE_EVENT_LOADSTART: MF_MEDIA_ENGINE_EVENT = 1
MF_MEDIA_ENGINE_EVENT_PROGRESS: MF_MEDIA_ENGINE_EVENT = 2
MF_MEDIA_ENGINE_EVENT_SUSPEND: MF_MEDIA_ENGINE_EVENT = 3
MF_MEDIA_ENGINE_EVENT_ABORT: MF_MEDIA_ENGINE_EVENT = 4
MF_MEDIA_ENGINE_EVENT_ERROR: MF_MEDIA_ENGINE_EVENT = 5
MF_MEDIA_ENGINE_EVENT_EMPTIED: MF_MEDIA_ENGINE_EVENT = 6
MF_MEDIA_ENGINE_EVENT_STALLED: MF_MEDIA_ENGINE_EVENT = 7
MF_MEDIA_ENGINE_EVENT_PLAY: MF_MEDIA_ENGINE_EVENT = 8
MF_MEDIA_ENGINE_EVENT_PAUSE: MF_MEDIA_ENGINE_EVENT = 9
MF_MEDIA_ENGINE_EVENT_LOADEDMETADATA: MF_MEDIA_ENGINE_EVENT = 10
MF_MEDIA_ENGINE_EVENT_LOADEDDATA: MF_MEDIA_ENGINE_EVENT = 11
MF_MEDIA_ENGINE_EVENT_WAITING: MF_MEDIA_ENGINE_EVENT = 12
MF_MEDIA_ENGINE_EVENT_PLAYING: MF_MEDIA_ENGINE_EVENT = 13
MF_MEDIA_ENGINE_EVENT_CANPLAY: MF_MEDIA_ENGINE_EVENT = 14
MF_MEDIA_ENGINE_EVENT_CANPLAYTHROUGH: MF_MEDIA_ENGINE_EVENT = 15
MF_MEDIA_ENGINE_EVENT_SEEKING: MF_MEDIA_ENGINE_EVENT = 16
MF_MEDIA_ENGINE_EVENT_SEEKED: MF_MEDIA_ENGINE_EVENT = 17
MF_MEDIA_ENGINE_EVENT_TIMEUPDATE: MF_MEDIA_ENGINE_EVENT = 18
MF_MEDIA_ENGINE_EVENT_ENDED: MF_MEDIA_ENGINE_EVENT = 19
MF_MEDIA_ENGINE_EVENT_RATECHANGE: MF_MEDIA_ENGINE_EVENT = 20
MF_MEDIA_ENGINE_EVENT_DURATIONCHANGE: MF_MEDIA_ENGINE_EVENT = 21
MF_MEDIA_ENGINE_EVENT_VOLUMECHANGE: MF_MEDIA_ENGINE_EVENT = 22
MF_MEDIA_ENGINE_EVENT_FORMATCHANGE: MF_MEDIA_ENGINE_EVENT = 1000
MF_MEDIA_ENGINE_EVENT_PURGEQUEUEDEVENTS: MF_MEDIA_ENGINE_EVENT = 1001
MF_MEDIA_ENGINE_EVENT_TIMELINE_MARKER: MF_MEDIA_ENGINE_EVENT = 1002
MF_MEDIA_ENGINE_EVENT_BALANCECHANGE: MF_MEDIA_ENGINE_EVENT = 1003
MF_MEDIA_ENGINE_EVENT_DOWNLOADCOMPLETE: MF_MEDIA_ENGINE_EVENT = 1004
MF_MEDIA_ENGINE_EVENT_BUFFERINGSTARTED: MF_MEDIA_ENGINE_EVENT = 1005
MF_MEDIA_ENGINE_EVENT_BUFFERINGENDED: MF_MEDIA_ENGINE_EVENT = 1006
MF_MEDIA_ENGINE_EVENT_FRAMESTEPCOMPLETED: MF_MEDIA_ENGINE_EVENT = 1007
MF_MEDIA_ENGINE_EVENT_NOTIFYSTABLESTATE: MF_MEDIA_ENGINE_EVENT = 1008
MF_MEDIA_ENGINE_EVENT_FIRSTFRAMEREADY: MF_MEDIA_ENGINE_EVENT = 1009
MF_MEDIA_ENGINE_EVENT_TRACKSCHANGE: MF_MEDIA_ENGINE_EVENT = 1010
MF_MEDIA_ENGINE_EVENT_OPMINFO: MF_MEDIA_ENGINE_EVENT = 1011
MF_MEDIA_ENGINE_EVENT_RESOURCELOST: MF_MEDIA_ENGINE_EVENT = 1012
MF_MEDIA_ENGINE_EVENT_DELAYLOADEVENT_CHANGED: MF_MEDIA_ENGINE_EVENT = 1013
MF_MEDIA_ENGINE_EVENT_STREAMRENDERINGERROR: MF_MEDIA_ENGINE_EVENT = 1014
MF_MEDIA_ENGINE_EVENT_SUPPORTEDRATES_CHANGED: MF_MEDIA_ENGINE_EVENT = 1015
MF_MEDIA_ENGINE_EVENT_AUDIOENDPOINTCHANGE: MF_MEDIA_ENGINE_EVENT = 1016
MF_MEDIA_ENGINE_EXTENSION_TYPE = Int32
MF_MEDIA_ENGINE_EXTENSION_TYPE_MEDIASOURCE: MF_MEDIA_ENGINE_EXTENSION_TYPE = 0
MF_MEDIA_ENGINE_EXTENSION_TYPE_BYTESTREAM: MF_MEDIA_ENGINE_EXTENSION_TYPE = 1
MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS = Int32
MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_PROTECTED: MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS = 1
MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_SURFACE_PROTECTION: MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS = 2
MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_ANTI_SCREEN_SCRAPE_PROTECTION: MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS = 4
MF_MEDIA_ENGINE_KEYERR = Int32
MF_MEDIAENGINE_KEYERR_UNKNOWN: MF_MEDIA_ENGINE_KEYERR = 1
MF_MEDIAENGINE_KEYERR_CLIENT: MF_MEDIA_ENGINE_KEYERR = 2
MF_MEDIAENGINE_KEYERR_SERVICE: MF_MEDIA_ENGINE_KEYERR = 3
MF_MEDIAENGINE_KEYERR_OUTPUT: MF_MEDIA_ENGINE_KEYERR = 4
MF_MEDIAENGINE_KEYERR_HARDWARECHANGE: MF_MEDIA_ENGINE_KEYERR = 5
MF_MEDIAENGINE_KEYERR_DOMAIN: MF_MEDIA_ENGINE_KEYERR = 6
MF_MEDIA_ENGINE_NETWORK = Int32
MF_MEDIA_ENGINE_NETWORK_EMPTY: MF_MEDIA_ENGINE_NETWORK = 0
MF_MEDIA_ENGINE_NETWORK_IDLE: MF_MEDIA_ENGINE_NETWORK = 1
MF_MEDIA_ENGINE_NETWORK_LOADING: MF_MEDIA_ENGINE_NETWORK = 2
MF_MEDIA_ENGINE_NETWORK_NO_SOURCE: MF_MEDIA_ENGINE_NETWORK = 3
MF_MEDIA_ENGINE_OPM_STATUS = Int32
MF_MEDIA_ENGINE_OPM_NOT_REQUESTED: MF_MEDIA_ENGINE_OPM_STATUS = 0
MF_MEDIA_ENGINE_OPM_ESTABLISHED: MF_MEDIA_ENGINE_OPM_STATUS = 1
MF_MEDIA_ENGINE_OPM_FAILED_VM: MF_MEDIA_ENGINE_OPM_STATUS = 2
MF_MEDIA_ENGINE_OPM_FAILED_BDA: MF_MEDIA_ENGINE_OPM_STATUS = 3
MF_MEDIA_ENGINE_OPM_FAILED_UNSIGNED_DRIVER: MF_MEDIA_ENGINE_OPM_STATUS = 4
MF_MEDIA_ENGINE_OPM_FAILED: MF_MEDIA_ENGINE_OPM_STATUS = 5
MF_MEDIA_ENGINE_PRELOAD = Int32
MF_MEDIA_ENGINE_PRELOAD_MISSING: MF_MEDIA_ENGINE_PRELOAD = 0
MF_MEDIA_ENGINE_PRELOAD_EMPTY: MF_MEDIA_ENGINE_PRELOAD = 1
MF_MEDIA_ENGINE_PRELOAD_NONE: MF_MEDIA_ENGINE_PRELOAD = 2
MF_MEDIA_ENGINE_PRELOAD_METADATA: MF_MEDIA_ENGINE_PRELOAD = 3
MF_MEDIA_ENGINE_PRELOAD_AUTOMATIC: MF_MEDIA_ENGINE_PRELOAD = 4
MF_MEDIA_ENGINE_PROTECTION_FLAGS = Int32
MF_MEDIA_ENGINE_ENABLE_PROTECTED_CONTENT: MF_MEDIA_ENGINE_PROTECTION_FLAGS = 1
MF_MEDIA_ENGINE_USE_PMP_FOR_ALL_CONTENT: MF_MEDIA_ENGINE_PROTECTION_FLAGS = 2
MF_MEDIA_ENGINE_USE_UNPROTECTED_PMP: MF_MEDIA_ENGINE_PROTECTION_FLAGS = 4
MF_MEDIA_ENGINE_READY = Int32
MF_MEDIA_ENGINE_READY_HAVE_NOTHING: MF_MEDIA_ENGINE_READY = 0
MF_MEDIA_ENGINE_READY_HAVE_METADATA: MF_MEDIA_ENGINE_READY = 1
MF_MEDIA_ENGINE_READY_HAVE_CURRENT_DATA: MF_MEDIA_ENGINE_READY = 2
MF_MEDIA_ENGINE_READY_HAVE_FUTURE_DATA: MF_MEDIA_ENGINE_READY = 3
MF_MEDIA_ENGINE_READY_HAVE_ENOUGH_DATA: MF_MEDIA_ENGINE_READY = 4
MF_MEDIA_ENGINE_S3D_PACKING_MODE = Int32
MF_MEDIA_ENGINE_S3D_PACKING_MODE_NONE: MF_MEDIA_ENGINE_S3D_PACKING_MODE = 0
MF_MEDIA_ENGINE_S3D_PACKING_MODE_SIDE_BY_SIDE: MF_MEDIA_ENGINE_S3D_PACKING_MODE = 1
MF_MEDIA_ENGINE_S3D_PACKING_MODE_TOP_BOTTOM: MF_MEDIA_ENGINE_S3D_PACKING_MODE = 2
MF_MEDIA_ENGINE_SEEK_MODE = Int32
MF_MEDIA_ENGINE_SEEK_MODE_NORMAL: MF_MEDIA_ENGINE_SEEK_MODE = 0
MF_MEDIA_ENGINE_SEEK_MODE_APPROXIMATE: MF_MEDIA_ENGINE_SEEK_MODE = 1
MF_MEDIA_ENGINE_STATISTIC = Int32
MF_MEDIA_ENGINE_STATISTIC_FRAMES_RENDERED: MF_MEDIA_ENGINE_STATISTIC = 0
MF_MEDIA_ENGINE_STATISTIC_FRAMES_DROPPED: MF_MEDIA_ENGINE_STATISTIC = 1
MF_MEDIA_ENGINE_STATISTIC_BYTES_DOWNLOADED: MF_MEDIA_ENGINE_STATISTIC = 2
MF_MEDIA_ENGINE_STATISTIC_BUFFER_PROGRESS: MF_MEDIA_ENGINE_STATISTIC = 3
MF_MEDIA_ENGINE_STATISTIC_FRAMES_PER_SECOND: MF_MEDIA_ENGINE_STATISTIC = 4
MF_MEDIA_ENGINE_STATISTIC_PLAYBACK_JITTER: MF_MEDIA_ENGINE_STATISTIC = 5
MF_MEDIA_ENGINE_STATISTIC_FRAMES_CORRUPTED: MF_MEDIA_ENGINE_STATISTIC = 6
MF_MEDIA_ENGINE_STATISTIC_TOTAL_FRAME_DELAY: MF_MEDIA_ENGINE_STATISTIC = 7
MF_MEDIA_ENGINE_STREAMTYPE_FAILED = Int32
MF_MEDIA_ENGINE_STREAMTYPE_FAILED_UNKNOWN: MF_MEDIA_ENGINE_STREAMTYPE_FAILED = 0
MF_MEDIA_ENGINE_STREAMTYPE_FAILED_AUDIO: MF_MEDIA_ENGINE_STREAMTYPE_FAILED = 1
MF_MEDIA_ENGINE_STREAMTYPE_FAILED_VIDEO: MF_MEDIA_ENGINE_STREAMTYPE_FAILED = 2
MF_MEDIA_SHARING_ENGINE_EVENT = Int32
MF_MEDIA_SHARING_ENGINE_EVENT_DISCONNECT: MF_MEDIA_SHARING_ENGINE_EVENT = 2000
MF_MSE_APPEND_MODE = Int32
MF_MSE_APPEND_MODE_SEGMENTS: MF_MSE_APPEND_MODE = 0
MF_MSE_APPEND_MODE_SEQUENCE: MF_MSE_APPEND_MODE = 1
MF_MSE_ERROR = Int32
MF_MSE_ERROR_NOERROR: MF_MSE_ERROR = 0
MF_MSE_ERROR_NETWORK: MF_MSE_ERROR = 1
MF_MSE_ERROR_DECODE: MF_MSE_ERROR = 2
MF_MSE_ERROR_UNKNOWN_ERROR: MF_MSE_ERROR = 3
MF_MSE_OPUS_SUPPORT_TYPE = Int32
MF_MSE_OPUS_SUPPORT_ON: MF_MSE_OPUS_SUPPORT_TYPE = 0
MF_MSE_OPUS_SUPPORT_OFF: MF_MSE_OPUS_SUPPORT_TYPE = 1
MF_MSE_READY = Int32
MF_MSE_READY_CLOSED: MF_MSE_READY = 1
MF_MSE_READY_OPEN: MF_MSE_READY = 2
MF_MSE_READY_ENDED: MF_MSE_READY = 3
MF_MSE_VP9_SUPPORT_TYPE = Int32
MF_MSE_VP9_SUPPORT_DEFAULT: MF_MSE_VP9_SUPPORT_TYPE = 0
MF_MSE_VP9_SUPPORT_ON: MF_MSE_VP9_SUPPORT_TYPE = 1
MF_MSE_VP9_SUPPORT_OFF: MF_MSE_VP9_SUPPORT_TYPE = 2
MF_MT_D3D_RESOURCE_VERSION_ENUM = Int32
MF_D3D11_RESOURCE: MF_MT_D3D_RESOURCE_VERSION_ENUM = 0
MF_D3D12_RESOURCE: MF_MT_D3D_RESOURCE_VERSION_ENUM = 1
MF_OBJECT_TYPE = Int32
MF_OBJECT_MEDIASOURCE: MF_OBJECT_TYPE = 0
MF_OBJECT_BYTESTREAM: MF_OBJECT_TYPE = 1
MF_OBJECT_INVALID: MF_OBJECT_TYPE = 2
MF_OPM_ACP_PROTECTION_LEVEL = Int32
MF_OPM_ACP_OFF: MF_OPM_ACP_PROTECTION_LEVEL = 0
MF_OPM_ACP_LEVEL_ONE: MF_OPM_ACP_PROTECTION_LEVEL = 1
MF_OPM_ACP_LEVEL_TWO: MF_OPM_ACP_PROTECTION_LEVEL = 2
MF_OPM_ACP_LEVEL_THREE: MF_OPM_ACP_PROTECTION_LEVEL = 3
MF_OPM_ACP_FORCE_ULONG: MF_OPM_ACP_PROTECTION_LEVEL = 2147483647
MF_OPM_CGMSA_PROTECTION_LEVEL = Int32
MF_OPM_CGMSA_OFF: MF_OPM_CGMSA_PROTECTION_LEVEL = 0
MF_OPM_CGMSA_COPY_FREELY: MF_OPM_CGMSA_PROTECTION_LEVEL = 1
MF_OPM_CGMSA_COPY_NO_MORE: MF_OPM_CGMSA_PROTECTION_LEVEL = 2
MF_OPM_CGMSA_COPY_ONE_GENERATION: MF_OPM_CGMSA_PROTECTION_LEVEL = 3
MF_OPM_CGMSA_COPY_NEVER: MF_OPM_CGMSA_PROTECTION_LEVEL = 4
MF_OPM_CGMSA_REDISTRIBUTION_CONTROL_REQUIRED: MF_OPM_CGMSA_PROTECTION_LEVEL = 8
MF_PLUGIN_CONTROL_POLICY = Int32
MF_PLUGIN_CONTROL_POLICY_USE_ALL_PLUGINS: MF_PLUGIN_CONTROL_POLICY = 0
MF_PLUGIN_CONTROL_POLICY_USE_APPROVED_PLUGINS: MF_PLUGIN_CONTROL_POLICY = 1
MF_PLUGIN_CONTROL_POLICY_USE_WEB_PLUGINS: MF_PLUGIN_CONTROL_POLICY = 2
MF_PLUGIN_CONTROL_POLICY_USE_WEB_PLUGINS_EDGEMODE: MF_PLUGIN_CONTROL_POLICY = 3
MF_Plugin_Type = Int32
MF_Plugin_Type_MFT: MF_Plugin_Type = 0
MF_Plugin_Type_MediaSource: MF_Plugin_Type = 1
MF_Plugin_Type_MFT_MatchOutputType: MF_Plugin_Type = 2
MF_Plugin_Type_Other: MF_Plugin_Type = -1
MF_QUALITY_ADVISE_FLAGS = Int32
MF_QUALITY_CANNOT_KEEP_UP: MF_QUALITY_ADVISE_FLAGS = 1
MF_QUALITY_DROP_MODE = Int32
MF_DROP_MODE_NONE: MF_QUALITY_DROP_MODE = 0
MF_DROP_MODE_1: MF_QUALITY_DROP_MODE = 1
MF_DROP_MODE_2: MF_QUALITY_DROP_MODE = 2
MF_DROP_MODE_3: MF_QUALITY_DROP_MODE = 3
MF_DROP_MODE_4: MF_QUALITY_DROP_MODE = 4
MF_DROP_MODE_5: MF_QUALITY_DROP_MODE = 5
MF_NUM_DROP_MODES: MF_QUALITY_DROP_MODE = 6
MF_QUALITY_LEVEL = Int32
MF_QUALITY_NORMAL: MF_QUALITY_LEVEL = 0
MF_QUALITY_NORMAL_MINUS_1: MF_QUALITY_LEVEL = 1
MF_QUALITY_NORMAL_MINUS_2: MF_QUALITY_LEVEL = 2
MF_QUALITY_NORMAL_MINUS_3: MF_QUALITY_LEVEL = 3
MF_QUALITY_NORMAL_MINUS_4: MF_QUALITY_LEVEL = 4
MF_QUALITY_NORMAL_MINUS_5: MF_QUALITY_LEVEL = 5
MF_NUM_QUALITY_LEVELS: MF_QUALITY_LEVEL = 6
class MF_QUATERNION(EasyCastStructure):
    x: Single
    y: Single
    z: Single
    w: Single
MF_RESOLUTION_FLAGS = Int32
MF_RESOLUTION_MEDIASOURCE: MF_RESOLUTION_FLAGS = 1
MF_RESOLUTION_BYTESTREAM: MF_RESOLUTION_FLAGS = 2
MF_RESOLUTION_CONTENT_DOES_NOT_HAVE_TO_MATCH_EXTENSION_OR_MIME_TYPE: MF_RESOLUTION_FLAGS = 16
MF_RESOLUTION_KEEP_BYTE_STREAM_ALIVE_ON_FAIL: MF_RESOLUTION_FLAGS = 32
MF_RESOLUTION_DISABLE_LOCAL_PLUGINS: MF_RESOLUTION_FLAGS = 64
MF_RESOLUTION_PLUGIN_CONTROL_POLICY_APPROVED_ONLY: MF_RESOLUTION_FLAGS = 128
MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY: MF_RESOLUTION_FLAGS = 256
MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY_EDGEMODE: MF_RESOLUTION_FLAGS = 512
MF_RESOLUTION_ENABLE_STORE_PLUGINS: MF_RESOLUTION_FLAGS = 1024
MF_RESOLUTION_READ: MF_RESOLUTION_FLAGS = 65536
MF_RESOLUTION_WRITE: MF_RESOLUTION_FLAGS = 131072
MF_SERVICE_LOOKUP_TYPE = Int32
MF_SERVICE_LOOKUP_UPSTREAM: MF_SERVICE_LOOKUP_TYPE = 0
MF_SERVICE_LOOKUP_UPSTREAM_DIRECT: MF_SERVICE_LOOKUP_TYPE = 1
MF_SERVICE_LOOKUP_DOWNSTREAM: MF_SERVICE_LOOKUP_TYPE = 2
MF_SERVICE_LOOKUP_DOWNSTREAM_DIRECT: MF_SERVICE_LOOKUP_TYPE = 3
MF_SERVICE_LOOKUP_ALL: MF_SERVICE_LOOKUP_TYPE = 4
MF_SERVICE_LOOKUP_GLOBAL: MF_SERVICE_LOOKUP_TYPE = 5
MF_SHARING_ENGINE_EVENT = Int32
MF_SHARING_ENGINE_EVENT_DISCONNECT: MF_SHARING_ENGINE_EVENT = 2000
MF_SHARING_ENGINE_EVENT_LOCALRENDERINGSTARTED: MF_SHARING_ENGINE_EVENT = 2001
MF_SHARING_ENGINE_EVENT_LOCALRENDERINGENDED: MF_SHARING_ENGINE_EVENT = 2002
MF_SHARING_ENGINE_EVENT_STOPPED: MF_SHARING_ENGINE_EVENT = 2003
MF_SHARING_ENGINE_EVENT_ERROR: MF_SHARING_ENGINE_EVENT = 2501
MF_SINK_WRITER_CONSTANTS = UInt32
MF_SINK_WRITER_INVALID_STREAM_INDEX: MF_SINK_WRITER_CONSTANTS = 4294967295
MF_SINK_WRITER_ALL_STREAMS: MF_SINK_WRITER_CONSTANTS = 4294967294
MF_SINK_WRITER_MEDIASINK: MF_SINK_WRITER_CONSTANTS = 4294967295
class MF_SINK_WRITER_STATISTICS(EasyCastStructure):
    cb: UInt32
    llLastTimestampReceived: Int64
    llLastTimestampEncoded: Int64
    llLastTimestampProcessed: Int64
    llLastStreamTickReceived: Int64
    llLastSinkSampleRequest: Int64
    qwNumSamplesReceived: UInt64
    qwNumSamplesEncoded: UInt64
    qwNumSamplesProcessed: UInt64
    qwNumStreamTicksReceived: UInt64
    dwByteCountQueued: UInt32
    qwByteCountProcessed: UInt64
    dwNumOutstandingSinkSampleRequests: UInt32
    dwAverageSampleRateReceived: UInt32
    dwAverageSampleRateEncoded: UInt32
    dwAverageSampleRateProcessed: UInt32
MF_SOURCE_READER_CONSTANTS = Int32
MF_SOURCE_READER_INVALID_STREAM_INDEX: MF_SOURCE_READER_CONSTANTS = -1
MF_SOURCE_READER_ALL_STREAMS: MF_SOURCE_READER_CONSTANTS = -2
MF_SOURCE_READER_ANY_STREAM: MF_SOURCE_READER_CONSTANTS = -2
MF_SOURCE_READER_FIRST_AUDIO_STREAM: MF_SOURCE_READER_CONSTANTS = -3
MF_SOURCE_READER_FIRST_VIDEO_STREAM: MF_SOURCE_READER_CONSTANTS = -4
MF_SOURCE_READER_MEDIASOURCE: MF_SOURCE_READER_CONSTANTS = -1
MF_SOURCE_READER_CONTROL_FLAG = Int32
MF_SOURCE_READER_CONTROLF_DRAIN: MF_SOURCE_READER_CONTROL_FLAG = 1
MF_SOURCE_READER_CURRENT_TYPE_CONSTANTS = Int32
MF_SOURCE_READER_CURRENT_TYPE_INDEX: MF_SOURCE_READER_CURRENT_TYPE_CONSTANTS = -1
MF_SOURCE_READER_FLAG = Int32
MF_SOURCE_READERF_ERROR: MF_SOURCE_READER_FLAG = 1
MF_SOURCE_READERF_ENDOFSTREAM: MF_SOURCE_READER_FLAG = 2
MF_SOURCE_READERF_NEWSTREAM: MF_SOURCE_READER_FLAG = 4
MF_SOURCE_READERF_NATIVEMEDIATYPECHANGED: MF_SOURCE_READER_FLAG = 16
MF_SOURCE_READERF_CURRENTMEDIATYPECHANGED: MF_SOURCE_READER_FLAG = 32
MF_SOURCE_READERF_STREAMTICK: MF_SOURCE_READER_FLAG = 256
MF_SOURCE_READERF_ALLEFFECTSREMOVED: MF_SOURCE_READER_FLAG = 512
MF_STREAM_STATE = Int32
MF_STREAM_STATE_STOPPED: MF_STREAM_STATE = 0
MF_STREAM_STATE_PAUSED: MF_STREAM_STATE = 1
MF_STREAM_STATE_RUNNING: MF_STREAM_STATE = 2
MF_TIMED_TEXT_ALIGNMENT = Int32
MF_TIMED_TEXT_ALIGNMENT_START: MF_TIMED_TEXT_ALIGNMENT = 0
MF_TIMED_TEXT_ALIGNMENT_END: MF_TIMED_TEXT_ALIGNMENT = 1
MF_TIMED_TEXT_ALIGNMENT_CENTER: MF_TIMED_TEXT_ALIGNMENT = 2
MF_TIMED_TEXT_BOUTEN_POSITION = Int32
MF_TIMED_TEXT_BOUTEN_POSITION_BEFORE: MF_TIMED_TEXT_BOUTEN_POSITION = 0
MF_TIMED_TEXT_BOUTEN_POSITION_AFTER: MF_TIMED_TEXT_BOUTEN_POSITION = 1
MF_TIMED_TEXT_BOUTEN_POSITION_OUTSIDE: MF_TIMED_TEXT_BOUTEN_POSITION = 2
MF_TIMED_TEXT_BOUTEN_TYPE = Int32
MF_TIMED_TEXT_BOUTEN_TYPE_NONE: MF_TIMED_TEXT_BOUTEN_TYPE = 0
MF_TIMED_TEXT_BOUTEN_TYPE_AUTO: MF_TIMED_TEXT_BOUTEN_TYPE = 1
MF_TIMED_TEXT_BOUTEN_TYPE_FILLEDCIRCLE: MF_TIMED_TEXT_BOUTEN_TYPE = 2
MF_TIMED_TEXT_BOUTEN_TYPE_OPENCIRCLE: MF_TIMED_TEXT_BOUTEN_TYPE = 3
MF_TIMED_TEXT_BOUTEN_TYPE_FILLEDDOT: MF_TIMED_TEXT_BOUTEN_TYPE = 4
MF_TIMED_TEXT_BOUTEN_TYPE_OPENDOT: MF_TIMED_TEXT_BOUTEN_TYPE = 5
MF_TIMED_TEXT_BOUTEN_TYPE_FILLEDSESAME: MF_TIMED_TEXT_BOUTEN_TYPE = 6
MF_TIMED_TEXT_BOUTEN_TYPE_OPENSESAME: MF_TIMED_TEXT_BOUTEN_TYPE = 7
MF_TIMED_TEXT_CUE_EVENT = Int32
MF_TIMED_TEXT_CUE_EVENT_ACTIVE: MF_TIMED_TEXT_CUE_EVENT = 0
MF_TIMED_TEXT_CUE_EVENT_INACTIVE: MF_TIMED_TEXT_CUE_EVENT = 1
MF_TIMED_TEXT_CUE_EVENT_CLEAR: MF_TIMED_TEXT_CUE_EVENT = 2
MF_TIMED_TEXT_DECORATION = Int32
MF_TIMED_TEXT_DECORATION_NONE: MF_TIMED_TEXT_DECORATION = 0
MF_TIMED_TEXT_DECORATION_UNDERLINE: MF_TIMED_TEXT_DECORATION = 1
MF_TIMED_TEXT_DECORATION_LINE_THROUGH: MF_TIMED_TEXT_DECORATION = 2
MF_TIMED_TEXT_DECORATION_OVERLINE: MF_TIMED_TEXT_DECORATION = 4
MF_TIMED_TEXT_DISPLAY_ALIGNMENT = Int32
MF_TIMED_TEXT_DISPLAY_ALIGNMENT_BEFORE: MF_TIMED_TEXT_DISPLAY_ALIGNMENT = 0
MF_TIMED_TEXT_DISPLAY_ALIGNMENT_AFTER: MF_TIMED_TEXT_DISPLAY_ALIGNMENT = 1
MF_TIMED_TEXT_DISPLAY_ALIGNMENT_CENTER: MF_TIMED_TEXT_DISPLAY_ALIGNMENT = 2
MF_TIMED_TEXT_ERROR_CODE = Int32
MF_TIMED_TEXT_ERROR_CODE_NOERROR: MF_TIMED_TEXT_ERROR_CODE = 0
MF_TIMED_TEXT_ERROR_CODE_FATAL: MF_TIMED_TEXT_ERROR_CODE = 1
MF_TIMED_TEXT_ERROR_CODE_DATA_FORMAT: MF_TIMED_TEXT_ERROR_CODE = 2
MF_TIMED_TEXT_ERROR_CODE_NETWORK: MF_TIMED_TEXT_ERROR_CODE = 3
MF_TIMED_TEXT_ERROR_CODE_INTERNAL: MF_TIMED_TEXT_ERROR_CODE = 4
MF_TIMED_TEXT_FONT_STYLE = Int32
MF_TIMED_TEXT_FONT_STYLE_NORMAL: MF_TIMED_TEXT_FONT_STYLE = 0
MF_TIMED_TEXT_FONT_STYLE_OBLIQUE: MF_TIMED_TEXT_FONT_STYLE = 1
MF_TIMED_TEXT_FONT_STYLE_ITALIC: MF_TIMED_TEXT_FONT_STYLE = 2
MF_TIMED_TEXT_RUBY_ALIGN = Int32
MF_TIMED_TEXT_RUBY_ALIGN_CENTER: MF_TIMED_TEXT_RUBY_ALIGN = 0
MF_TIMED_TEXT_RUBY_ALIGN_START: MF_TIMED_TEXT_RUBY_ALIGN = 1
MF_TIMED_TEXT_RUBY_ALIGN_END: MF_TIMED_TEXT_RUBY_ALIGN = 2
MF_TIMED_TEXT_RUBY_ALIGN_SPACEAROUND: MF_TIMED_TEXT_RUBY_ALIGN = 3
MF_TIMED_TEXT_RUBY_ALIGN_SPACEBETWEEN: MF_TIMED_TEXT_RUBY_ALIGN = 4
MF_TIMED_TEXT_RUBY_ALIGN_WITHBASE: MF_TIMED_TEXT_RUBY_ALIGN = 5
MF_TIMED_TEXT_RUBY_POSITION = Int32
MF_TIMED_TEXT_RUBY_POSITION_BEFORE: MF_TIMED_TEXT_RUBY_POSITION = 0
MF_TIMED_TEXT_RUBY_POSITION_AFTER: MF_TIMED_TEXT_RUBY_POSITION = 1
MF_TIMED_TEXT_RUBY_POSITION_OUTSIDE: MF_TIMED_TEXT_RUBY_POSITION = 2
MF_TIMED_TEXT_RUBY_RESERVE = Int32
MF_TIMED_TEXT_RUBY_RESERVE_NONE: MF_TIMED_TEXT_RUBY_RESERVE = 0
MF_TIMED_TEXT_RUBY_RESERVE_BEFORE: MF_TIMED_TEXT_RUBY_RESERVE = 1
MF_TIMED_TEXT_RUBY_RESERVE_AFTER: MF_TIMED_TEXT_RUBY_RESERVE = 2
MF_TIMED_TEXT_RUBY_RESERVE_BOTH: MF_TIMED_TEXT_RUBY_RESERVE = 3
MF_TIMED_TEXT_RUBY_RESERVE_OUTSIDE: MF_TIMED_TEXT_RUBY_RESERVE = 4
MF_TIMED_TEXT_SCROLL_MODE = Int32
MF_TIMED_TEXT_SCROLL_MODE_POP_ON: MF_TIMED_TEXT_SCROLL_MODE = 0
MF_TIMED_TEXT_SCROLL_MODE_ROLL_UP: MF_TIMED_TEXT_SCROLL_MODE = 1
MF_TIMED_TEXT_TRACK_KIND = Int32
MF_TIMED_TEXT_TRACK_KIND_UNKNOWN: MF_TIMED_TEXT_TRACK_KIND = 0
MF_TIMED_TEXT_TRACK_KIND_SUBTITLES: MF_TIMED_TEXT_TRACK_KIND = 1
MF_TIMED_TEXT_TRACK_KIND_CAPTIONS: MF_TIMED_TEXT_TRACK_KIND = 2
MF_TIMED_TEXT_TRACK_KIND_METADATA: MF_TIMED_TEXT_TRACK_KIND = 3
MF_TIMED_TEXT_TRACK_READY_STATE = Int32
MF_TIMED_TEXT_TRACK_READY_STATE_NONE: MF_TIMED_TEXT_TRACK_READY_STATE = 0
MF_TIMED_TEXT_TRACK_READY_STATE_LOADING: MF_TIMED_TEXT_TRACK_READY_STATE = 1
MF_TIMED_TEXT_TRACK_READY_STATE_LOADED: MF_TIMED_TEXT_TRACK_READY_STATE = 2
MF_TIMED_TEXT_TRACK_READY_STATE_ERROR: MF_TIMED_TEXT_TRACK_READY_STATE = 3
MF_TIMED_TEXT_UNIT_TYPE = Int32
MF_TIMED_TEXT_UNIT_TYPE_PIXELS: MF_TIMED_TEXT_UNIT_TYPE = 0
MF_TIMED_TEXT_UNIT_TYPE_PERCENTAGE: MF_TIMED_TEXT_UNIT_TYPE = 1
MF_TIMED_TEXT_WRITING_MODE = Int32
MF_TIMED_TEXT_WRITING_MODE_LRTB: MF_TIMED_TEXT_WRITING_MODE = 0
MF_TIMED_TEXT_WRITING_MODE_RLTB: MF_TIMED_TEXT_WRITING_MODE = 1
MF_TIMED_TEXT_WRITING_MODE_TBRL: MF_TIMED_TEXT_WRITING_MODE = 2
MF_TIMED_TEXT_WRITING_MODE_TBLR: MF_TIMED_TEXT_WRITING_MODE = 3
MF_TIMED_TEXT_WRITING_MODE_LR: MF_TIMED_TEXT_WRITING_MODE = 4
MF_TIMED_TEXT_WRITING_MODE_RL: MF_TIMED_TEXT_WRITING_MODE = 5
MF_TIMED_TEXT_WRITING_MODE_TB: MF_TIMED_TEXT_WRITING_MODE = 6
MF_TOPOLOGY_RESOLUTION_STATUS_FLAGS = Int32
MF_TOPOLOGY_RESOLUTION_SUCCEEDED: MF_TOPOLOGY_RESOLUTION_STATUS_FLAGS = 0
MF_OPTIONAL_NODE_REJECTED_MEDIA_TYPE: MF_TOPOLOGY_RESOLUTION_STATUS_FLAGS = 1
MF_OPTIONAL_NODE_REJECTED_PROTECTED_PROCESS: MF_TOPOLOGY_RESOLUTION_STATUS_FLAGS = 2
MF_TOPOLOGY_TYPE = Int32
MF_TOPOLOGY_OUTPUT_NODE: MF_TOPOLOGY_TYPE = 0
MF_TOPOLOGY_SOURCESTREAM_NODE: MF_TOPOLOGY_TYPE = 1
MF_TOPOLOGY_TRANSFORM_NODE: MF_TOPOLOGY_TYPE = 2
MF_TOPOLOGY_TEE_NODE: MF_TOPOLOGY_TYPE = 3
MF_TOPOLOGY_MAX: MF_TOPOLOGY_TYPE = -1
MF_TOPONODE_DRAIN_MODE = Int32
MF_TOPONODE_DRAIN_DEFAULT: MF_TOPONODE_DRAIN_MODE = 0
MF_TOPONODE_DRAIN_ALWAYS: MF_TOPONODE_DRAIN_MODE = 1
MF_TOPONODE_DRAIN_NEVER: MF_TOPONODE_DRAIN_MODE = 2
MF_TOPONODE_FLUSH_MODE = Int32
MF_TOPONODE_FLUSH_ALWAYS: MF_TOPONODE_FLUSH_MODE = 0
MF_TOPONODE_FLUSH_SEEK: MF_TOPONODE_FLUSH_MODE = 1
MF_TOPONODE_FLUSH_NEVER: MF_TOPONODE_FLUSH_MODE = 2
MF_TOPOSTATUS = Int32
MF_TOPOSTATUS_INVALID: MF_TOPOSTATUS = 0
MF_TOPOSTATUS_READY: MF_TOPOSTATUS = 100
MF_TOPOSTATUS_STARTED_SOURCE: MF_TOPOSTATUS = 200
MF_TOPOSTATUS_DYNAMIC_CHANGED: MF_TOPOSTATUS = 210
MF_TOPOSTATUS_SINK_SWITCHED: MF_TOPOSTATUS = 300
MF_TOPOSTATUS_ENDED: MF_TOPOSTATUS = 400
MF_TRANSCODE_ADJUST_PROFILE_FLAGS = Int32
MF_TRANSCODE_ADJUST_PROFILE_DEFAULT: MF_TRANSCODE_ADJUST_PROFILE_FLAGS = 0
MF_TRANSCODE_ADJUST_PROFILE_USE_SOURCE_ATTRIBUTES: MF_TRANSCODE_ADJUST_PROFILE_FLAGS = 1
class MF_TRANSCODE_SINK_INFO(EasyCastStructure):
    dwVideoStreamID: UInt32
    pVideoMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head
    dwAudioStreamID: UInt32
    pAudioMediaType: Windows.Win32.Media.MediaFoundation.IMFMediaType_head
MF_TRANSCODE_TOPOLOGYMODE_FLAGS = Int32
MF_TRANSCODE_TOPOLOGYMODE_SOFTWARE_ONLY: MF_TRANSCODE_TOPOLOGYMODE_FLAGS = 0
MF_TRANSCODE_TOPOLOGYMODE_HARDWARE_ALLOWED: MF_TRANSCODE_TOPOLOGYMODE_FLAGS = 1
MF_URL_TRUST_STATUS = Int32
MF_LICENSE_URL_UNTRUSTED: MF_URL_TRUST_STATUS = 0
MF_LICENSE_URL_TRUSTED: MF_URL_TRUST_STATUS = 1
MF_LICENSE_URL_TAMPERED: MF_URL_TRUST_STATUS = 2
MF_VIDEO_PROCESSOR_ALGORITHM_TYPE = Int32
MF_VIDEO_PROCESSOR_ALGORITHM_DEFAULT: MF_VIDEO_PROCESSOR_ALGORITHM_TYPE = 0
MF_VIDEO_PROCESSOR_ALGORITHM_MRF_CRF_444: MF_VIDEO_PROCESSOR_ALGORITHM_TYPE = 1
MF_VIDEO_PROCESSOR_MIRROR = Int32
MIRROR_NONE: MF_VIDEO_PROCESSOR_MIRROR = 0
MIRROR_HORIZONTAL: MF_VIDEO_PROCESSOR_MIRROR = 1
MIRROR_VERTICAL: MF_VIDEO_PROCESSOR_MIRROR = 2
MF_VIDEO_PROCESSOR_ROTATION = Int32
ROTATION_NONE: MF_VIDEO_PROCESSOR_ROTATION = 0
ROTATION_NORMAL: MF_VIDEO_PROCESSOR_ROTATION = 1
class MF_VIDEO_SPHERICAL_VIEWDIRECTION(EasyCastStructure):
    iHeading: Int32
    iPitch: Int32
    iRoll: Int32
MIC_ARRAY_MODE = Int32
MICARRAY_SINGLE_CHAN: MIC_ARRAY_MODE = 0
MICARRAY_SIMPLE_SUM: MIC_ARRAY_MODE = 256
MICARRAY_SINGLE_BEAM: MIC_ARRAY_MODE = 512
MICARRAY_FIXED_BEAM: MIC_ARRAY_MODE = 1024
MICARRAY_EXTERN_BEAM: MIC_ARRAY_MODE = 2048
class MOVEREGION_INFO(EasyCastStructure):
    FrameNumber: UInt32
    NumMoveRegions: UInt32
    MoveRegions: Windows.Win32.Media.MediaFoundation.MOVE_RECT * 1
class MOVE_RECT(EasyCastStructure):
    SourcePoint: Windows.Win32.Foundation.POINT
    DestRect: Windows.Win32.Foundation.RECT
MP3ACMCodecWrapper = Guid('{11103421-354c-4cca-a7a3-1aff9a5b6701}')
class MPEG1VIDEOINFO(EasyCastStructure):
    hdr: Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER
    dwStartTimeCode: UInt32
    cbSequenceHeader: UInt32
    bSequenceHeader: Byte * 1
class MPEG2VIDEOINFO(EasyCastStructure):
    hdr: Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER2
    dwStartTimeCode: UInt32
    cbSequenceHeader: UInt32
    dwProfile: UInt32
    dwLevel: UInt32
    dwFlags: Windows.Win32.Media.MediaFoundation.MPEG2VIDEOINFO_FLAGS
    dwSequenceHeader: UInt32 * 1
MPEG2VIDEOINFO_FLAGS = UInt32
AMMPEG2_DoPanScan: MPEG2VIDEOINFO_FLAGS = 1
AMMPEG2_DVDLine21Field1: MPEG2VIDEOINFO_FLAGS = 2
AMMPEG2_DVDLine21Field2: MPEG2VIDEOINFO_FLAGS = 4
AMMPEG2_SourceIsLetterboxed: MPEG2VIDEOINFO_FLAGS = 8
AMMPEG2_FilmCameraMode: MPEG2VIDEOINFO_FLAGS = 16
AMMPEG2_LetterboxAnalogOut: MPEG2VIDEOINFO_FLAGS = 32
AMMPEG2_DSS_UserData: MPEG2VIDEOINFO_FLAGS = 64
AMMPEG2_DVB_UserData: MPEG2VIDEOINFO_FLAGS = 128
AMMPEG2_27MhzTimebase: MPEG2VIDEOINFO_FLAGS = 256
AMMPEG2_WidescreenAnalogOut: MPEG2VIDEOINFO_FLAGS = 512
MSAMRNBDecoder = Guid('{265011ae-5481-4f77-a295-abb6ffe8d63e}')
MSAMRNBEncoder = Guid('{2fae8afe-04a3-423a-a814-85db454712b0}')
class MT_ARBITRARY_HEADER(EasyCastStructure):
    majortype: Guid
    subtype: Guid
    bFixedSizeSamples: Windows.Win32.Foundation.BOOL
    bTemporalCompression: Windows.Win32.Foundation.BOOL
    lSampleSize: UInt32
    formattype: Guid
class MT_CUSTOM_VIDEO_PRIMARIES(EasyCastStructure):
    fRx: Single
    fRy: Single
    fGx: Single
    fGy: Single
    fBx: Single
    fBy: Single
    fWx: Single
    fWy: Single
MULawCodecWrapper = Guid('{92b66080-5e2d-449e-90c4-c41f268e5514}')
class OPM_ACP_AND_CGMSA_SIGNALING(EasyCastStructure):
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    ulStatusFlags: UInt32
    ulAvailableTVProtectionStandards: UInt32
    ulActiveTVProtectionStandard: UInt32
    ulReserved: UInt32
    ulAspectRatioValidMask1: UInt32
    ulAspectRatioData1: UInt32
    ulAspectRatioValidMask2: UInt32
    ulAspectRatioData2: UInt32
    ulAspectRatioValidMask3: UInt32
    ulAspectRatioData3: UInt32
    ulReserved2: UInt32 * 4
    ulReserved3: UInt32 * 4
    _pack_ = 1
OPM_ACP_PROTECTION_LEVEL = Int32
OPM_ACP_OFF: OPM_ACP_PROTECTION_LEVEL = 0
OPM_ACP_LEVEL_ONE: OPM_ACP_PROTECTION_LEVEL = 1
OPM_ACP_LEVEL_TWO: OPM_ACP_PROTECTION_LEVEL = 2
OPM_ACP_LEVEL_THREE: OPM_ACP_PROTECTION_LEVEL = 3
OPM_ACP_FORCE_ULONG: OPM_ACP_PROTECTION_LEVEL = 2147483647
class OPM_ACTUAL_OUTPUT_FORMAT(EasyCastStructure):
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    ulStatusFlags: UInt32
    ulDisplayWidth: UInt32
    ulDisplayHeight: UInt32
    dsfSampleInterleaveFormat: Windows.Win32.Media.MediaFoundation.DXVA2_SampleFormat
    d3dFormat: Windows.Win32.Graphics.Direct3D9.D3DFORMAT
    ulFrequencyNumerator: UInt32
    ulFrequencyDenominator: UInt32
    _pack_ = 1
OPM_BUS_TYPE = Int32
OPM_BUS_TYPE_OTHER: OPM_BUS_TYPE = 0
OPM_BUS_TYPE_PCI: OPM_BUS_TYPE = 1
OPM_BUS_TYPE_PCIX: OPM_BUS_TYPE = 2
OPM_BUS_TYPE_PCIEXPRESS: OPM_BUS_TYPE = 3
OPM_BUS_TYPE_AGP: OPM_BUS_TYPE = 4
OPM_BUS_IMPLEMENTATION_MODIFIER_INSIDE_OF_CHIPSET: OPM_BUS_TYPE = 65536
OPM_BUS_IMPLEMENTATION_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_CHIP: OPM_BUS_TYPE = 131072
OPM_BUS_IMPLEMENTATION_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_SOCKET: OPM_BUS_TYPE = 196608
OPM_BUS_IMPLEMENTATION_MODIFIER_DAUGHTER_BOARD_CONNECTOR: OPM_BUS_TYPE = 262144
OPM_BUS_IMPLEMENTATION_MODIFIER_DAUGHTER_BOARD_CONNECTOR_INSIDE_OF_NUAE: OPM_BUS_TYPE = 327680
OPM_BUS_IMPLEMENTATION_MODIFIER_NON_STANDARD: OPM_BUS_TYPE = -2147483648
OPM_COPP_COMPATIBLE_BUS_TYPE_INTEGRATED: OPM_BUS_TYPE = -2147483648
OPM_CGMSA = Int32
OPM_CGMSA_OFF: OPM_CGMSA = 0
OPM_CGMSA_COPY_FREELY: OPM_CGMSA = 1
OPM_CGMSA_COPY_NO_MORE: OPM_CGMSA = 2
OPM_CGMSA_COPY_ONE_GENERATION: OPM_CGMSA = 3
OPM_CGMSA_COPY_NEVER: OPM_CGMSA = 4
OPM_CGMSA_REDISTRIBUTION_CONTROL_REQUIRED: OPM_CGMSA = 8
class OPM_CONFIGURE_PARAMETERS(EasyCastStructure):
    omac: Windows.Win32.Media.MediaFoundation.OPM_OMAC
    guidSetting: Guid
    ulSequenceNumber: UInt32
    cbParametersSize: UInt32
    abParameters: Byte * 4056
    _pack_ = 1
class OPM_CONNECTED_HDCP_DEVICE_INFORMATION(EasyCastStructure):
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    ulStatusFlags: UInt32
    ulHDCPFlags: UInt32
    ksvB: Windows.Win32.Media.MediaFoundation.OPM_HDCP_KEY_SELECTION_VECTOR
    Reserved: Byte * 11
    Reserved2: Byte * 16
    Reserved3: Byte * 16
    _pack_ = 1
OPM_CONNECTOR_TYPE = Int32
OPM_CONNECTOR_TYPE_OTHER: OPM_CONNECTOR_TYPE = -1
OPM_CONNECTOR_TYPE_VGA: OPM_CONNECTOR_TYPE = 0
OPM_CONNECTOR_TYPE_SVIDEO: OPM_CONNECTOR_TYPE = 1
OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO: OPM_CONNECTOR_TYPE = 2
OPM_CONNECTOR_TYPE_COMPONENT_VIDEO: OPM_CONNECTOR_TYPE = 3
OPM_CONNECTOR_TYPE_DVI: OPM_CONNECTOR_TYPE = 4
OPM_CONNECTOR_TYPE_HDMI: OPM_CONNECTOR_TYPE = 5
OPM_CONNECTOR_TYPE_LVDS: OPM_CONNECTOR_TYPE = 6
OPM_CONNECTOR_TYPE_D_JPN: OPM_CONNECTOR_TYPE = 8
OPM_CONNECTOR_TYPE_SDI: OPM_CONNECTOR_TYPE = 9
OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL: OPM_CONNECTOR_TYPE = 10
OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED: OPM_CONNECTOR_TYPE = 11
OPM_CONNECTOR_TYPE_UDI_EXTERNAL: OPM_CONNECTOR_TYPE = 12
OPM_CONNECTOR_TYPE_UDI_EMBEDDED: OPM_CONNECTOR_TYPE = 13
OPM_CONNECTOR_TYPE_RESERVED: OPM_CONNECTOR_TYPE = 14
OPM_CONNECTOR_TYPE_MIRACAST: OPM_CONNECTOR_TYPE = 15
OPM_CONNECTOR_TYPE_TRANSPORT_AGNOSTIC_DIGITAL_MODE_A: OPM_CONNECTOR_TYPE = 16
OPM_CONNECTOR_TYPE_TRANSPORT_AGNOSTIC_DIGITAL_MODE_B: OPM_CONNECTOR_TYPE = 17
OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL: OPM_CONNECTOR_TYPE = -2147483648
class OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS(EasyCastStructure):
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    guidInformation: Guid
    ulSequenceNumber: UInt32
    cbParametersSize: UInt32
    abParameters: Byte * 4056
    _pack_ = 1
OPM_DPCP_PROTECTION_LEVEL = Int32
OPM_DPCP_OFF: OPM_DPCP_PROTECTION_LEVEL = 0
OPM_DPCP_ON: OPM_DPCP_PROTECTION_LEVEL = 1
OPM_DPCP_FORCE_ULONG: OPM_DPCP_PROTECTION_LEVEL = 2147483647
OPM_DVI_CHARACTERISTIC = Int32
OPM_DVI_CHARACTERISTIC_1_0: OPM_DVI_CHARACTERISTIC = 1
OPM_DVI_CHARACTERISTIC_1_1_OR_ABOVE: OPM_DVI_CHARACTERISTIC = 2
class OPM_ENCRYPTED_INITIALIZATION_PARAMETERS(EasyCastStructure):
    abEncryptedInitializationParameters: Byte * 256
class OPM_GET_CODEC_INFO_INFORMATION(EasyCastStructure):
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    Merit: UInt32
    _pack_ = 1
class OPM_GET_CODEC_INFO_PARAMETERS(EasyCastStructure):
    cbVerifier: UInt32
    Verifier: Byte * 4052
    _pack_ = 1
class OPM_GET_INFO_PARAMETERS(EasyCastStructure):
    omac: Windows.Win32.Media.MediaFoundation.OPM_OMAC
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    guidInformation: Guid
    ulSequenceNumber: UInt32
    cbParametersSize: UInt32
    abParameters: Byte * 4056
    _pack_ = 1
OPM_HDCP_FLAGS = Int32
OPM_HDCP_FLAG_NONE: OPM_HDCP_FLAGS = 0
OPM_HDCP_FLAG_REPEATER: OPM_HDCP_FLAGS = 1
class OPM_HDCP_KEY_SELECTION_VECTOR(EasyCastStructure):
    abKeySelectionVector: Byte * 5
OPM_HDCP_PROTECTION_LEVEL = Int32
OPM_HDCP_OFF: OPM_HDCP_PROTECTION_LEVEL = 0
OPM_HDCP_ON: OPM_HDCP_PROTECTION_LEVEL = 1
OPM_HDCP_FORCE_ULONG: OPM_HDCP_PROTECTION_LEVEL = 2147483647
OPM_HDCP_STATUS = Int32
OPM_HDCP_STATUS_ON: OPM_HDCP_STATUS = 0
OPM_HDCP_STATUS_OFF: OPM_HDCP_STATUS = 1
OPM_HDCP_TYPE = Int32
OPM_HDCP_TYPE_0: OPM_HDCP_TYPE = 0
OPM_HDCP_TYPE_1: OPM_HDCP_TYPE = 1
OPM_IMAGE_ASPECT_RATIO_EN300294 = Int32
OPM_ASPECT_RATIO_EN300294_FULL_FORMAT_4_BY_3: OPM_IMAGE_ASPECT_RATIO_EN300294 = 0
OPM_ASPECT_RATIO_EN300294_BOX_14_BY_9_CENTER: OPM_IMAGE_ASPECT_RATIO_EN300294 = 1
OPM_ASPECT_RATIO_EN300294_BOX_14_BY_9_TOP: OPM_IMAGE_ASPECT_RATIO_EN300294 = 2
OPM_ASPECT_RATIO_EN300294_BOX_16_BY_9_CENTER: OPM_IMAGE_ASPECT_RATIO_EN300294 = 3
OPM_ASPECT_RATIO_EN300294_BOX_16_BY_9_TOP: OPM_IMAGE_ASPECT_RATIO_EN300294 = 4
OPM_ASPECT_RATIO_EN300294_BOX_GT_16_BY_9_CENTER: OPM_IMAGE_ASPECT_RATIO_EN300294 = 5
OPM_ASPECT_RATIO_EN300294_FULL_FORMAT_4_BY_3_PROTECTED_CENTER: OPM_IMAGE_ASPECT_RATIO_EN300294 = 6
OPM_ASPECT_RATIO_EN300294_FULL_FORMAT_16_BY_9_ANAMORPHIC: OPM_IMAGE_ASPECT_RATIO_EN300294 = 7
OPM_ASPECT_RATIO_FORCE_ULONG: OPM_IMAGE_ASPECT_RATIO_EN300294 = 2147483647
class OPM_OMAC(EasyCastStructure):
    abOMAC: Byte * 16
OPM_OUTPUT_HARDWARE_PROTECTION = Int32
OPM_OUTPUT_HARDWARE_PROTECTION_NOT_SUPPORTED: OPM_OUTPUT_HARDWARE_PROTECTION = 0
OPM_OUTPUT_HARDWARE_PROTECTION_SUPPORTED: OPM_OUTPUT_HARDWARE_PROTECTION = 1
class OPM_OUTPUT_ID_DATA(EasyCastStructure):
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    ulStatusFlags: UInt32
    OutputId: UInt64
    _pack_ = 1
OPM_PROTECTION_STANDARD_TYPE = UInt32
OPM_PROTECTION_STANDARD_OTHER: OPM_PROTECTION_STANDARD_TYPE = 2147483648
OPM_PROTECTION_STANDARD_NONE: OPM_PROTECTION_STANDARD_TYPE = 0
OPM_PROTECTION_STANDARD_IEC61880_525I: OPM_PROTECTION_STANDARD_TYPE = 1
OPM_PROTECTION_STANDARD_IEC61880_2_525I: OPM_PROTECTION_STANDARD_TYPE = 2
OPM_PROTECTION_STANDARD_IEC62375_625P: OPM_PROTECTION_STANDARD_TYPE = 4
OPM_PROTECTION_STANDARD_EIA608B_525: OPM_PROTECTION_STANDARD_TYPE = 8
OPM_PROTECTION_STANDARD_EN300294_625I: OPM_PROTECTION_STANDARD_TYPE = 16
OPM_PROTECTION_STANDARD_CEA805A_TYPEA_525P: OPM_PROTECTION_STANDARD_TYPE = 32
OPM_PROTECTION_STANDARD_CEA805A_TYPEA_750P: OPM_PROTECTION_STANDARD_TYPE = 64
OPM_PROTECTION_STANDARD_CEA805A_TYPEA_1125I: OPM_PROTECTION_STANDARD_TYPE = 128
OPM_PROTECTION_STANDARD_CEA805A_TYPEB_525P: OPM_PROTECTION_STANDARD_TYPE = 256
OPM_PROTECTION_STANDARD_CEA805A_TYPEB_750P: OPM_PROTECTION_STANDARD_TYPE = 512
OPM_PROTECTION_STANDARD_CEA805A_TYPEB_1125I: OPM_PROTECTION_STANDARD_TYPE = 1024
OPM_PROTECTION_STANDARD_ARIBTRB15_525I: OPM_PROTECTION_STANDARD_TYPE = 2048
OPM_PROTECTION_STANDARD_ARIBTRB15_525P: OPM_PROTECTION_STANDARD_TYPE = 4096
OPM_PROTECTION_STANDARD_ARIBTRB15_750P: OPM_PROTECTION_STANDARD_TYPE = 8192
OPM_PROTECTION_STANDARD_ARIBTRB15_1125I: OPM_PROTECTION_STANDARD_TYPE = 16384
OPM_PROTECTION_TYPE = Int32
OPM_PROTECTION_TYPE_OTHER: OPM_PROTECTION_TYPE = -2147483648
OPM_PROTECTION_TYPE_NONE: OPM_PROTECTION_TYPE = 0
OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP: OPM_PROTECTION_TYPE = 1
OPM_PROTECTION_TYPE_ACP: OPM_PROTECTION_TYPE = 2
OPM_PROTECTION_TYPE_CGMSA: OPM_PROTECTION_TYPE = 4
OPM_PROTECTION_TYPE_HDCP: OPM_PROTECTION_TYPE = 8
OPM_PROTECTION_TYPE_DPCP: OPM_PROTECTION_TYPE = 16
OPM_PROTECTION_TYPE_TYPE_ENFORCEMENT_HDCP: OPM_PROTECTION_TYPE = 32
class OPM_RANDOM_NUMBER(EasyCastStructure):
    abRandomNumber: Byte * 16
class OPM_REQUESTED_INFORMATION(EasyCastStructure):
    omac: Windows.Win32.Media.MediaFoundation.OPM_OMAC
    cbRequestedInformationSize: UInt32
    abRequestedInformation: Byte * 4076
    _pack_ = 1
class OPM_SET_ACP_AND_CGMSA_SIGNALING_PARAMETERS(EasyCastStructure):
    ulNewTVProtectionStandard: UInt32
    ulAspectRatioChangeMask1: UInt32
    ulAspectRatioData1: UInt32
    ulAspectRatioChangeMask2: UInt32
    ulAspectRatioData2: UInt32
    ulAspectRatioChangeMask3: UInt32
    ulAspectRatioData3: UInt32
    ulReserved: UInt32 * 4
    ulReserved2: UInt32 * 4
    ulReserved3: UInt32
    _pack_ = 1
class OPM_SET_HDCP_SRM_PARAMETERS(EasyCastStructure):
    ulSRMVersion: UInt32
    _pack_ = 1
class OPM_SET_PROTECTION_LEVEL_PARAMETERS(EasyCastStructure):
    ulProtectionType: UInt32
    ulProtectionLevel: UInt32
    Reserved: UInt32
    Reserved2: UInt32
    _pack_ = 1
class OPM_STANDARD_INFORMATION(EasyCastStructure):
    rnRandomNumber: Windows.Win32.Media.MediaFoundation.OPM_RANDOM_NUMBER
    ulStatusFlags: UInt32
    ulInformation: UInt32
    ulReserved: UInt32
    ulReserved2: UInt32
    _pack_ = 1
OPM_STATUS = Int32
OPM_STATUS_NORMAL: OPM_STATUS = 0
OPM_STATUS_LINK_LOST: OPM_STATUS = 1
OPM_STATUS_RENEGOTIATION_REQUIRED: OPM_STATUS = 2
OPM_STATUS_TAMPERING_DETECTED: OPM_STATUS = 4
OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED: OPM_STATUS = 8
OPM_TYPE = Int32
OPM_OMAC_SIZE: OPM_TYPE = 16
OPM_128_BIT_RANDOM_NUMBER_SIZE: OPM_TYPE = 16
OPM_ENCRYPTED_INITIALIZATION_PARAMETERS_SIZE: OPM_TYPE = 256
OPM_CONFIGURE_SETTING_DATA_SIZE: OPM_TYPE = 4056
OPM_GET_INFORMATION_PARAMETERS_SIZE: OPM_TYPE = 4056
OPM_REQUESTED_INFORMATION_SIZE: OPM_TYPE = 4076
OPM_HDCP_KEY_SELECTION_VECTOR_SIZE: OPM_TYPE = 5
OPM_PROTECTION_TYPE_SIZE: OPM_TYPE = 4
OPM_BUS_TYPE_MASK: OPM_TYPE = 65535
OPM_BUS_IMPLEMENTATION_MODIFIER_MASK: OPM_TYPE = 32767
OPM_TYPE_ENFORCEMENT_HDCP_PROTECTION_LEVEL = Int32
OPM_TYPE_ENFORCEMENT_HDCP_OFF: OPM_TYPE_ENFORCEMENT_HDCP_PROTECTION_LEVEL = 0
OPM_TYPE_ENFORCEMENT_HDCP_ON_WITH_NO_TYPE_RESTRICTION: OPM_TYPE_ENFORCEMENT_HDCP_PROTECTION_LEVEL = 1
OPM_TYPE_ENFORCEMENT_HDCP_ON_WITH_TYPE1_RESTRICTION: OPM_TYPE_ENFORCEMENT_HDCP_PROTECTION_LEVEL = 2
OPM_TYPE_ENFORCEMENT_HDCP_FORCE_ULONG: OPM_TYPE_ENFORCEMENT_HDCP_PROTECTION_LEVEL = 2147483647
OPM_VIDEO_OUTPUT_SEMANTICS = Int32
OPM_VOS_COPP_SEMANTICS: OPM_VIDEO_OUTPUT_SEMANTICS = 0
OPM_VOS_OPM_SEMANTICS: OPM_VIDEO_OUTPUT_SEMANTICS = 1
OPM_VOS_OPM_INDIRECT_DISPLAY: OPM_VIDEO_OUTPUT_SEMANTICS = 2
@winfunctype_pointer
def PDXVAHDSW_CreateDevice(pD3DDevice: Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9Ex_head, phDevice: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_CreateVideoProcessor(hDevice: Windows.Win32.Foundation.HANDLE, pVPGuid: POINTER(Guid), phVideoProcessor: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_DestroyDevice(hDevice: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_DestroyVideoProcessor(hVideoProcessor: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessBltStatePrivate(hVideoProcessor: Windows.Win32.Foundation.HANDLE, pData: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_BLT_STATE_PRIVATE_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessStreamStatePrivate(hVideoProcessor: Windows.Win32.Foundation.HANDLE, StreamNumber: UInt32, pData: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_STREAM_STATE_PRIVATE_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessorCaps(hDevice: Windows.Win32.Foundation.HANDLE, pContentDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CONTENT_DESC_head), Usage: Windows.Win32.Media.MediaFoundation.DXVAHD_DEVICE_USAGE, Count: UInt32, pCaps: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_VPCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessorCustomRates(hDevice: Windows.Win32.Foundation.HANDLE, pVPGuid: POINTER(Guid), Count: UInt32, pRates: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CUSTOM_RATE_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessorDeviceCaps(hDevice: Windows.Win32.Foundation.HANDLE, pContentDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CONTENT_DESC_head), Usage: Windows.Win32.Media.MediaFoundation.DXVAHD_DEVICE_USAGE, pCaps: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_VPDEVCAPS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessorFilterRange(hDevice: Windows.Win32.Foundation.HANDLE, Filter: Windows.Win32.Media.MediaFoundation.DXVAHD_FILTER, pRange: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_FILTER_RANGE_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessorInputFormats(hDevice: Windows.Win32.Foundation.HANDLE, pContentDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CONTENT_DESC_head), Usage: Windows.Win32.Media.MediaFoundation.DXVAHD_DEVICE_USAGE, Count: UInt32, pFormats: POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_GetVideoProcessorOutputFormats(hDevice: Windows.Win32.Foundation.HANDLE, pContentDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CONTENT_DESC_head), Usage: Windows.Win32.Media.MediaFoundation.DXVAHD_DEVICE_USAGE, Count: UInt32, pFormats: POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_Plugin(Size: UInt32, pCallbacks: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_ProposeVideoPrivateFormat(hDevice: Windows.Win32.Foundation.HANDLE, pFormat: POINTER(Windows.Win32.Graphics.Direct3D9.D3DFORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_SetVideoProcessBltState(hVideoProcessor: Windows.Win32.Foundation.HANDLE, State: Windows.Win32.Media.MediaFoundation.DXVAHD_BLT_STATE, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_SetVideoProcessStreamState(hVideoProcessor: Windows.Win32.Foundation.HANDLE, StreamNumber: UInt32, State: Windows.Win32.Media.MediaFoundation.DXVAHD_STREAM_STATE, DataSize: UInt32, pData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHDSW_VideoProcessBltHD(hVideoProcessor: Windows.Win32.Foundation.HANDLE, pOutputSurface: Windows.Win32.Graphics.Direct3D9.IDirect3DSurface9_head, OutputFrame: UInt32, StreamCount: UInt32, pStreams: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_STREAM_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PDXVAHD_CreateDevice(pD3DDevice: Windows.Win32.Graphics.Direct3D9.IDirect3DDevice9Ex_head, pContentDesc: POINTER(Windows.Win32.Media.MediaFoundation.DXVAHD_CONTENT_DESC_head), Usage: Windows.Win32.Media.MediaFoundation.DXVAHD_DEVICE_USAGE, pPlugin: Windows.Win32.Media.MediaFoundation.PDXVAHDSW_Plugin, ppDevice: POINTER(Windows.Win32.Media.MediaFoundation.IDXVAHD_Device_head)) -> Windows.Win32.Foundation.HRESULT: ...
PLAYTO_SOURCE_CREATEFLAGS = Int32
PLAYTO_SOURCE_NONE: PLAYTO_SOURCE_CREATEFLAGS = 0
PLAYTO_SOURCE_IMAGE: PLAYTO_SOURCE_CREATEFLAGS = 1
PLAYTO_SOURCE_AUDIO: PLAYTO_SOURCE_CREATEFLAGS = 2
PLAYTO_SOURCE_VIDEO: PLAYTO_SOURCE_CREATEFLAGS = 4
PLAYTO_SOURCE_PROTECTED: PLAYTO_SOURCE_CREATEFLAGS = 8
class ROI_AREA(EasyCastStructure):
    rect: Windows.Win32.Foundation.RECT
    QPDelta: Int32
SAMPLE_PROTECTION_VERSION = Int32
SAMPLE_PROTECTION_VERSION_NO: SAMPLE_PROTECTION_VERSION = 0
SAMPLE_PROTECTION_VERSION_BASIC_LOKI: SAMPLE_PROTECTION_VERSION = 1
SAMPLE_PROTECTION_VERSION_SCATTER: SAMPLE_PROTECTION_VERSION = 2
SAMPLE_PROTECTION_VERSION_RC4: SAMPLE_PROTECTION_VERSION = 3
SAMPLE_PROTECTION_VERSION_AES128CTR: SAMPLE_PROTECTION_VERSION = 4
SEEK_ORIGIN = Int32
_msoBegin: SEEK_ORIGIN = 0
_msoCurrent: SEEK_ORIGIN = 1
class SENSORPROFILEID(EasyCastStructure):
    Type: Guid
    Index: UInt32
    Unused: UInt32
class STREAM_MEDIUM(EasyCastStructure):
    gidMedium: Guid
    unMediumInstance: UInt32
class TOC_DESCRIPTOR(EasyCastStructure):
    guidID: Guid
    wStreamNumber: UInt16
    guidType: Guid
    wLanguageIndex: UInt16
class TOC_ENTRY_DESCRIPTOR(EasyCastStructure):
    qwStartTime: UInt64
    qwEndTime: UInt64
    qwStartPacketOffset: UInt64
    qwEndPacketOffset: UInt64
    qwRepresentativeFrameTime: UInt64
TOC_POS_TYPE = Int32
TOC_POS_INHEADER: TOC_POS_TYPE = 0
TOC_POS_TOPLEVELOBJECT: TOC_POS_TYPE = 1
class VIDEOINFOHEADER(EasyCastStructure):
    rcSource: Windows.Win32.Foundation.RECT
    rcTarget: Windows.Win32.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    bmiHeader: Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER
class VIDEOINFOHEADER2(EasyCastStructure):
    rcSource: Windows.Win32.Foundation.RECT
    rcTarget: Windows.Win32.Foundation.RECT
    dwBitRate: UInt32
    dwBitErrorRate: UInt32
    AvgTimePerFrame: Int64
    dwInterlaceFlags: UInt32
    dwCopyProtectFlags: UInt32
    dwPictAspectRatioX: UInt32
    dwPictAspectRatioY: UInt32
    Anonymous: _Anonymous_e__Union
    dwReserved2: UInt32
    bmiHeader: Windows.Win32.Graphics.Gdi.BITMAPINFOHEADER
    class _Anonymous_e__Union(EasyCastUnion):
        dwControlFlags: UInt32
        dwReserved1: UInt32
VorbisDecoderMFT = Guid('{1a198ef2-60e5-4ea8-90d8-da1f2832c288}')
WMT_PROP_DATATYPE = Int32
WMT_PROP_TYPE_DWORD: WMT_PROP_DATATYPE = 0
WMT_PROP_TYPE_STRING: WMT_PROP_DATATYPE = 1
WMT_PROP_TYPE_BINARY: WMT_PROP_DATATYPE = 2
WMT_PROP_TYPE_BOOL: WMT_PROP_DATATYPE = 3
WMT_PROP_TYPE_QWORD: WMT_PROP_DATATYPE = 4
WMT_PROP_TYPE_WORD: WMT_PROP_DATATYPE = 5
WMT_PROP_TYPE_GUID: WMT_PROP_DATATYPE = 6
WMV_DYNAMIC_FLAGS = Int32
WMV_DYNAMIC_BITRATE: WMV_DYNAMIC_FLAGS = 1
WMV_DYNAMIC_RESOLUTION: WMV_DYNAMIC_FLAGS = 2
WMV_DYNAMIC_COMPLEXITY: WMV_DYNAMIC_FLAGS = 4
_MFP_CREDENTIAL_FLAGS = Int32
MFP_CREDENTIAL_PROMPT: _MFP_CREDENTIAL_FLAGS = 1
MFP_CREDENTIAL_SAVE: _MFP_CREDENTIAL_FLAGS = 2
MFP_CREDENTIAL_DO_NOT_CACHE: _MFP_CREDENTIAL_FLAGS = 4
MFP_CREDENTIAL_CLEAR_TEXT: _MFP_CREDENTIAL_FLAGS = 8
MFP_CREDENTIAL_PROXY: _MFP_CREDENTIAL_FLAGS = 16
MFP_CREDENTIAL_LOGGED_ON_USER: _MFP_CREDENTIAL_FLAGS = 32
_MFP_MEDIAITEM_CHARACTERISTICS = Int32
MFP_MEDIAITEM_IS_LIVE: _MFP_MEDIAITEM_CHARACTERISTICS = 1
MFP_MEDIAITEM_CAN_SEEK: _MFP_MEDIAITEM_CHARACTERISTICS = 2
MFP_MEDIAITEM_CAN_PAUSE: _MFP_MEDIAITEM_CHARACTERISTICS = 4
MFP_MEDIAITEM_HAS_SLOW_SEEK: _MFP_MEDIAITEM_CHARACTERISTICS = 8
_MFT_INPUT_DATA_BUFFER_FLAGS = Int32
MFT_INPUT_DATA_BUFFER_PLACEHOLDER: _MFT_INPUT_DATA_BUFFER_FLAGS = -1
_MFT_INPUT_STATUS_FLAGS = Int32
MFT_INPUT_STATUS_ACCEPT_DATA: _MFT_INPUT_STATUS_FLAGS = 1
_MFT_INPUT_STREAM_INFO_FLAGS = Int32
MFT_INPUT_STREAM_WHOLE_SAMPLES: _MFT_INPUT_STREAM_INFO_FLAGS = 1
MFT_INPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER: _MFT_INPUT_STREAM_INFO_FLAGS = 2
MFT_INPUT_STREAM_FIXED_SAMPLE_SIZE: _MFT_INPUT_STREAM_INFO_FLAGS = 4
MFT_INPUT_STREAM_HOLDS_BUFFERS: _MFT_INPUT_STREAM_INFO_FLAGS = 8
MFT_INPUT_STREAM_DOES_NOT_ADDREF: _MFT_INPUT_STREAM_INFO_FLAGS = 256
MFT_INPUT_STREAM_REMOVABLE: _MFT_INPUT_STREAM_INFO_FLAGS = 512
MFT_INPUT_STREAM_OPTIONAL: _MFT_INPUT_STREAM_INFO_FLAGS = 1024
MFT_INPUT_STREAM_PROCESSES_IN_PLACE: _MFT_INPUT_STREAM_INFO_FLAGS = 2048
_MFT_OUTPUT_DATA_BUFFER_FLAGS = Int32
MFT_OUTPUT_DATA_BUFFER_INCOMPLETE: _MFT_OUTPUT_DATA_BUFFER_FLAGS = 16777216
MFT_OUTPUT_DATA_BUFFER_FORMAT_CHANGE: _MFT_OUTPUT_DATA_BUFFER_FLAGS = 256
MFT_OUTPUT_DATA_BUFFER_STREAM_END: _MFT_OUTPUT_DATA_BUFFER_FLAGS = 512
MFT_OUTPUT_DATA_BUFFER_NO_SAMPLE: _MFT_OUTPUT_DATA_BUFFER_FLAGS = 768
_MFT_OUTPUT_STATUS_FLAGS = Int32
MFT_OUTPUT_STATUS_SAMPLE_READY: _MFT_OUTPUT_STATUS_FLAGS = 1
_MFT_OUTPUT_STREAM_INFO_FLAGS = Int32
MFT_OUTPUT_STREAM_WHOLE_SAMPLES: _MFT_OUTPUT_STREAM_INFO_FLAGS = 1
MFT_OUTPUT_STREAM_SINGLE_SAMPLE_PER_BUFFER: _MFT_OUTPUT_STREAM_INFO_FLAGS = 2
MFT_OUTPUT_STREAM_FIXED_SAMPLE_SIZE: _MFT_OUTPUT_STREAM_INFO_FLAGS = 4
MFT_OUTPUT_STREAM_DISCARDABLE: _MFT_OUTPUT_STREAM_INFO_FLAGS = 8
MFT_OUTPUT_STREAM_OPTIONAL: _MFT_OUTPUT_STREAM_INFO_FLAGS = 16
MFT_OUTPUT_STREAM_PROVIDES_SAMPLES: _MFT_OUTPUT_STREAM_INFO_FLAGS = 256
MFT_OUTPUT_STREAM_CAN_PROVIDE_SAMPLES: _MFT_OUTPUT_STREAM_INFO_FLAGS = 512
MFT_OUTPUT_STREAM_LAZY_READ: _MFT_OUTPUT_STREAM_INFO_FLAGS = 1024
MFT_OUTPUT_STREAM_REMOVABLE: _MFT_OUTPUT_STREAM_INFO_FLAGS = 2048
_MFT_PROCESS_OUTPUT_FLAGS = Int32
MFT_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER: _MFT_PROCESS_OUTPUT_FLAGS = 1
MFT_PROCESS_OUTPUT_REGENERATE_LAST_OUTPUT: _MFT_PROCESS_OUTPUT_FLAGS = 2
_MFT_PROCESS_OUTPUT_STATUS = Int32
MFT_PROCESS_OUTPUT_STATUS_NEW_STREAMS: _MFT_PROCESS_OUTPUT_STATUS = 256
_MFT_SET_TYPE_FLAGS = Int32
MFT_SET_TYPE_TEST_ONLY: _MFT_SET_TYPE_FLAGS = 1
eAVAudioChannelConfig = Int32
eAVAudioChannelConfig_FRONT_LEFT: eAVAudioChannelConfig = 1
eAVAudioChannelConfig_FRONT_RIGHT: eAVAudioChannelConfig = 2
eAVAudioChannelConfig_FRONT_CENTER: eAVAudioChannelConfig = 4
eAVAudioChannelConfig_LOW_FREQUENCY: eAVAudioChannelConfig = 8
eAVAudioChannelConfig_BACK_LEFT: eAVAudioChannelConfig = 16
eAVAudioChannelConfig_BACK_RIGHT: eAVAudioChannelConfig = 32
eAVAudioChannelConfig_FRONT_LEFT_OF_CENTER: eAVAudioChannelConfig = 64
eAVAudioChannelConfig_FRONT_RIGHT_OF_CENTER: eAVAudioChannelConfig = 128
eAVAudioChannelConfig_BACK_CENTER: eAVAudioChannelConfig = 256
eAVAudioChannelConfig_SIDE_LEFT: eAVAudioChannelConfig = 512
eAVAudioChannelConfig_SIDE_RIGHT: eAVAudioChannelConfig = 1024
eAVAudioChannelConfig_TOP_CENTER: eAVAudioChannelConfig = 2048
eAVAudioChannelConfig_TOP_FRONT_LEFT: eAVAudioChannelConfig = 4096
eAVAudioChannelConfig_TOP_FRONT_CENTER: eAVAudioChannelConfig = 8192
eAVAudioChannelConfig_TOP_FRONT_RIGHT: eAVAudioChannelConfig = 16384
eAVAudioChannelConfig_TOP_BACK_LEFT: eAVAudioChannelConfig = 32768
eAVAudioChannelConfig_TOP_BACK_CENTER: eAVAudioChannelConfig = 65536
eAVAudioChannelConfig_TOP_BACK_RIGHT: eAVAudioChannelConfig = 131072
eAVDDSurroundMode = Int32
eAVDDSurroundMode_NotIndicated: eAVDDSurroundMode = 0
eAVDDSurroundMode_No: eAVDDSurroundMode = 1
eAVDDSurroundMode_Yes: eAVDDSurroundMode = 2
eAVDSPLoudnessEqualization = Int32
eAVDSPLoudnessEqualization_OFF: eAVDSPLoudnessEqualization = 0
eAVDSPLoudnessEqualization_ON: eAVDSPLoudnessEqualization = 1
eAVDSPLoudnessEqualization_AUTO: eAVDSPLoudnessEqualization = 2
eAVDSPSpeakerFill = Int32
eAVDSPSpeakerFill_OFF: eAVDSPSpeakerFill = 0
eAVDSPSpeakerFill_ON: eAVDSPSpeakerFill = 1
eAVDSPSpeakerFill_AUTO: eAVDSPSpeakerFill = 2
eAVDecAACDownmixMode = Int32
eAVDecAACDownmixMode_eAVDecAACUseISODownmix: eAVDecAACDownmixMode = 0
eAVDecAACDownmixMode_eAVDecAACUseARIBDownmix: eAVDecAACDownmixMode = 1
eAVDecAudioDualMono = Int32
eAVDecAudioDualMono_IsNotDualMono: eAVDecAudioDualMono = 0
eAVDecAudioDualMono_IsDualMono: eAVDecAudioDualMono = 1
eAVDecAudioDualMono_UnSpecified: eAVDecAudioDualMono = 2
eAVDecAudioDualMonoReproMode = Int32
eAVDecAudioDualMonoReproMode_STEREO: eAVDecAudioDualMonoReproMode = 0
eAVDecAudioDualMonoReproMode_LEFT_MONO: eAVDecAudioDualMonoReproMode = 1
eAVDecAudioDualMonoReproMode_RIGHT_MONO: eAVDecAudioDualMonoReproMode = 2
eAVDecAudioDualMonoReproMode_MIX_MONO: eAVDecAudioDualMonoReproMode = 3
eAVDecDDMatrixDecodingMode = Int32
eAVDecDDMatrixDecodingMode_OFF: eAVDecDDMatrixDecodingMode = 0
eAVDecDDMatrixDecodingMode_ON: eAVDecDDMatrixDecodingMode = 1
eAVDecDDMatrixDecodingMode_AUTO: eAVDecDDMatrixDecodingMode = 2
eAVDecDDOperationalMode = Int32
eAVDecDDOperationalMode_NONE: eAVDecDDOperationalMode = 0
eAVDecDDOperationalMode_LINE: eAVDecDDOperationalMode = 1
eAVDecDDOperationalMode_RF: eAVDecDDOperationalMode = 2
eAVDecDDOperationalMode_CUSTOM0: eAVDecDDOperationalMode = 3
eAVDecDDOperationalMode_CUSTOM1: eAVDecDDOperationalMode = 4
eAVDecDDOperationalMode_PORTABLE8: eAVDecDDOperationalMode = 5
eAVDecDDOperationalMode_PORTABLE11: eAVDecDDOperationalMode = 6
eAVDecDDOperationalMode_PORTABLE14: eAVDecDDOperationalMode = 7
eAVDecDDStereoDownMixMode = Int32
eAVDecDDStereoDownMixMode_Auto: eAVDecDDStereoDownMixMode = 0
eAVDecDDStereoDownMixMode_LtRt: eAVDecDDStereoDownMixMode = 1
eAVDecDDStereoDownMixMode_LoRo: eAVDecDDStereoDownMixMode = 2
eAVDecHEAACDynamicRangeControl = Int32
eAVDecHEAACDynamicRangeControl_OFF: eAVDecHEAACDynamicRangeControl = 0
eAVDecHEAACDynamicRangeControl_ON: eAVDecHEAACDynamicRangeControl = 1
eAVDecVideoCodecType = Int32
eAVDecVideoCodecType_NOTPLAYING: eAVDecVideoCodecType = 0
eAVDecVideoCodecType_MPEG2: eAVDecVideoCodecType = 1
eAVDecVideoCodecType_H264: eAVDecVideoCodecType = 2
eAVDecVideoDXVABusEncryption = Int32
eAVDecVideoDXVABusEncryption_NONE: eAVDecVideoDXVABusEncryption = 0
eAVDecVideoDXVABusEncryption_PRIVATE: eAVDecVideoDXVABusEncryption = 1
eAVDecVideoDXVABusEncryption_AES: eAVDecVideoDXVABusEncryption = 2
eAVDecVideoDXVAMode = Int32
eAVDecVideoDXVAMode_NOTPLAYING: eAVDecVideoDXVAMode = 0
eAVDecVideoDXVAMode_SW: eAVDecVideoDXVAMode = 1
eAVDecVideoDXVAMode_MC: eAVDecVideoDXVAMode = 2
eAVDecVideoDXVAMode_IDCT: eAVDecVideoDXVAMode = 3
eAVDecVideoDXVAMode_VLD: eAVDecVideoDXVAMode = 4
eAVDecVideoH264ErrorConcealment = Int32
eAVDecVideoH264ErrorConcealment_eErrorConcealmentTypeDrop: eAVDecVideoH264ErrorConcealment = 0
eAVDecVideoH264ErrorConcealment_eErrorConcealmentTypeBasic: eAVDecVideoH264ErrorConcealment = 1
eAVDecVideoH264ErrorConcealment_eErrorConcealmentTypeAdvanced: eAVDecVideoH264ErrorConcealment = 2
eAVDecVideoH264ErrorConcealment_eErrorConcealmentTypeDXVASetBlack: eAVDecVideoH264ErrorConcealment = 3
eAVDecVideoInputScanType = Int32
eAVDecVideoInputScan_Unknown: eAVDecVideoInputScanType = 0
eAVDecVideoInputScan_Progressive: eAVDecVideoInputScanType = 1
eAVDecVideoInputScan_Interlaced_UpperFieldFirst: eAVDecVideoInputScanType = 2
eAVDecVideoInputScan_Interlaced_LowerFieldFirst: eAVDecVideoInputScanType = 3
eAVDecVideoMPEG2ErrorConcealment = Int32
eAVDecVideoMPEG2ErrorConcealment_eErrorConcealmentOff: eAVDecVideoMPEG2ErrorConcealment = 0
eAVDecVideoMPEG2ErrorConcealment_eErrorConcealmentOn: eAVDecVideoMPEG2ErrorConcealment = 1
eAVDecVideoSWPowerLevel = Int32
eAVDecVideoSWPowerLevel_BatteryLife: eAVDecVideoSWPowerLevel = 0
eAVDecVideoSWPowerLevel_Balanced: eAVDecVideoSWPowerLevel = 50
eAVDecVideoSWPowerLevel_VideoQuality: eAVDecVideoSWPowerLevel = 100
eAVDecVideoSoftwareDeinterlaceMode = Int32
eAVDecVideoSoftwareDeinterlaceMode_NoDeinterlacing: eAVDecVideoSoftwareDeinterlaceMode = 0
eAVDecVideoSoftwareDeinterlaceMode_ProgressiveDeinterlacing: eAVDecVideoSoftwareDeinterlaceMode = 1
eAVDecVideoSoftwareDeinterlaceMode_BOBDeinterlacing: eAVDecVideoSoftwareDeinterlaceMode = 2
eAVDecVideoSoftwareDeinterlaceMode_SmartBOBDeinterlacing: eAVDecVideoSoftwareDeinterlaceMode = 3
eAVEncAV1PictureType = Int32
eAVEncAV1PictureType_Key: eAVEncAV1PictureType = 0
eAVEncAV1PictureType_Intra_Only: eAVEncAV1PictureType = 1
eAVEncAV1PictureType_Inter: eAVEncAV1PictureType = 2
eAVEncAV1PictureType_Switch: eAVEncAV1PictureType = 3
eAVEncAV1VLevel = Int32
eAVEncAV1VLevel_eAVEncAV1VLevel2: eAVEncAV1VLevel = 0
eAVEncAV1VLevel_eAVEncAV1VLevel2_1: eAVEncAV1VLevel = 1
eAVEncAV1VLevel_eAVEncAV1VLevel3: eAVEncAV1VLevel = 4
eAVEncAV1VLevel_eAVEncAV1VLevel3_1: eAVEncAV1VLevel = 5
eAVEncAV1VLevel_eAVEncAV1VLevel4: eAVEncAV1VLevel = 8
eAVEncAV1VLevel_eAVEncAV1VLevel4_1: eAVEncAV1VLevel = 9
eAVEncAV1VLevel_eAVEncAV1VLevel5: eAVEncAV1VLevel = 12
eAVEncAV1VLevel_eAVEncAV1VLevel5_1: eAVEncAV1VLevel = 13
eAVEncAV1VLevel_eAVEncAV1VLevel5_2: eAVEncAV1VLevel = 14
eAVEncAV1VLevel_eAVEncAV1VLevel5_3: eAVEncAV1VLevel = 15
eAVEncAV1VLevel_eAVEncAV1VLevel6: eAVEncAV1VLevel = 16
eAVEncAV1VLevel_eAVEncAV1VLevel6_1: eAVEncAV1VLevel = 17
eAVEncAV1VLevel_eAVEncAV1VLevel6_2: eAVEncAV1VLevel = 18
eAVEncAV1VLevel_eAVEncAV1VLevel6_3: eAVEncAV1VLevel = 19
eAVEncAV1VProfile = Int32
eAVEncAV1VProfile_unknown: eAVEncAV1VProfile = 0
eAVEncAV1VProfile_Main_420_8: eAVEncAV1VProfile = 1
eAVEncAV1VProfile_Main_420_10: eAVEncAV1VProfile = 2
eAVEncAV1VProfile_Main_400_8: eAVEncAV1VProfile = 3
eAVEncAV1VProfile_Main_400_10: eAVEncAV1VProfile = 4
eAVEncAV1VProfile_High_444_8: eAVEncAV1VProfile = 5
eAVEncAV1VProfile_High_444_10: eAVEncAV1VProfile = 6
eAVEncAV1VProfile_Professional_420_12: eAVEncAV1VProfile = 7
eAVEncAV1VProfile_Professional_400_12: eAVEncAV1VProfile = 8
eAVEncAV1VProfile_Professional_444_12: eAVEncAV1VProfile = 9
eAVEncAV1VProfile_Professional_422_8: eAVEncAV1VProfile = 10
eAVEncAV1VProfile_Professional_422_10: eAVEncAV1VProfile = 11
eAVEncAV1VProfile_Professional_422_12: eAVEncAV1VProfile = 12
eAVEncAdaptiveMode = Int32
eAVEncAdaptiveMode_None: eAVEncAdaptiveMode = 0
eAVEncAdaptiveMode_Resolution: eAVEncAdaptiveMode = 1
eAVEncAdaptiveMode_FrameRate: eAVEncAdaptiveMode = 2
eAVEncAudioDualMono = Int32
eAVEncAudioDualMono_SameAsInput: eAVEncAudioDualMono = 0
eAVEncAudioDualMono_Off: eAVEncAudioDualMono = 1
eAVEncAudioDualMono_On: eAVEncAudioDualMono = 2
eAVEncAudioInputContent = Int32
AVEncAudioInputContent_Unknown: eAVEncAudioInputContent = 0
AVEncAudioInputContent_Voice: eAVEncAudioInputContent = 1
AVEncAudioInputContent_Music: eAVEncAudioInputContent = 2
eAVEncChromaEncodeMode = Int32
eAVEncChromaEncodeMode_420: eAVEncChromaEncodeMode = 0
eAVEncChromaEncodeMode_444: eAVEncChromaEncodeMode = 1
eAVEncChromaEncodeMode_444_v2: eAVEncChromaEncodeMode = 2
eAVEncCommonRateControlMode = Int32
eAVEncCommonRateControlMode_CBR: eAVEncCommonRateControlMode = 0
eAVEncCommonRateControlMode_PeakConstrainedVBR: eAVEncCommonRateControlMode = 1
eAVEncCommonRateControlMode_UnconstrainedVBR: eAVEncCommonRateControlMode = 2
eAVEncCommonRateControlMode_Quality: eAVEncCommonRateControlMode = 3
eAVEncCommonRateControlMode_LowDelayVBR: eAVEncCommonRateControlMode = 4
eAVEncCommonRateControlMode_GlobalVBR: eAVEncCommonRateControlMode = 5
eAVEncCommonRateControlMode_GlobalLowDelayVBR: eAVEncCommonRateControlMode = 6
eAVEncCommonStreamEndHandling = Int32
eAVEncCommonStreamEndHandling_DiscardPartial: eAVEncCommonStreamEndHandling = 0
eAVEncCommonStreamEndHandling_EnsureComplete: eAVEncCommonStreamEndHandling = 1
eAVEncDDAtoDConverterType = Int32
eAVEncDDAtoDConverterType_Standard: eAVEncDDAtoDConverterType = 0
eAVEncDDAtoDConverterType_HDCD: eAVEncDDAtoDConverterType = 1
eAVEncDDDynamicRangeCompressionControl = Int32
eAVEncDDDynamicRangeCompressionControl_None: eAVEncDDDynamicRangeCompressionControl = 0
eAVEncDDDynamicRangeCompressionControl_FilmStandard: eAVEncDDDynamicRangeCompressionControl = 1
eAVEncDDDynamicRangeCompressionControl_FilmLight: eAVEncDDDynamicRangeCompressionControl = 2
eAVEncDDDynamicRangeCompressionControl_MusicStandard: eAVEncDDDynamicRangeCompressionControl = 3
eAVEncDDDynamicRangeCompressionControl_MusicLight: eAVEncDDDynamicRangeCompressionControl = 4
eAVEncDDDynamicRangeCompressionControl_Speech: eAVEncDDDynamicRangeCompressionControl = 5
eAVEncDDHeadphoneMode = Int32
eAVEncDDHeadphoneMode_NotIndicated: eAVEncDDHeadphoneMode = 0
eAVEncDDHeadphoneMode_NotEncoded: eAVEncDDHeadphoneMode = 1
eAVEncDDHeadphoneMode_Encoded: eAVEncDDHeadphoneMode = 2
eAVEncDDPreferredStereoDownMixMode = Int32
eAVEncDDPreferredStereoDownMixMode_LtRt: eAVEncDDPreferredStereoDownMixMode = 0
eAVEncDDPreferredStereoDownMixMode_LoRo: eAVEncDDPreferredStereoDownMixMode = 1
eAVEncDDProductionRoomType = Int32
eAVEncDDProductionRoomType_NotIndicated: eAVEncDDProductionRoomType = 0
eAVEncDDProductionRoomType_Large: eAVEncDDProductionRoomType = 1
eAVEncDDProductionRoomType_Small: eAVEncDDProductionRoomType = 2
eAVEncDDService = Int32
eAVEncDDService_CM: eAVEncDDService = 0
eAVEncDDService_ME: eAVEncDDService = 1
eAVEncDDService_VI: eAVEncDDService = 2
eAVEncDDService_HI: eAVEncDDService = 3
eAVEncDDService_D: eAVEncDDService = 4
eAVEncDDService_C: eAVEncDDService = 5
eAVEncDDService_E: eAVEncDDService = 6
eAVEncDDService_VO: eAVEncDDService = 7
eAVEncDDSurroundExMode = Int32
eAVEncDDSurroundExMode_NotIndicated: eAVEncDDSurroundExMode = 0
eAVEncDDSurroundExMode_No: eAVEncDDSurroundExMode = 1
eAVEncDDSurroundExMode_Yes: eAVEncDDSurroundExMode = 2
eAVEncH263PictureType = Int32
eAVEncH263PictureType_I: eAVEncH263PictureType = 0
eAVEncH263PictureType_P: eAVEncH263PictureType = 1
eAVEncH263PictureType_B: eAVEncH263PictureType = 2
eAVEncH263VLevel = Int32
eAVEncH263VLevel_eAVEncH263VLevel1: eAVEncH263VLevel = 10
eAVEncH263VLevel_eAVEncH263VLevel2: eAVEncH263VLevel = 20
eAVEncH263VLevel_eAVEncH263VLevel3: eAVEncH263VLevel = 30
eAVEncH263VLevel_eAVEncH263VLevel4: eAVEncH263VLevel = 40
eAVEncH263VLevel_eAVEncH263VLevel4_5: eAVEncH263VLevel = 45
eAVEncH263VLevel_eAVEncH263VLevel5: eAVEncH263VLevel = 50
eAVEncH263VLevel_eAVEncH263VLevel6: eAVEncH263VLevel = 60
eAVEncH263VLevel_eAVEncH263VLevel7: eAVEncH263VLevel = 70
eAVEncH263VProfile = Int32
eAVEncH263VProfile_Base: eAVEncH263VProfile = 0
eAVEncH263VProfile_CompatibilityV2: eAVEncH263VProfile = 1
eAVEncH263VProfile_CompatibilityV1: eAVEncH263VProfile = 2
eAVEncH263VProfile_WirelessV2: eAVEncH263VProfile = 3
eAVEncH263VProfile_WirelessV3: eAVEncH263VProfile = 4
eAVEncH263VProfile_HighCompression: eAVEncH263VProfile = 5
eAVEncH263VProfile_Internet: eAVEncH263VProfile = 6
eAVEncH263VProfile_Interlace: eAVEncH263VProfile = 7
eAVEncH263VProfile_HighLatency: eAVEncH263VProfile = 8
eAVEncH264PictureType = Int32
eAVEncH264PictureType_IDR: eAVEncH264PictureType = 0
eAVEncH264PictureType_P: eAVEncH264PictureType = 1
eAVEncH264PictureType_B: eAVEncH264PictureType = 2
eAVEncH264VLevel = Int32
eAVEncH264VLevel_eAVEncH264VLevel1: eAVEncH264VLevel = 10
eAVEncH264VLevel_eAVEncH264VLevel1_b: eAVEncH264VLevel = 11
eAVEncH264VLevel_eAVEncH264VLevel1_1: eAVEncH264VLevel = 11
eAVEncH264VLevel_eAVEncH264VLevel1_2: eAVEncH264VLevel = 12
eAVEncH264VLevel_eAVEncH264VLevel1_3: eAVEncH264VLevel = 13
eAVEncH264VLevel_eAVEncH264VLevel2: eAVEncH264VLevel = 20
eAVEncH264VLevel_eAVEncH264VLevel2_1: eAVEncH264VLevel = 21
eAVEncH264VLevel_eAVEncH264VLevel2_2: eAVEncH264VLevel = 22
eAVEncH264VLevel_eAVEncH264VLevel3: eAVEncH264VLevel = 30
eAVEncH264VLevel_eAVEncH264VLevel3_1: eAVEncH264VLevel = 31
eAVEncH264VLevel_eAVEncH264VLevel3_2: eAVEncH264VLevel = 32
eAVEncH264VLevel_eAVEncH264VLevel4: eAVEncH264VLevel = 40
eAVEncH264VLevel_eAVEncH264VLevel4_1: eAVEncH264VLevel = 41
eAVEncH264VLevel_eAVEncH264VLevel4_2: eAVEncH264VLevel = 42
eAVEncH264VLevel_eAVEncH264VLevel5: eAVEncH264VLevel = 50
eAVEncH264VLevel_eAVEncH264VLevel5_1: eAVEncH264VLevel = 51
eAVEncH264VLevel_eAVEncH264VLevel5_2: eAVEncH264VLevel = 52
eAVEncH264VProfile = Int32
eAVEncH264VProfile_unknown: eAVEncH264VProfile = 0
eAVEncH264VProfile_Simple: eAVEncH264VProfile = 66
eAVEncH264VProfile_Base: eAVEncH264VProfile = 66
eAVEncH264VProfile_Main: eAVEncH264VProfile = 77
eAVEncH264VProfile_High: eAVEncH264VProfile = 100
eAVEncH264VProfile_422: eAVEncH264VProfile = 122
eAVEncH264VProfile_High10: eAVEncH264VProfile = 110
eAVEncH264VProfile_444: eAVEncH264VProfile = 244
eAVEncH264VProfile_Extended: eAVEncH264VProfile = 88
eAVEncH264VProfile_ScalableBase: eAVEncH264VProfile = 83
eAVEncH264VProfile_ScalableHigh: eAVEncH264VProfile = 86
eAVEncH264VProfile_MultiviewHigh: eAVEncH264VProfile = 118
eAVEncH264VProfile_StereoHigh: eAVEncH264VProfile = 128
eAVEncH264VProfile_ConstrainedBase: eAVEncH264VProfile = 256
eAVEncH264VProfile_UCConstrainedHigh: eAVEncH264VProfile = 257
eAVEncH264VProfile_UCScalableConstrainedBase: eAVEncH264VProfile = 258
eAVEncH264VProfile_UCScalableConstrainedHigh: eAVEncH264VProfile = 259
eAVEncH265VLevel = Int32
eAVEncH265VLevel_eAVEncH265VLevel1: eAVEncH265VLevel = 30
eAVEncH265VLevel_eAVEncH265VLevel2: eAVEncH265VLevel = 60
eAVEncH265VLevel_eAVEncH265VLevel2_1: eAVEncH265VLevel = 63
eAVEncH265VLevel_eAVEncH265VLevel3: eAVEncH265VLevel = 90
eAVEncH265VLevel_eAVEncH265VLevel3_1: eAVEncH265VLevel = 93
eAVEncH265VLevel_eAVEncH265VLevel4: eAVEncH265VLevel = 120
eAVEncH265VLevel_eAVEncH265VLevel4_1: eAVEncH265VLevel = 123
eAVEncH265VLevel_eAVEncH265VLevel5: eAVEncH265VLevel = 150
eAVEncH265VLevel_eAVEncH265VLevel5_1: eAVEncH265VLevel = 153
eAVEncH265VLevel_eAVEncH265VLevel5_2: eAVEncH265VLevel = 156
eAVEncH265VLevel_eAVEncH265VLevel6: eAVEncH265VLevel = 180
eAVEncH265VLevel_eAVEncH265VLevel6_1: eAVEncH265VLevel = 183
eAVEncH265VLevel_eAVEncH265VLevel6_2: eAVEncH265VLevel = 186
eAVEncH265VProfile = Int32
eAVEncH265VProfile_unknown: eAVEncH265VProfile = 0
eAVEncH265VProfile_Main_420_8: eAVEncH265VProfile = 1
eAVEncH265VProfile_Main_420_10: eAVEncH265VProfile = 2
eAVEncH265VProfile_Main_420_12: eAVEncH265VProfile = 3
eAVEncH265VProfile_Main_422_10: eAVEncH265VProfile = 4
eAVEncH265VProfile_Main_422_12: eAVEncH265VProfile = 5
eAVEncH265VProfile_Main_444_8: eAVEncH265VProfile = 6
eAVEncH265VProfile_Main_444_10: eAVEncH265VProfile = 7
eAVEncH265VProfile_Main_444_12: eAVEncH265VProfile = 8
eAVEncH265VProfile_Monochrome_12: eAVEncH265VProfile = 9
eAVEncH265VProfile_Monochrome_16: eAVEncH265VProfile = 10
eAVEncH265VProfile_MainIntra_420_8: eAVEncH265VProfile = 11
eAVEncH265VProfile_MainIntra_420_10: eAVEncH265VProfile = 12
eAVEncH265VProfile_MainIntra_420_12: eAVEncH265VProfile = 13
eAVEncH265VProfile_MainIntra_422_10: eAVEncH265VProfile = 14
eAVEncH265VProfile_MainIntra_422_12: eAVEncH265VProfile = 15
eAVEncH265VProfile_MainIntra_444_8: eAVEncH265VProfile = 16
eAVEncH265VProfile_MainIntra_444_10: eAVEncH265VProfile = 17
eAVEncH265VProfile_MainIntra_444_12: eAVEncH265VProfile = 18
eAVEncH265VProfile_MainIntra_444_16: eAVEncH265VProfile = 19
eAVEncH265VProfile_MainStill_420_8: eAVEncH265VProfile = 20
eAVEncH265VProfile_MainStill_444_8: eAVEncH265VProfile = 21
eAVEncH265VProfile_MainStill_444_16: eAVEncH265VProfile = 22
eAVEncInputVideoSystem = Int32
eAVEncInputVideoSystem_Unspecified: eAVEncInputVideoSystem = 0
eAVEncInputVideoSystem_PAL: eAVEncInputVideoSystem = 1
eAVEncInputVideoSystem_NTSC: eAVEncInputVideoSystem = 2
eAVEncInputVideoSystem_SECAM: eAVEncInputVideoSystem = 3
eAVEncInputVideoSystem_MAC: eAVEncInputVideoSystem = 4
eAVEncInputVideoSystem_HDV: eAVEncInputVideoSystem = 5
eAVEncInputVideoSystem_Component: eAVEncInputVideoSystem = 6
eAVEncMPACodingMode = Int32
eAVEncMPACodingMode_Mono: eAVEncMPACodingMode = 0
eAVEncMPACodingMode_Stereo: eAVEncMPACodingMode = 1
eAVEncMPACodingMode_DualChannel: eAVEncMPACodingMode = 2
eAVEncMPACodingMode_JointStereo: eAVEncMPACodingMode = 3
eAVEncMPACodingMode_Surround: eAVEncMPACodingMode = 4
eAVEncMPAEmphasisType = Int32
eAVEncMPAEmphasisType_None: eAVEncMPAEmphasisType = 0
eAVEncMPAEmphasisType_50_15: eAVEncMPAEmphasisType = 1
eAVEncMPAEmphasisType_Reserved: eAVEncMPAEmphasisType = 2
eAVEncMPAEmphasisType_CCITT_J17: eAVEncMPAEmphasisType = 3
eAVEncMPALayer = Int32
eAVEncMPALayer_1: eAVEncMPALayer = 1
eAVEncMPALayer_2: eAVEncMPALayer = 2
eAVEncMPALayer_3: eAVEncMPALayer = 3
eAVEncMPVFrameFieldMode = Int32
eAVEncMPVFrameFieldMode_FieldMode: eAVEncMPVFrameFieldMode = 0
eAVEncMPVFrameFieldMode_FrameMode: eAVEncMPVFrameFieldMode = 1
eAVEncMPVIntraVLCTable = Int32
eAVEncMPVIntraVLCTable_Auto: eAVEncMPVIntraVLCTable = 0
eAVEncMPVIntraVLCTable_MPEG1: eAVEncMPVIntraVLCTable = 1
eAVEncMPVIntraVLCTable_Alternate: eAVEncMPVIntraVLCTable = 2
eAVEncMPVLevel = Int32
eAVEncMPVLevel_Low: eAVEncMPVLevel = 1
eAVEncMPVLevel_Main: eAVEncMPVLevel = 2
eAVEncMPVLevel_High1440: eAVEncMPVLevel = 3
eAVEncMPVLevel_High: eAVEncMPVLevel = 4
eAVEncMPVProfile = Int32
eAVEncMPVProfile_unknown: eAVEncMPVProfile = 0
eAVEncMPVProfile_Simple: eAVEncMPVProfile = 1
eAVEncMPVProfile_Main: eAVEncMPVProfile = 2
eAVEncMPVProfile_High: eAVEncMPVProfile = 3
eAVEncMPVProfile_422: eAVEncMPVProfile = 4
eAVEncMPVQScaleType = Int32
eAVEncMPVQScaleType_Auto: eAVEncMPVQScaleType = 0
eAVEncMPVQScaleType_Linear: eAVEncMPVQScaleType = 1
eAVEncMPVQScaleType_NonLinear: eAVEncMPVQScaleType = 2
eAVEncMPVScanPattern = Int32
eAVEncMPVScanPattern_Auto: eAVEncMPVScanPattern = 0
eAVEncMPVScanPattern_ZigZagScan: eAVEncMPVScanPattern = 1
eAVEncMPVScanPattern_AlternateScan: eAVEncMPVScanPattern = 2
eAVEncMPVSceneDetection = Int32
eAVEncMPVSceneDetection_None: eAVEncMPVSceneDetection = 0
eAVEncMPVSceneDetection_InsertIPicture: eAVEncMPVSceneDetection = 1
eAVEncMPVSceneDetection_StartNewGOP: eAVEncMPVSceneDetection = 2
eAVEncMPVSceneDetection_StartNewLocatableGOP: eAVEncMPVSceneDetection = 3
eAVEncMuxOutput = Int32
eAVEncMuxOutput_eAVEncMuxOutputAuto: eAVEncMuxOutput = 0
eAVEncMuxOutput_eAVEncMuxOutputPS: eAVEncMuxOutput = 1
eAVEncMuxOutput_eAVEncMuxOutputTS: eAVEncMuxOutput = 2
eAVEncVP9VProfile = Int32
eAVEncVP9VProfile_unknown: eAVEncVP9VProfile = 0
eAVEncVP9VProfile_420_8: eAVEncVP9VProfile = 1
eAVEncVP9VProfile_420_10: eAVEncVP9VProfile = 2
eAVEncVP9VProfile_420_12: eAVEncVP9VProfile = 3
eAVEncVideoChromaResolution = Int32
eAVEncVideoChromaResolution_SameAsSource: eAVEncVideoChromaResolution = 0
eAVEncVideoChromaResolution_444: eAVEncVideoChromaResolution = 1
eAVEncVideoChromaResolution_422: eAVEncVideoChromaResolution = 2
eAVEncVideoChromaResolution_420: eAVEncVideoChromaResolution = 3
eAVEncVideoChromaResolution_411: eAVEncVideoChromaResolution = 4
eAVEncVideoChromaSubsampling = Int32
eAVEncVideoChromaSubsamplingFormat_SameAsSource: eAVEncVideoChromaSubsampling = 0
eAVEncVideoChromaSubsamplingFormat_ProgressiveChroma: eAVEncVideoChromaSubsampling = 8
eAVEncVideoChromaSubsamplingFormat_Horizontally_Cosited: eAVEncVideoChromaSubsampling = 4
eAVEncVideoChromaSubsamplingFormat_Vertically_Cosited: eAVEncVideoChromaSubsampling = 2
eAVEncVideoChromaSubsamplingFormat_Vertically_AlignedChromaPlanes: eAVEncVideoChromaSubsampling = 1
eAVEncVideoColorLighting = Int32
eAVEncVideoColorLighting_SameAsSource: eAVEncVideoColorLighting = 0
eAVEncVideoColorLighting_Unknown: eAVEncVideoColorLighting = 1
eAVEncVideoColorLighting_Bright: eAVEncVideoColorLighting = 2
eAVEncVideoColorLighting_Office: eAVEncVideoColorLighting = 3
eAVEncVideoColorLighting_Dim: eAVEncVideoColorLighting = 4
eAVEncVideoColorLighting_Dark: eAVEncVideoColorLighting = 5
eAVEncVideoColorNominalRange = Int32
eAVEncVideoColorNominalRange_SameAsSource: eAVEncVideoColorNominalRange = 0
eAVEncVideoColorNominalRange_0_255: eAVEncVideoColorNominalRange = 1
eAVEncVideoColorNominalRange_16_235: eAVEncVideoColorNominalRange = 2
eAVEncVideoColorNominalRange_48_208: eAVEncVideoColorNominalRange = 3
eAVEncVideoColorPrimaries = Int32
eAVEncVideoColorPrimaries_SameAsSource: eAVEncVideoColorPrimaries = 0
eAVEncVideoColorPrimaries_Reserved: eAVEncVideoColorPrimaries = 1
eAVEncVideoColorPrimaries_BT709: eAVEncVideoColorPrimaries = 2
eAVEncVideoColorPrimaries_BT470_2_SysM: eAVEncVideoColorPrimaries = 3
eAVEncVideoColorPrimaries_BT470_2_SysBG: eAVEncVideoColorPrimaries = 4
eAVEncVideoColorPrimaries_SMPTE170M: eAVEncVideoColorPrimaries = 5
eAVEncVideoColorPrimaries_SMPTE240M: eAVEncVideoColorPrimaries = 6
eAVEncVideoColorPrimaries_EBU3231: eAVEncVideoColorPrimaries = 7
eAVEncVideoColorPrimaries_SMPTE_C: eAVEncVideoColorPrimaries = 8
eAVEncVideoColorTransferFunction = Int32
eAVEncVideoColorTransferFunction_SameAsSource: eAVEncVideoColorTransferFunction = 0
eAVEncVideoColorTransferFunction_10: eAVEncVideoColorTransferFunction = 1
eAVEncVideoColorTransferFunction_18: eAVEncVideoColorTransferFunction = 2
eAVEncVideoColorTransferFunction_20: eAVEncVideoColorTransferFunction = 3
eAVEncVideoColorTransferFunction_22: eAVEncVideoColorTransferFunction = 4
eAVEncVideoColorTransferFunction_22_709: eAVEncVideoColorTransferFunction = 5
eAVEncVideoColorTransferFunction_22_240M: eAVEncVideoColorTransferFunction = 6
eAVEncVideoColorTransferFunction_22_8bit_sRGB: eAVEncVideoColorTransferFunction = 7
eAVEncVideoColorTransferFunction_28: eAVEncVideoColorTransferFunction = 8
eAVEncVideoColorTransferMatrix = Int32
eAVEncVideoColorTransferMatrix_SameAsSource: eAVEncVideoColorTransferMatrix = 0
eAVEncVideoColorTransferMatrix_BT709: eAVEncVideoColorTransferMatrix = 1
eAVEncVideoColorTransferMatrix_BT601: eAVEncVideoColorTransferMatrix = 2
eAVEncVideoColorTransferMatrix_SMPTE240M: eAVEncVideoColorTransferMatrix = 3
eAVEncVideoContentType = Int32
eAVEncVideoContentType_Unknown: eAVEncVideoContentType = 0
eAVEncVideoContentType_FixedCameraAngle: eAVEncVideoContentType = 1
eAVEncVideoFilmContent = Int32
eAVEncVideoFilmContent_VideoOnly: eAVEncVideoFilmContent = 0
eAVEncVideoFilmContent_FilmOnly: eAVEncVideoFilmContent = 1
eAVEncVideoFilmContent_Mixed: eAVEncVideoFilmContent = 2
eAVEncVideoOutputFrameRateConversion = Int32
eAVEncVideoOutputFrameRateConversion_Disable: eAVEncVideoOutputFrameRateConversion = 0
eAVEncVideoOutputFrameRateConversion_Enable: eAVEncVideoOutputFrameRateConversion = 1
eAVEncVideoOutputFrameRateConversion_Alias: eAVEncVideoOutputFrameRateConversion = 2
eAVEncVideoOutputScanType = Int32
eAVEncVideoOutputScan_Progressive: eAVEncVideoOutputScanType = 0
eAVEncVideoOutputScan_Interlaced: eAVEncVideoOutputScanType = 1
eAVEncVideoOutputScan_SameAsInput: eAVEncVideoOutputScanType = 2
eAVEncVideoOutputScan_Automatic: eAVEncVideoOutputScanType = 3
eAVEncVideoSourceScanType = Int32
eAVEncVideoSourceScan_Automatic: eAVEncVideoSourceScanType = 0
eAVEncVideoSourceScan_Interlaced: eAVEncVideoSourceScanType = 1
eAVEncVideoSourceScan_Progressive: eAVEncVideoSourceScanType = 2
eAVFastDecodeMode = Int32
eAVFastDecodeMode_eVideoDecodeCompliant: eAVFastDecodeMode = 0
eAVFastDecodeMode_eVideoDecodeOptimalLF: eAVFastDecodeMode = 1
eAVFastDecodeMode_eVideoDecodeDisableLF: eAVFastDecodeMode = 2
eAVFastDecodeMode_eVideoDecodeFastest: eAVFastDecodeMode = 32
eAVScenarioInfo = Int32
eAVScenarioInfo_Unknown: eAVScenarioInfo = 0
eAVScenarioInfo_DisplayRemoting: eAVScenarioInfo = 1
eAVScenarioInfo_VideoConference: eAVScenarioInfo = 2
eAVScenarioInfo_Archive: eAVScenarioInfo = 3
eAVScenarioInfo_LiveStreaming: eAVScenarioInfo = 4
eAVScenarioInfo_CameraRecord: eAVScenarioInfo = 5
eAVScenarioInfo_DisplayRemotingWithFeatureMap: eAVScenarioInfo = 6
eVideoEncoderDisplayContentType = Int32
eVideoEncoderDisplayContent_Unknown: eVideoEncoderDisplayContentType = 0
eVideoEncoderDisplayContent_FullScreenVideo: eVideoEncoderDisplayContentType = 1
make_head(_module, 'AM_MEDIA_TYPE')
make_head(_module, 'ASF_FLAT_PICTURE')
make_head(_module, 'ASF_FLAT_SYNCHRONISED_LYRICS')
make_head(_module, 'ASF_INDEX_DESCRIPTOR')
make_head(_module, 'ASF_INDEX_IDENTIFIER')
make_head(_module, 'ASF_MUX_STATISTICS')
make_head(_module, 'AecQualityMetrics_Struct')
make_head(_module, 'DEVPKEY_DeviceInterface_IsVirtualCamera')
make_head(_module, 'DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable')
make_head(_module, 'DEVPKEY_DeviceInterface_VirtualCameraAssociatedCameras')
make_head(_module, 'CodecAPIEventData')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ARCHITECTURE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODER_HEAP_SIZE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODER_HEAP_SIZE1')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_FORMAT_COUNT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_HISTOGRAM')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILE_COUNT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_PROTECTED_RESOURCES')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_DECODE_SUPPORT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_HEAP_SIZE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_INPUT_FORMAT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_INTRA_REFRESH_MODE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_OUTPUT_RESOLUTION')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_OUTPUT_RESOLUTION_RATIOS_COUNT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_PROFILE_LEVEL')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_RATE_CONTROL_MODE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_RESOLUTION_SUPPORT_LIMITS')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_RESOURCE_REQUIREMENTS')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_ENCODER_SUPPORT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMANDS')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_COUNT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_PARAMETERS')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_PARAMETER_COUNT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_SIZE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_EXTENSION_COMMAND_SUPPORT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_FEATURE_AREA_SUPPORT')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR_PROTECTED_RESOURCES')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_MOTION_ESTIMATOR_SIZE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_PROCESSOR_SIZE')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_PROCESSOR_SIZE1')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_PROCESS_MAX_INPUT_STREAMS')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_PROCESS_PROTECTED_RESOURCES')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_PROCESS_REFERENCE_INFO')
make_head(_module, 'D3D12_FEATURE_DATA_VIDEO_PROCESS_SUPPORT')
make_head(_module, 'D3D12_QUERY_DATA_VIDEO_DECODE_STATISTICS')
make_head(_module, 'D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_INPUT')
make_head(_module, 'D3D12_RESOLVE_VIDEO_MOTION_VECTOR_HEAP_OUTPUT')
make_head(_module, 'D3D12_RESOURCE_COORDINATE')
make_head(_module, 'D3D12_VIDEO_DECODER_DESC')
make_head(_module, 'D3D12_VIDEO_DECODER_HEAP_DESC')
make_head(_module, 'D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM')
make_head(_module, 'D3D12_VIDEO_DECODE_CONFIGURATION')
make_head(_module, 'D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS1')
make_head(_module, 'D3D12_VIDEO_DECODE_FRAME_ARGUMENT')
make_head(_module, 'D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM')
make_head(_module, 'D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1')
make_head(_module, 'D3D12_VIDEO_DECODE_REFERENCE_FRAMES')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_H264')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_H264')
make_head(_module, 'D3D12_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_HEVC')
make_head(_module, 'D3D12_VIDEO_ENCODER_COMPRESSED_BITSTREAM')
make_head(_module, 'D3D12_VIDEO_ENCODER_DESC')
make_head(_module, 'D3D12_VIDEO_ENCODER_ENCODEFRAME_INPUT_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_ENCODER_ENCODEFRAME_OUTPUT_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_ENCODER_ENCODE_OPERATION_METADATA_BUFFER')
make_head(_module, 'D3D12_VIDEO_ENCODER_FRAME_SUBREGION_METADATA')
make_head(_module, 'D3D12_VIDEO_ENCODER_HEAP_DESC')
make_head(_module, 'D3D12_VIDEO_ENCODER_INTRA_REFRESH')
make_head(_module, 'D3D12_VIDEO_ENCODER_LEVEL_SETTING')
make_head(_module, 'D3D12_VIDEO_ENCODER_LEVEL_TIER_CONSTRAINTS_HEVC')
make_head(_module, 'D3D12_VIDEO_ENCODER_OUTPUT_METADATA')
make_head(_module, 'D3D12_VIDEO_ENCODER_OUTPUT_METADATA_STATISTICS')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_LIST_MODIFICATION_OPERATION')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_MARKING_OPERATION')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_DESC')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_SLICES')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC')
make_head(_module, 'D3D12_VIDEO_ENCODER_PICTURE_RESOLUTION_RATIO_DESC')
make_head(_module, 'D3D12_VIDEO_ENCODER_PROFILE_DESC')
make_head(_module, 'D3D12_VIDEO_ENCODER_RATE_CONTROL')
make_head(_module, 'D3D12_VIDEO_ENCODER_RATE_CONTROL_CBR')
make_head(_module, 'D3D12_VIDEO_ENCODER_RATE_CONTROL_CONFIGURATION_PARAMS')
make_head(_module, 'D3D12_VIDEO_ENCODER_RATE_CONTROL_CQP')
make_head(_module, 'D3D12_VIDEO_ENCODER_RATE_CONTROL_QVBR')
make_head(_module, 'D3D12_VIDEO_ENCODER_RATE_CONTROL_VBR')
make_head(_module, 'D3D12_VIDEO_ENCODER_RECONSTRUCTED_PICTURE')
make_head(_module, 'D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_H264')
make_head(_module, 'D3D12_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_HEVC')
make_head(_module, 'D3D12_VIDEO_ENCODER_RESOLVE_METADATA_INPUT_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_ENCODER_RESOLVE_METADATA_OUTPUT_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_ENCODER_SEQUENCE_CONTROL_DESC')
make_head(_module, 'D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE')
make_head(_module, 'D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_H264')
make_head(_module, 'D3D12_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_HEVC')
make_head(_module, 'D3D12_VIDEO_ENCODE_REFERENCE_FRAMES')
make_head(_module, 'D3D12_VIDEO_EXTENSION_COMMAND_DESC')
make_head(_module, 'D3D12_VIDEO_EXTENSION_COMMAND_INFO')
make_head(_module, 'D3D12_VIDEO_EXTENSION_COMMAND_PARAMETER_INFO')
make_head(_module, 'D3D12_VIDEO_FORMAT')
make_head(_module, 'D3D12_VIDEO_MOTION_ESTIMATOR_DESC')
make_head(_module, 'D3D12_VIDEO_MOTION_ESTIMATOR_INPUT')
make_head(_module, 'D3D12_VIDEO_MOTION_ESTIMATOR_OUTPUT')
make_head(_module, 'D3D12_VIDEO_MOTION_VECTOR_HEAP_DESC')
make_head(_module, 'D3D12_VIDEO_PROCESS_ALPHA_BLENDING')
make_head(_module, 'D3D12_VIDEO_PROCESS_FILTER_RANGE')
make_head(_module, 'D3D12_VIDEO_PROCESS_INPUT_STREAM')
make_head(_module, 'D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS1')
make_head(_module, 'D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC')
make_head(_module, 'D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE')
make_head(_module, 'D3D12_VIDEO_PROCESS_LUMA_KEY')
make_head(_module, 'D3D12_VIDEO_PROCESS_OUTPUT_STREAM')
make_head(_module, 'D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS')
make_head(_module, 'D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC')
make_head(_module, 'D3D12_VIDEO_PROCESS_REFERENCE_SET')
make_head(_module, 'D3D12_VIDEO_PROCESS_TRANSFORM')
make_head(_module, 'D3D12_VIDEO_SAMPLE')
make_head(_module, 'D3D12_VIDEO_SCALE_SUPPORT')
make_head(_module, 'D3D12_VIDEO_SIZE_RANGE')
if ARCH in 'X64,ARM64':
    make_head(_module, 'D3DCONTENTPROTECTIONCAPS')
if ARCH in 'X86':
    make_head(_module, 'D3DCONTENTPROTECTIONCAPS')
make_head(_module, 'D3DOVERLAYCAPS')
make_head(_module, 'DEVICE_INFO')
make_head(_module, 'DIRTYRECT_INFO')
make_head(_module, 'DXVA2_AES_CTR_IV')
make_head(_module, 'DXVA2_AYUVSample16')
make_head(_module, 'DXVA2_AYUVSample8')
make_head(_module, 'DXVA2_ConfigPictureDecode')
make_head(_module, 'DXVA2_DecodeBufferDesc')
make_head(_module, 'DXVA2_DecodeExecuteParams')
make_head(_module, 'DXVA2_DecodeExtensionData')
make_head(_module, 'DXVA2_ExtendedFormat')
make_head(_module, 'DXVA2_FilterValues')
make_head(_module, 'DXVA2_Fixed32')
make_head(_module, 'DXVA2_Frequency')
make_head(_module, 'DXVA2_ProcAmpValues')
make_head(_module, 'DXVA2_ValueRange')
make_head(_module, 'DXVA2_VideoDesc')
make_head(_module, 'DXVA2_VideoProcessBltParams')
make_head(_module, 'DXVA2_VideoProcessorCaps')
make_head(_module, 'DXVA2_VideoSample')
make_head(_module, 'DXVABufferInfo')
make_head(_module, 'DXVACompBufferInfo')
make_head(_module, 'DXVAHDETW_CREATEVIDEOPROCESSOR')
make_head(_module, 'DXVAHDETW_DESTROYVIDEOPROCESSOR')
make_head(_module, 'DXVAHDETW_VIDEOPROCESSBLTHD')
make_head(_module, 'DXVAHDETW_VIDEOPROCESSBLTHD_STREAM')
make_head(_module, 'DXVAHDETW_VIDEOPROCESSBLTSTATE')
make_head(_module, 'DXVAHDETW_VIDEOPROCESSSTREAMSTATE')
make_head(_module, 'DXVAHDSW_CALLBACKS')
make_head(_module, 'DXVAHD_BLT_STATE_ALPHA_FILL_DATA')
make_head(_module, 'DXVAHD_BLT_STATE_BACKGROUND_COLOR_DATA')
make_head(_module, 'DXVAHD_BLT_STATE_CONSTRICTION_DATA')
make_head(_module, 'DXVAHD_BLT_STATE_OUTPUT_COLOR_SPACE_DATA')
make_head(_module, 'DXVAHD_BLT_STATE_PRIVATE_DATA')
make_head(_module, 'DXVAHD_BLT_STATE_TARGET_RECT_DATA')
make_head(_module, 'DXVAHD_COLOR')
make_head(_module, 'DXVAHD_COLOR_RGBA')
make_head(_module, 'DXVAHD_COLOR_YCbCrA')
make_head(_module, 'DXVAHD_CONTENT_DESC')
make_head(_module, 'DXVAHD_CUSTOM_RATE_DATA')
make_head(_module, 'DXVAHD_FILTER_RANGE_DATA')
make_head(_module, 'DXVAHD_RATIONAL')
make_head(_module, 'DXVAHD_STREAM_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_ALPHA_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_ASPECT_RATIO_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_D3DFORMAT_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_DESTINATION_RECT_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_FILTER_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_FRAME_FORMAT_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_INPUT_COLOR_SPACE_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_LUMA_KEY_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_OUTPUT_RATE_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_PALETTE_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_PRIVATE_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_PRIVATE_IVTC_DATA')
make_head(_module, 'DXVAHD_STREAM_STATE_SOURCE_RECT_DATA')
make_head(_module, 'DXVAHD_VPCAPS')
make_head(_module, 'DXVAHD_VPDEVCAPS')
make_head(_module, 'DXVAUncompDataInfo')
make_head(_module, 'DXVA_AYUVsample2')
make_head(_module, 'DXVA_BufferDescription')
make_head(_module, 'DXVA_COPPCommand')
make_head(_module, 'DXVA_COPPSignature')
make_head(_module, 'DXVA_COPPStatusInput')
make_head(_module, 'DXVA_COPPStatusOutput')
make_head(_module, 'DXVA_ConfigPictureDecode')
make_head(_module, 'DXVA_DeinterlaceBlt')
make_head(_module, 'DXVA_DeinterlaceBltEx')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DXVA_DeinterlaceBltEx32')
make_head(_module, 'DXVA_DeinterlaceCaps')
make_head(_module, 'DXVA_DeinterlaceQueryAvailableModes')
make_head(_module, 'DXVA_DeinterlaceQueryModeCaps')
make_head(_module, 'DXVA_ExtendedFormat')
make_head(_module, 'DXVA_Frequency')
make_head(_module, 'DXVA_PictureParameters')
make_head(_module, 'DXVA_ProcAmpControlBlt')
make_head(_module, 'DXVA_ProcAmpControlCaps')
make_head(_module, 'DXVA_ProcAmpControlQueryRange')
make_head(_module, 'DXVA_VideoDesc')
make_head(_module, 'DXVA_VideoPropertyRange')
make_head(_module, 'DXVA_VideoSample')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DXVA_VideoSample2')
if ARCH in 'X86':
    make_head(_module, 'DXVA_VideoSample2')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DXVA_VideoSample32')
make_head(_module, 'DigitalWindowSetting')
make_head(_module, 'IAdvancedMediaCapture')
make_head(_module, 'IAdvancedMediaCaptureInitializationSettings')
make_head(_module, 'IAdvancedMediaCaptureSettings')
make_head(_module, 'IAudioSourceProvider')
make_head(_module, 'IClusterDetector')
make_head(_module, 'ICodecAPI')
make_head(_module, 'ID3D12VideoDecodeCommandList')
make_head(_module, 'ID3D12VideoDecodeCommandList1')
make_head(_module, 'ID3D12VideoDecodeCommandList2')
make_head(_module, 'ID3D12VideoDecodeCommandList3')
make_head(_module, 'ID3D12VideoDecoder')
make_head(_module, 'ID3D12VideoDecoder1')
make_head(_module, 'ID3D12VideoDecoderHeap')
make_head(_module, 'ID3D12VideoDecoderHeap1')
make_head(_module, 'ID3D12VideoDevice')
make_head(_module, 'ID3D12VideoDevice1')
make_head(_module, 'ID3D12VideoDevice2')
make_head(_module, 'ID3D12VideoDevice3')
make_head(_module, 'ID3D12VideoEncodeCommandList')
make_head(_module, 'ID3D12VideoEncodeCommandList1')
make_head(_module, 'ID3D12VideoEncodeCommandList2')
make_head(_module, 'ID3D12VideoEncodeCommandList3')
make_head(_module, 'ID3D12VideoEncoder')
make_head(_module, 'ID3D12VideoEncoderHeap')
make_head(_module, 'ID3D12VideoExtensionCommand')
make_head(_module, 'ID3D12VideoMotionEstimator')
make_head(_module, 'ID3D12VideoMotionVectorHeap')
make_head(_module, 'ID3D12VideoProcessCommandList')
make_head(_module, 'ID3D12VideoProcessCommandList1')
make_head(_module, 'ID3D12VideoProcessCommandList2')
make_head(_module, 'ID3D12VideoProcessCommandList3')
make_head(_module, 'ID3D12VideoProcessor')
make_head(_module, 'ID3D12VideoProcessor1')
make_head(_module, 'IDXVAHD_Device')
make_head(_module, 'IDXVAHD_VideoProcessor')
make_head(_module, 'IDirect3D9ExOverlayExtension')
make_head(_module, 'IDirect3DAuthenticatedChannel9')
make_head(_module, 'IDirect3DCryptoSession9')
make_head(_module, 'IDirect3DDevice9Video')
make_head(_module, 'IDirect3DDeviceManager9')
make_head(_module, 'IDirectXVideoAccelerationService')
make_head(_module, 'IDirectXVideoDecoder')
make_head(_module, 'IDirectXVideoDecoderService')
make_head(_module, 'IDirectXVideoMemoryConfiguration')
make_head(_module, 'IDirectXVideoProcessor')
make_head(_module, 'IDirectXVideoProcessorService')
make_head(_module, 'IEVRFilterConfig')
make_head(_module, 'IEVRFilterConfigEx')
make_head(_module, 'IEVRTrustedVideoPlugin')
make_head(_module, 'IEVRVideoStreamControl')
make_head(_module, 'IFileClient')
make_head(_module, 'IFileIo')
make_head(_module, 'IMF2DBuffer')
make_head(_module, 'IMF2DBuffer2')
make_head(_module, 'IMFASFContentInfo')
make_head(_module, 'IMFASFIndexer')
make_head(_module, 'IMFASFMultiplexer')
make_head(_module, 'IMFASFMutualExclusion')
make_head(_module, 'IMFASFProfile')
make_head(_module, 'IMFASFSplitter')
make_head(_module, 'IMFASFStreamConfig')
make_head(_module, 'IMFASFStreamPrioritization')
make_head(_module, 'IMFASFStreamSelector')
make_head(_module, 'IMFActivate')
make_head(_module, 'IMFAsyncCallback')
make_head(_module, 'IMFAsyncCallbackLogging')
make_head(_module, 'IMFAsyncResult')
make_head(_module, 'IMFAttributes')
make_head(_module, 'IMFAudioMediaType')
make_head(_module, 'IMFAudioPolicy')
make_head(_module, 'IMFAudioStreamVolume')
make_head(_module, 'IMFBufferListNotify')
make_head(_module, 'IMFByteStream')
make_head(_module, 'IMFByteStreamBuffering')
make_head(_module, 'IMFByteStreamCacheControl')
make_head(_module, 'IMFByteStreamCacheControl2')
make_head(_module, 'IMFByteStreamHandler')
make_head(_module, 'IMFByteStreamProxyClassFactory')
make_head(_module, 'IMFByteStreamTimeSeek')
make_head(_module, 'IMFCameraConfigurationManager')
make_head(_module, 'IMFCameraControlDefaults')
make_head(_module, 'IMFCameraControlDefaultsCollection')
make_head(_module, 'IMFCameraControlMonitor')
make_head(_module, 'IMFCameraControlNotify')
make_head(_module, 'IMFCameraOcclusionStateMonitor')
make_head(_module, 'IMFCameraOcclusionStateReport')
make_head(_module, 'IMFCameraOcclusionStateReportCallback')
make_head(_module, 'IMFCameraSyncObject')
make_head(_module, 'IMFCaptureEngine')
make_head(_module, 'IMFCaptureEngineClassFactory')
make_head(_module, 'IMFCaptureEngineOnEventCallback')
make_head(_module, 'IMFCaptureEngineOnSampleCallback')
make_head(_module, 'IMFCaptureEngineOnSampleCallback2')
make_head(_module, 'IMFCapturePhotoConfirmation')
make_head(_module, 'IMFCapturePhotoSink')
make_head(_module, 'IMFCapturePreviewSink')
make_head(_module, 'IMFCaptureRecordSink')
make_head(_module, 'IMFCaptureSink')
make_head(_module, 'IMFCaptureSink2')
make_head(_module, 'IMFCaptureSource')
make_head(_module, 'IMFCdmSuspendNotify')
make_head(_module, 'IMFClock')
make_head(_module, 'IMFClockConsumer')
make_head(_module, 'IMFClockStateSink')
make_head(_module, 'IMFCollection')
make_head(_module, 'IMFContentDecryptionModule')
make_head(_module, 'IMFContentDecryptionModuleAccess')
make_head(_module, 'IMFContentDecryptionModuleFactory')
make_head(_module, 'IMFContentDecryptionModuleSession')
make_head(_module, 'IMFContentDecryptionModuleSessionCallbacks')
make_head(_module, 'IMFContentDecryptorContext')
make_head(_module, 'IMFContentEnabler')
make_head(_module, 'IMFContentProtectionDevice')
make_head(_module, 'IMFContentProtectionManager')
make_head(_module, 'IMFD3D12SynchronizationObject')
make_head(_module, 'IMFD3D12SynchronizationObjectCommands')
make_head(_module, 'IMFDLNASinkInit')
make_head(_module, 'IMFDRMNetHelper')
make_head(_module, 'IMFDXGIBuffer')
make_head(_module, 'IMFDXGIDeviceManager')
make_head(_module, 'IMFDXGIDeviceManagerSource')
make_head(_module, 'IMFDesiredSample')
make_head(_module, 'IMFDeviceTransform')
make_head(_module, 'IMFDeviceTransformCallback')
make_head(_module, 'IMFExtendedCameraControl')
make_head(_module, 'IMFExtendedCameraController')
make_head(_module, 'IMFExtendedCameraIntrinsicModel')
make_head(_module, 'IMFExtendedCameraIntrinsics')
make_head(_module, 'IMFExtendedCameraIntrinsicsDistortionModel6KT')
make_head(_module, 'IMFExtendedCameraIntrinsicsDistortionModelArcTan')
make_head(_module, 'IMFExtendedDRMTypeSupport')
make_head(_module, 'IMFFieldOfUseMFTUnlock')
make_head(_module, 'IMFFinalizableMediaSink')
make_head(_module, 'IMFGetService')
make_head(_module, 'IMFHDCPStatus')
make_head(_module, 'IMFHttpDownloadRequest')
make_head(_module, 'IMFHttpDownloadSession')
make_head(_module, 'IMFHttpDownloadSessionProvider')
make_head(_module, 'IMFImageSharingEngine')
make_head(_module, 'IMFImageSharingEngineClassFactory')
make_head(_module, 'IMFInputTrustAuthority')
make_head(_module, 'IMFLocalMFTRegistration')
make_head(_module, 'IMFMediaBuffer')
make_head(_module, 'IMFMediaEngine')
make_head(_module, 'IMFMediaEngineAudioEndpointId')
make_head(_module, 'IMFMediaEngineClassFactory')
make_head(_module, 'IMFMediaEngineClassFactory2')
make_head(_module, 'IMFMediaEngineClassFactory3')
make_head(_module, 'IMFMediaEngineClassFactory4')
make_head(_module, 'IMFMediaEngineClassFactoryEx')
make_head(_module, 'IMFMediaEngineEME')
make_head(_module, 'IMFMediaEngineEMENotify')
make_head(_module, 'IMFMediaEngineEx')
make_head(_module, 'IMFMediaEngineExtension')
make_head(_module, 'IMFMediaEngineNeedKeyNotify')
make_head(_module, 'IMFMediaEngineNotify')
make_head(_module, 'IMFMediaEngineOPMInfo')
make_head(_module, 'IMFMediaEngineProtectedContent')
make_head(_module, 'IMFMediaEngineSrcElements')
make_head(_module, 'IMFMediaEngineSrcElementsEx')
make_head(_module, 'IMFMediaEngineSupportsSourceTransfer')
make_head(_module, 'IMFMediaEngineTransferSource')
make_head(_module, 'IMFMediaEngineWebSupport')
make_head(_module, 'IMFMediaError')
make_head(_module, 'IMFMediaEvent')
make_head(_module, 'IMFMediaEventGenerator')
make_head(_module, 'IMFMediaEventQueue')
make_head(_module, 'IMFMediaKeySession')
make_head(_module, 'IMFMediaKeySession2')
make_head(_module, 'IMFMediaKeySessionNotify')
make_head(_module, 'IMFMediaKeySessionNotify2')
make_head(_module, 'IMFMediaKeySystemAccess')
make_head(_module, 'IMFMediaKeys')
make_head(_module, 'IMFMediaKeys2')
make_head(_module, 'IMFMediaSession')
make_head(_module, 'IMFMediaSharingEngine')
make_head(_module, 'IMFMediaSharingEngineClassFactory')
make_head(_module, 'IMFMediaSink')
make_head(_module, 'IMFMediaSinkPreroll')
make_head(_module, 'IMFMediaSource')
make_head(_module, 'IMFMediaSource2')
make_head(_module, 'IMFMediaSourceEx')
make_head(_module, 'IMFMediaSourceExtension')
make_head(_module, 'IMFMediaSourceExtensionLiveSeekableRange')
make_head(_module, 'IMFMediaSourceExtensionNotify')
make_head(_module, 'IMFMediaSourcePresentationProvider')
make_head(_module, 'IMFMediaSourceTopologyProvider')
make_head(_module, 'IMFMediaStream')
make_head(_module, 'IMFMediaStream2')
make_head(_module, 'IMFMediaStreamSourceSampleRequest')
make_head(_module, 'IMFMediaTimeRange')
make_head(_module, 'IMFMediaType')
make_head(_module, 'IMFMediaTypeHandler')
make_head(_module, 'IMFMetadata')
make_head(_module, 'IMFMetadataProvider')
make_head(_module, 'IMFMuxStreamAttributesManager')
make_head(_module, 'IMFMuxStreamMediaTypeManager')
make_head(_module, 'IMFMuxStreamSampleManager')
make_head(_module, 'IMFNetCredential')
make_head(_module, 'IMFNetCredentialCache')
make_head(_module, 'IMFNetCredentialManager')
make_head(_module, 'IMFNetCrossOriginSupport')
make_head(_module, 'IMFNetProxyLocator')
make_head(_module, 'IMFNetProxyLocatorFactory')
make_head(_module, 'IMFNetResourceFilter')
make_head(_module, 'IMFNetSchemeHandlerConfig')
make_head(_module, 'IMFObjectReferenceStream')
make_head(_module, 'IMFOutputPolicy')
make_head(_module, 'IMFOutputSchema')
make_head(_module, 'IMFOutputTrustAuthority')
make_head(_module, 'IMFPMPClient')
make_head(_module, 'IMFPMPClientApp')
make_head(_module, 'IMFPMPHost')
make_head(_module, 'IMFPMPHostApp')
make_head(_module, 'IMFPMPServer')
make_head(_module, 'IMFPMediaItem')
make_head(_module, 'IMFPMediaPlayer')
make_head(_module, 'IMFPMediaPlayerCallback')
make_head(_module, 'IMFPluginControl')
make_head(_module, 'IMFPluginControl2')
make_head(_module, 'IMFPresentationClock')
make_head(_module, 'IMFPresentationDescriptor')
make_head(_module, 'IMFPresentationTimeSource')
make_head(_module, 'IMFProtectedEnvironmentAccess')
make_head(_module, 'IMFQualityAdvise')
make_head(_module, 'IMFQualityAdvise2')
make_head(_module, 'IMFQualityAdviseLimits')
make_head(_module, 'IMFQualityManager')
make_head(_module, 'IMFRateControl')
make_head(_module, 'IMFRateSupport')
make_head(_module, 'IMFReadWriteClassFactory')
make_head(_module, 'IMFRealTimeClient')
make_head(_module, 'IMFRealTimeClientEx')
make_head(_module, 'IMFRelativePanelReport')
make_head(_module, 'IMFRelativePanelWatcher')
make_head(_module, 'IMFRemoteAsyncCallback')
make_head(_module, 'IMFRemoteDesktopPlugin')
make_head(_module, 'IMFRemoteProxy')
make_head(_module, 'IMFSAMIStyle')
make_head(_module, 'IMFSSLCertificateManager')
make_head(_module, 'IMFSample')
make_head(_module, 'IMFSampleAllocatorControl')
make_head(_module, 'IMFSampleGrabberSinkCallback')
make_head(_module, 'IMFSampleGrabberSinkCallback2')
make_head(_module, 'IMFSampleOutputStream')
make_head(_module, 'IMFSampleProtection')
make_head(_module, 'IMFSaveJob')
make_head(_module, 'IMFSchemeHandler')
make_head(_module, 'IMFSecureBuffer')
make_head(_module, 'IMFSecureChannel')
make_head(_module, 'IMFSeekInfo')
make_head(_module, 'IMFSensorActivitiesReport')
make_head(_module, 'IMFSensorActivitiesReportCallback')
make_head(_module, 'IMFSensorActivityMonitor')
make_head(_module, 'IMFSensorActivityReport')
make_head(_module, 'IMFSensorDevice')
make_head(_module, 'IMFSensorGroup')
make_head(_module, 'IMFSensorProcessActivity')
make_head(_module, 'IMFSensorProfile')
make_head(_module, 'IMFSensorProfileCollection')
make_head(_module, 'IMFSensorStream')
make_head(_module, 'IMFSensorTransformFactory')
make_head(_module, 'IMFSequencerSource')
make_head(_module, 'IMFSharingEngineClassFactory')
make_head(_module, 'IMFShutdown')
make_head(_module, 'IMFSignedLibrary')
make_head(_module, 'IMFSimpleAudioVolume')
make_head(_module, 'IMFSinkWriter')
make_head(_module, 'IMFSinkWriterCallback')
make_head(_module, 'IMFSinkWriterCallback2')
make_head(_module, 'IMFSinkWriterEncoderConfig')
make_head(_module, 'IMFSinkWriterEx')
make_head(_module, 'IMFSourceBuffer')
make_head(_module, 'IMFSourceBufferAppendMode')
make_head(_module, 'IMFSourceBufferList')
make_head(_module, 'IMFSourceBufferNotify')
make_head(_module, 'IMFSourceOpenMonitor')
make_head(_module, 'IMFSourceReader')
make_head(_module, 'IMFSourceReaderCallback')
make_head(_module, 'IMFSourceReaderCallback2')
make_head(_module, 'IMFSourceReaderEx')
make_head(_module, 'IMFSourceResolver')
make_head(_module, 'IMFSpatialAudioObjectBuffer')
make_head(_module, 'IMFSpatialAudioSample')
make_head(_module, 'IMFStreamDescriptor')
make_head(_module, 'IMFStreamSink')
make_head(_module, 'IMFStreamingSinkConfig')
make_head(_module, 'IMFSystemId')
make_head(_module, 'IMFTimecodeTranslate')
make_head(_module, 'IMFTimedText')
make_head(_module, 'IMFTimedTextBinary')
make_head(_module, 'IMFTimedTextBouten')
make_head(_module, 'IMFTimedTextCue')
make_head(_module, 'IMFTimedTextCueList')
make_head(_module, 'IMFTimedTextFormattedText')
make_head(_module, 'IMFTimedTextNotify')
make_head(_module, 'IMFTimedTextRegion')
make_head(_module, 'IMFTimedTextRuby')
make_head(_module, 'IMFTimedTextStyle')
make_head(_module, 'IMFTimedTextStyle2')
make_head(_module, 'IMFTimedTextTrack')
make_head(_module, 'IMFTimedTextTrackList')
make_head(_module, 'IMFTimer')
make_head(_module, 'IMFTopoLoader')
make_head(_module, 'IMFTopology')
make_head(_module, 'IMFTopologyNode')
make_head(_module, 'IMFTopologyNodeAttributeEditor')
make_head(_module, 'IMFTopologyServiceLookup')
make_head(_module, 'IMFTopologyServiceLookupClient')
make_head(_module, 'IMFTrackedSample')
make_head(_module, 'IMFTranscodeProfile')
make_head(_module, 'IMFTranscodeSinkInfoProvider')
make_head(_module, 'IMFTransform')
make_head(_module, 'IMFTrustedInput')
make_head(_module, 'IMFTrustedOutput')
make_head(_module, 'IMFVideoCaptureSampleAllocator')
make_head(_module, 'IMFVideoDeviceID')
make_head(_module, 'IMFVideoDisplayControl')
make_head(_module, 'IMFVideoMediaType')
make_head(_module, 'IMFVideoMixerBitmap')
make_head(_module, 'IMFVideoMixerControl')
make_head(_module, 'IMFVideoMixerControl2')
make_head(_module, 'IMFVideoPositionMapper')
make_head(_module, 'IMFVideoPresenter')
make_head(_module, 'IMFVideoProcessor')
make_head(_module, 'IMFVideoProcessorControl')
make_head(_module, 'IMFVideoProcessorControl2')
make_head(_module, 'IMFVideoProcessorControl3')
make_head(_module, 'IMFVideoRenderer')
make_head(_module, 'IMFVideoRendererEffectControl')
make_head(_module, 'IMFVideoSampleAllocator')
make_head(_module, 'IMFVideoSampleAllocatorCallback')
make_head(_module, 'IMFVideoSampleAllocatorEx')
make_head(_module, 'IMFVideoSampleAllocatorNotify')
make_head(_module, 'IMFVideoSampleAllocatorNotifyEx')
make_head(_module, 'IMFVirtualCamera')
make_head(_module, 'IMFWorkQueueServices')
make_head(_module, 'IMFWorkQueueServicesEx')
make_head(_module, 'IOPMVideoOutput')
make_head(_module, 'IPlayToControl')
make_head(_module, 'IPlayToControlWithCapabilities')
make_head(_module, 'IPlayToSourceClassFactory')
make_head(_module, 'IToc')
make_head(_module, 'ITocCollection')
make_head(_module, 'ITocEntry')
make_head(_module, 'ITocEntryList')
make_head(_module, 'ITocParser')
make_head(_module, 'IValidateBinding')
make_head(_module, 'IWMCodecLeakyBucket')
make_head(_module, 'IWMCodecOutputTimestamp')
make_head(_module, 'IWMCodecPrivateData')
make_head(_module, 'IWMCodecProps')
make_head(_module, 'IWMCodecStrings')
make_head(_module, 'IWMColorConvProps')
make_head(_module, 'IWMColorLegalizerProps')
make_head(_module, 'IWMFrameInterpProps')
make_head(_module, 'IWMInterlaceProps')
make_head(_module, 'IWMResamplerProps')
make_head(_module, 'IWMResizerProps')
make_head(_module, 'IWMSampleExtensionSupport')
make_head(_module, 'IWMValidate')
make_head(_module, 'IWMVideoDecoderHurryup')
make_head(_module, 'IWMVideoDecoderReconBuffer')
make_head(_module, 'IWMVideoForceKeyFrame')
make_head(_module, 'MACROBLOCK_DATA')
make_head(_module, 'MFARGB')
make_head(_module, 'MFASYNCRESULT')
make_head(_module, 'MFAYUVSample')
make_head(_module, 'MFAudioDecoderDegradationInfo')
make_head(_module, 'MFBYTESTREAM_BUFFERING_PARAMS')
make_head(_module, 'MFCLOCK_PROPERTIES')
make_head(_module, 'MFCONTENTPROTECTIONDEVICE_INPUT_DATA')
make_head(_module, 'MFCONTENTPROTECTIONDEVICE_OUTPUT_DATA')
make_head(_module, 'MFCONTENTPROTECTIONDEVICE_REALTIMECLIENT_DATA')
make_head(_module, 'MFCameraExtrinsic_CalibratedTransform')
make_head(_module, 'MFCameraExtrinsics')
make_head(_module, 'MFCameraIntrinsic_CameraModel')
make_head(_module, 'MFCameraIntrinsic_DistortionModel')
make_head(_module, 'MFCameraIntrinsic_DistortionModel6KT')
make_head(_module, 'MFCameraIntrinsic_DistortionModelArcTan')
make_head(_module, 'MFCameraIntrinsic_PinholeCameraModel')
make_head(_module, 'MFExtendedCameraIntrinsic_IntrinsicModel')
make_head(_module, 'MFFOLDDOWN_MATRIX')
make_head(_module, 'MFINPUTTRUSTAUTHORITY_ACCESS_ACTION')
make_head(_module, 'MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS')
make_head(_module, 'MFMPEG2DLNASINKSTATS')
make_head(_module, 'MFMediaKeyStatus')
make_head(_module, 'MFNetCredentialManagerGetParam')
make_head(_module, 'MFOffset')
make_head(_module, 'MFPERIODICCALLBACK')
make_head(_module, 'MFP_ACQUIRE_USER_CREDENTIAL_EVENT')
make_head(_module, 'MFP_ERROR_EVENT')
make_head(_module, 'MFP_EVENT_HEADER')
make_head(_module, 'MFP_FRAME_STEP_EVENT')
make_head(_module, 'MFP_MEDIAITEM_CLEARED_EVENT')
make_head(_module, 'MFP_MEDIAITEM_CREATED_EVENT')
make_head(_module, 'MFP_MEDIAITEM_SET_EVENT')
make_head(_module, 'MFP_MF_EVENT')
make_head(_module, 'MFP_PAUSE_EVENT')
make_head(_module, 'MFP_PLAYBACK_ENDED_EVENT')
make_head(_module, 'MFP_PLAY_EVENT')
make_head(_module, 'MFP_POSITION_SET_EVENT')
make_head(_module, 'MFP_RATE_SET_EVENT')
make_head(_module, 'MFP_STOP_EVENT')
make_head(_module, 'MFPaletteEntry')
make_head(_module, 'MFPinholeCameraIntrinsic_IntrinsicModel')
make_head(_module, 'MFPinholeCameraIntrinsics')
make_head(_module, 'MFRR_COMPONENTS')
make_head(_module, 'MFRR_COMPONENT_HASH_INFO')
make_head(_module, 'MFRatio')
make_head(_module, 'MFTOPONODE_ATTRIBUTE_UPDATE')
make_head(_module, 'MFT_INPUT_STREAM_INFO')
make_head(_module, 'MFT_OUTPUT_DATA_BUFFER')
make_head(_module, 'MFT_OUTPUT_STREAM_INFO')
make_head(_module, 'MFT_REGISTER_TYPE_INFO')
make_head(_module, 'MFT_REGISTRATION_INFO')
make_head(_module, 'MFT_STREAM_STATE_PARAM')
make_head(_module, 'MFVIDEOFORMAT')
make_head(_module, 'MFVideoAlphaBitmap')
make_head(_module, 'MFVideoAlphaBitmapParams')
make_head(_module, 'MFVideoArea')
make_head(_module, 'MFVideoCompressedInfo')
make_head(_module, 'MFVideoInfo')
make_head(_module, 'MFVideoNormalizedRect')
make_head(_module, 'MFVideoSurfaceInfo')
make_head(_module, 'MF_BYTE_STREAM_CACHE_RANGE')
make_head(_module, 'MF_CAMERA_CONTROL_RANGE_INFO')
make_head(_module, 'MF_FLOAT2')
make_head(_module, 'MF_FLOAT3')
make_head(_module, 'MF_LEAKY_BUCKET_PAIR')
make_head(_module, 'MF_QUATERNION')
make_head(_module, 'MF_SINK_WRITER_STATISTICS')
make_head(_module, 'MF_TRANSCODE_SINK_INFO')
make_head(_module, 'MF_VIDEO_SPHERICAL_VIEWDIRECTION')
make_head(_module, 'MOVEREGION_INFO')
make_head(_module, 'MOVE_RECT')
make_head(_module, 'MPEG1VIDEOINFO')
make_head(_module, 'MPEG2VIDEOINFO')
make_head(_module, 'MT_ARBITRARY_HEADER')
make_head(_module, 'MT_CUSTOM_VIDEO_PRIMARIES')
make_head(_module, 'OPM_ACP_AND_CGMSA_SIGNALING')
make_head(_module, 'OPM_ACTUAL_OUTPUT_FORMAT')
make_head(_module, 'OPM_CONFIGURE_PARAMETERS')
make_head(_module, 'OPM_CONNECTED_HDCP_DEVICE_INFORMATION')
make_head(_module, 'OPM_COPP_COMPATIBLE_GET_INFO_PARAMETERS')
make_head(_module, 'OPM_ENCRYPTED_INITIALIZATION_PARAMETERS')
make_head(_module, 'OPM_GET_CODEC_INFO_INFORMATION')
make_head(_module, 'OPM_GET_CODEC_INFO_PARAMETERS')
make_head(_module, 'OPM_GET_INFO_PARAMETERS')
make_head(_module, 'OPM_HDCP_KEY_SELECTION_VECTOR')
make_head(_module, 'OPM_OMAC')
make_head(_module, 'OPM_OUTPUT_ID_DATA')
make_head(_module, 'OPM_RANDOM_NUMBER')
make_head(_module, 'OPM_REQUESTED_INFORMATION')
make_head(_module, 'OPM_SET_ACP_AND_CGMSA_SIGNALING_PARAMETERS')
make_head(_module, 'OPM_SET_HDCP_SRM_PARAMETERS')
make_head(_module, 'OPM_SET_PROTECTION_LEVEL_PARAMETERS')
make_head(_module, 'OPM_STANDARD_INFORMATION')
make_head(_module, 'PDXVAHDSW_CreateDevice')
make_head(_module, 'PDXVAHDSW_CreateVideoProcessor')
make_head(_module, 'PDXVAHDSW_DestroyDevice')
make_head(_module, 'PDXVAHDSW_DestroyVideoProcessor')
make_head(_module, 'PDXVAHDSW_GetVideoProcessBltStatePrivate')
make_head(_module, 'PDXVAHDSW_GetVideoProcessStreamStatePrivate')
make_head(_module, 'PDXVAHDSW_GetVideoProcessorCaps')
make_head(_module, 'PDXVAHDSW_GetVideoProcessorCustomRates')
make_head(_module, 'PDXVAHDSW_GetVideoProcessorDeviceCaps')
make_head(_module, 'PDXVAHDSW_GetVideoProcessorFilterRange')
make_head(_module, 'PDXVAHDSW_GetVideoProcessorInputFormats')
make_head(_module, 'PDXVAHDSW_GetVideoProcessorOutputFormats')
make_head(_module, 'PDXVAHDSW_Plugin')
make_head(_module, 'PDXVAHDSW_ProposeVideoPrivateFormat')
make_head(_module, 'PDXVAHDSW_SetVideoProcessBltState')
make_head(_module, 'PDXVAHDSW_SetVideoProcessStreamState')
make_head(_module, 'PDXVAHDSW_VideoProcessBltHD')
make_head(_module, 'PDXVAHD_CreateDevice')
make_head(_module, 'ROI_AREA')
make_head(_module, 'SENSORPROFILEID')
make_head(_module, 'STREAM_MEDIUM')
make_head(_module, 'TOC_DESCRIPTOR')
make_head(_module, 'TOC_ENTRY_DESCRIPTOR')
make_head(_module, 'VIDEOINFOHEADER')
make_head(_module, 'VIDEOINFOHEADER2')
