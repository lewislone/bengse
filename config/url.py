# coding: UTF-8
import sys
import webpyueditor
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

pre_fix = 'controllers.'
'''
urls = (
    '/',            pre_fix + 'main.Test',
    '/upload',      pre_fix + 'upload_file.UploadFile',
    '/new',  	    pre_fix + 'main.New',
    '/newbatch',    pre_fix + 'main.NewBatch',
    '/stop',        pre_fix + 'main.StopSend',
    '/imgs/(.*)',   pre_fix + 'main.Imgs',
    '/ue_imageUp',  pre_fix + 'webpyueditor.Ue_ImageUp',
    '/ue_fileUp',   pre_fix + 'webpyueditor.Ue_FileUp',
    '/ue_scrawlUp', pre_fix + 'webpyueditor.Ue_ScrawlUp',
    '/ue_getRemoteImage',   pre_fix + 'webpyueditor.Ue_GetRemoteImage',
    '/ue_getMovie',         pre_fix + 'webpyueditor.Ue_GetMovie',
    '/ue_imageManager',     pre_fix + 'webpyueditor.Ue_ImageManager',

#    '/(?:img|js|css)/.*', pre_fix + 'public.public',
)
'''
urls = (
    '/',            pre_fix + 'main.Show',
    '/upload',      pre_fix + 'upload_file.UploadFile',
    '/new',  	    pre_fix + 'main.New',
    '/newbatch',    pre_fix + 'main.NewBatch',
    '/stop',        pre_fix + 'main.StopSend',
    '/imgs/(.*)',   pre_fix + 'main.Imgs',
    '/ue_imageUp',  'webpyueditor.Ue_ImageUp',
    '/ue_fileUp',   'webpyueditor.Ue_FileUp',
    '/ue_scrawlUp', 'webpyueditor.Ue_ScrawlUp',
    '/ue_getRemoteImage',   'webpyueditor.Ue_GetRemoteImage',
    '/ue_getMovie',         'webpyueditor.Ue_GetMovie',
    '/ue_imageManager',     'webpyueditor.Ue_ImageManager',

#    '/(?:img|js|css)/.*', pre_fix + 'public.public',
)



