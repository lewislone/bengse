# coding: UTF-8
#import controllers
import sys
from webpyueditor import Ue_ImageUp, Ue_FileUp, Ue_ScrawlUp, Ue_GetRemoteImage, Ue_GetMovie, Ue_ImageManager

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

pre_fix = 'controllers.'

urls = (
     '/',        pre_fix + 'main.Test',
    '/upload',   pre_fix + 'upload_file.UploadFile',
    '/new',  	 pre_fix +'main.New',
    '/imgs/(.*)',pre_fix + 'main.Imgs',
    '/ue_imageUp', Ue_ImageUp,
    '/ue_fileUp', Ue_FileUp,
    '/ue_scrawlUp', Ue_ScrawlUp,
    '/ue_getRemoteImage', Ue_GetRemoteImage,
    '/ue_getMovie', Ue_GetMovie,
    '/ue_imageManager', Ue_ImageManager,

#    '/(?:img|js|css)/.*', pre_fix + 'public.public',

)



