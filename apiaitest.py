#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai

CLIENT_ACCESS_TOKEN = '62d96cc2d6b347a2ac050a7afb1c0574'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:
        print(u"> ", end=u"")
        user_message = raw_input()

        if user_message == u"exit":
            break

        request = ai.text_request()
        request.query = user_message

        response = json.loads(request.getresponse().read())
        print (response)
        result = response['result']
        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)
        print("ACTION: " + str(action))
        print(u"< %s" % response['result']['fulfillment']['speech'])

        if action is not None:
            if action == u"send_message":
                parameters = result['parameters']

                text = parameters.get('text')
                message_type = parameters.get('message_type')
                parent = parameters.get('parent')

                print (
                    'text: %s, message_type: %s, parent: %s' %
                    (
                        text if text else "null",
                        message_type if message_type else "null",
                        parent if parent else "null"
                    )
                )

                if not actionIncomplete:
                    print(u"...Sending Message...")
                    break


if __name__ == '__main__':
    main()