"""
Replies to user if image is shown
with species of leaf and confidence
"""

import plugins
import sys
sys.path.insert(0, 'D:\Krishna\DL\Deep-Leafsnap')
from chatbot_pred import predict_leaf

def _initialise(bot):
#    plugins.register_admin_command(["tellme"])
    plugins.register_handler(tellme, type="message", priority=50)


def tellme(bot, event, *args):
    """remember value for current user, memory must be empty.
    use /bot forgetme to clear previous storage
    """

    text = event.text
    pic_url = bot.call_shared('image_validate_link', text, reject_googleusercontent=False)
    if 'https://lh3.googleusercontent.com/' in text: #this is uploaded image
        pic_url = text+'.jpg'        
        yield from bot.coro_send_message(event.conv,'please wait, processing...')
        label, confidence = predict_leaf(pic_url)

        yield from bot.coro_send_message(
            event.conv,
            _("Species: <i><b>{}</b></i> \n Confidence: <b>{}</b>%").format(
                label,
                confidence))