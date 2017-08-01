# coding: UTF-8
#import controllers

pre_fix = 'controllers.'

urls = (
     '/',        pre_fix + 'main.Test',
#    '/index',   'controllers.handle_templates.index',
    '/upload',   'controllers.upload_file.UploadFile',
#    '/recipients', 'controllers.preview_recipients.browse',
#    '/statics', 'controllers.handle_templates.statics',

#    '/(?:img|js|css)/.*', 'controllers.public.public',

)
