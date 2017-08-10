# coding: UTF-8
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

pre_fix = 'controllers.'

urls = (
    '/',            pre_fix + 'main.Test',
    '/upload',      pre_fix + 'upload_file.UploadFile',
    '/new',  	    pre_fix + 'main.New',
    '/newbatch',    pre_fix + 'main.NewBatch',
    '/imgs/(.*)',   pre_fix + 'main.Imgs',
    '/ue_imageUp',  pre_fix + 'webpyueditor.Ue_ImageUp',
    '/ue_fileUp',   pre_fix + 'Ue_FileUp',
    '/ue_scrawlUp', pre_fix + 'webpyueditor.Ue_ScrawlUp',
    '/ue_getRemoteImage',   pre_fix + 'webpyueditor.Ue_GetRemoteImage',
    '/ue_getMovie',         pre_fix + 'webpyueditor.Ue_GetMovie',
    '/ue_imageManager',     pre_fix + 'webpyueditor.Ue_ImageManager',

#    '/(?:img|js|css)/.*', pre_fix + 'public.public',
)



