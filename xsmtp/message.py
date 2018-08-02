#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from xsmtp.compat import text_type
from xsmtp.utils import raw, inline
from xsmtp.headers import add_subject, add_date
from xsmtp.headers import add_recipients_headers

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate




def prepare_message(user, useralias, addresses, subject, contents, attachments, encoding):

    """ Prepare a MIME message """
    if isinstance(contents, text_type):
        contents = [contents]

    if isinstance(attachments, text_type):
        attachments = [attachments]

    if attachments is not None:
        contents = attachments if contents is None else contents + attachments


    print('contents: {0}'.format(contents))
    has_included_images, content_objects = prepare_contents(contents, encoding)

    print('has_included_images={0}\ncontent_objects={1}'.format(has_included_images, content_objects))



    # mixed
    msg = MIMEMultipart()

    add_date(msg)

    add_subject(msg, subject)

    # 纯文本与超文本共存
    msg_alternative = MIMEMultipart("alternative")

    # 可以包含内嵌资源。
    msg_related = MIMEMultipart("related")
    msg_related.attach("-- HTML goes here --")


    msg.attach(msg_alternative)




    add_recipients_headers(user, useralias, msg, addresses)




    htmlstr = ""
    altstr = []


    if contents is not None:
        for content_object, content_string in zip(content_objects, contents):

            print('*****************t200:', content_object)
            if content_object["main_type"] == "image":
                pass
            else:
                if content_object["encoding"] == "base64":
                    email.encoders.encode_base64(content_object["mime_object"])
                    msg.attach(content_object["mime_object"])

                else:
                    content_string = content_string.replace("\n", "<br>")
                    try:
                        htmlstr += "<div>{0}</div>".format(content_string)
                    except UnicodeEncodeError:
                        htmlstr += u"<div>{0}</div>".format(content_string)
                    altstr.append(content_string)

    msg_related.get_payload()[0] = MIMEText(htmlstr, "html", _charset=encoding)
    msg_alternative.attach(MIMEText("\n".join(altstr), _charset=encoding))
    msg_alternative.attach(msg_related)

    return msg



def prepare_contents(contents, encoding):
    mime_objects = []
    has_included_images = False
    if contents is not None:
        for content in contents:
            content_object = get_mime_object(content, encoding)
            if content_object["main_type"] == "image":
                has_included_images = True

            mime_objects.append(content_object)

    return has_included_images, mime_objects


def get_mime_object(content_string, encoding):
    print("content_string = ", content_string, encoding)
    content_object = {"mime_object": None, "encoding": None, "main_type": None, "sub_type": None}

    if isinstance(content_string, dict):
        pass

        print('*************************t101:')
    else:
        # content_name = os.path.basename(str(content_string))

        try:
            content_name = os.path.basename(str(content_string))
        except UnicodeEncodeError:
            content_name = os.path.basename(content_string)



        print('*************************t102:', content_name)


    is_raw = type(content_string) == raw
    if not is_raw and os.path.isfile(content_string):
        pass

    else:
        print('*************************t102.1:', content_name)
        content_object["main_type"] = "text"

        if is_raw:
            content_object["mime_object"] = MIMEText(content_string, _charset=encoding)
        else:
            content_object["mime_object"] = MIMEText(content_string, "html", _charset=encoding)
            content_object["sub_type"] = "html"

        if content_object["sub_type"] is None:
            content_object["sub_type"] = "plain"
        return content_object

    print('*************************t103:', is_raw, type(content_string), type(raw))
    return content_object